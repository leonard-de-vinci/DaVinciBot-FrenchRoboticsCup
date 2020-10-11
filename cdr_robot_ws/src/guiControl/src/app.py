#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import rospy
from std_msgs.msg import Bool
from PID.msg import IntArr

historic_data = "historique"


class controllerFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: controllerFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((454, 400))
        self.choice_pid_cote = wx.Choice(self, wx.ID_ANY, choices=["Gauche", "Droit"])
        self.choice_pid_cote.Bind(wx.EVT_CHOICE, self.OnPidChoice)
        self.ctrl_target_ticks = wx.SpinCtrl(self, wx.ID_ANY, "0", min=0, max=10000)
        self.ctrl_target_cycles = wx.SpinCtrl(self, wx.ID_ANY, "0", min=0, max=10000)
        self.target_send = wx.Button(self, wx.ID_ANY, "SEND")
        self.target_send.Bind(wx.EVT_BUTTON, self.OnSendClicked)
        self.scroll_panel = wx.ScrolledWindow(self, wx.ID_ANY, style=wx.TAB_TRAVERSAL)
        self.button_1 = wx.ToggleButton(self, wx.ID_ANY, u"EMERGENCY BREAK")
        self.button_1.Bind(wx.EVT_TOGGLEBUTTON, self.onBreak)
        self.choice_manche_cote = wx.Choice(self, wx.ID_ANY, choices=["Gauche", "Droit"])
        self.choice_manche_cote.Bind(wx.EVT_CHOICE, self.OnMancheChoice)
        self.checkbox_manche = wx.CheckBox(self, wx.ID_ANY, "Actif")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: controllerFrame.__set_properties
        self.SetTitle("The ultimate controller")
        _icon = wx.NullIcon
        _icon.CopyFromBitmap(wx.Bitmap("/home/dvb/Downloads/controller.png", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.choice_pid_cote.SetSelection(0)
        global pid_cote
        pid_cote = 1
        self.scroll_panel.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_BTNSHADOW))
        self.scroll_panel.SetScrollRate(10, 10)
        self.choice_manche_cote.SetSelection(0)
        
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: controllerFrame.__do_layout
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_13 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_14 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_11 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_7 = wx.BoxSizer(wx.VERTICAL)
        sizer_10 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_9 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_12 = wx.BoxSizer(wx.HORIZONTAL)
        title_pid = wx.StaticText(self, wx.ID_ANY, "PID", style=wx.ALIGN_CENTER)
        title_pid.SetFont(wx.Font(15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_1.Add(title_pid, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 8)
        label_pid_cote = wx.StaticText(self, wx.ID_ANY, u"Coté : ", style=wx.ALIGN_CENTER)
        sizer_12.Add(label_pid_cote, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 8)
        sizer_12.Add(self.choice_pid_cote, 0, 0, 0)
        sizer_1.Add(sizer_12, 0, wx.EXPAND, 0)
        static_line_4 = wx.StaticLine(self, wx.ID_ANY)
        sizer_1.Add(static_line_4, 0, wx.EXPAND, 0)
        sizer_2.Add(sizer_1, 0, wx.EXPAND, 0)
        title_target = wx.StaticText(self, wx.ID_ANY, "Target :", style=wx.ALIGN_CENTER)
        title_target.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_4.Add(title_target, 0, wx.ALL | wx.EXPAND, 7)
        label_target_ticks = wx.StaticText(self, wx.ID_ANY, "Ticks : ")
        sizer_5.Add(label_target_ticks, 0, wx.ALIGN_CENTER_VERTICAL | wx.BOTTOM | wx.LEFT | wx.TOP, 8)
        sizer_5.Add((8, 20), 0, 0, 0)
        sizer_5.Add(self.ctrl_target_ticks, 1, wx.BOTTOM | wx.RIGHT | wx.TOP, 8)
        sizer_4.Add(sizer_5, 0, wx.EXPAND, 0)
        label_target_cycles = wx.StaticText(self, wx.ID_ANY, "Cycles : ")
        sizer_6.Add(label_target_cycles, 0, wx.ALIGN_CENTER_VERTICAL | wx.BOTTOM | wx.LEFT | wx.TOP, 8)
        sizer_6.Add(self.ctrl_target_cycles, 1, wx.BOTTOM | wx.RIGHT | wx.TOP, 8)
        sizer_4.Add(sizer_6, 0, wx.EXPAND, 0)
        sizer_4.Add(self.target_send, 0, wx.ALL | wx.EXPAND, 8)
        sizer_3.Add(sizer_4, 1, wx.EXPAND, 0)
        static_line_3 = wx.StaticLine(self, wx.ID_ANY, style=wx.LI_VERTICAL)
        sizer_3.Add(static_line_3, 0, wx.EXPAND, 0)
        title_reality = wx.StaticText(self, wx.ID_ANY, "Reality :", style=wx.ALIGN_CENTER)
        title_reality.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_7.Add(title_reality, 0, wx.ALL | wx.EXPAND, 7)
        label_reality_ticks = wx.StaticText(self, wx.ID_ANY, "Ticks : ")
        sizer_8.Add(label_reality_ticks, 0, wx.ALIGN_CENTER_VERTICAL | wx.BOTTOM | wx.LEFT | wx.TOP, 8)
        sizer_8.Add((8, 0), 0, 0, 0)
        label_reality_ticks_data = wx.StaticText(self, wx.ID_ANY, "0")
        label_reality_ticks_data.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_8.Add(label_reality_ticks_data, 1, wx.ALIGN_CENTER_VERTICAL | wx.BOTTOM | wx.LEFT | wx.TOP, 8)
        sizer_7.Add(sizer_8, 0, wx.EXPAND, 0)
        label_reality_cycles = wx.StaticText(self, wx.ID_ANY, "Cycles : ")
        sizer_9.Add(label_reality_cycles, 0, wx.ALIGN_CENTER_VERTICAL | wx.BOTTOM | wx.LEFT | wx.TOP, 8)
        label_reality_ticks_data_copy = wx.StaticText(self, wx.ID_ANY, "0")
        label_reality_ticks_data_copy.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_9.Add(label_reality_ticks_data_copy, 1, wx.ALIGN_CENTER_VERTICAL | wx.BOTTOM | wx.LEFT | wx.TOP, 8)
        sizer_7.Add(sizer_9, 0, wx.EXPAND, 0)
        label_historic = wx.StaticText(self.scroll_panel, wx.ID_ANY, "label_1\ne\ner\ner\ne\ner\n")
        sizer_10.Add(label_historic, 1, wx.ALL | wx.EXPAND, 8)
        self.scroll_panel.SetSizer(sizer_10)
        sizer_7.Add(self.scroll_panel, 1, wx.EXPAND, 0)
        sizer_3.Add(sizer_7, 1, wx.EXPAND, 0)
        sizer_2.Add(sizer_3, 0, wx.EXPAND, 0)
        static_line_1 = wx.StaticLine(self, wx.ID_ANY)
        sizer_11.Add(static_line_1, 0, wx.EXPAND, 0)
        sizer_11.Add(self.button_1, 1, wx.ALL | wx.EXPAND, 8)
        static_line_2 = wx.StaticLine(self, wx.ID_ANY)
        sizer_11.Add(static_line_2, 0, wx.EXPAND, 0)
        sizer_2.Add(sizer_11, 0, wx.EXPAND, 0)
        title_manche = wx.StaticText(self, wx.ID_ANY, u"Manche à air", style=wx.ALIGN_CENTER)
        title_manche.SetFont(wx.Font(15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_2.Add(title_manche, 0, wx.ALL | wx.EXPAND, 8)
        label_pid_cote_copy = wx.StaticText(self, wx.ID_ANY, u"Coté : ", style=wx.ALIGN_CENTER)
        sizer_14.Add(label_pid_cote_copy, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 8)
        sizer_14.Add(self.choice_manche_cote, 0, 0, 0)
        sizer_13.Add(sizer_14, 1, 0, 0)
        sizer_13.Add(self.checkbox_manche, 1, wx.EXPAND, 0)
        sizer_2.Add(sizer_13, 0, wx.EXPAND, 0)
        self.SetSizer(sizer_2)
        self.Layout()
        # end wxGlade

    def OnSendClicked(self, e):
        ticks = self.ctrl_target_ticks.GetValue() 
        cycles = self.ctrl_target_cycles.GetValue()
        
        msg = IntArr()
        msg.ticks = int(ticks)
        msg.cycles = int(cycles) 
        if pid_cote == 0:
            rospy.loginfo('gauche | ticks : '+str(ticks)+" | cycles : "+str(cycles))
            lefttargetpub.publish(msg)
        else:
            rospy.loginfo('droit | ticks : '+str(ticks)+" | cycles : "+str(cycles))
            righttargetpub.publish(msg)
        e.Skip()

    def onBreak(self, e):
        cb = e.GetEventObject()
        rospy.loginfo(str(cb.GetValue()))
        global emergencypub
        emergencypub.publish(cb.GetValue())

    def reality_callback(self, msg):
        rospy.loginfo('rticks : '+str(msg.ticks)+" | rcycles : "+str(msg.cycles))
        global historic_data
        historic_data += 'rticks : '+str(msg.ticks)+" | rcycles : "+str(msg.cycles)+'\n'
        wx.CallAfter(self.label_reality_ticks_data.SetLabel, str(msg.ticks))
        wx.CallAfter(self.label_reality_cycles_data.SetLabel, str(msg.cycles))
        wx.CallAfter(self.label_historic.SetLabel, str(msg.cycles))

# end of class controllerFrame

class MyApp(wx.App):
    def OnInit(self):
        self.frame = controllerFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        global emergencypub, righttargetpub, rightrealitysub, lefttargetpub, leftrealitysub
        emergencypub = rospy.Publisher("/breakServo",Bool,queue_size=1)
        righttargetpub = rospy.Publisher("/right/target",IntArr,queue_size=1)
        rightrealitysub = rospy.Subscriber("/right/reality", IntArr, self.frame.reality_callback)
        lefttargetpub = rospy.Publisher("/left/target",IntArr,queue_size=1)
        leftrealitysub = rospy.Subscriber("/left/reality", IntArr, self.frame.reality_callback)
        rospy.init_node("ultimatecontroller", anonymous=False)
        rospy.loginfo("> ultimate controller correctly initialised")
        self.frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    
    app = MyApp(0)
    app.MainLoop()
