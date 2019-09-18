#!/usr/bin/python
"""
Find active port channels out of a list
"""


def find_port_channels(summary, interfaces):
    """
    Look for an oper_status of "up" and return interfaces with that status
    """
    active = []
    for interface in interfaces:
        #print(interface)
        if summary["interfaces"][interface]["oper_status"] == "up":
            #print("appending " + interface)
            active.append(interface)
    return active


class FilterModule(object):
    def filters(self):
        """
        Associate the filter with a specific function
        :return: the filter-to-function association
        """
        return {
            'active_port_channels': find_port_channels,
        }

