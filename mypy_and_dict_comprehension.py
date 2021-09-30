from typing import Dict, Union

d1: Dict[Union[int, str], Union[int, str]] = {0: 0, 1: 1, 'a': 'a', 'b': 'b'}
print(d1)

d2: Dict[int, int] = {k: v for k, v in d1.items() if isinstance(k, int) and isinstance(v, int)}
print(d2)
