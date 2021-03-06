from __future__ import absolute_import, unicode_literals

import uuid

from django.contrib.auth.models import User
from django.db import models


class PrimaryAuditModel(models.Model):
    """
    To have a uuid4 as primary key
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4,
                            editable=False)

    class Meta:
        abstract = True


class TimeAuditModel(models.Model):
    """
    To track when the record was created and last modified
    """
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Created At',
                                      db_index=True)
    modified_at = models.DateTimeField(auto_now=True,
                                       verbose_name='Last Modified At')

    class Meta:
        abstract = True
        ordering = ('-created_at',)


class UserAuditModel(models.Model):
    """
    To track who created and last modified the record
    """
    created_by = models.ForeignKey(
        User,
        related_name='created_%(class)s_set',
        null=True, blank=True,
        verbose_name='Created By',
        on_delete=models.SET_NULL
    )
    modified_by = models.ForeignKey(
        User,
        related_name='updated_%(class)s_set',
        null=True, blank=True,
        verbose_name='Modified By',
        on_delete=models.SET_NULL
    )

    class Meta:
        abstract = True


class AbstractAuditModel(PrimaryAuditModel, TimeAuditModel, UserAuditModel):

    class Meta:
        abstract = True
        ordering = ('-created_at',)
