# LocalStack Resource Provider Scaffolding v2
from __future__ import annotations

from pathlib import Path
from typing import Optional, Type, TypedDict

import localstack.services.cloudformation.provider_utils as util
from localstack.services.cloudformation.resource_provider import (
    CloudFormationResourceProviderPlugin,
    OperationStatus,
    ProgressEvent,
    ResourceProvider,
    ResourceRequest,
)


class EC2RouteTableProperties(TypedDict):
    VpcId: Optional[str]
    RouteTableId: Optional[str]
    Tags: Optional[list[Tag]]


class Tag(TypedDict):
    Key: Optional[str]
    Value: Optional[str]


REPEATED_INVOCATION = "repeated_invocation"


class EC2RouteTableProvider(ResourceProvider[EC2RouteTableProperties]):

    TYPE = "AWS::EC2::RouteTable"  # Autogenerated. Don't change
    SCHEMA = util.get_schema_path(Path(__file__))  # Autogenerated. Don't change

    def create(
        self,
        request: ResourceRequest[EC2RouteTableProperties],
    ) -> ProgressEvent[EC2RouteTableProperties]:
        """
        Create a new resource.

        Primary identifier fields:
          - /properties/RouteTableId

        Required properties:
          - VpcId

        Create-only properties:
          - /properties/VpcId

        Read-only properties:
          - /properties/RouteTableId

        IAM permissions required:
          - ec2:CreateRouteTable
          - ec2:CreateTags
          - ec2:DescribeRouteTables

        """
        model = request.desired_state

        # TODO: validations

        if not request.custom_context.get(REPEATED_INVOCATION):
            # this is the first time this callback is invoked
            # TODO: defaults
            # TODO: idempotency
            # TODO: actually create the resource
            request.custom_context[REPEATED_INVOCATION] = True
            return ProgressEvent(
                status=OperationStatus.IN_PROGRESS,
                resource_model=model,
                custom_context=request.custom_context,
            )

        # TODO: check the status of the resource
        # - if finished, update the model with all fields and return success event:
        #   return ProgressEvent(status=OperationStatus.SUCCESS, resource_model=model)
        # - else
        #   return ProgressEvent(status=OperationStatus.IN_PROGRESS, resource_model=model)

        raise NotImplementedError

    def read(
        self,
        request: ResourceRequest[EC2RouteTableProperties],
    ) -> ProgressEvent[EC2RouteTableProperties]:
        """
        Fetch resource information

        IAM permissions required:
          - ec2:DescribeRouteTables
        """
        raise NotImplementedError

    def delete(
        self,
        request: ResourceRequest[EC2RouteTableProperties],
    ) -> ProgressEvent[EC2RouteTableProperties]:
        """
        Delete a resource

        IAM permissions required:
          - ec2:DescribeRouteTables
          - ec2:DeleteRouteTable
        """
        raise NotImplementedError

    def update(
        self,
        request: ResourceRequest[EC2RouteTableProperties],
    ) -> ProgressEvent[EC2RouteTableProperties]:
        """
        Update a resource

        IAM permissions required:
          - ec2:CreateTags
          - ec2:DeleteTags
          - ec2:DescribeRouteTables
        """
        raise NotImplementedError


class EC2RouteTableProviderPlugin(CloudFormationResourceProviderPlugin):
    name = "AWS::EC2::RouteTable"

    def __init__(self):
        self.factory: Optional[Type[ResourceProvider]] = None

    def load(self):
        self.factory = EC2RouteTableProvider

