#!/usr/bin/env python3
''' My first python play_list project '''
# Basic Song Play list using linklist

class Song:
    def __init__(self, title, artist, duration):
            self.title = title
            self.artist = artist
            self.duration = duration

class Node:
    def __init__(self, song, next=None):
        self.song = song
        self.next = next

