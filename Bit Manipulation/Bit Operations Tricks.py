"""
Few Operations or Expressions are useful in bit manipulation.

X ^ 0 = X     X & 0 = 0    X | 0 = X
X ^ 1 = ~x    X & 1 = X    X | 1 = 1
X ^ X = 0     X & X = X    X | X = X

"""
__author__ = 'abhireddy96'


# Get Bit
# Shifts loWer by i bits, by performing an AND with num,
# Clear all bits other than the bit at bit i. Finally, we compare that to 0.
# If that new value is not zero,then bit i must have a 1. Otherwise, bit i is a 0.
def get_bit(num, i):
    return (num & (1 << i)) != 0


# SetBit
# Shifts lower by i bits, by performing an OR with num,
# Only the value at bit i will change. All other bits of the mask are zero and will not affect num.
def set_bit(num, i):
    return num | (1 << i)


# Clear Bit
# Reverse of setBit, Creating the reverse of it and negating it.
# Then, perform an AND with num. This will clear the ith bit and leave the remainder unchanged.
def clear_bit(num, i):
    return num & ~(1 << i)


# Create a mask with a 1 at the ith bit (1<< i).
# Then, we subtract 1 from it, giving us a sequence of 0s followed by i 1s.
# Then AND our number with this mask to leave just the last i bits.
def clear_bits_msb_through_i_inclusive(num, i):
    return num & ((1 << i) - 1)


# Take a sequence of all 1s (which is -1) and shift it left by i+1 bits.
# This gives sequence of 1 s (in the most significant bits) followed by i 0 bits.
def clear_bits_i_through_0_inclusive(num, i):
    return num & ~((1 << (i + 1)) - 1)


# Update Bit
# To set the ith bit to a value v, first clear the bit at position i by using a mask
# Then, shift the intended value v, left by i bits.
# This will create a number with bit i equal to v and all other bits equal to 0.
# Finally, OR these two numbers, updating the ith bit if v is 1 and leaving it as 0
# otherwise.
def update_bit(num, i, bit):
    return (num & ~(1 << i)) + (bit << i)
