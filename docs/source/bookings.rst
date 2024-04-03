.. _bookings_forms:

===================
Booking Form Class
===================

.. automodule:: bookings.forms
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: BookingForm
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__, __str__
   :exclude-members: Meta

   This class represents a form for booking appointments in the booking system.

   Inherits from :class:`django.forms.ModelForm`.

   .. attribute:: Meta

      A nested class that contains metadata for the form.

      - model (:class:`~bookings.models.Booking`): The associated model for the form.
      - fields (:class:`list`): The fields to include in the form, which are 'date', 'start_time', and 'end_time'.

   .. rubric:: Example

   .. code-block:: python

      from bookings.forms import BookingForm

      # Create an instance of the BookingForm
      form = BookingForm()

      # Use the form instance to render the form in a template
      {{ form.as_p }}

bookings package
================

Subpackages
-----------

.. toctree::
   :maxdepth: 4

   bookings.migrations

Submodules
----------

bookings.admin module
---------------------

.. automodule:: bookings.admin
   :members:
   :undoc-members:
   :show-inheritance:

bookings.apps module
--------------------

.. automodule:: bookings.apps
   :members:
   :undoc-members:
   :show-inheritance:

bookings.forms module
---------------------

.. automodule:: bookings.forms
   :members:
   :undoc-members:
   :show-inheritance:

bookings.models module
----------------------

.. automodule:: bookings.models
   :members:
   :undoc-members:
   :show-inheritance:

bookings.serializers module
---------------------------

.. automodule:: bookings.serializers
   :members:
   :undoc-members:
   :show-inheritance:

bookings.tasks module
---------------------

.. automodule:: bookings.tasks
   :members:
   :undoc-members:
   :show-inheritance:

bookings.tests module
---------------------

.. automodule:: bookings.tests
   :members:
   :undoc-members:
   :show-inheritance:

bookings.urls module
--------------------

.. automodule:: bookings.urls
   :members:
   :undoc-members:
   :show-inheritance:

.. _bookings_views:

===============
Bookings Views
===============

This module contains views for handling booking-related functionality.

The views include:

- :func:`book_appointment`: View function to handle booking appointment requests.
- :func:`booking_list`: View function to retrieve and render the list of all bookings.
- :func:`booking_success`: View function to render the booking success page.
- :func:`booking_failure`: View function to render the booking failure page.

For detailed information about each view, refer to the corresponding docstrings in the source code.

For more specific views or additional functionality, please refer to the sour

Module contents
---------------

.. automodule:: bookings
   :members:
   :undoc-members:
   :show-inheritance:
