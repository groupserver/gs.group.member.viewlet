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
from gs.group.member.base import user_admin_of_group, \
    user_group_admin_of_group, user_division_admin_of_group
from .member import MemberViewlet


class GroupAdminViewlet(MemberViewlet):
    def __init__(self, group, request, view, manager):
        super(GroupAdminViewlet, self).__init__(group, request, view, manager)

    @Lazy
    def isAdmin(self):
        retval = not(self.loggedInUser.anonymous) \
                    and user_admin_of_group(self.loggedInUser,
                                            self.groupInfo)
        return retval

    @Lazy
    def isSiteAdmin(self):
        retval = user_division_admin_of_group(self.loggedInUser,
                                                self.groupInfo)
        return retval

    @Lazy
    def isGroupAdmin(self):
        retval = user_group_admin_of_group(self.loggedInUser,
                                            self.groupInfo)
        return retval

    @Lazy
    def show(self):
        retval = self.isAdmin
        assert type(retval) == bool
        return retval
