with open('dataset', "r", encoding='utf-8') as bd:
    data = (int(line[6]) for line in (line.strip().split(';') for line in bd) if line[7] == 'a')
    all_raised = sum(data)
    print(weight_raised := all_raised / (30e6 - 10e6) * 1000)
with open('dataset', "r", encoding='utf-8') as bd:
    new_file = open('new_database.txt', 'w')
    data = ((line[0], line[2], line[6]) for line in (line.strip().split(';')for line in bd) if line[7] == 'a' and int(line[6]) < weight_raised)
    for i in data:
        new_file.write(str(i)+'\n')
    new_file.close()
