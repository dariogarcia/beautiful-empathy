from happytransformer import HappyWordPrediction

#Load text
filename = '../Questions - Sheet1.tsv'
with open(filename) as file:
    lines = file.readlines()
    lines = [line.split('.')[0] for line in lines]

#Process
#happy_wp_roberta = HappyWordPrediction("ROBERTA", "roberta-large")
#happy_wp_albert = HappyWordPrediction("ALBERT", "albert-xxlarge-v2")

happy_wp = HappyWordPrediction()
for l in lines:
    print(l)
    results = happy_wp.predict_mask(l, top_k = 6)
    for res in results:
        print(res.token) 
    #print(result[0].score)     
