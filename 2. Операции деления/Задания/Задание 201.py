sec = int(input())
hours =sec//3600
mins =sec%3600//60
secs =sec%60
print(f"{hours}:{mins}:{secs}")