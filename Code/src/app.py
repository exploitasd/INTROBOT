from Tkinter import *
import os
import time
import tkMessageBox
import PIL.Image
from PIL import ImageTk

import rospy
import actionlib
from actionlib_msgs.msg import *
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import Pose, PoseWithCovarianceStamped, Point, Quaternion, Twist

# ONEMLI NOT: KOD UZERINDEKI RESIM VE SESLERIN BULUNDUGU SATIRLARDAKI DIZINLER DUZELTILMELIDIR. 

class GoToPose():
	
	def __init__(self):
	
		def start_point():			
			
			goalx_0 = MoveBaseGoal()
			goalx_0.target_pose.header.frame_id = 'map'
			goalx_0.target_pose.header.stamp = rospy.Time.now()	
			goalx_0.target_pose.pose = Pose(Point(0.037, 0.009, 0.000), Quaternion(0.000, 0.000, 0.007, 1.000))
			self.move_base.send_goal(goalx_0)
			successx_0 = self.move_base.wait_for_result(rospy.Duration(120)) 	

			if not successx_0:
      				self.move_base.cancel_goal()
				tkMessageBox.showinfo("Hata", "Robotu kurtar!")
				os.system("aplay /home/kahya/Desktop/INTROBOT/sounds/hata.wav")
				return None
   			else:
				statex_0 = self.move_base.get_state()
				if statex_0 == GoalStatus.SUCCEEDED:
	    				#os.system("aplay /home/kahya/Desktop/INTROBOT/sounds/return.wav")
				else:
				    	tkMessageBox.showinfo("Hata", "Robotu kurtar!")
					os.system("aplay /home/kahya/Desktop/INTROBOT/sounds/hata.wav")
					return None
   	
		def computer_desk():			
			
			goal0_1 = MoveBaseGoal()
			goal0_1.target_pose.header.frame_id = 'map'
			goal0_1.target_pose.header.stamp = rospy.Time.now()	
			goal0_1.target_pose.pose = Pose(Point(-0.484, 5.178, 0.000), Quaternion(0.000, 0.000, -0.001, 1.000))
			self.move_base.send_goal(goal0_1)
			success0_1 = self.move_base.wait_for_result(rospy.Duration(120)) 	

			if not success0_1:
       	       			self.move_base.cancel_goal()
				tkMessageBox.showinfo("Hata", "Robotu kurtar!")
				os.system("aplay /home/kahya/Desktop/INTROBOT/sounds/hata.wav")
				return None
   			else:
				state0_1 = self.move_base.get_state()
				if state0_1 == GoalStatus.SUCCEEDED:
					os.system("aplay /home/kahya/Desktop/INTROBOT/sounds/bilgisayar.wav")
				else:
					tkMessageBox.showinfo("Hata", "Robotu kurtar!")
					os.system("aplay /home/kahya/Desktop/INTROBOT/sounds/hata.wav")
					return None
		
			goal1_0 = MoveBaseGoal()
			goal1_0.target_pose.header.frame_id = 'map'
			goal1_0.target_pose.header.stamp = rospy.Time.now()
			goal1_0.target_pose.pose = Pose(Point(0.037, 0.009, 0.000), Quaternion(0.000, 0.000, 0.007, 1.000))
       			self.move_base.send_goal(goal1_0)
			success1_0 = self.move_base.wait_for_result(rospy.Duration(120)) 
	
			if not success1_0:
            			self.move_base.cancel_goal()
				tkMessageBox.showinfo("Hata", "Robotu kurtar!")
				os.system("aplay /home/kahya/Desktop/INTROBOT/sounds/hata.wav")
				return None
    			else:
				state1_0 = self.move_base.get_state()
				if state1_0 == GoalStatus.SUCCEEDED:
	     				#os.system("aplay /home/kahya/Desktop/INTROBOT/sounds/return.wav")
				else: 
				    	tkMessageBox.showinfo("Hata", "Robotu kurtar!")
					os.system("aplay /home/kahya/Desktop/INTROBOT/sounds/hata.wav")
					return None

		def iktisat():

			goal0_2 = MoveBaseGoal()
			goal0_2.target_pose.header.frame_id = 'map'
			goal0_2.target_pose.header.stamp = rospy.Time.now()	
			goal0_2.target_pose.pose = Pose(Point(1.965, 9.969, 0.000), Quaternion(0.000, 0.000, -0.718, 0.696))
			self.move_base.send_goal(goal0_2)
			success0_2 = self.move_base.wait_for_result(rospy.Duration(120)) 	
	
			if not success0_2:
        	        	self.move_base.cancel_goal()
				tkMessageBox.showinfo("Hata", "Robotu kurtar!")
				os.system("aplay /home/kahya/Desktop/INTROBOT/sounds/hata.wav")
    			else:
				state0_2 = self.move_base.get_state()
				if state0_2 == GoalStatus.SUCCEEDED:
		    			os.system("aplay /home/kahya/Desktop/INTROBOT/sounds/iktisat.wav")
				else: 
				    	tkMessageBox.showinfo("Hata", "Robotu kurtar!")
					os.system("aplay /home/kahya/Desktop/INTROBOT/sounds/hata.wav")
					return None
		
			goal2_0 = MoveBaseGoal()
			goal2_0.target_pose.header.frame_id = 'map'
			goal2_0.target_pose.header.stamp = rospy.Time.now()
			goal2_0.target_pose.pose = Pose(Point(0.037, 0.009, 0.000), Quaternion(0.000, 0.000, 0.007, 1.000))
        		self.move_base.send_goal(goal2_0)
			success2_0 = self.move_base.wait_for_result(rospy.Duration(120)) 
	
			if not success2_0:
       				self.move_base.cancel_goal()
				tkMessageBox.showinfo("Hata", "Robotu kurtar!")
				os.system("aplay /home/kahya/Desktop/INTROBOT/sounds/hata.wav")
    			else:
				state2_0 = self.move_base.get_state()
				if state2_0 == GoalStatus.SUCCEEDED:
		     			#os.system("aplay /home/kahya/Desktop/INTROBOT/sounds/return.wav")
				else: 
				    	tkMessageBox.showinfo("Hata", "Robotu kurtar!")
					os.system("aplay /home/kahya/Desktop/INTROBOT/sounds/hata.wav")
					return None

		def mechanical_desk():			
			
			goal0_3 = MoveBaseGoal()
			goal0_3.target_pose.header.frame_id = 'map'
			goal0_3.target_pose.header.stamp = rospy.Time.now()	
			goal0_3.target_pose.pose = Pose(Point(8.126, 10.435, 0.000), Quaternion(0.000, 0.000, -0.674, 0.739))
			self.move_base.send_goal(goal0_3)
			success0_3 = self.move_base.wait_for_result(rospy.Duration(120)) 	

			if not success0_3:
       	       			self.move_base.cancel_goal()
				tkMessageBox.showinfo("Hata", "Robotu kurtar!")
				os.system("aplay /home/kahya/Desktop/INTROBOT/sounds/hata.wav")
				return None
   			else:
				state0_3 = self.move_base.get_state()
				if state0_3 == GoalStatus.SUCCEEDED:
					os.system("aplay /home/kahya/Desktop/INTROBOT/sounds/makina.wav")
				else:
					tkMessageBox.showinfo("Hata", "Robotu kurtar!")
					os.system("aplay /home/kahya/Desktop/INTROBOT/sounds/hata.wav")
					return None
		
			goal3_0 = MoveBaseGoal()
			goal3_0.target_pose.header.frame_id = 'map'
			goal3_0.target_pose.header.stamp = rospy.Time.now()
			goal3_0.target_pose.pose = Pose(Point(0.037, 0.009, 0.000), Quaternion(0.000, 0.000, 0.007, 1.000))
       			self.move_base.send_goal(goal3_0)
			success3_0 = self.move_base.wait_for_result(rospy.Duration(120)) 
	
			if not success3_0:
            			self.move_base.cancel_goal()
				tkMessageBox.showinfo("Hata", "Robotu kurtar!")
				os.system("aplay /home/kahya/Desktop/INTROBOT/sounds/hata.wav")
				return None
    			else:
				state3_0 = self.move_base.get_state()
				if state3_0 == GoalStatus.SUCCEEDED:
	     				#os.system("aplay /home/kahya/Desktop/INTROBOT/sounds/return.wav")
				else:
				    	tkMessageBox.showinfo("Hata", "Robotu kurtar!")
					os.system("aplay /home/kahya/Desktop/INTROBOT/sounds/hata.wav")
					return None
		    			
		def mimarlik():			
			
			goal0_4 = MoveBaseGoal()
			goal0_4.target_pose.header.frame_id = 'map'
			goal0_4.target_pose.header.stamp = rospy.Time.now()	
			goal0_4.target_pose.pose = Pose(Point(12.149, 5.525, 0.000), Quaternion(0.000, 0.000, 1.000, -0.029))
			self.move_base.send_goal(goal0_4)
			success0_4 = self.move_base.wait_for_result(rospy.Duration(120)) 	

			if not success0_4:
       	       			self.move_base.cancel_goal()
				tkMessageBox.showinfo("Hata", "Robotu kurtar!")
				os.system("aplay /home/kahya/Desktop/INTROBOT/sounds/hata.wav")
				return None
   			else:
				state0_4 = self.move_base.get_state()
				if state0_4 == GoalStatus.SUCCEEDED:
					os.system("aplay /home/kahya/Desktop/INTROBOT/sounds/mimarlik.wav")
				else:
					tkMessageBox.showinfo("Hata", "Robotu kurtar!")
					os.system("aplay /home/kahya/Desktop/INTROBOT/sounds/hata.wav")
					return None
		
			goal4_0 = MoveBaseGoal()
			goal4_0.target_pose.header.frame_id = 'map'
			goal4_0.target_pose.header.stamp = rospy.Time.now()
			goal4_0.target_pose.pose = Pose(Point(0.037, 0.009, 0.000), Quaternion(0.000, 0.000, 0.007, 1.000))
       			self.move_base.send_goal(goal4_0)
			success4_0 = self.move_base.wait_for_result(rospy.Duration(120)) 
	
			if not success4_0:
            			self.move_base.cancel_goal()
				tkMessageBox.showinfo("Hata", "Robotu kurtar!")
				os.system("aplay /home/kahya/Desktop/INTROBOT/sounds/hata.wav")
				return None
    			else:
				state4_0 = self.move_base.get_state()
				if state4_0 == GoalStatus.SUCCEEDED:
	     				#os.system("aplay /home/kahya/Desktop/INTROBOT/sounds/return.wav")
				else:
				    	tkMessageBox.showinfo("Hata", "Robotu kurtar!")
					os.system("aplay /home/kahya/Desktop/INTROBOT/sounds/hata.wav")
					return None
		
		rospy.init_node('nav_test', anonymous = False)
		self.move_base = actionlib.SimpleActionClient("move_base", MoveBaseAction)
		self.move_base.wait_for_server(rospy.Duration(3))		     			
		     			
		gui = Tk()
		gui.title("TOBB ETU - INTROBOT")
		gui.attributes('-zoomed', True)

		menubar = Menu(gui)

		recovermenu = Menu(menubar, tearoff = 0)
		menubar.add_cascade(label = "Turtlebot'u kurtar!", menu = recovermenu)
		recovermenu.add_command(label = "Başlangıç noktasına dön!", command = start_point)

		helpmenu = Menu(menubar, tearoff = 0)
		menubar.add_cascade(label = "Help", menu = helpmenu)
		helpmenu.add_command(label = "Document", command = lambda: os.system("evince /home/kahya/Desktop/INTROBOT/readme.pdf"))

		tempmenu = Menu(menubar, tearoff = 0)
		menubar.add_cascade(label = "                                                                   ", 
		menu = tempmenu, state = "disabled")

		infomenu = Menu(menubar, tearoff = 0)
		menubar.add_cascade(label="LÜTFEN BÖLÜM SEÇİNİZ", font = ("Verdana 15 bold"))

		computerimage = ImageTk.PhotoImage(PIL.Image.open('/home/kahya/Desktop/INTROBOT/images/bilgisayar.jpg'))
		computerbutton = Button(gui, command = computer_desk, image = computerimage).grid(row = 0, column = 0)

		iktisat = ImageTk.PhotoImage(PIL.Image.open('/home/kahya/Desktop/INTROBOT/images/iktisat.jpg'))
		iktisatbutton = Button(gui, command = iktisat, image = iktisat).grid(row = 0,column = 1)

		mechanicalimage = ImageTk.PhotoImage(PIL.Image.open('/home/kahya/Desktop/INTROBOT/images/makina.jpg'))
		mechanicalbutton = Button(gui, command = mechanical_desk, image = mechanicalimage).grid(row = 1, column = 0)

		mimarlik = ImageTk.PhotoImage(PIL.Image.open('/home/kahya/Desktop/INTROBOT/images/mimarlik.jpg'))
		mimarlikbutton = Button(gui, command = mimarlik, image = mimarlik).grid(row = 1, column = 1)

		gui.config(menu = menubar)
		gui.mainloop()

		os.system('rosnode kill --all')


if __name__ == '__main__':  

	time.sleep(16)

	try:
		os.system("aplay /home/kahya/Desktop/INTROBOT/sounds/hosgeldin.wav")
		GoToPose()
	except rospy.ROSInterruptException:
		tkMessageBox.showinfo("Exception", "Exception thrown")
