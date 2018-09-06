#4bi
"""
Deleting an item from a hash table using chaining for collision resolution
--------------------------------------------------------------------------
To delete an item from a hash table that uses chaining for collision resolution,
the hash value of the item is first derived using the modulo division.
Since the chaining method places multiple items on a single slot (Implemented
with a list), a sequential search is done on the slot and item deleted when found
"""
#4bii
"""
Deleting an item from a hash table using open adressing for collision resolution
--------------------------------------------------------------------------------
To delete an item from a hash table that uses the open addressing method for
collision resolution, the hash value ofthe item is first derived using
the modulo division. If the slot is occupied already with another item, a
sequential search is done until the item is found and then deleted. This is so
since items that have their slots already occupied are placed in the next empty
slot after them.
"""
#4biii
"""

"""
