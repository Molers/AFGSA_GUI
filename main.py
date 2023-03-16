"""
本代码由[Tkinter布局助手]生成
当前版本:3.1.2
官网:https://www.pytk.net/tkinter-helper
QQ交流群:788392508
"""
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import os

"""
全局通用函数
"""
# 自动隐藏滚动条
def scrollbar_autohide(bar,widget):
    def show():
        bar.lift(widget)
    def hide():
        bar.lower(widget)
    hide()
    widget.bind("<Enter>", lambda e: show())
    bar.bind("<Enter>", lambda e: show())
    widget.bind("<Leave>", lambda e: hide())
    bar.bind("<Leave>", lambda e: hide())

class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_tabs_lfaijb97 = Frame_lfaijb97(self)

    def __win(self):
        self.title("Tkinter布局助手")
        # 设置窗口大小、居中
        width = 800
        height = 600
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        self.resizable(width=False, height=False)

class Frame_lfaijb97(Notebook):
    def __init__(self,parent):
        super().__init__(parent)
        self.__frame()
    def __frame(self):

        self.tk_tabs_lfaijb97_0 = Frame_lfaijb97_0(self)
        self.add(self.tk_tabs_lfaijb97_0, text="选项卡1")

        self.tk_tabs_lfaijb97_1 = Frame_lfaijb97_1(self)
        self.add(self.tk_tabs_lfaijb97_1, text="选项卡2")

        self.tk_tabs_lfaijb97_2 = Frame_lfaijb97_2(self)
        self.add(self.tk_tabs_lfaijb97_2, text="3333")

        self.place(x=0, y=0, width=800, height=600)

