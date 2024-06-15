
# Image Context Analysis for Use in Social Media

## Introduction
The aim of this project is to test if pre-trained LLMs (such as ChatGPT) can be used for image context categorization based on image captions and tags. The role of the LLM is to decide if the image belongs to one of the following categories: personal, social, or professional.

## Prerequisite

Clone the repository using the following command:

```bash
git clone https://github.com/yagub03/YagubThesis.git
cd YagubThesis
```

## How to Run Our Project

### Captioning
1. Open `captioning.ipynb`.
2. Add the folder where your image data is located.
3. Choose where you want the `.txt` file result.
4. Run the code in Jupyter notebook.

### Tagging
To install the required packages, run:

```bash
pip install -r requirements.txt
```

#### Single File

```bash
python run.py --file image.jpg
```

#### Batch Execution

```bash
python run.py --dir dir/dir
```

### Support Models

You can specify different models for tagging:

```bash
python run.py --file image.jpg --model wd14-vit.v1
python run.py --file image.jpg --model wd14-vit.v2
python run.py --file image.jpg --model wd14-convnext.v1
python run.py --file image.jpg --model wd14-convnext.v2
python run.py --file image.jpg --model wd14-convnextv2.v1
python run.py --file image.jpg --model wd14-swinv2-v1
python run.py --file image.jpg --model wd-v1-4-moat-tagger.v2
python run.py --file image.jpg --model wd-v1-4-vit-tagger.v3
python run.py --file image.jpg --model wd-v1-4-convnext-tagger.v3
python run.py --file image.jpg --model wd-v1-4-swinv2-tagger.v3
python run.py --file image.jpg --model mld-caformer.dec-5-97527
python run.py --file image.jpg --model mld-tresnetd.6-30000
```

### Using GPU
Requires CUDA 12.2 and cuDNN 8.x.

## LLM

1. Open `sb6z.py`.
2. Add the tags and captions folder.
3. Add your API key.
4. Choose which GPT model you want to use.
5. Choose the output file path and run the code:

```bash
python sb6z.py
```
