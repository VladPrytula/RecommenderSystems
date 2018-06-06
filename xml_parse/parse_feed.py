import xml.etree.ElementTree as ET


tree = ET.parse('20180527_0349_certona_productfeed_de.xml')
root = tree.getroot()


def convert_to_csv():
    with open("feed_processed.csv", "a", encoding='utf-8') as myfile:
        for it in root.iter('item'):
            id = it.find('id')
            name = it.find('itemattributes').find('name')
            url = it.find('itemattributes').find('detailURL')
            myfile.write(id.text + "," + name.text + "," + url.text + "\n")

def main():
    convert_to_csv()
    #items = root.findall('./catalog/items/item/')
    #for item in items:
    #    print(item.items())
    for it in root.iter('item'):
        # print(ET.tostring(it, encoding='utf8').decode('utf8'))
        #print(sub_id.text)
        #print(ET.tostring(sub_id, encoding='utf8').decode('utf8'))
        tmp_id = it.find('id')
        #print(ET.tostring(tmp_id, encoding='utf8').decode('utf8'))
        print(tmp_id.text)
        #for e in it.iter('id'):
        #    print ('--------------------------------')
        #    print(ET.tostring(e, encoding='utf8').decode('utf8'))
        #    print ('--------------------------------')
        tmp = it.find('itemattributes').find('name')
        print(tmp.text)
        url = it.find('itemattributes').find('detailURL')
        #print(ET.tostring(tmp, encoding='utf8').decode('utf8'))
        print(url.text)

        break


if __name__=='__main__':
    main()
