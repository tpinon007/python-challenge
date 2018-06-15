
# coding: utf-8

# In[3]:



# coding: utf-8

# In[101]:


import os
import csv
import datetime

#Imports employee_data1.csv

employee_data1=os.path.join('python-challenge','employee_data1.csv')


with open(employee_data1, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    print(csvreader)
    
    for row in csvreader:
        print(row)
    


# In[102]:


#Imports employee_data2.csv

employee_data2=os.path.join('python-challenge','employee_data2.csv')

with open(employee_data2, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
    
    for row in csvreader:
        print(row)
   
    EmpID=[] #create list for employee ID
    FirstName=[] #create list for employee first names
    LastName=[] # create list for employee last names
    DOB=[] #create list for employee DOB
    SSN=[] #create list for employee SSN
    State_abbrev=[] #create list for employee State
    
    for line in csvreader:
        EmpID.append(line[0])
        Name=line[1].split(' ')
        FirstName.append(Name[0])
        LastName.append(Name[0])
    

#Replace state names with abbreviations

State_abbrev = {
    'Alabama':'AL',
    'Alaska': 'AK',
    'Arizona':'AZ',
    'Arkansas':'AR',
    'California':'CA',
    'Colorado':'CO',
    'Connecticut':'CT',
    'Delaware':'DE',
    'Florida':'FL',
    'Georgia':'GA',
    'Hawaii':'HI',
    'Idaho':'ID',
    'Illinois':'IL',
    'Indiana':'IN',
    'Iowa':'IA',
    'Kansas':'KS',
    'Kentucky':'KY',
    'Louisiana':'LA',
    'Maine':'ME',
    'Maryland':'MD',
    'Massachusetts': 'MA',
    'Michigan':'MI',
    'Minnesota':'MN',
    'Mississippi':'MS',
    'Missouri':'MO',
    'Montana':'MT',
    'Nebraska':'NE',
    'Nevada':'NV',
    'New Hampshire':'NH',
    'New Jersey':'NJ',
    'New Mexico':'NM',
    'New York':'NY',
    'North Carolina':'NC',
    'North Dakota':'ND',
    'Ohio':'OH',
    'Oklahoma':'OK',
    'Oregon':'OR',
    'Pennsylvania':'PA',
    'Rhode Island':'RI',
    'South Carolina':'SC',
    'South Dakota':'SD',
    'Tennessee':'TN',
    'Texas':'TX',
    'Utah':'UT',
    'Vermont':'VT',
    'Virginia':'VA',
    'Washington':'WA',
    'West Virginia':'WV',
    'Wisconsin':'WI',
    'Wyoming':'WY' }

def replace_all(State_abbrev, dic):
    for i, j in dic.iteritems():
        State_abbrev = State_abbrev.replace(i, j)
    return State_abbrev

###Modify date format
date = datetime.datetime.strptime(line[2], '%Y-%m-%d').strftime('%m/%d/%Y')
DOB.append(date)

# In[103]:

###Modify SSN format
SSN = line[3]
SSN.append('***-**-' + str(SSN))


mod_data1=zip(EmpID, FirstName, LastName, DOB, SSN, State_abbrev)
mod_data2=zip(EmpID, FirstName, LastName, DOB, SSN, State_abbrev)


# In[104]:


#Export modified employee data CSV for data1
modified_employee_data1=os.path.join('python-challenge','modified_employee_data1.csv')
with open(modified_employee_data1,'w',newline='') as csvfile:
    csvwriter=csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['EmpID','First Name','Last Name', 'DOB','SSN','State'])
    csvwriter.writerows(mod_data1)


# In[105]:


#Export modified employee data CSV for data2
modified_employee_data2=os.path.join('python-challenge','modified_employee_data2.csv')
with open(modified_employee_data2,'w',newline='') as csvfile:
    csvwriter=csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['EmpID','First Name','Last Name', 'DOB','SSN','State'])
    csvwriter.writerows(mod_data2)

