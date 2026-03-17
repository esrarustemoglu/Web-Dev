def cat_dog(str):
  count_cat = 0
  count_dog = 0
  if(len(str) > 2):
    for i in range(len(str)-2):
      if str[i] == "c" and str[i+1] == "a" and str[i+2] == "t":
        count_cat += 1
      elif str[i] == "d" and str[i+1] == "o" and str[i+2] == "g":
        count_dog += 1
  if count_cat == count_dog:
    return True
  return False