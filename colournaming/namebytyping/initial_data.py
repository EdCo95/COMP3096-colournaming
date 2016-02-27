import psycopg2
from PIL import Image
from os import path, pardir, environ
import random

base_path = path.join('static', 'namebytyping', 'images')

try:
    conn = psycopg2.connect("dbname='colournaming' user='{}' host='localhost' password='{}'".format(environ['DJANGO_USER'], environ['DJANGO_PASSWORD']))
except:
    print "I am unable to connect to the database"

cur = conn.cursor()

for i in range(1, 41):
    current_path = path.join(base_path, '{}.jpg'.format(i))
    I = Image.open(current_path)
    width, height = I.size

    current_path = path.join(pardir, pardir, current_path)

    cur.execute("""INSERT INTO namebytyping_image VALUES ({}, '', '{}', {}, {})""".format(i, current_path, width, height))

    patch_id = i
    radius = 20
    position_x = random.randint(radius, width - radius)
    position_y = random.randint(radius, height - radius)
    image_id = i
    cur.execute("""INSERT INTO namebytyping_patch VALUES ({}, {}, {}, {}, {})""".format(patch_id, radius, position_x, position_y, image_id))

conn.commit()