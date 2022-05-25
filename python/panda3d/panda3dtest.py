from direct.showbase.ShowBase import ShowBase
from math import pi, sin, cos
from direct.task import Task
from direct.actor.Actor import Actor


class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        #load enviroment
        self.scene = self.loader.loadModel("models/environment")
        #reparent the scene
        self.scene.reparentTo(self.render)
        #scale
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8,42,0)
        self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")
        # laod panda model and transform it
        self.pandaActor = Actor("models/panda-model",{"walk": "models/panda-walk4"})
        self.pandaActor.setScale(0.05, 0.05, 0.0005)
        self.pandaActor.reparentTo(self.render)
        self.pandaActor.loop("walk")

    def spinCameraTask(self,task):
        angleDegrees = task.time * 0
        angleRadians = angleDegrees * (pi/180.0)
        self.camera.setPos(20*sin(angleRadians), -20 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0,0)
        return Task.cont
app = MyApp()
app.run()
