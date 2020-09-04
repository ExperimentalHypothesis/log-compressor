# Log compressor

Projede '/var/log' adresar (vcetne vsech podlozek kam ma pristup) a zazipuje log fily do .gz formatu a smaze ty puvodni. Tim setri misto. Cesta na adresar je nastavitelna, takze kdyby se logy kumulovaly i jinde, tak je mozne to jednoduse pouzit s jinou cestou. 

## Instalace a spusteni:

Instalace pomoci requirements.txt
```
git clone git@github.com:ExperimentalHypothesis/log-compressor.git
cd log-compressor
python3.7 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Spusteni:

```
python compress.py
```

## Test:

```
pytest test_compress.py
```

## Nastaveni jako cron job:
Aby mazal logy kazdy mesic, je potreba ho nastavit jako cron job.

```
crontab -e
0 0 1 * * cd abspath/to/folder/with/compres.py && python compress.py >> compr_err.out
```

Pythoni compress.py script se tak bude spoustet kazdy 1. den v mesici, presne o pulnoci. Pripadne errory se budou logovat do stejne slozky, kde je skript do souboru compr_err.out


