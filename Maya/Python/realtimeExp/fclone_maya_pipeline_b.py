import maya.cmds as cmds
import random
import csv
import os
import pymel.core as pm

recstart = 0
recnow = 0
selectedBlend = ""
dataarray = []
gnumcurrenttime = 1
runstarttime = 0.0

server = None

def edit_cell(row, column, value):
	return 1

def startrealtimerec(*args):
	global recstart
	global server
	numrow = cmds.scriptTable('scrtable', query=True, rows=True)
	if len(selectedBlend) > 0 and numrow > 1:
		if recstart == 0:
			recstart = 1
			cmds.button( 'realtimerecbt' ,edit=True, label = 'Stop preview' )
			logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
			myport =  cmds.textField('Portnum', q=True, tx=True )
			server = WebSocketServer("", int(myport), WebSocket)
			server_thread = Thread(target=server.listen, args=[5])
			server_thread.start()
		else:
			recstart = 0
			cmds.button( 'realtimerecbt' ,edit=True, label = 'Real time preview' )
			server.running = False
			recnow = 0
			#cmds.button( 'nowrecbt' ,edit=True, label = 'Record motion(MAX 30 fps)' )
			
def startrec(*args):
	global recnow
	#numrow = cmds.scriptTable('scrtable', query=True, rows=True)
	if recstart == 1:
		if recnow == 0:
			recnow = 1
			global gnumcurrenttime
			gnumcurrenttime = cmds.currentTime( query=True )
			global runstarttime
			runstarttime = time.time()
			cmds.button( 'nowrecbt' ,edit=True, label = 'Stop recording' )
		else:
			recnow = 0
			cmds.button( 'nowrecbt' ,edit=True, label = 'Record motion(MAX 30 fps)' )
			
def delete_sel_row(*args):
	if recstart == 0:
		try:
			selected_row = cmds.scriptTable('scrtable', query=True, selectedRows=True)[0]
			if selected_row == None:
				print 'Select Row to Delete'
			else:
				cmds.scriptTable('scrtable', edit=True,deleteRow=selected_row)
		except:
			print 'Select Row to Delete'

def savecsvfile(*args):

	blendshapetxt = cmds.textField('selectedBlendShapeText', q=True, tx=True )
	filename = blendshapetxt + "_mayapipeline_setting.txt"
	o_file = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') + "\\"+ filename
	
	all_rows = cmds.scriptTable('scrtable', query=True, rows=True)
	
	if all_rows < 2:
		return 0
	
	if not (cmds.file(o_file,query=True, exists=True)):
		tmp_csv_file = open(o_file, 'w' ,os.O_CREAT)
	else:
		tmp_csv_file = open(o_file, 'w')
	writer = csv.writer(tmp_csv_file, lineterminator='\n')

	all_rows = cmds.scriptTable('scrtable', query=True, rows=True)
	for o_r in range(all_rows):
			
		all_colums = cmds.scriptTable('scrtable', query=True, columns=True)
		data_list = []
		for o_c in range( all_colums - 1):
			if o_r == 0:
				blendshapetxt = cmds.textField('selectedBlendShapeText', q=True, tx=True )
				headbonenametxt = cmds.textField('HeadbonenameF', q=True, tx=True )
				headxtxt = cmds.textField('HeadbonenameXF', q=True, tx=True )
				headytxt = cmds.textField('HeadbonenameYF', q=True, tx=True )
				headztxt = cmds.textField('HeadbonenameZF', q=True, tx=True )
				porttxt = cmds.textField('Portnum', q=True, tx=True )
				data_list = [blendshapetxt, headbonenametxt, headxtxt, headytxt, headztxt, porttxt]
				#data_list.append(["Target", "Link", "Receive val", "Strength", "ID(Target)", "ID(Link)"])
			else:
				cell_list = cmds.scriptTable('scrtable', cellIndex=(o_r,o_c + 1), query=True, cellValue=True)
				if o_c == 0:
					if type(cell_list) == list:
						cell_text = "".join(cell_list)
						print cell_text
					elif cell_list == None:
						cell_text = u''
					else:
						cell_text = cell_list
					data_list.append(cell_text)
				elif o_c == 1:
					if type(cell_list) == list:
						cell_text = "".join(cell_list)
						print cell_text
					elif cell_list == None:
						cell_text = u''
					else:
						cell_text = cell_list
					data_list.append(cell_text)
				else:
					if type(cell_list) == list:
						cell_text = "".join(cell_list)
					elif cell_list == None:
						cell_text = u''
					else:
						cell_text = cell_list
					data_list.append(cell_text)
		writer.writerow(data_list)
	tmp_csv_file.close()
	cmds.warning( "Saved file (" +o_file+ ")" )

