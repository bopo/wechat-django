# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..base import WeChatModelAdmin
from ..utils import foreignkey
from ...models import MessageLog


class MessageLogAdmin(WeChatModelAdmin):
    __category__ = "messagelog"
    __model__ = MessageLog

    list_display = (
        "msg_id", foreignkey("user"), "type", "content", "created_at")
    list_filter = ("type",)
    search_fields = (
        "=user__openid", "=user__unionid", "user__nickname", "user__comment",
        "content")

    fields = (
        "msg_id", foreignkey("user"), "type", "content", "created_at")
    readonly_fields = fields

    def has_add_permission(self, request):
        return False

    def get_model_perms(self, request):
        if not request.app.abilities.interactable:
            return {}
        return super(MessageLogAdmin, self).get_model_perms(request)
