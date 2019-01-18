
# coding: utf-8

# In[26]:


import os, fnmatch


# In[27]:


#def findReplace(directory, find, replace, filePattern):
def findReplace(directory, filePattern):
    for path, dirs, files in os.walk(os.path.abspath(directory)):
        for filename in fnmatch.filter(files, filePattern):
            filepath = os.path.join(path, filename)
            with open(filepath) as f:
                s = f.read()
            #s = s.replace(find, replace)
            mapping = {'DEPTH_(m~':'DEPTH_m'}
            for find, replace in mapping.iteritems():
                s = s.replace(find, replace)            
            with open(filepath, "w") as f:
                f.write(s)


# In[28]:


#findReplace("some_dir", "find this", "replace with this", "*.txt")
#findReplace(r'C:\Users\H159846\git\python_curve_name_changer\dir', ['DEPTH_(m)','DEPTH_(m~'], 'Depth_m', '*.las')
findReplace(r'C:\Users\H159846\git\python_curve_name_changer\dir', '*.las')

