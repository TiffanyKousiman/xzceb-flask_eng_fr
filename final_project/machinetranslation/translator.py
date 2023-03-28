"""
This module creates a Watson language translator API instance will be used 
in both the english_to_french and french_to_english functions to perform text 
translation.
"""

import os
from ibm_watson import LanguageTranslatorV3, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# create an instance of the IBM Watson Language translator
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """
    params: string: english text as an input into language translator 
        for translation
    returns: french text 
    """
    try:
        translation = language_translator.translate(
            text=english_text,
            model_id='en-fr').get_result()
        french_text = translation['translations'][0]['translation']
    except ApiException:
        french_text = None
        print("Text is empty, please provide an input.")

    return french_text

def french_to_english(french_text):
    """
    params: string: french text as an input into language translator 
        for translation
    returns: english text 
    """
    try:
        translation = language_translator.translate(
            text=french_text,
            model_id='fr-en').get_result()
        english_text = translation['translations'][0]['translation']
    except ApiException:
        english_text = None
        print("Text is empty, please provide an input.")

    return english_text
