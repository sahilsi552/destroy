
from asyncio import gather
import requests as session


async def get(url: str, *args, **kwargs):
    resp=session.get(url, *args, **kwargs)
    try:
        data = resp.json()
    except Exception:
        data = resp.text()
    return data


async def head(url: str, *args, **kwargs):
    resp=session.head(url, *args, **kwargs)
    try:
        data = resp.headers
    except Exception:
        data =  resp.text()
    return data


async def post(url: str, *args, **kwargs):
    resp=session.post(url, *args, **kwargs)
    try:
        data =  resp.json()
    except Exception:
        data =  resp.text()
    return data


async def multiget(url: str, times: int, *args, **kwargs):
    return await gather(*[get(url, *args, **kwargs) for _ in range(times)])


async def multihead(url: str, times: int, *args, **kwargs):
    return await gather(*[head(url, *args, **kwargs) for _ in range(times)])


async def multipost(url: str, times: int, *args, **kwargs):
    return await gather(*[post(url, *args, **kwargs) for _ in range(times)])


async def resp_get(url: str, *args, **kwargs):
    return session.get(url, *args, **kwargs)


async def resp_post(url: str, *args, **kwargs):
    return  session.post(url, *args, **kwargs)