import sys
import binascii
import tkinter

data_dir = "data/"
paths = {
        'train_images' : data_dir + "train-images",
        'train_labels' : data_dir + "train-labels",
        'test_images' : data_dir + "test-images",
        'test_labels' : data_dir + "test-labels"
        }

def get_bytes_as_int(loc, count):
    return int.from_bytes(loc.read(count), byteorder="big")

def main():
    dataset = "train"
    if len(sys.argv) > 1:
        if sys.argv[1] in ["train", "test"]:
            dataset = sys.argv[1]
        else:
            print("I don't know what you want me to do :(")
            return 1

    images = open(paths[dataset + '_images'], 'rb')
    labels = open(paths[dataset + '_labels'], 'rb')
    """
    What our images file looks like:

     [offset] [type]          [value]          [description]
     0000     32 bit integer  0x00000803(2051) magic number
     0004     32 bit integer  60000            number of images
     0008     32 bit integer  28               number of rows
     0012     32 bit integer  28               number of columns
     0016     unsigned byte   ??               pixel
     0017     unsigned byte   ??               pixel
     ........
     xxxx     unsigned byte   ??               pixel
    """

    images_magic_number = get_bytes_as_int(images, 4)
    num_images = get_bytes_as_int(images, 4)
    num_rows = get_bytes_as_int(images, 4)
    num_cols = get_bytes_as_int(images, 4)

    labels_magic_number = get_bytes_as_int(labels, 4)
    num_labels = get_bytes_as_int(labels, 4)

    # sanity check
    assert num_labels == num_images:

    # images are 28x28 pixels, we should scale them up for tkinter
    scale = 10

    root = tkinter.Tk()
    photo = tkinter.PhotoImage(width=num_rows*scale, height=num_cols*scale)
    label = tkinter.Label(root, image=photo)
    label.grid()

    def show_next_char():
        nonlocal label

        vals = bytearray(images.read(num_rows*num_cols))
        print("Showing a {0}".format(get_bytes_as_int(labels, 1)))
        pixel = 0
        for row in range(num_rows):
            for col in range(num_cols):
                val = vals[pixel]
                color = "#{0}{1}{2}".format(val, val, val)
                horizontal_line = "{" + " ".join([color]*scale) + "}"
                photo.put(" ".join([horizontal_line]*scale), to=(col*scale,row*scale))
                pixel += 1

        label.grid_forget()
        label.destroy()

        label = tkinter.Label(root, image=photo)
        label.grid()

    root.bind("<Key>", lambda event: show_next_char())
    root.mainloop()
    return 0

if __name__ == "__main__":
    sys.exit(main())
