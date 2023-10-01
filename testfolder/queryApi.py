from testfolder.apiCall import ApiCall
from testfolder.writeToFile import WriteToFile

def queryApi(argv):
    api_key = "Apv8O5vFyn0Mb4I7LC0meXS1FZ05Xz6C"
    api = f"https://api.giphy.com/v1/gifs/search"
    limit = 5
    query = "code"

    # extract query
    if len(argv) == 3:
        query = argv[2]
    # elif len(sys.argv) == 3:
    #     query = sys.argv[1]
    #     limit = sys.argv[2]

    data = ApiCall(api, {
        "api_key":api_key,
        "limit":limit,
        "q":query
    })
    WriteToFile(data.mapped_data,query)

if __name__ ==  '__main__':
    queryApi([])