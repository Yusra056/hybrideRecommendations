import pandas as pd
import csv
from sklearn.feature_extraction.text import TfidfVectorizer #Term Frequency and Inverse Document Frequency
from sklearn.metrics.pairwise import cosine_similarity, linear_kernel

df = pd.read_csv('C:\\Users\\IA\\Desktop\\Books\\Final Year Project\\code\\project\\books_dataset.csv', low_memory = False)

# stop words removing that is the a is
tfidf = TfidfVectorizer(stop_words= 'english')

#genre , book_desc
  
#nan words with empty string
df['genres'] = df['genres'].fillna('')

# TF and IDF construction
tfidf_matrix= tfidf.fit_transform(df['genres'])

#computating cosine similarity matrix
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

#reverse mapping
indice = pd.Series(df.index, df['book_title']).drop_duplicates()

#method create content-base recommendations

def create_contentBase_recommendations(title, cosine_sim=cosine_sim):
    #get the index of the book which show similarity
    idx = indice[title]

    #get the pairwise similiarity of the above book with other books
    similarity_score = list(enumerate(cosine_sim[idx])) 

    #sort the above list
    similarity_score = sorted(similarity_score, key=lambda x: x[1], reverse=True)

    #get the 15 most similar books
    similarity_score = similarity_score[1:9]

    #get the books indices
    book_indices = [i[0] for i in similarity_score]

    #return the top 9 similar books
    return df['book_title'].iloc[book_indices]

#a = 'Divergent'
#print(create_contentBase_recommendations(a))

#The Alchemist
#Divergent
#Chaos: Making a New Science
