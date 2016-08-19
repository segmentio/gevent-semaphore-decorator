# gevent-semaphore-decorator

pip install gevent_semaphore_decorator

# usage

```python
from gevent_semaphore_decorator import semaphore
import requests

@semaphore(5)
def make_request():
  requests.get(...)
```

Now, only 5 requests will be made concurrently. The rest will hold without
blocking the rest of your program.
