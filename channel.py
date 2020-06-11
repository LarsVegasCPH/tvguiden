from datetime import datetime
from typing import List

class Program():
    def __init__(self, name: str, start:datetime, stop:datetime, program_id:str, content:str):
        self.name = name
        self.start = start
        self.stop = stop
        self.id = program_id
        self.content = content
        self.duration = stop - start

    def __repr__(self):
        return self.name + "_" + f"{self.start.hour}" + f"_{self.stop.hour}"


class Channel:
    def __init__(self, channelname:str, channel_id:str):
        self.name = channelname
        self.id = channel_id

    def __repr__(self):
        return self.name.replace(" ","_").replace("'","")


class Listing:
    def __init__(self, programs:List[Program]):
        self.programs = programs


class ChannelListing:
    def __init__(self, channel:Channel, listing:Listing):
        self.channel = channel
        self.listing = listing
    def __repr__(self):
        return "Channel listing for {channel}"


class Listings:
    def __init__(self, listing:List[ChannelListing]):
        self.listing = listing