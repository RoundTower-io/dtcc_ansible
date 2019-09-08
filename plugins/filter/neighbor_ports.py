#!/usr/bin/python
import yaml
class FilterModule(object):
    def filters(self):
        return {
            'neighbor_ports': self.host_to_ports,
        }

    def host_to_ports(self, neighbors, host):
        ports = []
        for ndx in neighbors["cdp"]["index"]:
            if str(host).lower() in str(neighbors["cdp"]["index"][ndx]["device_id"]).lower():
                # print(neighbors["cdp"]["index"][ndx]["local_interface"])
                ports.append(neighbors["cdp"]["index"][ndx]["local_interface"])
        return ports

