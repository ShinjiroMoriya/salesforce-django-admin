# django-salesforce
#
# by Phil Christensen
# (c) 2012-2013 Freelancers Union (http://www.freelancersunion.org)
# See LICENSE.md for details
#

from __future__ import absolute_import, unicode_literals
from salesforce import models
from salesforce.models import SalesforceModel as SalesforceModelParent

import django
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible


# This class customizes `managed = True` for tests and does not disturbe SF
class SalesforceModel(SalesforceModelParent):
    class Meta:
        abstract = True
        managed = True


class SalesforceParentModel(SalesforceModel):
    """
    Example of standard fields present in all custom models.
    """
    # This is not a custom field because is not defined in a custom model.
    # The API name is therefore 'Name'.
    name = models.CharField(max_length=80)
    last_modified_date = models.DateTimeField(sf_read_only=models.READ_ONLY)
    # This model is not custom because it has not an explicit attribute
    # `custom = True` in Meta and also has not a `db_table` that ends with
    # '__c'.

    class Meta:
        abstract = True


class HakkouzumiCoupon(SalesforceParentModel):
    Aitemu = models.CharField(max_length=80, db_column='Aitemu__c')
    TestGazoo = models.CharField(max_length=80, db_column='TestGazoo__c')
    TestZansu = models.CharField(max_length=80, db_column='TestZansu__c')
    Zansusho = models.CharField(max_length=80, db_column='Zansusho__c')
    QRCode = models.CharField(max_length=80, db_column='QRCode__c')
    EventShopMaster = models.CharField(max_length=80, db_column='EventShopMaster__c')
    TorihikisakiMei = models.CharField(max_length=80, db_column='TorihikisakiMei__c')
    ServiceNaiyo = models.CharField(max_length=80, db_column='ServiceNaiyo__c')
    Pointoriyou = models.CharField(max_length=80, db_column='Pointoriyou__c')
    HansokuEvent = models.CharField(max_length=80, db_column='HansokuEvent__c')
    Riyoukaishibi = models.CharField(max_length=80, db_column='Riyoukaishibi__c')
    RiyouzumiCheck = models.CharField(max_length=80, db_column='RiyouzumiCheck__c')
    Riyoushuryoubi = models.CharField(max_length=80, db_column='Riyoushuryoubi__c')

    class Meta:
        custom = True
        db_table = 'HakkouzumiCoupon__c'

    def __str__(self):
        return self.name


class EventPromotion(SalesforceParentModel):
    EventDetail = models.CharField(max_length=80, db_column='EventDetail__c')

    class Meta:
        custom = True
        db_table = 'EventPromotion__c'

    def __str__(self):
        return self.name


class EventShopMaster(SalesforceParentModel):

    HakkouKaisuu = models.CharField(max_length=80, db_column='HakkouKaisuu__c')
    CouponRiyouKaisuu = models.CharField(max_length=80, db_column='CouponRiyouKaisuu__c')
    Service = models.CharField(max_length=80, db_column='Service__c')
    SankaTenpo = models.CharField(max_length=80, db_column='SankaTenpo__c')
    Jissibi = models.CharField(max_length=80, db_column='Jissibi__c')
    Shuryoubi = models.CharField(max_length=80, db_column='Shuryoubi__c')
    HansokuEvent = models.ForeignKey(EventPromotion, db_column='HansokuEvent__c', on_delete=models.DO_NOTHING)

    class Meta:
        custom = True
        db_table = 'EventShopMaster__c'
