import os
import xml.etree.ElementTree as ET

def count_members_in_package(package_file):
    if not os.path.exists(package_file):
        print(f"Fájl nem létezik: {package_file}")
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

def count_members_in_multiple_packages(package_files):
    total_members = 0
    for package_file in package_files:
        total_members += count_members_in_package(package_file)
    return total_members

if __name__ == "__main__":
    package_files = [
        'package/package.xml',
        'destructiveChanges/destructiveChanges.xml',
    ]
    

    total_member_count = count_members_in_multiple_packages(package_files)
    print(total_member_count)
