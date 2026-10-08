from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')

@app.route('/emotionDetector')
def sent_emotion():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    anger_reponse = response['anger']
    disgust_reponse = response['disgust']
    fear_reponse = response['fear']
    joy_response = response['joy']
    sadness_response = response['sadness']
    dominant_emotion_response = response['dominant_emotion']
    if dominant_emotion_response is None:
        return 'Invalid text! Please try again!.'
    return (
            f"For the given statement, the system response is "
            f"'anger': {anger_reponse}, 'disgust': {disgust_reponse}, "
            f"'fear': {fear_reponse}, 'joy': {joy_response} and "
            f"'sadness': {sadness_response}. "
            f"The dominant emotion is {dominant_emotion_response}.")

@app.route('/')
def render_index_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)