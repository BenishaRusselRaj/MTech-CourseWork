# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 15:40:54 2025

@author: IITM
"""
from pgmpy.independencies import IndependenceAssertion

assertion1 = IndependenceAssertion('X', 'Y')

print(assertion1)

threeVariableAssertion = IndependenceAssertion('X','Y','Z')

print(threeVariableAssertion)

multiAssertion = IndependenceAssertion('X',['Y','Z'],['A','B'])

print(multiAssertion)

#%%

from pgmpy.factors import JointProbabilityDistribution as Joint

distribution = Joint(['coin1','coin2'], [2, 2], 
                     [0.25, 0.25, 0.25, 0.25])

print(distribution)

#%%

from pgmpy.models import BayesianNetwork

model = BayesianNetwork()

model.add_nodes_from(['rain', 'traffic_jam'])
model.add_edge('rain', 'traffic_jam')

model.add_edge('accident','traffic_jam')

print('Nodes: ', model.nodes())
print('Edges:', model.edges())

#%%

from pgmpy.factors import TabularCPD

cpd_rain = TabularCPD("rain", 2, [[0.4], [0.6]])

cpd_accident = TabularCPD("accident", 2, [[0.2], [0.8]])

cpd_traffic_jam = TabularCPD("traffic_jam", 2, [[0.9,0.6,0.7,0.1],
                                                [0.1,0.4,0.3,0.9]], 
                             evidence = ["raing", "accident"], 
                             evidence_card = [2,2])

model.add_cpds(cpd_rain, cpd_accident, cpd_traffic_jam)
print (model.get_cpds())