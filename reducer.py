ip = open("shivaram02.txt", "r") # open file, write
op = open("shivaram03.txt", "w") # open file, write

thisKey = ""
thisValue  = 0

for line in ip:
    data = line.strip().split('\t')
    store, amount = data

    if store != thisKey:
        if thisKey:
     # output the last key value pair result
            op.write(thisKey + '\t' + str(thisValue)+'\n')

   # start over when changing keys
    thisKey = store
    thisValue = 0.0
 # apply the aggregation function
    thisValue += float(amount)
ip.close()
op.close()