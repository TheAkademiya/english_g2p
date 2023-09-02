import re

from english_g2p.tables import arpabet_ipa_table


_stresses = re.compile(r"[012]")

def arpabet_to_ipa(syls_arpabet):
    """Convert arpabet phonemes to IPA phonemes
    Input is a list of syllables. 
    Phonemes in each syllable is seperated by hyphen
    """

    syls_ipa = []   # return a list of ipa syllables
    for syl_arpabet in syls_arpabet:
        syl_arpabet = syl_arpabet.strip("-")    # remove redundant hyphen
        phns_arpabet = syl_arpabet.split("-")   # split syllabel into arpabet phonemes
        phns_ipa = []
        for phn_arpabet in phns_arpabet:
            if phn_arpabet in arpabet_ipa_table.keys():
                phn_ipa = arpabet_ipa_table[phn_arpabet]
                phns_ipa.append(phn_ipa)
        syl_ipa = "-".join(phns_ipa)
        syls_ipa.append(syl_ipa)

    return syls_ipa


def assign_stress(syls):
    """Assign stress to each (ipa) syllable
    Phonemes in each syllable is seperated by hyphen
    """
    # e.g. ['p-r-ɑ1ː', 'dʒ-ɛ0-k-t']

    for i, syl in enumerate(syls):
        stress = re.findall(_stresses, syl)
        if stress:
            stress = stress[0]
            syl = re.sub(stress, "", syl)
        else:
            raise ValueError("{} doesn't have stress.".format(syls))
        if stress == "1":
            # primary stress
            syls[i] = "ˈ-" + syl
        elif stress == "2":
            # secondary stress
            syls[i] = "ˌ" + syl
        else:
            # no stress
            syls[i] = syl
        
    return syls


def shift_vowel(syls_list):
    """Change the pronunciation of some vowel
    e.g. ðə -> ð
    """

    return syls_list

