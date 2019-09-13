#!/usr/bin/python
"""
Take an abbreviated interface name (like Eth1/1) and expand it to its full length (Ethernet1/1)
"""
import re


def normalize(input_interfaces):
    """
    Take a collection of interfaces and expand them to their full names

    :param input_interfaces: Input interfaces that are abbreviated
    :return: A list of fully-expanded interface names
    """
    INTERFACE_ABBREVIATE_LOOKUP = {
        'e': 'Ethernet',
        'g': 'GigabitEthernet',
        'p': 'Port-Channel'
    }
    ports = []
    for interface in input_interfaces:
        prefix = str(interface[0]).lower()
        # print(prefix)
        full_prefix = str(INTERFACE_ABBREVIATE_LOOKUP[prefix])
        m = re.search("\d", interface)
        suffix = interface[m.start():]
        # print(suffix)
        normalized_name = full_prefix + suffix
        # print(normalized_name)
        ports.append(normalized_name)
    return ports


class FilterModule(object):

    def filters(self):
        """
        Associate the filter name with a specific function
        :return: the filter-to-function conversion
        """
        return {
            'normalize_interface_names': normalize,
        }
