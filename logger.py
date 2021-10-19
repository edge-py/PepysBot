from imports import *

logger = tb.logger

Path("testlogs").mkdir(parents=True, exist_ok=True)

path_file_counter = 1
while (Path('./testlogs/test' + str(path_file_counter) + '.log').exists() == True):
    path_file_counter += 1
lg.basicConfig(filename='./testlogs/test' + str(path_file_counter)+ '.log', level=lg.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
