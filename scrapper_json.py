import requests
  
subreddit = 'wallstreetbets'
limit = 1
timeframe = 'all'
listing = 'hot'
  
def get_reddit(subreddit,listing,limit,timeframe):
    try:
        base_url = f'https://www.reddit.com/r/{subreddit}/{listing}.json?limit={limit}&t={timeframe}'
        request = requests.get(base_url, headers = {'User-agent': 'yourbot'})
    except:
        print('An Error Occured')
    return request.json()
  
r = get_reddit(subreddit, listing, limit, timeframe)

list_of_the_values = []
for child in r['data']['children']:
    to_extract = ['author', 'created_utc', 'selftext', 'ups'] 
    val = {}
    for e in to_extract:    
        # print(f"{e}: {child['data'][e]}")
        val[e] = child['data'][e]
   
    json_val = {
          "author": val['author'],
          "date": val['created_utc'],
          "content": val['selftext'], 
          "upvotes": val['ups']
        }
   
    list_of_the_values.append(json_val)
print(list_of_the_values)
# [print(x) for x in list_of_the_values]
