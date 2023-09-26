import tensorflow as tf


class MyModel(tf.keras.Model):
    def __init__(self, vocab_size, embedding_dim, rnn_units):
        super().__init__()
        self.embedding = tf.keras.layers.Embedding(vocab_size, embedding_dim)
        self.lstm = tf.keras.layers.LSTM(rnn_units, return_sequences=True, return_state=True)
        self.dense = tf.keras.layers.Dense(vocab_size)

    def call(self, inputs, states=None, return_state=False, training=False):
        x = inputs
        x = self.embedding(x, training=training)
        if states is None:
            states = self.lstm.get_initial_state(x)
        x, h, c = self.lstm(x, initial_state=states, training=training)
        x = self.dense(x, training=training)

        if return_state:
            return x, [h, c]
        else:
            return x


class OneStep(tf.keras.Model):
    def __init__(self, model: tf.keras.Model):
        print("OneStep.__init__")
        super().__init__()
        self.model = model

    def create_mask(self, size):
        return tf.one_hot([1], size, on_value=float("-inf"), off_value=0.0)

    @tf.function
    def generate_one_step(self, input_ids, states=None, temperature=1.0):
        if states is None or (tf.reduce_prod(tf.shape(states)) == 0):
            predicted_logits, states = self.model(inputs=input_ids, return_state=True)
        else:
            # Unpack the LSTM states (h and c) from the states list
            h = states[0]
            c = states[1]
            predicted_logits, [h, c] = self.model(inputs=input_ids, states=[h, c], return_state=True)
            # make [h, c] into tensor
            states = [h, c]  # Pack the LSTM states again into a list

        states = tf.convert_to_tensor(states)

        predicted_logits = predicted_logits[:, -1, :]
        predicted_logits = predicted_logits / temperature
        predicted_logits += self.create_mask(tf.shape(predicted_logits)[-1])
        predicted_ids = tf.random.categorical(predicted_logits, num_samples=1)
        predicted_ids = tf.squeeze(predicted_ids, axis=-1)
        return predicted_ids, states
