import sched
import time

s = sched.scheduler(time.time, time.sleep)


def do_some(sc):
    print("..............#")
    sc.enter(60, 1, do_some, (sc,))


s.enter(60, 1, do_some, (s,))
s.run()
