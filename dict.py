meme_dict = {
            "CRINGE": "Something very strange or embarrassing",
            "LOL": "A common response to something funny",
            "ROFL": "typically used to respond for a great joke",
            "SHEESH": "used to express disbelief or exasperation",
            "CREEPY": "causing an unpleasant feeling of fear or unease",
            "AGGRO": "aggressive, violent behavior",
            }
            
for i in range(5):
    word = input("type the words that you dont understand(use capital letters)")
    
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("no word in the dictionary")
