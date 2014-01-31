def typer(x):
    '''
    reutnrs datatype for x (limited use)
    '''

    if type(x) == int:
        print('This is an int')
    elif type(x) == str:
        print('This is a str')
    else:
        print('neither')

print(typer(200))
