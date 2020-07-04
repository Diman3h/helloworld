from contextvars import ContextVar
from functools import partial

import httpx

from ..utils import progress

Progress: ContextVar[progress] = ContextVar('Prog')


async def request(method: str, url: str, *args, timeout: int = 30, **kwargs):
    try:
        return await httpx.request(
            method, url, *args, timeout=timeout, **kwargs
        )
    finally:
        prog = Progress.get()
        prog(url)


get = partial(request, 'GET')
post = partial(request, 'POST')