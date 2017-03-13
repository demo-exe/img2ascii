from PIL import Image
import numpy as np

charset = list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz#%^&* .\'')
charset_op = list()
def GenChars():
    with open("chars.txt", "w") as f:
        for x in charset:
            f.write(x)


def CalcOp():
    im = Image.open('charset.png')

    n = 0
    char_op = list()
    for x in charset:
        ch = im.crop((n*8,0,(n+1)*8,13))
        ch.save('chars/' + str(n) + '.png', "PNG")

        data = np.array(ch)
        data = np.average(data,axis=2)
        data = np.average(data)
        char_op.append(data)
        
        n+=1
    co = np.array(char_op)
    co = Normalize(255-co)

    return co
    
def Normalize(nparr):
    mi = min(nparr)
    ma = max(nparr)
    ret = (nparr-mi)/(ma-mi)
    return ret


#generated stuff
char_op = np.array(
      [ 0.76493754,  0.60622486,  0.60364175,  0.59669701,  0.63963582,
        0.6025831 ,  0.80224434,  0.41740419,  0.86377303,  0.79966123,
        0.64484438,  0.87969511,  0.58602583,  0.82206225,  0.71882278,
        0.59504552,  0.75181029,  0.72161762,  0.57183993,  0.45805632,
        0.70874444,  0.49100148,  0.75325005,  0.77874232,  0.7506246 ,
        0.69328816,  0.85555791,  0.81698073,  0.67228456,  0.52720728,
        0.6225704 ,  0.57709083,  0.82710142,  0.65610841,  0.50908321,
        0.66673724,  0.71111582,  0.84475969,  0.50789752,  0.79995765,
        0.70806691,  0.65759051,  0.78124074,  0.76070294,  0.4572094 ,
        0.54787212,  0.7349566 ,  0.48570824,  0.82011433,  0.63849248,
        0.65678594,  0.81084057,  0.76862164,  0.43480838,  0.5611264 ,
        0.55684946,  0.61528689,  0.45001059,  0.70806691,  0.59796739,
        0.59665467,  0.63980521,  0.80923142,  0.82862587,  0.36485285,
        1.        ,  0.33161126,  0.        ,  0.12466653,  0.12060131])
        
def SelectClosest(inp):
    l = abs(char_op-inp)
    return np.where(l == min(l))[0][0]





