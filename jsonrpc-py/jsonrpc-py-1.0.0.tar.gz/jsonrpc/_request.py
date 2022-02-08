# Pure zero-dependency JSON-RPC 2.0 implementation.
# Copyright © 2022 Andrew Malchuk. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from abc import ABCMeta, abstractmethod
from collections.abc import Iterable, Iterator, MutableMapping, MutableSequence
from numbers import Number
from typing import Any, Final, TypeAlias, TypeVar

from ._errors import BaseError, Error, ErrorEnum
from ._utilities import Undefined, UndefinedType, make_hashable

__all__: Final[tuple[str, ...]] = (
    "BaseBatchRequest",
    "BaseRequest",
    "BatchRequest",
    "Request"
)

_T = TypeVar("_T")
_Args: TypeAlias = MutableSequence[Any]
_Kwargs: TypeAlias = MutableMapping[str, Any]


class BaseRequest(metaclass=ABCMeta):
    __slots__: tuple[str, ...] = ()

    @property
    @abstractmethod
    def method(self) -> str:
        raise NotImplementedError

    @property
    @abstractmethod
    def args(self) -> tuple[Any, ...]:
        raise NotImplementedError

    @property
    @abstractmethod
    def kwargs(self) -> dict[str, Any]:
        raise NotImplementedError

    @property
    @abstractmethod
    def request_id(self) -> str | Number | UndefinedType:
        raise NotImplementedError

    @property
    @abstractmethod
    def is_notification(self) -> bool:
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def from_json(cls, obj: dict[str, Any], /) -> "BaseRequest | BaseError":
        raise NotImplementedError


class BaseBatchRequest(Iterable[BaseRequest | BaseError]):
    __slots__: tuple[str, ...] = ()

    @abstractmethod
    def __len__(self) -> int:
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def from_json(cls, obj: list[dict[str, Any]], /) -> "BaseBatchRequest":
        raise NotImplementedError


class Request(BaseRequest):
    """
    Base JSON-RPC request object.

    :param method: The :py:class:`str` object containing the name of the method to be invoked by the :class:`jsonrpc.WSGIHandler` instance.
    :param params: The object of type :py:class:`collections.abc.MutableSequence` or :py:class:`collections.abc.MutableMapping` that holds
        the parameter values to be used during the invocation of the method. May be omitted if provided method has no parameters for
        example.
    :param request_id: The :py:class:`str` object or any type of :py:class:`numbers.Number` object which represents an identifier
        of the request instance. May be omitted. If its value omitted, the request assumed to be a notification.
    :raises jsonrpc.Error: If the request method isn't a string or have a \"rpc.\" prefix, if the request parameters
        aren't an objects of type :py:class:`collections.abc.MutableSequence` or :py:class:`collections.abc.MutableMapping` if provided,
        also if the request identifier isn't an object of type :py:class:`str` or :py:class:`numbers.Number` if provided.
    """
    __slots__: tuple[str, ...] = "_method", "_params", "_id"

    def __init__(self, *,
        method: str,
        params: _Args | _Kwargs | UndefinedType = Undefined,
        request_id: str | Number | UndefinedType = Undefined
    ) -> None:
        self._method: str = self._is_method_valid(method=method)
        self._params: _Args | _Kwargs | UndefinedType = self._is_params_valid(params=params)
        self._id: str | Number | UndefinedType = self._is_request_id_valid(request_id=request_id)

    def __repr__(self) -> str:
        return f"<{__package__}.{self.__class__.__name__}(" \
            f"method={self._method!r}, " \
            f"params={self._params!r}, " \
            f"request_id={self._id!r})>"

    def __hash__(self) -> int:
        return hash(self._method) ^ hash(make_hashable(self._params)) ^ hash(self._id)

    def __eq__(self, obj: Any, /) -> bool:
        return isinstance(obj, self.__class__) \
            and self._method == obj._method \
            and self._params == obj._params \
            and self._id == obj._id

    def _is_method_valid(self, *, method: _T) -> _T:
        if not isinstance(method, str) or method.startswith("\x72\x70\x63\x2E"):
            raise Error(
                code=ErrorEnum.INVALID_REQUEST,
                message=f"Request method must be a string and doesn't have a \"rpc.\" prefix")

        return method

    def _is_params_valid(self, *, params: _T) -> _T:
        if not isinstance(params, MutableSequence | MutableMapping | UndefinedType):
            raise Error(
                code=ErrorEnum.INVALID_REQUEST,
                message=f"Request params must be a sequence or mapping, not a {type(params).__name__!r}")

        return params

    def _is_request_id_valid(self, *, request_id: _T) -> _T:
        if not isinstance(request_id, str | Number | UndefinedType):
            raise Error(
                code=ErrorEnum.INVALID_REQUEST,
                message=f"Request id must be an optional string or number, not a {type(request_id).__name__!r}")

        return request_id

    @property
    def method(self) -> str:
        """
        Returns the :py:class:`str` object containing the name of the method.
        """
        return self._method

    @property
    def args(self) -> tuple[Any, ...]:
        """
        Returns the :py:class:`tuple` object containing positional arguments of the method.
        """
        return tuple(self._params) if isinstance(self._params, MutableSequence) else ()

    @property
    def kwargs(self) -> dict[str, Any]:
        """
        Returns the :py:class:`dict` object containing keyword arguments of the method.
        """
        return dict(self._params) if isinstance(self._params, MutableMapping) else {}

    @property
    def request_id(self) -> str | Number | UndefinedType:
        """
        Returns the :py:class:`str` object or any type of :py:class:`numbers.Number` object
        containing the identifier of the request if its value is set.
        """
        return self._id

    @property
    def is_notification(self) -> bool:
        """
        Returns :py:data:`True` if the identifier of the request is omitted, :py:data:`False` elsewise.
        """
        return isinstance(self._id, UndefinedType)

    @classmethod
    def from_json(cls, obj: dict[str, Any], /) -> "Request | Error":
        """
        The class method for creating the :class:`jsonrpc.Request` object from :py:class:`dict` object.
        Primarily used by the :class:`jsonrpc.WSGIHandler` instance.
        Unlike the :class:`jsonrpc.Request` constructor, doesn't raises any exceptions by validations,
        it returns the :class:`jsonrpc.Error` as is.

        Example usage::

            >>> Request.from_json({"jsonrpc": "2.0", "method": "foobar", "id": 1})
            <jsonrpc.Request(method="foobar", params=Undefined, request_id=1)>
            >>> Request.from_json({"not_jsonrpc": True})
            <jsonrpc.Error(code=-32600, message="Invalid request object", data={"not_jsonrpc": True})>
        """
        try:
            match obj:
                case {"jsonrpc": "2.0", "method": method, "params": params, "id": request_id}:
                    return Request(method=method, params=params, request_id=request_id)
                case {"jsonrpc": "2.0", "method": method, "params": params}:
                    return Request(method=method, params=params)
                case {"jsonrpc": "2.0", "method": method, "id": request_id}:
                    return Request(method=method, request_id=request_id)
                case {"jsonrpc": "2.0", "method": method}:
                    return Request(method=method)
                case _:
                    raise Error(code=ErrorEnum.INVALID_REQUEST, message="Invalid request object", data=obj)
        except BaseError as error:
            return error


