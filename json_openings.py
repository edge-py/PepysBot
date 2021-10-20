from bot_test import *
import json

ph_duck_list = []
ph_chick_list = []

with open(file = "ch_ph_paths.json") as chick_file:
    ph_chick_list = list(json.load(chick_file).values())

with open(file = "du_ph_paths.json") as duck_file:
    du_chick_list = list(json.load(duck_file).values())
