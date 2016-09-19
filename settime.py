from time import strftime, time, localtime, sleep

from serial import Serial
read = lambda s : s.read(s.in_waiting)
def write(s, t=None):
  s.write(b'\r')
  s.flush()
  if t is None:
    t = strftime('s%H:%M:%S', localtime(time() + 1)).encode('ascii')
  else:
    t = ('s%s' % t).encode('ascii')
  s.write(t)
  s.flush()
  while int(time()%1*1000): pass # wait for ms to be 0
  s.write(b'\r')
  s.flush()
  print(t)
  
if __name__ == '__main__':
  from sys import argv, platform
  s = Serial('\\com1' if platform == 'win32' else '/dev/ttyS1')
  write(s, None if len(argv)<2 else argv[1])
