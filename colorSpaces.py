#all color spaces convertation   -   hosseinsamadi22@gmail.com    -   HosseinSamadi - 96463128
import cv2;

img=cv2.imread("pic.jpg")
window_name='image'

def showImage(cSpaceType,pic):
    cv2.namedWindow(cSpaceType, cv2.WINDOW_NORMAL)
    cv2.imshow(cSpaceType,pic)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

print("choose and input color space num:")
print("1)gray   2)HSV   3)HLS   4)CIE Lab\n5)RGB CIE   6)XYZ   7)YCrCb  8)YUV")
userInput = input("num : ")

showImage("orginal image",img)


grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY )
HSVimg = cv2.cvtColor(img, cv2.COLOR_RGB2HSV )
HLSimg = cv2.cvtColor(img, cv2.COLOR_RGB2HLS )
CIELab = cv2.cvtColor(img, cv2.COLOR_RGB2Lab )
RGBCIE = cv2.cvtColor(img, cv2.COLOR_RGB2Luv )
XYZ = cv2.cvtColor(img, cv2.COLOR_RGB2XYZ)
YCbCr = cv2.cvtColor(img, cv2.COLOR_RGB2YCrCb)
YUV = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)


def switcher(userInput):
    if userInput == "1":
        showImage("gray",grayimg)
 
    elif userInput == "2":
        for (name, chan) in zip(("H", "S", "V"), cv2.split(HSVimg)):
            showImage(name,chan)
 
    elif userInput == "3":
        return showImage("HLS",HLSimg)

    elif userInput == "4":
        return showImage("Lab",CIELab)
 
    elif userInput == "5":
        return showImage("RGBCIE",RGBCIE)

    elif userInput == "6":
        return showImage("XYZ",XYZ)
 
    elif userInput == "7":
        return showImage("YCbCr",YCbCr)

    elif userInput == "8":
        return showImage("YUV",YUV)
 
    else:
        print("Incorrect input")





switcher(userInput)

