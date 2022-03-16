from curses import raw
from doctest import OutputChecker
from operator import index
import os
import shutil
from unittest import result
import numpy as np
import pandas as pd
from collections import Counter

def raw_parse():
    dfs = []
    # for subdir, dirs, files in os.walk("../output/"):
    for subdir, dirs, files in os.walk("./output/test2/"):
        for file in files:
            raw_file = subdir+file
            print(raw_file)
            if raw_file.endswith("np"):
                dfs.append(single_parse(subdir+file, "./testout/"+file+".csv", "np"))
            elif raw_file.endswith("pd"):
                dfs.append(single_parse(subdir+file, "./testout/"+file+".csv", "pd"))
            else:
                print("Fuck! We are having problem")
            # np_raw_file = "cache-misses-"+str(i)+"-np"
            # pd_raw_file = "cache-misses-"+str(i)+"-pd"
            # single_parse("../output/"+np_raw_file, "test_out_np"+str(i)+".csv", "np")
            # single_parse("../output/"+pd_raw_file, "test_out_pd"+str(i)+".csv", "pd")
    result = pd.concat(dfs, axis=0)
    # result.to_csv("./testout/result.csv", index=False)
    result.to_csv("./testout/firstinst2.csv", index=False)
    
    

def single_parse(raw_file, parsed_file, label):
    events = []
    with open(raw_file, 'r') as f:
        
        buf = f.readline()
        while buf:
            buf = buf.strip()
            buf = buf.replace(',', '')
            if buf.split(' ')[0].isdigit():
                while buf.split(' ')[0].isdigit():
                    events.append(buf.split()[1])
                    buf = f.readline()
                    buf = buf.strip()
                    buf = buf.replace(',', '')
                break
            buf = f.readline()
            
    dict_list = []
    with open(raw_file, 'r') as f:
        buf = f.readline()
        while buf:
            buf = buf.strip()
            buf = buf.replace(',', '')
            if buf.split(' ')[0].isdigit():
                dict_tmp = {}
                while buf.split(' ')[0].isdigit():
                    dict_tmp[buf.split()[1]] = buf.split()[0]
                    buf = f.readline()
                    buf = buf.strip()
                    buf = buf.replace(',', '')
                dict_list.append(dict_tmp)
            buf = f.readline()
    
    # temp = int(dict_list[-1]["cache-misses"]) - int(dict_list[0]["cache-misses"])
    # temp = int(dict_list[-1]["cache-misses"])
    # df = pd.DataFrame(data={"cache-misses":[temp], "label":[label]})
    attr_selector = 0
    df = pd.DataFrame(data={"cache-misses":[dict_list[attr_selector]["cache-misses"]], "cache-references": [dict_list[attr_selector]["cache-references"]],
                            "L1-dcache-load-misses": [dict_list[attr_selector]["L1-dcache-load-misses"]], "L1-dcache-loads": [dict_list[attr_selector]["L1-dcache-loads"]],
                            "L1-dcache-store-misses": [dict_list[attr_selector]["L1-dcache-store-misses"]], "L1-dcache-stores": [int(dict_list[attr_selector]["L1-dcache-stores"])],
                            "label":[label]})
    return df
    # df.to_csv(parsed_file, index=False);
    
def test():
    events = []
    with open("../output/cache-misses-0-np", 'r') as f:
        
        buf = f.readline()
        while buf:
            buf = buf.strip()
            buf = buf.replace(',', '')
            if buf.split(' ')[0].isdigit():
                while buf.split(' ')[0].isdigit():
                    events.append(buf.split()[1])
                    buf = f.readline()
                    buf = buf.strip()
                    buf = buf.replace(',', '')
                break
            buf = f.readline()
            
    dict_list = []
    with open("../output/cache-misses-0-np", 'r') as f:
        buf = f.readline()
        while buf:
            buf = buf.strip()
            buf = buf.replace(',', '')
            if buf.split(' ')[0].isdigit():
                dict_tmp = {}
                while buf.split(' ')[0].isdigit():
                    dict_tmp[buf.split()[1]] = buf.split()[0]
                    buf = f.readline()
                    buf = buf.strip()
                    buf = buf.replace(',', '')
                dict_list.append(dict_tmp)
            buf = f.readline()
    print(dict_list)
    print(events)
    # temp = int(dict_list[-1]["cache-misses"]) - int(dict_list[0]["cache-misses"])
    temp = int(dict_list[0]["cache-misses"])
    
    
    # print(temp)
    df = pd.DataFrame(data={"cache-misses":[dict_list[0]["cache-misses"]], "cache-references": [dict_list[0]["cache-references"]],
                            "L1-dcache-load-misses": [dict_list[0]["L1-dcache-load-misses"]], "L1-dcache-loads": [dict_list[0]["L1-dcache-loads"]],
                            "L1-dcache-store-misses": [dict_list[0]["L1-dcache-store-misses"]], "L1-dcache-stores": [dict_list[0]["L1-dcache-stores"]],
                            "label":["np"]})
    df.to_csv("testout1.csv", index=False)
    
def main():
    raw_parse();
    # test();
    

if __name__ == "__main__":
    main();