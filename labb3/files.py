import requests, json



class file_manager:
    def __init__(self):
        self.this_url = "http://www.omdbapi.com/?i=tt3896198&apikey=dc152a77"


    def search_def(self,serach_URL ):
        link = self.this_url + "s=" + serach_URL
        answered_req = requests.get(link)

        data_json = answered_req.json()
        
        if data_json["Response"] == True:
            result = data_json["Search"] 
            if int(data_json["totalResults"]) > 1:   
                for res in  range(len(result)):
                    print(f"{res+1}: {result[res]['Title']}")
                self.view_movie_info(result)
            elif int(data_json["totalResults"]) == 1:
                for data in data_json["Search"]:
                    print(data)
        
        else:
            print("No results is found")




    def view_movie_info(self,result):
        while True:

            index_search = input("-----Select your movie by index number: ")
            try:
                movie_url =  result[int(index_search) - 1]["imdbID"]
                request_resp = requests.get(self.this_url + "i=" + movie_url)
                data_responed = request_resp.json()
                print(json.dumps(data,index_search = 4))
                break
            except ValueError as value:
                print(value)
            except IndexError as index:
                print(index)

    def last_serached(self,searched):
        print(".....................")

        for index in range(len(searched)):
            print(f"{index+1}: {searched[index]}")
        
        while True:
            ask_search = input("-----Do you want to search for one of these agian?: y/n: ")

            if ask_search.lower() == "y":
                while True:
                    index_search = input("---select the search by index number: ")
                    try:
                        new_sear = searched[int(index_search) - 1]
                        self.search_def(new_sear)
                        break
                    except ValueError as value:
                        print(value)
                    except IndexError as index:
                        print(index)
            elif ask_search.lower() == "n":
                break
            else:
                print("wrong input try agian")

