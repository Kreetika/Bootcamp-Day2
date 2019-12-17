# import csv
# with open('newcsv.csv','w') as file:
#     writer = csv.DictWriter(file, ['name','email'])
#     writer.writeheader(
#     for i in range(100):
#         writer.writerow({'name':'Kritika', 'email':'abc.xyz.com'})
    

import csv
with open('student.csv','r') as file:
    with open('newcsv.csv','w') as file1:
        rows = csv.DictReader(file)
        writer= csv.DictWriter(file1,['name','email'])
        for row in rows:
            if int(row['sn'])%2 == 0:
                writer.writerow({'name':row['name'],'email':row['email']})
            
        
        


