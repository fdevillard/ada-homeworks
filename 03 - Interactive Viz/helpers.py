def google_canton_code(search):                                                 
    import googlemaps                                                             

    try:                                                                          
        from keys import GOOGLE_KEY                                                 
    except ImportError:                                                           
        print("Google canton search failed: no key found.")
        return None

    gmaps = googlemaps.Client(key=GOOGLE_KEY)

    ans = googlemaps.geocoding.geocode(gmaps, search, region='CH')    
        
    try:                                                                          
        ans = [d['short_name'] for d in ans[0]['address_components']                
                               if 'administrative_area_level_1' in d['types']]      
    except IndexError:                                                            
        return None                                                                 

    if len(ans) > 0:                                                              
        return ans[0]                                                               
    else :                                                                        
        return None                                                                 
                                                                                
def geoname_canton_code(search):                                                
    import requests
    URL="http://api.geonames.org/searchJSON"
    
    try:
        from keys import GEONAMES_KEY
    except ImportError:
        print("GeoName canton search failed: no key found")
        return None
    
    response = requests.get(URL, params={'q': search, 'country':'CH', 'username':GEONAMES_KEY})
    
    try:
        json = response.json()
        ans = [canton['adminCode1'] for canton in json['geonames']]
    except (ValueError, KeyError):
        return None
    
    if len(ans) > 0:
        return ans[0]
    
    return None