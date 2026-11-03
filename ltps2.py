class NoAlphabetError(Exception):
    pass
class NoSpaceError(Exception):
    pass
class NoNegativeError(Exception):
    pass

class LTPS:
    def __init__(self, l, t, p, s):
        self.l = float(l)
        self.t = float(t)
        self.p = float(p)
        self.s = float(s)

        if self.l < 0:
            raise NoNegativeError("Lecture attendance cannot be negative")
        if self.t < 0:
            raise NoNegativeError("Tutorial attendance cannot be negative")
        if self.p < 0:
            raise NoNegativeError("Practical attendance cannot be negative")
        if self.s < 0:
            raise NoNegativeError("Skilling attendance cannot be negative")

    def calculate(self):
        weighted_sum = (self.l * 100) + (self.t * 25) + (self.p * 50) + (self.s * 25)

        total_weight = 0
        if self.l > 0: total_weight += 100
        if self.t > 0: total_weight += 25
        if self.p > 0: total_weight += 50
        if self.s > 0: total_weight += 25

        if total_weight == 0:
            print("Error: Please enter at least one value")
            return

        overall = weighted_sum / total_weight

        print("\n" + "="*45)
        print(f"Lecture   (100%) : {self.l:.2f}%")
        print(f"Tutorial  (25%)  : {self.t:.2f}%")
        print(f"Practical (50%)  : {self.p:.2f}%")
        print(f"Skilling  (25%)  : {self.s:.2f}%")
        print("-" * 45)
        print(f"Overall LTPS Attendance : {overall:.2f}%")
        print("="*45)


try:
    l = input("Enter Lecture attendance (%): ").strip()
    t = input("Enter Tutorial attendance (%): ").strip()
    p = input("Enter Practical attendance (%): ").strip()
    s = input("Enter Skilling attendance (%): ").strip()

    for val, name in zip([l, t, p, s], ["Lecture", "Tutorial", "Practical", "Skilling"]):
        if any(c.isalpha() for c in val):
            raise NoAlphabetError(f"{name} component should not contain alphabets/letters")

    cal = LTPS(l, t, p, s)
    cal.calculate()

except NoAlphabetError as e:
    print("Error:", e)
except NoNegativeError as e:
    print("Error:", e)
except ValueError:
    print("Error: Please enter valid numbers only (no letters or special characters)")
except Exception as e:
    print("Unexpected Error:", e)