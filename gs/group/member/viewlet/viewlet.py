# coding=utf-8
from zope.cachedescriptors.property import Lazy
from Products.XWFCore.XWFUtils import getOption
from utils import user_admin_of_group, user_group_admin_of_group, \
    user_division_admin_of_group, user_member_of_group
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
