from app.response import ResponseFactory

def Farewell(**kwargs):
    response = ResponseFactory()
    if 'argument' not in kwargs:
        data = 'goodbye'
        return response.ok_response(action=data)
    else:
        return 'Goodbye! {name}'.format(name=kwargs['argument'])
