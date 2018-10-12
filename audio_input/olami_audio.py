from cht_package.config import OLAMI_APP_KEY, OLAMI_APP_SECRET, OLAMI_URL
from audio_input.asrapi import SpeechAPISample

import time

def OLAMI_audioInput(audio_path):
    
    asrApi = SpeechAPISample()
    asrApi.setLocalization(OLAMI_URL)
    asrApi.setAuthorization(OLAMI_APP_KEY, OLAMI_APP_SECRET)

    '''Start sending audio file for recognition'''
    print("\n----- Test Speech API, seq=nli,seg -----\n")
    print("\nSend audio file... \n");
    responseString =  asrApi.sendAudioFile(asrApi.API_NAME_ASR, 
            "nli,seg", True, audio_path, 0)
    print("\n\nResult:\n\n" , responseString, "\n")
    
    ''' Try to get recognition result if uploaded successfully.    
        We just check the state by a lazy way :P , you should do it by JSON.'''
    if ("error" not in responseString.lower()): 
        print("\n----- Get Recognition Result -----\n")
        time.sleep(1) #delay for 1 second
        ''' Try to get result until the end of the recognition is complete '''
        while (True):
            responseString = asrApi.getRecognitionResult(
                    asrApi.API_NAME_ASR, "nli,seg")
            print("\n\nResult:\n\n" , responseString ,"\n")
            ''' Well, check by lazy way...again :P , do it by JSON please. '''
            if ("\"final\":true" not in responseString.lower()): 
                print("The recognition is not yet complete.")
                if ("error" in responseString.lower()): 
                    break
                time.sleep(2) #delay for 2 second
            else: 
                break
    
    print("\n\n")

    return responseString
