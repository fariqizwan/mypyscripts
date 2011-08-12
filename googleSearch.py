import json,urllib

def showsome(searchtext):
	query = urllib.urlencode({'q':searchtext})
     	url = 'http://ajax.googleapis.com/ajax/services/search/video?v=1.0&%s' % query
     	search_response = urllib.urlopen(url)
     	search_results = search_response.read()
     	results = json.loads(search_results)
     	data = results['responseData']
     	print 'Total results: %s' % data['cursor']['estimatedResultCount']
     	hits = data['results']
     	print 'Top %d hits:' % len(hits)
     	for h in hits:
             print ' ',h['title']
     	print 'For more results, see %s' % data['cursor']['moreResultsUrl']
 
showsome('test')
