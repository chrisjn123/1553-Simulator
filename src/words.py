''' Defines the types of words that the protocol uses. '''
class CommandWord:
    def __init__(self, remote: int, transmit: bool, sub_addr_mode: int,
                 dataword_code: int) -> None:
        self.data = [0] * 20
        self.data[0] = [1]      # Sync is [0:3] and is 1, 0, 0
                                # No need to make a method for this...
        
        self.pack_remote(remote)
        self.pack_t_r(transmit)
        self.pack_subaddress_mode(sub_addr_mode)
        self.pack_dataword_mode_code(dataword_code)
        
        self.generate_partity()

    def pack_remote(self, value: int) -> None:
        ''' Packs the remote terminal number into the dataword. '''
        binary_str = format(value, '05b')
        self._packing_helper(3, binary_str)
    
    def pack_t_r(self, value: bool) -> None:
        if value:
            self.data[8] = 1
    
    def pack_subaddress_mode(self, value: int) -> None:
        binary_str = format(value, '05b')
        self._packing_helper(9, binary_str)

    def pack_dataword_mode_code(self, value: int) -> None:
        binary_str = format(value, '05b')
        self._packing_helper(14, binary_str)
    
    def _packing_helper(self, index: int, string) -> None:
        for i, val in enumerate(string):
            self.data[i + index] = int(val)
    
    def generate_partity(self) -> None:
        pass

    def send(self, bus):
        bus.add(self.data)