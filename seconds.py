all_seconds = int(input()) hours = all_seconds // 3600 minutes = (all_seconds % 3600) // 60 seconds = all_seconds % 60 
print(f"{hours:02}:{minutes:02}:{seconds:02}")
