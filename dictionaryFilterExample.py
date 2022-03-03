import pandas as pd
filters = {
    "Happy": {
        "Sky Color" : ["blue"],
        "Time Of Day" : ["Noon","Twilight"],
        "Weather" : ["Clear"]
    },
    "Terrible": {
        "Sky Color" : ["Red"],
        "Time Of Day" : ["Night"],
        "Weather" : ["Thunder"]
    },
    "Okay": {
        "Sky Color" : ["Grey"],
        "Time Of Day" : ["Twilight"],
        "Weather" : ["Overcast"]
    }
}
df = pd.DataFrame.from_dict({
    "Sky Color" : ["blue","blue","Red","Grey","blue"],
    "Time Of Day" : ["Noon","Noon","Night","Twilight","Twilight"],
    "Weather" : ["Clear","Thunder","Thunder","Overcast","Clear"]
    })

for row in df.itertuples():
    for key in filters:
        for i, filt in enumerate(filters[key]):
            if row[i+1] not in filters[key][filt]:
                break
        else:
            df.at[row.Index, "Type of Day"] = key

df["Type of Day"] = df["Type of Day"].fillna("")
print(df)