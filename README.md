#Inspiration
Student depression an incredibly yet rarely discussed topic on college campuses, and colleges do not have a way to gauge how happy their student bodies are relative to one another. We chose to address this problem by identifying and visualizing pockets of negativity. Besides, wouldn't it just be cool to see which areas in the world are happy or sad? We created an platform that does exactly that!

#What it does
We built a platform that receives a college name from either a user or a database, finds the longitude and latitude of the college, and then pulls tweets from Twitter's API within a one mile radius. It then removes any links or hashtags in the tweet and uploads the resulting list of transformed tweets to Indico's sentiment analysis.

We used this platform to calculate "happiness scores" for twenty two schools in and around Boston, and graphed the resulting scores on a heat map using Google Drive via an Google Sheet. Originally, we had hoped that our platform could import and automatically calculate "happiness scores" for every college in our database (over 4,00!); however, while our platform could perform this task, the Twitter API limits us to 500 downloaded tweets per hour, which made it infeasible to calculate happiness scores for over 4000. :(

#How we built it
We began by writing the entire python script in pseudocode, and assigned responsibilities from there. We individually built python scripts that accomplished our personal tasks (eg. calling the Twitter API, removing irrelevant information from each tweet, or calling Indico) to a GitHub and combined them in one large script on Sunday morning.

#Challenges we ran into and what we learned
Our team included both Python-illiterate and Python-literate students, so we were forced to learn to code in new languages, pull from API's that none of us had ever played with, integrate our different backend pieces, and maintain both good coding and problem-solving skills. Our initial idea was to use Yik Yak as our social media platform. However, Yik Yak's non existent APIs and responsive website prevented us from using its database. The team moved onto using Twitter's API for the rest of the time being. Another challenge we ran into was exceeding Twitter's API request limit. In response to this, we limited our college size to only the schools in the Boston area and we created four access keys.

Our larger challenges include learning how to code in new languages (Python for some and HTML/CSS for others) , how to pull from API's, how to integrate our different backend pieces, and how to keep the design process at the center of brainstorming.

#Accomplishments that we're proud of
Our team included beginner hackers and CS students. We each spent a lot of time learning new things that we've never done before! We're so proud of how we prioritized teamwork, positive learning (we aimed to create a friendly learning environment for every member), and successfully created a product!

#What's next for StudentSents
In the future, we'd like to clean up our data visualizations to make them more dynamic. We'd also like to analyze sentiment from other social media like Instagram photos! Ultimately we'd like our resource to be used by college campuses as they begin important dialogues on their campuses about mental health.