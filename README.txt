===========================
``gs.group.member.viewlet``
===========================
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Useful viewlets for different group members
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Author: `Michael JasonSmith`_
:Contact: Michael JasonSmith <mpj17@onlinegroups.net>
:Date: 2013-03-21
:Organization: `GroupServer.org`_
:Copyright: This document is licensed under a
  `Creative Commons Attribution-Share Alike 3.0 New Zealand License`_
  by `OnlineGroups.Net`_.

Introduction
============

This product provides some useful base classes for viewlets_ that are shown
to group members with different roles.

Viewlets
========

There are four viewlets defined:

#. `MemberViewlet`_
#. `MemberOnlyViewlet`_
#. `GroupAdminViewlet`_
#. `SiteAdminViewlet`_

``MemberViewlet``
-----------------

The ``gs.group.member.viewlet.MemberViewlet`` viewlet is like a standard
group viewlet [#groupViewlet]_, except that it provides the ``isMember``
property, which returns ``True`` if the logged in user is a group
member. This class is the parent of all the other member-viewlets.

``MemberOnlyViewlet``
---------------------

The ``gs.group.member.viewlet.MemberOnlyViewlet`` viewlet is a subclass of
the `MemberViewlet`_. It sets the ``show`` property to ``True`` if the
logged in user is a group member.

``GroupAdminViewlet``
---------------------

The ``gs.group.member.viewlet.GroupAdminViewlet`` is a subclass of
`MemberViewlet`_. It defines the following properties.

================ =========================================================
Property         Description
================ =========================================================
``isAdmin``      ``True`` if the logged in user is an administrator.
``show``         ``True`` if the logged in user is an administrator.
``isSiteAdmin``  ``True`` if the logged in user is a site administrator.
``isGroupAdmin`` ``True`` if the logged in user is a group administrator.
================ =========================================================

``SiteAdminViewlet``
--------------------

The ``gs.group.member.viewlet.SiteAdminViewlet`` is a subclass of the
`GroupAdminViewlet`_. It sets the ``show`` property to ``True`` if the
logged in user is a site administrator.

Resources
=========

- Code repository: https://source.iopen.net/groupserver/gs.group.member.viewlet
- Questions and comments to http://groupserver.org/groups/development
- Report bugs at https://redmine.iopen.net/projects/groupserver

.. _GroupServer: http://groupserver.org/
.. _GroupServer.org: http://groupserver.org/
.. _OnlineGroups.Net: https://onlinegroups.net
.. _Michael JasonSmith: http://groupserver.org/p/mpj17
.. _Creative Commons Attribution-Share Alike 3.0 New Zealand License:
   http://creativecommons.org/licenses/by-sa/3.0/nz/

.. [#groupViewlet] See ``gs.group.base.GroupViewlet`` for the standard
                   group viewlet
                   <https://source.iopen.net/groupserver/gs.group.base>


..  LocalWords:  viewlets
