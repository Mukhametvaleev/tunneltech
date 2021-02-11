from django_grpc_framework import proto_serializers
from rest_framework import serializers

import proto.windtunneltypes_pb2 as pb2


class ValueField(serializers.Field):
    def get_attribute(self, instance):
        return instance

    def to_representation(self, value):
        return getattr(value, value.WhichOneof("value"))


class ReadResultProtoSerializer(proto_serializers.ProtoSerializer):
    name = serializers.CharField()
    tags = serializers.CharField()
    value = ValueField()

    class Meta:
        proto_class = pb2.ReadResult


class ReadResultsProtoSerializer(proto_serializers.ProtoSerializer):
    parameters = ReadResultProtoSerializer(many=True)

    class Meta:
        proto_class = pb2.ReadResults
