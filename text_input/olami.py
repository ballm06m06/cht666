from text_input.nluapi import NluAPISample

from cht_package.config import OLAMI_APP_KEY, OLAMI_APP_SECRET, OLAMI_URL

def OLAMI_textInput(input):
    nluApi = NluAPISample()
    nluApi.setLocalization(OLAMI_URL)
    nluApi.setAuthorization(OLAMI_APP_KEY, OLAMI_APP_SECRET)     
    
    print("\n---------- Test NLU API, api=seg ----------\n");
    print("\nResult:\n\n", nluApi.getRecognitionResult(nluApi.API_NAME_SEG, input))
    
    print("\n---------- Test NLU API, api=nli ----------\n");
    print("\nResult:\n\n", nluApi.getRecognitionResult(nluApi.API_NAME_NLI, input))

    #return nluApi.getRecognitionResult(nluApi.API_NAME_NLI, input)