import csv

with open('800ren.csv') as r800_csv_file:
    r800_csv_reader = csv.reader(r800_csv_file, delimiter=',')
    r800_list = list(r800_csv_reader)

    with open('4000ren.csv') as r4000_csv_file:
        r4000_csv_reader = csv.reader(r4000_csv_file, delimiter=',')
        r4000_list = list(r4000_csv_reader)

        for h in r4000_list[0]:
            r800_list[0].append(h)
        
        print(r800_list[0])
        
        r4000_names = {}
        for idx, row in enumerate(r4000_list):
            r4000_names[row[1]] = idx

        count = 0
        for row in r800_list:
            if row[2] in r4000_names:
                count += 1
                for e in r4000_list[r4000_names[row[2]]]:
                    row.append(e)
                # print(row)
        
        print(r800_list)
        print('total:', count)

        with open('800ren_r.csv', mode='w') as r800_saved_file:
            r800_writer = csv.writer(r800_saved_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in r800_list:
                r800_writer.writerow(row)


