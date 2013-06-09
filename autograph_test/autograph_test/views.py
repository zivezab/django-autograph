import os
from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext

from autograph.models import Autograph

def home(request):
    """Home page for signature demo."""
    if request.method == 'POST':
        json_string = request.POST.get('json_string', None)
        if json_string:
            Autograph.objects.create(user=request.user if request.user.is_authenticated() else None,
                                     signature=json_string)
    image_name = None
    signature = None
    try:
        signature = Autograph.objects.latest('pk')
    except Autograph.DoesNotExist:
        pass
    else:
        image_name = signature.timestamp.strftime("%Y%m%d%H%M%S")
        if not os.path.exists('%s/%s' % (settings.MEDIA_ROOT, image_name)):
            try:
                signature.generate_signature_image(im_output_dir=settings.MEDIA_ROOT,
                                                   im_output_name='/%s' % (image_name))
            except:
                pass
    context = {
        'signature': signature,
        'image_name': image_name,
    }
    return render_to_response('home.html', context, context_instance=RequestContext(request))
