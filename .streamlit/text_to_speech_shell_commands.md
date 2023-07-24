# Open Cloud Shell

---

### Cloud Shell is a built-in command-line tool for the console. In this tutorial, you use Cloud Shell to deploy your app.

---

1. Open Cloud Shell by clicking `[>_]`

2. Activate Cloud Shell by clicking the `Activate` button

3. right click on the python file in the directory and choose an option that says something like `open in cloud shell` or `open in terminal`

4. follow these directions by typing in each of these commands, then pressing enter between each one.

### create the directory and the python file

```shell
mkdir speech-to-text-python && touch speech-to-text-python/app.py
```

### navigate into the directory and open the workspace editor 

```shell
cd speech-to-text-python
cloudshell open-workspace .
```

### set the project id for the current session

```shell
export PROJECT_ID=ultranslator
```

### Create a service account to authenticate your API requests:

> click `authorize` if a pop up asks you to accept the authorization connection

```shell
gcloud iam service-accounts create speech-to-text-quickstart --project ultranslator
```

### Grant your service account the roles/viewer Role:

```shell
gcloud projects add-iam-policy-binding ultranslator \
   --member serviceAccount:speech-to-text-quickstart@ultranslator.iam.gserviceaccount.com \
--role roles/viewer
```

### Create a service account key:

```shell
gcloud iam service-accounts keys create speech-to-text-key.json --iam-account \
   speech-to-text-quickstart@ultranslator.iam.gserviceaccount.com
```

### Set the key as your default credentials:

```shell
  export GOOGLE_APPLICATION_CREDENTIALS=speech-to-text-key.json
```

> Open app.py in the Cloud Shell Editor by running the following command in your terminal:


```shell
cloudshell open app.py
```


> Install the Speech-to-Text client library:



```shell
pip3 install --upgrade \
    google-cloud-speech

```


> In app.py, import the Speech-to-Text client library at the beginning of the file:


```shell
from google.cloud import speech
```

> Create a Speech-to-Text API client and add a variable that points to the path of the example audio file provided:


```python
# Instantiates a client
client = speech.SpeechClient()

# The name of the audio file to transcribe
gcs_uri = "gs://cloud-samples-data/speech/brooklyn_bridge.raw"
```


> Add the following code, which transcribes your audio file using the specified configuration, then prints the transcription:


```python
def transcribe_speech():
  audio = speech.RecognitionAudio(uri=gcs_uri)

  config = speech.RecognitionConfig(
      encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
      sample_rate_hertz=16000,
      language_code="en-US",
  )


  # Detects speech in the audio file


  response = client.recognize(config=config, audio=audio)

  for result in response.results:


    print("Transcript: {}".format(result.alternatives[0].transcript))
```

> At the end of your app.py file, call transcribeSpeech():

```python
transcribe_speech()
```

> From your terminal, run your application.

```shell
python3 app.py
```

> You should now see the transcribed message in your terminal:

```shell
Transcript: how old is the Brooklyn Bridge
```

> To avoid incurring charges to your account


> Delete the file containing your service account key.

```shell
  rm speech-to-text-key.json
```

> If you created a project specifically for this tutorial, you can delete it on the Google Cloud console Projects page.

> Install the Cloud Code extension for VS Code or JetBrains to explore more Google Cloud APIs from your IDE.
