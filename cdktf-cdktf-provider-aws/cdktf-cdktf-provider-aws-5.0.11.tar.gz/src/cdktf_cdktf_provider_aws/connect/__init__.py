import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from .._jsii import *

import cdktf
import constructs


class ConnectBotAssociation(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.connect.ConnectBotAssociation",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/connect_bot_association aws_connect_bot_association}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        instance_id: builtins.str,
        lex_bot: "ConnectBotAssociationLexBot",
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/connect_bot_association aws_connect_bot_association} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_bot_association#instance_id ConnectBotAssociation#instance_id}.
        :param lex_bot: lex_bot block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_bot_association#lex_bot ConnectBotAssociation#lex_bot}
        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        '''
        config = ConnectBotAssociationConfig(
            instance_id=instance_id,
            lex_bot=lex_bot,
            count=count,
            depends_on=depends_on,
            lifecycle=lifecycle,
            provider=provider,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="putLexBot")
    def put_lex_bot(
        self,
        *,
        name: builtins.str,
        lex_region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_bot_association#name ConnectBotAssociation#name}.
        :param lex_region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_bot_association#lex_region ConnectBotAssociation#lex_region}.
        '''
        value = ConnectBotAssociationLexBot(name=name, lex_region=lex_region)

        return typing.cast(None, jsii.invoke(self, "putLexBot", [value]))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="lexBot")
    def lex_bot(self) -> "ConnectBotAssociationLexBotOutputReference":
        return typing.cast("ConnectBotAssociationLexBotOutputReference", jsii.get(self, "lexBot"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceIdInput")
    def instance_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceIdInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="lexBotInput")
    def lex_bot_input(self) -> typing.Optional["ConnectBotAssociationLexBot"]:
        return typing.cast(typing.Optional["ConnectBotAssociationLexBot"], jsii.get(self, "lexBotInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceId"))

    @instance_id.setter
    def instance_id(self, value: builtins.str) -> None:
        jsii.set(self, "instanceId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.connect.ConnectBotAssociationConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "count": "count",
        "depends_on": "dependsOn",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "instance_id": "instanceId",
        "lex_bot": "lexBot",
    },
)
class ConnectBotAssociationConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        instance_id: builtins.str,
        lex_bot: "ConnectBotAssociationLexBot",
    ) -> None:
        '''AWS Connect.

        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        :param instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_bot_association#instance_id ConnectBotAssociation#instance_id}.
        :param lex_bot: lex_bot block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_bot_association#lex_bot ConnectBotAssociation#lex_bot}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(lex_bot, dict):
            lex_bot = ConnectBotAssociationLexBot(**lex_bot)
        self._values: typing.Dict[str, typing.Any] = {
            "instance_id": instance_id,
            "lex_bot": lex_bot,
        }
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def instance_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_bot_association#instance_id ConnectBotAssociation#instance_id}.'''
        result = self._values.get("instance_id")
        assert result is not None, "Required property 'instance_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def lex_bot(self) -> "ConnectBotAssociationLexBot":
        '''lex_bot block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_bot_association#lex_bot ConnectBotAssociation#lex_bot}
        '''
        result = self._values.get("lex_bot")
        assert result is not None, "Required property 'lex_bot' is missing"
        return typing.cast("ConnectBotAssociationLexBot", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectBotAssociationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.connect.ConnectBotAssociationLexBot",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "lex_region": "lexRegion"},
)
class ConnectBotAssociationLexBot:
    def __init__(
        self,
        *,
        name: builtins.str,
        lex_region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_bot_association#name ConnectBotAssociation#name}.
        :param lex_region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_bot_association#lex_region ConnectBotAssociation#lex_region}.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if lex_region is not None:
            self._values["lex_region"] = lex_region

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_bot_association#name ConnectBotAssociation#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def lex_region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_bot_association#lex_region ConnectBotAssociation#lex_region}.'''
        result = self._values.get("lex_region")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectBotAssociationLexBot(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ConnectBotAssociationLexBotOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.connect.ConnectBotAssociationLexBotOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        is_single_item: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param is_single_item: True if this is a block, false if it's a list.
        '''
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, is_single_item])

    @jsii.member(jsii_name="resetLexRegion")
    def reset_lex_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLexRegion", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="lexRegionInput")
    def lex_region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lexRegionInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="lexRegion")
    def lex_region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lexRegion"))

    @lex_region.setter
    def lex_region(self, value: builtins.str) -> None:
        jsii.set(self, "lexRegion", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ConnectBotAssociationLexBot]:
        return typing.cast(typing.Optional[ConnectBotAssociationLexBot], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ConnectBotAssociationLexBot],
    ) -> None:
        jsii.set(self, "internalValue", value)


class ConnectContactFlow(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.connect.ConnectContactFlow",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow aws_connect_contact_flow}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        instance_id: builtins.str,
        name: builtins.str,
        content: typing.Optional[builtins.str] = None,
        content_hash: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        filename: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional["ConnectContactFlowTimeouts"] = None,
        type: typing.Optional[builtins.str] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow aws_connect_contact_flow} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow#instance_id ConnectContactFlow#instance_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow#name ConnectContactFlow#name}.
        :param content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow#content ConnectContactFlow#content}.
        :param content_hash: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow#content_hash ConnectContactFlow#content_hash}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow#description ConnectContactFlow#description}.
        :param filename: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow#filename ConnectContactFlow#filename}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow#tags ConnectContactFlow#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow#tags_all ConnectContactFlow#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow#timeouts ConnectContactFlow#timeouts}
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow#type ConnectContactFlow#type}.
        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        '''
        config = ConnectContactFlowConfig(
            instance_id=instance_id,
            name=name,
            content=content,
            content_hash=content_hash,
            description=description,
            filename=filename,
            tags=tags,
            tags_all=tags_all,
            timeouts=timeouts,
            type=type,
            count=count,
            depends_on=depends_on,
            lifecycle=lifecycle,
            provider=provider,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow#create ConnectContactFlow#create}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow#update ConnectContactFlow#update}.
        '''
        value = ConnectContactFlowTimeouts(create=create, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetContent")
    def reset_content(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContent", []))

    @jsii.member(jsii_name="resetContentHash")
    def reset_content_hash(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContentHash", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetFilename")
    def reset_filename(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilename", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="contactFlowId")
    def contact_flow_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contactFlowId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ConnectContactFlowTimeoutsOutputReference":
        return typing.cast("ConnectContactFlowTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="contentHashInput")
    def content_hash_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentHashInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="contentInput")
    def content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="filenameInput")
    def filename_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "filenameInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceIdInput")
    def instance_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceIdInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tagsAllInput")
    def tags_all_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsAllInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(self) -> typing.Optional["ConnectContactFlowTimeouts"]:
        return typing.cast(typing.Optional["ConnectContactFlowTimeouts"], jsii.get(self, "timeoutsInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        jsii.set(self, "content", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="contentHash")
    def content_hash(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentHash"))

    @content_hash.setter
    def content_hash(self, value: builtins.str) -> None:
        jsii.set(self, "contentHash", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="filename")
    def filename(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "filename"))

    @filename.setter
    def filename(self, value: builtins.str) -> None:
        jsii.set(self, "filename", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceId"))

    @instance_id.setter
    def instance_id(self, value: builtins.str) -> None:
        jsii.set(self, "instanceId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        jsii.set(self, "tags", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        jsii.set(self, "tagsAll", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        jsii.set(self, "type", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.connect.ConnectContactFlowConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "count": "count",
        "depends_on": "dependsOn",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "instance_id": "instanceId",
        "name": "name",
        "content": "content",
        "content_hash": "contentHash",
        "description": "description",
        "filename": "filename",
        "tags": "tags",
        "tags_all": "tagsAll",
        "timeouts": "timeouts",
        "type": "type",
    },
)
class ConnectContactFlowConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        instance_id: builtins.str,
        name: builtins.str,
        content: typing.Optional[builtins.str] = None,
        content_hash: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        filename: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional["ConnectContactFlowTimeouts"] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''AWS Connect.

        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        :param instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow#instance_id ConnectContactFlow#instance_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow#name ConnectContactFlow#name}.
        :param content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow#content ConnectContactFlow#content}.
        :param content_hash: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow#content_hash ConnectContactFlow#content_hash}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow#description ConnectContactFlow#description}.
        :param filename: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow#filename ConnectContactFlow#filename}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow#tags ConnectContactFlow#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow#tags_all ConnectContactFlow#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow#timeouts ConnectContactFlow#timeouts}
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow#type ConnectContactFlow#type}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = ConnectContactFlowTimeouts(**timeouts)
        self._values: typing.Dict[str, typing.Any] = {
            "instance_id": instance_id,
            "name": name,
        }
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if content is not None:
            self._values["content"] = content
        if content_hash is not None:
            self._values["content_hash"] = content_hash
        if description is not None:
            self._values["description"] = description
        if filename is not None:
            self._values["filename"] = filename
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def instance_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow#instance_id ConnectContactFlow#instance_id}.'''
        result = self._values.get("instance_id")
        assert result is not None, "Required property 'instance_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow#name ConnectContactFlow#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def content(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow#content ConnectContactFlow#content}.'''
        result = self._values.get("content")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def content_hash(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow#content_hash ConnectContactFlow#content_hash}.'''
        result = self._values.get("content_hash")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow#description ConnectContactFlow#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def filename(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow#filename ConnectContactFlow#filename}.'''
        result = self._values.get("filename")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow#tags ConnectContactFlow#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow#tags_all ConnectContactFlow#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ConnectContactFlowTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow#timeouts ConnectContactFlow#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ConnectContactFlowTimeouts"], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow#type ConnectContactFlow#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectContactFlowConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ConnectContactFlowModule(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.connect.ConnectContactFlowModule",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow_module aws_connect_contact_flow_module}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        instance_id: builtins.str,
        name: builtins.str,
        content: typing.Optional[builtins.str] = None,
        content_hash: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        filename: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow_module aws_connect_contact_flow_module} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow_module#instance_id ConnectContactFlowModule#instance_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow_module#name ConnectContactFlowModule#name}.
        :param content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow_module#content ConnectContactFlowModule#content}.
        :param content_hash: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow_module#content_hash ConnectContactFlowModule#content_hash}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow_module#description ConnectContactFlowModule#description}.
        :param filename: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow_module#filename ConnectContactFlowModule#filename}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow_module#tags ConnectContactFlowModule#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow_module#tags_all ConnectContactFlowModule#tags_all}.
        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        '''
        config = ConnectContactFlowModuleConfig(
            instance_id=instance_id,
            name=name,
            content=content,
            content_hash=content_hash,
            description=description,
            filename=filename,
            tags=tags,
            tags_all=tags_all,
            count=count,
            depends_on=depends_on,
            lifecycle=lifecycle,
            provider=provider,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetContent")
    def reset_content(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContent", []))

    @jsii.member(jsii_name="resetContentHash")
    def reset_content_hash(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContentHash", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetFilename")
    def reset_filename(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilename", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="contactFlowModuleId")
    def contact_flow_module_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contactFlowModuleId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="contentHashInput")
    def content_hash_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentHashInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="contentInput")
    def content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="filenameInput")
    def filename_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "filenameInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceIdInput")
    def instance_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceIdInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tagsAllInput")
    def tags_all_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsAllInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        jsii.set(self, "content", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="contentHash")
    def content_hash(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentHash"))

    @content_hash.setter
    def content_hash(self, value: builtins.str) -> None:
        jsii.set(self, "contentHash", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="filename")
    def filename(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "filename"))

    @filename.setter
    def filename(self, value: builtins.str) -> None:
        jsii.set(self, "filename", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceId"))

    @instance_id.setter
    def instance_id(self, value: builtins.str) -> None:
        jsii.set(self, "instanceId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        jsii.set(self, "tags", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.connect.ConnectContactFlowModuleConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "count": "count",
        "depends_on": "dependsOn",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "instance_id": "instanceId",
        "name": "name",
        "content": "content",
        "content_hash": "contentHash",
        "description": "description",
        "filename": "filename",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class ConnectContactFlowModuleConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        instance_id: builtins.str,
        name: builtins.str,
        content: typing.Optional[builtins.str] = None,
        content_hash: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        filename: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''AWS Connect.

        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        :param instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow_module#instance_id ConnectContactFlowModule#instance_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow_module#name ConnectContactFlowModule#name}.
        :param content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow_module#content ConnectContactFlowModule#content}.
        :param content_hash: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow_module#content_hash ConnectContactFlowModule#content_hash}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow_module#description ConnectContactFlowModule#description}.
        :param filename: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow_module#filename ConnectContactFlowModule#filename}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow_module#tags ConnectContactFlowModule#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow_module#tags_all ConnectContactFlowModule#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        self._values: typing.Dict[str, typing.Any] = {
            "instance_id": instance_id,
            "name": name,
        }
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if content is not None:
            self._values["content"] = content
        if content_hash is not None:
            self._values["content_hash"] = content_hash
        if description is not None:
            self._values["description"] = description
        if filename is not None:
            self._values["filename"] = filename
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def instance_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow_module#instance_id ConnectContactFlowModule#instance_id}.'''
        result = self._values.get("instance_id")
        assert result is not None, "Required property 'instance_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow_module#name ConnectContactFlowModule#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def content(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow_module#content ConnectContactFlowModule#content}.'''
        result = self._values.get("content")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def content_hash(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow_module#content_hash ConnectContactFlowModule#content_hash}.'''
        result = self._values.get("content_hash")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow_module#description ConnectContactFlowModule#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def filename(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow_module#filename ConnectContactFlowModule#filename}.'''
        result = self._values.get("filename")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow_module#tags ConnectContactFlowModule#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow_module#tags_all ConnectContactFlowModule#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectContactFlowModuleConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.connect.ConnectContactFlowTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "update": "update"},
)
class ConnectContactFlowTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow#create ConnectContactFlow#create}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow#update ConnectContactFlow#update}.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow#create ConnectContactFlow#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_contact_flow#update ConnectContactFlow#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectContactFlowTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ConnectContactFlowTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.connect.ConnectContactFlowTimeoutsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        is_single_item: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param is_single_item: True if this is a block, false if it's a list.
        '''
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, is_single_item])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="updateInput")
    def update_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        jsii.set(self, "create", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        jsii.set(self, "update", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ConnectContactFlowTimeouts]:
        return typing.cast(typing.Optional[ConnectContactFlowTimeouts], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ConnectContactFlowTimeouts],
    ) -> None:
        jsii.set(self, "internalValue", value)


class ConnectHoursOfOperation(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.connect.ConnectHoursOfOperation",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/connect_hours_of_operation aws_connect_hours_of_operation}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        config: typing.Union[cdktf.IResolvable, typing.Sequence["ConnectHoursOfOperationConfigA"]],
        instance_id: builtins.str,
        name: builtins.str,
        time_zone: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional["ConnectHoursOfOperationTimeouts"] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/connect_hours_of_operation aws_connect_hours_of_operation} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param config: config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_hours_of_operation#config ConnectHoursOfOperation#config}
        :param instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_hours_of_operation#instance_id ConnectHoursOfOperation#instance_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_hours_of_operation#name ConnectHoursOfOperation#name}.
        :param time_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_hours_of_operation#time_zone ConnectHoursOfOperation#time_zone}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_hours_of_operation#description ConnectHoursOfOperation#description}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_hours_of_operation#tags ConnectHoursOfOperation#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_hours_of_operation#tags_all ConnectHoursOfOperation#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_hours_of_operation#timeouts ConnectHoursOfOperation#timeouts}
        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        '''
        config_ = ConnectHoursOfOperationConfig(
            config=config,
            instance_id=instance_id,
            name=name,
            time_zone=time_zone,
            description=description,
            tags=tags,
            tags_all=tags_all,
            timeouts=timeouts,
            count=count,
            depends_on=depends_on,
            lifecycle=lifecycle,
            provider=provider,
        )

        jsii.create(self.__class__, self, [scope, id, config_])

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_hours_of_operation#create ConnectHoursOfOperation#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_hours_of_operation#delete ConnectHoursOfOperation#delete}.
        '''
        value = ConnectHoursOfOperationTimeouts(create=create, delete=delete)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="hoursOfOperationArn")
    def hours_of_operation_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hoursOfOperationArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="hoursOfOperationId")
    def hours_of_operation_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hoursOfOperationId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ConnectHoursOfOperationTimeoutsOutputReference":
        return typing.cast("ConnectHoursOfOperationTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="configInput")
    def config_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ConnectHoursOfOperationConfigA"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ConnectHoursOfOperationConfigA"]]], jsii.get(self, "configInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceIdInput")
    def instance_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceIdInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tagsAllInput")
    def tags_all_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsAllInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(self) -> typing.Optional["ConnectHoursOfOperationTimeouts"]:
        return typing.cast(typing.Optional["ConnectHoursOfOperationTimeouts"], jsii.get(self, "timeoutsInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="timeZoneInput")
    def time_zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeZoneInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="config")
    def config(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["ConnectHoursOfOperationConfigA"]]:
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["ConnectHoursOfOperationConfigA"]], jsii.get(self, "config"))

    @config.setter
    def config(
        self,
        value: typing.Union[cdktf.IResolvable, typing.List["ConnectHoursOfOperationConfigA"]],
    ) -> None:
        jsii.set(self, "config", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceId"))

    @instance_id.setter
    def instance_id(self, value: builtins.str) -> None:
        jsii.set(self, "instanceId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        jsii.set(self, "tags", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        jsii.set(self, "tagsAll", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="timeZone")
    def time_zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeZone"))

    @time_zone.setter
    def time_zone(self, value: builtins.str) -> None:
        jsii.set(self, "timeZone", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.connect.ConnectHoursOfOperationConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "count": "count",
        "depends_on": "dependsOn",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "config": "config",
        "instance_id": "instanceId",
        "name": "name",
        "time_zone": "timeZone",
        "description": "description",
        "tags": "tags",
        "tags_all": "tagsAll",
        "timeouts": "timeouts",
    },
)
class ConnectHoursOfOperationConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        config: typing.Union[cdktf.IResolvable, typing.Sequence["ConnectHoursOfOperationConfigA"]],
        instance_id: builtins.str,
        name: builtins.str,
        time_zone: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional["ConnectHoursOfOperationTimeouts"] = None,
    ) -> None:
        '''AWS Connect.

        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        :param config: config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_hours_of_operation#config ConnectHoursOfOperation#config}
        :param instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_hours_of_operation#instance_id ConnectHoursOfOperation#instance_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_hours_of_operation#name ConnectHoursOfOperation#name}.
        :param time_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_hours_of_operation#time_zone ConnectHoursOfOperation#time_zone}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_hours_of_operation#description ConnectHoursOfOperation#description}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_hours_of_operation#tags ConnectHoursOfOperation#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_hours_of_operation#tags_all ConnectHoursOfOperation#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_hours_of_operation#timeouts ConnectHoursOfOperation#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = ConnectHoursOfOperationTimeouts(**timeouts)
        self._values: typing.Dict[str, typing.Any] = {
            "config": config,
            "instance_id": instance_id,
            "name": name,
            "time_zone": time_zone,
        }
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if timeouts is not None:
            self._values["timeouts"] = timeouts

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def config(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["ConnectHoursOfOperationConfigA"]]:
        '''config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_hours_of_operation#config ConnectHoursOfOperation#config}
        '''
        result = self._values.get("config")
        assert result is not None, "Required property 'config' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["ConnectHoursOfOperationConfigA"]], result)

    @builtins.property
    def instance_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_hours_of_operation#instance_id ConnectHoursOfOperation#instance_id}.'''
        result = self._values.get("instance_id")
        assert result is not None, "Required property 'instance_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_hours_of_operation#name ConnectHoursOfOperation#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def time_zone(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_hours_of_operation#time_zone ConnectHoursOfOperation#time_zone}.'''
        result = self._values.get("time_zone")
        assert result is not None, "Required property 'time_zone' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_hours_of_operation#description ConnectHoursOfOperation#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_hours_of_operation#tags ConnectHoursOfOperation#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_hours_of_operation#tags_all ConnectHoursOfOperation#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ConnectHoursOfOperationTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_hours_of_operation#timeouts ConnectHoursOfOperation#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ConnectHoursOfOperationTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectHoursOfOperationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.connect.ConnectHoursOfOperationConfigA",
    jsii_struct_bases=[],
    name_mapping={"day": "day", "end_time": "endTime", "start_time": "startTime"},
)
class ConnectHoursOfOperationConfigA:
    def __init__(
        self,
        *,
        day: builtins.str,
        end_time: "ConnectHoursOfOperationConfigEndTime",
        start_time: "ConnectHoursOfOperationConfigStartTime",
    ) -> None:
        '''
        :param day: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_hours_of_operation#day ConnectHoursOfOperation#day}.
        :param end_time: end_time block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_hours_of_operation#end_time ConnectHoursOfOperation#end_time}
        :param start_time: start_time block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_hours_of_operation#start_time ConnectHoursOfOperation#start_time}
        '''
        if isinstance(end_time, dict):
            end_time = ConnectHoursOfOperationConfigEndTime(**end_time)
        if isinstance(start_time, dict):
            start_time = ConnectHoursOfOperationConfigStartTime(**start_time)
        self._values: typing.Dict[str, typing.Any] = {
            "day": day,
            "end_time": end_time,
            "start_time": start_time,
        }

    @builtins.property
    def day(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_hours_of_operation#day ConnectHoursOfOperation#day}.'''
        result = self._values.get("day")
        assert result is not None, "Required property 'day' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def end_time(self) -> "ConnectHoursOfOperationConfigEndTime":
        '''end_time block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_hours_of_operation#end_time ConnectHoursOfOperation#end_time}
        '''
        result = self._values.get("end_time")
        assert result is not None, "Required property 'end_time' is missing"
        return typing.cast("ConnectHoursOfOperationConfigEndTime", result)

    @builtins.property
    def start_time(self) -> "ConnectHoursOfOperationConfigStartTime":
        '''start_time block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_hours_of_operation#start_time ConnectHoursOfOperation#start_time}
        '''
        result = self._values.get("start_time")
        assert result is not None, "Required property 'start_time' is missing"
        return typing.cast("ConnectHoursOfOperationConfigStartTime", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectHoursOfOperationConfigA(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.connect.ConnectHoursOfOperationConfigEndTime",
    jsii_struct_bases=[],
    name_mapping={"hours": "hours", "minutes": "minutes"},
)
class ConnectHoursOfOperationConfigEndTime:
    def __init__(self, *, hours: jsii.Number, minutes: jsii.Number) -> None:
        '''
        :param hours: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_hours_of_operation#hours ConnectHoursOfOperation#hours}.
        :param minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_hours_of_operation#minutes ConnectHoursOfOperation#minutes}.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "hours": hours,
            "minutes": minutes,
        }

    @builtins.property
    def hours(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_hours_of_operation#hours ConnectHoursOfOperation#hours}.'''
        result = self._values.get("hours")
        assert result is not None, "Required property 'hours' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def minutes(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_hours_of_operation#minutes ConnectHoursOfOperation#minutes}.'''
        result = self._values.get("minutes")
        assert result is not None, "Required property 'minutes' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectHoursOfOperationConfigEndTime(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ConnectHoursOfOperationConfigEndTimeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.connect.ConnectHoursOfOperationConfigEndTimeOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        is_single_item: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param is_single_item: True if this is a block, false if it's a list.
        '''
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, is_single_item])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="hoursInput")
    def hours_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "hoursInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="minutesInput")
    def minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minutesInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="hours")
    def hours(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "hours"))

    @hours.setter
    def hours(self, value: jsii.Number) -> None:
        jsii.set(self, "hours", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="minutes")
    def minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minutes"))

    @minutes.setter
    def minutes(self, value: jsii.Number) -> None:
        jsii.set(self, "minutes", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ConnectHoursOfOperationConfigEndTime]:
        return typing.cast(typing.Optional[ConnectHoursOfOperationConfigEndTime], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ConnectHoursOfOperationConfigEndTime],
    ) -> None:
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.connect.ConnectHoursOfOperationConfigStartTime",
    jsii_struct_bases=[],
    name_mapping={"hours": "hours", "minutes": "minutes"},
)
class ConnectHoursOfOperationConfigStartTime:
    def __init__(self, *, hours: jsii.Number, minutes: jsii.Number) -> None:
        '''
        :param hours: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_hours_of_operation#hours ConnectHoursOfOperation#hours}.
        :param minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_hours_of_operation#minutes ConnectHoursOfOperation#minutes}.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "hours": hours,
            "minutes": minutes,
        }

    @builtins.property
    def hours(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_hours_of_operation#hours ConnectHoursOfOperation#hours}.'''
        result = self._values.get("hours")
        assert result is not None, "Required property 'hours' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def minutes(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_hours_of_operation#minutes ConnectHoursOfOperation#minutes}.'''
        result = self._values.get("minutes")
        assert result is not None, "Required property 'minutes' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectHoursOfOperationConfigStartTime(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ConnectHoursOfOperationConfigStartTimeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.connect.ConnectHoursOfOperationConfigStartTimeOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        is_single_item: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param is_single_item: True if this is a block, false if it's a list.
        '''
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, is_single_item])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="hoursInput")
    def hours_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "hoursInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="minutesInput")
    def minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minutesInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="hours")
    def hours(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "hours"))

    @hours.setter
    def hours(self, value: jsii.Number) -> None:
        jsii.set(self, "hours", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="minutes")
    def minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minutes"))

    @minutes.setter
    def minutes(self, value: jsii.Number) -> None:
        jsii.set(self, "minutes", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ConnectHoursOfOperationConfigStartTime]:
        return typing.cast(typing.Optional[ConnectHoursOfOperationConfigStartTime], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ConnectHoursOfOperationConfigStartTime],
    ) -> None:
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.connect.ConnectHoursOfOperationTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete"},
)
class ConnectHoursOfOperationTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_hours_of_operation#create ConnectHoursOfOperation#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_hours_of_operation#delete ConnectHoursOfOperation#delete}.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_hours_of_operation#create ConnectHoursOfOperation#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_hours_of_operation#delete ConnectHoursOfOperation#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectHoursOfOperationTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ConnectHoursOfOperationTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.connect.ConnectHoursOfOperationTimeoutsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        is_single_item: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param is_single_item: True if this is a block, false if it's a list.
        '''
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, is_single_item])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        jsii.set(self, "create", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        jsii.set(self, "delete", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ConnectHoursOfOperationTimeouts]:
        return typing.cast(typing.Optional[ConnectHoursOfOperationTimeouts], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ConnectHoursOfOperationTimeouts],
    ) -> None:
        jsii.set(self, "internalValue", value)


class ConnectInstance(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.connect.ConnectInstance",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/connect_instance aws_connect_instance}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        identity_management_type: builtins.str,
        inbound_calls_enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        outbound_calls_enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        auto_resolve_best_voices_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        contact_flow_logs_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        contact_lens_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        directory_id: typing.Optional[builtins.str] = None,
        early_media_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        instance_alias: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional["ConnectInstanceTimeouts"] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/connect_instance aws_connect_instance} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param identity_management_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance#identity_management_type ConnectInstance#identity_management_type}.
        :param inbound_calls_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance#inbound_calls_enabled ConnectInstance#inbound_calls_enabled}.
        :param outbound_calls_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance#outbound_calls_enabled ConnectInstance#outbound_calls_enabled}.
        :param auto_resolve_best_voices_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance#auto_resolve_best_voices_enabled ConnectInstance#auto_resolve_best_voices_enabled}.
        :param contact_flow_logs_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance#contact_flow_logs_enabled ConnectInstance#contact_flow_logs_enabled}.
        :param contact_lens_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance#contact_lens_enabled ConnectInstance#contact_lens_enabled}.
        :param directory_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance#directory_id ConnectInstance#directory_id}.
        :param early_media_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance#early_media_enabled ConnectInstance#early_media_enabled}.
        :param instance_alias: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance#instance_alias ConnectInstance#instance_alias}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance#timeouts ConnectInstance#timeouts}
        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        '''
        config = ConnectInstanceConfig(
            identity_management_type=identity_management_type,
            inbound_calls_enabled=inbound_calls_enabled,
            outbound_calls_enabled=outbound_calls_enabled,
            auto_resolve_best_voices_enabled=auto_resolve_best_voices_enabled,
            contact_flow_logs_enabled=contact_flow_logs_enabled,
            contact_lens_enabled=contact_lens_enabled,
            directory_id=directory_id,
            early_media_enabled=early_media_enabled,
            instance_alias=instance_alias,
            timeouts=timeouts,
            count=count,
            depends_on=depends_on,
            lifecycle=lifecycle,
            provider=provider,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance#create ConnectInstance#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance#delete ConnectInstance#delete}.
        '''
        value = ConnectInstanceTimeouts(create=create, delete=delete)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAutoResolveBestVoicesEnabled")
    def reset_auto_resolve_best_voices_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoResolveBestVoicesEnabled", []))

    @jsii.member(jsii_name="resetContactFlowLogsEnabled")
    def reset_contact_flow_logs_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContactFlowLogsEnabled", []))

    @jsii.member(jsii_name="resetContactLensEnabled")
    def reset_contact_lens_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContactLensEnabled", []))

    @jsii.member(jsii_name="resetDirectoryId")
    def reset_directory_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDirectoryId", []))

    @jsii.member(jsii_name="resetEarlyMediaEnabled")
    def reset_early_media_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEarlyMediaEnabled", []))

    @jsii.member(jsii_name="resetInstanceAlias")
    def reset_instance_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceAlias", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="createdTime")
    def created_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceRole")
    def service_role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceRole"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ConnectInstanceTimeoutsOutputReference":
        return typing.cast("ConnectInstanceTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="autoResolveBestVoicesEnabledInput")
    def auto_resolve_best_voices_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "autoResolveBestVoicesEnabledInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="contactFlowLogsEnabledInput")
    def contact_flow_logs_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "contactFlowLogsEnabledInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="contactLensEnabledInput")
    def contact_lens_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "contactLensEnabledInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="directoryIdInput")
    def directory_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "directoryIdInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="earlyMediaEnabledInput")
    def early_media_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "earlyMediaEnabledInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="identityManagementTypeInput")
    def identity_management_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityManagementTypeInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="inboundCallsEnabledInput")
    def inbound_calls_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "inboundCallsEnabledInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceAliasInput")
    def instance_alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceAliasInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="outboundCallsEnabledInput")
    def outbound_calls_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "outboundCallsEnabledInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(self) -> typing.Optional["ConnectInstanceTimeouts"]:
        return typing.cast(typing.Optional["ConnectInstanceTimeouts"], jsii.get(self, "timeoutsInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="autoResolveBestVoicesEnabled")
    def auto_resolve_best_voices_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "autoResolveBestVoicesEnabled"))

    @auto_resolve_best_voices_enabled.setter
    def auto_resolve_best_voices_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        jsii.set(self, "autoResolveBestVoicesEnabled", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="contactFlowLogsEnabled")
    def contact_flow_logs_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "contactFlowLogsEnabled"))

    @contact_flow_logs_enabled.setter
    def contact_flow_logs_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        jsii.set(self, "contactFlowLogsEnabled", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="contactLensEnabled")
    def contact_lens_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "contactLensEnabled"))

    @contact_lens_enabled.setter
    def contact_lens_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        jsii.set(self, "contactLensEnabled", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="directoryId")
    def directory_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "directoryId"))

    @directory_id.setter
    def directory_id(self, value: builtins.str) -> None:
        jsii.set(self, "directoryId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="earlyMediaEnabled")
    def early_media_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "earlyMediaEnabled"))

    @early_media_enabled.setter
    def early_media_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        jsii.set(self, "earlyMediaEnabled", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="identityManagementType")
    def identity_management_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityManagementType"))

    @identity_management_type.setter
    def identity_management_type(self, value: builtins.str) -> None:
        jsii.set(self, "identityManagementType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="inboundCallsEnabled")
    def inbound_calls_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "inboundCallsEnabled"))

    @inbound_calls_enabled.setter
    def inbound_calls_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        jsii.set(self, "inboundCallsEnabled", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceAlias")
    def instance_alias(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceAlias"))

    @instance_alias.setter
    def instance_alias(self, value: builtins.str) -> None:
        jsii.set(self, "instanceAlias", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="outboundCallsEnabled")
    def outbound_calls_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "outboundCallsEnabled"))

    @outbound_calls_enabled.setter
    def outbound_calls_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        jsii.set(self, "outboundCallsEnabled", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.connect.ConnectInstanceConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "count": "count",
        "depends_on": "dependsOn",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "identity_management_type": "identityManagementType",
        "inbound_calls_enabled": "inboundCallsEnabled",
        "outbound_calls_enabled": "outboundCallsEnabled",
        "auto_resolve_best_voices_enabled": "autoResolveBestVoicesEnabled",
        "contact_flow_logs_enabled": "contactFlowLogsEnabled",
        "contact_lens_enabled": "contactLensEnabled",
        "directory_id": "directoryId",
        "early_media_enabled": "earlyMediaEnabled",
        "instance_alias": "instanceAlias",
        "timeouts": "timeouts",
    },
)
class ConnectInstanceConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        identity_management_type: builtins.str,
        inbound_calls_enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        outbound_calls_enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        auto_resolve_best_voices_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        contact_flow_logs_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        contact_lens_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        directory_id: typing.Optional[builtins.str] = None,
        early_media_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        instance_alias: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional["ConnectInstanceTimeouts"] = None,
    ) -> None:
        '''AWS Connect.

        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        :param identity_management_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance#identity_management_type ConnectInstance#identity_management_type}.
        :param inbound_calls_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance#inbound_calls_enabled ConnectInstance#inbound_calls_enabled}.
        :param outbound_calls_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance#outbound_calls_enabled ConnectInstance#outbound_calls_enabled}.
        :param auto_resolve_best_voices_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance#auto_resolve_best_voices_enabled ConnectInstance#auto_resolve_best_voices_enabled}.
        :param contact_flow_logs_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance#contact_flow_logs_enabled ConnectInstance#contact_flow_logs_enabled}.
        :param contact_lens_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance#contact_lens_enabled ConnectInstance#contact_lens_enabled}.
        :param directory_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance#directory_id ConnectInstance#directory_id}.
        :param early_media_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance#early_media_enabled ConnectInstance#early_media_enabled}.
        :param instance_alias: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance#instance_alias ConnectInstance#instance_alias}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance#timeouts ConnectInstance#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = ConnectInstanceTimeouts(**timeouts)
        self._values: typing.Dict[str, typing.Any] = {
            "identity_management_type": identity_management_type,
            "inbound_calls_enabled": inbound_calls_enabled,
            "outbound_calls_enabled": outbound_calls_enabled,
        }
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if auto_resolve_best_voices_enabled is not None:
            self._values["auto_resolve_best_voices_enabled"] = auto_resolve_best_voices_enabled
        if contact_flow_logs_enabled is not None:
            self._values["contact_flow_logs_enabled"] = contact_flow_logs_enabled
        if contact_lens_enabled is not None:
            self._values["contact_lens_enabled"] = contact_lens_enabled
        if directory_id is not None:
            self._values["directory_id"] = directory_id
        if early_media_enabled is not None:
            self._values["early_media_enabled"] = early_media_enabled
        if instance_alias is not None:
            self._values["instance_alias"] = instance_alias
        if timeouts is not None:
            self._values["timeouts"] = timeouts

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def identity_management_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance#identity_management_type ConnectInstance#identity_management_type}.'''
        result = self._values.get("identity_management_type")
        assert result is not None, "Required property 'identity_management_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def inbound_calls_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance#inbound_calls_enabled ConnectInstance#inbound_calls_enabled}.'''
        result = self._values.get("inbound_calls_enabled")
        assert result is not None, "Required property 'inbound_calls_enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def outbound_calls_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance#outbound_calls_enabled ConnectInstance#outbound_calls_enabled}.'''
        result = self._values.get("outbound_calls_enabled")
        assert result is not None, "Required property 'outbound_calls_enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def auto_resolve_best_voices_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance#auto_resolve_best_voices_enabled ConnectInstance#auto_resolve_best_voices_enabled}.'''
        result = self._values.get("auto_resolve_best_voices_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def contact_flow_logs_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance#contact_flow_logs_enabled ConnectInstance#contact_flow_logs_enabled}.'''
        result = self._values.get("contact_flow_logs_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def contact_lens_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance#contact_lens_enabled ConnectInstance#contact_lens_enabled}.'''
        result = self._values.get("contact_lens_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def directory_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance#directory_id ConnectInstance#directory_id}.'''
        result = self._values.get("directory_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def early_media_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance#early_media_enabled ConnectInstance#early_media_enabled}.'''
        result = self._values.get("early_media_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def instance_alias(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance#instance_alias ConnectInstance#instance_alias}.'''
        result = self._values.get("instance_alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ConnectInstanceTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance#timeouts ConnectInstance#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ConnectInstanceTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectInstanceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.connect.ConnectInstanceTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete"},
)
class ConnectInstanceTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance#create ConnectInstance#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance#delete ConnectInstance#delete}.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance#create ConnectInstance#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance#delete ConnectInstance#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectInstanceTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ConnectInstanceTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.connect.ConnectInstanceTimeoutsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        is_single_item: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param is_single_item: True if this is a block, false if it's a list.
        '''
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, is_single_item])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        jsii.set(self, "create", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        jsii.set(self, "delete", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ConnectInstanceTimeouts]:
        return typing.cast(typing.Optional[ConnectInstanceTimeouts], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ConnectInstanceTimeouts]) -> None:
        jsii.set(self, "internalValue", value)


class ConnectLambdaFunctionAssociation(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.connect.ConnectLambdaFunctionAssociation",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/connect_lambda_function_association aws_connect_lambda_function_association}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        function_arn: builtins.str,
        instance_id: builtins.str,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/connect_lambda_function_association aws_connect_lambda_function_association} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param function_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_lambda_function_association#function_arn ConnectLambdaFunctionAssociation#function_arn}.
        :param instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_lambda_function_association#instance_id ConnectLambdaFunctionAssociation#instance_id}.
        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        '''
        config = ConnectLambdaFunctionAssociationConfig(
            function_arn=function_arn,
            instance_id=instance_id,
            count=count,
            depends_on=depends_on,
            lifecycle=lifecycle,
            provider=provider,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="functionArnInput")
    def function_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "functionArnInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceIdInput")
    def instance_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceIdInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="functionArn")
    def function_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "functionArn"))

    @function_arn.setter
    def function_arn(self, value: builtins.str) -> None:
        jsii.set(self, "functionArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceId"))

    @instance_id.setter
    def instance_id(self, value: builtins.str) -> None:
        jsii.set(self, "instanceId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.connect.ConnectLambdaFunctionAssociationConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "count": "count",
        "depends_on": "dependsOn",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "function_arn": "functionArn",
        "instance_id": "instanceId",
    },
)
class ConnectLambdaFunctionAssociationConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        function_arn: builtins.str,
        instance_id: builtins.str,
    ) -> None:
        '''AWS Connect.

        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        :param function_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_lambda_function_association#function_arn ConnectLambdaFunctionAssociation#function_arn}.
        :param instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_lambda_function_association#instance_id ConnectLambdaFunctionAssociation#instance_id}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        self._values: typing.Dict[str, typing.Any] = {
            "function_arn": function_arn,
            "instance_id": instance_id,
        }
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def function_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_lambda_function_association#function_arn ConnectLambdaFunctionAssociation#function_arn}.'''
        result = self._values.get("function_arn")
        assert result is not None, "Required property 'function_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_lambda_function_association#instance_id ConnectLambdaFunctionAssociation#instance_id}.'''
        result = self._values.get("instance_id")
        assert result is not None, "Required property 'instance_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectLambdaFunctionAssociationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ConnectQueue(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.connect.ConnectQueue",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/connect_queue aws_connect_queue}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        hours_of_operation_id: builtins.str,
        instance_id: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        max_contacts: typing.Optional[jsii.Number] = None,
        outbound_caller_config: typing.Optional["ConnectQueueOutboundCallerConfig"] = None,
        quick_connect_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/connect_queue aws_connect_queue} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param hours_of_operation_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_queue#hours_of_operation_id ConnectQueue#hours_of_operation_id}.
        :param instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_queue#instance_id ConnectQueue#instance_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_queue#name ConnectQueue#name}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_queue#description ConnectQueue#description}.
        :param max_contacts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_queue#max_contacts ConnectQueue#max_contacts}.
        :param outbound_caller_config: outbound_caller_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_queue#outbound_caller_config ConnectQueue#outbound_caller_config}
        :param quick_connect_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_queue#quick_connect_ids ConnectQueue#quick_connect_ids}.
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_queue#status ConnectQueue#status}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_queue#tags ConnectQueue#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_queue#tags_all ConnectQueue#tags_all}.
        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        '''
        config = ConnectQueueConfig(
            hours_of_operation_id=hours_of_operation_id,
            instance_id=instance_id,
            name=name,
            description=description,
            max_contacts=max_contacts,
            outbound_caller_config=outbound_caller_config,
            quick_connect_ids=quick_connect_ids,
            status=status,
            tags=tags,
            tags_all=tags_all,
            count=count,
            depends_on=depends_on,
            lifecycle=lifecycle,
            provider=provider,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="putOutboundCallerConfig")
    def put_outbound_caller_config(
        self,
        *,
        outbound_caller_id_name: typing.Optional[builtins.str] = None,
        outbound_caller_id_number_id: typing.Optional[builtins.str] = None,
        outbound_flow_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param outbound_caller_id_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_queue#outbound_caller_id_name ConnectQueue#outbound_caller_id_name}.
        :param outbound_caller_id_number_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_queue#outbound_caller_id_number_id ConnectQueue#outbound_caller_id_number_id}.
        :param outbound_flow_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_queue#outbound_flow_id ConnectQueue#outbound_flow_id}.
        '''
        value = ConnectQueueOutboundCallerConfig(
            outbound_caller_id_name=outbound_caller_id_name,
            outbound_caller_id_number_id=outbound_caller_id_number_id,
            outbound_flow_id=outbound_flow_id,
        )

        return typing.cast(None, jsii.invoke(self, "putOutboundCallerConfig", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetMaxContacts")
    def reset_max_contacts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxContacts", []))

    @jsii.member(jsii_name="resetOutboundCallerConfig")
    def reset_outbound_caller_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOutboundCallerConfig", []))

    @jsii.member(jsii_name="resetQuickConnectIds")
    def reset_quick_connect_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQuickConnectIds", []))

    @jsii.member(jsii_name="resetStatus")
    def reset_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatus", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="outboundCallerConfig")
    def outbound_caller_config(
        self,
    ) -> "ConnectQueueOutboundCallerConfigOutputReference":
        return typing.cast("ConnectQueueOutboundCallerConfigOutputReference", jsii.get(self, "outboundCallerConfig"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="queueId")
    def queue_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "queueId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="hoursOfOperationIdInput")
    def hours_of_operation_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hoursOfOperationIdInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceIdInput")
    def instance_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceIdInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="maxContactsInput")
    def max_contacts_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxContactsInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="outboundCallerConfigInput")
    def outbound_caller_config_input(
        self,
    ) -> typing.Optional["ConnectQueueOutboundCallerConfig"]:
        return typing.cast(typing.Optional["ConnectQueueOutboundCallerConfig"], jsii.get(self, "outboundCallerConfigInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="quickConnectIdsInput")
    def quick_connect_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "quickConnectIdsInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tagsAllInput")
    def tags_all_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsAllInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="hoursOfOperationId")
    def hours_of_operation_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hoursOfOperationId"))

    @hours_of_operation_id.setter
    def hours_of_operation_id(self, value: builtins.str) -> None:
        jsii.set(self, "hoursOfOperationId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceId"))

    @instance_id.setter
    def instance_id(self, value: builtins.str) -> None:
        jsii.set(self, "instanceId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="maxContacts")
    def max_contacts(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxContacts"))

    @max_contacts.setter
    def max_contacts(self, value: jsii.Number) -> None:
        jsii.set(self, "maxContacts", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="quickConnectIds")
    def quick_connect_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "quickConnectIds"))

    @quick_connect_ids.setter
    def quick_connect_ids(self, value: typing.List[builtins.str]) -> None:
        jsii.set(self, "quickConnectIds", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        jsii.set(self, "status", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        jsii.set(self, "tags", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.connect.ConnectQueueConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "count": "count",
        "depends_on": "dependsOn",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "hours_of_operation_id": "hoursOfOperationId",
        "instance_id": "instanceId",
        "name": "name",
        "description": "description",
        "max_contacts": "maxContacts",
        "outbound_caller_config": "outboundCallerConfig",
        "quick_connect_ids": "quickConnectIds",
        "status": "status",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class ConnectQueueConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        hours_of_operation_id: builtins.str,
        instance_id: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        max_contacts: typing.Optional[jsii.Number] = None,
        outbound_caller_config: typing.Optional["ConnectQueueOutboundCallerConfig"] = None,
        quick_connect_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''AWS Connect.

        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        :param hours_of_operation_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_queue#hours_of_operation_id ConnectQueue#hours_of_operation_id}.
        :param instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_queue#instance_id ConnectQueue#instance_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_queue#name ConnectQueue#name}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_queue#description ConnectQueue#description}.
        :param max_contacts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_queue#max_contacts ConnectQueue#max_contacts}.
        :param outbound_caller_config: outbound_caller_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_queue#outbound_caller_config ConnectQueue#outbound_caller_config}
        :param quick_connect_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_queue#quick_connect_ids ConnectQueue#quick_connect_ids}.
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_queue#status ConnectQueue#status}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_queue#tags ConnectQueue#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_queue#tags_all ConnectQueue#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(outbound_caller_config, dict):
            outbound_caller_config = ConnectQueueOutboundCallerConfig(**outbound_caller_config)
        self._values: typing.Dict[str, typing.Any] = {
            "hours_of_operation_id": hours_of_operation_id,
            "instance_id": instance_id,
            "name": name,
        }
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if description is not None:
            self._values["description"] = description
        if max_contacts is not None:
            self._values["max_contacts"] = max_contacts
        if outbound_caller_config is not None:
            self._values["outbound_caller_config"] = outbound_caller_config
        if quick_connect_ids is not None:
            self._values["quick_connect_ids"] = quick_connect_ids
        if status is not None:
            self._values["status"] = status
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def hours_of_operation_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_queue#hours_of_operation_id ConnectQueue#hours_of_operation_id}.'''
        result = self._values.get("hours_of_operation_id")
        assert result is not None, "Required property 'hours_of_operation_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_queue#instance_id ConnectQueue#instance_id}.'''
        result = self._values.get("instance_id")
        assert result is not None, "Required property 'instance_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_queue#name ConnectQueue#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_queue#description ConnectQueue#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_contacts(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_queue#max_contacts ConnectQueue#max_contacts}.'''
        result = self._values.get("max_contacts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def outbound_caller_config(
        self,
    ) -> typing.Optional["ConnectQueueOutboundCallerConfig"]:
        '''outbound_caller_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_queue#outbound_caller_config ConnectQueue#outbound_caller_config}
        '''
        result = self._values.get("outbound_caller_config")
        return typing.cast(typing.Optional["ConnectQueueOutboundCallerConfig"], result)

    @builtins.property
    def quick_connect_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_queue#quick_connect_ids ConnectQueue#quick_connect_ids}.'''
        result = self._values.get("quick_connect_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_queue#status ConnectQueue#status}.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_queue#tags ConnectQueue#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_queue#tags_all ConnectQueue#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectQueueConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.connect.ConnectQueueOutboundCallerConfig",
    jsii_struct_bases=[],
    name_mapping={
        "outbound_caller_id_name": "outboundCallerIdName",
        "outbound_caller_id_number_id": "outboundCallerIdNumberId",
        "outbound_flow_id": "outboundFlowId",
    },
)
class ConnectQueueOutboundCallerConfig:
    def __init__(
        self,
        *,
        outbound_caller_id_name: typing.Optional[builtins.str] = None,
        outbound_caller_id_number_id: typing.Optional[builtins.str] = None,
        outbound_flow_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param outbound_caller_id_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_queue#outbound_caller_id_name ConnectQueue#outbound_caller_id_name}.
        :param outbound_caller_id_number_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_queue#outbound_caller_id_number_id ConnectQueue#outbound_caller_id_number_id}.
        :param outbound_flow_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_queue#outbound_flow_id ConnectQueue#outbound_flow_id}.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if outbound_caller_id_name is not None:
            self._values["outbound_caller_id_name"] = outbound_caller_id_name
        if outbound_caller_id_number_id is not None:
            self._values["outbound_caller_id_number_id"] = outbound_caller_id_number_id
        if outbound_flow_id is not None:
            self._values["outbound_flow_id"] = outbound_flow_id

    @builtins.property
    def outbound_caller_id_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_queue#outbound_caller_id_name ConnectQueue#outbound_caller_id_name}.'''
        result = self._values.get("outbound_caller_id_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def outbound_caller_id_number_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_queue#outbound_caller_id_number_id ConnectQueue#outbound_caller_id_number_id}.'''
        result = self._values.get("outbound_caller_id_number_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def outbound_flow_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_queue#outbound_flow_id ConnectQueue#outbound_flow_id}.'''
        result = self._values.get("outbound_flow_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectQueueOutboundCallerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ConnectQueueOutboundCallerConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.connect.ConnectQueueOutboundCallerConfigOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        is_single_item: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param is_single_item: True if this is a block, false if it's a list.
        '''
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, is_single_item])

    @jsii.member(jsii_name="resetOutboundCallerIdName")
    def reset_outbound_caller_id_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOutboundCallerIdName", []))

    @jsii.member(jsii_name="resetOutboundCallerIdNumberId")
    def reset_outbound_caller_id_number_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOutboundCallerIdNumberId", []))

    @jsii.member(jsii_name="resetOutboundFlowId")
    def reset_outbound_flow_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOutboundFlowId", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="outboundCallerIdNameInput")
    def outbound_caller_id_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "outboundCallerIdNameInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="outboundCallerIdNumberIdInput")
    def outbound_caller_id_number_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "outboundCallerIdNumberIdInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="outboundFlowIdInput")
    def outbound_flow_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "outboundFlowIdInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="outboundCallerIdName")
    def outbound_caller_id_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "outboundCallerIdName"))

    @outbound_caller_id_name.setter
    def outbound_caller_id_name(self, value: builtins.str) -> None:
        jsii.set(self, "outboundCallerIdName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="outboundCallerIdNumberId")
    def outbound_caller_id_number_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "outboundCallerIdNumberId"))

    @outbound_caller_id_number_id.setter
    def outbound_caller_id_number_id(self, value: builtins.str) -> None:
        jsii.set(self, "outboundCallerIdNumberId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="outboundFlowId")
    def outbound_flow_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "outboundFlowId"))

    @outbound_flow_id.setter
    def outbound_flow_id(self, value: builtins.str) -> None:
        jsii.set(self, "outboundFlowId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ConnectQueueOutboundCallerConfig]:
        return typing.cast(typing.Optional[ConnectQueueOutboundCallerConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ConnectQueueOutboundCallerConfig],
    ) -> None:
        jsii.set(self, "internalValue", value)


class ConnectQuickConnect(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.connect.ConnectQuickConnect",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/connect_quick_connect aws_connect_quick_connect}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        instance_id: builtins.str,
        name: builtins.str,
        quick_connect_config: "ConnectQuickConnectQuickConnectConfig",
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/connect_quick_connect aws_connect_quick_connect} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_quick_connect#instance_id ConnectQuickConnect#instance_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_quick_connect#name ConnectQuickConnect#name}.
        :param quick_connect_config: quick_connect_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_quick_connect#quick_connect_config ConnectQuickConnect#quick_connect_config}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_quick_connect#description ConnectQuickConnect#description}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_quick_connect#tags ConnectQuickConnect#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_quick_connect#tags_all ConnectQuickConnect#tags_all}.
        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        '''
        config = ConnectQuickConnectConfig(
            instance_id=instance_id,
            name=name,
            quick_connect_config=quick_connect_config,
            description=description,
            tags=tags,
            tags_all=tags_all,
            count=count,
            depends_on=depends_on,
            lifecycle=lifecycle,
            provider=provider,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="putQuickConnectConfig")
    def put_quick_connect_config(
        self,
        *,
        quick_connect_type: builtins.str,
        phone_config: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence["ConnectQuickConnectQuickConnectConfigPhoneConfig"]]] = None,
        queue_config: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence["ConnectQuickConnectQuickConnectConfigQueueConfig"]]] = None,
        user_config: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence["ConnectQuickConnectQuickConnectConfigUserConfig"]]] = None,
    ) -> None:
        '''
        :param quick_connect_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_quick_connect#quick_connect_type ConnectQuickConnect#quick_connect_type}.
        :param phone_config: phone_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_quick_connect#phone_config ConnectQuickConnect#phone_config}
        :param queue_config: queue_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_quick_connect#queue_config ConnectQuickConnect#queue_config}
        :param user_config: user_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_quick_connect#user_config ConnectQuickConnect#user_config}
        '''
        value = ConnectQuickConnectQuickConnectConfig(
            quick_connect_type=quick_connect_type,
            phone_config=phone_config,
            queue_config=queue_config,
            user_config=user_config,
        )

        return typing.cast(None, jsii.invoke(self, "putQuickConnectConfig", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="quickConnectConfig")
    def quick_connect_config(
        self,
    ) -> "ConnectQuickConnectQuickConnectConfigOutputReference":
        return typing.cast("ConnectQuickConnectQuickConnectConfigOutputReference", jsii.get(self, "quickConnectConfig"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="quickConnectId")
    def quick_connect_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "quickConnectId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceIdInput")
    def instance_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceIdInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="quickConnectConfigInput")
    def quick_connect_config_input(
        self,
    ) -> typing.Optional["ConnectQuickConnectQuickConnectConfig"]:
        return typing.cast(typing.Optional["ConnectQuickConnectQuickConnectConfig"], jsii.get(self, "quickConnectConfigInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tagsAllInput")
    def tags_all_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsAllInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceId"))

    @instance_id.setter
    def instance_id(self, value: builtins.str) -> None:
        jsii.set(self, "instanceId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        jsii.set(self, "tags", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.connect.ConnectQuickConnectConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "count": "count",
        "depends_on": "dependsOn",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "instance_id": "instanceId",
        "name": "name",
        "quick_connect_config": "quickConnectConfig",
        "description": "description",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class ConnectQuickConnectConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        instance_id: builtins.str,
        name: builtins.str,
        quick_connect_config: "ConnectQuickConnectQuickConnectConfig",
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''AWS Connect.

        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        :param instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_quick_connect#instance_id ConnectQuickConnect#instance_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_quick_connect#name ConnectQuickConnect#name}.
        :param quick_connect_config: quick_connect_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_quick_connect#quick_connect_config ConnectQuickConnect#quick_connect_config}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_quick_connect#description ConnectQuickConnect#description}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_quick_connect#tags ConnectQuickConnect#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_quick_connect#tags_all ConnectQuickConnect#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(quick_connect_config, dict):
            quick_connect_config = ConnectQuickConnectQuickConnectConfig(**quick_connect_config)
        self._values: typing.Dict[str, typing.Any] = {
            "instance_id": instance_id,
            "name": name,
            "quick_connect_config": quick_connect_config,
        }
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def instance_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_quick_connect#instance_id ConnectQuickConnect#instance_id}.'''
        result = self._values.get("instance_id")
        assert result is not None, "Required property 'instance_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_quick_connect#name ConnectQuickConnect#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def quick_connect_config(self) -> "ConnectQuickConnectQuickConnectConfig":
        '''quick_connect_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_quick_connect#quick_connect_config ConnectQuickConnect#quick_connect_config}
        '''
        result = self._values.get("quick_connect_config")
        assert result is not None, "Required property 'quick_connect_config' is missing"
        return typing.cast("ConnectQuickConnectQuickConnectConfig", result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_quick_connect#description ConnectQuickConnect#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_quick_connect#tags ConnectQuickConnect#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_quick_connect#tags_all ConnectQuickConnect#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectQuickConnectConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.connect.ConnectQuickConnectQuickConnectConfig",
    jsii_struct_bases=[],
    name_mapping={
        "quick_connect_type": "quickConnectType",
        "phone_config": "phoneConfig",
        "queue_config": "queueConfig",
        "user_config": "userConfig",
    },
)
class ConnectQuickConnectQuickConnectConfig:
    def __init__(
        self,
        *,
        quick_connect_type: builtins.str,
        phone_config: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence["ConnectQuickConnectQuickConnectConfigPhoneConfig"]]] = None,
        queue_config: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence["ConnectQuickConnectQuickConnectConfigQueueConfig"]]] = None,
        user_config: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence["ConnectQuickConnectQuickConnectConfigUserConfig"]]] = None,
    ) -> None:
        '''
        :param quick_connect_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_quick_connect#quick_connect_type ConnectQuickConnect#quick_connect_type}.
        :param phone_config: phone_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_quick_connect#phone_config ConnectQuickConnect#phone_config}
        :param queue_config: queue_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_quick_connect#queue_config ConnectQuickConnect#queue_config}
        :param user_config: user_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_quick_connect#user_config ConnectQuickConnect#user_config}
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "quick_connect_type": quick_connect_type,
        }
        if phone_config is not None:
            self._values["phone_config"] = phone_config
        if queue_config is not None:
            self._values["queue_config"] = queue_config
        if user_config is not None:
            self._values["user_config"] = user_config

    @builtins.property
    def quick_connect_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_quick_connect#quick_connect_type ConnectQuickConnect#quick_connect_type}.'''
        result = self._values.get("quick_connect_type")
        assert result is not None, "Required property 'quick_connect_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def phone_config(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ConnectQuickConnectQuickConnectConfigPhoneConfig"]]]:
        '''phone_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_quick_connect#phone_config ConnectQuickConnect#phone_config}
        '''
        result = self._values.get("phone_config")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ConnectQuickConnectQuickConnectConfigPhoneConfig"]]], result)

    @builtins.property
    def queue_config(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ConnectQuickConnectQuickConnectConfigQueueConfig"]]]:
        '''queue_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_quick_connect#queue_config ConnectQuickConnect#queue_config}
        '''
        result = self._values.get("queue_config")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ConnectQuickConnectQuickConnectConfigQueueConfig"]]], result)

    @builtins.property
    def user_config(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ConnectQuickConnectQuickConnectConfigUserConfig"]]]:
        '''user_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_quick_connect#user_config ConnectQuickConnect#user_config}
        '''
        result = self._values.get("user_config")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ConnectQuickConnectQuickConnectConfigUserConfig"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectQuickConnectQuickConnectConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ConnectQuickConnectQuickConnectConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.connect.ConnectQuickConnectQuickConnectConfigOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        is_single_item: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param is_single_item: True if this is a block, false if it's a list.
        '''
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, is_single_item])

    @jsii.member(jsii_name="resetPhoneConfig")
    def reset_phone_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPhoneConfig", []))

    @jsii.member(jsii_name="resetQueueConfig")
    def reset_queue_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueueConfig", []))

    @jsii.member(jsii_name="resetUserConfig")
    def reset_user_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserConfig", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="phoneConfigInput")
    def phone_config_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ConnectQuickConnectQuickConnectConfigPhoneConfig"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ConnectQuickConnectQuickConnectConfigPhoneConfig"]]], jsii.get(self, "phoneConfigInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="queueConfigInput")
    def queue_config_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ConnectQuickConnectQuickConnectConfigQueueConfig"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ConnectQuickConnectQuickConnectConfigQueueConfig"]]], jsii.get(self, "queueConfigInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="quickConnectTypeInput")
    def quick_connect_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "quickConnectTypeInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="userConfigInput")
    def user_config_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ConnectQuickConnectQuickConnectConfigUserConfig"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ConnectQuickConnectQuickConnectConfigUserConfig"]]], jsii.get(self, "userConfigInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="phoneConfig")
    def phone_config(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["ConnectQuickConnectQuickConnectConfigPhoneConfig"]]:
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["ConnectQuickConnectQuickConnectConfigPhoneConfig"]], jsii.get(self, "phoneConfig"))

    @phone_config.setter
    def phone_config(
        self,
        value: typing.Union[cdktf.IResolvable, typing.List["ConnectQuickConnectQuickConnectConfigPhoneConfig"]],
    ) -> None:
        jsii.set(self, "phoneConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="queueConfig")
    def queue_config(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["ConnectQuickConnectQuickConnectConfigQueueConfig"]]:
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["ConnectQuickConnectQuickConnectConfigQueueConfig"]], jsii.get(self, "queueConfig"))

    @queue_config.setter
    def queue_config(
        self,
        value: typing.Union[cdktf.IResolvable, typing.List["ConnectQuickConnectQuickConnectConfigQueueConfig"]],
    ) -> None:
        jsii.set(self, "queueConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="quickConnectType")
    def quick_connect_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "quickConnectType"))

    @quick_connect_type.setter
    def quick_connect_type(self, value: builtins.str) -> None:
        jsii.set(self, "quickConnectType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="userConfig")
    def user_config(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["ConnectQuickConnectQuickConnectConfigUserConfig"]]:
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["ConnectQuickConnectQuickConnectConfigUserConfig"]], jsii.get(self, "userConfig"))

    @user_config.setter
    def user_config(
        self,
        value: typing.Union[cdktf.IResolvable, typing.List["ConnectQuickConnectQuickConnectConfigUserConfig"]],
    ) -> None:
        jsii.set(self, "userConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ConnectQuickConnectQuickConnectConfig]:
        return typing.cast(typing.Optional[ConnectQuickConnectQuickConnectConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ConnectQuickConnectQuickConnectConfig],
    ) -> None:
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.connect.ConnectQuickConnectQuickConnectConfigPhoneConfig",
    jsii_struct_bases=[],
    name_mapping={"phone_number": "phoneNumber"},
)
class ConnectQuickConnectQuickConnectConfigPhoneConfig:
    def __init__(self, *, phone_number: builtins.str) -> None:
        '''
        :param phone_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_quick_connect#phone_number ConnectQuickConnect#phone_number}.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "phone_number": phone_number,
        }

    @builtins.property
    def phone_number(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_quick_connect#phone_number ConnectQuickConnect#phone_number}.'''
        result = self._values.get("phone_number")
        assert result is not None, "Required property 'phone_number' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectQuickConnectQuickConnectConfigPhoneConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.connect.ConnectQuickConnectQuickConnectConfigQueueConfig",
    jsii_struct_bases=[],
    name_mapping={"contact_flow_id": "contactFlowId", "queue_id": "queueId"},
)
class ConnectQuickConnectQuickConnectConfigQueueConfig:
    def __init__(
        self,
        *,
        contact_flow_id: builtins.str,
        queue_id: builtins.str,
    ) -> None:
        '''
        :param contact_flow_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_quick_connect#contact_flow_id ConnectQuickConnect#contact_flow_id}.
        :param queue_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_quick_connect#queue_id ConnectQuickConnect#queue_id}.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "contact_flow_id": contact_flow_id,
            "queue_id": queue_id,
        }

    @builtins.property
    def contact_flow_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_quick_connect#contact_flow_id ConnectQuickConnect#contact_flow_id}.'''
        result = self._values.get("contact_flow_id")
        assert result is not None, "Required property 'contact_flow_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def queue_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_quick_connect#queue_id ConnectQuickConnect#queue_id}.'''
        result = self._values.get("queue_id")
        assert result is not None, "Required property 'queue_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectQuickConnectQuickConnectConfigQueueConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.connect.ConnectQuickConnectQuickConnectConfigUserConfig",
    jsii_struct_bases=[],
    name_mapping={"contact_flow_id": "contactFlowId", "user_id": "userId"},
)
class ConnectQuickConnectQuickConnectConfigUserConfig:
    def __init__(self, *, contact_flow_id: builtins.str, user_id: builtins.str) -> None:
        '''
        :param contact_flow_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_quick_connect#contact_flow_id ConnectQuickConnect#contact_flow_id}.
        :param user_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_quick_connect#user_id ConnectQuickConnect#user_id}.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "contact_flow_id": contact_flow_id,
            "user_id": user_id,
        }

    @builtins.property
    def contact_flow_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_quick_connect#contact_flow_id ConnectQuickConnect#contact_flow_id}.'''
        result = self._values.get("contact_flow_id")
        assert result is not None, "Required property 'contact_flow_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_quick_connect#user_id ConnectQuickConnect#user_id}.'''
        result = self._values.get("user_id")
        assert result is not None, "Required property 'user_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectQuickConnectQuickConnectConfigUserConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ConnectSecurityProfile(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.connect.ConnectSecurityProfile",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/connect_security_profile aws_connect_security_profile}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        instance_id: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        permissions: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/connect_security_profile aws_connect_security_profile} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_security_profile#instance_id ConnectSecurityProfile#instance_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_security_profile#name ConnectSecurityProfile#name}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_security_profile#description ConnectSecurityProfile#description}.
        :param permissions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_security_profile#permissions ConnectSecurityProfile#permissions}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_security_profile#tags ConnectSecurityProfile#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_security_profile#tags_all ConnectSecurityProfile#tags_all}.
        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        '''
        config = ConnectSecurityProfileConfig(
            instance_id=instance_id,
            name=name,
            description=description,
            permissions=permissions,
            tags=tags,
            tags_all=tags_all,
            count=count,
            depends_on=depends_on,
            lifecycle=lifecycle,
            provider=provider,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetPermissions")
    def reset_permissions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPermissions", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="organizationResourceId")
    def organization_resource_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "organizationResourceId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="securityProfileId")
    def security_profile_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "securityProfileId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceIdInput")
    def instance_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceIdInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="permissionsInput")
    def permissions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "permissionsInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tagsAllInput")
    def tags_all_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsAllInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceId"))

    @instance_id.setter
    def instance_id(self, value: builtins.str) -> None:
        jsii.set(self, "instanceId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="permissions")
    def permissions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "permissions"))

    @permissions.setter
    def permissions(self, value: typing.List[builtins.str]) -> None:
        jsii.set(self, "permissions", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        jsii.set(self, "tags", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.connect.ConnectSecurityProfileConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "count": "count",
        "depends_on": "dependsOn",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "instance_id": "instanceId",
        "name": "name",
        "description": "description",
        "permissions": "permissions",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class ConnectSecurityProfileConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        instance_id: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        permissions: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''AWS Connect.

        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        :param instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_security_profile#instance_id ConnectSecurityProfile#instance_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_security_profile#name ConnectSecurityProfile#name}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_security_profile#description ConnectSecurityProfile#description}.
        :param permissions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_security_profile#permissions ConnectSecurityProfile#permissions}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_security_profile#tags ConnectSecurityProfile#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_security_profile#tags_all ConnectSecurityProfile#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        self._values: typing.Dict[str, typing.Any] = {
            "instance_id": instance_id,
            "name": name,
        }
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if description is not None:
            self._values["description"] = description
        if permissions is not None:
            self._values["permissions"] = permissions
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def instance_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_security_profile#instance_id ConnectSecurityProfile#instance_id}.'''
        result = self._values.get("instance_id")
        assert result is not None, "Required property 'instance_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_security_profile#name ConnectSecurityProfile#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_security_profile#description ConnectSecurityProfile#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def permissions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_security_profile#permissions ConnectSecurityProfile#permissions}.'''
        result = self._values.get("permissions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_security_profile#tags ConnectSecurityProfile#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_security_profile#tags_all ConnectSecurityProfile#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectSecurityProfileConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsConnectBotAssociation(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.connect.DataAwsConnectBotAssociation",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/d/connect_bot_association aws_connect_bot_association}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        instance_id: builtins.str,
        lex_bot: "DataAwsConnectBotAssociationLexBot",
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/d/connect_bot_association aws_connect_bot_association} Data Source.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_bot_association#instance_id DataAwsConnectBotAssociation#instance_id}.
        :param lex_bot: lex_bot block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_bot_association#lex_bot DataAwsConnectBotAssociation#lex_bot}
        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        '''
        config = DataAwsConnectBotAssociationConfig(
            instance_id=instance_id,
            lex_bot=lex_bot,
            count=count,
            depends_on=depends_on,
            lifecycle=lifecycle,
            provider=provider,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="putLexBot")
    def put_lex_bot(
        self,
        *,
        name: builtins.str,
        lex_region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_bot_association#name DataAwsConnectBotAssociation#name}.
        :param lex_region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_bot_association#lex_region DataAwsConnectBotAssociation#lex_region}.
        '''
        value = DataAwsConnectBotAssociationLexBot(name=name, lex_region=lex_region)

        return typing.cast(None, jsii.invoke(self, "putLexBot", [value]))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="lexBot")
    def lex_bot(self) -> "DataAwsConnectBotAssociationLexBotOutputReference":
        return typing.cast("DataAwsConnectBotAssociationLexBotOutputReference", jsii.get(self, "lexBot"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceIdInput")
    def instance_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceIdInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="lexBotInput")
    def lex_bot_input(self) -> typing.Optional["DataAwsConnectBotAssociationLexBot"]:
        return typing.cast(typing.Optional["DataAwsConnectBotAssociationLexBot"], jsii.get(self, "lexBotInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceId"))

    @instance_id.setter
    def instance_id(self, value: builtins.str) -> None:
        jsii.set(self, "instanceId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.connect.DataAwsConnectBotAssociationConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "count": "count",
        "depends_on": "dependsOn",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "instance_id": "instanceId",
        "lex_bot": "lexBot",
    },
)
class DataAwsConnectBotAssociationConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        instance_id: builtins.str,
        lex_bot: "DataAwsConnectBotAssociationLexBot",
    ) -> None:
        '''AWS Connect.

        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        :param instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_bot_association#instance_id DataAwsConnectBotAssociation#instance_id}.
        :param lex_bot: lex_bot block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_bot_association#lex_bot DataAwsConnectBotAssociation#lex_bot}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(lex_bot, dict):
            lex_bot = DataAwsConnectBotAssociationLexBot(**lex_bot)
        self._values: typing.Dict[str, typing.Any] = {
            "instance_id": instance_id,
            "lex_bot": lex_bot,
        }
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def instance_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_bot_association#instance_id DataAwsConnectBotAssociation#instance_id}.'''
        result = self._values.get("instance_id")
        assert result is not None, "Required property 'instance_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def lex_bot(self) -> "DataAwsConnectBotAssociationLexBot":
        '''lex_bot block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_bot_association#lex_bot DataAwsConnectBotAssociation#lex_bot}
        '''
        result = self._values.get("lex_bot")
        assert result is not None, "Required property 'lex_bot' is missing"
        return typing.cast("DataAwsConnectBotAssociationLexBot", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsConnectBotAssociationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.connect.DataAwsConnectBotAssociationLexBot",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "lex_region": "lexRegion"},
)
class DataAwsConnectBotAssociationLexBot:
    def __init__(
        self,
        *,
        name: builtins.str,
        lex_region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_bot_association#name DataAwsConnectBotAssociation#name}.
        :param lex_region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_bot_association#lex_region DataAwsConnectBotAssociation#lex_region}.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if lex_region is not None:
            self._values["lex_region"] = lex_region

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_bot_association#name DataAwsConnectBotAssociation#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def lex_region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_bot_association#lex_region DataAwsConnectBotAssociation#lex_region}.'''
        result = self._values.get("lex_region")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsConnectBotAssociationLexBot(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsConnectBotAssociationLexBotOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.connect.DataAwsConnectBotAssociationLexBotOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        is_single_item: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param is_single_item: True if this is a block, false if it's a list.
        '''
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, is_single_item])

    @jsii.member(jsii_name="resetLexRegion")
    def reset_lex_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLexRegion", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="lexRegionInput")
    def lex_region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lexRegionInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="lexRegion")
    def lex_region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lexRegion"))

    @lex_region.setter
    def lex_region(self, value: builtins.str) -> None:
        jsii.set(self, "lexRegion", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataAwsConnectBotAssociationLexBot]:
        return typing.cast(typing.Optional[DataAwsConnectBotAssociationLexBot], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsConnectBotAssociationLexBot],
    ) -> None:
        jsii.set(self, "internalValue", value)


class DataAwsConnectContactFlow(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.connect.DataAwsConnectContactFlow",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/d/connect_contact_flow aws_connect_contact_flow}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        instance_id: builtins.str,
        contact_flow_id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        type: typing.Optional[builtins.str] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/d/connect_contact_flow aws_connect_contact_flow} Data Source.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_contact_flow#instance_id DataAwsConnectContactFlow#instance_id}.
        :param contact_flow_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_contact_flow#contact_flow_id DataAwsConnectContactFlow#contact_flow_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_contact_flow#name DataAwsConnectContactFlow#name}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_contact_flow#tags DataAwsConnectContactFlow#tags}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_contact_flow#type DataAwsConnectContactFlow#type}.
        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        '''
        config = DataAwsConnectContactFlowConfig(
            instance_id=instance_id,
            contact_flow_id=contact_flow_id,
            name=name,
            tags=tags,
            type=type,
            count=count,
            depends_on=depends_on,
            lifecycle=lifecycle,
            provider=provider,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetContactFlowId")
    def reset_contact_flow_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContactFlowId", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="contactFlowIdInput")
    def contact_flow_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contactFlowIdInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceIdInput")
    def instance_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceIdInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="contactFlowId")
    def contact_flow_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contactFlowId"))

    @contact_flow_id.setter
    def contact_flow_id(self, value: builtins.str) -> None:
        jsii.set(self, "contactFlowId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceId"))

    @instance_id.setter
    def instance_id(self, value: builtins.str) -> None:
        jsii.set(self, "instanceId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        jsii.set(self, "tags", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        jsii.set(self, "type", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.connect.DataAwsConnectContactFlowConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "count": "count",
        "depends_on": "dependsOn",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "instance_id": "instanceId",
        "contact_flow_id": "contactFlowId",
        "name": "name",
        "tags": "tags",
        "type": "type",
    },
)
class DataAwsConnectContactFlowConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        instance_id: builtins.str,
        contact_flow_id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''AWS Connect.

        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        :param instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_contact_flow#instance_id DataAwsConnectContactFlow#instance_id}.
        :param contact_flow_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_contact_flow#contact_flow_id DataAwsConnectContactFlow#contact_flow_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_contact_flow#name DataAwsConnectContactFlow#name}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_contact_flow#tags DataAwsConnectContactFlow#tags}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_contact_flow#type DataAwsConnectContactFlow#type}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        self._values: typing.Dict[str, typing.Any] = {
            "instance_id": instance_id,
        }
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if contact_flow_id is not None:
            self._values["contact_flow_id"] = contact_flow_id
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def instance_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_contact_flow#instance_id DataAwsConnectContactFlow#instance_id}.'''
        result = self._values.get("instance_id")
        assert result is not None, "Required property 'instance_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def contact_flow_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_contact_flow#contact_flow_id DataAwsConnectContactFlow#contact_flow_id}.'''
        result = self._values.get("contact_flow_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_contact_flow#name DataAwsConnectContactFlow#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_contact_flow#tags DataAwsConnectContactFlow#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_contact_flow#type DataAwsConnectContactFlow#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsConnectContactFlowConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsConnectContactFlowModule(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.connect.DataAwsConnectContactFlowModule",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/d/connect_contact_flow_module aws_connect_contact_flow_module}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        instance_id: builtins.str,
        contact_flow_module_id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/d/connect_contact_flow_module aws_connect_contact_flow_module} Data Source.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_contact_flow_module#instance_id DataAwsConnectContactFlowModule#instance_id}.
        :param contact_flow_module_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_contact_flow_module#contact_flow_module_id DataAwsConnectContactFlowModule#contact_flow_module_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_contact_flow_module#name DataAwsConnectContactFlowModule#name}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_contact_flow_module#tags DataAwsConnectContactFlowModule#tags}.
        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        '''
        config = DataAwsConnectContactFlowModuleConfig(
            instance_id=instance_id,
            contact_flow_module_id=contact_flow_module_id,
            name=name,
            tags=tags,
            count=count,
            depends_on=depends_on,
            lifecycle=lifecycle,
            provider=provider,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetContactFlowModuleId")
    def reset_contact_flow_module_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContactFlowModuleId", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="contactFlowModuleIdInput")
    def contact_flow_module_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contactFlowModuleIdInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceIdInput")
    def instance_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceIdInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="contactFlowModuleId")
    def contact_flow_module_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contactFlowModuleId"))

    @contact_flow_module_id.setter
    def contact_flow_module_id(self, value: builtins.str) -> None:
        jsii.set(self, "contactFlowModuleId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceId"))

    @instance_id.setter
    def instance_id(self, value: builtins.str) -> None:
        jsii.set(self, "instanceId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.connect.DataAwsConnectContactFlowModuleConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "count": "count",
        "depends_on": "dependsOn",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "instance_id": "instanceId",
        "contact_flow_module_id": "contactFlowModuleId",
        "name": "name",
        "tags": "tags",
    },
)
class DataAwsConnectContactFlowModuleConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        instance_id: builtins.str,
        contact_flow_module_id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''AWS Connect.

        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        :param instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_contact_flow_module#instance_id DataAwsConnectContactFlowModule#instance_id}.
        :param contact_flow_module_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_contact_flow_module#contact_flow_module_id DataAwsConnectContactFlowModule#contact_flow_module_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_contact_flow_module#name DataAwsConnectContactFlowModule#name}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_contact_flow_module#tags DataAwsConnectContactFlowModule#tags}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        self._values: typing.Dict[str, typing.Any] = {
            "instance_id": instance_id,
        }
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if contact_flow_module_id is not None:
            self._values["contact_flow_module_id"] = contact_flow_module_id
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def instance_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_contact_flow_module#instance_id DataAwsConnectContactFlowModule#instance_id}.'''
        result = self._values.get("instance_id")
        assert result is not None, "Required property 'instance_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def contact_flow_module_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_contact_flow_module#contact_flow_module_id DataAwsConnectContactFlowModule#contact_flow_module_id}.'''
        result = self._values.get("contact_flow_module_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_contact_flow_module#name DataAwsConnectContactFlowModule#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_contact_flow_module#tags DataAwsConnectContactFlowModule#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsConnectContactFlowModuleConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsConnectHoursOfOperation(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.connect.DataAwsConnectHoursOfOperation",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/d/connect_hours_of_operation aws_connect_hours_of_operation}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        instance_id: builtins.str,
        hours_of_operation_id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/d/connect_hours_of_operation aws_connect_hours_of_operation} Data Source.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_hours_of_operation#instance_id DataAwsConnectHoursOfOperation#instance_id}.
        :param hours_of_operation_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_hours_of_operation#hours_of_operation_id DataAwsConnectHoursOfOperation#hours_of_operation_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_hours_of_operation#name DataAwsConnectHoursOfOperation#name}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_hours_of_operation#tags DataAwsConnectHoursOfOperation#tags}.
        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        '''
        config = DataAwsConnectHoursOfOperationConfig(
            instance_id=instance_id,
            hours_of_operation_id=hours_of_operation_id,
            name=name,
            tags=tags,
            count=count,
            depends_on=depends_on,
            lifecycle=lifecycle,
            provider=provider,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="config")
    def config(self, index: builtins.str) -> "DataAwsConnectHoursOfOperationConfigA":
        '''
        :param index: -
        '''
        return typing.cast("DataAwsConnectHoursOfOperationConfigA", jsii.invoke(self, "config", [index]))

    @jsii.member(jsii_name="resetHoursOfOperationId")
    def reset_hours_of_operation_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHoursOfOperationId", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="hoursOfOperationArn")
    def hours_of_operation_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hoursOfOperationArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="timeZone")
    def time_zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeZone"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="hoursOfOperationIdInput")
    def hours_of_operation_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hoursOfOperationIdInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceIdInput")
    def instance_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceIdInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="hoursOfOperationId")
    def hours_of_operation_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hoursOfOperationId"))

    @hours_of_operation_id.setter
    def hours_of_operation_id(self, value: builtins.str) -> None:
        jsii.set(self, "hoursOfOperationId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceId"))

    @instance_id.setter
    def instance_id(self, value: builtins.str) -> None:
        jsii.set(self, "instanceId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.connect.DataAwsConnectHoursOfOperationConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "count": "count",
        "depends_on": "dependsOn",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "instance_id": "instanceId",
        "hours_of_operation_id": "hoursOfOperationId",
        "name": "name",
        "tags": "tags",
    },
)
class DataAwsConnectHoursOfOperationConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        instance_id: builtins.str,
        hours_of_operation_id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''AWS Connect.

        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        :param instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_hours_of_operation#instance_id DataAwsConnectHoursOfOperation#instance_id}.
        :param hours_of_operation_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_hours_of_operation#hours_of_operation_id DataAwsConnectHoursOfOperation#hours_of_operation_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_hours_of_operation#name DataAwsConnectHoursOfOperation#name}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_hours_of_operation#tags DataAwsConnectHoursOfOperation#tags}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        self._values: typing.Dict[str, typing.Any] = {
            "instance_id": instance_id,
        }
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if hours_of_operation_id is not None:
            self._values["hours_of_operation_id"] = hours_of_operation_id
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def instance_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_hours_of_operation#instance_id DataAwsConnectHoursOfOperation#instance_id}.'''
        result = self._values.get("instance_id")
        assert result is not None, "Required property 'instance_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def hours_of_operation_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_hours_of_operation#hours_of_operation_id DataAwsConnectHoursOfOperation#hours_of_operation_id}.'''
        result = self._values.get("hours_of_operation_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_hours_of_operation#name DataAwsConnectHoursOfOperation#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_hours_of_operation#tags DataAwsConnectHoursOfOperation#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsConnectHoursOfOperationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsConnectHoursOfOperationConfigA(
    cdktf.ComplexComputedList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.connect.DataAwsConnectHoursOfOperationConfigA",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_computed_list_index: builtins.str,
        wraps_set: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param terraform_resource: -
        :param terraform_attribute: -
        :param complex_computed_list_index: -
        :param wraps_set: -

        :stability: experimental
        '''
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_computed_list_index, wraps_set])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="day")
    def day(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "day"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="endTime")
    def end_time(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "endTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="startTime")
    def start_time(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "startTime"))


class DataAwsConnectHoursOfOperationConfigEndTime(
    cdktf.ComplexComputedList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.connect.DataAwsConnectHoursOfOperationConfigEndTime",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_computed_list_index: builtins.str,
        wraps_set: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param terraform_resource: -
        :param terraform_attribute: -
        :param complex_computed_list_index: -
        :param wraps_set: -

        :stability: experimental
        '''
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_computed_list_index, wraps_set])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="hours")
    def hours(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "hours"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="minutes")
    def minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minutes"))


