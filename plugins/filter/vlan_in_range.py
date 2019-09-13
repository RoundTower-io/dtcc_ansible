#!/usr/bin/python
"""
Given a range, or collection, of vlan numbers ("input_ranges"), determine if "vlan_number"
is in the range.

"""


def port_in_ports(input_ranges, vlan_number):
    """
    Determine if "vlan_number" is included in "input_ranges"

    :param input_ranges: One or more vlan ranges of the form:
                         "1-99,101-199,201-1399,1401-4094"
                         OR
                         "1-4000"
    :param vlan_number: An int representing a vlan number
    :return: Boolean
    """
    if ',' in str(input_ranges):
        for vlan_range in str(input_ranges).split(','):
            bounds = str(vlan_range).split('-')
            if int(bounds[0]) <= int(vlan_number) <= int(bounds[1]):
                return True
    else:
        bounds = str(input_ranges).split('-')
        return int(bounds[0]) <= int(vlan_number) <= int(bounds[1])
    return False


class FilterModule(object):
    """
    A module for Ansible filters
    """

    def filters(self):
        """
        Associate the filter with a specific function
        :return: The filter-to-function associate
        """
        return {
            'vlan_in_range': port_in_ports
        }
