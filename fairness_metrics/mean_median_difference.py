#!/usr/bin/env python
# coding: utf-8

# In[54]:


get_ipython().system('pip install gerrychain')


# In[55]:


get_ipython().system('git clone https://github.com/mggg/GerryChain.git')


# In[56]:


# make sure this file shows up in this directory
get_ipython().system('ls GerryChain/docs/user/PA_VTDs.json')


# In[57]:


path_to_pa = r'C:\Users\adika\Downloads\PA_VTDs.json'


# In[58]:


from gerrychain import Graph, Partition, Election
from gerrychain.updaters import Tally, cut_edges

graph = Graph.from_json(path_to_pa)

election = Election("SEN12", {"Dem": "USS12D", "Rep": "USS12R"})

initial_partition = Partition(
    graph,
    assignment="CD_2011",
    updaters={
        "cut_edges": cut_edges,
        "population": Tally("TOTPOP", alias="population"),
        "SEN12": election
    }
)


# In[59]:


for district, pop in initial_partition["population"].items():
    print("District {}: {}".format(district, pop))


# In[60]:


from gerrychain import MarkovChain
from gerrychain.constraints import single_flip_contiguous
from gerrychain.proposals import propose_random_flip
from gerrychain.accept import always_accept

chain = MarkovChain(
    proposal=propose_random_flip,
    constraints=[single_flip_contiguous],
    accept=always_accept,
    initial_state=initial_partition,
    total_steps=1000
)


# In[61]:


for partition in chain:
    print(sorted(partition["SEN12"].percents("Dem")))


# In[62]:


import pandas as pd

d_percents = [sorted(partition["SEN12"].percents("Dem")) for partition in chain]

data = pd.DataFrame(d_percents)


# In[63]:


import matplotlib.pyplot as plt
ax = data.boxplot(positions=range(len(data.columns)))
plt.plot(data.iloc[0], "ro")
plt.ylim(0,1)
plt.show()


# In[64]:


import json

with open(path_to_pa) as f:
    data = json.load(f)


# In[65]:


df = pd.DataFrame(data['nodes'])


# In[66]:


df.info()


# In[67]:


df.head()


# In[68]:


df_by_cd2011 = df.groupby('CD_2011').sum()
df_by_cd2011['INDEX']=df_by_cd2011.index
df_by_cd2011['T16PRESTOT']=df_by_cd2011['T16PRESR']+df_by_cd2011['T16PRESD']

#df_by_cd2011['T16PRESOTH']

#median vote share of either party across all districts from the average vote share of the same party across all districts.
df_by_cd2011['T16PRESR_PCT']=df_by_cd2011['T16PRESR']/df_by_cd2011['T16PRESTOT']
df_by_cd2011['T16PRESD_PCT']=df_by_cd2011['T16PRESD']/df_by_cd2011['T16PRESTOT']

avg_repub_vote_share=df_by_cd2011['T16PRESR_PCT'].mean()
median_repub_vote_share=df_by_cd2011['T16PRESR_PCT'].median()


# In[69]:


print(avg_repub_vote_share)
print(median_repub_vote_share)


# In[70]:


avg_demo_vote_share=df_by_cd2011['T16PRESD_PCT'].mean()
median_demo_vote_share=df_by_cd2011['T16PRESD_PCT'].median()


# In[71]:


print(avg_demo_vote_share)
print(median_demo_vote_share)


# In[72]:


print("The mean-median difference is simply calculated by subtracting the median vote share of either party across all districts from the average vote share of the same party across all districts")


# In[73]:


mean_median_republic_diff=avg_repub_vote_share-median_repub_vote_share
mean_median_demo_diff=avg_demo_vote_share-median_demo_vote_share


# In[74]:


print(mean_median_republic_diff)
print(mean_median_demo_diff)


# In[75]:


print(" A negative mean-median difference indicates that the republic party has an advantage; a positive difference indicates that the democratic party is disadvantaged. ")


# In[76]:


df_by_cd2011 = df.groupby('REMEDIAL').sum() 


# In[77]:


cols=['REMEDIAL', 'GOV', 'TS', 'CD_2011', '538DEM', '538GOP', '538CMPCT']
res=[]


# In[78]:


df_by_REMEDIAL = df.groupby('REMEDIAL').sum()
df_by_REMEDIAL['INDEX']=df_by_REMEDIAL.index
df_by_REMEDIAL['T16PRESTOT']=df_by_REMEDIAL['T16PRESR']+df_by_REMEDIAL['T16PRESD']

#df_by_cd2011['T16PRESOTH']

#median vote share of either party across all districts from the average vote share of the same party across all districts.
df_by_REMEDIAL['T16PRESR_PCT']=df_by_REMEDIAL['T16PRESR']/df_by_REMEDIAL['T16PRESTOT']
df_by_REMEDIAL['T16PRESD_PCT']=df_by_REMEDIAL['T16PRESD']/df_by_REMEDIAL['T16PRESTOT']

avg_repub_vote_share=df_by_REMEDIAL['T16PRESR_PCT'].mean()
median_repub_vote_share=df_by_REMEDIAL['T16PRESR_PCT'].median()

print(avg_repub_vote_share)
print(median_repub_vote_share)

print(avg_repub_vote_share-median_repub_vote_share)


# In[87]:


