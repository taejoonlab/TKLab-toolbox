#!/usr/bin/env python3
import sys
from xml.dom import minidom

filename_xml = '/home/taejoon/pub/interpro/75.0/interpro.xml'
#filename_xml = '/home/taejoon/pub/interpro/75.0/tmp.xml'

doc = minidom.parse(filename_xml)

for tmp_ip in doc.getElementsByTagName("interpro"):
    tmp_id = tmp_ip.getAttribute('id')
    tmp_name = tmp_ip.getAttribute('short_name')

    for tmp_m in tmp_ip.getElementsByTagName('member_list'):
        for tmp_xref in tmp_m.getElementsByTagName('db_xref'):
            tmp_db = tmp_xref.getAttribute('db')
            tmp_db_key = tmp_xref.getAttribute('dbkey')
            tmp_db_name = tmp_xref.getAttribute('name')
            print("%s\t%s\t%s\t%s\t%s" % (tmp_id, tmp_name, tmp_db, tmp_db_key, tmp_db_name))

#<member_list>
#<db_xref protein_count="6582" db="PFAM" dbkey="PF00051" name="Kringle"/>
