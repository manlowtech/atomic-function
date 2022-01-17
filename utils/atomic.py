import math
from math import gcd
from functools import reduce


class Atomic:
    index_of_largest_divisorr = 0
    perfect_numbers_mag = 0
    below_junk_mag = 0
    right_junk_index = 0
    odd_numbers_mag = 0
    composite_odd_mag = 0
    duplicates_value = 0
    ps_duplicates = 0
    super_perfect_squares = 0

    def __init__(self,number):
        self.number = int(number)
        self.index_of_largest_divisor()
        self.calc_perfect_numbers()
        self.index_of_right_junk()
        self.mag_of_below_junk()
        self.composite_odd_magnitude()

    # convert even numbers to odd number ====DONE========================================
    def e_to_odd(self,numb):
        if numb % 2 == 0:
            return numb-1
        return numb

    # ============calculate gcd of a list of numbers====================================
    def calculate_list_gcd(self,n):
        x = reduce(gcd, n)
        print(x)
        return x

    def check_factor(self):
        factors = [(2*k+1) for k in range(10)]
        print(factors)
        for i in range(1,int(len(factors)/2)):
            for ele in factors:
                x = (2 * i + 1)
                if ele % x == 0:
                    print(f"{2 * i + 1} is factor")
                    continue
                else:
                    print(f"{2 * i + 1} is not factor")
                continue

    # ====================================DONE===========================================

    def index_of_largest_divisor(self):
        x = self.e_to_odd(self.number)
        n_index = self.e_to_odd(math.floor(x/3))
        y = (n_index - 1)/2
        self.index_of_largest_divisorr = int(y)
        print(f"The largest divisor is ==== {y}")
        return y

    # ============REMOVE FACTORS FROM A LIST ==============================================

    def remove_factors_in_list(self, n):
        full = n
        result = full.copy()
        for k in full:
            for j in full[full.index(k) + 1:len(full) - 2]:
                if j % k == 0:
                    print(f"{j} is a multiple of {k}")
                    result.remove(k)
                    break
        print(result)
        return result

    # ========DECOMPOSED LCM OF A LIST===================================================

    def decomposed_lcm_of_list(self,full):
        final_lcm = 1
        list_len = len(full)
        if list_len % 2 == 1:
            for k in range(0, list_len - 1, 2):
                current_lcm = int((full[k] * full[k + 1]) // math.gcd(full[k], full[k + 1]))
                print(f"current== {current_lcm}")
                final_lcm = int((current_lcm * final_lcm) // math.gcd(current_lcm, final_lcm))
                print(f"final lcm === {final_lcm}")
            return int(final_lcm * full[-1] // math.gcd(final_lcm, full[-1]))
        for k in range(0, list_len, 2):
            current_lcm = int((full[k] * full[k + 1]) // math.gcd(full[k], full[k + 1]))
            print(f"current == {current_lcm}")
            final_lcm = int((current_lcm * final_lcm) // math.gcd(current_lcm, final_lcm))
            print(f"final lcm === {final_lcm}")
        return final_lcm

    # ===================================DONE=============================================

    def index_of_right_junk(self):
        x = self.index_of_largest_divisorr - self.perfect_numbers_mag
        self.right_junk_index = int(x)
        return x

    # =========================DONE=======================================================
    def below_junk_function(self,k):
        a = self.e_to_odd(self.number)
        res = self.e_to_odd(math.floor(a / (2*k + 1))) - 1
        x = res / 2
        y = self.index_of_largest_divisorr - int(x)
        return y

    # ===================================================================DONE=============
    def mag_of_below_junk(self):
        x = sum(self.below_junk_function(k) for k in range(1,self.perfect_numbers_mag + 1))
        self.below_junk_mag = int(x)
        print(f"b junk the sum is {x}")
        return x

    # Magnitude of odd numbers ========== DONE ============================================
    def mag_of_odd_numbers(self):
        x = self.e_to_odd(self.number)
        y = math.floor(x/2)
        self.odd_numbers_mag = int(y)
        return y

    # Magnitude of even primes ======= DONE================================================
    def even_primes_mags(self):
        return 1

    # ============================================calculate duplicates in calculations ===
    def calc_duplicates(self,number):
        pass

    # =========calculating the divisors from a list ======================================
    def remove_lower_divisors(self,n):
        list_range = len(n)
        for num in range(list_range):
            for n[num] in n:
                for i in n:
                    if i % n[num] == 0:
                        del n[num]
                        break
        return n

    # ==========calculating magnitude of odd perfect numbers less than a number N, Done ============
    def calc_perfect_numbers(self):
        a = self.e_to_odd(self.number)
        sqr = math.floor(math.sqrt(a))
        x = math.floor(sqr/2)
        self.perfect_numbers_mag = int(x)
        sp = self.e_to_odd(math.floor(math.sqrt(math.sqrt(self.number)))) - 1
        sps = sp/2
        self.super_perfect_squares = int(sps)
        return x

    # ===========calculating odd composite numbers in the squares===================================
    def perfect_squares_dup_mag(self):
        pass

    # ===get Magnitude of composite numbers less than a given number =====DONE =====================
    def composite_odd_magnitude(self):
        # chooses-duplicates+perfectNumbers
        x = math.comb(self.index_of_largest_divisorr, 2)  # full body
        y = math.comb(self.right_junk_index, 2)  # right junk
        z = self.below_junk_mag
        d = self.duplicates_value # ==under study
        p = self.perfect_numbers_mag
        ps = self.ps_duplicates # under study
        b = x - y - z - d + p - ps
        self.composite_odd_mag = int(b)
        return b

    # ====get magnitude of primes less than a given number ==============DONE=====================
    def get_prime_magnitude(self):
        atomic = self.odd_numbers_mag - self.composite_odd_mag + self.even_primes_mags()
        return int(atomic)

    # ===get Magnitude of primes in a given interval=======================DONE===================
    def prime_interval(self,start,end):
        interval_mag = self.get_prime_magnitude(end) - self.get_prime_magnitude(start)
        return int(interval_mag)