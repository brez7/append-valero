browser-sync start --proxy "localhost:5000" --files "static/**/*, templates/**/*"



Build Docker Image and Deploy to Cloud Run:

Login to gcloud:
gcloud auth login

Set the project: 
gcloud config set project upbeat-button-265722

Build the Docker image: 
docker build -t gcr.io/upbeat-button-265722/valero-new .

Test run the app: 
docker run -p 5000:5000 -e PORT=5000 gcr.io/upbeat-button-265722/valero-new:latest

Push the Docker image to Cloud Run: 
docker push gcr.io/upbeat-button-265722/valero-new

Deploy the image to Cloud Run
gcloud run deploy valero-new --image gcr.io/upbeat-button-265722/valero-new --platform managed --region us-central1 --allow-unauthenticated

Live Site: 
https://valero-new-fvmy7faymq-uc.a.run.app/

docker build -t gcr.io/upbeat-button-265722/valero-new .
docker run -p 8080:8080 -e PORT=8080 gcr.io/upbeat-button-265722/valero-new:latest
docker push gcr.io/upbeat-button-265722/valero-new
gcloud run deploy valero-new --image gcr.io/upbeat-button-265722/valero-new --platform managed --region us-central1 --allow-unauthenticated