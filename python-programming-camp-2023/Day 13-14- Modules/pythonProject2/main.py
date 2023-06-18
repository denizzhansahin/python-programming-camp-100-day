from rembg import remove

input_path = "image.jpeg"
output_path = "output.png"

with open(input_path,'rb') as i:
    with open(output_path,'wb') as o:
        input_file = i.read()
        output_path = remove(input_file)
        o.write(output_path)