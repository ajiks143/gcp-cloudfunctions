# Command line argument Storage bucket to integrate with
BUCKET_NAME=$1

# CLI command to deploy Python Cloud function
gcloud functions deploy gcs_file_metdata \
--runtime python38 \
--trigger-resource $BUCKET_NAME \
--trigger-event google.storage.object.finalize
