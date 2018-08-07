import os, csv, re

def LoadProjects(filepath):
    with open(filepath, newline='') as csvfile:
        data = list(csv.reader(csvfile))
        return data

    return arr_projects

class ProjectName:
    self.RawName = ''
    self.Number = ''
    self.corridor = ''
    self.start = ''
    self.end = ''
    self.is_intersection = False
    def __init__(self, name, number):
        self.RawName = name
        self.Number = number

    def split_name(self):
        for char in ['&', ' and ', ' over ']:       #Check if intersection
            if self.RawName.find(char):
                self.is_intersection = True
                self.corridor = self.RawName.split(char, 1)[0].strip()
                self.start = self.RawName.split(char, 1)[1].strip()
                return
        for char in [',', ';']:         #find corrdior
            if self.RawName.find(char):
                self.corridor = self.RawName.split(char, 1)[0].strip()