class DataAwsConnectHoursOfOperationConfigStartTime(
    cdktf.ComplexComputedList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.connect.DataAwsConnectHoursOfOperationConfigStartTime",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_computed_list_index: builtins.str,
        wraps_set: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param terraform_resource: -
        :param terraform_attribute: -
        :param complex_computed_list_index: -
        :param wraps_set: -

        :stability: experimental
        '''
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_computed_list_index, wraps_set])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="hours")
    def hours(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "hours"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="minutes")
    def minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minutes"))


class DataAwsConnectInstance(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.connect.DataAwsConnectInstance",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/d/connect_instance aws_connect_instance}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        instance_alias: typing.Optional[builtins.str] = None,
        instance_id: typing.Optional[builtins.str] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/d/connect_instance aws_connect_instance} Data Source.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param instance_alias: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_instance#instance_alias DataAwsConnectInstance#instance_alias}.
        :param instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_instance#instance_id DataAwsConnectInstance#instance_id}.
        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        '''
        config = DataAwsConnectInstanceConfig(
            instance_alias=instance_alias,
            instance_id=instance_id,
            count=count,
            depends_on=depends_on,
            lifecycle=lifecycle,
            provider=provider,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetInstanceAlias")
    def reset_instance_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceAlias", []))

    @jsii.member(jsii_name="resetInstanceId")
    def reset_instance_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="autoResolveBestVoicesEnabled")
    def auto_resolve_best_voices_enabled(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "autoResolveBestVoicesEnabled"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="contactFlowLogsEnabled")
    def contact_flow_logs_enabled(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "contactFlowLogsEnabled"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="contactLensEnabled")
    def contact_lens_enabled(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "contactLensEnabled"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="createdTime")
    def created_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="earlyMediaEnabled")
    def early_media_enabled(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "earlyMediaEnabled"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="identityManagementType")
    def identity_management_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityManagementType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="inboundCallsEnabled")
    def inbound_calls_enabled(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "inboundCallsEnabled"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="outboundCallsEnabled")
    def outbound_calls_enabled(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "outboundCallsEnabled"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceRole")
    def service_role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceRole"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceAliasInput")
    def instance_alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceAliasInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceIdInput")
    def instance_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceIdInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceAlias")
    def instance_alias(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceAlias"))

    @instance_alias.setter
    def instance_alias(self, value: builtins.str) -> None:
        jsii.set(self, "instanceAlias", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceId"))

    @instance_id.setter
    def instance_id(self, value: builtins.str) -> None:
        jsii.set(self, "instanceId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.connect.DataAwsConnectInstanceConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "count": "count",
        "depends_on": "dependsOn",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "instance_alias": "instanceAlias",
        "instance_id": "instanceId",
    },
)
class DataAwsConnectInstanceConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        instance_alias: typing.Optional[builtins.str] = None,
        instance_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''AWS Connect.

        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        :param instance_alias: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_instance#instance_alias DataAwsConnectInstance#instance_alias}.
        :param instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_instance#instance_id DataAwsConnectInstance#instance_id}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        self._values: typing.Dict[str, typing.Any] = {}
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if instance_alias is not None:
            self._values["instance_alias"] = instance_alias
        if instance_id is not None:
            self._values["instance_id"] = instance_id

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def instance_alias(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_instance#instance_alias DataAwsConnectInstance#instance_alias}.'''
        result = self._values.get("instance_alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_instance#instance_id DataAwsConnectInstance#instance_id}.'''
        result = self._values.get("instance_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsConnectInstanceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsConnectLambdaFunctionAssociation(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.connect.DataAwsConnectLambdaFunctionAssociation",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/d/connect_lambda_function_association aws_connect_lambda_function_association}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        function_arn: builtins.str,
        instance_id: builtins.str,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/d/connect_lambda_function_association aws_connect_lambda_function_association} Data Source.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param function_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_lambda_function_association#function_arn DataAwsConnectLambdaFunctionAssociation#function_arn}.
        :param instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_lambda_function_association#instance_id DataAwsConnectLambdaFunctionAssociation#instance_id}.
        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        '''
        config = DataAwsConnectLambdaFunctionAssociationConfig(
            function_arn=function_arn,
            instance_id=instance_id,
            count=count,
            depends_on=depends_on,
            lifecycle=lifecycle,
            provider=provider,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="functionArnInput")
    def function_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "functionArnInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceIdInput")
    def instance_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceIdInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="functionArn")
    def function_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "functionArn"))

    @function_arn.setter
    def function_arn(self, value: builtins.str) -> None:
        jsii.set(self, "functionArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceId"))

    @instance_id.setter
    def instance_id(self, value: builtins.str) -> None:
        jsii.set(self, "instanceId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.connect.DataAwsConnectLambdaFunctionAssociationConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "count": "count",
        "depends_on": "dependsOn",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "function_arn": "functionArn",
        "instance_id": "instanceId",
    },
)
class DataAwsConnectLambdaFunctionAssociationConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        function_arn: builtins.str,
        instance_id: builtins.str,
    ) -> None:
        '''AWS Connect.

        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        :param function_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_lambda_function_association#function_arn DataAwsConnectLambdaFunctionAssociation#function_arn}.
        :param instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_lambda_function_association#instance_id DataAwsConnectLambdaFunctionAssociation#instance_id}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        self._values: typing.Dict[str, typing.Any] = {
            "function_arn": function_arn,
            "instance_id": instance_id,
        }
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def function_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_lambda_function_association#function_arn DataAwsConnectLambdaFunctionAssociation#function_arn}.'''
        result = self._values.get("function_arn")
        assert result is not None, "Required property 'function_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_lambda_function_association#instance_id DataAwsConnectLambdaFunctionAssociation#instance_id}.'''
        result = self._values.get("instance_id")
        assert result is not None, "Required property 'instance_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsConnectLambdaFunctionAssociationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsConnectPrompt(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.connect.DataAwsConnectPrompt",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/d/connect_prompt aws_connect_prompt}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        instance_id: builtins.str,
        name: builtins.str,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/d/connect_prompt aws_connect_prompt} Data Source.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_prompt#instance_id DataAwsConnectPrompt#instance_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_prompt#name DataAwsConnectPrompt#name}.
        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        '''
        config = DataAwsConnectPromptConfig(
            instance_id=instance_id,
            name=name,
            count=count,
            depends_on=depends_on,
            lifecycle=lifecycle,
            provider=provider,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="promptId")
    def prompt_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "promptId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceIdInput")
    def instance_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceIdInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceId"))

    @instance_id.setter
    def instance_id(self, value: builtins.str) -> None:
        jsii.set(self, "instanceId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.connect.DataAwsConnectPromptConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "count": "count",
        "depends_on": "dependsOn",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "instance_id": "instanceId",
        "name": "name",
    },
)
class DataAwsConnectPromptConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        instance_id: builtins.str,
        name: builtins.str,
    ) -> None:
        '''AWS Connect.

        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        :param instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_prompt#instance_id DataAwsConnectPrompt#instance_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_prompt#name DataAwsConnectPrompt#name}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        self._values: typing.Dict[str, typing.Any] = {
            "instance_id": instance_id,
            "name": name,
        }
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def instance_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_prompt#instance_id DataAwsConnectPrompt#instance_id}.'''
        result = self._values.get("instance_id")
        assert result is not None, "Required property 'instance_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_prompt#name DataAwsConnectPrompt#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsConnectPromptConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsConnectQuickConnect(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.connect.DataAwsConnectQuickConnect",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/d/connect_quick_connect aws_connect_quick_connect}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        instance_id: builtins.str,
        name: typing.Optional[builtins.str] = None,
        quick_connect_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/d/connect_quick_connect aws_connect_quick_connect} Data Source.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_quick_connect#instance_id DataAwsConnectQuickConnect#instance_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_quick_connect#name DataAwsConnectQuickConnect#name}.
        :param quick_connect_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_quick_connect#quick_connect_id DataAwsConnectQuickConnect#quick_connect_id}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_quick_connect#tags DataAwsConnectQuickConnect#tags}.
        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        '''
        config = DataAwsConnectQuickConnectConfig(
            instance_id=instance_id,
            name=name,
            quick_connect_id=quick_connect_id,
            tags=tags,
            count=count,
            depends_on=depends_on,
            lifecycle=lifecycle,
            provider=provider,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="quickConnectConfig")
    def quick_connect_config(
        self,
        index: builtins.str,
    ) -> "DataAwsConnectQuickConnectQuickConnectConfig":
        '''
        :param index: -
        '''
        return typing.cast("DataAwsConnectQuickConnectQuickConnectConfig", jsii.invoke(self, "quickConnectConfig", [index]))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetQuickConnectId")
    def reset_quick_connect_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQuickConnectId", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceIdInput")
    def instance_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceIdInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="quickConnectIdInput")
    def quick_connect_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "quickConnectIdInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceId"))

    @instance_id.setter
    def instance_id(self, value: builtins.str) -> None:
        jsii.set(self, "instanceId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="quickConnectId")
    def quick_connect_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "quickConnectId"))

    @quick_connect_id.setter
    def quick_connect_id(self, value: builtins.str) -> None:
        jsii.set(self, "quickConnectId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.connect.DataAwsConnectQuickConnectConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "count": "count",
        "depends_on": "dependsOn",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "instance_id": "instanceId",
        "name": "name",
        "quick_connect_id": "quickConnectId",
        "tags": "tags",
    },
)
class DataAwsConnectQuickConnectConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        lifecycle: typing.Optional[cdktf.TerraformResourceLifecycle] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        instance_id: builtins.str,
        name: typing.Optional[builtins.str] = None,
        quick_connect_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''AWS Connect.

        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        :param instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_quick_connect#instance_id DataAwsConnectQuickConnect#instance_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_quick_connect#name DataAwsConnectQuickConnect#name}.
        :param quick_connect_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_quick_connect#quick_connect_id DataAwsConnectQuickConnect#quick_connect_id}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_quick_connect#tags DataAwsConnectQuickConnect#tags}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        self._values: typing.Dict[str, typing.Any] = {
            "instance_id": instance_id,
        }
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if name is not None:
            self._values["name"] = name
        if quick_connect_id is not None:
            self._values["quick_connect_id"] = quick_connect_id
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def instance_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_quick_connect#instance_id DataAwsConnectQuickConnect#instance_id}.'''
        result = self._values.get("instance_id")
        assert result is not None, "Required property 'instance_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_quick_connect#name DataAwsConnectQuickConnect#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def quick_connect_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_quick_connect#quick_connect_id DataAwsConnectQuickConnect#quick_connect_id}.'''
        result = self._values.get("quick_connect_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/connect_quick_connect#tags DataAwsConnectQuickConnect#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsConnectQuickConnectConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsConnectQuickConnectQuickConnectConfig(
    cdktf.ComplexComputedList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.connect.DataAwsConnectQuickConnectQuickConnectConfig",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_computed_list_index: builtins.str,
        wraps_set: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param terraform_resource: -
        :param terraform_attribute: -
        :param complex_computed_list_index: -
        :param wraps_set: -

        :stability: experimental
        '''
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_computed_list_index, wraps_set])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="phoneConfig")
    def phone_config(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "phoneConfig"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="queueConfig")
    def queue_config(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "queueConfig"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="quickConnectType")
    def quick_connect_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "quickConnectType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="userConfig")
    def user_config(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "userConfig"))


class DataAwsConnectQuickConnectQuickConnectConfigPhoneConfig(
    cdktf.ComplexComputedList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.connect.DataAwsConnectQuickConnectQuickConnectConfigPhoneConfig",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_computed_list_index: builtins.str,
        wraps_set: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param terraform_resource: -
        :param terraform_attribute: -
        :param complex_computed_list_index: -
        :param wraps_set: -

        :stability: experimental
        '''
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_computed_list_index, wraps_set])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="phoneNumber")
    def phone_number(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "phoneNumber"))


