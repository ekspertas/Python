""" Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
    реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
    создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
    Проверьте корректность полученного результата.
"""


class ComplexDigits(object):
    def __new__(cls, dig_complex):
        dig_complex = complex(dig_complex)
        sample = object.__new__(cls)
        sample.dig_complex = dig_complex
        return sample

    def __add__(self, other):
        return self.dig_complex + other.dig_complex

    def __mul__(self, other):
        return self.dig_complex * other.dig_complex


my_complex_dig_1 = ComplexDigits(4 + 6j)
my_complex_dig_2 = ComplexDigits(10 + 12j)
print(my_complex_dig_1 + my_complex_dig_2)
print(my_complex_dig_1 * my_complex_dig_2)
