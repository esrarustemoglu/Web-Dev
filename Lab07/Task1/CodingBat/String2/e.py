def end_other(a, b):
  if(len(a) > len(b)):
    if a.lower().endswith(b.lower()):
      return True
  else:
    if b.lower().endswith(a.lower()):
      return True
  return False