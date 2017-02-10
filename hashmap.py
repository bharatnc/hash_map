# Python class for storing hash values
# Operations: put(), get(),remove(), sizeOf(),has()

class HashMap:
  def __init__(self):
    self.size = 11
    self.data = [None] * self.size

  def hashing_function(self, key):
    hash_val = key % self.size
    return hash_val

  def put(self, key, data):
    hash = self.hashing_function(key)
    if self.data[hash] == None:
      self.data[hash] = [[key, data]]
      return self.data
    elif self.data[hash] != None:
      sub_list = []
      old_val = []
      old_val = self.data[hash]
      for i in old_val:
        sub_list.append(i)
      if sub_list[0][0] == key:
        sub_list[0][1] = data
      else:
        sub_list.append([key, data])
        self.data[hash] = sub_list
      return self.data

  def get(self, key):
    hash = self.hashing_function(key)
    if self.data[hash] == -1:
      return False
    else:
      if self.data[hash] != None:
        for i in self.data[hash]:
          for j in i:
            if j == key:
              return i[1]
      else:
        return False

  def remove(self, key):
    hash = self.hashing_function(key)
    if self.data[hash] == None:
      return False
    else:
      for i in xrange(len(self.data[hash])):
        if key in self.data[hash][i]:
          del self.data[hash][i]
          print self.data
          return True
    return False

  def has(self, key):
    hash = self.hashing_function(key)
    if self.data[hash] == None:
      return False
    elif self.data[hash] != None:
      val = self.data[hash]
      for i in val:
        if key in i:
          return True
      return False

  def sizeof(self):
    tot_len = 0
    for i in self.data:
      if i != None:
        l = len(i)
        tot_len = tot_len + l
    return tot_len
