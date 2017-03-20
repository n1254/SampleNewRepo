#!C:\Users\n1254\AppData\Local\Programs\Python\Python36-32\python
# -*- coding:utf-8 -*-
from jinja2 import Environment, FileSystemLoader
from numpy.random import *
import codecs, math

env = Environment(loader=FileSystemLoader('./', encoding='utf-8'))
tmp1 = env.get_template('js/template_d3.js')

#html = tmp1.render(data_list = "[0, 30, 5, 60, 40, 178, 56, 130, 24, 80]")
numeric_list = []
for i in range(0, 10):
	numeric_list.append(math.floor(normal(150, 20)))
js = tmp1.render(data_list = numeric_list)

f = codecs.open('js/sample_d3.js', 'w', 'utf-8')
#f.write(html)
f.write(js)
f.close

