#!/usr/bin/env python
# coding: utf-8

# # Imports

# In[2]:


# To install pymdp on  my mac
#!pip install pymdptoolbox


# In[1]:


import numpy as np
import pandas as pd
import mdptoolbox
import time as time
import itertools
import csv
from decimal import *
import pdb


# # States

# In[2]:


###################  States   ###################
## Group 1= G0000
G0000=['0000']


###########################################################
## Group 2= G0010
import itertools

# Define the characters for the third place
third_place_characters = ['N', 'G', 'Y', 'S']

# Generate all combinations for the third place
combinations = itertools.product(third_place_characters, repeat=1)

# Initialize the list G0010
G0010 = []

# Store all combinations in G0010
for combo in combinations:
    G0010.append('0' * 2 + combo[0] + '0' )

#G0010


###########################################################
## Group 3= G0011
import itertools

# Define the characters for the third and fourth places
third_fourth_place_characters = ['N', 'G', 'Y', 'S']

# Generate all combinations for the third and fourth places
combinations = itertools.product(third_fourth_place_characters, repeat=2)

# Initialize the list G0011
G0011 = []

# Store all combinations in G0011
for combo in combinations:
    G0011.append('0' * 2 + combo[0] + combo[1])

# Print the list G0011
#print(G0011)


##########################################################
## Group 4= G1000
import itertools

# Define the characters for the first place
first_place_characters = ['N', 'G', 'Y', 'S']

# Generate all combinations for the first place
combinations = itertools.product(first_place_characters, repeat=1)

# Initialize the list G1000
G1000 = []

# Store all combinations in G1000
for combo in combinations:
    G1000.append(combo[0] + '0' * 3)

# Print the list G1000
#print(G1000)



###########################################################
## Group 5=G1010
import itertools

# Define the characters for the first and third places
first_third_place_characters = ['N', 'G', 'Y', 'S']

# Generate all combinations for the first and third places
combinations = itertools.product(first_third_place_characters, repeat=2)

# Initialize the list G1010
G1010 = []

# Store all combinations in G1010
for combo in combinations:
    G1010.append(combo[0] + '0' + combo[1] + '0')

# Print the list G1010
#print(G1010)


###########################################################
##Group 6= G1011
import itertools

# Define the characters for the first, third, and fourth places
first_third_fourth_place_characters = ['N', 'G', 'Y', 'S']

# Generate all combinations for the first, third, and fourth places
combinations = itertools.product(first_third_fourth_place_characters, repeat=3)

# Initialize the list G1011
G1011 = []

# Store all combinations in G1011
for combo in combinations:
    G1011.append(combo[0] + '0' + combo[1] + combo[2])

# Print the list G1011
#print(G1011)



###########################################################
## Group 7= G1100
import itertools

# Define the characters for the first and second places
first_second_place_characters = ['N', 'G', 'Y', 'S']

# Generate all combinations for the first and second places
combinations = itertools.product(first_second_place_characters, repeat=2)

# Initialize the list G1100
G1100 = []

# Store all combinations in G1100
for combo in combinations:
    G1100.append(combo[0] + combo[1] + '00')

# Print the list G1100
#print(G1100)

###########################################################
## Group 8 = G1110
import itertools

# Define the characters for the first, second, and third places
first_second_third_place_characters = ['N', 'G', 'Y', 'S']

# Generate all combinations for the first, second, and third places
combinations = itertools.product(first_second_third_place_characters, repeat=3)

# Initialize the list G1110
G1110 = []

# Store all combinations in G1110
for combo in combinations:
    G1110.append(combo[0] + combo[1] + combo[2] + '0')

# Print the list G1110
#print(G1110)



###########################################################
## Group 9= G1111
import itertools

# Define the characters for the places
place_characters = ['N', 'G', 'Y', 'S']

# Generate all combinations for all places
combinations = itertools.product(place_characters, repeat=4)

# Initialize the list G1111
G1111 = []

# Store all combinations in G1111
for combo in combinations:
    G1111.append(''.join(combo))

# Print the list G1111
#print(G1111)


###########################################################
## Group 10 =GF
GF=['Final']

##############################################################################################
## All states together
all_states=G0000 + G1000 + G0010 + G1010 + G0011+ G1100 +G1110 +G1011 +G1111 +GF
#all_states


# # Actions

# In[3]:


###################  Actions   ###################

# Actualy Only on line A
action_A=["a-N0", "a-G0", "a-Y0", "a-S0"] 

###########################################################
# Actualy Only on line B
action_B=["a-0N", "a-0G", "a-0Y", "a-0S"]

###########################################################
# on both line
action_AB=["a-NN", "a-NG", "a-NY", "a-NS",
    "a-GN", "a-GG", "a-GY", "a-GS",
    "a-YN", "a-YG", "a-YY", "a-YS",
    "a-SN", "a-SG", "a-SY", "a-SS"]

###########################################################
# On the Merge line
action_M=["a-M"]

###########################################################
#on the final state
action_F=['a-F']

#################################################################################################
# All actions together
action_list= action_AB+action_A + action_B  + action_M +action_F #for the convinience I changed the order 
#action_list


# # Transition Probabilities

# ## 1-From State = G0000   taking  action=a-AB

# In[70]:


#P1
#1-From State = G0000   taking  action=a-AB
#1.a.It goes to G1010 with prob of P1= P(IA1p)*P(IB1p)
# Define transitions and probabilities from G0000 to G1010

trans_G0000ToG1010 = {}
actions=action_AB

for from_state in G0000:
    for action in actions:
        to_state = action[2]+from_state[0]+ action[3] + from_state[3]
        probability = f'P1-{from_state}-{to_state}'
        trans_G0000ToG1010[(from_state,action,to_state)] = {'probability': probability}
trans_G0000ToG1010


# In[71]:


#P2
#1-From State = G0000   taking  action=a-AB
#1.b.IT GOES TO G0010 with Prob of P2=P(IA1f)*P(IB1p)

## G0000 to G0010
# Define transitions and probabilities from G0000 to G0010
trans_G0000ToG0010 = {}
#action_AB=["a-NN", "a-NG", "a-NY", "a-NS","a-GN", "a-GG", "a-GY", "a-GS","a-YN", "a-YG", "a-YY", "a-YS","a-SN", "a-SG", "a-SY", "a-SS"]
actions=action_AB

for from_state in G0000:
    for action in actions:
        #print(action)
        to_state = from_state[0:2]+ action[3] + from_state[3]
        #print(to_state)
        probability = f'P2-{from_state}-{to_state}'
        trans_G0000ToG0010[(from_state,action,to_state)] = {'probability': probability}
    #print(trans_G0000ToG0010)
trans_G0000ToG0010


# In[72]:


#P3
#1-From State = G0000   taking  action=a-AB
#c.It goes to G1000 with prob of   P3=P(IA1p)*P(IB1f)
## G0000 to G1000
# Define transitions and probabilities from G0000 to G1000
trans_G0000ToG1000 = {}
actions=action_AB

for from_state in G0000:
    for action in actions:
        to_state = action[2] + from_state[1:]
        probability = f'P3-{from_state}-{to_state}'
        trans_G0000ToG1000[(from_state,action,to_state)] = {'probability': probability}
trans_G0000ToG1000


# In[73]:


#P4
#1-From State = G0000   taking  action=a-AB
#d.It goes back to G0000 with prob of P4=P(IA1f)*P(IB1f)
trans_G0000ToG0000 = {}
actions=action_AB

for from_state in G0000:
    for action in actions:
        to_state = from_state
        probability = f'P4-{from_state}-{to_state}'
        trans_G0000ToG0000[(from_state,action,to_state)] = {'probability': probability}
trans_G0000ToG0000


# ## 2-From State    G0010     taking    action=a-AB

# In[74]:


#P5
#2-From State    G0010     taking    action=a-AB
#a.It goes to G1011  with prob of P5= P(IA1p)*P(IB2p|IB1p)
## G0010 to G1011

# Define transitions and probabilities from G0010 to G1011
trans_G0010ToG1011 = {}
actions=action_AB

for from_state in G0010:
    for action in actions:
        to_state =  action[2]+ from_state[1]+ from_state[2] + action[3] 
        probability = f'P5-{from_state}-{to_state}'
        trans_G0010ToG1011[(from_state,action,to_state)] = {'probability': probability}
trans_G0010ToG1011


# In[75]:


#P6
#2-From State    G0010     taking    action=a-AB
#b.It goes to G0011  with prob of P6= P(IA1f)*P(IB2p|IB1p)
## G0010 to G0011

# Define transitions and probabilities from G0010 to G0011
trans_G0010ToG0011 = {}
actions=action_AB

for from_state in G0010:
    for action in actions:
        to_state = from_state[0:3]+ action[3]
        probability = f'P6-{from_state}-{to_state}'
        trans_G0010ToG0011[(from_state,action,to_state)] = {'probability': probability}
        
#trans_G0010ToG0011


# In[76]:


#P7
#2-From State    G0010     taking    action=a-AB
#c.It goes to G1000  with prob of P7= P(IA1p)*P(IB2f|IB1p)
# Define transitions and probabilities from G0010 to G1000
trans_G0010ToG1000 = {}
actions=action_AB

for from_state in G0010:
    for action in actions:
        to_state =action[2]+from_state[1]+'0'+from_state[3]
        probability = f'P7-{from_state}-{to_state}'
        trans_G0010ToG1000[(from_state,action,to_state)] = {'probability': probability}
        
#trans_G0010ToG1000


# In[77]:


#P8
#2-From State    G0010     taking    action=a-AB
#d.It goes to G0000  with prob of P8= P(IA1f)*P(IB2f|IB1p)
# Define transitions and probabilities from G0010 to G0000
trans_G0010ToG0000 = {}
actions=action_AB

for from_state in G0010:
    for action in actions:
        to_state ='0000'
        probability = f'P8-{from_state}-{to_state}'
        trans_G0010ToG0000[(from_state,action,to_state)] = {'probability': probability}
        
#trans_G0010ToG0000


# ## 3-From state   G1010   taking action=a-AB

