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
binaryf = BinaryFile(home, log, "Bins")
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


@app.route('/binaryfile_del/<string:name>', methods=['POST', 'GET'])
def binaryfile_delete(name):
    binF = ""
    for item in home.list:
        if item.get_name() == name + ".bin":
            binF = item
    if binF == "":
        return redirect('/binaryfile')

    if request.method == 'POST':
        binF.delete()
        return redirect('/')
    else:
        return render_template("binaryfile_del.html")


@app.route('/binaryfile_move/<string:name>', methods=['POST', 'GET'])
def binaryfile_move(name):
    binF = ""
    for item in home.list:
        if item.get_name() == name + ".bin":
            binF = item
    if binF == "":
        return redirect('/binaryfile')

    if request.method == 'POST':
        name = request.form['name']
        dir = ""
        for item in home.list:
            if item.get_name() == name:
                dir = item
        if dir == "":
            return redirect('/binaryfile')

        binF.move(dir)
        return redirect('/')
    else:
        return render_template("binaryfile_move.html")



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


@app.route('/bufferfile_del/<string:name>', methods=['POST', 'GET'])
def bufferfile_delete(name):
    bufF = ""
    for item in home.list:
        if item.get_name() == name + ".buf":
            bufF = item
    if bufF == "":
        return redirect('/bufferfile')

    if request.method == 'POST':
        bufF.delete()
        return redirect('/')
    else:
        return render_template("bufferfile_del.html")


@app.route('/bufferfile_move/<string:name>', methods=['POST', 'GET'])
def bufferfile_move(name):
    bufF = ""
    for item in home.list:
        if item.get_name() == name + ".buf":
            bufF = item
    if bufF == "":
        return redirect('/bufferfile')

    if request.method == 'POST':
        name = request.form['name']
        dir = ""
        for item in home.list:
            if item.get_name() == name:
                dir = item
        if dir == "":
            return redirect('/bufferfile')

        bufF.move(dir)
        return redirect('/')
    else:
        return render_template("bufferfile_move.html")



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


@app.route('/logtextfile_del', methods=['POST', 'GET'])
def logtextfile_delete():
    if request.method == 'POST':
        return redirect('/')
    else:
        return render_template("logtextfile_del.html")



### Directory block
@app.route('/directory')
def directory_page():
    return render_template("directory.html")


@app.route('/directory_create', methods=['POST', 'GET'])
def directory_create():
    if request.method == 'POST':
        name = request.form['name']
        directory = Directory(name)
        directory.move_repository(home)
        return redirect('/')
    else:
        return render_template('directory_create.html')


@app.route('/directory_read/<string:name>')
def directory_read(name):
    dirF = ""
    for item in home.list:
        if item.get_name() == name:
            dirF = item
    if dirF == "":
        return redirect('/directory')
    list = dirF.list
    return render_template("directory_read.html", list=list)


@app.route('/directory_del/<string:name>', methods=['POST', 'GET'])
def directory_delete(name):
    dirF = ""
    for item in home.list:
        if item.get_name() == name:
            dirF = item
    if dirF == "":
        return redirect('/directory')

    if request.method == 'POST':
        home.delete_directory(dirF)
        dirF.delete()
        return redirect('/')
    else:
        return render_template("directory_del.html")


@app.route('/directory_move/<string:name>', methods=['POST', 'GET'])
def directory_move(name):
    dirF = ""
    for item in home.list:
        if item.get_name() == name:
            dirF = item
    if dirF == "":
        return redirect('/directory')

    if request.method == 'POST':
        name = request.form['name']
        dir = ""
        for item in home.list:
            if item.get_name() == name:
                dir = item
        if dir == "":
            return redirect('/directory')
        home.delete_directory(dirF)
        dirF.move_repository(dir)
        return redirect('/')
    else:
        return render_template("directory_move.html")



if __name__ == "__main__":
    app.run(debug=True)
