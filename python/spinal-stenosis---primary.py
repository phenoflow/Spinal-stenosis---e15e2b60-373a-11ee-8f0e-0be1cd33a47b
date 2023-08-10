# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"106536.0","system":"med"},{"code":"12094.0","system":"med"},{"code":"15331.0","system":"med"},{"code":"3370.0","system":"med"},{"code":"35117.0","system":"med"},{"code":"41147.0","system":"med"},{"code":"43577.0","system":"med"},{"code":"45296.0","system":"med"},{"code":"52139.0","system":"med"},{"code":"62612.0","system":"med"},{"code":"69388.0","system":"med"},{"code":"72614.0","system":"med"},{"code":"73730.0","system":"med"},{"code":"91625.0","system":"med"},{"code":"93836.0","system":"med"},{"code":"93849.0","system":"med"},{"code":"94588.0","system":"med"},{"code":"97870.0","system":"med"},{"code":"98630.0","system":"med"},{"code":"9912.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('spinal-stenosis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["spinal-stenosis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["spinal-stenosis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["spinal-stenosis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
