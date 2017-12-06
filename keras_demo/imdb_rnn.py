#Import
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM
from keras.datasets import imdb

# Load Data
max_features = 8000
maxlen = 80
batch_size = 32

(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)

print(x_train[0])

x_train = sequence.pad_sequences(x_train, maxlen=maxlen)
x_test = sequence.pad_sequences(x_test, maxlen=maxlen)

print(x_train[0])

# Build Model
model = Sequential()
model.add(Embedding(max_features, 128))  # word2vector = Embedding to do 1 layer NN , 8000 trans to 128 
model.add(LSTM(128, dropout=0.3, recurrent_dropout=0.3))  
model.add(Dense(1, activation="sigmoid"))  #  0 1 一個
model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])


# Train
model.fit(x_train, y_train, batch_size=batch_size, verbose=1)
score, acc = model.evaluate(x_test, y_test, batch_size=batch_size)

# Print Summary
print(model.summary())