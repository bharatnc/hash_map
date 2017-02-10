# Test class for hashmap class - for  put(), get(), remove(), has(), and sizeof() operations
import unittest
from hashmap import HashMap

class HashMapTestCases(unittest.TestCase):
  def test_put_and_get(self):
    # New HashMap object
    HM = HashMap()

    # For Normal Inputs

    # Putting Value
    self.assertTrue(HM.put(1, "one"))
    self.assertTrue(HM.put(2, "two"))
    # Getting value
    self.assertEquals(HM.get(1), "one")
    self.assertEquals(HM.get(2), "two")

    # For Inputs with colliding hash values

    # Putting values
    self.assertTrue(HM.put(3, "three"))
    self.assertTrue(HM.put(25, "twenty-five"))
    self.assertTrue(HM.put(36, "thirty-six"))
    self.assertTrue(HM.put(47, "forty-seven"))

    # Getting values
    self.assertEquals(HM.get(3), "three")
    self.assertEquals(HM.get(25), "twenty-five")
    self.assertEquals(HM.get(36), "thirty-six")
    self.assertEquals(HM.get(47), "forty-seven")

    # For inserting different values for same key

    # Putting value
    self.assertTrue(HM.put(4, "four"))
    # Getting value
    self.assertEquals(HM.get(4), "four")

    # Putting a different value

    self.assertTrue(HM.put(4, "four-again"))
    # Getting value
    self.assertTrue(HM.get(4), "four-again")

    # Getting a value not in hashmap

    self.assertFalse(HM.get(5), "five")

    # Getting value previously declared
    self.assertTrue(HM.get(4), "four-again")

  def test_remove(self):
    HM = HashMap()

    # Removing value from hashmap
    self.assertTrue(HM.put(6, "six"))
    self.assertTrue(HM.remove(6))

    # Removing values with colliding hash value
    self.assertTrue(HM.put(3, "three"))
    self.assertTrue(HM.put(25, "twenty-five"))
    self.assertTrue(HM.put(36, "thirty-six"))
    self.assertTrue(HM.put(47, "forty-seven"))
    self.assertTrue(HM.remove(3))
    self.assertTrue(HM.remove(25))
    self.assertTrue(HM.remove(36))
    self.assertFalse(HM.has(36))
    self.assertFalse(HM.has(25))
    self.assertTrue(HM.has(47))

    # Testing again
    self.assertTrue(HM.put(25, "twenty-five"))
    self.assertTrue(HM.has(25))

    self.assertTrue(HM.remove(47))

  def test_has(self):
    # New HashMap object
    HM = HashMap()

    # For Normal Inputs

    # Putting Value
    self.assertTrue(HM.put(1, "one"))
    self.assertTrue(HM.put(2, "two"))

    # Testing has()
    self.assertTrue(HM.has(1))
    self.assertTrue(HM.has(2))

    # For Inputs with colliding hash values
    self.assertTrue(HM.put(3, "three"))
    self.assertTrue(HM.put(25, "twenty-five"))
    self.assertTrue(HM.put(36, "thirty-six"))
    self.assertTrue(HM.put(47, "forty-seven"))
    self.assertTrue(HM.has(3))
    self.assertTrue(HM.has(25))
    self.assertTrue(HM.has(36))
    self.assertTrue(HM.has(47))
    self.assertTrue(HM.has(1))
    self.assertTrue(HM.has(2))
    self.assertFalse(HM.has(4))

  def test_sizeof(self):
    HM = HashMap()

    # Size for Normal Inputs
    self.assertTrue(HM.put(1, "one"))
    self.assertTrue(HM.put(2, "two"))
    self.assertEquals(HM.sizeof(), 2)

    # Size including colliding hashes
    self.assertTrue(HM.put(3, "three"))
    self.assertTrue(HM.put(25, "twenty-five"))
    self.assertTrue(HM.put(36, "thirty-six"))
    self.assertTrue(HM.put(47, "forty-seven"))
    self.assertEquals(HM.sizeof(), 6)


if __name__ == "__main__":
  unittest.main()
