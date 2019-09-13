#!/usr/bin/python
"""
Given a list of interfaces, return only the port channel interfaces
"""


def port_channels(input_interfaces):
    """
    Find (and return) port channels in a collection of interface names
    :param input_interfaces: A collection of interface names
    :return: A list of port channel interfaces
    """
    ports = []
    for interface in input_interfaces:
        interface_lower = str(interface).lower()
        if interface_lower.startswith('po'):
            ports.append(interface)
    return ports


class FilterModule(object):

    def filters(self):
        """
        Associate the filter with a function
        :return: The filter-to-function association
        """
        return {
            'port_channels': port_channels
        }
