url_lt = "https://api.jp-tok.language-translator.watson.cloud.ibm.com/instances/2ffcb8ea-a786-427b-82d9-751f7c00d9d1"
apikey_lt = "Zi8vP-N-S967jYCx0dwux6xWfR2EmqwVjCjzghl8-Zm5"

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator



authenticator = IAMAuthenticator(apikey_lt)
version_lt = "2018-05-01"

def translator(text, lang):
    language_translator = LanguageTranslatorV3(authenticator=authenticator, version=version_lt)
    language_translator.set_service_url(url_lt)

    translation_response = language_translator.translate(text=text, model_id=lang)

    translation = translation_response.get_result()

    translated_text = translation['translations'][0]['translation']
    return translated_text

def englishToFrench(text):
    return translator(text, "en-fr")

def frenchToEnglish (text):
    return translator(text, "fr-en")

#print(englishToFrench("Hello, How are you?"))
#print(frenchToEnglish ("Je vais bien"))