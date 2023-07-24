# Ultranslator

This repository contains an application that allows you to translate text into different styles or languages. It utilizes the OpenAI GPT-3.5 Turbo model for generating translations. Here's a brief overview of the application:

## How to Translate

1. Enter the text you want to translate in the provided text area.
2. Enter the desired translation directions or style in the corresponding text area. This can be a language, a specific style, or any other instructions.
3. Click the "Translate" button.
4. The translated text will be displayed in the main panel.

## Translation History

The sidebar displays a history of your translations. It includes the original text, the translation directions or style, and the corresponding translated text. This allows you to keep track of your previous translations.

Note: The application currently supports translating one set of text and translation directions at a time. If you want to translate multiple sets, you can uncomment the code for the second set of translation directions and modify it accordingly.

<br>

---

<br>


> update Monday, July 24th 2023
## Update **experimental** feature


<br>

### **Speech To Text** Now Available

----

This feature allows you to make a voice recording and have it automatically transcribe as the input to your text.

The audio recording used to transcribe is briefly sent to Google's Speech to Text API however:

- No Audio Data is only ever stored in your on system browser, specific to your device.

- Each time you record for a transcription, it will overwrite the previous recording (since it's your browser's cache that is storing the audio)

- You can play back, edit, download and immediately delete as the custom component includes these options.

- A more unified and improved User Interface for the Transcription element is in the works.
