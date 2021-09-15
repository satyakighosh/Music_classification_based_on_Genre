# Music_classification_based_on_Genre
In this project, I have tried to classify small segments of music based on its genre. It is a difficult task because audio or speech signals usually need sequence
models to process, which are often difficult to tune.Two different approaches are given here. 

1. One method involves calculating the MEL spectrogram from
the audio samples and giving it as an input to a CNN. It gives the label as the output. Because audio signals are perceptually more relevant in log-scale, the
use MEL scale seems useful here. And using a CNN on the MEL-spectrograms is a different idea than using sequence models. 

2. The second idea is to use hand-crafted features from the audio samples and then use three different classifiers on them. The features include both time-domain and frequency-domain features.
