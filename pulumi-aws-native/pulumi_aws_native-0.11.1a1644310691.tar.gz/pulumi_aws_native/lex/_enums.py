# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'BotAliasStatus',
    'BotObfuscationSettingObfuscationSettingType',
    'BotSlotConstraint',
    'BotSlotValueResolutionStrategy',
]


class BotAliasStatus(str, Enum):
    CREATING = "Creating"
    AVAILABLE = "Available"
    DELETING = "Deleting"
    FAILED = "Failed"


class BotObfuscationSettingObfuscationSettingType(str, Enum):
    """
    Value that determines whether Amazon Lex obscures slot values in conversation logs. The default is to obscure the values.
    """
    NONE = "None"
    DEFAULT_OBFUSCATION = "DefaultObfuscation"


class BotSlotConstraint(str, Enum):
    REQUIRED = "Required"
    OPTIONAL = "Optional"


class BotSlotValueResolutionStrategy(str, Enum):
    ORIGINAL_VALUE = "ORIGINAL_VALUE"
    TOP_RESOLUTION = "TOP_RESOLUTION"
