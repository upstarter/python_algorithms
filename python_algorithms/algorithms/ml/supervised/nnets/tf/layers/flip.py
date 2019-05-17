# tf 2.0 streamlined API: Custom Layers
class Flip(tf.keras.layers.Layer):
    def __init__(self, pivot=0, **kwargs):
        super(Flipm, self).__init__(**kwargs)
        self.pivot = pivot

    def call(self, inputs):
        return self.pivot - inputs


x = tf.keras.layers.Dense(units=10)(x_train)
x = Flip(pivot=100)(x)