# In[79]:


#P9
#3-From state   G1010  taking action=a-AB
#a.It goes to G1111 with prob of P9= P(IA2p|IA1p)*P(IB2p|IB1p)
# Define transitions and probabilities from G1010 to G1111
trans_G1010ToG1111 = {}
actions=action_AB

for from_state in G1010:
    for action in actions:
        to_state = from_state[0] + action[2]+ from_state[2] + action[3] 
        probability = f'P9-{from_state}-{to_state}'
        trans_G1010ToG1111[(from_state,action,to_state)] = {'probability': probability}
#trans_G1010ToG1111


# In[78]:


#P10
#3-From state   G1010   taking action=a-AB
#b.It goes to G0011 with prob of P10= P(IA2f|IA1p)*P(IB2p|IB1p)
# Define transitions and probabilities from 1010 to G0011
trans_G1010ToG0011 = {}
actions=action_AB

for from_state in G1010:
    for action in actions:
        to_state ='00'+from_state[2]+action[3]
        probability = f'P10-{from_state}-{to_state}'
        trans_G1010ToG0011[(from_state,action,to_state)] = {'probability': probability}
        
#trans_G1010ToG0011


# In[80]:


#P11
#3-From state   G1010  taking action=a-AB
#c.It goes to G1100 with prob of P11= P(IA2p|IA1p)*P(IB2f|IB1p))
# Define transitions and probabilities from G1010 to G1100
trans_G1010ToG1100 = {}
actions=action_AB

for from_state in G1010:
    for action in actions:
        to_state = from_state[0] + action[2]+ '00'  
        probability = f'P11-{from_state}-{to_state}'
        trans_G1010ToG1100[(from_state,action,to_state)] = {'probability': probability}
#trans_G1010ToG1100


# In[81]:


#P12
#3-From state   G1010  taking action=a-AB
#d.It goes to G0000 with prob of P12= P(IA2f|IA1p)*P(IB2f|IB1p))
# Define transitions and probabilities from G1010 to G0000
trans_G1010ToG0000 = {}
actions=action_AB

for from_state in G1010:
    for action in actions:
        to_state = '0000'  
        probability = f'P12-{from_state}-{to_state}'
        trans_G1010ToG0000[(from_state,action,to_state)] = {'probability': probability}
#trans_G1010ToG0000


# ## 4-From state   G1000   taking action=a-AB

# In[82]:


#P13
#4-From state   G1000   taking action=a-AB
#a.It goes to G1110 with Prob of P13=P(IA2p|IA1p)*P(IB1p)
# Define transitions and probabilities from G1000 to G1110
trans_G1000ToG1110 = {}
actions=action_AB

for from_state in G1000:
    for action in actions:
        to_state =  from_state[0]+action[2] + action[3] + from_state[3]
        probability = f'P13-{from_state}-{to_state}'
        trans_G1000ToG1110[(from_state,action,to_state)] = {'probability': probability}
trans_G1000ToG1110


# In[83]:


#P14
#4-From state   G1000   taking action=a-AB
#b.It goes to G1100 with Prob of P14=P(IA2p|IA1p)*P(IB1f)
## G1000 to G1100

# Define transitions and probabilities from G1000 to G1100
trans_G1000ToG1100 = {}
actions = action_AB

for from_state in G1000:
    for action in actions:
        to_state = from_state[0] + action[2] + from_state[2:]
        probability = f'P14-{from_state}-{to_state}'
        trans_G1000ToG1100[(from_state,action,to_state)] = {'probability': probability}
#trans_G1000ToG1100


# In[84]:


#P15
#4-From state   G1000   taking action=a-AB
#c.It goes to G0010 with Prob of P15=P(IA2f|IA1p)*P(IB1p)
## G1000 to G0010

# Define transitions and probabilities from G1000 to G0010
trans_G1000ToG0010 = {}
actions = action_AB

for from_state in G1000:
    for action in actions:
        to_state = '00' + action[3]+from_state[3]
        probability = f'P15-{from_state}-{to_state}'
        trans_G1000ToG0010[(from_state,action,to_state)] = {'probability': probability}
#trans_G1000ToG0010


# In[85]:


#P16
#4-From state   G1000   taking action=a-AB
#d.It goes to G0000 with Prob of P16=P(IA2f|IA1p)*P(IB1f)
## G1000 to G0000

# Define transitions and probabilities from G1000 to G0000
trans_G1000ToG0000 = {}
actions = action_AB

for from_state in G1000:
    for action in actions:
        to_state = '0000' 
        probability = f'P16-{from_state}-{to_state}'
        trans_G1000ToG0000 [(from_state,action,to_state)] = {'probability': probability}
#trans_G1000ToG0000 


# ## 5-From state   G0011   taking action=a-A0

# In[86]:


#P17
#5-From state   G0011   taking action=a-A0
#a.It goes to G1011 with Prob of P17=P(IA1p)
## G0011 To G1011 

# Define transitions and probabilities from G0011 to G1011
trans_G0011ToG1011 = {}
#action_A=["a-N0", "a-G0", "a-Y0", "a-S0"]
actions=action_A

