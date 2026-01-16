def convertor_fahrenheit(celsius):
    return (celsius * 9 /5) +32
def convertor_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 /9 

opção = input("digite ai zé 'f' pra fahrnei e 'c' para celso ")
if opção == 'c':
    temp_C = float(input('digite a temperatura em celsius: '))
    temp_fah = convertor_celsius(temp_C)
    print(f'{temp_C}°C = {temp_fah:.2f}°F ')

elif opção == 'f':
    temp_fah = float(input('digita essa merda '))
    temp_C = convertor_fahrenheit(temp_fah)
    print(f'{temp_fah}°F = {temp_C}°C')
