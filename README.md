<h1>Options and usage</h1>

usage: main.py [-h] [-G] [-P] [-V] [-L] [--url] [--sha256] [--urlId]
                  [--host] [--payloadmd5] [--payloadsha256] [--tag]
                  [--signature]

Hello, this program is meant to aid in basic and advanced analytics,
collecting and tracking and sharing of malware URLs, helping network
administrators and security analysts to protect their network and customers
from cyber threats.

options:  
  -h, --help               show this help message and exit  
  -G, --getRequest	       create a get request to the API  
  -P, --postRequest   	   create a post request to the API  
  -V, --version        	   show program's version number and exit  
  -L, --limit         		 Used to limit the number of entries received by the API
                       		 call, example "-L 3" OR "-limit 3"  
  --url                		 the url that the user wants to query  
  --sha256             	   the hash of the payload that you want to download  
  --urlId              		 the ID of the url that is queried  
  --host               		 the name of the queried host  
  --payloadmd5         	   the md5 hash of the payload that is queried  
  --payloadsha256      	   the sha256 hash of the payload that is queried  
  --tag                		 the tag of the database entry that was searched  
  --signature          	   the signature that will be used to query the API  

  
  
<h2>Querying options</h2>  
This tool gives the user the full access to the API of URLhaus, we will go through all the possibilities that are available to the user.

<h3>Query recent URLs</h3>  
Querying for the most recent additions that were made in the past 3 days, this call is restricted to 1000 entries (image 1).
There is the ability to cap the number of entries that will be returned by this call (image 2)  