df_by_REMEDIAL = df.groupby('TS').sum()
df_by_REMEDIAL['INDEX']=df_by_REMEDIAL.index
df_by_REMEDIAL['T16PRESTOT']=df_by_REMEDIAL['T16PRESR']+df_by_REMEDIAL['T16PRESD']

#df_by_cd2011['T16PRESOTH']

#median vote share of either party across all districts from the average vote share of the same party across all districts.
df_by_REMEDIAL['T16PRESR_PCT']=df_by_REMEDIAL['T16PRESR']/df_by_REMEDIAL['T16PRESTOT']
df_by_REMEDIAL['T16PRESD_PCT']=df_by_REMEDIAL['T16PRESD']/df_by_REMEDIAL['T16PRESTOT']

avg_repub_vote_share=df_by_REMEDIAL['T16PRESR_PCT'].mean()
median_repub_vote_share=df_by_REMEDIAL['T16PRESR_PCT'].median()

print(avg_repub_vote_share)
print(median_repub_vote_share)

print(avg_repub_vote_share-median_repub_vote_share)


# In[84]:


df_by_REMEDIAL = df.groupby('GOV').sum()
df_by_REMEDIAL['INDEX']=df_by_REMEDIAL.index
df_by_REMEDIAL['T16PRESTOT']=df_by_REMEDIAL['T16PRESR']+df_by_REMEDIAL['T16PRESD']

#df_by_cd2011['T16PRESOTH']

#median vote share of either party across all districts from the average vote share of the same party across all districts.
df_by_REMEDIAL['T16PRESR_PCT']=df_by_REMEDIAL['T16PRESR']/df_by_REMEDIAL['T16PRESTOT']
df_by_REMEDIAL['T16PRESD_PCT']=df_by_REMEDIAL['T16PRESD']/df_by_REMEDIAL['T16PRESTOT']

avg_repub_vote_share=df_by_REMEDIAL['T16PRESR_PCT'].mean()
median_repub_vote_share=df_by_REMEDIAL['T16PRESR_PCT'].median()

print(avg_repub_vote_share)
print(median_repub_vote_share)

print(avg_repub_vote_share-median_repub_vote_share)


# In[83]:


df_by_REMEDIAL = df.groupby('538DEM').sum()
df_by_REMEDIAL['INDEX']=df_by_REMEDIAL.index
df_by_REMEDIAL['T16PRESTOT']=df_by_REMEDIAL['T16PRESR']+df_by_REMEDIAL['T16PRESD']

#df_by_cd2011['T16PRESOTH']

#median vote share of either party across all districts from the average vote share of the same party across all districts.
df_by_REMEDIAL['T16PRESR_PCT']=df_by_REMEDIAL['T16PRESR']/df_by_REMEDIAL['T16PRESTOT']
df_by_REMEDIAL['T16PRESD_PCT']=df_by_REMEDIAL['T16PRESD']/df_by_REMEDIAL['T16PRESTOT']

avg_repub_vote_share=df_by_REMEDIAL['T16PRESR_PCT'].mean()
median_repub_vote_share=df_by_REMEDIAL['T16PRESR_PCT'].median()

print(avg_repub_vote_share)
print(median_repub_vote_share)

print(avg_repub_vote_share-median_repub_vote_share)


# In[85]:


df_by_REMEDIAL = df.groupby('538GOP').sum()
df_by_REMEDIAL['INDEX']=df_by_REMEDIAL.index
df_by_REMEDIAL['T16PRESTOT']=df_by_REMEDIAL['T16PRESR']+df_by_REMEDIAL['T16PRESD']

#df_by_cd2011['T16PRESOTH']

#median vote share of either party across all districts from the average vote share of the same party across all districts.
df_by_REMEDIAL['T16PRESR_PCT']=df_by_REMEDIAL['T16PRESR']/df_by_REMEDIAL['T16PRESTOT']
df_by_REMEDIAL['T16PRESD_PCT']=df_by_REMEDIAL['T16PRESD']/df_by_REMEDIAL['T16PRESTOT']

avg_repub_vote_share=df_by_REMEDIAL['T16PRESR_PCT'].mean()
median_repub_vote_share=df_by_REMEDIAL['T16PRESR_PCT'].median()

print(avg_repub_vote_share)
print(median_repub_vote_share)

print(avg_repub_vote_share-median_repub_vote_share)


# In[86]:


df_by_REMEDIAL = df.groupby('538CMPCT').sum()
df_by_REMEDIAL['INDEX']=df_by_REMEDIAL.index
df_by_REMEDIAL['T16PRESTOT']=df_by_REMEDIAL['T16PRESR']+df_by_REMEDIAL['T16PRESD']

#df_by_cd2011['T16PRESOTH']

#median vote share of either party across all districts from the average vote share of the same party across all districts.
df_by_REMEDIAL['T16PRESR_PCT']=df_by_REMEDIAL['T16PRESR']/df_by_REMEDIAL['T16PRESTOT']
df_by_REMEDIAL['T16PRESD_PCT']=df_by_REMEDIAL['T16PRESD']/df_by_REMEDIAL['T16PRESTOT']

avg_repub_vote_share=df_by_REMEDIAL['T16PRESR_PCT'].mean()
median_repub_vote_share=df_by_REMEDIAL['T16PRESR_PCT'].median()

print(avg_repub_vote_share)
print(median_repub_vote_share)

print(avg_repub_vote_share-median_repub_vote_share)


# In[ ]:




