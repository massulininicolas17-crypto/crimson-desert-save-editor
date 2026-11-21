# Extension API

An extension is any Python object exposing:

```python
class MyExt:
    name = "my_ext"
    commands = ["my.verb"]
    def handle(self, payload: dict) -> dict: ...
```

Drop a `.cdse_ext` file in `plugins/`:

```python
from my_pkg.my_ext import MyExt
```

The host loads each `.cdse_ext` with `importlib`, scans for classes whose
`__module__` matches the shim, and registers them. Command verbs must be
unique across the whole host — collisions raise at boot.