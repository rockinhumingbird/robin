library(tidyverse)
library(tidytext)
library(tm)
library(SnowballC)
library(stringr)
library(wordcloud)
library(readtext)
####part 1 
text1review<-VectorSource(text1)
corpus1<-Corpus(text1review)
corpus1<-tm_map(corpus1,content_transformer(tolower))
corpus1<-tm_map(corpus1,removePunctuation)
corpus1<-tm_map(corpus1,stripWhitespace)
corpus1<-tm_map(corpus1,removeWords,stopwords("english"))
dtm <- DocumentTermMatrix(corpus1)
##use as control for the creation of tdm
tf <- list(weighting = weightTf, stopwords = stopwords,
           removePunctuation = TRUE,
           tolower = TRUE,
           minWordLength = 4,
           removeNumbers = TRUE)
tdm <- TermDocumentMatrix(corpus1,tf )
dim(tdm)
frequent2<-sort(rowSums(as.matrix(tdm)),decreasing=TRUE)

sum(frequency)
frequency[1:30]
words1<-names(frequency)
wordcloud(words1[1:50],frequency[1:70])
################total consulting
file1 <-read.csv("consulting.csv",stringsAsFactors = FALSE)
text1<- file1$text
text_df<-data_frame(line = 1:2645, text= text1)
text_df%>%
  unnest_tokens(word, text)

consulting<-file1 %>%
  group_by(size)%>%
  ungroup()
consulting1<-consulting %>%
  unnest_tokens(word,text)
consulting1 <- consulting1 %>%
  anti_join(stop_words)
#plot most commonwords
library(ggplot2)
consulting1 %>%
  filter(size == "") %>%
  count(word, sort=TRUE) %>%
  mutate(word = reorder(word, n))%>%
  ggplot(aes(word,n)) + 
  geom_col()+
  xlab(NULL)+
  coord_flip()

nrcjoy<-get_sentiments("nrc")%>%
  filter(sentiment == "joy")
consulting1%>%
  filter(size == "large") %>%
  inner_join(nrc) %>%
  count(word, sort= TRUE)
install.packages("reshape2")
library(reshape2)
consulting1 %>%
  filter(size == "small") %>%
  inner_join(get_sentiments("bing")) %>%
  count(word, sentiment, sort = TRUE) %>%
  acast(word ~ sentiment, value.var = "n", fill = 0) %>%
  comparison.cloud(colors = c("gray30", "red"),
                   max.words = 100)

dtm <- consulting1 %>%
    # get count of each token in each document
    # create a document-term matrix with all features and tf weighting
    cast_dtm(size,word)

dtm <- DocumentTermMatrix(consulting)


install.packages("scales")
library(scales)
# expect a warning about rows with missing values being removed
ggplot(frequency, aes(x = proportion, y = `Jane Austen`,
                      color = abs(`Jane Austen` - proportion))) +
  geom_abline(color = "gray40", lty = 2) +
  geom_jitter(alpha = 0.1, size = 2.5, width = 0.3, height = 0.3) +
  geom_text(aes(label = word), check_overlap = TRUE, vjust = 1.5) +
  scale_x_log10(labels = percent_format()) +
  scale_y_log10(labels = percent_format()) +
  scale_color_gradient(limits = c(0, 0.001),
                       low = "darkslategray4", high = "gray75") +
  facet_wrap(~author, ncol = 2) +
  theme(legend.position="none") +
  labs(y = "Jane Austen", x = NULL)
library(tidyr)
library(tidytext)
library(dplyr)
sentiment1 <- consulting1 %>%
  inner_join(get_sentiments("bing")) %>%
  count(size, index = row_number() %/% 10, sentiment) %>%
  spread(sentiment, n, fill = 0) %>%
  mutate(sentiment = positive - negative)
#compare size differnt 
library(ggplot2)
ggplot(sentiment1, aes(index, sentiment, fill = size)) +
  geom_col(show.legend = FALSE) +
  facet_wrap(~size, ncol = 2, scales = "free_x")

afinn <- consulting1 %>%
  inner_join(get_sentiments("afinn")) %>%
  group_by(index = row_number()%/%50) %>%
  summarise(sentiment = sum(score)) %>%
  mutate(method = "AFINN")
