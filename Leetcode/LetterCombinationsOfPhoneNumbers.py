import itertools
def lettercombinations(digits):
    letters={2:['a','b','c'],
             3:['d','e','f'],
             4:['g','h','i'],
             5:['j','k','l'],
             6:['m','n','o'],
             7:['p','q','r','s'],
             8:['t','u','v'],
             9:['w','x','y','z']
        }
    digits=list(map(int,digits))
    
    all_letters=[]
    for i in digits:
            all_letters.append(letters[i])
    print(all_letters)
    output=[p for p in itertools.product(*all_letters)]
    output=[''.join(x) for x in output]
    print(output)    
    
    
digits="234"
lettercombinations(digits)
