from PIL import Image
import os
import random

traits_path = './img_traits'

backgrounds = traits_path + './backgrounds'
chains = traits_path + './chains'
eyes = traits_path + './eyes'
headwears = traits_path + './headwear'
jesus = traits_path + './jesus'
outfits = traits_path + './outfits'


def create_random():
    backgrounds_choices = random.choice(os.listdir(backgrounds))
    chain_choices = random.choice(os.listdir(chains))
    eyes_choices = random.choice(os.listdir(eyes))
    headwears_choices = random.choice(os.listdir(headwears))
    jesus_choices = random.choice(os.listdir(jesus))
    outfits_choices = random.choice(os.listdir(outfits))

    background = Image.open(f'{backgrounds}/{backgrounds_choices}').convert("RGBA")
    im1 = Image.open(f'{jesus}/{jesus_choices}').convert("RGBA")
    im2 = Image.open(f'{outfits}/{outfits_choices}').convert("RGBA")
    im3 = Image.open(f'{chains}/{chain_choices}').convert("RGBA")
    im4 = Image.open(f'{headwears}/{headwears_choices}').convert("RGBA")
    im5 = Image.open(f'{eyes}/{eyes_choices}').convert("RGBA")

    # Create each composite
    com0 = Image.alpha_composite(background, im1)
    com1 = Image.alpha_composite(com0, im2)
    com2 = Image.alpha_composite(com1, im3)
    com3 = Image.alpha_composite(com2, im4)
    com4 = Image.alpha_composite(com3, im5)

    # Convert to RGB
    rgb_im = com4.convert('RGB')

    return rgb_im


def crop_to_size(img, width=400, height=400):
    width_img, height_img = img.size
    left = (width_img - width)/2
    right = (width_img + width)/2
    top = (height_img - height)/2
    bottom = (height_img + height)/2
    return img.crop((left, top, right, bottom))


def show_random(n):
    images = []
    for _ in range(n):
        img = create_random()
        images.append(img)
        img.show()
    return images


def test(crop=False, width=400, height=400, save=False):
    img = create_random()
    img.show()
    if crop:
        cropped = crop_to_size(img, width, height)
        cropped.show()
        if save:
            cropped.save('cropped.jpg')
    if save:
        img.save('test.jpg')


test(True, width=600, height=600, save=True)