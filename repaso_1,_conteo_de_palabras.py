# -*- coding: utf-8 -*-
"""Repaso 1, Conteo de palabras

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aQp9ngE4pxmWoXKHDOmhm0zpZklmmuHT

%%writefile file1.txt

Analytics is the discovery, interpretation, and communication of meaningful 
patterns in data; and the process of applying those patterns towards effective 
decision making. In other words, analytics can be understood as the connective 
tissue between data and effective decision making, within an organization. 
Especially valuable in areas rich with recorded information, analytics relies 
on the simultaneous application of statistics, computer programming and 
operations research to quantify performance.
"""

!ls

!cat file1.txt

txt = open('file1.txt', 'rt').readlines()
txt = [line.replace('\n', '') for line in txt]
txt = [line.replace('.', '') for line in txt]
txt = [line.replace(',', '') for line in txt]
txt = [line.replace(';', '') for line in txt]
txt = [line.lower() for line in txt]
txt = [line.split(' ') for line in txt]
txt = [[e for e in line if e != ''] for line in txt]
txt = ','.join([','.join(line) for line in txt]).split(',')
term = set(sorted(txt))
[(t, txt.count(t)) for t in sorted(term)]