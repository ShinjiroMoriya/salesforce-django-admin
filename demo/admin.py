# django-salesforce
#
# by Phil Christensen
# (c) 2012-2013 Freelancers Union (http://www.freelancersunion.org)
# See LICENSE.md for details
#

from django.contrib import admin
from demo import models
from demo.univasal_admin import register_omitted_classes

register_omitted_classes(models)
