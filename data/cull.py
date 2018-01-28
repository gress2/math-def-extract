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
        if text is not None and '{{math|' in text:
            page = etree.Element('page')
            page.text = text
            mathroot.append(page)
        element.clear()
    f.write(etree.tostring(mathroot, method='xml'))
