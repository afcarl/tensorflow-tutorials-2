import tensorflow as tf

node1 = tf.constant(3.0)
node2 = tf.constant(4.0)
node3 = tf.add(node1, node2)

sess = tf.Session()

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)

adder = tf.add(a,b)

result = sess.run(adder, {a: 3, b: 4.5})

print(result)
