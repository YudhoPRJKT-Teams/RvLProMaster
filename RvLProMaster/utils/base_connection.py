import asyncio
import aiohttp

class SyncClientResponse:
    def __init__(self, data, status):
        self._data = data
        self._status = status

    def json(self):
        return self._data

    def status(self):
        return self._status


class BaseConnection:
    def __enter__(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        self.session = self.loop.run_until_complete(self._create_session())
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.loop.run_until_complete(self.session.close())
        self.loop.close()

    async def _create_session(self):
        return aiohttp.ClientSession()

    def post(self, url, **kwargs):
        return self.loop.run_until_complete(self._post(url, **kwargs))

    async def _post(self, url, **kwargs):
        async with self.session.post(url, **kwargs) as resp:
            data = await resp.json()
            return SyncClientResponse(data, resp.status)
