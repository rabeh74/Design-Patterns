"""
Proxy is a structural design pattern that lets you provide a substitute or placeholder for another object.
A proxy controls access to the original object, allowing you to perform something either before or after the request gets through to the original object.
used for lazy initialization, caching, controlling the access, logging, etc.
"""

from abc import ABC, abstractmethod

class ThirdPartyYouTubeLib(ABC):
    @abstractmethod
    def listVideos(self):
        pass
    @abstractmethod
    def getVideoInfo(self, id):
        pass
    @abstractmethod
    def downloadVideo(self, id):
        pass
class ThirdPartyYouTubeClass(ThirdPartyYouTubeLib):
    def listVideos(self):
        print("listVideos")
    def getVideoInfo(self, id):
        print("getVideoInfo")
    def downloadVideo(self, id):
        print("download")

class CachedYouTubeClass(ThirdPartyYouTubeLib):
    def __init__(self):
        self._service = ThirdPartyYouTubeClass()
        self._listCache = {}
        self._videoCache = {}
        self._downloadCache = {}
    def listVideos(self):
        if "list" not in self._listCache:
            self._listCache["list"] = self._service.listVideos()
        return self._listCache["list"]
    def getVideoInfo(self, id):
        if id not in self._videoCache:
            self._videoCache[id] = self._service.getVideoInfo(id)
        return self._videoCache[id]
    def downloadVideo(self, id):
        if id not in self._downloadCache:
            self._downloadCache[id] = self._service.downloadVideo(id)
        return self._downloadCache[id]

class YouTubeManager:
    def __init__(self, service):
        self._service = service
    def renderVideoPage(self, id):
        info = self._service.getVideoInfo(id)
        print("renderVideoPage")
    def renderListPanel(self):
        list = self._service.listVideos()
        print("renderListPanel")
    def reactOnUserInput(self):
        self.renderListPanel()
        self.renderVideoPage("some_id")

service = CachedYouTubeClass()
manager = YouTubeManager(service)
manager.reactOnUserInput()
