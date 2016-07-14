"""
Django migrations for user_sessions app

This package does not contain South migrations.  South migrations can be found
in the ``south_migrations`` package.

Source: http://treyhunner.com/2014/03/migrating-to-django-1-dot-7/
"""

SOUTH_ERROR_MESSAGE = """\n
For South support, customize the SOUTH_MIGRATION_MODULES setting like so:

    SOUTH_MIGRATION_MODULES = {
        'user_sessions': 'user_sessions.south_migrations',
    }
"""

# Ensure the user is not using Django 1.6 or below with South
try:
    from django.db import migrations  # noqa
except ImportError:
    from django.core.exceptions import ImproperlyConfigured
    raise ImproperlyConfigured(SOUTH_ERROR_MESSAGE)