for from_state in G0011:
    for action in actions:
        to_state = action[2:] +from_state[2:]
        probability = f'P17-{from_state}-{to_state}'
        trans_G0011ToG1011[(from_state,action,to_state)] = {'probability': probability}
#trans_G0011ToG1011


# In[87]:


#P18
#5-From state   G0011   taking action=a-A0
#b.It goes to G0011 with Prob of P18=P(IA1f)
# Define transitions and probabilities from G0011 to G0011
trans_G0011ToG0011 = {}
actions=action_A

for from_state in G0011:
    for action in actions:
        to_state = from_state
        probability = f'P18-{from_state}-{to_state}'
        trans_G0011ToG0011[(from_state,action,to_state)] = {'probability': probability}
#trans_G0011ToG0011


# ## 6-From state G1100 taking action a-0B

# In[88]:


#P19
#6-From state, G1100 taking action a-0B
#a.It goes to G1110 with Prob of P19=P(IB1p)
## G1100 to G1110

# Define transitions and probabilities from G1100 to G1110
trans_G1100ToG1110 = {}
#action_B=["a-0N", "a-0G", "a-0Y", "a-0S"]
actions=action_B

for from_state in G1100:
    for action in actions:
        to_state = from_state[:2] + action[3] + from_state[3]
        probability = f'P19-{from_state}-{to_state}'
        trans_G1100ToG1110[(from_state,action,to_state)] = {'probability': probability}
#trans_G1100ToG1110


# In[89]:


#P20
#6-From state, G1100 taking action a-0B
#b.It goes to G1100 with Prob of P20=P(IB1f)
# Define transitions and probabilities from G1100 to G1100
trans_G1100ToG1100 = {}
actions=action_B

for from_state in G1100:
    for action in actions:
        to_state = from_state
        probability = f'P20-{from_state}-{to_state}'
        trans_G1100ToG1100[(from_state,action,to_state)] = {'probability': probability}
#trans_G1100ToG1100


# ## 7-From state   G1011   taking action=a-A0

# In[90]:


#P21
#7-From state   G1011   taking action=a-A0
#a.It goes to G1111 with Prob of P21=P(IA2p|IA1p)
## G1011 to G1111

# Define transitions and probabilities from G1011 to G1111
trans_G1011ToG1111= {}
actions=action_A

for from_state in G1011:
    for action in actions:
        to_state = from_state[0]+ action[2] +from_state[2:]
        probability = f'P21-{from_state}-{to_state}'
        trans_G1011ToG1111[(from_state,action,to_state)] = {'probability': probability}
trans_G1011ToG1111


# In[91]:


#P22
#7-From state   G1011   taking action=a-A0
#b.It goes to G0011 with Prob of P22= P(IA2f|IA1p)
## G1011 to G0011

# Define transitions and probabilities from G1011 to G0011
trans_G1011ToG0011= {}
actions=action_A

for from_state in G1011:
    for action in actions:
        to_state = '00'+from_state[2:]
        probability = f'P22-{from_state}-{to_state}'
        trans_G1011ToG0011[(from_state,action,to_state)] = {'probability': probability}
#trans_G1011ToG0011


# ## 8-From state G1110 taking action a-0B

# In[92]:


#P23
#8-From state G1110 taking action a-0B
#a.It goes to G1111 with Prob of P23=P(IB2p|IB1p)
## G1110 to G1111

# Define transitions and probabilities from G1110 to G1111
trans_G1110ToG1111 = {}
actions=action_B

for from_state in G1110:
    for action in actions:
        to_state = from_state[0:3]+ action[3] 
        probability = f'P23-{from_state}-{to_state}'
        trans_G1110ToG1111[(from_state,action,to_state)] = {'probability': probability}
trans_G1110ToG1111


# In[93]:


#P24
#8-From state G1110 taking action a-0B
#b.It goes to G1100 with Prob of P24=P(IB2f|IB1p)
## G1110 to G1100

# Define transitions and probabilities from G1110 to G1100
trans_G1110ToG1100 = {}
actions=action_B

for from_state in G1110:
    for action in actions:
        to_state = from_state[0:2]+ '00'
        probability = f'P24-{from_state}-{to_state}'
        trans_G1110ToG1100[(from_state,action,to_state)] = {'probability': probability}
#trans_G1110ToG1100


# ## 9-From State G1111 taking action a-M

# In[94]:


#P25
#9-From State G1111 taking action a-M
#a.It goes to GF with the prob of P25
## G1111 to GF

# Define transitions and probabilities from G1111 to GF
trans_G1111ToGF = {}
#action_M=["a-M"]
actions=action_M

for from_state in G1111:
    for action in actions:
        to_state = 'Final'
        probability = f'P25-{from_state}-{to_state}'
        trans_G1111ToGF[(from_state,action,to_state)] = {'probability': probability}
#trans_G1111ToGF


# In[95]:


#P26
#9-From State G1111 taking action a-M
#b.It goes to G0000 with the prob of P26
## G1111 to G0000

# Define transitions and probabilities from G1111 to G0000
trans_G1111ToG0000 = {}
actions=action_M

