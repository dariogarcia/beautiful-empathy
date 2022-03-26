class Color:
    def __init__(self, c_id, c_hex, coordinates):
         self.id = c_id
         self.hex = c_hex
         self.coords = coordinates
         if c_id > 31:
             self.text_col = (0,0,0)
         else:
             self.text_col = (255,255,255)
         self.player_name = None
         self.in_use = False

def get_initial_colors():
    colors = {
        -1:Color(-1,"#ffffff",(0,0)),
        1:Color(1,"#6b006b",(302,33)),
        2:Color(2,"#35006b",(416,102)), 
        3:Color(3,"#07076a",(467,205)) ,
        4:Color(4,"#00356b",(466,325)) ,
        5:Color(5,"#006b6b",(405,425)) ,
        6:Color(6,"#006b35",(302,483)) ,
        7:Color(7,"#005500",(188,484)) ,
        8:Color(8,"#4f6b00",(79,423)) ,
        9:Color(9,"#6b6b00",(21,325)) ,
        10:Color(10,"#6b3500",(25,180)), 
        11:Color(11,"#6b0000",(72,100)) ,
        12:Color(12,"#6b0035",(188,33)) ,
        13:Color(13,"#9b009b",(295,66)) ,
        14:Color(14,"#4d009b",(389,125)) ,
        15:Color(15,"#0b0b9a",(430,207)) ,
        16:Color(16,"#004d9b",(431,301)) ,
        17:Color(17,"#009b9b",(377,398)) ,
        18:Color(18,"#009b4d",(295,444)) ,
        19:Color(19,"#009b00",(190,444)) ,
        20:Color(20,"#729b00",(103,394)) ,
        21:Color(21,"#9b9b00",(55,306)) ,
        22:Color(22,"#9b4d00",(55,219)) ,
        23:Color(23,"#9b0000",(100,125)) ,
        24:Color(24,"#9b004d",(190,66)) ,
        25:Color(25,"#ce00ce",(286,103)) ,
        26:Color(26,"#6700ce",(352,145)) ,
        27:Color(27,"#0f0fcd",(392,209)) ,
        28:Color(28,"#0067ce",(396,284)) ,
        29:Color(29,"#00cece",(358,360)) ,
        30:Color(30,"#00ce67",(278,407)) ,
        31:Color(31,"#00ce00",(207,405)) ,
        32:Color(32,"#98ce00",(128,360)) ,
        33:Color(33,"#cece00",(88,290)) ,
        34:Color(34,"#ce6700",(95,208)) ,
        35:Color(35,"#ce0000",(135,145)) ,
        36:Color(36,"#ce0067",(205,110)) ,
        37:Color(37,"#fa08fb",(275,140)) ,
        38:Color(38,"#8000ff",(329,175)) ,
        39:Color(39,"#1313fe",(355,220)) ,
        40:Color(40,"#0080ff",(355,290)) ,
        41:Color(41,"#00ffff",(330,340)) ,
        42:Color(42,"#00ff80",(280,370)) ,
        43:Color(43,"#42ff42",(210,370)) ,
        44:Color(44,"#bdff00",(155,335)) ,
        45:Color(45,"#ffff00",(130,280)) ,
        46:Color(46,"#ff8000",(130,230)) ,
        47:Color(47,"#ff0000",(155,180)) ,
        48:Color(48,"#ff0080",(220,140)) ,
        49:Color(49,"#ff86ff",(263,180)) ,
        50:Color(50,"#c286ff",(305,200)) ,
        51:Color(51,"#8f8ffe",(325,245)) ,
        52:Color(52,"#86c2ff",(325,280)) ,
        53:Color(53,"#86ffff",(300,315)) ,
        54:Color(54,"#86ffc2",(265,335)) ,
        55:Color(55,"#7fff7f",(225,335)) ,
        56:Color(56,"#dfff86",(185,315)) ,
        57:Color(57,"#ffff86",(170,280)) ,
        58:Color(58,"#ffc286",(165,244)) ,
        59:Color(59,"#ff8686",(190,200)) ,
        60:Color(60,"#ff86c2",(220,175)) ,
        61:Color(61,"#ffc6ff",(255,217)) ,
        62:Color(62,"#e2c6ff",(280,228)) ,
        63:Color(63,"#cacafe",(290,245)) ,
        64:Color(64,"#c6e2ff",(288,270)) ,
        65:Color(65,"#c6ffff",(280,291)) ,
        66:Color(66,"#c6ffe2",(257,302)) ,
        67:Color(67,"#c0ffc0",(225,307)) ,
        68:Color(68,"#f0ffc6",(210,292)) ,
        69:Color(69,"#ffffc6",(203,268)) ,
        70:Color(70,"#ffe2c6",(203,248)) ,
        71:Color(71,"#ffc6c6",(215,225)) ,
        72:Color(72,"#ffc6e2",(230,210))
    }
    return colors

