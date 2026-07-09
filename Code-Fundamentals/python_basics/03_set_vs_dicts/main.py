print(type({}))       # <class 'dict'>   -- {} alone is ALWAYS dict, never set
print(type(set()))     # <class 'set'>    -- only way to write an empty set
print(type({1,2,3}))    # <class 'set'>    -- values with no colons = set
print(type(dict()))      # <class 'dict'>   -- same as {}

d = {"name": "Kavya", "role": "engineer"}
d.get("role")            # 'engineer'
d.get("missing")          # None            -- safe, no crash
d.get("missing", "NA")     # 'NA'             -- your own fallback

d.items()    # dict_items([('name', 'Kavya'), ('role', 'engineer')])
d.keys()      # dict_keys(['name', 'role'])
d.values()     # dict_values(['Kavya', 'engineer'])


            # The rule that ties both questions together:

# Membership check (x in d.keys() vs x in d.values()) → keys win, O(1) vs O(n), because hashing lets you skip straight to the answer instead of searching.
# Full iteration (for x in d.keys() vs for x in d.values()) → tied, O(n) vs O(n), because there's no "skipping" to do when you're visiting everything anyway.