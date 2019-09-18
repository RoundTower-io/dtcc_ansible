#!/usr/bin/python
"""

"""
import pprint


def host_in_output(host, output):
    """

    """
    for line in output.split('\n'):
        #print("line: " + line)
        if str(host).lower() in str(line).lower():
            return True
    
    return False 

def neighbor_port_channels(neighbors, hosts):
    """

    """
    interfaces = []
    for host in hosts:
#        print("host: " + host)
#        pprint.pprint(neighbors)
        for result in neighbors['results']:
#            print('stdout:')
#            pprint.pprint(result['stdout'][0])
            if host_in_output(host, result['stdout'][0]):
#                print("appending: " + str(result['item']))
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

