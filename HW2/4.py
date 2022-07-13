age = int(input("Ваш возраст?: "))

if age <= 13:
    print("детство")

elif age >= 14 and age <= 24:
    print("молодость")

elif age >= 25 and age <= 59:
    print("зрелость")

elif age >= 60:
    print("старость")