#!/usr/bin/python
#
# Copyright 2018-2021 Polyaxon, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# coding: utf-8

# flake8: noqa

"""
    Polyaxon SDKs and REST API specification.

    Polyaxon SDKs and REST API specification.  # noqa: E501

    The version of the OpenAPI document: 1.15.0
    Contact: contact@polyaxon.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "1.15.0"

# import apis into sdk package
from polyaxon_sdk.api.agents_v1_api import AgentsV1Api
from polyaxon_sdk.api.artifacts_stores_v1_api import ArtifactsStoresV1Api
from polyaxon_sdk.api.auth_v1_api import AuthV1Api
from polyaxon_sdk.api.connections_v1_api import ConnectionsV1Api
from polyaxon_sdk.api.dashboards_v1_api import DashboardsV1Api
from polyaxon_sdk.api.organizations_v1_api import OrganizationsV1Api
from polyaxon_sdk.api.presets_v1_api import PresetsV1Api
from polyaxon_sdk.api.project_dashboards_v1_api import ProjectDashboardsV1Api
from polyaxon_sdk.api.project_searches_v1_api import ProjectSearchesV1Api
from polyaxon_sdk.api.projects_v1_api import ProjectsV1Api
from polyaxon_sdk.api.queues_v1_api import QueuesV1Api
from polyaxon_sdk.api.runs_v1_api import RunsV1Api
from polyaxon_sdk.api.schemas_v1_api import SchemasV1Api
from polyaxon_sdk.api.searches_v1_api import SearchesV1Api
from polyaxon_sdk.api.service_accounts_v1_api import ServiceAccountsV1Api
from polyaxon_sdk.api.tags_v1_api import TagsV1Api
from polyaxon_sdk.api.teams_v1_api import TeamsV1Api
from polyaxon_sdk.api.users_v1_api import UsersV1Api
from polyaxon_sdk.api.versions_v1_api import VersionsV1Api

# import ApiClient
from polyaxon_sdk.api_client import ApiClient
from polyaxon_sdk.configuration import Configuration
from polyaxon_sdk.exceptions import OpenApiException
from polyaxon_sdk.exceptions import ApiTypeError
from polyaxon_sdk.exceptions import ApiValueError
from polyaxon_sdk.exceptions import ApiKeyError
from polyaxon_sdk.exceptions import ApiAttributeError
from polyaxon_sdk.exceptions import ApiException
# import models into sdk package
from polyaxon_sdk.models.agent_state_response_agent_state import AgentStateResponseAgentState
from polyaxon_sdk.models.mpi_job_implementation import MPIJobImplementation
from polyaxon_sdk.models.mx_job_mode import MXJobMode
from polyaxon_sdk.models.protobuf_any import ProtobufAny
from polyaxon_sdk.models.protobuf_null_value import ProtobufNullValue
from polyaxon_sdk.models.runtime_error import RuntimeError
from polyaxon_sdk.models.search_view import SearchView
from polyaxon_sdk.models.spark_deploy_mode import SparkDeployMode
from polyaxon_sdk.models.v1_activity import V1Activity
from polyaxon_sdk.models.v1_agent import V1Agent
from polyaxon_sdk.models.v1_agent_state_response import V1AgentStateResponse
from polyaxon_sdk.models.v1_agent_status_body_request import V1AgentStatusBodyRequest
from polyaxon_sdk.models.v1_analytics_spec import V1AnalyticsSpec
from polyaxon_sdk.models.v1_artifact_kind import V1ArtifactKind
from polyaxon_sdk.models.v1_artifact_tree import V1ArtifactTree
from polyaxon_sdk.models.v1_artifacts_mount import V1ArtifactsMount
from polyaxon_sdk.models.v1_artifacts_type import V1ArtifactsType
from polyaxon_sdk.models.v1_auth import V1Auth
from polyaxon_sdk.models.v1_auth_type import V1AuthType
from polyaxon_sdk.models.v1_average_stopping_policy import V1AverageStoppingPolicy
from polyaxon_sdk.models.v1_bayes import V1Bayes
from polyaxon_sdk.models.v1_bucket_connection import V1BucketConnection
from polyaxon_sdk.models.v1_build import V1Build
from polyaxon_sdk.models.v1_cache import V1Cache
from polyaxon_sdk.models.v1_claim_connection import V1ClaimConnection
from polyaxon_sdk.models.v1_clean_pod_policy import V1CleanPodPolicy
from polyaxon_sdk.models.v1_cloning import V1Cloning
from polyaxon_sdk.models.v1_cloning_kind import V1CloningKind
from polyaxon_sdk.models.v1_compatibility import V1Compatibility
from polyaxon_sdk.models.v1_compiled_operation import V1CompiledOperation
from polyaxon_sdk.models.v1_component import V1Component
from polyaxon_sdk.models.v1_connection_kind import V1ConnectionKind
from polyaxon_sdk.models.v1_connection_response import V1ConnectionResponse
from polyaxon_sdk.models.v1_connection_schema import V1ConnectionSchema
from polyaxon_sdk.models.v1_connection_type import V1ConnectionType
from polyaxon_sdk.models.v1_credentials import V1Credentials
from polyaxon_sdk.models.v1_cron_schedule import V1CronSchedule
from polyaxon_sdk.models.v1_dag import V1Dag
from polyaxon_sdk.models.v1_dag_ref import V1DagRef
from polyaxon_sdk.models.v1_dashboard import V1Dashboard
from polyaxon_sdk.models.v1_dashboard_spec import V1DashboardSpec
from polyaxon_sdk.models.v1_dask import V1Dask
from polyaxon_sdk.models.v1_date_time_schedule import V1DateTimeSchedule
from polyaxon_sdk.models.v1_diff_stopping_policy import V1DiffStoppingPolicy
from polyaxon_sdk.models.v1_dockerfile_type import V1DockerfileType
from polyaxon_sdk.models.v1_early_stopping import V1EarlyStopping
from polyaxon_sdk.models.v1_entities_tags import V1EntitiesTags
from polyaxon_sdk.models.v1_entities_transfer import V1EntitiesTransfer
from polyaxon_sdk.models.v1_entity_notification_body import V1EntityNotificationBody
from polyaxon_sdk.models.v1_entity_stage_body_request import V1EntityStageBodyRequest
from polyaxon_sdk.models.v1_entity_status_body_request import V1EntityStatusBodyRequest
from polyaxon_sdk.models.v1_environment import V1Environment
from polyaxon_sdk.models.v1_event import V1Event
from polyaxon_sdk.models.v1_event_artifact import V1EventArtifact
from polyaxon_sdk.models.v1_event_audio import V1EventAudio
from polyaxon_sdk.models.v1_event_chart import V1EventChart
from polyaxon_sdk.models.v1_event_chart_kind import V1EventChartKind
from polyaxon_sdk.models.v1_event_confusion_matrix import V1EventConfusionMatrix
from polyaxon_sdk.models.v1_event_curve import V1EventCurve
from polyaxon_sdk.models.v1_event_curve_kind import V1EventCurveKind
from polyaxon_sdk.models.v1_event_dataframe import V1EventDataframe
from polyaxon_sdk.models.v1_event_histogram import V1EventHistogram
from polyaxon_sdk.models.v1_event_image import V1EventImage
from polyaxon_sdk.models.v1_event_kind import V1EventKind
from polyaxon_sdk.models.v1_event_model import V1EventModel
from polyaxon_sdk.models.v1_event_trigger import V1EventTrigger
from polyaxon_sdk.models.v1_event_type import V1EventType
from polyaxon_sdk.models.v1_event_video import V1EventVideo
from polyaxon_sdk.models.v1_events_response import V1EventsResponse
from polyaxon_sdk.models.v1_failure_early_stopping import V1FailureEarlyStopping
from polyaxon_sdk.models.v1_file_type import V1FileType
from polyaxon_sdk.models.v1_flink import V1Flink
from polyaxon_sdk.models.v1_gcs_type import V1GcsType
from polyaxon_sdk.models.v1_git_connection import V1GitConnection
from polyaxon_sdk.models.v1_git_type import V1GitType
from polyaxon_sdk.models.v1_grid_search import V1GridSearch
from polyaxon_sdk.models.v1_hook import V1Hook
from polyaxon_sdk.models.v1_host_connection import V1HostConnection
from polyaxon_sdk.models.v1_host_path_connection import V1HostPathConnection
from polyaxon_sdk.models.v1_hp_choice import V1HpChoice
from polyaxon_sdk.models.v1_hp_date_range import V1HpDateRange
from polyaxon_sdk.models.v1_hp_date_time_range import V1HpDateTimeRange
from polyaxon_sdk.models.v1_hp_geom_space import V1HpGeomSpace
from polyaxon_sdk.models.v1_hp_lin_space import V1HpLinSpace
from polyaxon_sdk.models.v1_hp_log_normal import V1HpLogNormal
from polyaxon_sdk.models.v1_hp_log_space import V1HpLogSpace
from polyaxon_sdk.models.v1_hp_log_uniform import V1HpLogUniform
from polyaxon_sdk.models.v1_hp_normal import V1HpNormal
from polyaxon_sdk.models.v1_hp_p_choice import V1HpPChoice
from polyaxon_sdk.models.v1_hp_params import V1HpParams
from polyaxon_sdk.models.v1_hp_q_log_normal import V1HpQLogNormal
from polyaxon_sdk.models.v1_hp_q_log_uniform import V1HpQLogUniform
from polyaxon_sdk.models.v1_hp_q_normal import V1HpQNormal
from polyaxon_sdk.models.v1_hp_q_uniform import V1HpQUniform
from polyaxon_sdk.models.v1_hp_range import V1HpRange
from polyaxon_sdk.models.v1_hp_uniform import V1HpUniform
from polyaxon_sdk.models.v1_hub_ref import V1HubRef
from polyaxon_sdk.models.v1_hyperband import V1Hyperband
from polyaxon_sdk.models.v1_hyperopt import V1Hyperopt
from polyaxon_sdk.models.v1_hyperopt_algorithms import V1HyperoptAlgorithms
from polyaxon_sdk.models.v1_io import V1IO
from polyaxon_sdk.models.v1_init import V1Init
from polyaxon_sdk.models.v1_installation import V1Installation
from polyaxon_sdk.models.v1_interval_schedule import V1IntervalSchedule
from polyaxon_sdk.models.v1_iterative import V1Iterative
from polyaxon_sdk.models.v1_job import V1Job
from polyaxon_sdk.models.v1_join import V1Join
from polyaxon_sdk.models.v1_join_param import V1JoinParam
from polyaxon_sdk.models.v1_k8s_resource_schema import V1K8sResourceSchema
from polyaxon_sdk.models.v1_k8s_resource_type import V1K8sResourceType
from polyaxon_sdk.models.v1_kf_replica import V1KFReplica
from polyaxon_sdk.models.v1_list_activities_response import V1ListActivitiesResponse
from polyaxon_sdk.models.v1_list_agents_response import V1ListAgentsResponse
from polyaxon_sdk.models.v1_list_bookmarks_response import V1ListBookmarksResponse
from polyaxon_sdk.models.v1_list_connections_response import V1ListConnectionsResponse
from polyaxon_sdk.models.v1_list_dashboards_response import V1ListDashboardsResponse
from polyaxon_sdk.models.v1_list_organization_members_response import V1ListOrganizationMembersResponse
from polyaxon_sdk.models.v1_list_organizations_response import V1ListOrganizationsResponse
from polyaxon_sdk.models.v1_list_presets_response import V1ListPresetsResponse
from polyaxon_sdk.models.v1_list_project_versions_response import V1ListProjectVersionsResponse
from polyaxon_sdk.models.v1_list_projects_response import V1ListProjectsResponse
from polyaxon_sdk.models.v1_list_queues_response import V1ListQueuesResponse
from polyaxon_sdk.models.v1_list_run_artifacts_response import V1ListRunArtifactsResponse
from polyaxon_sdk.models.v1_list_run_connections_response import V1ListRunConnectionsResponse
from polyaxon_sdk.models.v1_list_run_edges_response import V1ListRunEdgesResponse
from polyaxon_sdk.models.v1_list_runs_response import V1ListRunsResponse
from polyaxon_sdk.models.v1_list_searches_response import V1ListSearchesResponse
from polyaxon_sdk.models.v1_list_service_accounts_response import V1ListServiceAccountsResponse
from polyaxon_sdk.models.v1_list_tags_response import V1ListTagsResponse
from polyaxon_sdk.models.v1_list_team_members_response import V1ListTeamMembersResponse
from polyaxon_sdk.models.v1_list_teams_response import V1ListTeamsResponse
from polyaxon_sdk.models.v1_list_token_response import V1ListTokenResponse
from polyaxon_sdk.models.v1_log import V1Log
from polyaxon_sdk.models.v1_log_handler import V1LogHandler
from polyaxon_sdk.models.v1_logs import V1Logs
from polyaxon_sdk.models.v1_mpi_job import V1MPIJob
from polyaxon_sdk.models.v1_mx_job import V1MXJob
from polyaxon_sdk.models.v1_mapping import V1Mapping
from polyaxon_sdk.models.v1_matrix import V1Matrix
from polyaxon_sdk.models.v1_matrix_kind import V1MatrixKind
from polyaxon_sdk.models.v1_median_stopping_policy import V1MedianStoppingPolicy
from polyaxon_sdk.models.v1_metric_early_stopping import V1MetricEarlyStopping
from polyaxon_sdk.models.v1_notification import V1Notification
from polyaxon_sdk.models.v1_operation import V1Operation
from polyaxon_sdk.models.v1_operation_body import V1OperationBody
from polyaxon_sdk.models.v1_optimization import V1Optimization
from polyaxon_sdk.models.v1_optimization_metric import V1OptimizationMetric
from polyaxon_sdk.models.v1_optimization_resource import V1OptimizationResource
from polyaxon_sdk.models.v1_organization import V1Organization
from polyaxon_sdk.models.v1_organization_member import V1OrganizationMember
from polyaxon_sdk.models.v1_owner_sub_entity_resource_request_by_uid import V1OwnerSubEntityResourceRequestByUid
from polyaxon_sdk.models.v1_param import V1Param
from polyaxon_sdk.models.v1_password_change import V1PasswordChange
from polyaxon_sdk.models.v1_patch_strategy import V1PatchStrategy
from polyaxon_sdk.models.v1_path_ref import V1PathRef
from polyaxon_sdk.models.v1_pipeline import V1Pipeline
from polyaxon_sdk.models.v1_pipeline_kind import V1PipelineKind
from polyaxon_sdk.models.v1_plugins import V1Plugins
from polyaxon_sdk.models.v1_polyaxon_init_container import V1PolyaxonInitContainer
from polyaxon_sdk.models.v1_polyaxon_sidecar_container import V1PolyaxonSidecarContainer
from polyaxon_sdk.models.v1_preset import V1Preset
from polyaxon_sdk.models.v1_project import V1Project
from polyaxon_sdk.models.v1_project_settings import V1ProjectSettings
from polyaxon_sdk.models.v1_project_user_access import V1ProjectUserAccess
from polyaxon_sdk.models.v1_project_version import V1ProjectVersion
from polyaxon_sdk.models.v1_project_version_kind import V1ProjectVersionKind
from polyaxon_sdk.models.v1_pytorch_job import V1PytorchJob
from polyaxon_sdk.models.v1_queue import V1Queue
from polyaxon_sdk.models.v1_random_search import V1RandomSearch
from polyaxon_sdk.models.v1_ray import V1Ray
from polyaxon_sdk.models.v1_reference import V1Reference
from polyaxon_sdk.models.v1_resource_type import V1ResourceType
from polyaxon_sdk.models.v1_run import V1Run
from polyaxon_sdk.models.v1_run_artifact import V1RunArtifact
from polyaxon_sdk.models.v1_run_artifacts import V1RunArtifacts
from polyaxon_sdk.models.v1_run_connection import V1RunConnection
from polyaxon_sdk.models.v1_run_edge import V1RunEdge
from polyaxon_sdk.models.v1_run_edge_kind import V1RunEdgeKind
from polyaxon_sdk.models.v1_run_kind import V1RunKind
from polyaxon_sdk.models.v1_run_pending import V1RunPending
from polyaxon_sdk.models.v1_run_reference_catalog import V1RunReferenceCatalog
from polyaxon_sdk.models.v1_run_resources import V1RunResources
from polyaxon_sdk.models.v1_run_schema import V1RunSchema
from polyaxon_sdk.models.v1_run_settings import V1RunSettings
from polyaxon_sdk.models.v1_s3_type import V1S3Type
from polyaxon_sdk.models.v1_schedule import V1Schedule
from polyaxon_sdk.models.v1_schedule_kind import V1ScheduleKind
from polyaxon_sdk.models.v1_scheduling_policy import V1SchedulingPolicy
from polyaxon_sdk.models.v1_schemas import V1Schemas
from polyaxon_sdk.models.v1_search import V1Search
from polyaxon_sdk.models.v1_search_spec import V1SearchSpec
from polyaxon_sdk.models.v1_section_spec import V1SectionSpec
from polyaxon_sdk.models.v1_service import V1Service
from polyaxon_sdk.models.v1_service_account import V1ServiceAccount
from polyaxon_sdk.models.v1_settings_catalog import V1SettingsCatalog
from polyaxon_sdk.models.v1_spark import V1Spark
from polyaxon_sdk.models.v1_spark_replica import V1SparkReplica
from polyaxon_sdk.models.v1_spark_type import V1SparkType
from polyaxon_sdk.models.v1_stage import V1Stage
from polyaxon_sdk.models.v1_stage_condition import V1StageCondition
from polyaxon_sdk.models.v1_stages import V1Stages
from polyaxon_sdk.models.v1_status import V1Status
from polyaxon_sdk.models.v1_status_condition import V1StatusCondition
from polyaxon_sdk.models.v1_statuses import V1Statuses
from polyaxon_sdk.models.v1_tf_job import V1TFJob
from polyaxon_sdk.models.v1_tag import V1Tag
from polyaxon_sdk.models.v1_team import V1Team
from polyaxon_sdk.models.v1_team_member import V1TeamMember
from polyaxon_sdk.models.v1_team_settings import V1TeamSettings
from polyaxon_sdk.models.v1_template import V1Template
from polyaxon_sdk.models.v1_termination import V1Termination
from polyaxon_sdk.models.v1_token import V1Token
from polyaxon_sdk.models.v1_trial_start import V1TrialStart
from polyaxon_sdk.models.v1_trigger_policy import V1TriggerPolicy
from polyaxon_sdk.models.v1_truncation_stopping_policy import V1TruncationStoppingPolicy
from polyaxon_sdk.models.v1_tuner import V1Tuner
from polyaxon_sdk.models.v1_uri_type import V1UriType
from polyaxon_sdk.models.v1_url_ref import V1UrlRef
from polyaxon_sdk.models.v1_user import V1User
from polyaxon_sdk.models.v1_user_email import V1UserEmail
from polyaxon_sdk.models.v1_user_singup import V1UserSingup
from polyaxon_sdk.models.v1_uuids import V1Uuids
from polyaxon_sdk.models.v1_version import V1Version
from polyaxon_sdk.models.v1_wasb_type import V1WasbType
from polyaxon_sdk.models.v1_xg_boost_job import V1XGBoostJob

