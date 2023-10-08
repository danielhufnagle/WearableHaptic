import pyrealsense2 as rs
import numpy as np
import math
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

PIN_DATA = 16
PIN_LATCH = 20
PIN_CLOCK = 21

GPIO.setup(PIN_DATA, GPIO.OUT)
GPIO.setup(PIN_LATCH, GPIO.OUT)
GPIO.setup(PIN_CLOCK, GPIO.OUT)

GPIO.setwarnings(False)

pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 1280, 720, rs.format.z16, 6)
config.enable_stream(rs.stream.color, 1280, 720, rs.format.bgr8, 6)
pipeline.start(config)

align_to = rs.stream.depth
align = rs.align(align_to)

try:
    while True:
        frames = pipeline.wait_for_frames()

        aligned_frames = align.process(frames)
        depth_frame = aligned_frames.get_depth_frame()
        aligned_color_frame = aligned_frames.get_color_frame()

        if not depth_frame or not aligned_color_frame: continue
        
        # color_intrin = aligned_color_frame.profile.as_video_stream_profine().int
        depth_image = np.asanyarray(depth_frame.get_data())
        color_image = np.asanyarray(aligned_color_frame.get_data())
        ##################
        x, y = 20, 360
        depth1 = depth_frame.get_distance(x, y)

        x2, y2 = 183, 360
        depth2 = depth_frame.get_distance(x2, y2)

        x3, y3 = 366, 360
        depth3 = depth_frame.get_distance(x3, y3)

        x4, y4 = 549, 360
        depth4 = depth_frame.get_distance(x4, y4)

        x5, y5 = 732, 360
        depth5 = depth_frame.get_distance(x5, y5)

        x6, y6 = 915, 360
        depth6 = depth_frame.get_distance(x6, y6)

        x7, y7 = 1098, 360
        depth7 = depth_frame.get_distance(x7, y7)

        x8, y8 = 1279, 360
        depth8 = depth_frame.get_distance(x8, y8)
        ##################
        A1 = 0 if depth1 < 0.6 else 1
        A2 = 0 if depth1 < 0.6 else 1
        A3 = 0 if depth1 < 0.6 else 1
        A4 = 0 if depth1 < 0.6 else 1
        A5 = 0 if depth1 < 0.6 else 1
        A6 = 0 if depth1 < 0.6 else 1
        A7 = 0 if depth1 < 0.6 else 1
        A8 = 0 if depth1 < 0.6 else 1

        ledpattern = [A1, A2, A3, A4, A5, A6, A7, A8]
        print(ledpattern)

        GPIO.output(PIN_LATCH, 0)

        for x in ledpattern:
            GPIO.output(PIN_DATA, int(x))
            GPIO.output(PIN_CLOCK, 1)
            GPIO.output(PIN_CLOCK, 0)
        
        GPIO.output(PIN_LATCH, 1)

        sleep(0.5)
        print('break')
except Exception as e:
    print(e)
    pass
finally:
    pipeline.stop()
