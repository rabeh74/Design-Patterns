from abc import ABC, abstractmethod

class Device(ABC):
    def __init__(self):
        self.volume = 0
        self.channel = 0

    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        self.volume = volume

    def get_channel(self):
        return self.channel

    def set_channel(self, channel):
        self.channel = channel

    def print_status(self):
        print("Volume: {} Channel: {}".format(self.volume, self.channel))

    def enable(self):
        pass
    def is_enabled(self):
        pass
    def disable(self):
        pass

class TV(Device):
    def enable(self):
        print("TV enabled")
    def is_enabled(self):
        print("TV enabled")
    def disable(self):
        print("TV disabled")

class Radio(Device):
    def enable(self):
        print("Radio enabled")
    def is_enabled(self):
        print("Radio enabled")
    def disable(self):
        print("Radio disabled")

class Remote:
    _device = None
    def __init__(self, device):
        self._device = device
    def toggle_power(self):
        if self._device.is_enabled():
            self._device.disable()
        else:
            self._device.enable()
    def volume_down(self):
        self._device.set_volume(self._device.get_volume() - 10)
    def volume_up(self):
        self._device.set_volume(self._device.get_volume() + 10)
    def channel_down(self):
        self._device.set_channel(self._device.get_channel() - 1)
    def channel_up(self):
        self._device.set_channel(self._device.get_channel() + 1)

class AdvancedRemote(Remote):
    def mute(self):
        self._device.set_volume(0)

def client_code(device):
    remote = Remote(device)
    remote.toggle_power()
    remote.volume_up()
    remote.volume_up()
    print("Volume: {}".format(device.get_volume()))
    remote.volume_down()
    print("Volume: {}".format(device.get_volume()))
    remote.channel_up()
    print("Channel: {}".format(device.get_channel()))
    remote.channel_down()
    print("Channel: {}".format(device.get_channel()))

    advanced_remote = AdvancedRemote(device)
    advanced_remote.mute()
    print("Volume: {}".format(device.get_volume()))

client_code(TV())
client_code(Radio())





