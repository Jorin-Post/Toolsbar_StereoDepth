import tkinter as tk
import cv2

BSg = 0
ming = 0
maxg = 0
Uniqg = 0
Dispg = 0
SpeckWg = 0
SpeckRg = 0
modeg = ""


def Sidebar(BS, min, max, Uniq, Disp, SpeckW, SpeckR, mode):
    global BSg
    global ming
    global maxg
    global Uniqg
    global Dispg
    global SpeckWg
    global SpeckRg
    global modeg
    BSg = BS
    ming = min
    maxg = max
    Uniqg = Uniq
    Dispg = Disp
    SpeckWg = SpeckW
    SpeckRg = SpeckR
    modeg = mode

    root = tk.Tk()
    root.geometry("150x800")

    def B1():
        global BSg
        BSg += 1
        l1_text.set("Bloksize: {}".format(BSg))

    def B2():
        global BSg
        BSg -= 1
        l1_text.set("Bloksize: {}".format(BSg))

    l1_text = tk.StringVar()
    l1_text.set("Bloksize: {}".format(BSg))
    l1 = tk.Label(root, textvariable=l1_text)
    l1.pack()
    b1 = tk.Button(root, text="+", command=B1)
    b1.pack(side=tk.TOP)
    b2 = tk.Button(root, text="-", command=B2)
    b2.pack(side=tk.TOP)

    def B3():
        global ming
        ming += 16
        l2_text.set("MinDisparity: {}".format(ming))

    def B4():
        global ming
        ming -= 16
        l2_text.set("MinDisparity: {}".format(ming))

    l2_text = tk.StringVar()
    l2_text.set("MinDisparity: {}".format(ming))
    l2 = tk.Label(root, textvariable=l2_text)
    l2.pack()
    b3 = tk.Button(root, text="+", command=B3)
    b3.pack(side=tk.TOP)
    b4 = tk.Button(root, text="-", command=B4)
    b4.pack(side=tk.TOP)

    def B5():
        global maxg
        maxg += 16
        l3_text.set("MaxDisparity: {}".format(maxg))

    def B6():
        global maxg
        maxg -= 16
        l3_text.set("MaxDisparity: {}".format(maxg))

    l3_text = tk.StringVar()
    l3_text.set("MaxDisparity: {}".format(maxg))
    l3 = tk.Label(root, textvariable=l3_text)
    l3.pack()
    b5 = tk.Button(root, text="+", command=B5)
    b5.pack(side=tk.TOP)
    b6 = tk.Button(root, text="-", command=B6)
    b6.pack(side=tk.TOP)

    def B7():
        global Uniqg
        Uniqg += 2
        l4_text.set("Uniqueness: {}".format(Uniqg))

    def B8():
        global Uniqg
        Uniqg -= 2
        l4_text.set("Uniqueness: {}".format(Uniqg))

    l4_text = tk.StringVar()
    l4_text.set("Uniqueness: {}".format(Uniqg))
    l4 = tk.Label(root, textvariable=l4_text)
    l4.pack()
    b7 = tk.Button(root, text="+", command=B7)
    b7.pack(side=tk.TOP)
    b8 = tk.Button(root, text="-", command=B8)
    b8.pack(side=tk.TOP)

    def B9():
        global Dispg
        Dispg += 1
        l5_text.set("Disp12MaxDiff: {}".format(Dispg))

    def B10():
        global Dispg
        Dispg -= 1
        l5_text.set("Disp12MaxDiff: {}".format(Dispg))

    l5_text = tk.StringVar()
    l5_text.set("Disp12MaxDiff: {}".format(Dispg))
    l5 = tk.Label(root, textvariable=l5_text)
    l5.pack()
    b9 = tk.Button(root, text="+", command=B9)
    b9.pack(side=tk.TOP)
    b10 = tk.Button(root, text="-", command=B10)
    b10.pack(side=tk.TOP)

    def B11():
        global SpeckWg
        SpeckWg += 1
        l6_text.set("SpeckleWindow: {}".format(SpeckWg))

    def B12():
        global SpeckWg
        SpeckWg -= 1
        l6_text.set("SpeckleWindow: {}".format(SpeckWg))

    l6_text = tk.StringVar()
    l6_text.set("SpeckleWindow: {}".format(SpeckWg))
    l6 = tk.Label(root, textvariable=l6_text)
    l6.pack()
    b11 = tk.Button(root, text="+", command=B11)
    b11.pack(side=tk.TOP)
    b12 = tk.Button(root, text="-", command=B12)
    b12.pack(side=tk.TOP)

    def B13():
        global SpeckRg
        SpeckRg += 10
        l7_text.set("SpeckleRange: {}".format(SpeckRg))

    def B14():
        global SpeckRg
        SpeckRg -= 10
        l7_text.set("SpeckleRange: {}".format(SpeckRg))

    l7_text = tk.StringVar()
    l7_text.set("SpeckleRange: {}".format(SpeckRg))
    l7 = tk.Label(root, textvariable=l7_text)
    l7.pack()
    b13 = tk.Button(root, text="+", command=B13)
    b13.pack(side=tk.TOP)
    b14 = tk.Button(root, text="-", command=B14)
    b14.pack(side=tk.TOP)

    def Men(cl):
        global modeg
        if cl == "SGBM":
            modeg = cv2.StereoSGBM_MODE_SGBM
        elif cl == "SGBM_3WAY":
            modeg = cv2.StereoSGBM_MODE_SGBM_3WAY
        elif cl == "HH":
            modeg = cv2.StereoSGBM_MODE_HH
        elif cl == "HH4":
            modeg = cv2.StereoSGBM_MODE_HH4

    l8 = tk.Label(root, text="Mode:")
    l8.pack(side=tk.TOP)
    options = ["SGBM", "SGBM_3WAY", "HH", "HH4"]
    clicked = tk.StringVar()
    clicked.set("SGBM")
    drop = tk.OptionMenu(root, clicked, *options, command=Men)
    drop.pack()
    root.mainloop()
    return BSg, ming, maxg, Uniqg, Dispg, SpeckWg, SpeckRg, modeg
