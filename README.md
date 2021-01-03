![test](https://github.com/davips/lange/workflows/test/badge.svg)
[![codecov](https://codecov.io/gh/davips/lange/branch/main/graph/badge.svg)](https://codecov.io/gh/davips/lange)

# lange
Lazy lists (i.e. Haskell-like ranges) for Python

**Arithmetic Progression**
<p>

```python3
from lange import h
print(h[0.6, 0.8, ..., 2])
# [0.6 0.8 1.0 1.2 1.4 1.6 1.8 2.0]
```

```python3
print(h[0.6, 0.8, ...][:5])
# [0.6 0.8 1.0 1.2 1.4]
```


</p>

**Geometric Progression**
<p>

```python3
from lange import h_
print(h_[0.3, 0.6, ..., 2])
# [0.3 0.6 1.2]
```

```python3
print(h_[0.3, 0.6, ...][:8])
# [0.3 0.6 1.2 2.4 4.8 9.6 19.2 38.4]
```


</p>