def loadpresetfile(*args):
	if recstart != 0:
		return 0
	
	presetfile = pm.fileDialog2(fileMode=1)
	
	if presetfile:
	
		cmds.scriptTable('scrtable', edit=True, selectedRows=[])
		
		o_file = open(str(presetfile[0]), 'r')
		reader = csv.reader(o_file)
		#header = next(reader)
		
		all_rows = cmds.scriptTable('scrtable', query=True, rows=True)
		for o_r in range(all_rows):
			cmds.scriptTable('scrtable', edit=True,deleteRow= o_r)
	
		row_no = 0
		for row in reader:
			if row_no > 0:
				cmds.scriptTable('scrtable', edit=True,insertRow=row_no)
				cmds.scriptTable('scrtable', cellIndex=(row_no,1), edit=True, cellValue=row[0])
				cmds.scriptTable('scrtable', cellIndex=(row_no,2), edit=True, cellValue=row[1])
				cmds.scriptTable('scrtable', cellIndex=(row_no,3), edit=True, cellValue="0")
				cmds.scriptTable('scrtable', cellIndex=(row_no,4), edit=True, cellValue=row[3])
				cmds.scriptTable('scrtable', cellIndex=(row_no,5), edit=True, cellValue=row[4])
				cmds.scriptTable('scrtable', cellIndex=(row_no,6), edit=True, cellValue=row[5])
			else:
				cmds.textField('selectedBlendShapeText', edit=True, text=row[0] )
				cmds.textField('HeadbonenameF', edit=True, text=row[1] )
				cmds.textField('HeadbonenameXF', edit=True, text=row[2] )
				cmds.textField('HeadbonenameYF', edit=True, text=row[3] )
				cmds.textField('HeadbonenameZF', edit=True, text=row[4] )
				cmds.textField('Portnum', edit=True, text=row[5] )
				loadTargetList()
			row_no = 1 + row_no
		o_file.close()
	
