m=int(input())
for i in range(m):
    no_of_std=int(input())
    sum_of_amount=0
    distribution1=0
    distribution2=0
    amount_spent=[]
    if no_of_std<1000:
        for i in range(no_of_std):
            amount_spent.append(float(input()))
            sum_of_amount+=amount_spent[i]

    avrg=sum_of_amount/no_of_std
    #print(r)
    for i in amount_spent:
        if i<avrg:
            distribution1+=avrg-i
        else:
            distribution2+=i-avrg
    if distribution1<distribution2:
            print(distribution1)
    else:
            print(distribution2)
