# gcp-cloudfunctions
Sample use-case using Google Cloud Functions

**Code Execution:**

 - Clone the git repo
    ```sh
    git clone https://github.com/ajiks143/gcp-cloudfunctions.git
    ```   
 - Go to respective project folder
    ```sh
    cd gcp-cloudfunctions
    ```
 - Provide authentication credentials to your application code by setting the environment variable `GOOGLE_APPLICATION_CREDENTIALS`
    ```sh
    export GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH"
    ```
 - Run the shell script to build and delpoy the Cloud Functions
    ```sh
    ./deploy.sh <Google storage bucket name>
    ```
