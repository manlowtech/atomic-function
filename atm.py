from utils import Atomic
import math

nums = [(2*k+1) for k in range(1,10000)]
#for k in range(0,len(nums),2):
    #print(nums[k])


def evs(full):
    final_lcm = 1
    list_len = len(full)
    if list_len%2 == 1:
        for k in range(0, list_len-1, 2):
            current_lcm = int((full[k] * full[k + 1]) // math.gcd(full[k], full[k + 1]))
            print(f"current== {current_lcm}")
            final_lcm = int((current_lcm * final_lcm) // math.gcd(current_lcm, final_lcm))
            print(f"final lcm === {final_lcm}")
        return int(final_lcm*full[-1]//math.gcd(final_lcm,full[-1]))
    for k in range(0, list_len, 2):
        current_lcm = int((full[k] * full[k + 1]) // math.gcd(full[k], full[k + 1]))
        print(f"current == {current_lcm}")
        final_lcm = int((current_lcm * final_lcm) // math.gcd(current_lcm, final_lcm))
        print(f"final lcm === {final_lcm}")
    return final_lcm
print(nums)
print(evs(nums))
