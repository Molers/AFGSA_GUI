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
import tkinter as tk
from tkinter import ttk
import argparse


parser = argparse.ArgumentParser()


parser.add_argument("--seed", type=int, default=990819)
parser.add_argument("--saveInterval", type=int, default=1)
parser.add_argument("--GUpdateIters", type=int, default=1)
parser.add_argument("--patchSize", type=int, default=128)
parser.add_argument("--numPatches", type=int, default=400)

parser.add_argument("--isLoad", dest="loadModel", action="store_true")
parser.set_defaults(loadModel=False)
parser.add_argument("--modelPath", type=str, default=None)

parser.add_argument("--blockSize", type=int, default=8)
parser.add_argument("--haloSize", type=int, default=3)
parser.add_argument("--numHeads", type=int, default=4)
parser.add_argument("--baseCh", type=int, default=256)
parser.add_argument("--numGradientCheckpoint", type=int, default=0)
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

class Tooltip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)

    def enter(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + self.widget.winfo_width() // 2
        y += self.widget.winfo_rooty() + self.widget.winfo_height()
        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry("+%d+%d" % (x, y))
        label = ttk.Label(self.tooltip, text=self.text, justify='left',
                          background="#ffffff", relief='solid', borderwidth=1,
                          font=("tahoma", "10", "normal"))
        label.pack(ipadx=1)

    def leave(self, event=None):
        if self.tooltip:
            self.tooltip.destroy()

class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_tabs_lfaijb97 = Frame_lfaijb97(self)

    def __win(self):
        self.title("基于辅助特征的自注意力蒙特卡罗医学体积渲染去噪系统")
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
        self.add(self.tk_tabs_lfaijb97_0, text="训练参数")

        self.tk_tabs_lfaijb97_1 = Frame_lfaijb97_1(self)
        self.add(self.tk_tabs_lfaijb97_1, text="训练")

        self.tk_tabs_lfaijb97_2 = Frame_lfaijb97_2(self)
        self.add(self.tk_tabs_lfaijb97_2, text="测试")

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
        self.tk_text_lfaux3dy = self.__tk_text_lfaux3dy()
        self.tk_button_lfav0l8b = self.__tk_button_lfav0l8b()

    def __frame(self):
        self.place(x=0, y=0, width=800, height=600)

    def __tk_text_lfaux3dy(self):
        text = Text(self)
        text.place(x=10, y=365, width=782, height=197)

        vbar = Scrollbar(self)
        text.configure(yscrollcommand=vbar.set)
        vbar.config(command=text.yview)
        vbar.place(x=777, y=365, width=15, height=197)
        scrollbar_autohide(vbar, text)
        return text

    def __tk_button_lfav0l8b(self):
        btn = Button(self, text="开始训练")
        btn.place(x=10, y=120, width=87, height=36)
        return btn


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
        self.tk_label_PathSetting = self.__tk_label_PathSetting()
        # Exr 路径选择
        self.tk_button_SelectExrPath = self.__tk_button_SelectExrPath()
        self.tk_label_ExrPath = self.__tk_label_ExrPath()
        # H5 数据集
        self.tk_button_SelectH5DatasetPath = self.__tk_button_SelectH5DatasetPath()
        self.tk_label_H5DatasetPath = self.__tk_label_H5DatasetPath()
        # 模型路径
        self.tk_button_ModelOutputPath = self.__tk_button_ModelOutputPath()
        self.tk_label_ModelOutputPath = self.__tk_label_ModelOutputPath()

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
        self.tk_button_lfawaqs2 = self.__tk_button_lfawaqs2()
        self.tk_button_lfawat4x = self.__tk_button_lfawat4x()

    def __frame(self):
        self.place(x=0, y=0, width=798, height=575)
    # 数据集与模型路径设置
    def __tk_label_PathSetting(self): # lfailtcr PathSetting
        label = Label(self,text="数据集与模型路径设置",anchor="center")
        label.place(x=20, y=10, width=133, height=24)
        return label

    # <editor-fold desc="EXR数据集路径按钮">
    # EXR数据集路径按钮
    def __tk_button_SelectExrPath(self): #lfailbfn SelectExrPath
        btn = Button(self, text="EXR数据集路径")
        btn.place(x=20, y=40, width=97, height=24)
        return btn

    def __tk_label_ExrPath(self): # lfainqrg
        label = Label(self,text="请选择EXR数据集路径",anchor="center")
        label.place(x=120, y=40, width=560, height=24)
        return label

    def select_dataset_dir(self):
        dir_path = filedialog.askdirectory()
        print("Selected Exr dataset directory path:", dir_path)
        if os.listdir(dir_path):
            self.tk_label_ExrPath.config(text=dir_path)
            parser.set_defaults(inDir=dir_path)
        else:
            self.tk_label_ExrPath.config(text="所选文件夹为空")

    # </editor-fold>

    # <editor-fold desc="H5数据集路径按钮">
    def __tk_button_SelectH5DatasetPath(self): # SelectH5DatasetPath
        btn = Button(self, text="h5数据集路径")
        btn.place(x=20, y=70, width=97, height=24)
        return btn

    def __tk_label_H5DatasetPath(self): # SelectH5DatasetPath
        label = Label(self,text="请选择生成的h5数据集要保存的文件夹路径",anchor="center")
        label.place(x=120, y=70, width=560, height=24)
        return label

    def select_dataset_h5_dir(self):
        dir_path = filedialog.askdirectory()
        print("Selected h5 dataset directory path:", dir_path)
        if os.listdir(dir_path):
            self.tk_label_H5DatasetPath.config(text=dir_path)
            parser.set_defaults(datasetDir=dir_path)
        else:
            self.tk_label_H5DatasetPath.config(text="所选文件夹为空")

    # </editor-fold>

    def __tk_button_ModelOutputPath(self): # lfainyxp
        btn = Button(self, text="pt模型保存路径", command=self.select_model_output_dir)
        btn.place(x=20, y=100, width=97, height=24)
        return btn

    def __tk_label_ModelOutputPath(self):
        label = Label(self,text="请选择pt模型保存路径",anchor="center")
        label.place(x=120, y=100, width=560, height=24)
        return label

    def select_model_output_dir(self): # lfaipekh ModelOutputPath
        dir_path = filedialog.askdirectory()
        print("Selected model output directory path:", dir_path)
        if os.listdir(dir_path):
            self.tk_label_ModelOutputPath.config(text=dir_path)
            parser.set_defaults(outDir=dir_path)
        else:
            self.tk_label_ModelOutputPath.config(text="所选文件夹为空")
    def __tk_label_lfaiqnwx(self):
        label = Label(self,text="训练参数设置",anchor="center")
        label.place(x=20, y=140, width=95, height=24)
        return label

    def __tk_label_lfairc6s(self):
        label = Label(self,text="epochs",anchor="center")
        tooltip = Tooltip(label,
                                "深度学习中，模型的训练通常分为多个轮次（Epoch）。每个Epoch中，模型会对整个训练数据集进行一次迭代，\n 通过不断地调整模型参数，使得模型的预测结果与真实标签更加接近。\n"
                                "Epoch数量的选择需要根据具体任务和数据集进行调整，一般情况下，Epoch数量越多，模型性能会越好，")
        label.place(x=20, y=170, width=95, height=24)
        return label

    def __tk_label_lfairdsm(self):
        label = Label(self,text="batchSize",anchor="center")
        tooltip = Tooltip(label, "Batch size是指每次迭代训练时使用的样本数量，通常会将训练数据集分成多个小批量，每个批量中的样本数就是batch size。\n较大的batch size可以提高训练效率，但可能会导致内存溢出或无法收敛；\n较小的batch size可以提高模型收敛的稳定性和准确性，但会增加训练时间。")
        label.place(x=20, y=200, width=95, height=24)
        return label

    # Epoch
    def __tk_input_lfaisycj(self):
        ipt = Entry(self)
        ipt.insert(0, "24")  # 在输入框中插入默认值
        ipt.place(x=120, y=170, width=150, height=24)
        return ipt
    # BatchSize
    def __tk_input_lfaiszy4(self):
        ipt = Entry(self)
        ipt.insert(0, "2")  # 在输入框中插入默认值
        ipt.place(x=120, y=200, width=150, height=24)
        return ipt

    def __tk_label_lfait3gd(self):
        label = Label(self,text="学习率设置",anchor="center")
        label.place(x=20, y=230, width=95, height=24)
        return label

    def __tk_label_lfaitj73(self):
        label = Label(self,text="lrG",anchor="center")
        tooltip = Tooltip(label,"lrG是指生成器的学习率，用于控制生成器在每次迭代中参数的更新量大小。\n较小的lrG可以提高模型的稳定性和鲁棒性，但训练时间可能会更长；\n较大的lrG可以加快模型的收敛速度，但可能会导致模型训练不稳定。")
        label.place(x=20, y=260, width=95, height=24)
        return label

    def __tk_label_lfaitkcw(self):
        label = Label(self,text="lrD",anchor="center")
        tooltip = Tooltip(label,
                          "判别器的学习率，用于控制判别器在每次迭代中参数的更新量大小。\n较小的lrD可以提高模型的稳定性和鲁棒性，但训练时间可能会更长；\n较大的lrD可以加快模型的收敛速度，但可能会导致模型训练不稳定。")
        label.place(x=20, y=290, width=95, height=24)
        return label

    def __tk_label_lfaitlst(self):
        label = Label(self,text="lrGamma",anchor="center")
        tooltip = Tooltip(label,
                          "学习率的下降率，通常在学习率下降策略中使用。当训练过程中模型的收敛速度变慢时，可以通过降低学习率来提高模型的性能。\nlrGamma可以控制每次学习率下降的比例，通常设置在0.1到0.5之间。较小的lrGamma可以使学习率下降得更加平滑，但需要更多的迭代次数；\n较大的lrGamma可以使学习率下降得更加快速，但可能会导致模型训练不稳定。")

        label.place(x=20, y=320, width=95, height=24)
        return label

    def __tk_label_lfaiu4cg(self):
        label = Label(self,text="lrMilestone",anchor="center")
        tooltip = Tooltip(label,
                          "学习率下降的里程碑，通常在学习率下降策略中使用。当训练过程中模型的收敛速度变慢时，可以通过降低学习率来提高模型的性能。\n"
                          "lrMilestone指的是在哪些训练轮数之后下降学习率，通常设置为一个列表，表示在哪些训练轮数之后下降学习率。\n"
                          "例如，如果将lrMilestone设置为[30, 60, 90]，则表示在第30、60和90个训练轮数之后下降学习率。")

        label.place(x=20, y=350, width=95, height=24)
        return label
    #lrG
    def __tk_input_lfaiuqxx(self):
        ipt = Entry(self)
        ipt.insert(0, "1e-4")  #
        ipt.place(x=120, y=260, width=150, height=24)
        return ipt

    # lrD
    def __tk_input_lfaiuswa(self):
        ipt = Entry(self)
        ipt.insert(0, "1e-4")  #
        ipt.place(x=120, y=290, width=150, height=24)
        return ipt
    #lrGamma
    def __tk_input_lfaiutxy(self):
        ipt = Entry(self)
        ipt.insert(0, "0.5")  #
        ipt.place(x=120, y=320, width=150, height=24)
        return ipt

    #lrMileStone
    def __tk_input_lfaiuuxj(self):
        ipt = Entry(self)
        ipt.insert(0, "3")  #
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

    def __tk_button_lfawaqs2(self):
        btn = Button(self, text="保存训练参数")
        btn.place(x=300, y=410, width=97, height=28)
        return btn

    def __tk_button_lfawat4x(self):
        btn = Button(self, text="导入训练参数")
        btn.place(x=300, y=450, width=97, height=29)
        return btn

class Win(WinGUI):
    def __init__(self):
        super().__init__()
        self.__event_bind()

    # def SelectExrPath(self, evt):
    #     self.tk_tabs_lfaijb97.tk_tabs_lfaijb97_0.tk_frame_lfaik3l6.tk_button_SelectExrPath.config(state=tk.DISABLED)
    #     dir_path = filedialog.askdirectory()
    #     print("Selected Exr dataset directory path:", dir_path, evt)
    #     if os.listdir(dir_path):
    #         self.tk_tabs_lfaijb97.tk_tabs_lfaijb97_0.tk_frame_lfaik3l6.tk_label_ExrPath.config(text=dir_path)
    #         parser.set_defaults(inDir=dir_path)
    #     else:
    #         self.tk_tabs_lfaijb97.tk_tabs_lfaijb97_0.tk_frame_lfaik3l6.tk_label_ExrPath.config(text="所选文件夹为空")
    #     self.tk_tabs_lfaijb97.tk_tabs_lfaijb97_0.tk_frame_lfaik3l6.tk_button_SelectExrPath.config(state=tk.NORMAL)
    #
    # def SelectH5DatasetPath(self, evt):
    #     dir_path = filedialog.askdirectory()
    #     print("Selected h5 dataset directory path:", dir_path, evt)
    #     if os.listdir(dir_path):
    #         self.tk_tabs_lfaijb97.tk_tabs_lfaijb97_0.tk_frame_lfaik3l6.tk_label_H5DatasetPath.config(text=dir_path)
    #         parser.set_defaults(datasetDir=dir_path)
    #     else:
    #         self.tk_tabs_lfaijb97.tk_tabs_lfaijb97_0.tk_frame_lfaik3l6.tk_label_H5DatasetPath.config(text="所选文件夹为空")

    def SaveSetting(self, evt):
        print("<Button>事件未处理", evt)

    def ImportSetting(self, evt):
        print("<Button>事件未处理", evt)

    def __event_bind(self):
        # self.tk_tabs_lfaijb97.tk_tabs_lfaijb97_0.tk_frame_lfaik3l6.tk_button_SelectExrPath.bind('<Button>', self.SelectExrPath)
        # self.tk_tabs_lfaijb97.tk_tabs_lfaijb97_0.tk_frame_lfaik3l6.tk_button_SelectH5DatasetPath.bind('<Button>', self.SelectH5DatasetPath)
        self.tk_tabs_lfaijb97.tk_tabs_lfaijb97_0.tk_frame_lfaik3l6.tk_button_lfawaqs2.bind('<Button>', self.SaveSetting)
        self.tk_tabs_lfaijb97.tk_tabs_lfaijb97_0.tk_frame_lfaik3l6.tk_button_lfawat4x.bind('<Button>', self.ImportSetting)

def train():
    args, unknown = parser.parse_known_args()
    print("inDir parameter value:", args.inDir)
    print("datasetDir parameter value:", args.datasetDir)

    # 格式化为字符串
    # print("inDir parameter value: {}".format(args.inDir))
    # print("datasetDir parameter value: {}".format(args.datasetDir))


if __name__ == "__main__":
    win = Win()
    win.mainloop()
