
# coding: utf-8

# In[9]:


import pandas as pd


# In[10]:


from matplotlib import pyplot as plt


# In[11]:


latency = pd.read_csv('./data/latency.csv')


# In[12]:


latency


# In[13]:


plt.plot(latency.Reno_DropTail_Time, latency.Reno_DropTail_Value)
plt.plot(latency.Reno_RED_Time, latency.Reno_RED_Value)
plt.plot(latency.SACK_DropTail_Time, latency.SACK_DropTail_Value)
plt.plot(latency.SACK_RED_Time, latency.SACK_RED_Value)
plt.title("Latency for Different Time Period")
plt.xlabel("Time in seconds")
plt.ylabel("Latency in ms")
plt.legend(["Reno DropTail", "Reno RED", "SACK DropTail", "SACK RED"])
plt.show()


# In[14]:


throughput = pd.read_csv('./data/throughput.csv')


# In[15]:


throughput


# In[16]:


plt.plot(throughput.Time, throughput.Reno_DropTail)
plt.plot(throughput.Time, throughput.Reno_RED)
plt.plot(throughput.Time, throughput.SACK_DropTail)
plt.plot(throughput.Time, throughput.SACK_RED)
plt.title("Throughput for Different Time Period")
plt.xlabel("Time in seconds")
plt.ylabel("Mega Bytes")
plt.legend(["Reno DropTail", "Reno RED", "SACK DropTail", "SACK RED"])
plt.show()

