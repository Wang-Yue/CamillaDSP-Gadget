#!/usr/bin/python3
import camilladsp
import sys

c = camilladsp.CamillaConnection("127.0.0.1", 5678)

try:
  c.connect()
  rate = int(sys.argv[1])
  config = c.stop()
  config = c.get_config()
  if config == None:
    config = c.get_previous_config()
    print("VIS: Get previous config.")
  config['devices']['capture_samplerate'] = rate
  if rate in [44100, 88200, 176400, 352800, 705600]:
    config['devices']['samplerate'] = 44100
  elif rate in [48000, 96000, 192000, 384000, 768000]:
    config['devices']['samplerate'] = 48000
  if rate > 0 and rate <= 96000:
    config['devices']['chunksize'] = 2048
  elif rate > 96000 and rate <= 192000:
    config['devices']['chunksize'] = 1024
  elif rate > 192000 and rate <= 384000:
    config['devices']['chunksize'] = 512
  elif rate > 384000:
    config['devices']['chunksize'] = 256
  c.set_config(config)
  print("VIS: Successfully adjust to the new sample rate!")
  c.disconnect()

except ConnectionRefusedError as e:
  print("VIS: Can't connect to CamillaDSP, is it running? Error:" + str(e))
except camilladsp.CamillaError as e:
  print("VIS: CamillaDSP replied with error:" + str(e))
except IOError as e:
  print("VIS: Websocket is not connected:" + str(e))
finally:
  pass

c = camilladsp.CamillaConnection("127.0.0.1", 1234)

try:
  c.connect()
  rate = int(sys.argv[1])
  config = c.stop()
  config = c.get_config()
  if config == None:
    config = c.get_previous_config()
    print("DSP: Get previous config.")
  if rate in [44100, 88200, 176400, 352800, 705600]:
    config['devices']['samplerate'] = 705600
  elif rate in [48000, 96000, 192000, 384000, 768000]:
    config['devices']['samplerate'] = 768000
  config['devices']['capture_samplerate'] = rate
  if rate > 0 and rate <= 96000:
    config['devices']['chunksize'] = 8192
  elif rate > 96000 and rate <= 192000:
    config['devices']['chunksize'] = 8192
  elif rate > 192000 and rate <=384000:
    config['devices']['chunksize'] = 4096
  elif rate > 384000:
    config['devices']['chunksize'] = 2048
  config['devices']['capture_samplerate'] = rate
  c.set_config(config)
  print("DSP: Successfully adjust to the new sample rate!")
  c.disconnect()

except ConnectionRefusedError as e:
  print("DSP: Can't connect to CamillaDSP, is it running? Error:" + str(e))
except camilladsp.CamillaError as e:
  print("DSP: CamillaDSP replied with error:" + str(e))
except IOError as e:
  print("DSP: Websocket is not connected:" + str(e))
finally:
  pass

