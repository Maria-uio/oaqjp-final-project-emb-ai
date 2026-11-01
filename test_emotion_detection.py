"""Pruebas unitarias para la función emotion_detector."""
import unittest
from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Pruebas de la emoción dominante para distintas declaraciones."""

    def test_joy(self):
        """Alegría."""
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger(self):
        """Ira."""
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_disgust(self):
        """Disgusto."""
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_sadness(self):
        """Tristeza."""
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_fear(self):
        """Miedo."""
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result['dominant_emotion'], 'fear')


if __name__ == '__main__':
    unittest.main()
