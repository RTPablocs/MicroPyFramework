def Greet(**kwargs):
    if 'argument' not in kwargs:
        return 'Hello!'
    else:
        return 'Hello! {name}'.format(name=kwargs['argument'])
