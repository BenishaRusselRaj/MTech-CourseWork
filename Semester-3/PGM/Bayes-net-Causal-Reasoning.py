# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 15:28:51 2025

@author: IITM
"""
from libpgm.graphskeleton import GraphSkeleton
from libpgm.nodedata import NodeData
from libpgm.discretebayesiannetwork import DiscreteBayesianNetwork
from libpgm.tablepdffactorization import TableCPDFactorization

def getTableCPD():
    nd = NodeData()
    skel = GraphSkeleton()
    jsonpath = "job_interview.txt"
    nd.load(jsonpath)
    skel.load(jsonpath)
    
    bn = DiscreteBayesianNetwork(skel, nd)
    tablecpd = TableCPDFactorization(bn)
    return tablecpd

tcpd = getTableCPD()
tcpd.specificquery(dict(Offer = '1'))