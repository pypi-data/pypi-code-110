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

from collections.abc import Hashable, Iterable, MutableMapping
from typing import Any, Final, Literal

__all__: Final[tuple[str, ...]] = (
    "make_hashable",
    "Undefined",
    "UndefinedType"
)


def make_hashable(obj: Any, /) -> Hashable:
    if isinstance(obj, MutableMapping):
        return tuple((key, make_hashable(value)) for key, value in sorted(obj.items()))

    # Try hash to avoid converting a hashable iterable (e.g. string, frozenset)
    # to a tuple:
    try:
        hash(obj)
    except TypeError:
        if isinstance(obj, Iterable):
            return tuple(map(make_hashable, obj))
        # Non-hashable, non-iterable:
        raise

    return obj


class UndefinedType:
    __slots__: tuple[str, ...] = ()

    def __repr__(self) -> Literal["Undefined"]:
        return "Undefined"

    def __hash__(self) -> Literal[0xDEADBEEF]:
        return 0xDEADBEEF

    def __eq__(self, obj: Any, /) -> bool:
        return isinstance(obj, self.__class__)

    def __bool__(self) -> Literal[False]:
        return False


Undefined: Final[UndefinedType] = UndefinedType()
