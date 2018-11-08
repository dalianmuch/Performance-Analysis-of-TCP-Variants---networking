
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


from matplotlib import pyplot as plt


# In[6]:


throughput = pd.read_csv('./data/throughput.csv')


# In[7]:


throughput


# In[8]:


plt.plot(throughput.CBR_Flow_Rate, throughput.Reno_1_1_4)
plt.plot(throughput.CBR_Flow_Rate, throughput.Reno_1_5_6)
plt.title("Throughput for Different CBR Flow Rate")
plt.xlabel("CBR Flow Rate")
plt.ylabel("Mega bits")
plt.legend(["Reno N1->N4", "Reno N5->N6"])
plt.show()


# In[9]:


plt.plot(throughput.CBR_Flow_Rate, throughput.NewReno_2)
plt.plot(throughput.CBR_Flow_Rate, throughput.Reno_2)
plt.title("Throughput for Different CBR Flow Rate")
plt.xlabel("CBR Flow Rate")
plt.ylabel("Mega bits")
plt.legend(["NewReno N1->N4", "Reno N5->N6"])
plt.show()


# In[10]:


plt.plot(throughput.CBR_Flow_Rate, throughput.Vegas_3_1_4)
plt.plot(throughput.CBR_Flow_Rate, throughput.Vegas_3_5_6)
plt.title("Throughput for Different CBR Flow Rate")
plt.xlabel("CBR Flow Rate")
plt.ylabel("Mega bits")
plt.legend(["Vegas N1->N4", "Vegas N5->N6"])
plt.show()


# In[11]:


plt.plot(throughput.CBR_Flow_Rate, throughput.NewReno_4)
plt.plot(throughput.CBR_Flow_Rate, throughput.Vegas_4)
plt.title("Throughput for Different CBR Flow Rate")
plt.xlabel("CBR Flow Rate")
plt.ylabel("Mega bits")
plt.legend(["NewReno N1->N4", "Vegas N5->N6"])
plt.show()


# In[14]:


packet_drop_rate = pd.read_csv('./data/packet_drop_rate.csv')


# In[15]:


# Reno Reno
plt.plot(packet_drop_rate.CBR_Flow_Rate, packet_drop_rate.Reno_1_1_4)
plt.plot(packet_drop_rate.CBR_Flow_Rate, packet_drop_rate.Reno_1_5_6)
plt.title("Packet Drop Rate for Different CBR Flow Rate")
plt.xlabel("CBR Flow Rate")
plt.ylabel("in percentage")
plt.legend(["Reno N1->N4", "Reno N5->N6"])
plt.show()


# In[27]:


# NewReno Reno
plt.plot(packet_drop_rate.CBR_Flow_Rate, packet_drop_rate.NewReno_2)
plt.plot(packet_drop_rate.CBR_Flow_Rate, packet_drop_rate.Reno_2)
plt.title("Packet Drop Rate for Different CBR Flow Rate")
plt.xlabel("CBR Flow Rate")
plt.ylabel("in percentage")
plt.legend(["NewReno N1->N4", "Reno N5->N6"])
plt.show()


# In[17]:


# Vegas Vegas
plt.plot(packet_drop_rate.CBR_Flow_Rate, packet_drop_rate.Vegas_3_1_4)
plt.plot(packet_drop_rate.CBR_Flow_Rate, packet_drop_rate.Vegas_3_5_6)
plt.title("Packet Drop Rate for Different CBR Flow Rate")
plt.xlabel("CBR Flow Rate")
plt.ylabel("in percentage")
plt.legend(["Vegas N1->N4", "Vegas N5->N6"])
plt.show()


# In[18]:


# NewReno Vegas
plt.plot(packet_drop_rate.CBR_Flow_Rate, packet_drop_rate.NewReno_4)
plt.plot(packet_drop_rate.CBR_Flow_Rate, packet_drop_rate.Vegas_4)
plt.title("Packet Drop Rate for Different CBR Flow Rate")
plt.xlabel("CBR Flow Rate")
plt.ylabel("in percentage")
plt.legend(["NewReno N1->N4", "Vegas N5->N6"])
plt.show()


# In[19]:


latency = pd.read_csv('./data/latency.csv')


# In[20]:


latency


# In[21]:


# Reno Reno
plt.plot(latency.CBR_Flow_Rate, latency.Reno_1_1_4)
plt.plot(latency.CBR_Flow_Rate, latency.Reno_1_5_6)
plt.title("Latency for Different CBR Flow Rate")
plt.xlabel("CBR Flow Rate")
plt.ylabel("in ms")
plt.legend(["Reno N1->N4", "Reno N5->N6"])
plt.show()


# In[26]:


# NewReno Reno
plt.plot(latency.CBR_Flow_Rate, latency.NewReno_2)
plt.plot(latency.CBR_Flow_Rate, latency.Reno_2)
plt.title("Latency for Different CBR Flow Rate")
plt.xlabel("CBR Flow Rate")
plt.ylabel("in ms")
plt.legend(["NewReno N1->N4", "Reno N5->N6"])
plt.show()


# In[24]:


# Vegas Vegas
plt.plot(latency.CBR_Flow_Rate, latency.Vegas_3_1_4)
plt.plot(latency.CBR_Flow_Rate, latency.Vegas_3_5_6)
plt.title("Latency for Different CBR Flow Rate")
plt.xlabel("CBR Flow Rate")
plt.ylabel("in ms")
plt.legend(["Vegas N1->N4", "Vegas N5->N6"])
plt.show()


# In[25]:


# NewReno Vegas
plt.plot(latency.CBR_Flow_Rate, latency.NewReno_4)
plt.plot(latency.CBR_Flow_Rate, latency.Vegas_4)
plt.title("Latency for Different CBR Flow Rate")
plt.xlabel("CBR Flow Rate")
plt.ylabel("in ms")
plt.legend(["NewReno N1->N4", "Vegas N5->N6"])
plt.show()

