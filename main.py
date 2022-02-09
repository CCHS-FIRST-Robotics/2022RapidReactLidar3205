from multiprocessing import Process
import tf_handler as tfh # XYZ coords
import sub_map_handler as smp # pathfind


if __name__ == '__main__':
    tf = Process(target=tfh.listen())
    tf.start()

    pf = Process(target=smp.listen())
    pf.start()