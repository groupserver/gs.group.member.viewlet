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
from gs.group.base.viewlet import GroupViewlet
from gs.group.member.base import user_member_of_group


class MemberViewlet(GroupViewlet):
    def __init__(self, group, request, view, manager):
        super(MemberViewlet, self).__init__(group, request, view, manager)

    @Lazy
    def isMember(self):
        retval = ((not self.loggedInUser.anonymous) and
                    user_member_of_group(self.loggedInUser, self.groupInfo))
        return retval


class MemberOnlyViewlet(MemberViewlet):
    @Lazy
    def show(self):
        retval = self.isMember
        return retval
