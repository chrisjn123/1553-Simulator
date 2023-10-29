class Device:
    def __init__(self) -> None:
        pass

class RemoteTerminal(Device):
    def __init__(self) -> None:
        super().__init__()

class BusController(Device):
    def __init__(self) -> None:
        super().__init__()

class BusMonitor(Device):
    def __init__(self) -> None:
        super().__init__()

class BackupBusController(BusController):
    def __init__(self) -> None:
        super().__init__()
