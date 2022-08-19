from psutil import net_if_addrs, net_if_stats
import socket

class InterfaceCard():
    # Constants
    INETV4 = 2
    INETV6 = 10
    PACKET = 17

    # DataVars
    addrs = {}
    stats = {}

    def __init__(self, addrs, stats):
        self.addrs = addrs
        self.stats = stats
    def isup(self):
        return self.stats.isup or False
    def ipv4(self):
        for addr in self.addrs:
            if addr.family == self.INETV4:
                return addr
        return False
    def ipv6(self):
        for addr in self.addrs:
            if addr.family == self.INETV6:
                return addr
        return False


class Network():
    data = {}
    def __init__(self):
        addrs = net_if_addrs()
        stats = net_if_stats()
        for net, addresses in addrs.items():
            self.data[net] = InterfaceCard(addresses, stats[net])
    def default_route(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # doesn't even have to be reachable
            s.connect(('10.255.255.255', 1))
            return s.getsockname()[0]
        except Exception:
            return '127.0.0.1'
        finally:
            s.close()
        return False

# net = Network()