def loadfclonemotion(*args):
	
	all_rows = cmds.scriptTable('scrtable', query=True, rows=True)
	global recstart
	if all_rows > 1 and recstart == 0:
		
		motionfile = pm.fileDialog2(fileMode=1)
		cmds.currentUnit( time='ntsc' )
		numcurrenttime = cmds.currentTime( query=True )
		
		if motionfile:
			o_file = open(str(motionfile[0]), 'r')
			reader = csv.reader(o_file)
			#header = next(reader)
			
			row_no = 0
			for row in reader:
				if row_no > 0 and len(row)>5:
					
					bonename = cmds.textField('HeadbonenameF', q=True, tx=True )
		
					if len(bonename) > 0:
						cX = cmds.textField('HeadbonenameXF', q=True, tx=True )
						cY = cmds.textField('HeadbonenameYF', q=True, tx=True )
						cZ = cmds.textField('HeadbonenameZF', q=True, tx=True )
						CrX = 0;
						CrY = 0;
						CrZ = 0;
						if cX.replace(".","").isdigit():
							CrX = float(cX);
						if cY.replace(".","").isdigit():
							CrY = float(cY);
						if cZ.replace(".","").isdigit():
							CrZ = float(cZ);
						
						bjoint = pm.PyNode(bonename)
						#pm.rotate(bjoint, [float(row[1])*-1+CrX ,float(row[2])*-1+CrY,float(row[3])*-1+CrZ], euler= True,a=True, ws=False) 
						pm.setKeyframe(bjoint, v=float(row[1])*-1+CrX, attribute='rotateX', t=[str(row_no+numcurrenttime-1)+"ntsc"])
						pm.setKeyframe(bjoint, v=float(row[2])*-1+CrY, attribute='rotateY', t=[str(row_no+numcurrenttime-1)+"ntsc"])
						pm.setKeyframe(bjoint, v=float(row[3])*-1+CrZ, attribute='rotateZ', t=[str(row_no+numcurrenttime-1)+"ntsc"])
						
					for o_r in range(all_rows):
						all_colums = cmds.scriptTable('scrtable', query=True, columns=True)
						data_list = []
						for o_c in range(all_colums):
							cell_list = cmds.scriptTable('scrtable', cellIndex=(o_r,o_c), query=True, cellValue=True)
							if type(cell_list) == 'list':
								cell_text = "".join(cell_list)
							elif cell_list == None:
								cell_text = cell_list
							else:
								cell_text = cell_list[0]

							data_list.append(cell_text)
						#print(data_list)
						if o_r > 0:
							streng = 1.0
							if data_list[4].replace(".","").isdigit():
								streng = float(data_list[4])
							recdataDeformStreng = (((float(row[int(data_list[6])-2+3+1]))+0.0)/100.0)*(streng+0.0)
							targetdefnum = int(data_list[5])-2;
							cmds.blendShape( selectedBlend, edit=True, w=[(targetdefnum, recdataDeformStreng)] )
							cmds.setKeyframe("%s.w[%i]" %(selectedBlend,targetdefnum),t=str(row_no+numcurrenttime-1)+"ntsc")

				row_no = 1 + row_no
			o_file.close()
		

