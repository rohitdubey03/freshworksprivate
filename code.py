import threading
from threading import *
import time

d = {}


def create(entity, value, timeout=0):
    if entity in d:
        print("this entity already exists")
    else:
        if (entity.isalpha()):
            if len(d) < (1024 * 1020 * 1024) and value <= (16 * 1024 * 1024):
                if timeout == 0:
                    l = [value, timeout]
                else:
                    l = [value, time.time() + timeout]
                if len(entity) <= 32:
                    d[entity] = l
            else:
                print("Memory limit exceeded!! ")
        else:
            print("Invalid entity_name")


def read(entity):
    if entity not in d:
        print("does not exist")
    else:
        b = d[entity]
        if b[1] != 0:
            if time.time() < b[1]:
                stri = str(entity) + ":" + str(b[0])
                return stri
            else:
                print("time-to-live of", entity, "has expired")
        else:
            stri = str(entity) + ":" + str(b[0])
            return stri


def delete(entity):
    if entity not in d:
        print("does not exist")
    else:
        b = d[entity]
        if b[1] != 0:
            if time.time() < b[1]:
                print("entity is successfully deleted")
            else:
                print("time-to-live of", entity, "has expired")
        else:
            del d[entity]
            print("entity is successfully deleted")


def modify(entity, value):
    b = d[entity]
    if b[1] != 0:
        if time.time() < b[1]:
            if entity not in d:
                print("does not exist")
            else:
                l = []
                l.append(value)
                l.append(b[1])
                d[entity] = l
        else:
            print("time-to-live of", entity, "has expired")
    else:
        if entity not in d:
            print("does not exist")
        else:
            l = []
            l.append(value)
            l.append(b[1])
            d[entity] = l
