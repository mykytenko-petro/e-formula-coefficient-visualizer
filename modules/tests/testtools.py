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

    @staticmethod
    def get_pid_values():
        return [
            ([3000, 3500, 4000], 1, 0.5, 0.1, "list"),
            ([0, 3500, 7000], 1, 1, 1, "list"),
            ([3500, 3600, 3700], 0, 0, 0, [0.0, 0.0]),
            ([3000, 3100, 3200], 0.1, 0.2, 0.3, "list"),

            ("not a list", 1, 1, 1, -1),
            ([], 1, 1, 1, -2),  # пустой список
            ([3500], 1, 1, 1, -2),  # один элемент

            ([1000, 8000, 3000], 1, 1, 1, -3),  # 8000 > 7000
            ([3000, -100, 3100], 1, 1, 1, -3),  # отрицательное значение
            ([7001, 6999], 1, 1, 1, -3),        # значение выше предела

            ([0, 7000, 3500], 1, 1, 1, "list"),

            ([3000, 3100], "a", 0, 0, -1),
            ([3000, 3100], 1, None, 0, -1),
        ]
