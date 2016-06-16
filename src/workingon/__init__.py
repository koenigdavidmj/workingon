import yaml

class Device(object):
    def __init__(self, host):
        self.host = host
        self.user = None
        self.providers = []

    @classmethod
    def from_yaml(cls, node):
        rv = cls(node['host'])
        rv.providers.extend(node.get('providers', []))
        return rv

class Group(object):
    def __init__(self, members):
        self.members = members

class FileHandler(object):
    def __init__(self, pattern, target):
        self.pattern = pattern
        self.target = target
        self.script = None

    @classmethod
    def from_yaml(cls, node):
        rv = cls(node['pattern'], node['target'])
        rv.script = node.get('script')
        return rv

class State(object):
    def __init__(self):
        self.devices = {}
        self.groups = {}
        self.file_handlers = []

    @classmethod
    def load(cls, stream):
        rv = cls()
        data = yaml.safe_load(stream)

        for device in data.get('devices', []):
            rv.devices[device['name']] = Device.from_yaml(device)

        for name, members in data.get('groups', {}).iteritems():
            member_objs = {}
            for member in members:
                member_objs[member] = rv.devices[member]
            rv.groups[name] = Group(member_objs)

        rv.file_handlers.extend(
            map(FileHandler.from_yaml, data.get('files', [])))

        return rv

