import json

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _

from autograph.utils import redrawSignature


class Autograph(models.Model):
    """Store Autograph details."""
    signature = models.TextField(verbose_name=_('Signature'))
    user = models.ForeignKey(User, verbose_name=_('User'), blank=True, null=True)
    timestamp = models.DateTimeField(verbose_name=_('Timestamp'), auto_now_add=True)

    class Meta:
        verbose_name_plural = 'autographs'
        ordering = ('timestamp',)

    def __unicode__(self):
        """Return human-readable representation."""
        return u"Signature for {0}, {1}".format(self.user, self.timestamp)

    def generate_signature_image(self, **kwargs):
        """Create Image of Signature based on JSON."""
        redrawSignature(self.signature, **kwargs)

    def clean(self, *args, **kwargs):
        """Verify signature JSON Format."""
        if self.signature:
            try:
                json.loads(self.signature)
            except ValueError:
                raise ValidationError('Invalid JSON format.')