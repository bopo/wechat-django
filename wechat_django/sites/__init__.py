# -*- coding: utf-8 -*-
# flake8: noqa
from __future__ import unicode_literals

try:
    from .wechat import default_site as wechat, WeChatSite
except ImportError:
    pass
