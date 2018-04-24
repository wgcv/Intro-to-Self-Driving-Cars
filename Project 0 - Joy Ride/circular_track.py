
# coding: utf-8

# In[1]:


get_ipython().run_cell_magic('HTML', '', '<button id="launcher">Launch Car Simulator</button>\n<script src="setupLauncher.js"></script>')


# In[7]:


from Car import Car
import time

def circle(car):
    car.steer(5)
    car.gas(1)
    
car = Car()

circle(car)

