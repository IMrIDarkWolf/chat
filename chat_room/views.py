from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from chat_room.models import Room, Message
from chat_room.serializers import RoomSerializers, MessageSerializers, MessagePostSerializers


class RoomView(APIView):
    """
    chat rooms
    """

    def get(self, request):
        rooms = Room.objects.all()
        serializer = RoomSerializers(rooms, many=True)
        return Response({"data": serializer.data})


class MessageView(APIView):
    """
    chat dialog
    """

    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.AllowAny]

    def get(self, request):
        room = request.GET.get('room')
        messages = Message.objects.filter(room=room)

        serializer = MessageSerializers(messages, many=True)
        return Response({'data': serializer.data})


    def post(self, request):
        # room = request.data.get('room')
        message = MessagePostSerializers(data=request.data)

        if message.is_valid():
            message.save(user=request.user)
            return Response({'status': 'success'})
        else:
            return Response({'status': 'error'})

