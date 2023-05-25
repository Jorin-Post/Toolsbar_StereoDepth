import cv2
import numpy as np
import SideBar


def initCam():
    # Open the webcam with cv2 in a view window with 1280 * 1024 resolution
    cap1 = cv2.VideoCapture(0, cv2.CAP_MSMF)
    cap1.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap1.set(cv2.CAP_PROP_FRAME_HEIGHT, 1024)
    cap2 = cv2.VideoCapture(1, cv2.CAP_MSMF)
    cap2.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap2.set(cv2.CAP_PROP_FRAME_HEIGHT, 1024)
    return cap1, cap2


def downsample_image(image, reduce_factor):
    for i in range(0, reduce_factor):
        # Check if image is color or grayscale
        if len(image.shape) > 2:
            row, col = image.shape[:2]
        else:
            row, col = image.shape
        image = cv2.pyrDown(image, dstsize=(col // 2, row // 2))
    return image


capL, capR = initCam()

##### Stereo camera matrix #####
cv_file = cv2.FileStorage()
cv_file.open("stereoMap.xml", cv2.FileStorage_READ)
stereoMapL_x = cv_file.getNode("stereoMapL_x").mat()
stereoMapL_y = cv_file.getNode("stereoMapL_y").mat()
stereoMapR_x = cv_file.getNode("stereoMapR_x").mat()
stereoMapR_y = cv_file.getNode("stereoMapR_y").mat()
Q = cv_file.getNode("q").mat()

#### init parameters ####
# More info: https://docs.opencv.org/3.4/d2/d85/classcv_1_1StereoSGBM.html#ad985310396dd4d95a003b83811bbc138a0f746667febe92e1189e924c40752660
BS = 5
min_disp = -1
max_disp = 31
Uniq = 0
Disp = 0
SpeckW = 0
SpeckR = 0
mode = cv2.StereoSGBM_MODE_SGBM

while True:
    ret1, imgL = capL.read()
    ret2, imgR = capR.read()

    # Rectifies image frames
    imgR = cv2.remap(
        imgR, stereoMapR_x, stereoMapR_y, cv2.INTER_LANCZOS4, cv2.BORDER_CONSTANT, 0
    )
    imgL = cv2.remap(
        imgL, stereoMapL_x, stereoMapL_y, cv2.INTER_LANCZOS4, cv2.BORDER_CONSTANT, 0
    )

    imgL = downsample_image(imgL, 1)
    imgR = downsample_image(imgR, 1)
    imgLgray = cv2.cvtColor(imgL, cv2.COLOR_BGR2GRAY)
    imgRgray = cv2.cvtColor(imgR, cv2.COLOR_BGR2GRAY)

    # While loop is running, press key p to open the Sidebar. Key my needs to be pressed more than once
    if cv2.waitKey(1) & 0xFF == ord("p"):
        BS, min_disp, max_disp, Uniq, Disp, SpeckW, SpeckR, mode = SideBar.Sidebar(
            BS, min_disp, max_disp, Uniq, Disp, SpeckW, SpeckR, mode
        )

    # Create parameters disparity map
    num_disp = max_disp - min_disp
    stereo = cv2.StereoSGBM_create(
        minDisparity=min_disp,
        numDisparities=num_disp,
        blockSize=BS,
        uniquenessRatio=Uniq,
        speckleWindowSize=SpeckW,
        speckleRange=SpeckR,
        disp12MaxDiff=Disp,
        P1=8 * 3 * BS**2,
        P2=32 * 3 * BS**2,
        mode=mode,
    )

    # Compute disparity map
    disparity_map = stereo.compute(imgLgray, imgRgray)

    # change disparity map to magma colormap
    dmap = cv2.normalize(
        src=disparity_map,
        dst=disparity_map,
        beta=0,
        alpha=255,
        norm_type=cv2.NORM_MINMAX,
    )
    dmap = np.uint8(dmap)
    dmap = cv2.applyColorMap(dmap, cv2.COLORMAP_MAGMA)

    cv2.imshow("imgL", imgL)
    cv2.imshow("imgR", imgR)
    cv2.imshow("Dmap", dmap)

    # Press q key to exit program
    if cv2.waitKey(1) & 0xFF == ord("q"):
        capL.release()
        capR.release()
        cv2.destroyAllWindows()
        break
