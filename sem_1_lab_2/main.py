from flask import Flask, render_template, request, url_for, redirect
from binary_file import BinaryFile
from directory import Directory
from bufferFile import BufferFile
from logtextfile import LogTextFile

app = Flask(__name__)
home = Directory("home")
log = LogTextFile()
log.move(home)
binary = BinaryFile(home, log, "Binn")
bufferfile = BufferFile(5, home, log, "")

@app.route('/')
def main_page():
    return render_template("main_page.html", home=home)


#####Bin block
@app.route('/binaryfile')
def binaryfile_page():
    return render_template("binaryfile.html")


@app.route('/binaryfile_create', methods=['POST', 'GET'])
def binaryfile_create():
    if request.method == 'POST':
        name = request.form['name']
        binaryfile = BinaryFile(home, log, name)
        return redirect('/')
    else:
        return render_template('binaryfile_create.html')


@app.route('/binaryfile_read/<string:name>')
def binaryfile_read(name):
    binF = ""
    for item in home.list:
        if item.get_name() == name + ".bin":
            binF = item
    if binF == "":
        return redirect('/binaryfile')
    text = binF.get_context()
    return render_template("binaryfile_read.html", text=text)


#####Buf block
@app.route('/bufferfile')
def bufferfile_page():
    return render_template("bufferfile.html")


@app.route('/bufferfile_create', methods=['POST', 'GET'])
def bufferfile_create():
    if request.method == 'POST':
        name = request.form['name']
        size = request.form['size']
        bufferfile = BufferFile(size, home, log, name)
        return redirect('/')
    else:
        return render_template('bufferfile_create.html')


@app.route('/bufferfile_read/<string:name>')
def bufferfile_read(name):
    bufF = ""
    for item in home.list:
        if item.get_name() == name + ".buf":
            bufF = item
    if bufF == "":
        return redirect('/bufferfile')
    text = bufF.get_context()
    return render_template("bufferfile_read.html", text=text)


@app.route('/bufferfile_add/<string:name_buf>', methods=['POST', 'GET'])
def bufferfile_add(name_buf):
    bufF = ""
    for item in home.list:
        if item.get_name() == name_buf + ".buf":
            bufF = item
    if bufF == "":
        return redirect('/bufferfile')

    if request.method == 'POST':
        name = request.form['name']
        bufF.append_queue(name)
        return redirect('/bufferfile_read/<string:name>')
    else:
        return render_template('bufferfile_add.html')


@app.route('/bufferfile_pop/<string:name_buf>', methods=['POST', 'GET'])
def bufferfile_pop(name_buf):
    bufF = ""
    for item in home.list:
        if item.get_name() == name_buf + ".buf":
            bufF = item
    if bufF == "":
        return redirect('/bufferfile')

    if request.method == 'POST':
        bufferfile.first_out()
        return redirect('/bufferfile_read/<string:name>')
    else:
        return render_template('bufferfile_pop.html')



#####Log block
@app.route('/logtextfile')
def logtextfile_page():
    return render_template("logtextfile.html")


@app.route('/logtextfile_create', methods=['POST', 'GET'])
def logtextfile_create():
    if request.method == 'POST':
        return redirect('/')
    else:
        return render_template('logtextfile_create.html')


@app.route('/logtextfile_read')
def logtextfile_read():
    text = log.get_context()
    return render_template("logtextfile_read.html", text=text)



if __name__ == "__main__":
    app.run(debug=True)
