# Repository for final project

Final project

## Emotion Detection Web Application

A Flask web application that analyses a piece of text and detects the emotions expressed in it, using the IBM Watson NLP emotion prediction service. For any sentence, the app returns a score for five emotions (anger, disgust, fear, joy and sadness) and identifies the dominant one.

Built as the final project for the IBM AI engineering course.

## Features

- Emotion analysis of any English text via the Watson NLP `EmotionPredict` endpoint
- Scores for anger, disgust, fear, joy and sadness, plus the dominant emotion
- Simple web interface: type a sentence, click the button, see the result without reloading the page
- Error handling for blank input, with a clear message to the user
- Packaged as a reusable Python package (`EmotionDetection`)
- Unit tests covering all five dominant emotions
- `server.py` scores 10/10 on static code analysis with Pylint

## Project Structure

```
final_project/
├── EmotionDetection/
│   ├── __init__.py              # Makes EmotionDetection a package
│   └── emotion_detection.py     # emotion_detector() function
├── static/
│   └── mywebscript.js           # Sends the text to the server and shows the result
├── templates/
│   └── index.html               # Web interface
├── server.py                    # Flask application
├── test_emotion_detection.py    # Unit tests
├── LICENSE
└── README.md
```

## How It Works

1. The user enters text on the web page and clicks the button.
2. JavaScript reads the text and sends a GET request to `/emotionDetector?textToAnalyze=<text>`.
3. Flask passes the text to `emotion_detector()`, which calls the Watson NLP service.
4. The function extracts the five emotion scores and works out the dominant emotion.
5. Flask returns a formatted response, which is displayed on the page.

## Getting Started

### Prerequisites

- Python 3.10+
- Access to the Watson NLP service (available in the IBM Skills Network lab environment)

### Installation

```bash
git clone https://github.com/tomi2077/oaqjp-final-project-emb-ai.git final_project
cd final_project
python3 -m pip install flask requests pylint
```

### Running the App

```bash
python3 server.py
```

Then open `http://localhost:5000` in your browser.

## Usage

### Web interface

Enter a sentence such as `I think I am having fun` and click **Run Sentiment Analysis**. Example response:

```
For the given statement, the system response is 'anger': 0.0104, 'disgust': 0.0005,
'fear': 0.0029, 'joy': 0.9739 and 'sadness': 0.0157. The dominant emotion is joy.
```

### As a Python package

```python
from EmotionDetection.emotion_detection import emotion_detector

emotion_detector("I hate working long hours")
# {'anger': 0.649, 'disgust': 0.037, 'fear': 0.056, 'joy': 0.009,
#  'sadness': 0.196, 'dominant_emotion': 'anger'}
```

## Error Handling

If the input is blank, the Watson service returns status code `400`. In that case `emotion_detector()` returns every value as `None`, and the web app displays:

```
Invalid text! Please try again!
```

## Testing

Run the unit tests from the project root:

```bash
python3 test_emotion_detection.py
```

The tests check that the correct dominant emotion is detected for a sample sentence of each type (joy, anger, disgust, sadness and fear).

## Code Quality

Static code analysis with Pylint:

```bash
pylint server.py
```

Result: `10.00/10`

## Technologies

- Python
- Flask
- IBM Watson NLP
- JavaScript (XMLHttpRequest)
- HTML
- unittest
- Pylint

## Licence

See the [LICENSE](LICENSE) file for details.