def poseTrackerWindow():
	if cmds.window( 'fcloneMAYApipeline', exists = True ):
		cmds.deleteUI( 'fcloneMAYApipeline')

	#window definition
	cmds.window( 'fcloneMAYApipeline', widthHeight = ( 600, 450 ), title = 'f-clone MAYA pipeline(Beta)', minimizeButton = False, maximizeButton = False, resizeToFitChildren = True, sizeable = True )
	
	cmds.rowColumnLayout(numberOfColumns = 3, columnWidth = [(1,200), (2, 200), (3, 200)])
				
	#select an existing blendShape node
	cmds.text( label='Blend Shape node name' )
	selectedBlendShapeTextField = cmds.textField( 'selectedBlendShapeText' )
	cmds.button( label = 'Load Targets', command = 'loadTargetList()' )

	
	cmds.text( label='' )
	cmds.text( label='' )
	cmds.text( label='' )

	
	targetList = cmds.optionMenu( 'targetObjectMenu', label='Target' )
	cmds.menuItem(label=' ' )
	fcloneList = cmds.optionMenu( 'fcloneObjectMenu', label='Link' )
	cmds.menuItem(label='Please select f-clone param' )
	cmds.menuItem(label='Brow Left UP')
	cmds.menuItem(label='Brow Left Down')
	cmds.menuItem(label='Brow Right UP')
	cmds.menuItem(label='Brow Right Down')
	cmds.menuItem(label='Brow Centering')
	cmds.menuItem(label='Brow outer left down')
	cmds.menuItem(label='Brow outer right down')
	cmds.menuItem(label='Eye Close Left')
	cmds.menuItem(label='Eye Close Right')
	cmds.menuItem(label='Mouse Open')
	cmds.menuItem(label='Mouse Left Smile')
	cmds.menuItem(label='Mouse Right Smile')
	cmds.menuItem(label='Mouse Left Spread')
	cmds.menuItem(label='Mouse Right Spread')
	cmds.menuItem(label='Mouse Left Frawn')
	cmds.menuItem(label='Mouse Right Frawn')
	cmds.menuItem(label='Mouse Left Centering')
	cmds.menuItem(label='Mouse Right Centering')
	cmds.menuItem(label='Cheek Left UP')
	cmds.menuItem(label='Cheek Right UP')
	cmds.button( label = 'Add link', command = 'addlink()' )
	
	cmds.text( label='' )
	cmds.text( label='' )
	cmds.text( label='' )
	
	cmds.columnLayout('mytable', width=600)

	table =  cmds.scriptTable('scrtable',rows=0, columns=6,columnWidth=([1,200],[2,200],[3,99],[4,99],[5,1],[6,1]),
		label=[(1,"Target"), (2,"Link"), (3,"Receive val"), (4,"Strength"), (5,"ID(Target)"), (6,"ID(Link)")], width=600,
		cellChangedCmd=edit_cell)
	
	cmds.rowColumnLayout(numberOfColumns = 3, columnWidth = [(1,100),(2, 250), (3, 250)])
	

	cmds.text( label='' )
	cmds.text( label='' )
	cmds.button( label = 'Delete select row',command=delete_sel_row )
	

	cmds.text( label='' )
	cmds.text( label='' )
	cmds.text( label='' )
	

	cmds.text( label='' )
	cmds.text( label='Head bone name' )
	Headbonename = cmds.textField('HeadbonenameF')


	cmds.text( label='' )
	cmds.text( label='Head bone rotation compensation X' )
	HeadbonenameX = cmds.textField('HeadbonenameXF',text='0')


	cmds.text( label='' )
	cmds.text( label='Head bone rotation compensation Y' )
	HeadbonenameY = cmds.textField('HeadbonenameYF',text='0')
	

	cmds.text( label='' )
	cmds.text( label='Head bone rotation compensation Z' )
	HeadbonenameZ = cmds.textField('HeadbonenameZF',text='0')
	

	cmds.text( label='' )
	cmds.text( label='' )
	cmds.text( label='' )
	
	cmds.text( label='' )
	cmds.text( label='' )
	cmds.button( label = 'Load f-clone motion csv (30 fps)', command = loadfclonemotion )
	
	
	cmds.text( label='' )
	cmds.text( label='' )
	cmds.text( label='' )
	
	cmds.text( label='' )
	cmds.text( label='Server port' )
	HeadbonenameZ = cmds.textField('Portnum',text='8080')

	cmds.text( label='' )
	cmds.text( label='' )
	cmds.button( 'realtimerecbt' , label = 'Real time preview', command = startrealtimerec )
	#cmds.button( 'nowrecbt' , label = 'Record motion(MAX 30 fps)', command = startrec )
	
	
	cmds.text( label='' )
	cmds.text( label='' )
	cmds.text( label='' )
	

	cmds.text( label='' )
	cmds.button( label = 'Save preset', command = savecsvfile )
	cmds.button( label = 'Load preset', command = loadpresetfile )
	
	cmds.showWindow( 'fcloneMAYApipeline' )
	
	
	
poseTrackerWindow()

# 여기 위에까지가 윈도우 창 만드는거

#function that loads target list to the UI

def loadTargetList():
	
	global selectedBlend
	selectedBlend = cmds.textField('selectedBlendShapeText', q=True, tx=True )
	
	existingItems = cmds.optionMenu( 'targetObjectMenu', q=True, itemListLong=True )
	if existingItems != None and existingItems != []:
		cmds.deleteUI(existingItems)
	
	cmds.menuItem(label='Please select blendShape', parent='targetObjectMenu')
	

	blendTargets = cmds.listAttr (selectedBlend + '.w', m = True)
	for target in blendTargets:
		cmds.menuItem(label='%s' %(target), parent='targetObjectMenu')


def addlink():
	if recstart == 0:
		selectedBlend = cmds.optionMenu('targetObjectMenu', query=True, value=True )
		selectedBlendI = cmds.optionMenu('targetObjectMenu', query=True, select=True )
		selectedLinkBlend = cmds.optionMenu('fcloneObjectMenu', query=True, value=True )
		selectedLinkBlendI = cmds.optionMenu('fcloneObjectMenu', query=True, select=True )
		
		if selectedBlendI > 1 and selectedLinkBlendI > 1:
			add_row();
			#print(selectedBlend);


