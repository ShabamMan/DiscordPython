
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


# so far I have tried things like this
for item in filters.keys():
    df.loc[(df[filters[item].keys()].isin(filters[item].values()).all(axis=1)),'Type of Day'] = item




df.to_csv("C:\\Users\\mrber\\Desktop\\test.csv")