#!/usr/bin/env python
import wx
import rospy
from std_msgs.msg import Bool
from PID.msg import IntArr

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        self.InitUI()
        self.Centre()

    def InitUI(self):

        panel = wx.Panel(self)

        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)

        font.SetPointSize(9)

        vbox = wx.BoxSizer(wx.VERTICAL)

        hboxHaut = wx.BoxSizer(wx.HORIZONTAL)

        vboxTarget = wx.BoxSizer(wx.VERTICAL)
        vboxReality = wx.BoxSizer(wx.VERTICAL)
        st1 = wx.StaticText(panel, label='Target')
        st1.SetFont(font)
        vboxTarget.Add(st1, flag=wx.LEFT | wx.TOP, border=10)

        vboxTarget.Add((-1, 10))

        stT = wx.StaticText(panel, label='Ticks :')
        stT.SetFont(font)
        vboxTarget.Add(stT, flag=wx.LEFT | wx.TOP, border=10)

        self.tcTick = wx.TextCtrl(panel)
        vboxTarget.Add(self.tcTick, flag=wx.LEFT | wx.TOP, border=10)
        vboxTarget.Add((-1, 10))
        stC = wx.StaticText(panel, label='Cycles :')
        stC.SetFont(font)
        vboxTarget.Add(stC, flag=wx.LEFT | wx.TOP, border=10)

        self.tcCycle = wx.TextCtrl(panel)
        vboxTarget.Add(self.tcCycle, flag=wx.LEFT | wx.TOP, border=10)

        btn1 = wx.Button(panel, label='Send', size=(70, 30))
        btn1.Bind(wx.EVT_BUTTON, self.OnButtonClicked)
        vboxTarget.Add(btn1, flag=wx.LEFT | wx.TOP, border=10)


        st2 = wx.StaticText(panel, label='Reality')
        st2.SetFont(font)
        vboxReality.Add(st2, flag=wx.LEFT | wx.TOP, border=10)
        global tc2
        tc2 = wx.StaticText(panel, 
                    label ='')
        vboxReality.Add(tc2, proportion=1, flag=wx.EXPAND)
        hboxHaut.Add(vboxTarget, proportion=1)
        hboxHaut.Add(vboxReality, proportion=1)

        vbox.Add(hboxHaut, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)




       

        vbox.Add((-1, 25))

        cb1 = wx.CheckBox(panel, label='Break')
        cb1.SetFont(font)
        cb1.Bind(wx.EVT_CHECKBOX, self.onChecked)
        
        vbox.Add(cb1, flag=wx.CENTER, border=10)
        vbox.Add((-1, 25))
        

        panel.SetSizer(vbox)

        
 
 
 
    def onChecked(self, e):
        cb = e.GetEventObject()
        rospy.loginfo(str(cb.IsChecked()))
        global emergencypub
        emergencypub.publish(cb.IsChecked())
    
    def OnButtonClicked(self, e):
        ticks = self.tcTick.GetValue() 
        cycles = self.tcCycle.GetValue()
        rospy.loginfo('ticks : '+ticks+" | cycles : "+cycles)
        global targetpub
        msg = IntArr()
        msg.ticks = int(ticks)
        msg.cycles = int(cycles) 
        targetpub.publish(msg)
        e.Skip()
    
def reality_callback(msg):
    global tc2
    rospy.loginfo('rticks : '+str(msg.ticks)+" | rcycles : "+str(msg.cycles))
    wx.CallAfter(tc2.SetLabel, 'ticks : '+str(msg.ticks)+" | cycles : "+str(msg.cycles))
    
        


def main():
    global emergencypub, targetpub, realitysub
    emergencypub = rospy.Publisher("/breakServo",Bool,queue_size=1)
    targetpub = rospy.Publisher("/right/target",IntArr,queue_size=1)
    realitysub = rospy.Subscriber("/right/reality", IntArr, reality_callback)
    rospy.init_node("ultimatecontroller", anonymous=False)
    rospy.loginfo("> emergency publisher correctly initialised")
    app = wx.App()
    ex = Example(None, title='the ultimate controller')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()