for from_state in G1111:
    for action in actions:
        to_state = '0000'
        probability = f'P26-{from_state}-{to_state}'
        trans_G1111ToG0000[(from_state,action,to_state)] = {'probability': probability}
trans_G1111ToG0000


# ## 10-From state GF taking action a-F

# In[96]:


#P27
#10-From state GF taking action a-F
#a.It goes to GF with the prob of P27
## GF to GF

# Define transitions and probabilities from GF to GF
trans_GFToGF = {}
actions=action_F

for from_state in GF:
    for action in actions:
        to_state = 'Final'
        probability = 'P27-Final-Final'
        trans_GFToGF[(from_state,action,to_state)] = {'probability': probability}
trans_GFToGF


# ## All transitions

# In[99]:


transitions={**trans_G0000ToG1010,**trans_G0000ToG0010,**trans_G0000ToG1000,**trans_G0000ToG0000,
             **trans_G0010ToG1011,**trans_G0010ToG0011,**trans_G0010ToG1000,**trans_G0010ToG0000,
             **trans_G1010ToG1111,**trans_G1010ToG0011,**trans_G1010ToG1100,**trans_G1010ToG0000,
             **trans_G1000ToG1110,**trans_G1000ToG1100,**trans_G1000ToG0010,**trans_G1000ToG0000 ,
             **trans_G0011ToG1011,**trans_G0011ToG0011,
             **trans_G1100ToG1110,**trans_G1100ToG1100,
             **trans_G1011ToG1111,**trans_G1011ToG0011,
             **trans_G1110ToG1111,**trans_G1110ToG1100,
             **trans_G1111ToGF,**trans_G1111ToG0000,
             **trans_GFToGF}
len(transitions)


# In[100]:


transitions


# ## Initial Dictionary of all transition probabilities

# In[32]:


# Initial Dictionary of all transition probabilities

#all probabilities in one list
all_probs = [value['probability'] for value in transitions.values()]

#create a dictionary which initial values of all probablities be equal to zero
probsValues_dict = {name: 0 for name in all_probs}


# # Rewards 

# ## cost variables and the initial matrix of rewards

# In[33]:


############################ cost variables and the initial matrix of rewards ############################
#
######################################
#cost Variables

#raw material cost:
rawMaterial_cost=-2

#Inspection cost
noInsp_cost=0
gel_cost=-14      #changing GElCost
bio_cost=-76.25
seqCost=-626
    
    
#Operastion Costs
PCR_cost=-29
cloning_cost=-54.10
assembly_cost=-81
#assembly_cost=0
#large cost
large_cost=-100000

#stay in the current state(Final-Final) cost
stay_in_final_cost=0


# ## Costs of taking each action

# In[34]:


# Define costs
cost_dict = {
    'a-NN': noInsp_cost + noInsp_cost,
    'a-NG': noInsp_cost + gel_cost,
    'a-NY': noInsp_cost + bio_cost,
    'a-NS': noInsp_cost + seqCost,
    'a-GN': gel_cost + noInsp_cost,
    'a-GG': gel_cost + gel_cost,
    'a-GY': gel_cost + bio_cost,
    'a-GS': gel_cost + seqCost,
    'a-YN': bio_cost + noInsp_cost,
    'a-YG': bio_cost + gel_cost,
    'a-YY': bio_cost + bio_cost,
    'a-YS': bio_cost + seqCost,
    'a-SN': seqCost + noInsp_cost,
    'a-SG': seqCost + gel_cost,
    'a-SY': seqCost + bio_cost,
    'a-SS': seqCost + seqCost,
    'a-0N': noInsp_cost,
    'a-0G': gel_cost,
    'a-0Y': bio_cost,
    'a-0S': seqCost,
    'a-N0': noInsp_cost,
    'a-G0': gel_cost,
    'a-Y0': bio_cost,
    'a-S0': seqCost,
    'a-M': assembly_cost +seqCost , #think about this one
    'a-F': stay_in_final_cost
}


# # Cost of each transition

# ## 1-Cost :From State = G0000   taking  action=a-AB

# In[36]:


#1.a Cost of transition 
#1-From State = G0000   taking  action=a-AB
#a.It goes to G1010 with prob of P1= P(IA1p)*P(IB1p)
## Cost of G0000 to G1010


# Define transitions and costs from G0000 to G1010
cost_G0000ToG1010 = {}
actions=action_AB

for from_state in G0000:
    for action in actions:
        to_state =  action[2]+from_state[0]+ action[3] + from_state[3]
        trans_cost = cost_dict[action] +2*PCR_cost
        cost_G0000ToG1010[(from_state,action,to_state)] = {'transition cost': trans_cost}
#cost_G0000ToG1010


# In[35]:


#1.b Cost of transition 
#1-From State = G0000   taking  action=a-AB
#b.IT GOES TO G0010 with Prob of P2=P(IA1f)*P(IB1p)
## Cost of G0000 to G0010
# Define transitions and costs from G0000 to G0010
cost_G0000ToG0010 = {}
actions=action_AB