"""""
 در زیر آمده است cv2.cvtColorسینتکس تبدیل تمامی محیط های رنگ برای دستور گ  
 Color space conversion code string, e.g., 'RGB2GRAY'. The following codes are supported:
RGB2RGBA: add alpha channel to RGB and BGR image
RGBA2RGB: remove alpha channel from RGB and BGR image
RGB2BGRA, RGBA2BGR, BGRA2RGB, BGR2RGB, RGB2BGR, BGRA2RGBA, RGBA2BGRA: convert between RGB and BGR color spaces (with or without alpha channel)
RGB2GRAY, GRAY2BGR, GRAY2RGB, GRAY2BGRA, GRAY2RGBA, BGRA2GRAY, RGBA2GRAY: convert between RGB/BGR and grayscale
RGB2BGR565, BGR5652BGR, BGR5652RGB, BGRA2BGR565, RGBA2BGR565, BGR5652BGRA, BGR5652RGBA: convert between RGB/BGR and BGR565 (16-bit images)
GRAY2BGR565, BGR5652GRAY: convert between grayscale and BGR565 (16-bit images)
RGB2BGR555, BGR5552BGR, BGR5552RGB, BGRA2BGR555, RGBA2BGR555, BGR5552BGRA, BGR5552RGBA: convert between RGB/BGR and BGR555 (16-bit images)
GRAY2BGR555, BGR5552GRAY: convert between grayscale and BGR555 (16-bit images)
RGB2XYZ, XYZ2BGR, XYZ2RGB: convert between RGB/BGR and CIE XYZ
BGR2YCrCb, RGB2YCrCb, YCrCb2BGR, YCrCb2RGB: convert between RGB/BGR and luma-chroma (aka YCC)
BGR2YUV, RGB2YUV, YUV2BGR, YUV2RGB: convert between RGB/BGR and YUV
BGR2HSV, RGB2HSV, HSV2BGR, HSV2RGB, BGR2HSV_FULL, RGB2HSV_FULL, HSV2BGR_FULL, HSV2RGB_FULL: convert between RGB/BGR and HSV (hue saturation value)
BGR2HLS, RGB2HLS, HLS2BGR, HLS2RGB, BGR2HLS_FULL, RGB2HLS_FULL, HLS2BGR_FULL, HLS2RGB_FULL: convert between RGB/BGR and HLS (hue lightness saturation)
BGR2Lab, RGB2Lab, Lab2BGR, Lab2RGB, LBGR2Lab, LRGB2Lab, Lab2LBGR, Lab2LRGB: convert between RGB/BGR and CIE Lab
BGR2Luv, RGB2Luv, Luv2BGR, Luv2RGB, LBGR2Luv, LRGB2Luv, Luv2LBGR, Luv2LRGB: convert between RGB/BGR and CIE Luv
YUV2RGB_NV12, YUV2BGR_NV12, YUV2RGB_NV21, YUV2BGR_NV21, YUV420sp2RGB, YUV420sp2BGR, YUV2RGBA_NV12, YUV2BGRA_NV12, YUV2RGBA_NV21, YUV2BGRA_NV21, YUV420sp2RGBA, YUV420sp2BGRA, YUV2RGB_YV12, YUV2BGR_YV12, YUV2RGB_IYUV, YUV2BGR_IYUV, YUV2RGB_I420, YUV2BGR_I420, YUV420p2RGB, YUV420p2BGR, YUV2RGBA_YV12, YUV2BGRA_YV12, YUV2RGBA_IYUV, YUV2BGRA_IYUV, YUV2RGBA_I420, YUV2BGRA_I420, YUV420p2RGBA, YUV420p2BGRA, YUV2GRAY_420, YUV2GRAY_NV21, YUV2GRAY_NV12, YUV2GRAY_YV12, YUV2GRAY_IYUV, YUV2GRAY_I420, YUV420sp2GRAY, YUV420p2GRAY: YUV 4:2:0 family to RGB
YUV2RGB_UYVY, YUV2BGR_UYVY, YUV2RGB_Y422, YUV2BGR_Y422, YUV2RGB_UYNV, YUV2BGR_UYNV, YUV2RGBA_UYVY, YUV2BGRA_UYVY, YUV2RGBA_Y422, YUV2BGRA_Y422, YUV2RGBA_UYNV, YUV2BGRA_UYNV, YUV2RGB_YUY2, YUV2BGR_YUY2, YUV2RGB_YVYU, YUV2BGR_YVYU, YUV2RGB_YUYV, YUV2BGR_YUYV, YUV2RGB_YUNV, YUV2BGR_YUNV, YUV2RGBA_YUY2, YUV2BGRA_YUY2, YUV2RGBA_YVYU, YUV2BGRA_YVYU, YUV2RGBA_YUYV, YUV2BGRA_YUYV, YUV2RGBA_YUNV, YUV2BGRA_YUNV, YUV2GRAY_UYVY, YUV2GRAY_YUY2, YUV2GRAY_Y422, YUV2GRAY_UYNV, YUV2GRAY_YVYU, YUV2GRAY_YUYV, YUV2GRAY_YUNV: YUV 4:2:2 family to RGB
RGBA2mRGBA, mRGBA2RGBA: alpha premultiplication
RGB2YUV_I420, BGR2YUV_I420, RGB2YUV_IYUV, BGR2YUV_IYUV, RGBA2YUV_I420, BGRA2YUV_I420, RGBA2YUV_IYUV, BGRA2YUV_IYUV, RGB2YUV_YV12, BGR2YUV_YV12, RGBA2YUV_YV12, BGRA2YUV_YV12: RGB to YUV 4:2:0 family
BayerBG2BGR, BayerGB2BGR, BayerRG2BGR, BayerGR2BGR, BayerBG2RGB, BayerGB2RGB, BayerRG2RGB, BayerGR2RGB, BayerBG2GRAY, BayerGB2GRAY, BayerRG2GRAY, BayerGR2GRAY, BayerBG2BGRA, BayerGB2BGRA, BayerRG2BGRA, BayerGR2BGRA, BayerBG2RGBA, BayerGB2RGBA, BayerRG2RGBA, BayerGR2RGBA: Demosaicing
BayerBG2BGR_VNG, BayerGB2BGR_VNG, BayerRG2BGR_VNG, BayerGR2BGR_VNG, BayerBG2RGB_VNG, BayerGB2RGB_VNG, BayerRG2RGB_VNG, BayerGR2RGB_VNG: Demosaicing using Variable Number of Gradients
BayerBG2BGR_EA, BayerGB2BGR_EA, BayerRG2BGR_EA, BayerGR2BGR_EA, BayerBG2RGB_EA, BayerGB2RGB_EA, BayerRG2RGB_EA, BayerGR2RGB_EA: Edge-Aware Demosaicing
"""


