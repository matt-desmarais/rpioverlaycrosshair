import picamera
import datetime as dt



with picamera.PiCamera() as camera:
    # Turn the camera's LED off
    camera.led = False
    camera.resolution = (1280, 720)
    camera.framerate = 24
    camera.start_preview()
    camera.annotate_background = picamera.Color('black')
    camera.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    camera.start_recording('dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S').h264')
    start = dt.datetime.now()
    while (dt.datetime.now() - start).seconds < 30:
        camera.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        camera.wait_recording(0.2)
    camera.stop_recording()
