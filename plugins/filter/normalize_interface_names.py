#!/usr/bin/python
import re


class FilterModule(object):

    def filters(self):
        return {
            'normalize_interface_names': self.normalize,
        }

    def normalize(self, input_interfaces):
        INTERFACE_ABBREVIATE_LOOKUP = {
            'e': 'Ethernet',
            'g': 'GigabitEthernet'
        }
        ports = []
        for interface in input_interfaces:
            prefix = str(interface[0]).lower()
            # print(prefix)
            full_prefix = str(INTERFACE_ABBREVIATE_LOOKUP[prefix])
            m = re.search('\d', interface)
            suffix = interface[m.start():]
            # print(suffix)
            normalized_name = full_prefix + suffix
            # print(normalized_name)
            ports.append(normalized_name)
        return ports