for from_state in G0000:
    for action in actions:
        to_state = from_state[0:2]+ action[3] + from_state[3]
        trans_cost = cost_dict[action] +2*PCR_cost
        cost_G0000ToG0010[(from_state,action,to_state)] = {'transition cost': trans_cost}

#cost_G0000ToG0010


# In[37]:


#1.c Cost of transition
#1-From State = G0000   taking  action=a-AB
## Cost of  G0000 to G1000
# Define transitions and costs from G0000 to G1000
cost_G0000ToG1000 = {}
actions=action_AB

for from_state in G0000:
    for action in actions:
        to_state = action[2] + from_state[1:]
        trans_cost = cost_dict[action] +2*PCR_cost
        cost_G0000ToG1000[(from_state,action,to_state)] = {'transition cost': trans_cost}
#cost_G0000ToG1000


# In[38]:


#1.d Cost of transition
#1-From State = G0000   taking  action=a-AB
#G0000 to G0000
cost_G0000ToG0000 = {}
actions=action_AB

for from_state in G0000:
    for action in actions:
        to_state = from_state
        trans_cost = cost_dict[action] +2*PCR_cost
        cost_G0000ToG0000[(from_state,action,to_state)] = {'transition cost': trans_cost}
#cost_G0000ToG0000


# ## 2- Cost: From State    G0010     taking    action=a-AB

# In[39]:


#2.a Cost of transition
#2-From State    G0010     taking    action=a-AB
## Cost of G0010 to G1011

# Define transitions and cost from G0010 to G1011
cost_G0010ToG1011 = {}
actions=action_AB

for from_state in G0010:
    for action in actions:
        to_state = action[2]+ from_state[1]+ from_state[2] + action[3]
        trans_cost = cost_dict[action] + PCR_cost+  cloning_cost
        cost_G0010ToG1011[(from_state,action,to_state)] = {'transition cost': trans_cost}
#cost_G0010ToG1011


# In[40]:


#2.b
#2-From State    G0010     taking    action=a-AB
## Cost of G0010 to G0011
## G0010 to G0011

# Define transitions and costs from G0010 to G0011
cost_G0010ToG0011 = {}
actions=action_AB

for from_state in G0010:
    for action in actions:
        to_state = from_state[0:3]+ action[3]
        trans_cost = cost_dict[action] +PCR_cost+  cloning_cost
        cost_G0010ToG0011[(from_state,action,to_state)] = {'transition cost': trans_cost}
        
#cost_G0010ToG0011


# In[41]:


#2.c
#2-From State    G0010     taking    action=a-AB
# Define transitions and costs from G0010 to G1000
cost_G0010ToG1000 = {}
actions=action_AB

for from_state in G0010:
    for action in actions:
        to_state = action[2]+from_state[1]+'0'+from_state[3]
        trans_cost = cost_dict[action] +PCR_cost+  cloning_cost
        cost_G0010ToG1000[(from_state,action,to_state)] = {'transition cost': trans_cost}
        
#cost_G0010ToG1000


# In[42]:


#2.d
#2-From State    G0010     taking    action=a-AB
# Define transitions and costs from G0010 to G0000
cost_G0010ToG0000 = {}
actions=action_AB

for from_state in G0010:
    for action in actions:
        to_state = '0000'
        trans_cost = cost_dict[action] +PCR_cost+  cloning_cost
        cost_G0010ToG0000[(from_state,action,to_state)] = {'transition cost': trans_cost}
        
#cost_G0010ToG0000


# ## 3- Cost: From state   G1010   taking action=a-AB

# In[44]:


#3.a
#3-From state   G1010  taking action=a-AB
#G1010 to G1111
## Cost of G1010 to G1111

# Define transitions and costs from G1010 to G1111
cost_G1010ToG1111 = {}
actions=action_AB

for from_state in G1010:
    for action in actions:
        to_state = from_state[0] + action[2]+ from_state[2] + action[3] 
        trans_cost = cost_dict[action] +2*cloning_cost
        cost_G1010ToG1111[(from_state,action,to_state)] = {'transition cost': trans_cost}
#cost_G1010ToG1111


# In[43]:


#3.b
#3-From state   G1010   taking action=a-AB
#G1010 to G0011
cost_G1010ToG0011 = {}
actions=action_AB

for from_state in G1010:
    for action in actions:
        to_state = '00'+from_state[2]+action[3]
        trans_cost = cost_dict[action] +2*cloning_cost
        cost_G1010ToG0011[(from_state,action,to_state)] = {'transition cost': trans_cost}
        
#cost_G1010ToG0011


# In[45]:


#3.c
#3-From state   G1010  taking action=a-AB
#G1010 to G1100
# Define transitions and costs from G1010 to G1100
cost_G1010ToG1100 = {}
actions=action_AB

for from_state in G1010:
    for action in actions:
        to_state = from_state[0] + action[2]+ '00'  
        trans_cost = cost_dict[action] +2*cloning_cost
        cost_G1010ToG1100[(from_state,action,to_state)] = {'transition cost': trans_cost}
#cost_G1010ToG1100


# In[46]:


#3.d
#3-From state   G1010  taking action=a-AB
#G1010 to G0000
cost_G1010ToG0000 = {}
actions=action_AB

