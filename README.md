# Spotify-Linear-Regression
Quantitative way for artists to interface with their fans; better understand what features in your music your fans love!

Checkout the paper [here](https://github.com/lukeaal/Spotify-Linear-Regression/blob/main/Report.pdf) and the [slide deck](https://github.com/lukeaal/Spotify-Linear-Regression/blob/main/Slide_Deck.pdf) for an in-depth presentation!

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![R](https://img.shields.io/badge/R-4.0%2B-green) ![Spotipy](https://img.shields.io/badge/Spotipy-2.18%2B-yellow) ![rpart](https://img.shields.io/badge/rpart-4.1%2B-red)

This repository contains code and data for analyzing user engagement on Spotify based on audio attributes using multivariate regression. Our project explores the relationships between various audio features and listener engagement, aiming to predict music niches and enhance music recommendation methods on the world's largest music streaming platform.

# Table of Contents

- [Data Grab](#data-grab)
- [Regression](#regression)
- [Summary of Paper](#summary-of-paper)
- [Use Yourself](#use-yourself)

# Data Grab

This code snippet is written in Python and utilizes the following libraries and their versions:

- `requests`: Version not specified.
- `spotipy`: Version not specified. This library is used to interact with the Spotify Web API.
- `pandas`: Version not specified. This library is used for data manipulation.
- `csv`: Standard Python library for working with CSV files.

## How to Use:

1. **Tech Stack** 
   - Ensure that you have the required Python libraries (`requests`, `spotipy`, `pandas`, and `csv`) installed in your Python environment.
  
2. **Obtain a Spotify client ID** 
    - by registering your application with Spotify on their developer platform.

3. **Replace the `client_id` and `client_pass` variables** 
    - with your own Spotify client credentials.
  
4. **Artist Codes** 
    - The code collects data for three artists: Megan The Stallion, Father John Misty, and Foo Fighters. If you want to collect data for different artists, replace their Spotify Artist IDs with the ones provided in the code.

5. **Cleaning** 
    - It then removes certain non-continuous numerical data from the audio features and adds the 'popularity' index by querying the Spotify API for each song's popularity. (one could keep these in with one-hot encoding)

6. **Data Save;** 
    - Finally, it writes the cleaned data for each artist to separate CSV files: `MeganTheStallion.csv`, `FatherJohnMisty.csv`, and `FooFighters.csv`, containing the audio features and popularity information for each song.

Note, Make sure to handle any potential errors related to API requests, authentication, or file writing as needed in a real-world scenario.


# Regression

1. **Data Reading:**
   - The code reads a CSV file named "FatherJohnMisty.csv" from the "/data" directory into a variable `x`. It specifies that columns should not be treated as factors (`stringsAsFactors=FALSE`) and uses a comma (`,`) as the separator.

2. **Data Type Conversion:**
   - `x` is then converted to a character matrix using `sapply` and `as.character`.
   - Next, the character matrix is converted to a numeric matrix using `as.numeric`.

3. **Standardization:**
   - A subset of the numeric matrix (`x[, 9:11]`) is standardized using the `scale` function, resulting in a new standardized dataset named `new_data`.

4. **Data Concatenation:**
   - The standardized dataset `new_data` is combined with the first 8 columns of the original numeric matrix (`x[, 1:8]`) using `cbind`. The resulting matrix is stored in `new_x`.

5. **Linear Regression:**
   - `new_x` is further subset to create a matrix `X` containing the first 10 columns.
   - A vector `y` is created from the 11th column of `new_x`.
   - Linear regression coefficients `a` are calculated using the formula: `a = solve(t(X) %*% X, t(X) %*% y)`.
   - The code calculates the predicted values `yhat` using the computed coefficients and calculates the sum of squared errors (`sse`) between the predicted values and the actual values.

6. **Feature Elimination:**
   - The code then proceeds to perform feature elimination by iteratively removing one variable at a time from `X` and recalculating the linear regression model.
   - It calculates new sums of squared errors `new_sse` for each iteration and the difference `diff` between the old and new sums of squared errors.
   - It outputs information about the omitted variable, the new sum of squared errors, and the difference.

7. **Summary Statistics:**
   - Finally, the code prints the maximum and minimum differences observed during the feature elimination process.


### Usage

1. Run the R scripts in the `regression` directory to create multivariate regression models.
2. Analyze the results to gain insights into user engagement.

# Summary of Paper

# User Engagement As A Function Of Audio Attributes Using Multivariate Regression

**Authors:** Jack Fahrnow, Luke Atkins, Akshika Rai

## Abstract

In this project, we employ a multivariate regression model to explore the relationships between various audio attributes on Spotify and listener engagement. Understanding these relationships can help us predict a listener's next song choice and enhance their overall listening experience. As music enthusiasts and data analysts, our goal is to uncover insights that can benefit both artists and listeners on the world's largest music streaming platform.

## Usage

This repository contains code and data for conducting multivariate regression analysis on Spotify audio attributes. Our primary objectives are:

1. Predicting the niche of musical artists on Spotify.
2. Identifying the attributes of music that contribute to song popularity.
3. Measuring the impact of removing specific attributes on the model's performance.

The code is written in Python for data collection and preprocessing, and R Studio for regression modeling. We have used the Spotipy Python library to interact with the Spotify API and collect data. All data is stored as CSV files for easy access and analysis.

## Results

### Father John Misty Results and Interpretation

We analyzed the impact of audio attributes on the popularity of Father John Misty's songs. Our findings indicate that the attribute 'acousticness' has the most significant effect on his song popularity, while 'tempo' has the least influence. As an Alternative/Indie artist, his songs' high acousticness aligns with the preferences of his genre's fans, resulting in increased popularity. Conversely, tempo has less impact since it is typically higher for genres involving electronic instruments.

### Foo Fighters Results and Interpretation

For the rock band Foo Fighters, the attribute 'liveness' has the most substantial influence on song popularity, while 'danceability' has the least impact. Rock music enthusiasts appreciate higher levels of 'liveness' as it is associated with authenticity in this genre, contributing to song popularity. Conversely, 'danceability' has minimal effect as Foo Fighters' songs typically have a tempo above the range considered danceable.

## References

[1] Ashrith. (2019, March 22). What makes a song likeable? Medium. [Link](https://towardsdatascience.com/what-makes-a-song-likeable-dbfdb7abe404)

[2] Plantinga, B. (2018, April 29). What do Spotify's audio features tell us about this year's Eurovision Song Contest? Medium. [Link](https://medium.com/@boplantinga/what-do-spotifys-audio-features-tell-us-about-this-year-s-eurovision-song-contest-66ad188e112a)

[3] Bode, A. (2021, October 1). Spotify API and audio features. Medium. [Link](https://towardsdatascience.com/spotify-api-audio-features-5d8bcbd780b2)

[4] Ditto Inc. (n.d.). The simple way to get your music on Spotify: Ditto music. [Link](https://dittomusic.com/en/sell-your-music/spotify/)

[5] Ostrow, J. (2014, February 17). Finding and nurturing your musical niche. Disc Makers Blog. [Link](https://blog.discmakers.com/2014/01/finding-and-nurturing-your-musical-niche/#:~:text=By%20focusing%20on%20your%20niche,daily%20conversation%20with%20your%20fans.)

## Contributions of the Authors

- Luke Atkins: Wrote Python code for API calls and initial data cleaning, created presentation slides, and assisted in the final report.
- Jack Fahrnow: Assisted with the presentation, final report, and IEEE-style formatting of the project.
- Akshika Rai: Created the multilinear regressions in R for both artists, generated outcomes, created presentation slides, and contributed to report writing.
- Yichen Gao: [Contribution details needed]

## Challenges and Future Directions

In our analysis, we focused on using multivariate regression models. However, for future research, we could explore alternative algorithms such as approximate nearest-neighbor search algorithms. These methods can group songs based on shared attributes or qualities, potentially providing more efficient ways to enhance listener engagement and artist promotion on streaming platforms.

Moving forward, our team is interested in incorporating challenging parameters into our model and exploring decision trees or new types of models. These avenues of research could lead to more accurate predictions and a deeper understanding of the dynamics between audio attributes and user engagement on Spotify.



## Use Yourself

Feel free to use our code and methodology for your own research or projects. You can adapt the regression models and data collection scripts to analyze different artists or explore other aspects of user engagement on Spotify.

---

Please refer to the [paper](#summary-of-paper) for detailed results and interpretations. If you have any questions or suggestions, please open an issue in this repository.

**Contributors:**
- Luke Atkins
- Jack Fahrnow
- Akshika Rai

![Spotipy](https://img.shields.io/badge/Powered%20by-Spotipy-yellow)
![rpart](https://img.shields.io/badge/Powered%20by-rpart-red)
