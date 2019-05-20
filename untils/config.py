import os
import codecs
import configparser

file_path = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(file_path, "config.ini")
# print(configPath)

