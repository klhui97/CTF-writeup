## brute force
```
- Some challenge requires brute force the password
```

### Python example
#### Random number
```
from itertools import product

# generate a permutation
permutation = product("0123456789", repeat=4)

# convert to a string array
passwordList = []
for value in permutation:
    passwordList.append(''.join(value))
```