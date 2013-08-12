from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from autograph.models import Autograph


def home(request):
    """Home page for autograph demo."""
    autograph_type = request.GET.get('type', None)
    autograph = None
    if autograph_type:
        try:
            autograph_type = int(autograph_type)
        except Exception:
            return redirect('home')
        if request.method == 'POST':
            json_string = request.POST.get('json_string', None)
            if json_string:
                Autograph.objects.create(user=request.user if request.user.is_authenticated() else None,
                                         autograph=json_string, autograph_type=autograph_type)
        try:
            autograph = Autograph.objects.filter(autograph_type=autograph_type).latest('pk')
        except Autograph.DoesNotExist:
            pass
    if autograph_type == 1:
        template = 'autograph/jQueryUISignature.html'
        selected_page = 'uisignature'
    elif autograph_type == 2:
        template = 'autograph/jSignature.html'
        selected_page = 'jsignature'
    else:
        template = 'home.html'
        selected_page = 'home'
    context = {
        'autograph': autograph,
        'selected_page': selected_page,
    }
    return render_to_response(template, context, context_instance=RequestContext(request))