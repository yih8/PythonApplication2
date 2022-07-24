numbers=[1,2,-3,4,5,7]
total=0
for num in numbers:
    assert num >0, "number must be posiive"
    total += num
    print (total)

