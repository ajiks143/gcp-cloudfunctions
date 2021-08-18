from google.cloud import datastore

# Instantiates a client
datastore_client = datastore.Client()

# The kind for the new entity
kind = "file_metdata"

def gcs_file_metdata(event, context):
    """Background Cloud Function to be triggered by Cloud Storage.
       This generic function write the file metadata to Cloud Datastore when the file is uploaded to Storage.

    Args:
        event (dict):  The dictionary with data specific to this type of event.
                       The `data` field contains a description of the event in
                       the Cloud Storage `object` format described here:
                       https://cloud.google.com/storage/docs/json_api/v1/objects#resource
        context (google.cloud.functions.Context): Metadata of triggering event.
    Returns:
        None; the output is written to Stackdriver Logging
    """

    # The name/ID for the new entity
    ID = context.event_id
    
    # The Cloud Datastore key for the new entity
    metdata_key = datastore_client.key(kind, ID)

    # Prepares the new entity
    metadata = datastore.Entity(key=metdata_key)
    metadata["Bucket"] = event['bucket']
    metadata["File"] = event['name']
    metadata["md5Hash"] = event['md5Hash']
    metadata["timeCreated"] = event['timeCreated']
    metadata["updated"] = event['updated']

    # Saves the entity
    datastore_client.put(metadata)

    print("File Metdata uploaded to Datastore...")
