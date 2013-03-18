# -*- coding: utf-8 -*-
from zope.cachedescriptors.property import Lazy
from gs.group.privacy.visibility import GroupVisibility
from viewlet import MemberViewlet


class MemberInfo(MemberViewlet):

    def __init__(self, group, request, view, manager):
        super(MemberInfo, self).__init__(group, request, view, manager)

    @Lazy
    def groupVisibility(self):
        retval = GroupVisibility(self.groupInfo)
        return retval


class LoggedInMemberInfo(MemberInfo):
    '''Membership information for logged in members'''
    @Lazy
    def show(self):
        retval = self.isMember
        return retval


class PublicGroupMemberInfo(MemberInfo):
    '''Membership information for public groups.'''
    @Lazy
    def show(self):
        retval = not(self.isMember) and self.groupVisibility.isPublic
        return retval


class PrivateGroupMemberInfo(MemberInfo):
    '''Membership information for private groups'''
    @Lazy
    def show(self):
        retval = not(self.isMember) and self.groupVisibility.isPrivate
        return retval


# Secret groups are not shown to people we know will be Anonymous.
