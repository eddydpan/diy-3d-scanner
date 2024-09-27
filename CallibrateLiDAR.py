import pandas as pd

inp = ""
df = pd.DataFrame(columns=['actual (cm)', 'sensor value'])
switch = 0
actual = ""
recorded = ""
while inp != "done":
    
    if switch % 2 == 0:
        if actual != "" and recorded != "":
            df.loc[len(df)] = [actual, recorded]
            if inp == "done":
                break
        inp = input("Actual value: ") 
        actual = inp
    else:
        inp = input("Recorded value: ")
        recorded = inp
    switch = switch + 1
# print(df)
df.to_csv("calibration_data.csv")