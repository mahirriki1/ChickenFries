def missing_char(str, n):
  if n<len(str)-1:
    return str[0:n]+str[n+1:]
  return str[0:n]
