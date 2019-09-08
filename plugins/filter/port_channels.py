#!/usr/bin/python

class FilterModule(object):

    def filters(self):
        return {
            'port_channels': self.port_channels
        }

    def port_channels(self, input_interfaces):
        ports = []
        for interface in input_interfaces:
            if 'port-channel' in str(interface).lower():
                ports.append(interface)
        return ports
