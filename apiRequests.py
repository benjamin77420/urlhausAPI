import requests
from typing import Optional

#sending the get request to the API for the recent additions to the URLhaus, limiting the amount of values returned is optional
def requestToApi(callType, callArgument: Optional = None, md5: Optional = None, payloadsha256: Optional = None) -> str:
    match callType: # all the variations of URLs that can be used to query the API
        case 'payloads': apiAddress = 'https://urlhaus-api.abuse.ch/v1/payloads/recent/'
        case 'urls': apiAddress = 'https://urlhaus-api.abuse.ch/v1/urls/recent/'
        case 'download': apiAddress = 'https://urlhaus-api.abuse.ch/v1/download/'
        case 'url': apiAddress = 'https://urlhaus-api.abuse.ch/v1/url/'
        case 'urlId': apiAddress = 'https://urlhaus-api.abuse.ch/v1/urlid/'
        case 'host': apiAddress = 'https://urlhaus-api.abuse.ch/v1/host/'
        case 'payload': apiAddress = 'https://urlhaus-api.abuse.ch/v1/payload/'
        case 'tag': apiAddress = 'https://urlhaus-api.abuse.ch/v1/tag/'
        case 'signature' : apiAddress = 'https://urlhaus-api.abuse.ch/v1/signature/'
    try:
        match callType:
            case 'payloads' | 'urls':# requests that may involve a limiter to the amount of data fetched
                if callArgument is not None and 0 < callArgument <= 1000:  # checking if the given limiter is in the valid range
                    response = requests.get(apiAddress + f"limit/{callArgument}/")
                    print(f'limit of amount received set to {callArgument}')
                else:  # no limiter was given, using the default API call
                    response = requests.get(apiAddress)

            case 'download': # if the user request to download a payload using a sha256 as payload ID
                response = requests.get(apiAddress + f'{callArgument}/')
                return response.content

            case 'url': # query a particular url for data
                response = requests.post(apiAddress, data={'url': f'{callArgument}'})

            case 'urlId': # query for url data, using the URL ID as a searching variable
                response = requests.post(apiAddress, data={'urlid': f'{callArgument}'})

            case 'host': # query the API, using the host name as a searching variable
                response = requests.post(apiAddress, data={'host': f'{callArgument}'})

            case 'payload': # querying the APi for a specific payload using its md5 or its sha256
                if md5 is not None:
                    response = requests.post(apiAddress, data={'md5_hash': f'{md5}'})
                elif payloadsha256 is not None:
                    response = requests.post(apiAddress, data={'sha256_hash': f'{payloadsha256}'})

            case 'tag':# querying the APi for a specific database entry using its tags
                response = requests.post(apiAddress, data={'tag': f'{callArgument}'})

            case 'signature':
                response = requests.post(apiAddress, data={'signature': f'{callArgument}'})

    except response.exceptions.HTTPError as errh: #catch HTTP errors and prints to the user
        print(errh)
    except response.exceptions.ConnectionError as errc: #catch connection errors and prints to the user
        print(errc)
    except response.exceptions.Timeout as errt: #catch timeout errors and prints to the user
        print(errt)
    except response.exceptions.RequestException as err:#catch request errors and prints to the user
        print(err)

    if response.status_code == 200:
        print(f'query passed, the query for all recent additions was OK, the request was {response.url}')
    elif response.status_code == 404:
        print(f'URL: {response.url}, was not found, check the URL')

    return response.text