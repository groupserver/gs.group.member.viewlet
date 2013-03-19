# -*- coding: utf-8 -*-
from zope.cachedescriptors.property import Lazy
from utils import user_member_of_group
from gs.group.base.viewlet import GroupViewlet


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
