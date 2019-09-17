#!/usr/bin/python
"""

"""


def neighbor_port_channels(neighbors, hosts):
    """

    """
    interfaces = []
    for host in hosts:
        for result in neighbors['results']:
            if host in result['stdout'][0]:
                interfaces.append(result['item'])

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

