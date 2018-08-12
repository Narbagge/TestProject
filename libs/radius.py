import libs.arithmetic.add as add
import libs.arithmetic.mul as mul

def radius_squared(x, y):
  xs = mul.mulnum(x, x)
  ys = mul.mulnum(y, y)

  return add.addnum(xs, ys)