from multiprocessing import Process
import tf_handler as tfh # XYZ coords
import pf_handler as pfh # pathfind


if __name__ == '__main__':
    tf = Process(target=tfh.listen())
    tf.start()

    pf = Process(target=pfh.listen())
    pf.start()