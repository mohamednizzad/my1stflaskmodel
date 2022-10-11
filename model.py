from keras.models import load_model
        
# returns a compiled model
# identical to the previous one
model = load_model('my_model.h5')

import random

while True:
  texts_p = []
  prediction_input = input("You: ")

  name = "Lucy,Erica,Ask Becky,Abbie,Abi,Bailey,Balbo,Ballerina,Bambi,Alice,Daisie,Dandelion,Dane,Alita,Galaxina,Mia,Elly,Lisa,Valerie,Rhoda,Emma"
  names = name.split(",")
  bot_name = names[random.randint(0,len(names))]

  prediction_input = [letters.lower() for letters in prediction_input if letters not in string.punctuation]
  prediction_input = ''.join(prediction_input)
  texts_p.append(prediction_input)

  prediction_input = tokenizer.texts_to_sequences(texts_p)
  prediction_input = np.array(prediction_input).reshape(-1)
  prediction_input = pad_sequences([prediction_input],input_shape)

  output = model.predict(prediction_input)
  output = output.argmax()

  response_tag = le.inverse_transform([output])[0]
  print(bot_name,":",random.choice(responses[response_tag]))
  if (response_tag == 'goodbye' or response_tag == 'goodnight'):
    break