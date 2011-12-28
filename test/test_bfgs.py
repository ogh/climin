import scipy

from climin import Bfgs 


quadratic = lambda x: (x**2).sum()
quadraticprime = lambda x: 2 * x
quadraticandprime = lambda x: (quadratic(x), quadraticprime(x))


def test_bfgs():
    dim = 2
    wrt = scipy.random.standard_normal((dim,)) * 10 + 5
    f = lambda: quadratic(wrt)
    fprime = lambda: quadraticprime(wrt)

    opt = Bfgs(wrt, f, fprime)
    for i, info in enumerate(opt):
        if i > 10:
            break
    assert (abs(wrt) < 0.01).all(), 'did not find solution'
