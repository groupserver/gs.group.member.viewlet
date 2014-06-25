# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright © 2013, 2014 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
from __future__ import absolute_import, unicode_literals
from zope.cachedescriptors.property import Lazy
from Products.XWFCore.XWFUtils import getOption
from .groupadmin import GroupAdminViewlet


class SiteAdminViewlet(GroupAdminViewlet):
    def __init__(self, group, request, view, manager):
        super(SiteAdminViewlet, self).__init__(group, request, view, manager)

    # TODO: Sort out the posting limit mess
    @Lazy
    def canSetPostingLimit(self):
        retval = self.isSiteAdmin and \
            getOption(self.context, 'admin_can_set_posting_limit', True)
        return retval

    @Lazy
    def show(self):
        retval = not(self.loggedInUser.anonymous) and self.isSiteAdmin
        assert type(retval) == bool
        return retval
