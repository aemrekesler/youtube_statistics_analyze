import pandas as pd

df = pd.read_csv("FRvideos.csv")

#Average likes and dislikes
likeAverage = df["likes"].mean().round()
dislikeAverage = df["dislikes"].mean().round()
#print(f"Like average: {likeAverage}\nDislike average: {dislikeAverage}")

#Most viewed video
result = df[(df["views"].max()) == df["views"]]["title"].iloc[0]
#print(result)

#Least viewed video
result = df[(df["views"].min()) == df["views"]]["title"].iloc[0]
#print(result)

#Top 10 most viewed videos
result = df.sort_values("views", ascending=False).head(10)[["title","views"]]
#print(result)

#Average likes in every category
result = df.groupby("category_id").mean().sort_values("likes")["likes"]
#print(result)

#Comments count in every category
result = df.groupby("category_id").sum().sort_values("comment_count",ascending=False)["comment_count"]
#print(result)   

#Numbers of videos in every category
result = df["category_id"].value_counts()
#print(result)

#Most popular videos (Like/Dislike Rate)
def likesDislikes(dataset):
    likesList = list(dataset["likes"])
    dislikesList = list(dataset["dislikes"])
    list_ = list(zip(likesList, dislikesList))
    rateList = []
    for like,dislike in list_:
        if(like+dislike) == 0:
            rateList.append(0)
        else:
            rateList.append(like/(like+dislike))
    return rateList    

df["likes_rate"] = likesDislikes(df)
print(df.sort_values("likes_rate",ascending=False)[["title","likes","dislikes","likes_rate"]])