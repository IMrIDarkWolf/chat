from django.contrib import admin
from chat_room.models import Room, Message


class RoomAdmin(admin.ModelAdmin):
    """
    chat rooms
    """

    list_display = ('creator', 'invited_user', 'date')

    def invited_user(self, obj):
        return '\n'.join([user.username for user in obj.invited.all()])


class MessageAdmin(admin.ModelAdmin):
    """
    messages
    """

    list_display = ('room', 'user', 'text', 'date')


admin.site.register(Room, RoomAdmin)
admin.site.register(Message, MessageAdmin)
