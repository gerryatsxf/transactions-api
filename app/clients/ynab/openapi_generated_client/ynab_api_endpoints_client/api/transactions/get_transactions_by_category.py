import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error_response import ErrorResponse
from ...models.get_transactions_by_category_type import GetTransactionsByCategoryType
from ...models.hybrid_transactions_response import HybridTransactionsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    budget_id: str,
    category_id: str,
    *,
    client: Client,
    since_date: Union[Unset, None, datetime.date] = UNSET,
    type: Union[Unset, None, GetTransactionsByCategoryType] = UNSET,
    last_knowledge_of_server: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/budgets/{budget_id}/categories/{category_id}/transactions".format(
        client.base_url, budget_id=budget_id, category_id=category_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_since_date: Union[Unset, None, str] = UNSET
    if not isinstance(since_date, Unset):
        json_since_date = since_date.isoformat() if since_date else None

    params["since_date"] = json_since_date

    json_type: Union[Unset, None, str] = UNSET
    if not isinstance(type, Unset):
        json_type = type.value if type else None

    params["type"] = json_type

    params["last_knowledge_of_server"] = last_knowledge_of_server

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[ErrorResponse, HybridTransactionsResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = HybridTransactionsResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[ErrorResponse, HybridTransactionsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    budget_id: str,
    category_id: str,
    *,
    client: Client,
    since_date: Union[Unset, None, datetime.date] = UNSET,
    type: Union[Unset, None, GetTransactionsByCategoryType] = UNSET,
    last_knowledge_of_server: Union[Unset, None, int] = UNSET,
) -> Response[Union[ErrorResponse, HybridTransactionsResponse]]:
    """List category transactions

     Returns all transactions for a specified category

    Args:
        budget_id (str):
        category_id (str):
        since_date (Union[Unset, None, datetime.date]):
        type (Union[Unset, None, GetTransactionsByCategoryType]):
        last_knowledge_of_server (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, HybridTransactionsResponse]]
    """

    kwargs = _get_kwargs(
        budget_id=budget_id,
        category_id=category_id,
        client=client,
        since_date=since_date,
        type=type,
        last_knowledge_of_server=last_knowledge_of_server,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    budget_id: str,
    category_id: str,
    *,
    client: Client,
    since_date: Union[Unset, None, datetime.date] = UNSET,
    type: Union[Unset, None, GetTransactionsByCategoryType] = UNSET,
    last_knowledge_of_server: Union[Unset, None, int] = UNSET,
) -> Optional[Union[ErrorResponse, HybridTransactionsResponse]]:
    """List category transactions

     Returns all transactions for a specified category

    Args:
        budget_id (str):
        category_id (str):
        since_date (Union[Unset, None, datetime.date]):
        type (Union[Unset, None, GetTransactionsByCategoryType]):
        last_knowledge_of_server (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, HybridTransactionsResponse]]
    """

    return sync_detailed(
        budget_id=budget_id,
        category_id=category_id,
        client=client,
        since_date=since_date,
        type=type,
        last_knowledge_of_server=last_knowledge_of_server,
    ).parsed


async def asyncio_detailed(
    budget_id: str,
    category_id: str,
    *,
    client: Client,
    since_date: Union[Unset, None, datetime.date] = UNSET,
    type: Union[Unset, None, GetTransactionsByCategoryType] = UNSET,
    last_knowledge_of_server: Union[Unset, None, int] = UNSET,
) -> Response[Union[ErrorResponse, HybridTransactionsResponse]]:
    """List category transactions

     Returns all transactions for a specified category

    Args:
        budget_id (str):
        category_id (str):
        since_date (Union[Unset, None, datetime.date]):
        type (Union[Unset, None, GetTransactionsByCategoryType]):
        last_knowledge_of_server (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, HybridTransactionsResponse]]
    """

    kwargs = _get_kwargs(
        budget_id=budget_id,
        category_id=category_id,
        client=client,
        since_date=since_date,
        type=type,
        last_knowledge_of_server=last_knowledge_of_server,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    budget_id: str,
    category_id: str,
    *,
    client: Client,
    since_date: Union[Unset, None, datetime.date] = UNSET,
    type: Union[Unset, None, GetTransactionsByCategoryType] = UNSET,
    last_knowledge_of_server: Union[Unset, None, int] = UNSET,
) -> Optional[Union[ErrorResponse, HybridTransactionsResponse]]:
    """List category transactions

     Returns all transactions for a specified category

    Args:
        budget_id (str):
        category_id (str):
        since_date (Union[Unset, None, datetime.date]):
        type (Union[Unset, None, GetTransactionsByCategoryType]):
        last_knowledge_of_server (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, HybridTransactionsResponse]]
    """

    return (
        await asyncio_detailed(
            budget_id=budget_id,
            category_id=category_id,
            client=client,
            since_date=since_date,
            type=type,
            last_knowledge_of_server=last_knowledge_of_server,
        )
    ).parsed
