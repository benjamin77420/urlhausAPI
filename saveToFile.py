import pandas

def save(data, fineName):
    if data is not None:
        try:
            dataframe = pandas.DataFrame.from_dict(data, orient='index')
            dataframe = dataframe[1]
        except:
            dataframe = pandas.DataFrame.from_dict(data, orient='index')
            dataframe = dataframe[0]

        filetype = fineName.split('.')
        match filetype[-1]:#get the rest of the string after the last occurrence of the char '.' (the file type)
            case 'json':dataframe.to_json(fineName)
            case 'xlsx':dataframe.to_excel(fineName)
            case 'cvs' :dataframe.to_csv(fineName)
            case 'html':dataframe.to_html(fineName)
            case 'xml' :dataframe.to_xml(fineName)
            case _: print('was not able to output to file, please check the file extension that was given')
    else:
        print("There is no data to save to the file")