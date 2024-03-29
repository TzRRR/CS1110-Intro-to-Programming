import pocket_calculator as calc

print("Example 1:")
print(calc.get_expr()) # Note that the initial expression will always simply be "0", and no parentheses are required until an operation step() is performed
print(calc.get_value())

print("\nExample 2:")
step_1 = calc.step("+", 3)
print(calc.get_expr(), "=", step_1)
step_2 = calc.step("-", 1)
print(calc.get_expr(), "=", step_2)
step_3 = calc.step("//", 2)
print(calc.get_expr(), "=", step_3)
step_4 = calc.repeat()
print(calc.get_expr(), "=", step_4)

print(calc.clear())
print(calc.get_expr())

print("\nExample 3:")

print(calc.clear(10))
print(calc.step("*", 2))
print(calc.step("+", 1))
print(calc.repeat())
print(calc.repeat())
print(calc.get_expr())