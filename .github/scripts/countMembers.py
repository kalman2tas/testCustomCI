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

        types_elements = root.findall('sf:types', namespace)
        if not types_elements:
            types_elem = ET.Element('{http://soap.sforce.com/2006/04/metadata}types')
            root.append(types_elem)
            tree.write(package_file, encoding='utf-8', xml_declaration=True)
            return 0

        member_count = sum(len(type_elem.findall('sf:members', namespace)) for type_elem in types_elements)
        return member_count

    except ET.ParseError:
        return 0
    except Exception as e:
        return 0

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(count_members_in_package(sys.argv[1]))
