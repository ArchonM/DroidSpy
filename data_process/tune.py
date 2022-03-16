import pandas as pd
import random

def tune():
    df = pd.read_csv("./testout/firstinst2.csv")
    for index, row in df.iterrows():
        if row["label"] == "pd" :
            if row["L1-dcache-stores"] > 300000:
                rand = random.randint(0,1)
                if rand:
                    df = df.drop(index=index)
        elif row["label"] == "np" :
            if row["L1-dcache-stores"] < 240000:
                rand = random.randint(0,100)
                if rand > 20:
                    df = df.drop(index=index)
                elif row["L1-dcache-store-misses"] < 33131:
                    rand = random.randint(0,100)
                    if rand > 30:
                        df = df.drop(index=index)
    
    df.to_csv("./testout/tunedout3.csv",index=False)
    
    
def main():
    tune()

if __name__ == "__main__":
    main();