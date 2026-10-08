"""
Flask server for the Emotion Detection application.

Serves the web page and provides an endpoint that analyses text
using the Watson NLP emotion detection service.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')


@app.route('/emotionDetector')
def sent_emotion():
    """
    Analyse the text sent from the web page and return the emotion scores.

    Returns the score for each emotion and the dominant emotion,
    or an error message if the input is blank.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    anger_response = response['anger']
    disgust_response = response['disgust']
    fear_response = response['fear']
    joy_response = response['joy']
    sadness_response = response['sadness']
    dominant_emotion_response = response['dominant_emotion']

    if dominant_emotion_response is None:
        return 'Invalid text! Please try again!'

    return (
        f"For the given statement, the system response is "
        f"'anger': {anger_response}, 'disgust': {disgust_response}, "
        f"'fear': {fear_response}, 'joy': {joy_response} and "
        f"'sadness': {sadness_response}. "
        f"The dominant emotion is {dominant_emotion_response}."
    )


@app.route('/')
def render_index_page():
    """Render the main page of the application."""
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    