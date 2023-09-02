import os
import re
from typing import Any

import pkg_resources

from english_g2p.cmudict import CMUDict
from english_g2p.syllabify import get_syllables
from english_g2p.utils import arpabet_to_ipa, assign_stress


# TODO: complete puncts
_punctuations = re.compile(r"[,.!\?]")


class G2P(object):
    """English grapheme-to-phoneme conversion
    """

    def __init__(self, dict_path=None):
        if dict_path is None:
            # try to load cmudict in current directory
            dict_path = pkg_resources.resource_filename(__name__, "cmudict-0.7b")
            if os.path.exists(dict_path) and os.path.isfile(dict_path):
                self.dict = CMUDict(dict_path)
            else:
                # TODO: download cmudict
                raise FileNotFoundError("No dictionary available.")
        else:
            if os.path.exists(dict_path) and os.path.isfile(dict_path):
                self.dict = CMUDict(dict_path)
    
    def __call__(self, text):
        return self.convert(text)

    def convert(self, text):
        # split text into sentences
        sentences = re.split(_punctuations, text)
        sentences = list(filter(None, sentences))
        puncts = re.findall(_punctuations, text)
        phonemes_list = []

        for i, sentence in enumerate(sentences):
            # split sentence into words
            words = sentence.split()
            for word in words:
                # lookup in dictionary and get arpabet pronunciation
                pron = self.dict.lookup(word)
                if pron:
                    # TODO: more possible pronunciations
                    pron = pron[0]
                    # syllabify
                    syls_arpabet = get_syllables(pron)
                    # to ipa
                    syls_ipa = arpabet_to_ipa(syls_arpabet)
                    # assign stress
                    syls_ipa = assign_stress(syls_ipa)
                    # post-process
                    phns = "".join(syls_ipa).replace("-", "")
                else:
                    # unknown word
                    phns = word.lower() + "*"

                phonemes_list.append(phns)
                
            if i < len(puncts):
                phonemes_list.append(puncts[i])

        phonemes = " ".join(phonemes_list)
        
        return phonemes





