# Text to Speech Demo

This demo uses Google Text to Speech API to turn input text in `main.py` into an `mp3` file. 

After you have the appropriate GCP Project and Authentication, run the following:

```
make audio
```

You can update `main.py` with different text and voice parameters.

## GCP Requirements

You need to to sign-in to GCP, create project or use existing, connect billing, and enable the API for text to speech. You can do all of this by following the instructions below:

`make shell` will give you shell in a docker container with `gcloud` installed.

Create a service account to start using text to speech with gcp:

```
GCP_SERVICE_USER=foo
GCP_PROJ=bar
GCP_KEY_FILENAME=text2speechkey

gcloud init
gcloud iam service-accounts create ${GCP_SERVICE_USER}
gcloud projects add-iam-policy-binding ${GCP_PROJ} --member="serviceAccount:${GCP_SERVICE_USER}@${GCP_PROJ}.iam.gserviceaccount.com" --role="roles/owner"
gcloud iam service-accounts keys create ${GCP_KEY_FILENAME}.json --iam-account=${GCP_SERVICE_USER}@${GCP_PROJ}.iam.gserviceaccount.com
```

This repo expects you to create `text2speechkey.json` (which should happen when running the above commands).