bing_and_nrc <- bind_rows(
  consulting1 %>%
    inner_join(get_sentiments("bing")) %>%
    mutate(method = "Bing et al."),
  consulting1 %>%
    inner_join(get_sentiments("nrc") %>%
                 filter(sentiment %in% c("positive",
                                         "negative"))) %>%
    mutate(method = "NRC")) %>%
  count(method, index = row_number()%/%50, sentiment) %>%
  spread(sentiment, n, fill = 0) %>%
  mutate(sentiment = positive - negative)

bind_rows(afinn,
          bing_and_nrc) %>%
  ggplot(aes(index, sentiment, fill = method)) +
  geom_col(show.legend = FALSE) +
  facet_wrap(~method, ncol = 1, scales = "free_y")

##compare dictionaries
words_1 = 
  m%>%
  unnest_tokens(output = word,input = m$text)%>%
  mutate(row=1:n())

original <- file2 %>%
  group_by(story) %>%
  mutate(linenumber = row_number())%>%
  ungroup()
data(stop_words)

tidy_text2 <- original %>%
  unnest_tokens(word, ï..text)

tidy_text2 <- original %>%
  anti_join(stop_words)
tidy_text2 %>%
  count(word, sort = TRUE)

afinn <- words_1 %>%
  inner_join(get_sentiments("afinn")) %>%
  group_by(row) %>%
  summarise(sentiment = sum(score)) %>%
  mutate(method = "AFINN")
bing_and_nrc <- bind_rows(
  words_1  %>%
    inner_join(get_sentiments("bing")) %>%
    mutate(method = "Bing et al."),
  words_1  %>%
    inner_join(get_sentiments("nrc") %>%
                 filter(sentiment %in% c("positive",
                                         "negative"))) %>%
    mutate(method = "NRC")) %>%
  count(method, index = row, sentiment) %>%
  spread(sentiment, n, fill = 0) %>%
  mutate(sentiment = positive - negative)

bind_rows(afinn,
          bing_and_nrc) %>%
  ggplot(aes(index, sentiment, fill = method)) +
  geom_col(show.legend = FALSE) +
  facet_wrap(~method, ncol = 1, scales = "free_y")


install.packages("drlib")
library(drlib)

tf_idf <- tidy_text2 %>%
  count(story, word, sort = TRUE) %>%
  bind_tf_idf(word, story, n) %>%
  arrange(-tf_idf) %>%
  group_by(story) %>%
  top_n(10) %>%
  ungroup

tf_idf %>%
  mutate(word = reorder_within(word, tf_idf, story)) %>%
  ggplot(aes(word, tf_idf, fill = story)) +
  geom_col(alpha = 0.8, show.legend = FALSE) +
  facet_wrap(~ story, scales = "free", ncol = 3) +
  scale_x_reordered() +
  coord_flip() +
  theme(strip.text=element_text(size=11)) +
  labs(x = NULL, y = "tf-idf",
       title = "Highest tf-idf words",
       subtitle = "different categories")

td_gamma <- tidy(topic_model, matrix = "gamma",                    
                 document_names = rownames(dfm))

ggplot(td_gamma, aes(gamma, fill = as.factor(topic))) +
  geom_histogram(alpha = 0.8, show.legend = FALSE) +
  facet_wrap(~ topic, ncol = 3) +
  labs(title = "Distribution of document probabilities for each topic",
       subtitle = "Each topic is associated with 1-3 stories",
       y = "Number of stories", x = expression(gamma))

library(quanteda)
library(stm)

dfm <- consulting1 %>%
  count(size, word, sort = TRUE) %>%
  cast_dfm(size, word, n)

sparse <- consulting1 %>%
  count(size, word, sort = TRUE) %>%
  cast_sparse(size, word, n)
dfm <- removeSparseTerms(dfm, sparse = .99)
tfidf <- consulting1 %>%
    count(size, word) %>%
    bind_tf_idf(word, size, n)
plot1 <- tfidf %>%
  arrange(desc(tf_idf)) %>%
  mutate(word = factor(word, levels = rev(unique(word))))

