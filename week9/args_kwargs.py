def f(*args, **kwargs):
    print("Positional:", args)


f(100, 50, 25)

def f1(*args, **kwargs):
    print("Named:", kwargs)


f1(galleons=100, sickles=50, knuts=25)