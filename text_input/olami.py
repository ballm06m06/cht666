from text_input.nluapi import NluAPISample

from cht_package.config import OLAMI_APP_KEY, OLAMI_APP_SECRET, OLAMI_URL

def OLAMI_textInput(input):
    nluApi = NluAPISample()
    nluApi.setLocalization(OLAMI_URL)
    nluApi.setAuthorization('c97b4c08105144ee874c7329aa9e076a', '17256f7d09e34f8983cd20f60c5d9ae8')     
    
    print("\n---------- Test NLU API, api=seg ----------\n");
    print("\nResult:\n\n", nluApi.getRecognitionResult(nluApi.API_NAME_SEG, input))
    
    print("\n---------- Test NLU API, api=nli ----------\n");
    print("\nResult:\n\n", nluApi.getRecognitionResult(nluApi.API_NAME_NLI, input))

    return nluApi.getRecognitionResult(nluApi.API_NAME_NLI, input)