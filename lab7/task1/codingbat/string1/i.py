def combo_string(a, b):
  longStr = a
  shortStr = b
  if len(b) > len(a):
    longStr = b
    shortStr = a
    
  return shortStr + longStr + shortStr