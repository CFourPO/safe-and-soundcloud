import soundcloud


def sc_user_proc(request):
    if not request.user.is_authenticated:
        return {}
    else:
        user = request.user
        access_token = user.access_token
        client = soundcloud.Client(access_token=access_token)
        sc_user_data = client.get('/me').obj

        return {
            'client': client,
            'user': request.user,
            'sc_user_data': sc_user_data
        }
