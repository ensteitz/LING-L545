# Final Project

  For my project, I wanted to merge text cleaning and segmentation with data scraped from a social media platform using Reddit's Python Reddit API Wrapper (PRAW) and Valence Aware Dictionary and sEntiment Reasoner (VADER).


## Collecting the data:

   To begin, I coded `get_comments.py` to scrape data from this url: 
    [Link] https://www.reddit.com/r/IsraelPalestine/comments/172w9gt/i_have_changed_my_mind_about_the_israelpalestine/?sort=new

   I then ran it through terminal: 

    python3 get_comments.py

   The result is the output of the files `df_comments.csv` and `comments.txt`


## Cleaning the data:

   From there, I went about cleaning the CSV file. This is done in `clean_csv.py` and running the following line in terminal:

    python3 clean_csv.py

   This code removes unnecessary lines from the data such as hyperlinks, AutoModerator comments, and empty lines.

   The output is a file called `df_clean_comments.csv`

   In addition to ensuring the coding of the data is correct, I had noticed when scraping that the data that there was a marker in front of sentences that were replies to comments. While this would be great to keep for an in depth analysis surrounding specific conversations, it is not needed for this analysis. Therefore, they have been removed for text cleaning purposes.

   The removal of the reply marker '>' at the beginning of sentences was done through through terminal with the following pipeline command:

    cat comments.txt | sed 's/^>//g' > mod_comments.txt


## Segmenting the data:

   In this step, some of the data in the text file was segmented: each sentence is returned on a new line for text analysis by breaking down the comment bodies line per line in a text file.

   This was done through the command line::

    sed '/a-zA-Z/!d' \< mod_comments.txt \> mod2\_comments.txt
    sed '/\\[deleted\\]/d' \< mod2_comments.txt \> mod3\_comments.txt
    sed '/[^https:\/\/.*]/d' \< mod3\_comments.txt \> clean\_comments.txt

   The result is a TXT file that puts each sentence on a new line for sentiment analysis and deletes hyperlinks.

## Data Analysis:
   I then ran a few data analysis measures on the CSV file. This adds two columns to the CSV: `sentiment_score` and `time_of_day`. These were added to make data visualization easier in the last step.
   A couple of other measures were computed:
    1. The timestamp for the first comment.
    2. The timestamp for the last comment.
    3. The amount of time that passed between the first and last comment accepted on the submission before being locked.
    4. The count for the most upvotes on one comment. 
    5. The count for the most downvotes on one comment.

   These counts are shown if you run analysis.py. You will also get a visual of the data frame. 

## Sentiment Analysis:
   Using VADER, sentiment analysis was performed on the text scraped from the original Reddit post. This was done through running the following through the command line:

    python3 vader_sa.py

   The results were stored in the files `sa_clean_comments.txt` and `df_sa_extralabels_clean_comments.csv`.


## Data Visualization:
   PNGs of data visualization models are included in this folder. The most important ones are the Upvotes vs Compound Sentiment Score, Comments by Time of Day, and Comments by Sentiment Category.

## References:
   1. [Link] https://praw.readthedocs.io/en/latest/getting_started/quick_start.html
   2. [Link] https://github.com/cjhutto/vaderSentiment