# graph the top 10 tokens for 4 categories
plot1%>%
  mutate(size = factor(size, 
                        labels = c("large", "Medium",
                                   "Small"))) %>%
  group_by(size) %>%
  top_n(10) %>%
  ungroup() %>%
  ggplot(aes(word, tf_idf, fill= size)) +
  geom_col() +
  labs(x = NULL, y = "tf-idf") +
  facet_wrap(~size, scales = "free") +
  coord_flip()
(tokens <- consulting %>%
    unnest_tokens(output = word, input = text) %>%
    # remove numbers
    filter(!str_detect(word, "^[0-9]*$")) %>%
    # remove stop words
    anti_join(stop_words) %>%
    # stem the words
    mutate(word = SnowballC::wordStem(word)))


dtm <- consulting %>%
    cast_dtm(document=row_number(),word)

library(caret)
rf <- train(x = dtm2,
                     y = factor(consulting1$size),
                     method = "rf",
                     ntree = 200,
                     trControl = trainControl(method = "oob"))
system.time({
  congress_rf_10 <- train(x = as.matrix(congress_dtm),
                          y = factor(congress$major),
                          method = "rf",
                          ntree = 10,
                          trControl = trainControl(method = "oob"))
})

words %>%
  bind_tf_idf(word,size,n) %>%
  arrange(desc(tf_idf))


tfidf <- consulting1 %>%
    count(size, word) %>%
    bind_tf_idf(term_col = word, document_col = size)


topic_model <- stm(dfm, K = 6, 
                   verbose = FALSE, init.type = "Spectral")
td_beta <- tidy(topic_model)

td_beta %>%
  group_by(topic) %>%
  top_n(10, beta) %>%
  ungroup() %>%
  mutate(topic = paste0("Topic ", topic),
         term = reorder_within(term, beta, topic)) %>%
  ggplot(aes(term, beta, fill = as.factor(topic))) +
  geom_col(alpha = 0.8, show.legend = FALSE) +
  facet_wrap(~ topic, scales = "free_y") +
  coord_flip() +
  scale_x_reordered() +
  labs(x = NULL, y = expression(beta),
       title = "Highest word probabilities for each topic",
       subtitle = "Different words are associated with different topics")

as.data.frame(get_sentiments('bing'))[1:50,]
get_sentiments('bing')%>%
  group_by(sentiment)%>%
  count()
as.data.frame(get_sentiments('afinn'))[1:50,]
get_sentiments('afinn') %>%
  group_by(score)%>%
  count()
consulting1 %>%
  inner_join(get_sentiments('afinn'),by = 'word')%>%
  select('score')%>%
  ggplot(aes(x=score))+geom_histogram()

library(ggplot2)
 words_1%>%
  inner_join(get_sentiments('bing'),by ='word')%>%
  select('sentiment')%>%
  group_by(sentiment)%>%
  summarize(freq=n())%>%
  ungroup()%>%
  ggplot(aes(x=sentiment,y=freq))+geom_bar(position='dodge',stat='identity',fill=c('red','green'))

 
words_1%>%
   inner_join(get_sentiments('afinn'),by ='word')%>%
   select('sentiment')%>%
   group_by(sentiment)%>%
   summarize(freq=n())%>%
   ungroup()%>%
   ggplot(aes(x=sentiment,y=freq))+geom_bar(position='dodge',stat='identity',fill=c('red','green'))
 
 
 
library(RColorBrewer)
words_1 %>%
   inner_join(get_sentiments('bing'),by = 'word')%>%
   select('sentiment')%>%
   group_by(sentiment)%>%
   summarize(freq=n())%>%
   ungroup() %>%
   ggplot(aes(x=reorder(sentiment,desc(freq)),y=freq,fill=freq))+geom_bar(position='dodge',stat='identity')+xlab('Sentiment')+ylab('Frequency')+coord_flip()




words_1 %>%
  inner_join(get_sentiments('afinn'),by = 'word')%>%
  select('score')%>%
  ggplot(aes(x=score))+geom_histogram()

words_1 %>%
  left_join(get_sentiments('afinn'),by = 'word')%>%
  summarize(score = mean(score,na.rm=T))%>%
  ggplot(aes(x=score))+geom_histogram()
