def body_serve(**kwargs):
    if not kwargs['body']:
        return 'Empty Response'
    else:
        return kwargs['body']
