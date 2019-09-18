#!/usr/bin/python
"""
Get the neighbor switch name from cdp neighbors output
"""


def host_in_output(host, output):
    """
    Find the host name in the output passed
    """
    for line in output.split('\n'):
        if str(host).lower() in str(line).lower():
            return True

    return False


def neighbor_port_channels(neighbors, hosts):
    """
    Take cdp neighbors output and find the neighbor for a particular host
    """
    interfaces = []
    for host in hosts:
        for result in neighbors['results']:
            if host_in_output(host, result['stdout'][0]):
                interfaces.append(str(result['item']))

    return interfaces


class FilterModule(object):
    def filters(self):
        """
        Associate the filter with a specific function
        :return: the filter-to-function association
        """
        return {
            'get_neighbor_port_channels': neighbor_port_channels,
        }
