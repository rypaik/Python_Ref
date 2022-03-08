# Redis Python

\#redis

---

[redis-cli, the Redis command line interface – Redis](https://redis.io/topics/rediscli)

[How to install the latest Redis on macOS](https://medium.com/macoclock/how-to-install-the-latest-redis-on-macos-7ad879f66799)

[An introduction to Redis data types and abstractions – Redis](https://redis.io/topics/data-types-intro)

[Red by Echodot](https://echodot.com/red/)

## Setup

Setting up Apple Silicon

Start/Stop on M1 CLI

```Bash
brew services start redis

brew services stop redis

brew services restart redis
```

```Bash
#enters redis cli
redis-cli

# quit
```

REDIS IN BASH

CONNECTING

REDIS IN PYTHON

```python
import redis 
from config import redis_uri

r = redis.StrictRedis(url=redis_uri)
```

