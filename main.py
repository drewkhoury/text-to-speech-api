"""Synthesizes speech from the input string of text or ssml.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""
from google.cloud import texttospeech

# these lines needed as script was erroring on finding the env file from os var
import os
credential_path = "/tmp/text2speechkey.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

# Instantiates a client
client = texttospeech.TextToSpeechClient()

# Set the text input to be synthesized
synthesis_input = texttospeech.SynthesisInput(text="""

Hi, I'm Ralph. Well not really but you get the point. And the point is, Agile doesn't deliver Business Value.

There's a problem with how we deliver software today. The practice of iterative development (small batches) started in the 90s, followed by Agile in the early 2000s. Even with a "perfect" implementation of an Agile framework, most organizations are struggling to deliver business value.
In this podcast, we're going to explore business value together, and find out what happens when you fail to include business value as part of software delivery.

What is Business Value

Business value is what your business values, and, what your business values is actions that lead to profits. We define these actions as "an experiment that will lead to immediate or near future profits."
Every action we take is a guess at what might lead to that business value, but that's all it is, an educated guess. A guess in engineering is called a hypothesis. However, your business has no way of knowing if a hypothesis is successful or not until it conducts an experiment that proves, or disproves, it.
Tinkerbell and the lost boys - The perfect Agile project

Let's walk through the story of a company named Tinkerbell & The Lost Boys. At Tinker Bell & The Lost Boys we manufacture pixie dust. Materials are readily available, and our brilliant engineers understand dust formulations really well. Our profits appear to have plateaued. In an attempt to bring profits back up, our board of directors set a cost reduction goal of 20% for the coming year. The idea is to achieve the reductions in cost without negatively impacting revenues. In addition to the goal, the board set an overall budget.

""")

# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL, name="ar-XA-Standard-B"
)
# see https://cloud.google.com/text-to-speech/docs/voices for voice names

# Select the type of audio file you want returned
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

# The response's audio_content is binary.
with open("output.mp3", "wb") as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')
