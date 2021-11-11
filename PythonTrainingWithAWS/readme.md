# XML to Ansible-Compatible YAML

### Requirement:

1. Write a converter to read the XML[1] and generate an Ansible-compatible YAML file.
2. it outputs a JSON-formatted string [2] indicating that instructions for each IP
address have been converted successfully or not.
3. It is expected that you will test this by deploying via Ansible <br/>

[1] Here is an example of an XML file:
```xml
<systems>
  <host>
    <ip>192.168.1.1</ip>
    <job>
      <command>some_command argument</command>
      <comment>Do something!</comment>
    </job>
  </host>
  <host>
    <ip>192.168.1.2</ip>
    <job>
      <command>another_command</command>
      <comment>Do something else</comment>
    </job>
    <job>
      <command>yet_another_command</command>
    </job>
  </host>
  <host>
    <ip>666.666.666.666</ip>
    <job>
      <command>some_command argument</command>
      <comment>Do something!</comment>
    </job>
  </host>
  <host>
    <ip>192.168.202.130</ip>
    <job>
      <command>mkdir /tmp/markinghere</command>
      <comment>Leaving a mark</comment>
    </job>
  </host>
</systems>
```


[2] For the systems described in the XML format above will output JSON like:<br/>
[{"ip":"192.168.1.1", "success":true},{"ip":"192.168.1.2", "success":true},{"ip":"666.666.666.666","success":false}]<br/><br/>


### System requirement
Please install python 3.8.10

### Running the tests

usage: ./xml2yaml.py INFILE.xml OUTFILE.yml<br/><br/>

  INFILE is XML file format<br/>
  OUTFILE is an extract in YAML format<br/>
  nb: OUTFILE will be overwritten.<br/>


### Imported Libraries
1.	xml.com.minidom
2.	xml.etree.ElementTree as ET
3.	subprocess
4.	json
5.	sys
6. 	os
7.	re


### Bug Fixes:

### Release Notes:
#1.0.0 - CJ 11.11.2021 First draft
