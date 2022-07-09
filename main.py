import pywhatkit
from datetime import datetime, timedelta
import csv
import asyncio

# phone_number = "+918828386615"

Image_path= "Images/index.jpeg"


async def main():
    count = 0

    with open('index.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)
            if count > 0:
                date = datetime.now() + timedelta(seconds=90)
                hours = date.strftime("%H")
                minutes = date.strftime("%M")
                print(hours)
                print(minutes)
                name = row[0]
                phone_number = row[1]
                message= f'''*IIT Bombay* collaborated with *Cantilever Labs* for the placement training of 2023 batch. This is the 4th collaboration in last 3 years & we at Cantilever Labs are both Proud & Humbled.
                
*Be a MENTOR at Cantilever Labs*. Join us in shaping the dreams of these young kids who will be shaping the world tomorrow.

“ Which is more important The Journey or Destination ” asked Tiny Dragon

“ The Company ” said the Big Panda

It’s your chance to be “ *The Company*”. 

Here is the link explaining all about the “ Mentorship & IIT Bombay” - 
https://bit.ly/CantileverIITBombayMentorship

Thank you
                '''
                pywhatkit.sendwhats_image("+91" + phone_number, Image_path, message, 15, True, 2)

            count += 1

asyncio.run(main())

