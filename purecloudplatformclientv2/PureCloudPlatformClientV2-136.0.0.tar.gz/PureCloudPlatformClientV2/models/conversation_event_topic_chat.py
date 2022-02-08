# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems
import re
import json

from ..utils import sanitize_for_serialization

class ConversationEventTopicChat(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ConversationEventTopicChat - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'state': 'str',
            'id': 'str',
            'provider': 'str',
            'script_id': 'str',
            'peer_id': 'str',
            'room_id': 'str',
            'avatar_image_url': 'str',
            'held': 'bool',
            'disconnect_type': 'str',
            'start_hold_time': 'datetime',
            'connected_time': 'datetime',
            'disconnected_time': 'datetime',
            'journey_context': 'ConversationEventTopicJourneyContext',
            'wrapup': 'ConversationEventTopicWrapup',
            'after_call_work': 'ConversationEventTopicAfterCallWork',
            'after_call_work_required': 'bool'
        }

        self.attribute_map = {
            'state': 'state',
            'id': 'id',
            'provider': 'provider',
            'script_id': 'scriptId',
            'peer_id': 'peerId',
            'room_id': 'roomId',
            'avatar_image_url': 'avatarImageUrl',
            'held': 'held',
            'disconnect_type': 'disconnectType',
            'start_hold_time': 'startHoldTime',
            'connected_time': 'connectedTime',
            'disconnected_time': 'disconnectedTime',
            'journey_context': 'journeyContext',
            'wrapup': 'wrapup',
            'after_call_work': 'afterCallWork',
            'after_call_work_required': 'afterCallWorkRequired'
        }

        self._state = None
        self._id = None
        self._provider = None
        self._script_id = None
        self._peer_id = None
        self._room_id = None
        self._avatar_image_url = None
        self._held = None
        self._disconnect_type = None
        self._start_hold_time = None
        self._connected_time = None
        self._disconnected_time = None
        self._journey_context = None
        self._wrapup = None
        self._after_call_work = None
        self._after_call_work_required = None

    @property
    def state(self):
        """
        Gets the state of this ConversationEventTopicChat.
        The connection state of this communication.

        :return: The state of this ConversationEventTopicChat.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this ConversationEventTopicChat.
        The connection state of this communication.

        :param state: The state of this ConversationEventTopicChat.
        :type: str
        """
        allowed_values = ["alerting", "dialing", "contacting", "offering", "connected", "disconnected", "terminated", "none"]
        if state.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for state -> " + state)
            self._state = "outdated_sdk_version"
        else:
            self._state = state

    @property
    def id(self):
        """
        Gets the id of this ConversationEventTopicChat.
        A globally unique identifier for this communication.

        :return: The id of this ConversationEventTopicChat.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ConversationEventTopicChat.
        A globally unique identifier for this communication.

        :param id: The id of this ConversationEventTopicChat.
        :type: str
        """
        
        self._id = id

    @property
    def provider(self):
        """
        Gets the provider of this ConversationEventTopicChat.
        The source provider of the chat.

        :return: The provider of this ConversationEventTopicChat.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """
        Sets the provider of this ConversationEventTopicChat.
        The source provider of the chat.

        :param provider: The provider of this ConversationEventTopicChat.
        :type: str
        """
        
        self._provider = provider

    @property
    def script_id(self):
        """
        Gets the script_id of this ConversationEventTopicChat.
        The UUID of the script to use.

        :return: The script_id of this ConversationEventTopicChat.
        :rtype: str
        """
        return self._script_id

    @script_id.setter
    def script_id(self, script_id):
        """
        Sets the script_id of this ConversationEventTopicChat.
        The UUID of the script to use.

        :param script_id: The script_id of this ConversationEventTopicChat.
        :type: str
        """
        
        self._script_id = script_id

    @property
    def peer_id(self):
        """
        Gets the peer_id of this ConversationEventTopicChat.
        The id of the peer communication corresponding to a matching leg for this communication.

        :return: The peer_id of this ConversationEventTopicChat.
        :rtype: str
        """
        return self._peer_id

    @peer_id.setter
    def peer_id(self, peer_id):
        """
        Sets the peer_id of this ConversationEventTopicChat.
        The id of the peer communication corresponding to a matching leg for this communication.

        :param peer_id: The peer_id of this ConversationEventTopicChat.
        :type: str
        """
        
        self._peer_id = peer_id

    @property
    def room_id(self):
        """
        Gets the room_id of this ConversationEventTopicChat.
        The room id for the chat.

        :return: The room_id of this ConversationEventTopicChat.
        :rtype: str
        """
        return self._room_id

    @room_id.setter
    def room_id(self, room_id):
        """
        Sets the room_id of this ConversationEventTopicChat.
        The room id for the chat.

        :param room_id: The room_id of this ConversationEventTopicChat.
        :type: str
        """
        
        self._room_id = room_id

    @property
    def avatar_image_url(self):
        """
        Gets the avatar_image_url of this ConversationEventTopicChat.
        The avatar for the chat (if available).

        :return: The avatar_image_url of this ConversationEventTopicChat.
        :rtype: str
        """
        return self._avatar_image_url

    @avatar_image_url.setter
    def avatar_image_url(self, avatar_image_url):
        """
        Sets the avatar_image_url of this ConversationEventTopicChat.
        The avatar for the chat (if available).

        :param avatar_image_url: The avatar_image_url of this ConversationEventTopicChat.
        :type: str
        """
        
        self._avatar_image_url = avatar_image_url

    @property
    def held(self):
        """
        Gets the held of this ConversationEventTopicChat.
        True if this call is held and the person on this side hears silence.

        :return: The held of this ConversationEventTopicChat.
        :rtype: bool
        """
        return self._held

    @held.setter
    def held(self, held):
        """
        Sets the held of this ConversationEventTopicChat.
        True if this call is held and the person on this side hears silence.

        :param held: The held of this ConversationEventTopicChat.
        :type: bool
        """
        
        self._held = held

    @property
    def disconnect_type(self):
        """
        Gets the disconnect_type of this ConversationEventTopicChat.
        System defined string indicating what caused the communication to disconnect. Will be null until the communication disconnects.

        :return: The disconnect_type of this ConversationEventTopicChat.
        :rtype: str
        """
        return self._disconnect_type

    @disconnect_type.setter
    def disconnect_type(self, disconnect_type):
        """
        Sets the disconnect_type of this ConversationEventTopicChat.
        System defined string indicating what caused the communication to disconnect. Will be null until the communication disconnects.

        :param disconnect_type: The disconnect_type of this ConversationEventTopicChat.
        :type: str
        """
        allowed_values = ["endpoint", "client", "system", "timeout", "transfer", "transfer.conference", "transfer.consult", "transfer.noanswer", "transfer.notavailable", "transfer.forward", "transport.failure", "error", "peer", "other", "spam", "uncallable"]
        if disconnect_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for disconnect_type -> " + disconnect_type)
            self._disconnect_type = "outdated_sdk_version"
        else:
            self._disconnect_type = disconnect_type

    @property
    def start_hold_time(self):
        """
        Gets the start_hold_time of this ConversationEventTopicChat.
        The timestamp the chat was placed on hold in the cloud clock if the chat is currently on hold.

        :return: The start_hold_time of this ConversationEventTopicChat.
        :rtype: datetime
        """
        return self._start_hold_time

    @start_hold_time.setter
    def start_hold_time(self, start_hold_time):
        """
        Sets the start_hold_time of this ConversationEventTopicChat.
        The timestamp the chat was placed on hold in the cloud clock if the chat is currently on hold.

        :param start_hold_time: The start_hold_time of this ConversationEventTopicChat.
        :type: datetime
        """
        
        self._start_hold_time = start_hold_time

    @property
    def connected_time(self):
        """
        Gets the connected_time of this ConversationEventTopicChat.
        The timestamp when this communication was connected in the cloud clock.

        :return: The connected_time of this ConversationEventTopicChat.
        :rtype: datetime
        """
        return self._connected_time

    @connected_time.setter
    def connected_time(self, connected_time):
        """
        Sets the connected_time of this ConversationEventTopicChat.
        The timestamp when this communication was connected in the cloud clock.

        :param connected_time: The connected_time of this ConversationEventTopicChat.
        :type: datetime
        """
        
        self._connected_time = connected_time

    @property
    def disconnected_time(self):
        """
        Gets the disconnected_time of this ConversationEventTopicChat.
        The timestamp when this communication disconnected from the conversation in the provider clock.

        :return: The disconnected_time of this ConversationEventTopicChat.
        :rtype: datetime
        """
        return self._disconnected_time

    @disconnected_time.setter
    def disconnected_time(self, disconnected_time):
        """
        Sets the disconnected_time of this ConversationEventTopicChat.
        The timestamp when this communication disconnected from the conversation in the provider clock.

        :param disconnected_time: The disconnected_time of this ConversationEventTopicChat.
        :type: datetime
        """
        
        self._disconnected_time = disconnected_time

    @property
    def journey_context(self):
        """
        Gets the journey_context of this ConversationEventTopicChat.


        :return: The journey_context of this ConversationEventTopicChat.
        :rtype: ConversationEventTopicJourneyContext
        """
        return self._journey_context

    @journey_context.setter
    def journey_context(self, journey_context):
        """
        Sets the journey_context of this ConversationEventTopicChat.


        :param journey_context: The journey_context of this ConversationEventTopicChat.
        :type: ConversationEventTopicJourneyContext
        """
        
        self._journey_context = journey_context

    @property
    def wrapup(self):
        """
        Gets the wrapup of this ConversationEventTopicChat.
        Call wrap up or disposition data.

        :return: The wrapup of this ConversationEventTopicChat.
        :rtype: ConversationEventTopicWrapup
        """
        return self._wrapup

    @wrapup.setter
    def wrapup(self, wrapup):
        """
        Sets the wrapup of this ConversationEventTopicChat.
        Call wrap up or disposition data.

        :param wrapup: The wrapup of this ConversationEventTopicChat.
        :type: ConversationEventTopicWrapup
        """
        
        self._wrapup = wrapup

    @property
    def after_call_work(self):
        """
        Gets the after_call_work of this ConversationEventTopicChat.
        A communication's after-call work data.

        :return: The after_call_work of this ConversationEventTopicChat.
        :rtype: ConversationEventTopicAfterCallWork
        """
        return self._after_call_work

    @after_call_work.setter
    def after_call_work(self, after_call_work):
        """
        Sets the after_call_work of this ConversationEventTopicChat.
        A communication's after-call work data.

        :param after_call_work: The after_call_work of this ConversationEventTopicChat.
        :type: ConversationEventTopicAfterCallWork
        """
        
        self._after_call_work = after_call_work

    @property
    def after_call_work_required(self):
        """
        Gets the after_call_work_required of this ConversationEventTopicChat.
        Indicates if after-call is required for a communication. Only used when the ACW Setting is Agent Requested.

        :return: The after_call_work_required of this ConversationEventTopicChat.
        :rtype: bool
        """
        return self._after_call_work_required

    @after_call_work_required.setter
    def after_call_work_required(self, after_call_work_required):
        """
        Sets the after_call_work_required of this ConversationEventTopicChat.
        Indicates if after-call is required for a communication. Only used when the ACW Setting is Agent Requested.

        :param after_call_work_required: The after_call_work_required of this ConversationEventTopicChat.
        :type: bool
        """
        
        self._after_call_work_required = after_call_work_required

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_json(self):
        """
        Returns the model as raw JSON
        """
        return json.dumps(sanitize_for_serialization(self.to_dict()))

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

