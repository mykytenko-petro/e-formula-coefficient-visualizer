from random import randint

class TestTools:
    @staticmethod
    def get_random_values_for_get_errors():
        values = []
        for i in range(0, 10):
            original_vals = []
            error_vals = []
            for k in range(0, 10):
                num = randint(0, 7000)
                original_vals.append(num)
                error_vals.append(num-3500)
            values.append((original_vals, error_vals))
        return values

print(TestTools.get_random_values_for_get_errors())