class BatchRequest(BaseBatchRequest[Request | Error]):
    """
    The :py:class:`collections.abc.Iterable` subclass representing the collection
    of :class:`jsonrpc.Request` and :class:`jsonrpc.Error` objects.

    :var requests: Instance variable representing the :py:class:`tuple` object
        for proxying the :py:class:`collections.abc.Iterable` interface methods.
    """
    __slots__: str = "requests"

    def __init__(self, requests: Iterable[Request | Error], /) -> None:
        self.requests: tuple[Request | Error, ...] = tuple(requests)

    def __repr__(self) -> str:
        return f"<{__package__}.{self.__class__.__name__}({self.requests!r})>"

    def __hash__(self) -> int:
        return hash(self.requests)

    def __eq__(self, obj: Any, /) -> bool:
        return isinstance(obj, self.__class__) \
            and len(self.requests) == len(obj.requests) \
            and frozenset(self.requests).issubset(obj.requests)

    def __iter__(self) -> Iterator[Request | Error]:
        return iter(self.requests)

    def __len__(self) -> int:
        return len(self.requests)

    @classmethod
    def from_json(cls, obj: list[dict[str, Any]], /) -> "BatchRequest":
        """
        The class method for creating the :class:`jsonrpc.BatchRequest` object from :py:class:`collections.abc.Iterable`
        of :py:class:`dict` objects.
        Primarily used by the :class:`jsonrpc.WSGIHandler` instance.
        Similar to :func:`jsonrpc.Request.from_json` function it doesn't raises any exceptions.

        Example usage::

            >>> BatchRequest.from_json([
            ...     {"jsonrpc": "2.0", "method": "foobar", "id": 1},
            ...     {"not_jsonrpc": True}
            ... ])
            <jsonrpc.BatchRequest((<jsonrpc.Request(\u2026)>, <jsonrpc.Error(\u2026)>))>
        """
        return BatchRequest(map(Request.from_json, obj))
