from apiRequests import requestToApi

def getRequest(args) -> str:
    data = ""
    match args.getRequest:  # checking the user's get request
        case 'U' | 'urls':
            data = requestToApi('urls', callArgument=args.limit)  # in case it is a urls request
        case 'P' | 'payloads':
            data = requestToApi('payloads', callArgument=args.limit)  # in case it is a payload request
        case 'D' | 'download':
            if len(args.sha256) == 64:
                data = requestToApi('download', callArgument=args.sha256)
                with open("payload.zip", "wb") as zipfile:
                    zipfile.write(data)
                print('the download is done, the file is saved in the working directory')
            else:
                print('ERROR, sha256 must be 64 chars long')

    return data