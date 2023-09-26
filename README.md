[![Demo](https://img.shields.io/badge/Demo-Visit-blue)](https://www.shivam.pro/projects/textgen)

# Text Generation using 30M-param LSTM Model

The model is trained on a corpus of 9000+ articles from StackExchange Academia. The dataset was found from [this archive](https://archive.org/details/stack-exchange-2022-03-07) The compute resources used in training are a single GPU (1070 Ti) for approximately 12 hours.

<details>
  <summary>Model Diagram</summary>

![Spoiler Image](/model.png)

</details>

## How to Use

The model is available to try online [here](https://www.shivam.pro/projects/textgen). However, if you want to run it on your own, the code is provided.
First, run [main-text-gen-rnn.ipynb](/main-text-gen-rnn.ipynb). A folder should be created under models. This folder contains the model weights and the vocab. Next, if you want to convert it to Tensorflow.js format, run [tfjs-convert.ipynb](/tfjs-convert.ipynb).

## Sample Output

1. No starting text

```
I recently published my first research paper and it was accepted in a peer-reviewed journal in the field of Ai. I worked in private engineering in Europe (mostly in area, linear algebra, coding, and field topics that I have never seen on a topic that is required in the field on research and also engineering). I am worried about the quality of the world at the moment, but I know that this source of my ability of doing research is for all of those fields, being a big"
```

2. Starting text: "I am a"

```
I am a Masters student in math and thus new to academia and publishing in general. I am a coauthor on a number of recently submitted papers and had the (somewhat unreasonable) thought about it, now after reading on the blog, more proofreading. Now, to be clear, I failed a lot of emotional and open process as I can look at the methods eventually novel stuff.

My thought is that this may mean that I would also consider the" how you will somehow"
```
