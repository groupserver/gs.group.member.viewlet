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
logged in user is a group member. For example, the viewlet that displays
the *Hide a Post* JavaScript in a topic [#topic]_::

  <browser:viewlet 
    name="gs-group-messages-topic-hide-js"
    manager=".interfaces.ITopicJavaScript"
    template="browser/templates/hidejs.pt"
    class="gs.group.member.viewlet.MemberOnlyViewlet"
    permission="zope2.View"
    weight="35"
    title="Show and Hide Buttons" />


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

For example, the *Encouragement* [#encouragement]_ that is added to the
Group page::

  <browser:viewlet 
    name="gs-group-encouragement-area"
    manager="gs.group.home.interfaces.IGroupHomepageScripts"
    for="gs.group.base.interfaces.IGSGroupMarker"
    template="browser/templates/encouragementarea.pt"
    class="gs.group.member.viewlet.GroupAdminViewlet"
    permission="zope2.ManageProperties"
    weight="90"
    title="Encouragement" />

``SiteAdminViewlet``
--------------------

The ``gs.group.member.viewlet.SiteAdminViewlet`` is a subclass of the
`GroupAdminViewlet`_. It sets the ``show`` property to ``True`` if the
logged in user is a site administrator. For example, the viewlet that list
all the links to change the group properties [#properties]_::

  <browser:viewlet 
    name="gs-group-properties-admin"
    manager="gs.group.home.interfaces.IGroupHomepageAdmin"
    template="browser/templates/admin.pt"
    class="gs.group.member.viewlet.SiteAdminViewlet"
    permission="zope2.ManageProperties"
    weight="20" />

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

.. [#topic] See ``gs.group.messages.topic``
            <https://source.iopen.net/groupserver/gs.group.messages.topic>

.. [#encouragement] See ``gs.group.encouragement``
                    <https://source.iopen.net/groupserver/gs.group.encouragement>

.. [#properties] Group administrators can only alter the membership of the
                 group, and edit the *About* box. All other properties are
                 the purview of the site administrator. See
                 ``gs.group.properties``
                 <https://source.iopen.net/groupserver/gs.group.properties>

..  LocalWords:  viewlets