for from_state in G1010:
    for action in actions:
        to_state = '0000'   
        trans_cost = cost_dict[action] +2*cloning_cost
        cost_G1010ToG0000[(from_state,action,to_state)] = {'transition cost': trans_cost}
cost_G1010ToG0000


# ## 4- Cost: From state   G1000   taking action=a-AB

# In[47]:


#13
#4.a
#4-From state   G1000   taking action=a-AB
#G1000 to G1110
## Cost of G1000 to G1110

# Define transitions and cost from G1000 to G1110
cost_G1000ToG1110 = {}
actions=action_AB

for from_state in G1000:
    for action in actions:
        to_state =  from_state[0]+action[2] + action[3] + from_state[3]
        trans_cost = cost_dict[action] +   cloning_cost + PCR_cost
        cost_G1000ToG1110[(from_state,action,to_state)] = {'transition cost': trans_cost}
#cost_G1000ToG1110


# In[48]:


#14
#4.b
#4-From state   G1000   taking action=a-AB
## G1000 to G1100
## Cost of G1000 to G1100

# Define transitions and costs from G1000 to G1100
cost_G1000ToG1100 = {}
actions = action_AB

for from_state in G1000:
    for action in actions:
        to_state = from_state[0] + action[2] + from_state[2:]
        trans_cost = cost_dict[action] +cloning_cost+PCR_cost
        cost_G1000ToG1100[(from_state,action,to_state)] = {'transition cost': trans_cost}
#cost_G1000ToG1100


# In[49]:


#15
#4.c
#4-From state   G1000   taking action=a-AB
## G1000 to G0010
# Define transitions and costs from G1000 to G0010
cost_G1000ToG0010 = {}
actions = action_AB

for from_state in G1000:
    for action in actions:
        to_state = '00' + action[3]+from_state[3]
        trans_cost = cost_dict[action] +cloning_cost+PCR_cost
        cost_G1000ToG0010[(from_state,action,to_state)] = {'transition cost': trans_cost}
#cost_G1000ToG0010


# In[50]:


#16
#4.d
#4-From state   G1000   taking action=a-AB
## G1000 to G0000
cost_G1000ToG0000 = {}
actions = action_AB

for from_state in G1000:
    for action in actions:
        to_state = '0000'
        trans_cost = cost_dict[action] +cloning_cost+PCR_cost
        cost_G1000ToG0000[(from_state,action,to_state)] = {'transition cost': trans_cost}
#cost_G1000ToG0000


# ## 5-From state   G0011   taking action=a-A0

# In[51]:


#17
#5.a
#5-From state   G0011   taking action=a-A0
## G0011 To G1011

# Define transitions and costs from G0011 to G1011
cost_G0011ToG1011 = {}
actions=action_A

for from_state in G0011:
    for action in actions:
        to_state = action[2:] +from_state[2:]
        trans_cost = cost_dict[action] + PCR_cost
        cost_G0011ToG1011[(from_state,action,to_state)] = {'transition cost': trans_cost}
#cost_G0011ToG1011


# In[52]:


#18
#5.b
#5-From state   G0011   taking action=a-A0
# G0011 to G0011
cost_G0011ToG0011 = {}
actions=action_A

for from_state in G0011:
    for action in actions:
        to_state = from_state
        trans_cost = cost_dict[action] + PCR_cost
        cost_G0011ToG0011[(from_state,action,to_state)] = {'transition cost': trans_cost}
#cost_G0011ToG0011


# ## 6-Cost: From state G1100 taking action a-0B

# In[53]:


#19
#6.a
#6-From state, G1100 taking action a-0B
## G1100 to G1110
## Cost of G1100 to G1110

# Define transitions and costs from G1100 to G1110
cost_G1100ToG1110 = {}
#action_B=["a-0N", "a-0G", "a-0Y", "a-0S"]
actions=action_B

for from_state in G1100:
    for action in actions:
        to_state = from_state[:2] + action[3] + from_state[3]
        trans_cost = cost_dict[action] +PCR_cost
        cost_G1100ToG1110[(from_state,action,to_state)] = {'transition cost': trans_cost}
#cost_G1100ToG1110


# In[54]:


#20
#6.b
#6-From state, G1100 taking action a-0B
cost_G1100ToG1100 = {}
#action_B=["a-0N", "a-0G", "a-0Y", "a-0S"]
actions=action_B

for from_state in G1100:
    for action in actions:
        to_state = from_state
        trans_cost = cost_dict[action] +PCR_cost
        cost_G1100ToG1100[(from_state,action,to_state)] = {'transition cost': trans_cost}
#cost_G1100ToG1100


# ## 7-Cost: From state   G1011   taking action=a-A0

# In[55]:


#21
#7.a
#7-From state   G1011   taking action=a-A0
## G1011 to G1111
## Cost of G1011 to G1111

cost_G1011ToG1111= {}
actions=action_A

for from_state in G1011:
    for action in actions:
        to_state = from_state[0]+ action[2] +from_state[2:]
        trans_cost = cost_dict[action] + cloning_cost
        cost_G1011ToG1111[(from_state,action,to_state)] = {'transition cost': trans_cost}
