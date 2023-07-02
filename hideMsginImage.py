from stegano import lsb 
secret = lsb.hide("Sunflower.png","This is very cool") 
secret.save("New_Sunflower.png")