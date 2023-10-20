# Sentiment Analysis on Automobile Brands
 Sentiment Analysis on Automobile Brands Using DonanımHaber Data

Sentiment Analysis on Automobile Brands is a sentiment analysis project that that helps you gain insights from text data by analyzing and classifying as negative, neutral or positive the sentiment expressed within the text.

# Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Documentation](#documentation)
4. [Usage](#usage)
5. [Features](#features)
6. [Contributing](#contributing)
7. [License](#license)

## Introduction

The project analyzes and visualizes the sentiment of automobile brands by analyzing the comments on the DonanımHaber forum site.
The reviews in the DonanımHaber list are real-time and unlabelled comments.

![GitHub Logo](https://github.com/EmineSener/Sentiment-Analysis-on-Automobile-Brands/blob/main/readme/intro.png)

### Description
Sentiment Analysis on Automobile Brands is a project that offers the following key features:

**Data Collection**: Collect data from the DonanımHaber website for use in model training and sentiment analysis.

**Data Prepocessing**: Prepare and preprocess text data for improved readability, analysis, and modeling.

**Data Annatation**: Annotate collected data with sentiment labels (positive, negative, neutral) to build ground-truth datasets.

**Feature Extraction**: Feature extraction enables the accurate representation of sentiment in text data.

**Create Model**: Create and train a model to ensure high accuracy in sentiment prediction.

**Sentiment Analyse**: Process analysis data, extract features and use as input for the model to make predictions.

**Process Result**: Process predictions for data visualization.

**Data Visualization**: Use graphics to communicate and share analysis results more clearly and effectively.

**Web Application**: Create a dynamic web application that display and enable interaction with visualizations that are generated from sentiment analysis.


## Installation

If you have Git installed on your computer, clone the repo.

Go to the directory you want to clone.For example Desktop:

```bash
cd ~/Desktop
```

Clone the repostory.

```bash
git clone https://github.com/EmineSener/Sentiment-Analysis-on-Automobile-Brands
```

If you are not using git, after clicking the green `Code` button at the top right of the repository, select the `Download ZIP` option, and the project source code will be downloaded to your local computer.


Open a command line and enter the project folder.

Install the required packages:

```bash
pip install -r requirements.txt
```

To run it:

```bash
python app.py
```

## Usage 

When you run the project, you can view the results of the model that has been trained with the data I collected previously. 

However, this project offers more than just that. You have the option to create your dataset by collecting the latest comments and then train the model using your dataset.

Afterward, you can analyze and view the results.

You will need jupyter notebook for this.

Open the terminal and go to the directory where the project is located.

Start the Jupyter Notebook server:

```bash
   jupyter notebook
```

To run cells in Jupyter Notebook, click on the cells and press "Shift+Enter".


## Documentation

### [Web Scraping](./WebScraping/)

I collected the reviews needed to train and test the model from the `DonanımHaber` news site with [create_dataset.ipynb](./WebScraping/create_dataset.ipynb/) in this folder.

Creating the dataset from scratch may be time-consuming.You can utilize my dataset.My dataset is quite large, which is why I haven't uploaded it to GitHub. 

You can download [dataset](https://drive.google.com/file/d/1Gr8_PRvZZS3irgXelXMa5PMjCRzyYqZi/view?usp=sharing)

If you want to create your own dataset, run [create_dataset.ipynb](./Web Scraping/create_dataset.ipynb/).

You can customize settings for your own dataset using the information provided in the notebook.

You can also download the data required for analysis via [create_dataset.ipynb](./WebScraping/create_dataset.ipynb/).

If you don't want to run for analyse data,you can download [my analyze data](./WebScraping/Brands).

### [Machine Learning](./MachineLearning/)

In this section, we apply machine learning techniques to perform natural language processing in Turkish.

#### [Preprocessing](./MachineLearning/data_preprocessing.ipynb)
Preprocessing is cleaning and transforming unstructured text data to prepare it for analysis. It includes removing punctstemming, lemmatization, stop-word removal, and part-of-speech tagging.

The preprocessing steps involve removing punctuation marks, stop words, non-sentiment phrases, URLs, and numbers. Additionally, all letters are converted to lowercase, and time information is transformed into a date format to prepare the data for analysis. In the [preprocessing](./MachineLearning/data_preprocessing
.ipynb) , explanations were provided for the necessity of these operations in sentiment analysis.

You can prepare your raw dataset for natural language processing with the [preprocessing](./MachineLearning/data_preprocessing.ipynb) tool, or you can use [my preprocessed dataset](https://drive.google.com/file/d/1XM762OaeK4O3fQyjPtUkLBgz1jptI2tr/view?usp=sharing).


#### Data Annotation

The comments on the DonanımHaber site lack sentiment tags. If the comments had a star rating feature like other websites, we could easily categorize them based on their star ratings. 

Since we don't have any data other than the text itself, we must rely on the textual context to label the comments as negative, positive, or neutral. 

To achieve this, we employed two different approaches:

1.[Data Annotation with OpenAI API](./MachineLearning/data_annotation_openai.ipynb)

If you are using the free version of OpenAI, you won't be able to send prompts continuously. The free version encounters an error in approximately 20 seconds. That's why we wait for 20 seconds when an error occurs. However, this approach proved to be very time-consuming when applied to the entire dataset, so we couldn't label the dataset using this method.
When I compare a few comments I labeled using the OPENAI API with the alternative approach, I can confidently say that this method provides more accurate results.


2.[Data Annotation with FLAN](./MachineLearning/data_annotation_openai.ipynb)

However, it can be stated that manual tagging is the most trustworthy approach for labeling text




## Usage

This is the usage section.

## Features

List of features goes here.

## Contributing

Guidelines for contributing to the project.

## License

Information about the project's license.

 
 
