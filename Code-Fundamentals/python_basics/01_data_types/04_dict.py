# What it is: unordered-by-nature-but-actually-ordered-since-3.7, mutable, key→value pairs, keys must be hashable.

a = {"name": "Kavya", "role": "engineer"}
b = dict()
c = dict(name="Kavya", role="engineer")           # keyword style
d = dict([("a", 1), ("b", 2)])                       # from a list of pairs
e = dict(zip(["x", "y", "z"], [1, 2, 3]))              # zip() pairs keys with values

print(e)   # {'x': 1, 'y': 2, 'z': 3}

d = {"name": "Kavya", "role": "engineer"}

d["name"]           # 'Kavya'
d["missing"]
# KeyError: 'missing'

d.get("missing")            # None            <- safe, no crash
d.get("missing", "N/A")      # 'N/A'            <- safe, with your own fallback

d.keys()      # dict_keys(['name', 'role'])
d.values()     # dict_values(['Kavya', 'engineer'])
d.items()       # dict_items([('name', 'Kavya'), ('role', 'engineer')])

"name" in d     # True    <- checks KEYS
"Kavya" in d     # False   <- NOT checking values!

# Update / Add — same syntax does both

d = {"name": "Kavya"}
d["name"] = "Kavya H"    # key exists -> UPDATES it
d["role"] = "engineer"     # key doesn't exist -> ADDS it
print(d)                     # {'name': 'Kavya H', 'role': 'engineer'}

d.update({"level": "senior", "role": "AI engineer"})
print(d)   # {'name': 'Kavya H', 'role': 'AI engineer', 'level': 'senior'}

# Remove
d = {"a": 1, "b": 2, "c": 3}

del d["a"]                   # {'b': 2, 'c': 3}
d.pop("b")                    # 2   -- removes & returns the value
d.pop("missing", "default_val")   # 'default_val'  -- safe pop, no crash
d.popitem()                        # ('c', 3)  -- removes the LAST inserted pair
d.clear()                           # {}

# setdefault — the "get it, or set it if missing" pattern

d = {}
d.setdefault("count", 0)
d["count"] += 1
print(d)   # {'count': 1}

d.setdefault("count", 0)     # count already exists — this does NOT reset it
print(d)                       # {'count': 1}   <- still 1, untouched

# Keys must be hashable — same rule as tuple-as-dict-key and set elements

{[1, 2]: "value"}
# TypeError: unhashable type: 'list'

{(1, 2): "value"}     # fine — tuple is hashable
# Third time this exact rule has shown up now: tuple can be a dict key, list can't. Tuple can live inside a set, list can't. Dict keys must be hashable, same requirement. It's one rule, three places.

# ⚠️ Insertion order IS preserved — unlike set
d = {}
d["z"] = 1
d["a"] = 2
d["m"] = 3
print(d)   # {'z': 1, 'a': 2, 'm': 3}   <- insertion order, not alphabetical, not hashed


from collections import defaultdict

count = defaultdict(int)   # missing key -> auto-starts at int(), which is 0
for x in arr:
    count[x] += 1
print(count)   # {1: 3, 2: 2, 3: 1}

from collections import Counter
count = Counter(arr)
print(count)   # Counter({1: 3, 2: 2, 3: 1})

dict.fromkeys(tokens)       # {'cat': None, 'dog': None, 'bird': None}
dict.fromkeys(tokens, 0)     # {'cat': 0, 'dog': 0, 'bird': 0}   <- every key gets 0

# dict.fromkeys(tokens) builds {cat: None, dog: None, bird: None} 
# (duplicates collapse automatically, since it's just repeatedly doing 
# d[key] = None, and you already know repeat insertions don't move position). 
# list(...) around the outside then converts that dict back into a plain list of just its keys, in the same order — since a dict already knows how to hand back its keys via .keys(), and wrapping in list() is what actually iterates it into a list rather than a dict_keys view object.

list(dict.fromkeys(tokens))
dict.fromkeys(tokens)       # {'cat': None, 'dog': None, 'bird': None}
dict.fromkeys(tokens, 0)     # {'cat': 0, 'dog': 0, 'bird': 0}   <- every key gets 0

# x in d (keys) → O(1) average — same as set
# x in s → O(1) average
# x in d.values() → O(n) — same as list