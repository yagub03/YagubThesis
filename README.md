# Image context analysis for use in social media
## Introduction
The aim of this project is to test if pre-trained LLMs (ChatGPT) can be used for imaging context categorisation based on image captions and tags. The role of LLM is to decide if the image belongs to one of the following categories: personal, social, professional.

## Prequisite: 

Clone the repository by using git clone https://github.com/yagub03/YagubThesis.git command and then cd YagubThesis

## How to run our project:
## Captioning: Open captioing.ipynb
We ned to add folder where our image data is and then also choose where we want our .txt file result. After this we can run our code in Jupyter notebook
## Tagging: Open run.py 
For running: pip install -r requirements.txt
single file

```
python run.py --file image.jpg
```

batch execution

```
python run.py --dir dir/dir
```

## Support Models

```
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

## Using GPU

Requires CUDA 12.2 and cuDNN8.x.

## LLM
Open sb6z.py
Add tags and captions folder and don't forget to add your API key
Then you need to choose which GPT model you want to use.At last we choose output file path adn run the code as 
## 
``` python sb6z.py ``` 



