f=open('poem.txt')
while True:
    line = f.readline()
    if len(line) == 0: # Zero length indicates EOF
        break
    print (line),
    # Notice comma to avoid automatic newline added by Python
f.close() # close the file
