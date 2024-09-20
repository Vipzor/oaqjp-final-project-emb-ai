import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers = headers)
    formatted_response = json.loads(response.text)

    if response.status_code == 400:
        return {"anger": None, "disgust": None, "fear": None, "joy": None, "sadness": None, 
        "dominant_emotion": None}

    a = formatted_response['emotionPredictions'][0]['emotion']
    anger_score = a['anger']
    disgust_score = a['disgust']
    fear_score = a['fear']
    joy_score = a['joy']
    sadness_score = a['sadness']
    max_score = max([anger_score, disgust_score, fear_score, joy_score, sadness_score])
    max_score_emotion = ''

    for k, v in a.items():
        if v == max_score:
            max_score_emotion = k

    return {"anger": anger_score, "disgust": disgust_score, "fear": fear_score, "joy": joy_score, "sadness": sadness_score, 
            "dominant_emotion": max_score_emotion}


