
# Sentiment Analyser

This is a flask api that can be used to do the analysis of text sentiments. 

Depending upon the text we get a value from 0 to 100 where 50 indicates a neutral value while value>50 indicate postive sentence and value< 50 indicate negative sentence


## Installation

Install sentiment-analyser

Create virtual environment for python 3.7

```bash
  conda create -n <environment-name> python=3.7 -y
```
    
Enter the virtual environment

```bash
  activate <environment-name>
```

install all dependencies of the this project by
```bash
  pip install -r requirements.txt
```
## Hosted API
https://analytics.webemps.com/

## Postman output

### neutral sentence
![neutral](https://user-images.githubusercontent.com/52929512/186461428-d986a0cd-1623-4275-8a0d-e2dfad40b876.png)

### positive sentence
![postive](https://user-images.githubusercontent.com/52929512/186461464-bec46529-9c5d-4dd2-ad39-0a31dab7fa03.png)

### negative sentence
![neg](https://user-images.githubusercontent.com/52929512/186461497-188b4620-42f1-4615-8ede-25e323a133c9.png)