def get_initial_edges():
    edges = [
        (1,2), 
        (1,13), 
        (2,3), 
        (2,14), 
        (3,4), 
        (3,15), 
        (4,5), 
        (4,16), 
        (5,6), 
        (5,17), 
        (6,7), 
        (6,18), 
        (7,8), 
        (7,19), 
        (8,9), 
        (8,20), 
        (9,10), 
        (9,21), 
        (10,11), 
        (10,22), 
        (11,12), 
        (11,23), 
        (12,1),
        (12,24),
        (13,14), 
        (13,25), 
        (14,15), 
        (14,26), 
        (15,16), 
        (15,27), 
        (16,17), 
        (16,28), 
        (17,18), 
        (17,29), 
        (18,19), 
        (18,30), 
        (19,20), 
        (19,31), 
        (20,21), 
        (20,32), 
        (21,22), 
        (21,33), 
        (22,23), 
        (22,34), 
        (23,24), 
        (23,35), 
        (24,13), 
        (24,36),
        (25,26), 
        (25,37), 
        (26,27), 
        (26,38), 
        (27,28), 
        (27,39), 
        (28,29), 
        (28,40), 
        (29,30), 
        (29,41), 
        (30,31), 
        (30,42), 
        (31,32), 
        (31,43), 
        (32,33), 
        (32,44), 
        (33,34), 
        (33,45), 
        (34,35), 
        (34,46), 
        (35,36), 
        (35,47), 
        (36,25), 
        (36,48), 
        (37,38), 
        (37,49), 
        (38,39), 
        (38,50), 
        (39,40), 
        (39,51), 
        (40,41), 
        (40,52), 
        (41,42), 
        (41,53), 
        (42,43), 
        (42,54), 
        (43,44), 
        (43,55), 
        (44,45), 
        (44,56), 
        (45,46), 
        (45,57), 
        (46,47), 
        (46,58), 
        (47,48), 
        (47,59), 
        (48,37), 
        (48,60), 
        (49,50), 
        (49,61), 
        (50,51), 
        (50,62), 
        (51,52), 
        (51,63), 
        (52,53), 
        (52,64), 
        (53,54), 
        (53,65), 
        (54,55), 
        (54,66), 
        (55,56), 
        (55,67), 
        (56,57), 
        (56,68), 
        (57,58), 
        (57,69), 
        (58,59), 
        (58,70), 
        (59,60), 
        (59,71), 
        (60,49), 
        (60,72), 
        (61,62), 
        (62,63), 
        (63,64), 
        (64,65), 
        (65,66), 
        (66,67), 
        (67,68), 
        (68,69), 
        (69,70), 
        (70,71), 
        (71,72), 
        (72,61),
###External border edges
        (1,3),
        (1,4),
        (1,5),
        (1,6),
        (1,7),
        (1,8),
        (1,9),
        (1,10),
        (1,11),
        (2,4),
        (2,5),
        (2,6),
        (2,7),
        (2,8),
        (2,9),
        (2,10),
        (2,11),
        (3,5),
        (3,6),
        (3,7),
        (3,8),
        (3,9),
        (3,10),
        (3,11),
        (4,6),
        (4,7),
        (4,8),
        (4,9),
        (4,10),
        (4,11),
        (5,7),
        (5,8),
        (5,9),
        (5,10),
        (5,11),
        (6,8),
        (6,9),
        (6,10),
        (6,11),
        (7,9),
        (7,10),
        (7,11),
        (8,10),
        (8,11),
        (9,11),
###Internal border edges
        (61,63),
        (61,64),
        (61,65),
        (61,66),
        (61,67),
        (61,68),
        (61,69),
        (61,70),
        (61,71),
        (62,64),
        (62,65),
        (62,66),
        (62,67),
        (62,68),
        (62,69),
        (62,70),
        (62,71),
        (63,65),
        (63,66),
        (63,67),
        (63,68),
        (63,69),
        (63,70),
        (63,71),
        (64,66),
        (64,67),
        (64,68),
        (64,69),
        (64,70),
        (64,71),
        (65,67),
        (65,68),
        (65,69),
        (65,70),
        (65,71),
        (66,68),
        (66,69),
        (66,70),
        (66,71),
        (67,69),
        (67,70),
        (67,71),
        (68,70),
        (68,71),
        (69,71)
    ]
    return edges

