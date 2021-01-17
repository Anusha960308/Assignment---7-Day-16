#!/usr/bin/env python
# coding: utf-8

# In[9]:


import re 
  

with open('https://study-ccna.com/classes-of-ip-addresses/') as fh: 
   fstring = fh.readlines() 
  
 
pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})') 
  
 
lst=[] 
  
 
for line in fstring: 
   lst.append(pattern.search(line)[0]) 
  
 
print(lst) 


# In[ ]:




