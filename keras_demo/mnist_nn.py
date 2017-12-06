#Step 1. Import
import numpy as np
import matplotlib.pyplot as plt

from keras.datasets import mnist
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.utils import np_utils

#Step 2. Load Data
nb_classes = 10
(x_train, y_train), (x_test, y_test) = mnist.load_data()

print(type(x_train))
print("x_train shape", x_train.shape)
print("y_train shape", y_train.shape)

#Step 3. Show Data
# fig = plt.figure()
# plt.subplot(2,1,1)
# plt.imshow(x_train[0], cmap="binary", interpolation="none")
# plt.title("image" + str(y_train[0]))
# plt.subplot(2,1,2)
# plt.hist(x_train[0].reshape(784))
# plt.title("Pixel Values")
# plt.show()

#Step 4. Prepare Training
x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)
x_train = x_train.astype("float32")
x_test = x_test.astype("float32")
x_train /= 255
x_test /= 255

#Step 5. One hot encoding
original_y_test = y_test
y_train = np_utils.to_categorical(y_train,nb_classes)
y_test = np_utils.to_categorical(y_test,nb_classes)

print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)


#Step 6. Create model
model = Sequential()
model.add(Dense(256, input_shape=(784,)))
model.add(Activation("relu"))
# model.add(Dropout(0.3))

# model.add(Dense(256))
# model.add(Activation("relu"))
# model.add(Dropout(0.3))

model.add(Dense(10))
model.add(Activation("softmax"))

#Step 7. Compile
model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])

#Step 8. Training
history = model.fit(x_train, y_train, batch_size=128, epochs=10, verbose=2, validation_data=(x_test, y_test))

#Step 9. Check Accuracy
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.title('Training & Validation Accuracy')
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.legend(['training','validation'],loc='lower right')
plt.show()


#Step 10. Check Accuracy
loss_and_metrics = model.evaluate(x_test, y_test, verbose=2)
print("Test Loss", loss_and_metrics[0])
print("Test Accuracy", loss_and_metrics[1])


#Step 11. Filter incorrect data
predicted_classes = model.predict_classes(x_test, verbose=2)
correct_items = np.nonzero(predicted_classes == original_y_test)[0]
incorrect_items = np.nonzero(predicted_classes != original_y_test)[0]


for i in range(0,30):
    plt.subplot(3, 10, i+1)
    plt.imshow(x_test[incorrect_items[i]].reshape(28, 28), cmap="binary")
    plt.title("Predict " + str(predicted_classes[incorrect_items[i]]))
    
plt.show()