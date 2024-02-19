import requests
import shutil
from PIL import Image, ImageDraw, ImageFont
#from io import BytesIO
import os

#beatmap_id = 807850
#beatmap_id = 1114770
beatmap_id = 1948622
#bid = 1796301
b_cover_url = f"https://assets.ppy.sh/beatmaps/{beatmap_id}/covers/cover.jpg"
b_tl_url = f'https://b.ppy.sh/thumb/{beatmap_id}l.jpg'
b_info_before = requests.get(f'https://osu.ppy.sh/api/get_beatmaps?k=a1f72d1b74804700d59b5e66b1b42b7c0054ebe6&s={beatmap_id}').json()
bid = b_info_before[0]['beatmap_id']
b_info = requests.get(f'https://osu.ppy.sh/api/get_beatmaps?k=a1f72d1b74804700d59b5e66b1b42b7c0054ebe6&b={bid}').json()

font1 = ImageFont.truetype("arial.ttf", 30)
font2 = ImageFont.truetype("arial.ttf", 25)
font3 = ImageFont.truetype("arial.ttf", 16)
gradefont = ImageFont.truetype("arial.ttf", 40)
font3 = ImageFont.truetype("jpfont.otf", 16)

beatmap_title = b_info[0]['title']
beatmap_title_unicode = b_info[0]['title_unicode']
beatmap_artist = b_info[0]['artist']
beatmap_artist_unicode = b_info[0]['artist_unicode']
beatmap_creator = b_info[0]['creator']
beatmap_version = b_info[0]['version']
beatmap_cs = b_info[0]['diff_size']
beatmap_hp = b_info[0]['diff_drain']
beatmap_od = b_info[0]['diff_overall']
beatmap_ar = b_info[0]['diff_approach']
beatmap_bpm = b_info[0]['bpm']

beatmap_difficultyrating = b_info[0]['difficultyrating']
beatmap_difficultyrating = float(beatmap_difficultyrating)
beatmap_diff = round(beatmap_difficultyrating, 2)
print('\n', beatmap_title,'\n', beatmap_artist,'\n', beatmap_creator,'\n', beatmap_version,'\n', beatmap_diff, '\n')
beatmap_diff = str(beatmap_diff)

#beatmap cover 900x250
path = f'cover{beatmap_id}.png'
r = requests.get(b_cover_url, stream=True)
if r.status_code == 200:
    with open(path, 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f) 
        print('Image cover saved!')
#beatmao second 160x120
path = f'tl{beatmap_id}.png'
r = requests.get(b_tl_url, stream=True)
if r.status_code == 200:
    with open(path, 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f) 
        print('Image tl saved!')
#beatmap cover end
print('\nBefore saved:')
#dark box
img = Image.open(f'cover{beatmap_id}.png')
img = img.convert("RGBA")
print('Image RGBA')
overlay = Image.new('RGBA', img.size, (0, 0, 0)+(0,))
draw = ImageDraw.Draw(overlay)
draw.rectangle(((20, 60), (880, 190)), fill=(0, 0, 0)+(int(255 * .5),))
print('Draw rectangle')
img = Image.alpha_composite(img, overlay)
img = img.convert("RGB")
img.save(f'dark_b{beatmap_id}.png')
print('Saved darked image')

#dark box 2
img = Image.open(f'dark_b{beatmap_id}.png')
img = img.convert("RGBA")
print('Image RGBA')
overlay = Image.new('RGBA', img.size, (0, 0, 0)+(0,))
draw = ImageDraw.Draw(overlay)
draw.rectangle(((20, 35), (880, 60)), fill=(0, 0, 0)+(int(255 * .7),))
print('Draw rectangle')
img = Image.alpha_composite(img, overlay)
img = img.convert("RGB")
img.save(f'dark_b{beatmap_id}.png')
print('Saved darked image 2')

#dark box 3
img = Image.open(f'dark_b{beatmap_id}.png')
img = img.convert("RGBA")
print('Image RGBA')
overlay = Image.new('RGBA', img.size, (0, 0, 0)+(0,))
draw = ImageDraw.Draw(overlay)
draw.rectangle(((20, 190), (880, 215)), fill=(0, 0, 0)+(int(255 * .7),))
print('Draw rectangle')
img = Image.alpha_composite(img, overlay)
img = img.convert("RGB")
img.save(f'dark_b{beatmap_id}.png')
print('Saved darked image 3')

#draw text&image
img = Image.open(f'dark_b{beatmap_id}.png')
d = ImageDraw.Draw(img)

cimg = Image.open(f'tl{beatmap_id}.png')
img.paste(cimg, (25, 65))

print('Pasting text')
d.text((225, 70), beatmap_title, fill=(255, 255, 255), font=font1)
d.text((225, 105), f"{beatmap_artist} // {beatmap_creator}", fill=(255, 255, 255), font=font2)
d.text((225, 135), beatmap_version, fill=(255, 255, 255), font=font2)
#d.text((192, 103), "S", fill=(255, 255, 170), font=gradefont)
#d.text((190, 100), "S", fill=(250, 250, 0), font=gradefont)
d.text((190, 100), "D", fill=(255, 0, 0), font=gradefont)
d.text((630, 160), f'{beatmap_diff}*', fill=(255, 255, 255), font=font2)
d.text((25, 36), f'CS: {beatmap_cs}', fill=(255, 255, 255), font=font3)
d.text((90, 36), f'AR: {beatmap_ar}', fill=(255, 255, 255), font=font3)
d.text((155, 36), f'OD: {beatmap_od}', fill=(255, 255, 255), font=font3)
d.text((220, 36), f'HP: {beatmap_hp}', fill=(255, 255, 255), font=font3)
d.text((280, 36), f'BPM: {beatmap_bpm}', fill=(255, 255, 255), font=font3)
d.text((25, 190), f'{beatmap_title_unicode} - {beatmap_artist_unicode}', fill=(255, 255, 255), font=font3)


print('Pasting stars')
#stars
star = Image.new('RGB', (30, 10), (255, 255, 255))
starmiddle = Image.new('RGB', (30, 10), (170, 170, 170))
nostar = Image.new('RGB', (30, 10), (100, 100, 100))

#draw stars
a1 = 0
b1 = 225
b2 = 170
while a1 < int(beatmap_difficultyrating):
    img.paste(star, (b1, b2))
    b1 = b1 + 40
    a1 = a1 + 1
    print('star', a1)
c1 = round(beatmap_difficultyrating - 1, 0)
print('c1', c1)
if c1 < beatmap_difficultyrating:
    img.paste(starmiddle, (b1, b2))
    b1 = b1 + 40
    a1 = a1 + 1
    print('starmiddle', a1)
while a1 < 10:
    img.paste(nostar, (b1, b2))
    b1 = b1 + 40
    a1 = a1 + 1
    print('nostar', a1)

img.save(f'map {beatmap_id} {beatmap_version}.png')
print('Deleting trash images.')
os.remove(f'cover{beatmap_id}.png')
print('Deleting trash images..')
os.remove(f'dark_b{beatmap_id}.png')
print('Deleting trash images...')
os.remove(f'tl{beatmap_id}.png')
print('Image done!')