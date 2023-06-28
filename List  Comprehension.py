# Declare list

array = ["사과", "자두", "초코렛", "바나나", "체리"]
Output = [fruit for fruit in array if fruit != "초코렛"]

print(Output)

meter_list = [3, 7, 9, 10]
meter_square_list = [100*i for i in meter_list if i != 10]
print(meter_square_list)

result =[]
for x in range(1,10):
    if x%2 == 0:
        for y in range(1,10):
            result.append(x*y)

print(result)

result = [x*y for x in range(1,10) if x%2 == 0 for y in range(1,10)]

print(result)