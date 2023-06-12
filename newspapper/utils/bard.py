import os

from bardapi import Bard
from googletrans import Translator


token = os.getenv("BARD_API_KEY")
bard = Bard(token=token)
translator = Translator()
