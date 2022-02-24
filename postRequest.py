from apiRequests import requestToApi


def postRequest(args) -> str:
    data = ""
    match args.postRequest:
        case 'U' | 'url':  # a specific URL was queried, the URL was was used as a search variable
            if args.url != -1:
                data = requestToApi('url', callArgument=args.url)
            else:
                print('Please provide a URL to query, using the URL ID number is available as well.')

        case 'urlId':  # a specific URL was queried, the URL ID was was used as a search variable
            if args.urlId != -1:
                data = requestToApi('urlId', callArgument=args.urlId)
            else:
                print('Please provide a URL ID to query, using the URL is available as well.')

        case 'H' | 'host':  # querying a host, using its name as a searching variable
            if args.host != -1:
                data = requestToApi('host', callArgument=args.host)
            else:
                print('Please provide a valid host name for the query')

        case 'P' | 'payload':
            if args.payloadmd5 != -1:
                data = requestToApi('payload', md5=args.payloadmd5)
            elif args.payloadsha256 != -1:
                data = requestToApi('payload', payloadsha256=args.payloadsha256)
            else:
                print('Please enter a hash for the search, ether MD5 or SHA256 can be used for this search.')

        case 'T' | 'tag':
            if args.tag != -1:
                data = requestToApi('tag', callArgument=args.tag)
            else:
                print('Please enter a valid tag for the search')

        case 'S' | 'signature':
            if args.signature != -1:
                data = requestToApi('signature', callArgument=args.signature)
            else:
                print('Please provide a valid signature for the search')

    return data

