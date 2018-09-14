import tensorflow as tf

FLAGS = tf.app.flags.FLAGS
tf.app.flags.DEFINE_string('gpu', '0', """gpu id.""")

def main(argv=None):
    str_gpu = FLAGS.gpu
    print("str_gpu:", str_gpu)  




if __name__ == '__main__':
  tf.app.run()
