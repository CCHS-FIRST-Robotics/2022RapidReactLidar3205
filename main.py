from multiprocessing import Process
import tf_handler as tfh  # translation data processing
import submap_handler as smp  # obstacle mapping data processing


if __name__ == '__main__':
    tf = Process(target=tfh.listen())
    tf.start()

    pf = Process(target=smp.listen())
    pf.start()