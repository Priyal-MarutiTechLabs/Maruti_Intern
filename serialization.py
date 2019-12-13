import pickle

#example_dict = {"1":0,"2":2,"3":3,"4":6}

picke_out = open("dict.pickle","wb")
example_dict= "hi"
pickle.dumps(example_dict,picke_out)
picke_out.close()