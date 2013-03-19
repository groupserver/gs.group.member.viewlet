# -*- coding: utf-8 -*-
from zope.cachedescriptors.property import Lazy
from Products.XWFCore.XWFUtils import getOption
from groupadmin import GroupAdminViewlet


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
