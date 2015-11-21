#coding utf-8
import markdown
import sys
import os
from PyQt4.QtCore import QUrl
from PyQt4.QtGui import QApplication, QPrinter
from PyQt4.QtWebKit import QWebView

app = QApplication(sys.argv)
web = QWebView()
printer = QPrinter()

def load_finished():
    global web
    global printer

    web.print_(printer)
    QApplication.exit()

def md2html(_fileName):
	md=markdown.Markdown()
	tmpText = u'<html><head><meta http-equiv="Content-Type" content="text/html;charset=UTF-8"></head><body>' 
	text=""
	for i in open(_fileName,"r"):
		 text+=unicode(i,'utf-8')
	
	text=md.convert(text)
	tmpText+=text+u"</body></html>"
	fn=open("test.html","w")
	fn.write(tmpText.encode("utf-8"))
	fn.close()
	
def html2pdf():
	global app,param
	outputFile=param[1].split(".")[0]+".pdf"
	printer.setOutputFormat(QPrinter.PdfFormat)
	printer.setOrientation(QPrinter.Landscape)
	printer.setPageSize(QPrinter.A4)
	printer.setResolution(QPrinter.HighResolution)
	printer.setOutputFileName(outputFile)
	
	web.loadFinished.connect(load_finished)
	web.load(QUrl.fromLocalFile(os.path.abspath('test.html')))
	
	sys.exit(app.exec_())

def main():
	global param
	md2html(param[1])
	html2pdf()
	
if __name__=="__main__":
	param=sys.argv
	main()
	