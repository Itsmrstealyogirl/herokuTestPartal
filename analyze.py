import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud import ToneAnalyzerV3
from os.path import join, dirname
from watson_developer_cloud.natural_language_understanding_v1 \
  import Features, EntitiesOptions,EmotionOptions,KeywordsOptions,ConceptsOptions,SentimentOptions, CategoriesOptions

natural_language_understanding = NaturalLanguageUnderstandingV1(
  username='9b6a8482-b8a3-4f1b-8d76-08d5c65fc08a',
  password='emH6VS7UXAAk',
  version='2017-02-27')

response = natural_language_understanding.analyze(
  url='https://www.nytimes.com/2014/05/25/magazine/must-the-captain-always-go-down-with-the-ship.html',
  features=Features(
  	entities=EntitiesOptions(
      emotion=True,
      sentiment=True,
      limit=15),
  	emotion=EmotionOptions(
      targets= ['keyword1','keyword2']),
    keywords=KeywordsOptions(
      emotion=True,
      sentiment=True,
      limit=2),
    concepts=ConceptsOptions(
      limit=5),
    sentiment=SentimentOptions(
      targets=['stocks']),
    categories=CategoriesOptions()))

print(json.dumps(response, indent=2))

tone_analyzer = ToneAnalyzerV3(
  username='0a1b2be1-47e7-451c-aaf3-d97b4f0b522e',
  password='p0pRXK3WP0Hu',
  version='2017-09-21'
)

with open('https://www.nytimes.com/2014/05/25/magazine/must-the-captain-always-go-down-with-the-ship.html') as tone_json:
  tone = tone_analyzer.tone(tone_json.read())

print(json.dumps(tone, indent=2))