''' Problem:
- Parse text datafile DNI, SEX, NAME with ; as dilimter.
- Datas presente in next format:   $DNI; SEX; Name@ 
SEX representes as M (masculine) or F (feminine)
- Create filter by SEX field
- Print result using filter
'''

import csv

# setting datas delimiter
DELIMITER = ';'
# setting column names
fieldnames = ['DNI', 'SEXO', 'Nombre']
sexo = input('A quien buscamos? F (Femenino) / M (Masculino): ').capitalize()
if sexo in ('F', 'M'):
    #read datafile
    with open("datafile.txt", encoding='utf-8') as r_file:
        file_reader = csv.DictReader(r_file, fieldnames = fieldnames, delimiter = DELIMITER)
        # Printing Header 
        print(f'    {"   -   ".join(fieldnames)}')
        for row in file_reader:
            if row['SEXO'] == sexo:
                print(f" {row['DNI'][1:]}  -  {row['SEXO']}  -  {row['Nombre'][:-1]}")
else:
    print('ERROR - Filtro debe ser letra "M" o "F". Reinicie el script')
