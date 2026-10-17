.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

============================
Helpdesk - Ticket Dependency
============================

Lets a helpdesk ticket list the blockers it depends on. A blocker is
another ticket, linked with a project management dependency type, or an
external work item that is marked as resolved by hand.

* Finish to Start: the ticket cannot be started until the blocker ticket
  is finished.
* Start to Start: the ticket cannot be started until the blocker ticket
  is started.
* Finish to Finish: the ticket cannot be confirmed or finished until the
  blocker ticket is finished.
* Start to Finish: the ticket cannot be confirmed or finished until the
  blocker ticket is started.
* External: the ticket cannot be confirmed or finished until the
  external blocker is ticked as resolved.

A blocker ticket that is done, cancelled or terminated counts as
finished. The rejection message names the blockers that hold the ticket.
The *Blocked* filter on the ticket search view finds the tickets that are
still held.

Work Instruction
================

* `Edit Helpdesk Ticket (Ticket Dependency) <docs/helpdesk_ticket/02-edit.html>`_
* `Start Helpdesk Ticket (Ticket Dependency) <docs/helpdesk_ticket/07-start.html>`_
* `Confirm Helpdesk Ticket (Ticket Dependency) <docs/helpdesk_ticket/04-confirm.html>`_

Installation
============

To install this module, you need to:

1.  Clone the branch 14.0 of the repository https://github.com/open-synergy/ssi-helpdesk
2.  Add the path to this repository in your configuration (addons-path)
3.  Update the module list (Must be on developer mode)
4.  Go to menu *Apps -> Apps -> Main Apps*
5.  Search For *Helpdesk - Ticket Dependency*
6.  Install the module

Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/open-synergy/ssi-helpdesk/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smash it by providing detailed and welcomed feedback.


Credits
=======

Contributors
------------

* Andhitia Rama <andhitia.r@gmail.com>

Maintainer
----------

.. image:: https://simetri-sinergi.id/logo.png
   :alt: PT. Simetri Sinergi Indonesia
   :target: https://simetri-sinergi.id

This module is maintained by the PT. Simetri Sinergi Indonesia.
