"""Example working with XML"""

import xml.etree.ElementTree as xml
from datetime import datetime

#De-serialize XML file
tree = xml.parse('metric.xml')
root = tree.getroot()

print(root.tag)
for child in root:
    print(child.tag)

value = root.find('value') # find 'value' child tag
print('value: ', value.text)

for label in root.findall('./*/label'): #find children by XPATH
    key, value = label.get('key'), label.get('value')
    print(f'key = {key!r}, value = {value!r}')

#Serialize a dict
metric = {
    'time': datetime.now(),
    'name': 'CPU',
    'value': 3.4,
    'labels': {
        'host': 'prod9',
        'version': '1.4.4'
    }
}

def new_element(tag, text):
    """ a func to  create an element with text"""
    elem = xml.Element(tag)
    elem.text = text
    return elem

root = xml.Element('metric')
root.append(new_element('time', metric['time'].isoformat()))
root.append(new_element('name', metric['name']))
root.append(new_element('value', str(metric['value'])))
labels = xml.Element('labels')
for key, value in metric['labels'].items():
    labels.append(xml.Element('label', key=key, value=value))
root.append(labels)
data = xml.tostring(root)
print('xml:', data.decode(encoding='utf-8'))
