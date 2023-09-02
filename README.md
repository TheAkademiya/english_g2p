# english_g2p

## Introduction

A simple tool to convert English text to IPA transcription based on CMU Pronouncing Dictionary.

## Usage

```python
from english_g2p import G2P

g2p = G2P()
text = "Dear passengers, the next station is The Akademiya. Please get ready to get off."
phonemes = g2p.convert(text)
print(phonemes)
```

```bash
ˈdɪɹ ˈpæsəndʒɚz , ðə ˈnɛkst ˈsteɪʃən ˈɪz ðə akademiya* . ˈpliːz ˈgɛt ˈɹɛdi ˈtuː ˈgɛt ˈɔːf .
```
