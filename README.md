# Spotify-Linear-Regression
Quantitative way for artists to interface with their fans; better understand what features in your music your fans love!

# Spotify User Engagement Analysis

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![R](https://img.shields.io/badge/R-4.0%2B-green) ![Spotipy](https://img.shields.io/badge/Spotipy-2.18%2B-yellow) ![rpart](https://img.shields.io/badge/rpart-4.1%2B-red)

This repository contains code and data for analyzing user engagement on Spotify based on audio attributes using multivariate regression. Our project explores the relationships between various audio features and listener engagement, aiming to predict music niches and enhance music recommendation methods on the world's largest music streaming platform.

## Table of Contents

- [Data Grab](#data-grab)
- [Regression](#regression)
- [Summary of Paper](#summary-of-paper)
- [Use Yourself](#use-yourself)

## Data Grab

In this section, we employ Python and the Spotipy library to interact with the Spotify API and collect data. We gather information about audio attributes for various artists and their songs. The collected data is stored as CSV files for further analysis.

### Prerequisites

- Python 3.8 or higher
- Spotipy 2.18 or higher

### Usage

1. Clone this repository.
2. Install the required packages using `pip install -r requirements.txt`.
3. Run the Python scripts in the `data_grab` directory to collect Spotify data.

## Regression

In the regression section, we utilize R and the rpart library to create multivariate regression models. These models help us understand the relationships between audio attributes and user engagement on Spotify. We measure the impact of removing specific attributes on the model's performance using the sum square error.

### Prerequisites

- R 4.0 or higher
- rpart 4.1 or higher

### Usage

1. Run the R scripts in the `regression` directory to create multivariate regression models.
2. Analyze the results to gain insights into user engagement.

## Summary of Paper

Our research findings and interpretations are summarized in the paper included in this repository. We present case studies on artists like Father John Misty and Foo Fighters to illustrate the impact of audio attributes on song popularity. The paper discusses the significance of attributes like 'acousticness,' 'liveness,' and 'danceability' in different music niches.

## Use Yourself

Feel free to use our code and methodology for your own research or projects. You can adapt the regression models and data collection scripts to analyze different artists or explore other aspects of user engagement on Spotify.

---

Please refer to the [paper](#summary-of-paper) for detailed results and interpretations. If you have any questions or suggestions, please open an issue in this repository.

**Contributors:**
- Luke Atkins
- Jack Fahrnow
- Akshika Rai
- Yichen Gao

![Spotipy](https://img.shields.io/badge/Powered%20by-Spotipy-yellow)
![rpart](https://img.shields.io/badge/Powered%20by-rpart-red)
