def generate(numrows):
    output=[]
    for i in range(0,numrows):
        ele=i+1
        row=[]
        for j in range(0,ele):
            if i==j or j==0:
                row.append(1)
            elif(i>=2):
                row.append(output[i-1][j-1]+output[i-1][j])
        output.append(row)
    print(output)

generate(10)