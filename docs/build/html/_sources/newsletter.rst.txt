newsletter package
==================

Subpackages
-----------

.. toctree::
   :maxdepth: 4

   newsletter.migrations

Submodules
----------

newsletter.admin module
-----------------------

.. automodule:: newsletter.admin
   :members:
   :undoc-members:
   :show-inheritance:

newsletter.apps module
----------------------

.. automodule:: newsletter.apps
   :members:
   :undoc-members:
   :show-inheritance:

.. _newsletter_forms:

================
Newsletter Forms
================

newsletter.forms
================

NewsletterForm
--------------

.. autoclass:: newsletter.forms.NewsletterForm
   :members:
   :undoc-members:
   :show-inheritance:

   Form for creating and updating newsletters.

   Inherits from :class:`django.forms.ModelForm`.

   .. attribute:: Meta

      A nested class that contains metadata for the form.

      - model (:class:`~newsletter.models.Newsletter`): The associated model for the form.
      - fields (:class:`list`): The fields to include in the form, which are 'subject', 'message', and 'recipients'.

   .. rubric:: Example

   .. code-block:: python

      from newsletter.forms import NewsletterForm

      # Create an instance of the NewsletterForm
      form = NewsletterForm()

      # Use the form instance to render the form in a template
      {{ form.as_p }}


newsletter.models
==================

Newsletter
----------

.. autoclass:: newsletter.models.Newsletter
   :members:
   :undoc-members:
   :show-inheritance:

   Model representing a newsletter.

   Attributes:
   - subject (CharField): The subject of the newsletter.
   - message (TextField): The content/message of the newsletter.
   - recipients (ManyToManyField): The recipients of the newsletter.

   .. rubric:: Example

   .. code-block:: python

      from newsletter.models import Newsletter

      # Create an instance of the Newsletter model
      newsletter = Newsletter(subject='Subject', message='Message')

      NewsletterSubscriber
--------------------

.. autoclass:: newsletter.models.NewsletterSubscriber
   :members:
   :undoc-members:
   :show-inheritance:

   Model representing a subscriber to the newsletter.

   Attributes:
   - email (EmailField): Email address of the subscriber.
   - subscribed_at (DateTimeField): Date and time when the subscriber subscribed.

   .. rubric:: Example

   .. code-block:: python

      from newsletter.models import NewsletterSubscriber

      # Create an instance of the NewsletterSubscriber model
      subscriber = NewsletterSubscriber(email='example@example.com')

newsletter.tasks module
-----------------------

.. automodule:: newsletter.tasks
   :members:
   :undoc-members:
   :show-inheritance:

newsletter.tests module
-----------------------

.. automodule:: newsletter.tests
   :members:
   :undoc-members:
   :show-inheritance:

newsletter.urls module
----------------------

.. automodule:: newsletter.urls
   :members:
   :undoc-members:
   :show-inheritance:

newsletter.views module
-----------------------

.. automodule:: newsletter.views
   :members:
   :undoc-members:
   :show-inheritance:

Module contents
---------------

.. automodule:: newsletter
   :members:
   :undoc-members:
   :show-inheritance:
