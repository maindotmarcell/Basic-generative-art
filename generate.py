from sys import meta_path
from PIL import Image
import random
import json

#global variables
taken_combos = []

def getRand():
    return random.randint(1,3)

def getNums():
    nums = []
    for i in range(5):
        nums.append(str(getRand()))
    return nums

def generate_image(id):
    nums = getNums()
    combo = ''.join(nums)
    while combo in taken_combos or combo == '':
        nums = getNums()
        combo = ''.join(nums)

    img1 = Image.open(f"./Layers/BG{nums[0]}.png")
    img2 = Image.open(f"./Layers/Head.png")
    intermediate = Image.alpha_composite(img1,img2)
    img3 = Image.open(f"./Layers/Mouth{nums[1]}.png")
    intermediate = Image.alpha_composite(intermediate, img3)
    img4 = Image.open(f"./Layers/Nose{nums[2]}.png")
    intermediate = Image.alpha_composite(intermediate, img4)
    img5 = Image.open(f"./Layers/Eyes{nums[3]}.png")
    intermediate = Image.alpha_composite(intermediate, img5)
    img6 = Image.open(f"./Layers/Hair{nums[4]}.png")
    intermediate = Image.alpha_composite(intermediate, img6)

    meta = {
        "image": f"final{id}.png",
        "attributes": [
            {
                "BG": f"{nums[0]}",
                "Mouth": f"{nums[1]}",
                "Nose": f"{nums[2]}",
                "Eyes": f"{nums[3]}",
                "Hair": f"{nums[4]}",
                "rarity": 0.5
            }
        ]
    }

    meta_json = json.dumps(meta)
    with open(f'./output/final{id}.json', 'w') as outfile:
        outfile.write(meta_json)

    intermediate.save(f'./output/final{id}.png')

    taken_combos.append(combo)


def generate_collection():
    for i in range(100):
        generate_image(str(i))

generate_collection()
