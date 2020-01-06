import xml.etree.ElementTree as ET
data = '''<person> #multilined string
    <name>Chuck</name>
    <phone type="intl">
        +1 734 303 4456
    </phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
#.text returns the text between
print('Attr:', tree.find('email').get('hide'))
#no text because this is a self-closing tag

#if there is a syntax error, this code could blow up
