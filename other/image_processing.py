from skimage import io, transform

img = io.imread(r"C:\Users\29241\Desktop\QASystemOnLawKG\static\images\首页法官锤.png")
resized_img = transform.resize(img, (4000, 6000))
io.imsave(r"C:\Users\29241\Desktop\QASystemOnLawKG\static\images\首页法官锤1.png", resized_img)


