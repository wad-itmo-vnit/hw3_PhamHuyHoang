from flask import Flask, render_template,send_file
app= Flask (__name__)
@app.route('/')
def main():
   return render_template("index.html")

@app.route('/img/get/<numberImg>')
def getImg(numberImg):
    fileName='./static/pic/pic_'+ numberImg + '.jpg'
    return send_file(fileName)
   

app.run(host='localhost',port=5000, debug=True)