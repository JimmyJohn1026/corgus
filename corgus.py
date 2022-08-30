from PIL import Image


def main():
    file = input("Image filename: ")
    im = Image.open(file)

#    # resize image to be no larger than 255
#    if im.size[0] >= 256:
#        im.resize((255, im.size[1]))
#    if im.size[1] >= 256:
#        im.resize((im.size[0], 255))
    im.thumbnail((255, 255))

    # make it pure rgb
    rgb_im = im.convert("RGB")

    # make the hex file
    h = open(file + ".txt", "w")

    # write the width, height, and bits per pixel
    h.write("%02x" % rgb_im.size[0])
    h.write("%02x" % rgb_im.size[1])
    h.write("18")


    # write the rgb hex code for each pixel
    for y in range(0, rgb_im.size[1]):
        for x in range(0, rgb_im.size[0]):
            h.write("%02x%02x%02x" % rgb_im.getpixel((x-1, y-1))) # use magic to convert rgb tuplet to hex
#    print(rgb_im.size)
#    print("%02x%02x%02x" % rgb_im.getpixel((32, 32)))
    h.close()

if __name__ == "__main__":
    main()
