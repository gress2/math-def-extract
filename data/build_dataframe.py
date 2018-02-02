'''
Note: You probably will just want to deal with the generated committed
dataframe directly but committing these scripts in case we need to
modify what and how we're extracting data from the dumps.

All we're doing here is reading math type articles as xml and creating
a dataframe containing the raw articles for data exploration.
'''
import pandas as pd
import os

from lxml import etree

pages = list()

math_dir = os.path.dirname(os.path.realpath(__file__)) + '/math/'
for math_file in os.listdir(math_dir):
    if math_file.endswith('_math'):
        with open(math_dir + math_file) as m:
            root = etree.parse(m).getroot()
            for el in root.iter('page'):
                pages.append(el.text)

df = pd.DataFrame.from_items([('article', pages)])
df.to_pickle('math_articles.pd')
