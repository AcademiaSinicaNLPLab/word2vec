# Steps
1. Download pretrained [file](https://doc-0o-1c-docs.googleusercontent.com/docs/securesc/6ico03p8bbrcremslk1f25c64o4ot88q/r61lob8k17h7l0tnaa7gs8febqceul4t/1458273600000/06848720943842814915/07127650454305743752/0B7XkCwpI5KDYNlNUTTlSS21pQmM?e=download&nonce=etmi94mssg0fe&user=07127650454305743752&hash=a9s7rvi5d4ujd11hifm8qqd4ht0gpjv1)
2. Run frombin2gensim.py
```python
./frombin2gensim.py # will generate google_word2vec_pretrained
```
3. Use google_word2vec_pretrained in your project
```python
from gensim.models import Word2Vec as W2V
model_path = 'path/to/google_word2vec_pretrained'
w2v = W2V.load(model_path)

```
