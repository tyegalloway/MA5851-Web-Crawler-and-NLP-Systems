# MA5851: Doc 1
How can hotels in Townsville improve their customer experience?
Tye Galloway 
James Cook University
tye.galloway@my.jcu.edu.au

Task 1: Overview –Web Crawler and NLP Systems. 
More so than ever before in history, users are actively generating content and collaborating with other users to create a virtual community. The burgeoning information explosion offered on the internet suggests that customers regularly check other users' opinions in forums, blogs, and social networks before buying a product or contracting a service. The tourism domain is no different, and TripAdvisor has emerged as the most popular ranked website for holiday planning, with millions of tourists visiting the site when arranging their holidays. This user-generated content website offers many reviews detailing travellers' experiences with hotels, restaurants, and tourist spots. 
Studies suggest that the TripAdvisor website has been increasingly influential in a traveller's decision-making process when looking for accommodation. Understanding the TripAdvisor rating score system, plus the many customer hotel reviews, can be a daunting process for travellers and hotel managers. This investigation developed three separate web-crawler programs to extract text data from TripAdvisor to aid hotels in improving their customer experience. The first program was to scrape the URLs of all the hotels in Townsville advertised on TripAdvisor. The URLs were then passed through the second web scraping algorithm to gather the TripAdvisor hotel name and description. A third web-crawler program extracted every customer review for each hotel, the customer rating, and the date of their stay. 
To derive insight from the mountains of user-generated content (text data), natural language processing (NLP) techniques and tasks must be performed. This study implemented for following techniques:
	Tokenisation
	Stemming and Lemmatisation 
	N-Gram
	Vectorisation


Two NLP tasks addressed the issue of how hotels in Townsville can improve their customer experience:
	Topic Modelling using Latent Dirichlet Allocation (LDA).
	Sentiment Analysis using a Decision Tree Classification model.
Topic Modelling is an unsupervised data mining technique that constitutes a popular tool for extracting important themes (topics) from unstructured data and is employed to reveal and annotate extensive documents collection with thematic information (Christodoulou, 2020). This study used LDA as a topic-modelling technique. In LDA, a topic is a probability distribution function over a set of words used as a type of text summarisation (Chang & Ku, 2019). Using Bayesian probabilities, LDA then expresses the relationships between words regarding their affinity to certain latent variables (topics) (Alexander, Blank, & Hale, 2018). 
Sentiment analysis is an NLP tool that monitors user-generated content websites as it can provide insight into public opinion about numerous issues without requiring follow-up enquiries. Sentiment analysis is the process of programmatically identifying and categorising public opinion expressed in a piece of text, such as customer reviews (Luzon & Herrera, 2017). The idea is to determine whether the writer's attitude toward a particular topic or product is generally positive, negative, or neutral. Sentiment analysis has significantly increased in interest and is an active area of research due to the large amount of stored text on the internet and the importance of customer-generated opinions. As a result, more than 1 million research papers contain the term 'sentiment analysis, and various start-ups have been created to analyse sentiment in social media companies (Valdivia, Luzon, & Herrera, 2017). 
Multiple studies on TripAdvisor exist, but there is no complete analysis from the Topic Model or Sentiment Analysis viewpoint. This report proposes TripAdvisor as the data source for two NLP tasks mentioned above. Both NLP tasks address the issue of how hotels in Townsville can improve their customer experience. NLP will be performed on the TripAdvisor hotel customer reviews. The customer reviews were analysed to determine the themes of customer reviews via LDA Topic Modelling. The customer reviews were also used to predict the sentiment of the customer reviews using Sentiment Analysis and a Decision Tree Classification model. The performance of the classification model was evaluated using the following metrics: precision, recall, accuracy, and f1-score. 
![image](https://user-images.githubusercontent.com/52813413/145131133-95783780-1e1c-47fc-b5e1-f74d6315b393.png)

