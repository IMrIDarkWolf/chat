from rest_framework import serializers
from chat_room.models import Room, Message
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer of user
    """

    class Meta:
        model = User
        fields = ('id', 'username')


class RoomSerializers(serializers.ModelSerializer):
    """
    Serializer of rooms
    """

    creator = UserSerializer()
    invited = UserSerializer(many=True)

    class Meta:
        model = Room
        fields = ("name", "creator", "invited", "date")


class MessageSerializers(serializers.ModelSerializer):
    """
    chat serializer
    """
    user = UserSerializer()

    class Meta:
        model = Message
        fields = ('user', 'text', 'date')


class MessagePostSerializers(serializers.ModelSerializer):
    """
    chat serializer
    """

    class Meta:
        model = Message
        fields = ('room', 'text')
