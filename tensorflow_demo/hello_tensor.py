import tensorflow as tf

sess = tf.Session()

# tf.constant
node1 = tf.constant(3.0, dtype=tf.float32)
node2 = tf.constant(4.0) # also tf.float32 implicitly
print(node1, node2)
print(sess.run([node1, node2]))


node3 = tf.add(node1, node2)
node3 = node1 + node2
print("node3:", node3)
print("sess.run(node3):", sess.run(node3))

# tf.placeholder 容器
a = tf.placeholder(tf.float32) 
b = tf.placeholder(tf.float32)
adder_node = a + b  # + provides a shortcut for tf.add(a, b)
print(sess.run(adder_node, {a: 3, b: 4.5})) # Run 執行 3, 4.5帶入
print(sess.run(adder_node, {a: [1, 3], b: [2, 4]}))

add_and_triple = adder_node * 3.
print(sess.run(add_and_triple, {a: 3, b: 4.5}))

# tf.Variable  類神經權重
W = tf.Variable([.3], dtype=tf.float32) # 0.3
b = tf.Variable([-.3], dtype=tf.float32) # -0.3
x = tf.placeholder(tf.float32)
linear_model = W*x + b
init = tf.global_variables_initializer()
sess.run(init)
print(sess.run(linear_model, {x: [1, 2, 3, 4]}))

y = tf.placeholder(tf.float32) #input 的變量 
squared_deltas = tf.square(linear_model - y) # Cost Function 
loss = tf.reduce_sum(squared_deltas) # Cost Function  
print(sess.run(loss, {x: [1, 2, 3, 4], y: [0, -1, -2, -3]}))

#正確答案先comment掉否則 Train 無意義
#fixW = tf.assign(W, [-1.]) 
#fixb = tf.assign(b, [1.]) 
#sess.run([fixW, fixb])
#print(sess.run(loss, {x: [1, 2, 3, 4], y: [0, -1, -2, -3]})) #代入x.y , 手動W , b  自我learning 

# tf.train API  
optimizer = tf.train.GradientDescentOptimizer(0.01)  #learning rate loss Function的微分斜率
train = optimizer.minimize(loss)  #minimize loss function 
print(sess.run(W), " & ", sess.run(b))
sess.run(init) # reset values to incorrect defaults.
for i in range(1000):    #跑1000次 Train結果
    sess.run(train, {x: [1, 2, 3, 4], y: [0, -1, -2, -3]})
    print(sess.run(W), " & ", sess.run(b))

print(sess.run([W, b]))
