# a floating point range
def frange(start, end, step):
  r = start
  while r < end:
    yield r
    r += step

def xy_tuples(xmin, xmax, xstep, ymin, ymax, ystep):
  for x in frange(xmin, xmax, xstep):
    for y in frange(ymin, ymax, ystep):
      yield (x, y)
