# -*- coding: utf-8 -*-

from pyload.plugins.internal.DeadHoster import DeadHoster, create_getInfo


class ShareFilesCo(DeadHoster):
    __name    = "ShareFilesCo"
    __type    = "hoster"
    __version = "0.02"

    __pattern = r'http://(?:www\.)?sharefiles\.co/\w{12}'

    __description = """Sharefiles.co hoster plugin"""
    __license     = "GPLv3"
    __authors     = [("stickell", "l.stickell@yahoo.it")]


getInfo = create_getInfo(ShareFilesCo)