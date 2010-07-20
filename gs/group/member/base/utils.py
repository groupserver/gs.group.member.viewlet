# coding=utf-8
from Products.CustomUserFolder.interfaces import IGSUserInfo
import logging
log = logging.getLogger('gs.group.member.base.utils') #@UndefinedVariable

def user_member_of_group(u, g):
    '''Is the user the member of the group
    
    ARGUMENTS
        "user":  A Custom User.
        "group": A GroupServer group-folder.
        
    RETURNS
        True if the user is the member of the group. False otherwise.
    '''
    group = g.groupObj
    user = u.user
    
    retval = 'GroupMember' in user.getRolesInContext(group)
    
    # Thundering great sanity check
    memberGroup = member_id(group.getId())
    userGroups = user.getGroups()
    if retval and (memberGroup not in userGroups):
        m = u'(%s) has the GroupMember role for (%s) but is not in  %s'%\
          (user.getId(), group.getId(), memberGroup)
        log.error(m)
    elif not(retval) and (memberGroup in userGroups):
        m = u'(%s) is in %s, but does not have the GroupMember role in (%s)'%\
          (user.getId(), memberGroup, group.getId())
        log.error(m)
        
    assert type(retval) == bool
    return retval
    return user
    
def user_member_of_site(user, site):
    retval = 'DivisionMember' in user.getRolesInContext(site)
    assert type(retval) == bool
    return retval

def user_division_admin_of_group(u, g):
    group = groupInfo_to_group(g)
    user = userInfo_to_user(u)
    retval = ('DivisionAdmin' in user.getRolesInContext(group))
    assert type(retval) == bool
    return retval

def member_id(groupId):
    assert type(groupId) == str
    assert groupId != ''
    retval = '%s_member' % groupId    
    assert type(retval) == str
    return retval

