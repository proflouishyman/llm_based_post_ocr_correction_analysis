with open ("/home/sbacker2/projects/post_ocr_correction/data/chap_text.txt", "r") as in_file:
    text = in_file.read()
    text_list = text.split("**BREAK_HERE**")
    counter = 0 
    for entry in text_list:
        with open("/home/sbacker2/projects/post_ocr_correction/data/chap_test/{}.txt".format(counter), "w") as out_file:
            out_file.write(entry)
        counter = counter + 1
