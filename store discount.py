def apply_discount(total, status, code):
    discount = 0.0
    if status == True:
        discount = discount + 0.10
    if code == "SAVE15":
        discount = discount + 0.15
    savings = total * discount
    final = total - savings
    return savings, final
saved, final = apply_discount(100.0, True, "SAVE15")
print("savings:", saved)
print("final price:", final)
