import math


class Atomic:
    index_of_largest_divisorr = 0
    perfect_numbers_mag = 0
    below_junk_mag = 0
    right_junk_index = 0
    odd_numbers_mag = 0
    composite_odd_mag = 0
    duplicates_value = 0

    def __init__(self, number):
        self.number = int(number)
        self.index_of_largest_divisor()
        self.calc_perfect_numbers()
        self.index_of_right_junk()
        self.mag_of_below_junk()
        self.outer_sum()
        self.mag_of_odd_numbers()
        self.composite_odd_magnitude()
        self.outer_sum()

    # convert even numbers to odd number ====DONE========================================
    def e_to_odd(self, numb):
        if numb % 2 == 0:
            return numb - 1
        return numb

    # ====================================DONE==========================================
    def index_of_largest_divisor(self):
        x = self.e_to_odd(self.number)
        n_index = self.e_to_odd(math.floor(x // 3))
        y = (n_index - 1) // 2
        self.index_of_largest_divisorr = int(y)
        print(f"The largest divisor is ==== {self.index_of_largest_divisorr}")
        return y

    # ===================================DONE==========================================
    def index_of_right_junk(self):
        x = self.index_of_largest_divisorr - self.perfect_numbers_mag
        self.right_junk_index = int(x)
        return x

    # =========================DONE=====================================================
    def below_junk_function(self, k):
        a = self.e_to_odd(self.number)
        res = self.e_to_odd(math.floor(a / (2 * k + 1))) - 1
        x = res // 2
        y = self.index_of_largest_divisorr - int(x)
        return int(y)

    # ===================================================================DONE=============
    def mag_of_below_junk(self):
        x = sum(self.below_junk_function(k) for k in range(1, self.perfect_numbers_mag + 1))
        self.below_junk_mag = int(x)
        print(f"the sum of below junk is {x}")
        return x

    # Magnitude of odd numbers ========== DONE ============================================
    def mag_of_odd_numbers(self):
        x = self.e_to_odd(self.number)
        y = math.floor(x // 2)
        self.odd_numbers_mag = int(y)
        return y

    # Magnitude of even primes ======= DONE===============================================

    def v_fn(self,k,r):
        # r = k+1
        # print(f"vn k value is {r}")
        x = math.floor(self.e_to_odd(math.floor(self.number / int((2*r+1)))) / 2) - math.floor((2*r+1) / 2)
        # print(f"magnitude of odd numbers in an intervaal is x=::{x}")
        return x  # magnitude of odd numbers in a given interval

    def d_fn(self, number,k,r):
        # print(f"THE NUMBER CAUSING NOISE IN AT:::::{number}")
        # print(f"dunc k-value is {k}")
        # r = k + 1
        checker = 2*k+1
        pointer = 2*r+1
        first_occ = checker * int(math.ceil(pointer / checker))
        if(first_occ % 2 == 0):
            x = math.floor(number / 2)
            # print(f"THE NUMBER AFTER DIVIDING BY 2 IN CEIL IS {x}")
            return x
        if first_occ % 2 == 1:
            x = math.ceil(number / 2)
            # print(f"the RESULTING AFTER DIVIDING IN FLOOR BY 2 ::: {x}")
            return x

    def h_fn(self,k,r):  # multiples of x in[y,z]
        # r = k+1
        x = (math.floor(self.e_to_odd(
            math.floor(self.number / int((2*r+1)))) / (2*k+1))-int(math.ceil((2*r+1) / int((2*k+1))))+1)
        # print(f"x value on hr fn :: {x}")
        return int(x)  # to divide by 2

    def l_fn(self,k, r):
        # print(f"l fin k value is {k}") ====================MANLOW PANASHEC======ATOMIC FUNCTION=============
        # r = k+1
        checker = 2*k+1
        # print(f"checker is {checker}")
        pointer = 2*r+1
        # print(f"pointer is {pointer}")
        # print(f"k ln value is {k}")
        # print(f"pointer % checker is {pointer % checker}")
        if pointer % checker == 0:
            # print(f"i was executed for mods")
            # print(f"pointer{pointer} is cong to 0 mod ck{checker} {self.v_fn(k,r)+1}")
            return self.v_fn(k,r)+1
        h = self.h_fn(k,r)
        return self.d_fn(h,k,r)

    # the iterative sum to remove duplicates
    def iterative_inner_sum(self, k):
        x = sum(self.l_fn(k,r) for r in range(k+1, self.perfect_numbers_mag+1))
        # print(f"number innersum::{k}, x:::{x}")
        return x

    def outer_sum(self):
        lis = list()
        for k in range(1,self.perfect_numbers_mag+1):
            v = sum(self.l_fn(k,r) for r in range(k+1,self.perfect_numbers_mag+1))
            lis.append(v)
        x = sum(self.iterative_inner_sum(k) for k in range(1, self.perfect_numbers_mag))
        y = int(x)
        self.duplicates_value = y  # for N=1000, duplicates = 231
        print(f"dup value in outer sum must be {self.duplicates_value} and lis::{lis}")
        print(f"outer sum value {y}")
        return y

    # calculating magnitude of odd perfect numbers less than a number N, Done ============
    def calc_perfect_numbers(self):
        a = self.e_to_odd(self.number)
        sqr = math.floor(math.sqrt(a))
        x = int(math.floor(int(sqr) / 2))
        self.perfect_numbers_mag = int(x)
        return x

    def odd_factorial(self,start=1,end=1):
        factorial_res = 1
        for x in range(start,end+1):
            if x % 2 == 0:
                continue
            factorial_res = factorial_res*x
        return factorial_res

        # calculate duplicates in calculations ===

    def calc_duplicates(self):
        for k in range(1, self.perfect_numbers_mag):
            x = sum(self.l_fn(k, r) for r in range(k + 1, self.perfect_numbers_mag + 1))
            print(f"DUPLCATES FROM CALC DUP ==={x} pn={self.perfect_numbers_mag}")

    # ===get Magnitude of composite numbers less than a given number =====DONE ===========
    def composite_odd_magnitude(self):
        # chooses-duplicates+perfectNumbers
        x = math.comb(self.index_of_largest_divisorr, 2)  # full body
        print(f"whole body {x}")
        y = math.comb(self.right_junk_index, 2)  # right junk
        print(f"whole r junk {y}")
        z = self.below_junk_mag
        print(f"whole body below junk {z}")
        d = self.duplicates_value
        print(f"duplicates value {d}")
        p = self.perfect_numbers_mag
        print(f"perfect numbers magnitude {p}")
        print(f" x:{x} - {y} is {x-y-z-d+p}")
        b = (x-y-z+p)
        print(f"b value is :: b {b}")
        self.composite_odd_mag = int(b)
        return b

    # ====get magnitude of primes less than a given number ==============DONE===============
    def get_prime_magnitude(self):
        atomic = self.odd_numbers_mag-self.composite_odd_mag+1
        print(f"odd numbers magnitude is  {self.odd_numbers_mag}")
        print(f"atomic value is ::: {atomic}")
        return int(atomic)

    # ===get Magnitude of primes in a given interval=======================DONE=============
    def prime_interval(self, start, end):
        interval_mag = self.get_prime_magnitude(end) - self.get_prime_magnitude(start)
        return int(interval_mag)


atm = Atomic(10)
#print(f"ODD FACTORIAL IS :::: {atm.odd_factorial(5,10)}")
print(atm.calc_duplicates())
print(f"Magnitude of primes less than {atm.number} is ::: {atm.get_prime_magnitude()}")

