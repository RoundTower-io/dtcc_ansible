#!/usr/bin/python

class FilterModule(object):

    def filters(self):
        return {
            'vlan_in_range': self.port_in_ports
        }


    def port_in_ports(self, input_ranges, vlan_number):
        if ',' in str(input_ranges):
            for range in str(input_ranges).split(','):
                bounds = str(range).split('-')
                if int(bounds[0]) <= int(vlan_number) <= int(bounds[1]):
                    return True
        else:
            bounds = str(input_ranges).split('-')
            return int(bounds[0]) <= int(vlan_number) <= int(bounds[1])
        return False
