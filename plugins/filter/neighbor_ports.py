#!/usr/bin/python
"""
Take a "cdp neighbors" structure created by parse genie.  Return the local interfaces pointing to "host"
"""


def host_to_ports(neighbors, host):
    """
    Take a cdp neighbors structure created by parse genie and return the interfaces pointing to "host"
    :param neighbors: The cdp neighbors structure created by parse genie
    :param host: The host we want to find interfaces for
    :return: A list of interfaces connected to "host"
    """
    ports = []
    for ndx in neighbors["cdp"]["index"]:
        if str(host).lower() in str(neighbors["cdp"]["index"][ndx]["device_id"]).lower():
            # print(neighbors["cdp"]["index"][ndx]["local_interface"])
            ports.append(neighbors["cdp"]["index"][ndx]["local_interface"])
    return ports


class FilterModule(object):
    def filters(self):
        """
        Associate the filter with a specific function
        :return: the filter-to-function association
        """
        return {
            'neighbor_ports': host_to_ports,
        }

