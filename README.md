# DBSCAN-JSON-INPUT 
/DBSCAN
- need skema  {
                "Uid" : "-",
                "Choice" : [-, -, -, -, -, -, -, -, -],
                "Result" : -,
                "Week" : -,
                "Skip" : -
            }
- methode POST
- the data will push to firebase realtime DB and then DBSCAN. the respon of POST is result

/DBSCAN_FB_DB
- need skema {}
- methode POST
- the respon of POST is all point of data in firebase

/DBSCAN_FB_DB_RESULT
- need skema {}
- methode POST
- the respon of POST is number of clusters and number of noise points

/setup
- need skema {
                "esp":0.30,
                "min_samples":30
            }
- methode POST
- setup esp and min_samples

/PUSH_DATA
- push data to firebase

/get_data
- get data to firebase