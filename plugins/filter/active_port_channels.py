#!/usr/bin/python
"""

"""


def find_port_channels(summary, interfaces):
    """
    """
    active = []
    for interface in interfaces:
        print(interface)
        if summary["interfaces"][interface]["oper_status"] == "up":
            print("appending " + interface)
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

