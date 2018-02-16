'''
Note: You probably will just want to deal with the generated committed
dataframe directly but committing these scripts in case we need to
modify what and how we're extracting data from the dumps.

This script should be run on each xml pulled from the en-wiki dump.
It searches the articles within the xml and outputs only the
articles containing mathematical expressions in the math
directory. When processing large xml files, its not feasible to load
the entire xml tree into memory so we use lxml.etree.iterparse instead
'''
from sys import argv
from lxml import etree

if len(argv) != 2:
    print('Usage: python cull.py <FILE>')
    exit()

fname = argv[1]
print('Parsing ' + fname)

nsmap = {}

# build a namespace map
for event, element in etree.iterparse(fname):
    tag = element.tag
    if '}' in tag:
        tag_no_ns = tag.split('}', 1)[1]
        if tag_no_ns not in nsmap:
            nsmap[tag_no_ns] = tag

mathroot = etree.Element('pages')

with open('math/' + fname + '_math', 'ab') as f:
    for event, element in etree.iterparse(fname, tag=nsmap['page']):
        text = element.find(nsmap['revision']).find(nsmap['text']).text
        if text is not None and (('{{math|' in text) or ('&lt;math' in text)):
            page = etree.Element('page')
            page.text = text
            mathroot.append(page)
        element.clear()
    f.write(etree.tostring(mathroot, method='xml'))
