import os
import sys
import xml.etree.ElementTree as ET

def count_members_in_package(package_file):
    if not os.path.exists(package_file):
        return 0
    
    try:
        tree = ET.parse(package_file)
        root = tree.getroot()

        namespace = {'sf': 'http://soap.sforce.com/2006/04/metadata'}

        member_count = sum(len(type_elem.findall('sf:members', namespace)) for type_elem in root.findall('sf:types', namespace))
        return member_count

    except ET.ParseError:
        return 0
    except Exception as e:
        return 0

print(count_members_in_package(sys.argv[1]))
