from typing import Dict, Type

from .created import Created
from .duplicate import Duplicate
from .empty import Empty
from .exif import Exif
from .extension import Extension
from .filecontent import FileContent
from .filter import Filter
from .hash import Hash
from .lastmodified import LastModified
from .mimetype import MimeType
from .name import Name
from .python import Python
from .regex import Regex
from .size import Size

FILTERS = {
    Created.name: Created,
    Duplicate.name: Duplicate,
    Empty.name: Empty,
    Exif.name: Exif,
    Extension.name: Extension,
    FileContent.name: FileContent,
    Hash.name: Hash,
    Name.name: Name,
    Size.name: Size,
    LastModified.name: LastModified,
    MimeType.name: MimeType,
    Python.name: Python,
    Regex.name: Regex,
}  # type: Dict[str, Type[Filter]]
