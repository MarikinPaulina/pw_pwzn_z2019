def generate_fibonacci(n=100):
    if not isinstance(n, int) or n < 1:
        raise RuntimeError
    n = n if n <= 100 else 100
    fibonaci1 = 0
    yield fibonaci1
    i = 1
    fibonaci2 = 1
    while i < n:
        yield fibonaci2
        fibonaci1, fibonaci2 = fibonaci2, fibonaci1 + fibonaci2
        i += 1



if __name__ == '__main__':
    assert list(generate_fibonacci(1)) == [0]
    assert list(generate_fibonacci(2)) == [0, 1]
    assert sum(generate_fibonacci(10)) == 88
    ii = 0
    for ii in generate_fibonacci():
        pass
    assert ii == 218922995834555169026
    try:
        generate_fibonacci(0)
    except Exception as exc:
        assert isinstance(exc, RuntimeError)
