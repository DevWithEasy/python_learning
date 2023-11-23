#find odd and even number from n-th number

def odd_even(n) :
    odd = []
    even = []

    for i in range(0,n) :
        if i > 0 :
            if  i % 2 == 0 :
                even.append(i)
            else :
                odd.append(i)
    
    return {
        'odd' : odd,
        'even' : even
    }

print(odd_even(10))