![image](https://github.com/benjamin77420/urlhausAPI/assets/66326085/466eb666-4b84-4a57-827f-5c4efb1e2fe0)  
Image 1: the use of the U and urls flags, the two variations can be seen.

The user can use the -G flag to send a GET request or he can user the –getRequest flag as well, they serve the same purpose.
As mentioned above the U value that is passed to -G or –getRequest has two variants, the user can use ether U or urls to query for the recently added URLs.
![image](https://github.com/benjamin77420/urlhausAPI/assets/66326085/0fadc1b6-02a8-4cf1-a91f-00fa12c18d28)  
Image 2: the use of limits on the number of entries received from the AIP call.

There is the option to limit the amount of database entries that are retrieved from the query, this is possible by using the -L or –limit flag, the value of the flag must be an integer and its value must be between 1 and 1000 (max entries that can be fetched).




<h3>Query recent payloads</h3>
To retrieve a list of recent payloads (recent payloads seen by URLhaus), the API will return a list of recent payloads from the past 3 days, this call is restricted to 1000 entries (image 3).
There is the ability to cap the number of entries that will be returned by this call (image 4).

![image](https://github.com/benjamin77420/urlhausAPI/assets/66326085/959091cf-18a8-4285-a140-80606dd40344)  
Image 3: the use of the P and payloads flags, the two variations can be seen.

The user can use the -G flag to send a GET request or he can user the –getRequest flag as well, they serve the same purpose.
As mentioned above the P value that is passed to -G or –getRequest has two variants, the user can use ether P or payloads to query for the recently added URLs.  

![image](https://github.com/benjamin77420/urlhausAPI/assets/66326085/44b10320-3bd0-435e-9a42-dddea7e08018)  
Image 4: the use of limits on the number of entries received from the AIP call.

There is the option to limit the amount of database entries that are retrieved from the query, this is possible by using the -L or –limit flag, the value of the flag must be an integer and its value must be between 1 and 1000 (max entries that can be fetched).








<h3>Query URL information</h3>
To retrieve information about an URL, the URL must be supplied in the commend line (image 5), there is the possibility to use the URL ID if it is known instead of the URL (image 6).
In the case that a url will not be provided the user will be prompted with a message saying that a url must be provided for the search, or if the –url was used but not supplied (image 7).

![image](https://github.com/benjamin77420/urlhausAPI/assets/66326085/c99c247f-8ce5-4fe3-bf65-c4d477580259)  
Image 5: the use of the U and url flags, the two variations can be seen.

This kind of query uses the –url flag, it must include a valid url so the search will be successful, by valid we mean a url that exists in the records of URLhaus and not an empty string, empty strings will be handled, and a message will be shown to the user.

![image](https://github.com/benjamin77420/urlhausAPI/assets/66326085/d3609003-8306-4a2b-98bc-584468dafb10)   
Image 6: the use of the urlId flag being passed with the matching URLs ID.
This kind of query uses the variable urlId as a parameter that will be passed to the -P flag, this will make a post request to the API searching for the URL ID that will be passed by the user in the –urlId flag that will follow.  

![image](https://github.com/benjamin77420/urlhausAPI/assets/66326085/c07733c0-0bad-41f5-81a0-0ca3ebca70a3)  
Image 7: the user being notified that ether the –url flag was empty or not used at all.





<h2>Query host information</h2>
To retrieve information about a host, the host’s name must be supplied in the command line (image 8).

![image](https://github.com/benjamin77420/urlhausAPI/assets/66326085/7dbb112e-52e1-4c16-b707-64bb4a39f566)  
Image 8: the use of the H and host flags, the two variations can be seen.

This kind of query will use the –host flag to search the URLhaus database, it will retrieve every entry that has the value passed in the –host flag as its value, the use of H or host as the value passed to the -P flag server the same purpose.

<h3>Query payload information</h3>
To retrieve information about a payload (malware sample) that URLhaus has retrieved, there are two types of data types that can be passed to ID the payload that the user wants to search, the 1st is a MD5 hash, the 2nd is a SHA256, one of these data types must be givens to send a request to the API (image 9), if the user will not supply ether one of the options given to him a message saying that a hash is needed will be shown (image 10).

![image](https://github.com/benjamin77420/urlhausAPI/assets/66326085/99d31e1c-c4dd-4aeb-895a-5712f34525d7)  
Image 9: the use of the P and payload flags, the two variations can be seen, as well the use	   of both MD5 hash and SHA256 for the search vector.

![image](https://github.com/benjamin77420/urlhausAPI/assets/66326085/d84ac9e8-0b92-46a2-a8f5-bdc59c59a6a9)  
Image 10: a message being shown to the user asking for a hash as a input for the search.

<h3>Query tag information</h3>
To retrieve information about a tag, there are tags that are associated with each entry on the database, the user needs to enter a value to the –tag flag, this will filter only the entries that have the tag that was given by the user (image 11).

![image](https://github.com/benjamin77420/urlhausAPI/assets/66326085/f4eaffad-0ff1-4fbb-ae92-6428996afc28)  
Image 11: the use of the P and payload flags, the two variations can be seen.



<h3>Query signature information</h3>
URLhaus tries to identify the malware family of a payload (malware sample) served by malware URLs.
Unlink tags, the signature is something that the reporter of the malware URL cannot influence. To retrieve information using this method the user will need to pass the signature as value to the – signature flag (image 12).

![image](https://github.com/benjamin77420/urlhausAPI/assets/66326085/36897b99-ab6e-4950-8b34-5ef69e976786)  
Image 12: the use of the P and payload flags, the two variations can be seen.

<h2>Download malware</h2>  

There is the ability to download a zip file that contains the wanted malware, the user must supply the SHA256 hash in the –sha256 flag for the get request to be successful, the zip containing the malware will be called payload.zip and will not be protected by any kind of password, please act with caution (image 13).
![image](https://github.com/benjamin77420/urlhausAPI/assets/66326085/fbcf1995-2d93-4e40-85de-f4a88260adc0)  
Image 13: the zip file downloaded and containing the wanted malware.


Data manipulation and filtering
There are several options that we are offering the user to focus its search and filter specifically what the user needs, ether using the key to the value or using regular expressions in order to filter them out.

<h3>Fetch</h3>

We gave the user the ability to mark the kyes that he wants to collect there value and the program will filter through all the response and will detect when it sees key that the user stated that he is interested in, then it will append it to a list of all the other matching values, at the end of the matching it will be sent back to the main program as data (image 14).

![image](https://github.com/benjamin77420/urlhausAPI/assets/66326085/4a6ca412-fc8b-4d43-9f9d-66d633a2b02d)  
Image 14: the program in debug, showing that only the URLs were taken from the full API response.

<h3>Output to file</h3>  

We gave the user the ability to export the results that he received to a file, the types that are supported at the moment are, json, xlsx, CVS, html, xml, to choose the file type just enter the name of the file with the wanted extension attached to it for example, test.xml, check.json, etc. (image 15)  
![image](https://github.com/benjamin77420/urlhausAPI/assets/66326085/8040934b-e3c3-4d2e-a6cb-e5fc05b0191f)  
Image 15: the result being outputted as a json file the current active directory

<h3>Regex filtering</h3>  

We can filter all the values that are received by the API with regular expression as well, this comes as a combination of two flags the --fetch flag and the –regex (OR -R) flag, both are needed to create a regular expression filtering (image 16).
![image](https://github.com/benjamin77420/urlhausAPI/assets/66326085/f3c9c67d-c1a5-47ca-ac05-057597820a28)  
Image 16: the result of the use of regex and fetch to get a specific pattern on the URLs.
