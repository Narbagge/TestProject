import libs.arithmetic.add as add
import libs.arithmetic.mul as mul

def radius_squared(x, y):
  xs = mul.mulnum(x, x)
  ys = mul.mulnum(y, y)

  noEinsteinDefect = add.addnum(xs, ys)
  
  return noEinsteinDefect / (1 + 0.0000001 * noEinsteinDefect)