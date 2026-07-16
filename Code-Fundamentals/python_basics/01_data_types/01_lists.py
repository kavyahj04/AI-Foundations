# Lists - ordered, mutable, allows duplicates, allows mixed types.

# append/insert/extend/remove/pop/sort/reverse/clear → these mutate. You'll use append and pop so often they'll stick automatically.

# Anything that looks like a standalone function (sorted, reversed, len, sum) → doesn't mutate, gives you something back.


# Create 

a = [1, 2, 3]
b = list()
c = list(range(5))          # [0, 1, 2, 3, 4]
mixed = [1, "two", 3.0, True]   # mixed types are fine

# Access

nums = [10, 20, 30, 40, 50]
nums[0]        # 10
nums[-1]       # 50              — last item
nums[1:3]      # [20, 30]        — slice
nums[:2]       # [10, 20]        — from start
nums[::2]      # [10, 30, 50]    — every 2nd item
nums[::-1]     # [50, 40, 30, 20, 10]   — reversed copy

nums[::1]    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]   — every element, in order
nums[::2]    # [0, 2, 4, 6, 8]                   — every 2nd element
nums[::3]    # [0, 3, 6, 9]                       — every 3rd element
nums[::-1]   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]     — every element, backward = full reverse
nums[::-2]   # [9, 7, 5, 3, 1]                     — every 2nd element, backward
# nums[::0]    # ValueError: slice step cannot be zero

# Update

nums[0] = 999                # [999, 20, 30, 40, 50]
nums[1:3] = [21, 31]         # [999, 21, 31, 40, 50]  — replace a slice
nums[1:3] = [1, 2, 3, 4]     # [999, 1, 2, 3, 4, 40, 50]  — slice assign can change the LENGTH

# Add

nums = [10, 20, 30]

nums.append(40)          # add one item to the end
print(nums)              # [10, 20, 30, 40]

nums.insert(1, 99)        # insert at a specific index, shifts everything right
print(nums)                # [10, 99, 20, 30, 40]   <- 99 pushed 20,30,40 one step right

nums.extend([50, 60])     # add multiple items, in place
print(nums)                # [10, 99, 20, 30, 40, 50, 60]

nums + [70, 80]           # returns a NEW list — does NOT change nums
print(nums + [70, 80])      # [10, 99, 20, 30, 40, 50, 60, 70, 80]   <- the new combined list
print(nums)                  # [10, 99, 20, 30, 40, 50, 60]           <- nums itself is untouched


# Remove

nums.remove(20)     # deletes the FIRST 20 it finds — error if value isn't there
nums.pop()           # removes & returns the LAST item
nums.pop(0)          # removes & returns the item at index 0
del nums[0]          # removes by index, returns nothing
nums.clear()         # empties the whole list → []

# Other methods
nums.index(10)    # 1     — position of FIRST 10
nums.count(10)    # 2     — how many 10s exist
nums.sort()       # sorts IN PLACE, returns None (don't do `nums = nums.sort()` — that gives you None!)
nums.reverse()    # reverses IN PLACE, returns None

original = [1, 2, 3]
alias = original          # NOT a copy. Same list, two names pointing at it.
alias.append(4)
print(original)            # [1, 2, 3, 4]  <- original changed too!

safe_copy = original.copy()
safe_copy.append(999)
print(original)             # [1, 2, 3, 4]  <- unaffected this time
print(safe_copy)             # [1, 2, 3, 4, 999]


nums = [1,2,3,4,5,6,7,8,9,10,11]

print(nums[::10])