#cost_G1011ToG1111


# In[56]:


#22
#7.b
#7-From state   G1011   taking action=a-A0
## G1011 to G0011
cost_G1011ToG0011= {}
actions=action_A

for from_state in G1011:
    for action in actions:
        to_state = '00'+from_state[2:]
        trans_cost = cost_dict[action] + cloning_cost
        cost_G1011ToG0011[(from_state,action,to_state)] = {'transition cost': trans_cost}
#cost_G1011ToG0011


# ## 8-From state G1110 taking action a-0B

# In[57]:


#23
#8.a
#8-From state G1110 taking action a-0B
## G1110 to G1111

# Define transitions and cost from G1110 to G1111
cost_G1110ToG1111 = {}
actions=action_B

for from_state in G1110:
    for action in actions:
        to_state = from_state[0:3]+ action[3] 
        trans_cost = cost_dict[action] + cloning_cost
        cost_G1110ToG1111[(from_state,action,to_state)] = {'transition cost': trans_cost}
#cost_G1110ToG1111


# In[58]:


#24
#8.b
#8-From state G1110 taking action a-0B
## G1110 to G1100
# Define transitions and cost from G1110 to G1100
cost_G1110ToG1100 = {}
actions=action_B

for from_state in G1110:
    for action in actions:
        to_state = from_state[0:2]+ '00' 
        trans_cost = cost_dict[action] + cloning_cost
        cost_G1110ToG1100[(from_state,action,to_state)] = {'transition cost': trans_cost}
#cost_G1110ToG1100


# ## 9-From State G1111 taking action a-M

# In[59]:


#25
#9.a
##9-From State G1111 taking action a-M
## G1111 to GF
# Define transitions and cost from G1111 to GF
cost_G1111ToGF = {}
#action_M=["a-M"]
actions=action_M

for from_state in G1111:
    for action in actions:
        to_state = 'Final'
        trans_cost = cost_dict[action] # a-M has both assembly cost and final sequencing cost
        cost_G1111ToGF[(from_state,action,to_state)] = {'transition cost': trans_cost}
#cost_G1111ToGF


# In[60]:


#26
#9.b
##9-From State G1111 taking action a-M
## G1111 to G0000
cost_G1111ToG0000 = {}
actions=action_M

for from_state in G1111:
    for action in actions:
        to_state = '0000'
        trans_cost = cost_dict[action] # a-M has both assembly cost and final sequencing cost
        cost_G1111ToG0000[(from_state,action,to_state)] = {'transition cost': trans_cost}
#cost_G1111ToG0000


# ## 10-From state GF taking action a-F

# In[61]:


#27
#10.a
#10-From state GF taking action a-F
## GF to GF
cost_GFToGF = {}
#action_F=["a-F"]
actions=action_F

for from_state in GF:
    for action in actions:
        to_state = 'Final'
        trans_cost = cost_dict[action]
        cost_GFToGF[(from_state,action,to_state)] = {'transition cost': trans_cost}
cost_GFToGF


# # All cost transitions

# In[101]:


# Concatenate all transitions with their costs
cost_all_transitions ={**cost_G0000ToG1010,**cost_G0000ToG0010,**cost_G0000ToG1000,**cost_G0000ToG0000,
                       **cost_G0010ToG1011,**cost_G0010ToG0011,**cost_G0010ToG1000,**cost_G0010ToG0000,
                       **cost_G1010ToG1111,**cost_G1010ToG0011,**cost_G1010ToG1100,**cost_G1010ToG0000,
                       **cost_G1000ToG1110,**cost_G1000ToG1100,**cost_G1000ToG0010,**cost_G1000ToG0000,
                       **cost_G0011ToG1011,**cost_G0011ToG0011,
                       **cost_G1100ToG1110,**cost_G1100ToG1100,
                       **cost_G1011ToG1111,**cost_G1011ToG0011,
                       **cost_G1110ToG1111,**cost_G1110ToG1100,
                       **cost_G1111ToGF,**cost_G1111ToG0000,
                       **cost_GFToGF}
len(cost_all_transitions)


# # Table of Rewards

# In[102]:


####################################
### Table of Rewards

#the initial matrix of rewards

#data frame of states num_states *num_actions
import pandas as pd

# Define the number of rows and columns
num_rows = len(all_states)
num_cols = len(action_list)

# Create column and index labels
index = all_states
columns = action_list

# Create an empty DataFrame
df_rewards = pd.DataFrame(large_cost,index=index, columns=columns) #we use -100000as the big cost , 
                                                                #for the transition which we 
#                                                               # do not want to happend
########################################

# Update the table based on transition dictionary
for (from_state, action,to_state), details in cost_all_transitions.items():
    #print(action)
    transition_cost = details['transition cost']
    #print(transition_cost)
    df_rewards.at[from_state,action] = transition_cost #when we are in a state and taking an action, 
                                                       #it does not matter where we end up by taking that action ,
                                                       #the cost is fixed
    
df_rewards


# In[103]:


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
df_rewards


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




