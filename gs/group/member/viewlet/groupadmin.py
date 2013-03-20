# -*- coding: utf-8 -*-
from zope.cachedescriptors.property import Lazy
from gs.group.member.base import user_admin_of_group, \
    user_group_admin_of_group, user_division_admin_of_group
from member import MemberViewlet


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
