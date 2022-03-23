import requests

from recursos.clave import clave

GOOGLE_API_KEY = clave

def extract_distance(coord1,coord2):
    #lat, lng = None, None
    #$url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=".$lat1.",".$long1."&destinations=".$lat2.",".$long2."&mode=driving&language=pl-PL";
    api_key = GOOGLE_API_KEY
    base_url = "https://maps.googleapis.com/maps/api/distancematrix/json"
    endpoint = f"{base_url}?origins={coord1}&destinations={coord2}&mode=driving&key={api_key}"
    # see how our endpoint includes our API key? Yes this is yet another reason to restrict the key
    r = requests.get(endpoint)
    if r.status_code not in range(200, 299):
        return None, None
    try:
        '''
        This try block incase any of our inputs are invalid. This is done instead
        of actually writing out handlers for all kinds of responses.
        '''
        print(r.json())
        results = r.json()['rows'][0]
        distance = results['elements'][0]['duration']['text']
        #lng = results['geometry']['location']['lng']
    except:
        pass
    return distance