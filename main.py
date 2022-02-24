import argparse
import json
from saveToFile import save
from typing import Optional
from typing import Sequence
from extract import json_extract
from postRequest import postRequest
from getRequest import getRequest


#TODO: OPTIONAL -> gather statistics
#TODO: ASAP -> pars the HTML to get the javascript and check for anomalies

def main(argv: Optional[Sequence[str]] = None):
    # adding the program's name and description
    parser = argparse.ArgumentParser(prog="URLhausAPI",
                                     description="Hello, this program is meant to aid in basic and advanced analytics, "
                                                "collecting and tracking and sharing of malware URLs, "
                                                "helping network administrators and security analysts to protect their "
                                                "network and customers from cyber threats.",
                                     epilog="the fallowing libraries are needed: requests, pandas, argparse, typing")

    # creating a get request to the API
    parser.add_argument('-G', '--getRequest', metavar="", choices=['U', 'urls', 'P', 'payloads', 'D', 'download'],
                        help='create a get request to the API')

    # create a post request to the API
    parser.add_argument('-P', '--postRequest', metavar="",
                        choices=['U', 'url', 'urlId', 'H', 'host', 'T', 'tag', 'S', 'signature', 'P', 'payload'],
                        help='create a post request to the API')

    # Adding the current version of the program
    parser.add_argument('-V', '--version', action='version', version='%(prog)s beta')

    # Adding the ability to limit the amount of entries received by the API call
    parser.add_argument('-L', '--limit', metavar="", type=int, help='Used to limit the amount of entries received by the API call, example \"-L 3\" OR \"-limit 3\"', default=-1)

    # adding the ability to query a single url
    parser.add_argument('--url', default=-1, metavar="", help='the url that the user wants to query')

    # get the hash that will be passed to the download request
    parser.add_argument('--sha256', metavar="", default=-1, help='the hash of the payload that you want to download')

    # adding the ability to query a url by its ID
    parser.add_argument('--urlId', metavar="", default=-1, help='the ID of the url that is queried')

    # adding the ability to query a host
    parser.add_argument('--host', metavar="", default=-1, help='the name of the queried host')

    # adding the ability to query a payload, using the md5_hash or the sha256_hash
    parser.add_argument('--payloadmd5', metavar="", default=-1, help='the md5 hash of the payload that is queried')

    # adding the ability to query a payload, using the md5_hash or the sha256_hash
    parser.add_argument('--payloadsha256', metavar="", default=-1, help='the sha256 hash of the payload that is queried')

    # adding the ability to query the API using a tag
    parser.add_argument('--tag', metavar='', default=-1, help='the tag of the database entry that was searched')

    # adding the ability to query the API using a signature
    parser.add_argument('--signature', metavar='', default=-1, help='the signature that will be used to query the API')

    # adding the ability to filter data that is given by names of Keys from the key value pairs
    parser.add_argument('--fetch', metavar="", nargs='+', default=[], help='these are the keys of the values that you want to retrieve from the API call')

    # adding the ability to save the data to a file
    parser.add_argument('-O', '--output', metavar="", default=None, help='the file name and the type that you want to give to the output file, can be only json, xlsx, cvs, html, xml')

    # adding regex filtering for the filtering arsenal
    parser.add_argument('-R', '--regex', metavar='', default=None, help='the regex expression that will be used in the filtering process')

    #pars the given args to a list of variables
    args = parser.parse_args(argv)

    if args.getRequest is not None:# a get request was issued
        data = getRequest(args)
    elif args.postRequest is not None:# a post request was issued
        data = postRequest(args)

    try:
        data = json.loads(data)

        if len(args.fetch) != 0 :# fetching the values of the keys that were given
            data = json_extract(data, args.fetch, regex=args.regex)

        if args.output is not None:# saving to a file the data that was collected
            save(data, args.output)

    except Exception as e:
        print(e)



if __name__ == '__main__':
    exit(main('-P U --url https://klapalevanda.com/rtptaleduloovmo/-rnmpbrrhei-ereqinreqsautheoerumnetsunddatepu  -O urlMatch.json'.split()))