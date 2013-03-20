# -*- coding: utf-8 -*-
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
