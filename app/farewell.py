def Farewell(**kwargs):
    if 'argument' not in kwargs:
        return 'Goodbye'
    else:
        return 'Goodbye! {name}'.format(name=kwargs['argument'])