class DataAwsConnectQuickConnectQuickConnectConfigQueueConfig(
    cdktf.ComplexComputedList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.connect.DataAwsConnectQuickConnectQuickConnectConfigQueueConfig",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_computed_list_index: builtins.str,
        wraps_set: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param terraform_resource: -
        :param terraform_attribute: -
        :param complex_computed_list_index: -
        :param wraps_set: -

        :stability: experimental
        '''
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_computed_list_index, wraps_set])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="contactFlowId")
    def contact_flow_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contactFlowId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="queueId")
    def queue_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "queueId"))


class DataAwsConnectQuickConnectQuickConnectConfigUserConfig(
    cdktf.ComplexComputedList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.connect.DataAwsConnectQuickConnectQuickConnectConfigUserConfig",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_computed_list_index: builtins.str,
        wraps_set: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param terraform_resource: -
        :param terraform_attribute: -
        :param complex_computed_list_index: -
        :param wraps_set: -

        :stability: experimental
        '''
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_computed_list_index, wraps_set])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="contactFlowId")
    def contact_flow_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contactFlowId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="userId")
    def user_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userId"))


__all__ = [
    "ConnectBotAssociation",
    "ConnectBotAssociationConfig",
    "ConnectBotAssociationLexBot",
    "ConnectBotAssociationLexBotOutputReference",
    "ConnectContactFlow",
    "ConnectContactFlowConfig",
    "ConnectContactFlowModule",
    "ConnectContactFlowModuleConfig",
    "ConnectContactFlowTimeouts",
    "ConnectContactFlowTimeoutsOutputReference",
    "ConnectHoursOfOperation",
    "ConnectHoursOfOperationConfig",
    "ConnectHoursOfOperationConfigA",
    "ConnectHoursOfOperationConfigEndTime",
    "ConnectHoursOfOperationConfigEndTimeOutputReference",
    "ConnectHoursOfOperationConfigStartTime",
    "ConnectHoursOfOperationConfigStartTimeOutputReference",
    "ConnectHoursOfOperationTimeouts",
    "ConnectHoursOfOperationTimeoutsOutputReference",
    "ConnectInstance",
    "ConnectInstanceConfig",
    "ConnectInstanceTimeouts",
    "ConnectInstanceTimeoutsOutputReference",
    "ConnectLambdaFunctionAssociation",
    "ConnectLambdaFunctionAssociationConfig",
    "ConnectQueue",
    "ConnectQueueConfig",
    "ConnectQueueOutboundCallerConfig",
    "ConnectQueueOutboundCallerConfigOutputReference",
    "ConnectQuickConnect",
    "ConnectQuickConnectConfig",
    "ConnectQuickConnectQuickConnectConfig",
    "ConnectQuickConnectQuickConnectConfigOutputReference",
    "ConnectQuickConnectQuickConnectConfigPhoneConfig",
    "ConnectQuickConnectQuickConnectConfigQueueConfig",
    "ConnectQuickConnectQuickConnectConfigUserConfig",
    "ConnectSecurityProfile",
    "ConnectSecurityProfileConfig",
    "DataAwsConnectBotAssociation",
    "DataAwsConnectBotAssociationConfig",
    "DataAwsConnectBotAssociationLexBot",
    "DataAwsConnectBotAssociationLexBotOutputReference",
    "DataAwsConnectContactFlow",
    "DataAwsConnectContactFlowConfig",
    "DataAwsConnectContactFlowModule",
    "DataAwsConnectContactFlowModuleConfig",
    "DataAwsConnectHoursOfOperation",
    "DataAwsConnectHoursOfOperationConfig",
    "DataAwsConnectHoursOfOperationConfigA",
    "DataAwsConnectHoursOfOperationConfigEndTime",
    "DataAwsConnectHoursOfOperationConfigStartTime",
    "DataAwsConnectInstance",
    "DataAwsConnectInstanceConfig",
    "DataAwsConnectLambdaFunctionAssociation",
    "DataAwsConnectLambdaFunctionAssociationConfig",
    "DataAwsConnectPrompt",
    "DataAwsConnectPromptConfig",
    "DataAwsConnectQuickConnect",
    "DataAwsConnectQuickConnectConfig",
    "DataAwsConnectQuickConnectQuickConnectConfig",
    "DataAwsConnectQuickConnectQuickConnectConfigPhoneConfig",
    "DataAwsConnectQuickConnectQuickConnectConfigQueueConfig",
    "DataAwsConnectQuickConnectQuickConnectConfigUserConfig",
]

publication.publish()
