from contextlib import contextmanager


@contextmanager
def optional(cond, ctx, *args, **kwargs):
    "Optionally wrap within context manager if `cond` is true."
    if cond:
        with ctx(*args, **kwargs) as c:
            yield c
    else:
        yield
