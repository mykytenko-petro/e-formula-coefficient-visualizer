from random import randint

class TestTools:
    @staticmethod
    def get_random_values():
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

    @staticmethod
    def get_wrong_values():
        values = []
        for i in range(0, 5):
            values.append((list([randint(-1000, -1) for i in range(0, 10)])))
        for i in range(0, 5):
            values.append((list([randint(7001, 8000) for i in range(0, 10)])))

        return values
