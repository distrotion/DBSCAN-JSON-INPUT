# DBSCAN-JSON-INPUT 
gcloud builds submit --tag gcr.io/first-test-api-01/dbscan-deploy
gcloud run deploy --image gcr.io/first-test-api-01/dbscan-deploy