class Frame_lfaijb97_0(Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.__frame()
        self.tk_frame_lfaik3l6 = Frame_lfaik3l6(self)
    def __frame(self):
        self.place(x=0, y=0, width=800, height=600)

class Frame_lfaijb97_1(Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.__frame()
    def __frame(self):
        self.place(x=0, y=0, width=800, height=600)

class Frame_lfaijb97_2(Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.__frame()
    def __frame(self):
        self.place(x=0, y=0, width=800, height=600)

class Frame_lfaik3l6(Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.__frame()
        self.tk_button_lfailbfn = self.__tk_button_lfailbfn()
        self.tk_label_lfailtcr = self.__tk_label_lfailtcr()
        self.tk_label_lfainqrg = self.__tk_label_lfainqrg()
        self.tk_button_lfainxiq = self.__tk_button_lfainxiq()
        self.tk_button_lfainyxp = self.__tk_button_lfainyxp()
        self.tk_label_lfaipd7t = self.__tk_label_lfaipd7t()
        self.tk_label_lfaipekh = self.__tk_label_lfaipekh()
        self.tk_label_lfaiqnwx = self.__tk_label_lfaiqnwx()
        self.tk_label_lfairc6s = self.__tk_label_lfairc6s()
        self.tk_label_lfairdsm = self.__tk_label_lfairdsm()
        self.tk_input_lfaisycj = self.__tk_input_lfaisycj()
        self.tk_input_lfaiszy4 = self.__tk_input_lfaiszy4()
        self.tk_label_lfait3gd = self.__tk_label_lfait3gd()
        self.tk_label_lfaitj73 = self.__tk_label_lfaitj73()
        self.tk_label_lfaitkcw = self.__tk_label_lfaitkcw()
        self.tk_label_lfaitlst = self.__tk_label_lfaitlst()
        self.tk_label_lfaiu4cg = self.__tk_label_lfaiu4cg()
        self.tk_input_lfaiuqxx = self.__tk_input_lfaiuqxx()
        self.tk_input_lfaiuswa = self.__tk_input_lfaiuswa()
        self.tk_input_lfaiutxy = self.__tk_input_lfaiutxy()
        self.tk_input_lfaiuuxj = self.__tk_input_lfaiuuxj()
        self.tk_label_lfaiuz51 = self.__tk_label_lfaiuz51()
        self.tk_label_lfaivhqv = self.__tk_label_lfaivhqv()
        self.tk_label_lfaivu2k = self.__tk_label_lfaivu2k()
        self.tk_label_lfaiw5qg = self.__tk_label_lfaiw5qg()
        self.tk_label_lfaiwk34 = self.__tk_label_lfaiwk34()
        self.tk_input_lfaiwwo3 = self.__tk_input_lfaiwwo3()
        self.tk_input_lfaiwy9m = self.__tk_input_lfaiwy9m()
        self.tk_input_lfaiwzee = self.__tk_input_lfaiwzee()
        self.tk_input_lfaix0e1 = self.__tk_input_lfaix0e1()
        self.tk_label_lfaix9vp = self.__tk_label_lfaix9vp()
        self.tk_label_lfaixh21 = self.__tk_label_lfaixh21()
        self.tk_input_lfaixixg = self.__tk_input_lfaixixg()
        self.tk_label_lfaiy7zx = self.__tk_label_lfaiy7zx()
        self.tk_input_lfaiy9nv = self.__tk_input_lfaiy9nv()
        self.tk_label_lfaiygzx = self.__tk_label_lfaiygzx()
        self.tk_input_lfaiylsc = self.__tk_input_lfaiylsc()
        self.tk_label_lfaiyufr = self.__tk_label_lfaiyufr()
        self.tk_input_lfaiyw8b = self.__tk_input_lfaiyw8b()
        self.tk_label_lfaiz5yh = self.__tk_label_lfaiz5yh()
        self.tk_input_lfaiz7ln = self.__tk_input_lfaiz7ln()
        self.tk_label_lfaize37 = self.__tk_label_lfaize37()
        self.tk_input_lfaizg8s = self.__tk_input_lfaizg8s()
        self.tk_label_lfaizodk = self.__tk_label_lfaizodk()
        self.tk_input_lfaizpv5 = self.__tk_input_lfaizpv5()
    def __frame(self):
        self.place(x=0, y=0, width=798, height=575)

    def __tk_button_lfailbfn(self):
        btn = Button(self, text="EXR数据集路径", command=self.select_dataset_dir)
        btn.place(x=20, y=40, width=97, height=24)
        return btn

    def __tk_label_lfailtcr(self):
        label = Label(self,text="数据集与模型路径设置",anchor="center")
        label.place(x=20, y=10, width=133, height=24)
        return label

    def __tk_label_lfainqrg(self):
        label = Label(self,text="请选择EXR数据集路径",anchor="center")
        label.place(x=120, y=40, width=560, height=24)
        return label

    def select_dataset_dir(self):
        dir_path = filedialog.askdirectory()
        print("Selected h5 dataset directory path:", dir_path)
        if os.listdir(dir_path):
            self.tk_label_lfainqrg.config(text=dir_path)
        else:
            self.tk_label_lfainqrg.config(text="所选文件夹为空")

    def select_dataset_h5_dir(self):
        dir_path = filedialog.askdirectory()
        print("Selected h5 dataset directory path:", dir_path)
        if os.listdir(dir_path):
            self.tk_label_lfaipd7t.config(text=dir_path)
        else:
            self.tk_label_lfaipd7t.config(text="所选文件夹为空")

    def select_model_output_dir(self):
        dir_path = filedialog.askdirectory()
        print("Selected model output directory path:", dir_path)
        if os.listdir(dir_path):
            self.tk_label_lfaipekh.config(text=dir_path)
        else:
            self.tk_label_lfaipekh.config(text="所选文件夹为空")

    def __tk_button_lfainxiq(self):
        btn = Button(self, text="h5数据集路径", command=self.select_dataset_h5_dir)
        btn.place(x=20, y=70, width=97, height=24)
        return btn

    def __tk_button_lfainyxp(self):
        btn = Button(self, text="pt模型保存路径", command=self.select_model_output_dir)
        btn.place(x=20, y=100, width=97, height=24)
        return btn

    def __tk_label_lfaipd7t(self):
        label = Label(self,text="请选择生成的h5数据集要保存的文件夹路径",anchor="center")
        label.place(x=120, y=70, width=560, height=24)
        return label

    def __tk_label_lfaipekh(self):
        label = Label(self,text="请选择pt模型保存路径",anchor="center")
        label.place(x=120, y=100, width=560, height=24)
        return label

    def __tk_label_lfaiqnwx(self):
        label = Label(self,text="训练参数设置",anchor="center")
        label.place(x=20, y=140, width=95, height=24)
        return label

    def __tk_label_lfairc6s(self):
        label = Label(self,text="epochs",anchor="center")
        label.place(x=20, y=170, width=95, height=24)
        return label

    def __tk_label_lfairdsm(self):
        label = Label(self,text="batchSize",anchor="center")
        label.place(x=20, y=200, width=95, height=24)
        return label

    def __tk_input_lfaisycj(self):
        ipt = Entry(self)
        ipt.place(x=120, y=170, width=150, height=24)
        return ipt

    def __tk_input_lfaiszy4(self):
        ipt = Entry(self)
        ipt.place(x=120, y=200, width=150, height=24)
        return ipt

    def __tk_label_lfait3gd(self):
        label = Label(self,text="学习率设置",anchor="center")
        label.place(x=20, y=230, width=95, height=24)
        return label

    def __tk_label_lfaitj73(self):
        label = Label(self,text="lrG",anchor="center")
        label.place(x=20, y=260, width=95, height=24)
        return label

    def __tk_label_lfaitkcw(self):
        label = Label(self,text="lrD",anchor="center")
        label.place(x=20, y=290, width=95, height=24)
        return label

    def __tk_label_lfaitlst(self):
        label = Label(self,text="lrGamma",anchor="center")
        label.place(x=20, y=320, width=95, height=24)
        return label

    def __tk_label_lfaiu4cg(self):
        label = Label(self,text="lrMilestone",anchor="center")
        label.place(x=20, y=350, width=95, height=24)
        return label

    def __tk_input_lfaiuqxx(self):
        ipt = Entry(self)
        ipt.place(x=120, y=260, width=150, height=24)
        return ipt

    def __tk_input_lfaiuswa(self):
        ipt = Entry(self)
        ipt.place(x=120, y=290, width=150, height=24)
        return ipt

    def __tk_input_lfaiutxy(self):
        ipt = Entry(self)
        ipt.place(x=120, y=320, width=150, height=24)
        return ipt

    def __tk_input_lfaiuuxj(self):
        ipt = Entry(self)
        ipt.place(x=120, y=350, width=150, height=24)
        return ipt

    def __tk_label_lfaiuz51(self):
        label = Label(self,text="损失函数权重设置",anchor="center")
        label.place(x=20, y=380, width=98, height=24)
        return label

    def __tk_label_lfaivhqv(self):
        label = Label(self,text="L1LossW",anchor="center")
        label.place(x=20, y=410, width=95, height=24)
        return label

    def __tk_label_lfaivu2k(self):
        label = Label(self,text="lhfLossW",anchor="center")
        label.place(x=20, y=440, width=95, height=24)
        return label

    def __tk_label_lfaiw5qg(self):
        label = Label(self,text="ganLossW",anchor="center")
        label.place(x=20, y=470, width=95, height=24)
        return label

    def __tk_label_lfaiwk34(self):
        label = Label(self,text="gpLossW",anchor="center")
        label.place(x=20, y=500, width=95, height=24)
        return label

    def __tk_input_lfaiwwo3(self):
        ipt = Entry(self)
        ipt.place(x=120, y=410, width=150, height=24)
        return ipt

    def __tk_input_lfaiwy9m(self):
        ipt = Entry(self)
        ipt.place(x=120, y=440, width=150, height=24)
        return ipt

    def __tk_input_lfaiwzee(self):
        ipt = Entry(self)
        ipt.place(x=120, y=470, width=150, height=24)
        return ipt

    def __tk_input_lfaix0e1(self):
        ipt = Entry(self)
        ipt.place(x=120, y=500, width=150, height=24)
        return ipt

    def __tk_label_lfaix9vp(self):
        label = Label(self,text="模型参数设置",anchor="center")
        label.place(x=300, y=140, width=95, height=24)
        return label

    def __tk_label_lfaixh21(self):
        label = Label(self,text="blockSize",anchor="center")
        label.place(x=300, y=170, width=95, height=24)
        return label

    def __tk_input_lfaixixg(self):
        ipt = Entry(self)
        ipt.place(x=400, y=170, width=150, height=24)
        return ipt

    def __tk_label_lfaiy7zx(self):
        label = Label(self,text="haloSize",anchor="center")
        label.place(x=300, y=200, width=95, height=24)
        return label

    def __tk_input_lfaiy9nv(self):
        ipt = Entry(self)
        ipt.place(x=400, y=200, width=150, height=24)
        return ipt

    def __tk_label_lfaiygzx(self):
        label = Label(self,text="numHeads",anchor="center")
        label.place(x=300, y=230, width=95, height=24)
        return label

    def __tk_input_lfaiylsc(self):
        ipt = Entry(self)
        ipt.place(x=400, y=230, width=150, height=24)
        return ipt

    def __tk_label_lfaiyufr(self):
        label = Label(self,text="numSA",anchor="center")
        label.place(x=300, y=260, width=95, height=24)
        return label

    def __tk_input_lfaiyw8b(self):
        ipt = Entry(self)
        ipt.place(x=400, y=260, width=150, height=24)
        return ipt

    def __tk_label_lfaiz5yh(self):
        label = Label(self,text="inCh",anchor="center")
        label.place(x=300, y=290, width=95, height=24)
        return label

    def __tk_input_lfaiz7ln(self):
        ipt = Entry(self)
        ipt.place(x=400, y=290, width=150, height=24)
        return ipt

    def __tk_label_lfaize37(self):
        label = Label(self,text="auxInCh",anchor="center")
        label.place(x=300, y=320, width=95, height=24)
        return label

    def __tk_input_lfaizg8s(self):
        ipt = Entry(self)
        ipt.place(x=400, y=320, width=150, height=24)
        return ipt

    def __tk_label_lfaizodk(self):
        label = Label(self,text="baseCh",anchor="center")
        label.place(x=300, y=350, width=95, height=24)
        return label

    def __tk_input_lfaizpv5(self):
        ipt = Entry(self)
        ipt.place(x=400, y=350, width=150, height=24)
        return ipt

class Win(WinGUI):
    def __init__(self):
        super().__init__()
        self.__event_bind()

    def __event_bind(self):
        pass

if __name__ == "__main__":
    win = Win()
    win.mainloop()
