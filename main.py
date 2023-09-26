import csv, os
os.system('clear')
with open ('100MostStreamedSongs.csv') as csv_file:
  read_file = csv.DictReader(csv_file)
  
  for i in read_file:
    art = f"{i['Artist(s)']}/"
    song = i['Song']
    print(f'{art}, {song}')
    if os.path.exists(art):
      pass
    else:
      os.mkdir(art)
      
    joining = os.path.join(art, song)
    song_file = open(joining, 'w')
    song_file.write('')
    song_file.close()


