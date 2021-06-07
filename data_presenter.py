open_file = open("CupcakeInvoices.csv")
print(open_file.read())

for line in open_file:
    print(line)

for line in open_file:
    line = line.strip()
    values = line.split(',')
    print(values[2:3])


for line in open_file:
    line = line.strip()
    values = line.split(',')
    print(float(values[3]) * float(values[4]))
    




    