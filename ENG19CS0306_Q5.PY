def uniqueUpdate(data1, data2):
    # Initially empty dictionary
    dupKeys = {}

    # Examine every (k, v2) pair in data2
    for k, v2 in data2.items():
        # Search for a key-value pair
        # with key = k in data1
        # (no such pair found yet)
        kFound = False

        for [k1, v1] in data1:
            if k1 == k:
                # Found pair with key = k
                kFound = True

                if v1 != v2:
                	# Remove (k, v1) from data1
                	data1.remove([k,v1])
                	# Add (k, [v1, v2])
                	# to dictionary
                	dupKeys[k] = [v1,v2]
  
        # After the loop, check if
        # k was not found
        if not kFound:
            # Add (k, v2) to data1
            data1.append([k, v2])

    # After processing all (k, v2) in
    # data2, return the dictionary
    return dupKeys
## DO NOT MODIFY BELOW THIS LINE! ##


import sys
if __name__ == '__main__':
    data1 = {}
    n1 = int(input())
    for _ in range(n1):
        k, v = map(int, input().split())
        if k in data1:
            sys.exit("Illegal: data1")
        data1[k] = v
    data2 = []
    n2 = int(input())
    for _ in range(n2):
        k, v = map(int, input().split())
        for [k2, v2] in data2:
            if k2 == k:
                sys.exit("Illegal: data2")
        data2.append([k, v])
dup = uniqueUpdate(data1, data2)
print(data1)
print(data2)
print(dup)
