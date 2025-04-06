
# def make_binary(n):
#     cur = 0
#     tmp = n
#     ctr = 1
#     while tmp > 0:
#         cur += tmp % 2 * ctr
#         ctr *= 10
#         tmp = int(tmp/2)
#     return cur

# I started by making a binary representation over and over - but once I made this algorithm I realized it is going
# to be slower than incrementing a binary representation
# def concatenatedBinary(n):
#     current_binary_value = [0]
#     concatenation = ""
#     for _ in range(0,n):
#         flip = True
#         for j in range(0, len(current_binary_value)):
#             if current_binary_value[j] == 1 and flip:
#                 current_binary_value[j] = 0
#             elif flip:
#                 current_binary_value[j] = 1
#                 flip = False
#                 break
#         if flip:
#             current_binary_value.append(1)
#         concatenation += ''.join(str(bit) for bit in reversed(current_binary_value))
#     print(concatenation)
#     res = 0
#     mod = 10**9 +7
#     print(mod)
#     for bit in concatenation:
#         res = (res*2 + int(bit)) % mod
#
#     return res

# this can def be done faster than the above this is just a starting algorithm to prove I can do it - now lets try bit
# wise manipulation

def concatenatedBinary(n):
    mod = 10**9+7
    res = 0
    length = 0
    for i in range(1, n + 1):
        # If i is a power of 2, increase the binary length
        if i & (i - 1) == 0:
            length += 1
        res = ((res << length) | i) % mod
    return res

print(concatenatedBinary(12))
# 505379714

# Lesson for future me - take some time to get better at the bitwise operators - I should be reaching to them instantly
# when I see a problem like this in the future. This is a familiarity problem not an understanding issue