def add_row(*args):

	cmds.scriptTable('scrtable', edit=True, selectedRows=[])
	
	selectedBlend = cmds.optionMenu('targetObjectMenu', query=True, value=True )
	selectedBlendI = cmds.optionMenu('targetObjectMenu', query=True, select=True )
	selectedLinkBlend = cmds.optionMenu('fcloneObjectMenu', query=True, value=True )
	selectedLinkBlendI = cmds.optionMenu('fcloneObjectMenu', query=True, select=True )
	
	last_row_num = cmds.scriptTable('scrtable', query=True, rows=True)
	cmds.scriptTable('scrtable', edit=True,insertRow=last_row_num)
	
	cmds.scriptTable('scrtable', e=True, ci=[last_row_num, 1], cv=selectedBlend)
	cmds.scriptTable('scrtable', e=True, ci=[last_row_num, 2], cv=selectedLinkBlend)
	cmds.scriptTable('scrtable', e=True, ci=[last_row_num, 3], cv='0')
	cmds.scriptTable('scrtable', e=True, ci=[last_row_num, 4], cv='1')
	cmds.scriptTable('scrtable', e=True, ci=[last_row_num, 5], cv=selectedBlendI)
	cmds.scriptTable('scrtable', e=True, ci=[last_row_num, 6], cv=selectedLinkBlendI)

import time
import struct
import socket
import hashlib
import base64
import sys
from select import select
import re
import logging
from threading import Thread
import signal

# Simple WebSocket server implementation. Handshakes with the client then echos back everything
# that is received. Has no dependencies (doesn't require Twisted etc) and works with the RFC6455
# version of WebSockets. Tested with FireFox 16, though should work with the latest versions of
# IE, Chrome etc.
#
# rich20b@gmail.com
# Adapted from https://gist.github.com/512987 with various functions stolen from other sites, see
# below for full details.

# Constants
TEXT = 0x01
BINARY = 0x02

import pymel.core as pm

def deformface():
	global dataarray 
	if len(dataarray) < 3:
		return 0
		
	all_rows = cmds.scriptTable('scrtable', query=True, rows=True)
	global recstart
	global gnumcurrenttime
	if all_rows > 1 and recstart == 1:
		#print(recvtxt)
		ornum = 1;
		
		numcurrenttime = gnumcurrenttime
		bonename = cmds.textField('HeadbonenameF', q=True, tx=True )
		
		if len(bonename) > 0:
			cX = cmds.textField('HeadbonenameXF', q=True, tx=True )
			cY = cmds.textField('HeadbonenameYF', q=True, tx=True )
			cZ = cmds.textField('HeadbonenameZF', q=True, tx=True )
			CrX = 0;
			CrY = 0;
			CrZ = 0;
			if cX.replace(".","").isdigit():
				CrX = float(cX);
			if cY.replace(".","").isdigit():
				CrY = float(cY);
			if cZ.replace(".","").isdigit():
				CrZ = float(cZ);
			
			bjoint = pm.PyNode(bonename)
			pm.rotate(bjoint, [float(dataarray[0])*-1+CrX ,float(dataarray[1])*-1+CrY,float(dataarray[2])*-1+CrZ], euler= True,a=True, ws=False)
			if recnow == 1:
				pm.setKeyframe(bjoint, v=float(row[1])*-1+CrX, attribute='rotateX', t=[numcurrenttime])
				pm.setKeyframe(bjoint, v=float(row[2])*-1+CrY, attribute='rotateY', t=[numcurrenttime])
				pm.setKeyframe(bjoint, v=float(row[3])*-1+CrZ, attribute='rotateZ', t=[numcurrenttime])
		
		for o_r in range(all_rows):
			all_colums = cmds.scriptTable('scrtable', query=True, columns=True)
			data_list = []
			for o_c in range(all_colums):
				cell_list = cmds.scriptTable('scrtable', cellIndex=(o_r,o_c), query=True, cellValue=True)
				if type(cell_list) == 'list':
					cell_text = "".join(cell_list)
				elif cell_list == None:
					cell_text = cell_list
				else:
					cell_text = cell_list[0]

				data_list.append(cell_text)
			#print(data_list)
			if o_r > 0 and len(dataarray) > 3:
				streng = 1.0
				if data_list[4].replace(".","").isdigit():
					streng = float(data_list[4])
				recdataDeformStreng = (((float(dataarray[int(data_list[6])-2+3]))+0.0)/100.0)*(streng+0.0)
				targetdefnum = int(data_list[5])-2;
				cmds.blendShape( selectedBlend, edit=True, w=[(targetdefnum, recdataDeformStreng)] )
				if recnow == 1:
					cmds.setKeyframe("%s.w[%i]" %(selectedBlend,targetdefnum),t=numcurrenttime)
				
				if random.random() < 0.2:
					datastring = '%.4f' % recdataDeformStreng
					cmds.scriptTable('scrtable', e=True, ci=[o_r, 3], cv=datastring)
				


