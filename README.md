RiSE
====
Regulation Intelligence Surveillance Engine
-------------------------------------------

RiSE is a tool for analysing large volumes of unstructured data to filter and sort according to relevance and priority.

This repo is the barebones MVP showing how RiSE can use the Python [spaCy](https://spacy.io/) library to analyse text and identify relevant sections. The MVP was used as the basis for our pitch at the UTS/KWM #breakinglaw hackathon on September 15th 2018 where it won first place and the peoples choice award.

To get started I recommend working in a python virtual environment.

```
virtualenv venv
```

You now need to activate the new environment.
```
source venv/bin/activate
```

The only requirement currently is spaCy but best to prepare for more.
```
pip install -r requirements.txt
```

SpaCy needs to download the language packs. The demo was in English so:
```
python -m spacy download en
```

If you want to receive a notification when running the tool you'll need to setup your own [ifttt](https://ifttt.com) account and webhook to obtain a secret key and configure a notification task. (I used pushover to send the notifications to my phone for the demo).

If everything worked you can now invoke rise.py which will read the m1.txt file and analyse the contents. A graphical depiction of the results can be obtained at [http://localhost:5000](http://localhost:5000)

The intention of this demonstration is to keep it simple. If a team wanted to take our concept and build a real product the results of the spaCy analysis would be stored in a database and used to build out the full interface. We didn't win the hackathon because our code was awesome (it isn't) we won because we'd thought through the impacts of how do we obtain the data, how do we process it and then what do we do with the data and why is this analysis important.
