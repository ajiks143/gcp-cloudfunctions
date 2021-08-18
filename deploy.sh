BUCKET_NAME=$1

gcloud functions deploy gcs_file_metdata \
--runtime python38 \
--trigger-resource $BUCKET_NAME \
--trigger-event google.storage.object.finalize