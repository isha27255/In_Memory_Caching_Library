# In_Memory_Caching_Library

Here's an implementation for an in-memory cache with support for multiple `standard eviction policies ( LRU, FIFO, LIFO )` and `custom eviction policies`.

The cache implements the dictionary data structure to store key-value pairs. The history list keeps track of the keys in the order they were accessed. The eviction policy is specified at initialization, and the set method evicts the oldest key if the cache size has been exceeded. The get method updates the history of a key if it exists in the cache. 

There is `eviction_policies` dictionary, which is used to store custom eviction policies added using the add_eviction_policy method.The `add_eviction_policy` method allows for custom eviction policies to be added to the cache.The custom eviction policies must take the form of functions that return the key of the item to be evicted, based on the custom policy's logic.

To make the cache thread-safe, I have used the `threading` module in Python and used locks to synchronize access to the cache.

Here's an example of how you can use the cache with different eviction policies:

```
# Example 1: FIFO Cache
cache = Cache(size=3, eviction_policy='FIFO')
cache.set(1, 'one')
cache.set(2, 'two')
cache.set(3, 'three')
print(cache.cache) # Output: {1: 'one', 2: 'two', 3: 'three'}

cache.set(4, 'four')
print(cache.cache) # Output: {2: 'two', 3: 'three', 4: 'four'}
```
```
# Example 2: LRU Cache
cache = Cache(size=3, eviction_policy='LRU')
cache.set(1, 'one')
cache.set(2, 'two')
cache.set(3, 'three')
print(cache.cache) # Output: {1: 'one', 2: 'two', 3: 'three'}

cache.get(1) # Output: 'one'
cache.set(4, 'four')
print(cache.cache) # Output: {1: 'one', 3: 'three', 4: 'four'}
```
```
# Example 3: LIFO Cache
cache = Cache(size=3, eviction_policy='LIFO')
cache.set(1, 'one')
cache.set(2, 'two')
cache.set(3, 'three')
print(cache.cache) # Output: {1: 'one', 2: 'two', 3: 'three'}

cache.set(4, 'four')
print(cache.cache) # Output: {1: 'one', 2: 'two', 4: 'four'}
```
```
# Example 4: Custom Eviction Policy
def custom_policy(history):
    return history.pop(1)

cache = Cache(size=3, eviction_policy='CUSTOM')
cache.add_eviction_policy('CUSTOM', custom_policy)
cache.set(1, 'one')
cache.set(2, 'two')
cache.set(3, 'three')
print(cache.cache) # Output: {1: 'one', 2: 'two', 3: 'three'}

cache.set(4, 'four')
print(cache.cache) # Output: {1: 'one', 3: 'three', 4: 'four'}

```
