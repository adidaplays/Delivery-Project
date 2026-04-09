from django.shortcuts import redirect


def redirect_if_logged_in(view_func):
    def get_id(request):
        if request.session.get('user_id'):
            return redirect('landing')   
        return view_func(request)
    return get_id



