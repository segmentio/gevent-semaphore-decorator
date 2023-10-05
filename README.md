# gevent-semaphore-decorator

> **Note**  
> Segment has paused maintenance on this project, but may return it to an active status in the future. Issues and pull requests from external contributors are not being considered, although internal contributions may appear from time to time. The project remains available under its open source license for anyone to use.

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
