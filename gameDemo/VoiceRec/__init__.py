import pyaudio
import wave
import audioop
import base64
from io import BytesIO
#tencent
import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.asr.v20190614 import asr_client, models

import time

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 16000
RECORD_SECONDS = 0.8
WAVE_OUTPUT_FILENAME = "./output.wav"

THRESHOLD = 500

global result
result = ""
global run
run = True

def stop():
    global run
    run = False
def resultInit():
    global result
    result =""

def VoiceRec():
    #receive voice
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=CHUNK)
    frames=[]
    global run
    while run:
        try:
            data = stream.read(CHUNK)
        except:
            data = None
        rms = audioop.rms(data,2)

        if rms >THRESHOLD:
            #record voice
            frames.clear()
            print("* recording")
            for i in range(0, int(RATE  * RECORD_SECONDS / CHUNK)):
                data = stream.read(CHUNK)
                frames.append(data)
                
            print("* done recording")
            wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(p.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))
            wf.close()

            
            file = open(WAVE_OUTPUT_FILENAME, "rb")
            VoiceRecognizeAI(base64.b64encode(file.read()).decode('utf-8'))
            
            #restart the stream
            stream.stop_stream()
            stream.close()
            p.terminate()
            p = pyaudio.PyAudio()
            stream = p.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=CHUNK)
    
#0.tencent ai
def VoiceRecognizeAI(b64):
    if b64 ==None:
        print("No voice")
    else:
        try: 
            cred = credential.Credential("AKID2qV4PUimZ5vnPnv8IFOHvJRJvAEApZ4Q", "GF8pJDLFtHVUI3ZpRnvnQq2ziDRq0tYw") 
            httpProfile = HttpProfile()
            httpProfile.endpoint = "asr.tencentcloudapi.com"

            clientProfile = ClientProfile()
            clientProfile.httpProfile = httpProfile
            client = asr_client.AsrClient(cred, "", clientProfile) 

            req = models.SentenceRecognitionRequest()
            params = {
                "ProjectId": 1,
                "SubServiceType": 2,
                "EngSerViceType": "16k_en",
                "SourceType": 1,
                "VoiceFormat": "wav",
                "UsrAudioKey": "UsrAudioKey",
                "Data": b64
            }
            req.from_json_string(json.dumps(params))

            resp = client.SentenceRecognition(req) 
            #print(resp.to_json_string()) 
            global result
            result = json.loads(resp.to_json_string())['Result']
            print(result)
        except TencentCloudSDKException as err: 
            print(err) 

