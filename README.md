# Transform google-pretrained (C format) to gensim format (python)
1. Download pretrained [file](https://drive.google.com/a/ucsc.edu/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit) [(Reference)](https://github.com/3Top/word2vec-api#where-to-get-a-pretrained-models)
2. Run frombin2gensim.py
```python
./frombin2gensim.py # will generate google_word2vec_pretrained
```

# Train word embedding from raw corpus
1. Run train_from_corpus.py
```python
./train_from_corpus.py corpus model_output 
```


# Use word embedding in your project
```python
from gensim.models import Word2Vec as W2V
model_path = 'path/to/embedding_model'
w2v = W2V.load(model_path)

```
