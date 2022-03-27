from src.logger import logger

class parameters:
    def __init__(self, default):
        self._logger = logger()
        self._switches = {}
        self._parameters = {}
        self._default = default

    def register_parameter(self, key, function):
        self._parameters[key.lower()] = function

    def register_switch(self, key, action):
        self._switches[key.lower()] = action
    
    def parse(self, argv):
        argv_len = len(argv)
        i = 0
        while (i < argv_len):
            arg = argv[i]
            if len(arg) > 2 and arg.startswith('--'):
                key = arg[2:].lower()
                if key in self._switches:
                    self._switches[key]()
                else:
                    if (i + 1) < argv_len:
                        if key in self._parameters:
                            i = i + 1
                            self._parameters[key](argv[i])
                        else:
                            self._default(arg)
                    else:
                        self._default(arg)
            else:
                self._default(arg)
            i = i + 1