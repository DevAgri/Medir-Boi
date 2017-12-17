import argparse
import cv2
from math import sqrt
from scipy.spatial import distance as dist

def click_and_crop(event, x, y, flags, param):
    global refPt, cropping


    if event == cv2.EVENT_LBUTTONDOWN:
        refPt.append((x, y))


image = cv2.imread('boi6.jpg')
#cv2.namedWindow('JANELA1', cv2.WINDOW_GUI_NORMAL)
image1 = cv2.resize(image, (500,500 ))
#cv2.namedWindow("image")
cv2.setMouseCallback("image", click_and_crop)

print(image.shape)
while True:

    refPt = []
    #cv2.imshow("JANELA1", image)
    cv2.setMouseCallback("image", click_and_crop)
    key = cv2.waitKey()# & 0xFF

    if key == 99:#ord("c"):
        cv2.line(image1, (refPt[0]), (refPt[1]), (0, 255, 0), 5, cv2.LINE_AA)
        compBoi = dist.euclidean(refPt[0], refPt[1])
        print('compBoi:',compBoi)


    elif key == 108:#ord("l"):
        cv2.line(image1, (refPt[0]), (refPt[1]), (0, 255, 0), 5, cv2.LINE_AA)
        largBoi = dist.euclidean(refPt[0], refPt[1])
        print('largBoi:',largBoi)

    elif key == 116:#ord("t"):
        cv2.line(image1, (refPt[0]), (refPt[1]), (0, 255, 0), 5, cv2.LINE_AA)
        toraxBoi = dist.euclidean(refPt[0], refPt[1])
        print('largBoi:',toraxBoi)


    elif key == 98:#ord("b"):
        cv2.line(image1, (refPt[0]), (refPt[1]), (0, 255, 0), 5, cv2.LINE_AA)
        baseCocho = dist.euclidean(refPt[0], refPt[1])
        print('baseCocho:',baseCocho)

    elif key == 97:#ord("a"):
        cv2.line(image1, (refPt[0]), (refPt[1]), (0, 255, 0), 5, cv2.LINE_AA)
        altCocho = dist.euclidean(refPt[0], refPt[1])
        print('altCocho:',altCocho)


    elif key == 115:# ord("s"):
        print('sair')
        break
    cv2.imshow("image", image1)



cv2.destroyAllWindows()