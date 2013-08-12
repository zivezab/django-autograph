import json

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _

from autograph.utils import redrawAutograph

AUTOGRAPH_JQUERY_UI_SIGNATURE = 1
AUTOGRAPH_JSIGNATURE = 2
AUTOGRAPH_TYPE_LIST = {
    (AUTOGRAPH_JQUERY_UI_SIGNATURE, _('jQuery UI Signature')),
    (AUTOGRAPH_JSIGNATURE, _('jSignature')),
}


class Autograph(models.Model):
    """Store Autograph details."""
    autograph = models.TextField(verbose_name=_('Autograph'), default='')
    autograph_type = models.PositiveIntegerField(verbose_name=_('Autograph type'), max_length=3, blank=True, null=True,
                                                 choices=sorted(AUTOGRAPH_TYPE_LIST, key=lambda item: item[0]))
    user = models.ForeignKey(User, verbose_name=_('User'), blank=True, null=True)
    timestamp = models.DateTimeField(verbose_name=_('Timestamp'), auto_now_add=True)

    class Meta:
        verbose_name_plural = 'autographs'
        ordering = ('timestamp',)

    def __unicode__(self):
        """Return human-readable representation."""
        return u"Autograph for {0}, {1}".format(self.user, self.timestamp)

    def generate_autograph_image(self, **kwargs):
        """Create Image of Autograph based on JSON."""
        return redrawAutograph(self.autograph, **kwargs)

    def clean(self, *args, **kwargs):
        """Verify autograph JSON Format."""
        if self.autograph:
            try:
                json.loads(self.autograph)
            except ValueError:
                raise ValidationError('Invalid JSON format.')