# WebSocket implementation
class WebSocket(object):

	handshake = (
		"HTTP/1.1 101 Web Socket Protocol Handshake\r\n"
		"Upgrade: WebSocket\r\n"
		"Connection: Upgrade\r\n"
		"Sec-WebSocket-Accept: %(acceptstring)s\r\n"
		"Server: TestTest\r\n"
		"Access-Control-Allow-Origin: http://localhost\r\n"
		"Access-Control-Allow-Credentials: true\r\n"
		"\r\n"
	)


	# Constructor
	def __init__(self, client, server):
		self.client = client
		self.server = server
		self.handshaken = False
		self.header = ""
		self.data = ""


	# Serve this client
	def feed(self, data):
	
		# If we haven't handshaken yet
		if not self.handshaken:
			logging.debug("No handshake yet")
			self.header += data
			if self.header.find('\r\n\r\n') != -1:
				parts = self.header.split('\r\n\r\n', 1)
				self.header = parts[0]
				if self.dohandshake(self.header, parts[1]):
					logging.info("Handshake successful")
					self.handshaken = True

		# We have handshaken
		else:
			#logging.debug("Handshake is complete")
			
			global selectedBlend
			# Decode the data that we received according to section 5 of RFC6455
			recv = self.decodeCharArray(data)
			recvtxt = ''.join(recv)
			
			global dataarray
			dataarray = recvtxt.split(",")
			#maya.utils.executeDeferred(deformface);
			#deformface(dataarray)
							
							
			# Send our reply
			#self.sendMessage(''.join(recv).strip());


	# Stolen from http://www.cs.rpi.edu/~goldsd/docs/spring2012-csci4220/websocket-py.txt
	def sendMessage(self, s):
		"""
		Encode and send a WebSocket message
		"""

		# Empty message to start with
		message = ""
		
		# always send an entire message as one frame (fin)
		b1 = 0x80

		# in Python 2, strs are bytes and unicodes are strings
		if type(s) == unicode:
			b1 |= TEXT
			payload = s.encode("UTF8")
			
		elif type(s) == str:
			b1 |= TEXT
			payload = s

		# Append 'FIN' flag to the message
		message += chr(b1)

		# never mask frames from the server to the client
		b2 = 0
		
		# How long is our payload?
		length = len(payload)
		if length < 126:
			b2 |= length
			message += chr(b2)
		
		elif length < (2 ** 16) - 1:
			b2 |= 126
			message += chr(b2)
			l = struct.pack(">H", length)
			message += l
		
		else:
			l = struct.pack(">Q", length)
			b2 |= 127
			message += chr(b2)
			message += l

		# Append payload to message
		message += payload

		# Send to the client
		self.client.send(str(message))


	# Stolen from http://stackoverflow.com/questions/8125507/how-can-i-send-and-receive-websocket-messages-on-the-server-side
	def decodeCharArray(self, stringStreamIn):
	
		# Turn string values into opererable numeric byte values
		byteArray = [ord(character) for character in stringStreamIn]
		datalength = byteArray[1] & 127
		indexFirstMask = 2

		if datalength == 126:
			indexFirstMask = 4
		elif datalength == 127:
			indexFirstMask = 10

		# Extract masks
		masks = [m for m in byteArray[indexFirstMask : indexFirstMask+4]]
		indexFirstDataByte = indexFirstMask + 4
		
		# List of decoded characters
		decodedChars = []
		i = indexFirstDataByte
		j = 0
		
		# Loop through each byte that was received
		while i < len(byteArray):
		
			# Unmask this byte and add to the decoded buffer
			decodedChars.append( chr(byteArray[i] ^ masks[j % 4]) )
			i += 1
			j += 1

		# Return the decoded string
		return decodedChars


	# Handshake with this client
	def dohandshake(self, header, key=None):
	
		logging.debug("Begin handshake: %s" % header)
		
		# Get the handshake template
		handshake = self.handshake
		
		# Step through each header
		for line in header.split('\r\n')[1:]:
			name, value = line.split(': ', 1)
			
			# If this is the key
			if name.lower() == "sec-websocket-key":
			
				# Append the standard GUID and get digest
				combined = value + "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"
				response = base64.b64encode(hashlib.sha1(combined).digest())
				
				# Replace the placeholder in the handshake response
				handshake = handshake % { 'acceptstring' : response }

		logging.debug("Sending handshake %s" % handshake)
		self.client.send(handshake)
		return True

	def onmessage(self, data):
		#logging.info("Got message: %s" % data)
		self.send(data)

	def send(self, data):
		logging.info("Sent message: %s" % data)
		self.client.send("\x00%s\xff" % data)

	def close(self):
		self.client.close()


