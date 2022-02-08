# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['starsessions', 'starsessions.backends']

package_data = \
{'': ['*']}

install_requires = \
['itsdangerous>=2.0.1,<3.0.0', 'starlette>=0,<1']

extras_require = \
{'redis': ['aioredis>=2.0.0,<3.0.0']}

setup_kwargs = {
    'name': 'starsessions',
    'version': '1.2.3',
    'description': 'Pluggable session support for Starlette.',
    'long_description': '## Pluggable session support for Starlette and FastAPI frameworks\n\nThis package is based on this long standing [pull request](https://github.com/encode/starlette/pull/499) in the\nmainstream by the same author.\n\n## Installation\n\nInstall `starsessions` using PIP or poetry:\n\n```bash\npip install starsessions\n# or\npoetry add starsessions\n```\n\nUse `redis` extra for [Redis support](#redis).\n\n## Quick start\n\nSee example application in [`examples/`](examples) directory of this repository.\n\n## Enable session support\n\nIn order to enable session support add `starsessions.SessionMiddleware` to your application.\n\n```python\nfrom starlette.applications import Starlette\nfrom starlette.middleware import Middleware\nfrom starsessions import SessionMiddleware\n\nmiddleware = [\n    Middleware(SessionMiddleware, secret_key=\'TOP SECRET\'),\n]\n\napp = Starlette(middleware=middleware, **other_options)\n```\n\n### Session autoloading\n\nNote, for performance reasons session won\'t be autoloaded by default, you need to explicitly\ncall `await request.session.load()` before accessing the session otherwise `SessionNotLoaded` exception will be raised.\nYou can change this behavior by passing `autoload=True` to your middleware settings:\n\n```python\nMiddleware(SessionMiddleware, secret_key=\'TOP SECRET\', autoload=True)\n```\n\n### Cookie path\n\nYou can pass `path` arguments to enable session cookies on specific URLs. For example, to activate session cookie only\nfor admin area (which is hosted under `/admin` path prefix), use `path="/admin"` middleware argument.\n\n```python\nMiddleware(SessionMiddleware, path = \'/admin\', ...)\n```\n\nAll other URLs not matching value of `path` will not receive cookie thus session will be unavailable.\n\n### Cookie domain\n\nYou can also specify which hosts can receive a cookie by passing `domain` argument to the middleware.\n\n```python\nMiddleware(SessionMiddleware, domain = \'example.com\', ...)\n```\n\n> Note, this makes session cookie available for subdomains too.\n> For example, when you set `domain=example.com` then session cookie will be available on subdomains like `app.example.com`.\n\n### Session-only cookies\n\nIf you want session cookie to automatically remove from tbe browser when tab closes then set `max_age` to `0`:\n\n```python\nMiddleware(SessionMiddleware, max_age=0, ...)\n```\n\n### Default session backend\n\nThe default backend is `CookieBackend`. You don\'t need to configure it just pass `secret_key` argument and the backend\nwill be automatically configured for you.\n\n## Change default backend\n\nWhen you want to use a custom session storage then pass a desired backend instance via `backend` argument of the\nmiddleware.\n\n```python\nfrom starlette.applications import Starlette\nfrom starlette.middleware.sessions import SessionMiddleware\nfrom starlette.sessions import CookieBackend\n\nbackend = CookieBackend(secret_key=\'secret\', max_age=3600)\n\napp = Starlette()\napp.add_middleware(SessionMiddleware, backend=backend)\n```\n\n## Built-in backends\n\n### Memory\n\nClass: `starsessions.InMemoryBackend`\n\nSimply stores data in memory. The data is cleared after server restart. Mostly for use with unit tests.\n\n### CookieBackend\n\nClass: `starsessions.CookieBackend`\n\nStores session data in a signed cookie on the client. This is the default backend.\n\n### Redis\n\nClass: `starsessions.backends.redis.RedisBackend`\n\n> Requires [aioredis](https://aioredis.readthedocs.io/en/latest/getting-started/),\n> use `pip install starsessions[redis]` or `poetry add starsessions[redis]`\n\nStores session data in a Redis server. The backend accepts either connection URL or an instance of `aioredis.Redis`.\n\n```python\nimport aioredis\nfrom starsessions.backends.redis import RedisBackend\n\nbackend = RedisBackend(\'redis://localhost\')\n# or\nredis = aioredis.from_url(\'redis://localhost\')\n\nbackend = RedisBackend(connection=redis)\n```\n\n## Custom backend\n\nCreating new backends is quite simple. All you need is to extend `starsessions.SessionBackend`\nclass and implement abstract methods.\n\nHere is an example of how we can create a memory-based session backend. Note, it is important that `write` method\nreturns session ID as a string value.\n\n```python\nfrom starlette.sessions import SessionBackend\nfrom typing import Dict\n\n\n# instance of class which manages session persistence\n\nclass InMemoryBackend(SessionBackend):\n    def __init__(self):\n        self._storage = {}\n\n    async def read(self, session_id: str) -> Dict:\n        """ Read session data from a data source using session_id. """\n        return self._storage.get(session_id, {})\n\n    async def write(self, data: Dict, session_id: str = None) -> str:\n        """ Write session data into data source and return session id. """\n        session_id = session_id or await self.generate_id()\n        self._storage[session_id] = data\n        return session_id\n\n    async def remove(self, session_id: str):\n        """ Remove session data. """\n        del self._storage[session_id]\n\n    async def exists(self, session_id: str) -> bool:\n        return session_id in self._storage\n```\n\n## Serializers\n\nSometimes you cannot pass raw session data to the backend. The data must be serialized into something the backend can\nhandle.\n\nSome backends (like `RedisBackend`) optionally accept `serializer` argument that will be used to serialize and\ndeserialize session data. By default, we provide (and use) `starsessions.JsonSerializer` but you can implement your own\nby extending `starsessions.Serializer` class.\n',
    'author': 'alex.oleshkevich',
    'author_email': 'alex.oleshkevich@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/alex-oleshkevich/starsessions',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
