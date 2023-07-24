# About Google Cloud Services
### The overall, google cloud account is under: `augurybot@gmail.com`

### Use `augurybot@gmail.com` to login to google cloud services.

### Once logged in, navigate to `projects` / `ultranslator`.

### Within the project called `ultranslator` there is another service account called `augurybot`.

### The billing is associated directly with this service account: `augurybot` which is within the `ultranslator` project.

### (mastercard ending in 6396)

### This service account provides the authorizations, sets permissions (currently set role: `owner`)

### and provides the key to connect to the api.

### This key is a number and also a locally downloaded file that must be pointed to in order to maintain connection.

### If you lose this key it cannot be recovered. 

### You must create a new service level account that's associated with this project, the current one being `augurybot`.

 <sub> (not to be confused with the general overall account = `augurybot@gmail.com`) </sub> 

### This key is a `.json` file and can be found by navigating to **this** project's directory (the files where your application live on your computer not google cloud)

---
> root/.streamlit/.google/[ultranslator-312fe4951217.json](ultranslator-312fe4951217.json)
---

> to set the environment variable for session authentication
```
export GOOGLE_APPLICATION_CREDENTIALS=".streamlit/.google/ultranslator-312fe4951217.json"
```
---

<br>

# **Creating A `Google Cloud Storage Bucket`**

### For audio that exceeds 60 seconds in length or for file sizes that are > =  10mb you have to store the data in a [Google Cloud Storage Bucket](https://cloud.google.com/speech-to-text/docs/before-you-begin#optional_create_a_bucket)

<br>

- In the Google Cloud console, go to the [Cloud Storage Buckets page](https://console.cloud.google.com/welcome/new?_ga=2.21989245.730026214.1689936508-2079899434.1689936508&project=ultranslator).

- Go to Buckets page

- Click Create bucket.

- On the Create a bucket page, enter your bucket information. To go to the next step, click Continue.

- For Name your bucket, enter a unique bucket name. Don't include sensitive information in the bucket name, because the bucket namespace is global and publicly visible.

- For Choose where to store your data, do the following:

- Select a Location type option.

- Select a Location option.

- For Choose a default storage class for your data, select a storage class.

- For Choose how to control access to objects, select an Access control option.

- For Advanced settings (optional), specify an encryption method, a retention policy, or bucket labels.

- Click Create.
---

## Disable the Speech-to-Text API

#### Complete the [following steps](https://cloud.google.com/speech-to-text/docs/before-you-begin#disable_the) if you no longer need to use the Speech-to-Text API in the future.

1. Navigate to your  [Google Cloud dashboard](https://console.cloud.google.com/home/dashboard?project=ultranslator) and click on the Go to APIs overview link in the APIs box.

2. Select Cloud Speech-to-Text API.

3. Click the DISABLE API button at the top of the Cloud Speech-to-Text API page.

```