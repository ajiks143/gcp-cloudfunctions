# gcp-cloudfunctions
This sample code makes use of Google Cloud Function to capture file metadata as and when the file is uploaded to Cloud Storage.
The metadata is captured into Cloud Datastore.

**Code Execution:**

 - Clone the git repo
    ```sh
    git clone https://github.com/ajiks143/gcp-cloudfunctions.git
    ```   
 - Go to respective project folder
    ```sh
    cd gcp-cloudfunctions
    ```
 - Create a service account from IAM console and create Key from the created Service account
   .Provide authentication credentials to your application code by setting the environment variable `GOOGLE_APPLICATION_CREDENTIALS`
    ```sh
    export GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH"
    ```
 - Run the shell script to build and delpoy the Cloud Functions
    ```sh
    ./deploy.sh <Google storage bucket name>
    ```
