import xml.etree.ElementTree as ET
from typing import Union

def xml_to_dict(xml_string: Union[str, bytes]) -> Union[dict, None]:
    try:
        etree_obj = ET.XML(xml_string)
        result = element_to_dict(etree_obj)
        result = {etree_obj.tag: result}
        return result
    except Exception as ex:
        print(f'Failed to transform XML to dict. Error: {str(ex)}')
        return None

def element_to_dict(element):
    dict_obj = {}

    # Process attributes
    if element.attrib:
        for attr_name, attr_value in element.attrib.items():
            dict_obj["@" + attr_name] = attr_value

    # Process child elements
    for child_element in element:
        child_dict = element_to_dict(child_element)

        # Add to dict if the child element has text, attributes, or child elements
        if child_element.text and child_element.text.strip():
            dict_obj[child_element.tag] = child_element.text.strip()

        if child_dict or element.attrib:
            if child_element.tag in dict_obj:
                if type(dict_obj[child_element.tag]) is list:
                    dict_obj[child_element.tag].append(child_dict)
                else:
                    dict_obj[child_element.tag] = [dict_obj[child_element.tag], child_dict]
            else:
                dict_obj[child_element.tag] = child_dict

    return dict_obj
