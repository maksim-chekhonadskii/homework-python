a = int(input("введите результаты пробежки первого дня в км "))
b = int(input("введите общий желаемый результат в км "))
result_days = 1
result_km = a
while result_km < b:
        a = a + 0.1 * a
        result_days += 1
        result_km = result_km + a
print(f"вы достигнете показателей на %.d день" % result_days)