import threading

class Cache:
    def __init__(self, size, eviction_policy='LRU'):
        self.size = size
        self.eviction_policy = eviction_policy
        self.cache = {}
        self.history = []
        self.eviction_policies = {'FIFO': self.evict_fifo, 'LRU': self.evict_lru, 'LIFO': self.evict_lifo}
        self.lock = threading.Lock()
  
    def set(self, key, value):
        with self.lock:
            if key in self.cache:
                self.history.remove(key)
            elif len(self.cache) >= self.size:
                if self.eviction_policy in self.eviction_policies:
                    oldest_key = self.eviction_policies[self.eviction_policy]()
                else:
                    raise ValueError(f"Invalid eviction policy: {self.eviction_policy}")
                self.cache.pop(oldest_key)
            self.cache[key] = value
            self.history.append(key)
  
    def get(self, key):
        with self.lock:
            if key in self.cache:
                if self.eviction_policy == 'LRU':
                    self.history.remove(key)
                    self.history.append(key)
                return self.cache[key]
            return "Key not present in Cache"
  
    def add_eviction_policy(self, name, policy_fn):
        with self.lock:
            self.eviction_policies[name] = policy_fn
  
    def evict_fifo(self):
        return self.history.pop(0)
  
    def evict_lru(self):
        return self.history.pop(0)
  
    def evict_lifo(self):
        return self.history.pop(-1)