# WebSocket server implementation
class WebSocketServer(object):

	# Constructor
	def __init__(self, bind, port, cls):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.socket.bind((bind, port))
		self.bind = bind
		self.port = port
		self.cls = cls
		self.connections = {}
		self.listeners = [self.socket]

	# Listen for requests
	def listen(self, backlog=5):

		self.socket.listen(backlog)
		logging.info("Listening on %s" % self.port)

		# Keep serving requests
		self.running = True
		while self.running:
		
			# Find clients that need servicing
			rList, wList, xList = select(self.listeners, [], self.listeners, 1)
			for ready in rList:
				if ready == self.socket:
					logging.debug("New client connection")
					client, address = self.socket.accept()
					fileno = client.fileno()
					self.listeners.append(fileno)
					self.connections[fileno] = self.cls(client, self)
				else:
					#logging.debug("Client ready for reading %s" % ready)
					client = self.connections[ready].client
					
					try:
						data = client.recv(4096)
					except socket.error, e:
						data = None

					fileno = client.fileno()
					if data:
						self.connections[fileno].feed(data)
					else:
						logging.debug("Closing client %s" % ready)
						self.connections[fileno].close()
						del self.connections[fileno]
						self.listeners.remove(ready)
			
			# Step though and delete broken connections
			for failed in xList:
				if failed == self.socket:
					logging.error("Socket broke")
					for fileno, conn in self.connections:
						conn.close()
					self.running = False




# Add SIGINT handler for killing the threads
def signal_handler(signal, frame):
	logging.info("Caught Ctrl+C, shutting down...")
	server.running = False
	sys.exit()

signal.signal(signal.SIGINT, signal_handler)


def createTimer(seconds, function, *args, **kwargs):
	def isItTime():
		now = time.time()
		if now - isItTime.then > seconds:
			isItTime.then = now			# swap the order of these two lines ...
			function(*args, **kwargs)	  # ... to wait before restarting timer

	isItTime.then = time.time() # set this to zero if you want it to fire once immediately
	cmds.scriptJob(event=("idle", isItTime))

createTimer(0.03, deformface)

oldframe = 0

def createTimer2(seconds, *args, **kwargs):
	def isItTime2():
		global gnumcurrenttime
		global runstarttime
		global oldframe
		now = time.time()
		if now - isItTime2.then > seconds:
			isItTime2.then = now			# swap the order of these two lines ...
			cframe = gnumcurrenttime+int((now-runstarttime)/0.0333)
			if cframe != oldframe and recnow == 1:
				#cmds.currentTime( cframe , edit=True )
				oldframe = cframe

	isItTime2.then = time.time() # set this to zero if you want it to fire once immediately
	cmds.scriptJob(event=("idle", isItTime2))

#createTimer2(0.01)


