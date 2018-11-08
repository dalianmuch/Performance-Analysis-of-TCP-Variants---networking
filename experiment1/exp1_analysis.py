
# coding: utf-8

# In[7]:


import pandas as pd


# In[8]:


from matplotlib import pyplot as plt


# In[10]:


throughput = pd.read_csv('./data/throughput.csv')


# In[14]:


plt.plot(throughput.CBR_Flow_Rate, throughput.Tahoe)
plt.plot(throughput.CBR_Flow_Rate, throughput.Reno)
plt.plot(throughput.CBR_Flow_Rate, throughput.NewReno)
plt.plot(throughput.CBR_Flow_Rate, throughput.Vegas)
plt.title("Throughput for Different CBR Flow Rate")
plt.xlabel("CBR Flow Rate")
plt.ylabel("Mbps")
plt.legend(["Tahoe", "Reno", "New Reno", "Vegas"])
plt.show()


# In[15]:


packet_drop_rate = pd.read_csv('./data/packet_drop_rate.csv')


# In[19]:


plt.plot(packet_drop_rate.CBR_Flow_Rate, packet_drop_rate.Tahoe)
plt.plot(packet_drop_rate.CBR_Flow_Rate, packet_drop_rate.Reno)
plt.plot(packet_drop_rate.CBR_Flow_Rate, packet_drop_rate.NewReno)
plt.plot(packet_drop_rate.CBR_Flow_Rate, packet_drop_rate.Vegas)
plt.title("Packet Drop Rate for Different CBR Flow Rate")
plt.xlabel("CBR Flow Rate")
plt.ylabel("in percentage")
plt.legend(["Tahoe", "Reno", "New Reno", "Vegas"])
plt.show()


# In[20]:


latency = pd.read_csv('./data/latency.csv')


# In[22]:


plt.plot(latency.CBR_Flow_Rate, latency.Tahoe)
plt.plot(latency.CBR_Flow_Rate, latency.Reno)
plt.plot(latency.CBR_Flow_Rate, latency.NewReno)
plt.plot(latency.CBR_Flow_Rate, latency.Vegas)
plt.title("Latency for Different CBR Flow Rate")
plt.xlabel("CBR Flow Rate")
plt.ylabel("in ms")
plt.legend(["Tahoe", "Reno", "New Reno", "Vegas"])
plt.show()

