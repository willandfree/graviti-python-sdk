#!/usr/bin/env python3
#
# Copyright 2022 Graviti. Licensed under MIT License.
#

"""Interfaces about the commit."""

from typing import Any, Dict, Optional
from urllib.parse import urljoin

from graviti.openapi.request import URL_PATH_PREFIX, open_api_do


def commit_draft(
    url: str,
    access_key: str,
    dataset_name: str,
    draft_number: int,
    title: str,
    *,
    description: Optional[str] = None,
) -> Dict[str, str]:
    """Execute the OpenAPI `POST /v1/datasets/{dataset_name}/commits`.

    Arguments:
        url: The URL of the graviti website.
        access_key: User's access key.
        dataset_name: Name of the dataset, unique for a user.
        draft_number: The draft number.
        title: The draft title.
        description: The draft description.

    Returns:
        The response of OpenAPI.

    Examples:
        >>> commit_draft(
        ...     "https://graviti.com/",
        ...     "ACCESSKEY-********",
        ...     "MNIST",
        ...     2,
        ...     "commit-2",
        ... )
        {
            "commitId": "a0d4065872f245e4ad1d0d1186e3d397"
        }

    """
    url = urljoin(url, f"{URL_PATH_PREFIX}/datasets/{dataset_name}/commits")
    post_data: Dict[str, Any] = {"draft_number": draft_number, "title": title}

    if description:
        post_data["description"] = description

    return open_api_do(  # type: ignore[no-any-return]
        "POST", access_key, url, json=post_data
    ).json()


def list_commits(
    url: str,
    access_key: str,
    dataset_name: str,
    *,
    revision: Optional[str] = None,
    offset: int = 0,
    limit: int = 128,
) -> Dict[str, Any]:
    """Execute the OpenAPI `GET /v1/datasets/{dataset_name}/commits`.

    Arguments:
        url: The URL of the graviti website.
        access_key: User's access key.
        dataset_name: Name of the dataset, unique for a user.
        revision: The information to locate the specific commit, which can be the commit id,
            the branch name, or the tag name.
        offset: The offset of the page.
        limit: The limit of the page.

    Returns:
        The response of OpenAPI.

    Examples:
        >>> list_commits(
        ...     "https://graviti.com/",
        ...     "ACCESSKEY-********",
        ...     "MNIST",
        ... )
        {
           "commits": [
               {
                   "commit_id": "85c57a7f03804ccc906632248dc8c359",
                   "parent_commitId": "784ba0d3bf0a41f6a7bfd771d8c00fcb",
                   "title": "upload data",
                   "description": "",
                   "committer": "Gravitier",
                   "committed_at": "2021-03-03T18:58:10Z"
               }
           ],
           "offset": 0,
           "record_size": 1,
           "total_count": 1
        }

    """
    url = urljoin(url, f"{URL_PATH_PREFIX}/datasets/{dataset_name}/commits")
    params: Dict[str, Any] = {"offset": offset, "limit": limit}

    if revision:
        params["revision"] = revision

    return open_api_do("GET", access_key, url, params=params).json()  # type: ignore[no-any-return]


def get_commit(url: str, access_key: str, dataset_name: str, commit_id: str) -> Dict[str, str]:
    """Execute the OpenAPI `GET /v1/datasets/{dataset_name}/commits/{commit_id}`.

    Arguments:
        url: The URL of the graviti website.
        access_key: User's access key.
        dataset_name: Name of the dataset, unique for a user.
        commit_id: The commit ID.

    Returns:
        The response of OpenAPI.

    Examples:
        >>> get_commit(
        ...     "https://graviti.com/",
        ...     "ACCESSKEY-********",
        ...     "MNIST",
        ...     "85c57a7f03804ccc906632248dc8c359"
        ... )
        {
            "commit_id": "85c57a7f03804ccc906632248dc8c359",
            "parent_commit_id": "784ba0d3bf0a41f6a7bfd771d8c00fcb",
            "title": "upload data",
            "description": "",
            "committer": "czhual",
            "committed_at": "2021-03-03T18:58:10Z"
        }

    """
    url = urljoin(url, f"{URL_PATH_PREFIX}/datasets/{dataset_name}/commits/{commit_id}")
    return open_api_do("GET", access_key, url).json()  # type: ignore[no-any-return]


def get_revision(url: str, access_key: str, dataset_name: str, revision: str) -> Dict[str, str]:
    """Execute the OpenAPI `GET /v1/datasets/{dataset_name}/revisions/{revision}`.

    Arguments:
        url: The URL of the graviti website.
        access_key: User's access key.
        dataset_name: Name of the dataset, unique for a user.
        revision: The information to locate the specific commit, which can be the commit id,
            the branch name, or the tag name.

    Returns:
        The response of OpenAPI.

    Examples:
        >>> get_revision(
        ...     "https://graviti.com/",
        ...     "ACCESSKEY-********",
        ...     "MNIST",
        ...     "branch-1"
        ... )
        {
           "commit_id": "85c57a7f03804ccc906632248dc8c359",
           "type": "branch"
        }

    """
    url = urljoin(url, f"{URL_PATH_PREFIX}/datasets/{dataset_name}/revisions/{revision}")
    return open_api_do("GET", access_key, url).json()  # type: ignore[no-any-return]
