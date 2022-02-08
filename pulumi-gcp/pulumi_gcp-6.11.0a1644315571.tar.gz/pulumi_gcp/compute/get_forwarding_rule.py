# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetForwardingRuleResult',
    'AwaitableGetForwardingRuleResult',
    'get_forwarding_rule',
    'get_forwarding_rule_output',
]

@pulumi.output_type
class GetForwardingRuleResult:
    """
    A collection of values returned by getForwardingRule.
    """
    def __init__(__self__, all_ports=None, allow_global_access=None, backend_service=None, creation_timestamp=None, description=None, id=None, ip_address=None, ip_protocol=None, is_mirroring_collector=None, label_fingerprint=None, labels=None, load_balancing_scheme=None, name=None, network=None, network_tier=None, port_range=None, ports=None, project=None, region=None, self_link=None, service_label=None, service_name=None, subnetwork=None, target=None):
        if all_ports and not isinstance(all_ports, bool):
            raise TypeError("Expected argument 'all_ports' to be a bool")
        pulumi.set(__self__, "all_ports", all_ports)
        if allow_global_access and not isinstance(allow_global_access, bool):
            raise TypeError("Expected argument 'allow_global_access' to be a bool")
        pulumi.set(__self__, "allow_global_access", allow_global_access)
        if backend_service and not isinstance(backend_service, str):
            raise TypeError("Expected argument 'backend_service' to be a str")
        pulumi.set(__self__, "backend_service", backend_service)
        if creation_timestamp and not isinstance(creation_timestamp, str):
            raise TypeError("Expected argument 'creation_timestamp' to be a str")
        pulumi.set(__self__, "creation_timestamp", creation_timestamp)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ip_address and not isinstance(ip_address, str):
            raise TypeError("Expected argument 'ip_address' to be a str")
        pulumi.set(__self__, "ip_address", ip_address)
        if ip_protocol and not isinstance(ip_protocol, str):
            raise TypeError("Expected argument 'ip_protocol' to be a str")
        pulumi.set(__self__, "ip_protocol", ip_protocol)
        if is_mirroring_collector and not isinstance(is_mirroring_collector, bool):
            raise TypeError("Expected argument 'is_mirroring_collector' to be a bool")
        pulumi.set(__self__, "is_mirroring_collector", is_mirroring_collector)
        if label_fingerprint and not isinstance(label_fingerprint, str):
            raise TypeError("Expected argument 'label_fingerprint' to be a str")
        pulumi.set(__self__, "label_fingerprint", label_fingerprint)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if load_balancing_scheme and not isinstance(load_balancing_scheme, str):
            raise TypeError("Expected argument 'load_balancing_scheme' to be a str")
        pulumi.set(__self__, "load_balancing_scheme", load_balancing_scheme)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network and not isinstance(network, str):
            raise TypeError("Expected argument 'network' to be a str")
        pulumi.set(__self__, "network", network)
        if network_tier and not isinstance(network_tier, str):
            raise TypeError("Expected argument 'network_tier' to be a str")
        pulumi.set(__self__, "network_tier", network_tier)
        if port_range and not isinstance(port_range, str):
            raise TypeError("Expected argument 'port_range' to be a str")
        pulumi.set(__self__, "port_range", port_range)
        if ports and not isinstance(ports, list):
            raise TypeError("Expected argument 'ports' to be a list")
        pulumi.set(__self__, "ports", ports)
        if project and not isinstance(project, str):
            raise TypeError("Expected argument 'project' to be a str")
        pulumi.set(__self__, "project", project)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if self_link and not isinstance(self_link, str):
            raise TypeError("Expected argument 'self_link' to be a str")
        pulumi.set(__self__, "self_link", self_link)
        if service_label and not isinstance(service_label, str):
            raise TypeError("Expected argument 'service_label' to be a str")
        pulumi.set(__self__, "service_label", service_label)
        if service_name and not isinstance(service_name, str):
            raise TypeError("Expected argument 'service_name' to be a str")
        pulumi.set(__self__, "service_name", service_name)
        if subnetwork and not isinstance(subnetwork, str):
            raise TypeError("Expected argument 'subnetwork' to be a str")
        pulumi.set(__self__, "subnetwork", subnetwork)
        if target and not isinstance(target, str):
            raise TypeError("Expected argument 'target' to be a str")
        pulumi.set(__self__, "target", target)

    @property
    @pulumi.getter(name="allPorts")
    def all_ports(self) -> bool:
        return pulumi.get(self, "all_ports")

    @property
    @pulumi.getter(name="allowGlobalAccess")
    def allow_global_access(self) -> bool:
        return pulumi.get(self, "allow_global_access")

    @property
    @pulumi.getter(name="backendService")
    def backend_service(self) -> str:
        return pulumi.get(self, "backend_service")

    @property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> str:
        return pulumi.get(self, "creation_timestamp")

    @property
    @pulumi.getter
    def description(self) -> str:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> str:
        return pulumi.get(self, "ip_address")

    @property
    @pulumi.getter(name="ipProtocol")
    def ip_protocol(self) -> str:
        return pulumi.get(self, "ip_protocol")

    @property
    @pulumi.getter(name="isMirroringCollector")
    def is_mirroring_collector(self) -> bool:
        return pulumi.get(self, "is_mirroring_collector")

    @property
    @pulumi.getter(name="labelFingerprint")
    def label_fingerprint(self) -> str:
        return pulumi.get(self, "label_fingerprint")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, str]:
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="loadBalancingScheme")
    def load_balancing_scheme(self) -> str:
        return pulumi.get(self, "load_balancing_scheme")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def network(self) -> str:
        return pulumi.get(self, "network")

    @property
    @pulumi.getter(name="networkTier")
    def network_tier(self) -> str:
        return pulumi.get(self, "network_tier")

    @property
    @pulumi.getter(name="portRange")
    def port_range(self) -> str:
        return pulumi.get(self, "port_range")

    @property
    @pulumi.getter
    def ports(self) -> Sequence[str]:
        return pulumi.get(self, "ports")

    @property
    @pulumi.getter
    def project(self) -> Optional[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def region(self) -> Optional[str]:
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> str:
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter(name="serviceLabel")
    def service_label(self) -> str:
        return pulumi.get(self, "service_label")

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> str:
        return pulumi.get(self, "service_name")

    @property
    @pulumi.getter
    def subnetwork(self) -> str:
        return pulumi.get(self, "subnetwork")

    @property
    @pulumi.getter
    def target(self) -> str:
        return pulumi.get(self, "target")


class AwaitableGetForwardingRuleResult(GetForwardingRuleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetForwardingRuleResult(
            all_ports=self.all_ports,
            allow_global_access=self.allow_global_access,
            backend_service=self.backend_service,
            creation_timestamp=self.creation_timestamp,
            description=self.description,
            id=self.id,
            ip_address=self.ip_address,
            ip_protocol=self.ip_protocol,
            is_mirroring_collector=self.is_mirroring_collector,
            label_fingerprint=self.label_fingerprint,
            labels=self.labels,
            load_balancing_scheme=self.load_balancing_scheme,
            name=self.name,
            network=self.network,
            network_tier=self.network_tier,
            port_range=self.port_range,
            ports=self.ports,
            project=self.project,
            region=self.region,
            self_link=self.self_link,
            service_label=self.service_label,
            service_name=self.service_name,
            subnetwork=self.subnetwork,
            target=self.target)


def get_forwarding_rule(name: Optional[str] = None,
                        project: Optional[str] = None,
                        region: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetForwardingRuleResult:
    """
    Get a forwarding rule within GCE from its name.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_gcp as gcp

    my_forwarding_rule = gcp.compute.get_forwarding_rule(name="forwarding-rule-us-east1")
    ```


    :param str name: The name of the forwarding rule.
    :param str project: The project in which the resource belongs. If it
           is not provided, the provider project is used.
    :param str region: The region in which the resource belongs. If it
           is not provided, the project region is used.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['project'] = project
    __args__['region'] = region
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('gcp:compute/getForwardingRule:getForwardingRule', __args__, opts=opts, typ=GetForwardingRuleResult).value

    return AwaitableGetForwardingRuleResult(
        all_ports=__ret__.all_ports,
        allow_global_access=__ret__.allow_global_access,
        backend_service=__ret__.backend_service,
        creation_timestamp=__ret__.creation_timestamp,
        description=__ret__.description,
        id=__ret__.id,
        ip_address=__ret__.ip_address,
        ip_protocol=__ret__.ip_protocol,
        is_mirroring_collector=__ret__.is_mirroring_collector,
        label_fingerprint=__ret__.label_fingerprint,
        labels=__ret__.labels,
        load_balancing_scheme=__ret__.load_balancing_scheme,
        name=__ret__.name,
        network=__ret__.network,
        network_tier=__ret__.network_tier,
        port_range=__ret__.port_range,
        ports=__ret__.ports,
        project=__ret__.project,
        region=__ret__.region,
        self_link=__ret__.self_link,
        service_label=__ret__.service_label,
        service_name=__ret__.service_name,
        subnetwork=__ret__.subnetwork,
        target=__ret__.target)


@_utilities.lift_output_func(get_forwarding_rule)
def get_forwarding_rule_output(name: Optional[pulumi.Input[str]] = None,
                               project: Optional[pulumi.Input[Optional[str]]] = None,
                               region: Optional[pulumi.Input[Optional[str]]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetForwardingRuleResult]:
    """
    Get a forwarding rule within GCE from its name.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_gcp as gcp

    my_forwarding_rule = gcp.compute.get_forwarding_rule(name="forwarding-rule-us-east1")
    ```


    :param str name: The name of the forwarding rule.
    :param str project: The project in which the resource belongs. If it
           is not provided, the provider project is used.
    :param str region: The region in which the resource belongs. If it
           is not provided, the project region is used.
    """
    ...
