from dataclasses import field as dataclass_field

from pydantic.dataclasses import dataclass
from serde import deserialize

from metaphor.common.sampling import SamplingConfig
from metaphor.redshift.config import PostgreSQLRunConfig


@deserialize
@dataclass
class PostgreSQLProfileRunConfig(PostgreSQLRunConfig):

    max_concurrency = 10

    include_views: bool = False

    sampling: SamplingConfig = dataclass_field(default_factory=lambda: SamplingConfig())
