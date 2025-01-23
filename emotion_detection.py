import json
import requests

def emotion_detector(text_to_analyze):

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    input_json = { "raw_document": { "text": text_to_analyze } }

    try:
        response = requests.post(url, headers=headers, json=input_json)
        response.raise_for_status()
        response_dict = response.json()
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Errore durante la chiamata al servizio Watson NLP: {e}")

    anger = response_dict.get('emotionPredictions')[0]['emotion']['anger']
    disgust = response_dict.get('emotionPredictions')[0]['emotion']['disgust']
    fear = response_dict.get('emotionPredictions')[0]['emotion']['fear']
    joy = response_dict.get('emotionPredictions')[0]['emotion']['joy']
    sadness = response_dict.get('emotionPredictions')[0]['emotion']['sadness']

    emotions = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness
    }
    dominant_emotion = max(emotions, key=emotions.get)

    result = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }

    return result['dominant_emotion']


if __name__ == "__main__":
    example_text = "Sono molto felice oggi!"
    output = emotion_detector(example_text)
    print(output)