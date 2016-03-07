import psycopg2
from PIL import Image, ImageDraw
from os import path, pardir, environ
import random

base_path = path.join('static', 'namebytyping', 'images')

try:
    conn = psycopg2.connect("dbname='colournaming' user='{}' host='localhost' password='{}'".format(environ['DJANGO_USER'], environ['DJANGO_PASSWORD']))
except:
    print "I am unable to connect to the database"

cur = conn.cursor()

coords = open("patch_coords.txt", "r")

for i in range(1, 41):
    current_path = path.join(base_path, '{}.jpg'.format(i))
    I = Image.open(current_path)
    width, height = I.size
    draw = ImageDraw.Draw(I)

    current_path = path.join(pardir, pardir, current_path)

    cur.execute("""INSERT INTO namebytyping_image VALUES ({}, '', '{}', {}, {})""".format(i, current_path, width, height))

    patch_id = i
    patch_line = coords.readline()
    coords_list = patch_line.split()
    position_x = coords_list[2]
    position_y = coords_list[4]
    radius = 20

    draw.ellipse((int(position_x) - radius, int(position_y) - radius, int(position_x) + radius, int(position_y) + radius))
    filename = "static/namebytyping/images/new/" + str(i) + ".png"
    I.save(filename, "png")

    image_id = i
    cur.execute("""INSERT INTO namebytyping_patch VALUES ({}, {}, {}, {}, {})""".format(patch_id, radius, position_x, position_y, image_id))

conn.commit()

secondary_path = path.join('static', 'namebytyping', 'images_original')
coords = open("patch_coords.txt", "r")
