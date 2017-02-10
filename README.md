# Python hash_map
A Python hash-map implementation implemented using simple chaining. Supports basic operations like `put(), get(),remove(), sizeOf() and has()`. Hash value for determining the position of the insert is calculated from the key of an element. Hash value is represented as `hash_val = key % self.size`. Where `size` is the total length of the hash-map.


## Importing and using the hash-map

You can start using the hash-map by importing the HashMap class. <br>
`from hashmap import HashMap` <br>

For using the HashMap class one can instantiate a new HashMap object and then use the `put(), get(),remove(), sizeOf() and has()` operations. <br>

`HM = HashMap()`<br>
`HM.put(key,value)` <br>

For a complete example please refer to the `examples.py` file.

## Tests for HashMap class

All tests to ensure that the HashMap class is error-free are available under the `test` folder as `test_hashmap.py`. Any other tests can be created and run from this file.


##Questions?

For other questions - please drop me a mail @ `bharatnc [at] gmail [dot] com`. If you find any other possible bugs - please go ahead and create a pull request. Thanks.
