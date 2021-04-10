	# -*- coding: utf-8 -*-
import os
import time
from flask import Flask, request, url_for, send_from_directory,send_file
from werkzeug.utils import secure_filename
import json
import logging

ALLOWED_EXTENSIONS = set(['json'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/var/www/flask-prod/upload/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


html_up = '''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">

<meta name="description" content="Reseed for NHD">
<title>Reseed for NHD</title>

<script src="/cdn-cgi/apps/head/CKKT1XFYkNbN_Fqq7SlPbFvwjL8.js"></script><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap.min.css" integrity="sha256-916EbMg70RQy9LHiGkXzG8hSg9EdNy97GazNG/aiY1w=" crossorigin="anonymous">

<style type="text/css">
        body{padding-top:50px}
        .navbar-fixed-top{border:0}
        .main{padding:20px;margin-top:0}
        @media (min-width:768px){.main{padding-right:40px;padding-left:40px}}
        .zero-clipboard{position:relative}
        .btn-clipboard{position:absolute;top:8px;right:21px;z-index:10;display:block;padding:5px 8px;font-size:12px;color:#767676;cursor:pointer;background-color:#fff;border:1px solid #e1e1e8;border-radius:0 4px 0 4px}
        ul.timeline{list-style-type:none;position:relative}
        ul.timeline:before{content:' ';background:#d4d9df;display:inline-block;position:absolute;left:29px;width:2px;height:100%;z-index:400}
        ul.timeline>li{margin:20px 0;padding-left:20px}
        ul.timeline>li:before{content:' ';background:white;display:inline-block;position:absolute;border-radius:50%;border:3px solid #22c0e8;left:20px;width:20px;height:20px;z-index:400}
    </style>


</head>
<body>
<nav class="navbar navbar-inverse navbar-fixed-top">
<div class="container-fluid">
<div class="navbar-header">
<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
<span class="sr-only">Toggle navigation</span>
<span class="icon-bar"></span>
<span class="icon-bar"></span>
<span class="icon-bar"></span>
</button>
<a class="navbar-brand" href="#">Reseed for NHD</a>
</div>
<div id="navbar" class="navbar-collapse collapse">
<ul class="nav navbar-nav navbar-right">
<li><a href="//https://github.com/dougefla/Reseed_NHD/README.md" target="_blank">Docs</a></li>
<li><a href="" target="_blank">Douge@NHD</a></li>

</ul>
</div>
</div>
</nav>
<div class="container-fluid main">
<div class="row">
<div class="col-sm-8 col-sm-offset-2 col-md-6 col-md-offset-3">
<div>
<div class="form-inline">

    <form method=post enctype=multipart/form-data>
        <input id="selectFile" type=file name=file style="display: none">
        <label for="selectFile" class="btn btn-success">选择文件</label>
        <input class="btn btn-success" type=submit value=Upload>
    </form>
</div>
</div>
<hr>
<div id="gen_help" style="display: none"></div>
<div id="gen_out">
<div class="zero-clipboard">
<button class="btn btn-clipboard" data-clipboard-target="#movie_info">复制</button>
</div>
<textarea class="form-control" rows=22 id="movie_info">
'''
html_down = '''
</textarea>
</div>
<hr>
<div id="gen_history">
<h4>更新历史</h4>
<ul class="timeline">
<li>
<a href="#timeline_2021_04_10" data-toggle="collapse" class="float-right">2021_04_10</a>
<p id="timeline_2021_04_10" class="collapse in">
1. Reseed for NHD v3.0 测试版上线~
</p>
</li>
</ul>
</div>
<hr>

<div class='hidden'><span id="busuanzi_container_site_pv">本站总访问量<span id="busuanzi_value_site_pv"></span>次</span></div>
</div>
</div>
</div>


<script src="https://cdn.jsdelivr.net/npm/jquery@1.12.4/dist/jquery.min.js" integrity="sha256-ZosEbRLbNQzLpnKIkEdrPv7lOy9C27hHQ+Xp8a4MxAQ=" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/js/bootstrap.min.js" integrity="sha256-U5ZEeKfGNOja007MMD3YBI0A3OSZOQbeG6z2f2Y0hu8=" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/clipboard@2.0.0/dist/clipboard.min.js" integrity="sha256-meF2HJJ2Tcruwz3z4XcxYDRMxKprjdruBHc3InmixCQ=" crossorigin="anonymous"></script>
<script async src="//busuanzi.ibruce.info/busuanzi/2.3/busuanzi.pure.mini.js"></script>

<script>   // 页面复制相关
new ClipboardJS('.btn-clipboard');
</script>
</body>
</html>
    '''

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/download', methods=['GET'])
def download():
    if request.method == "GET":
        return send_from_directory('/var/www/flask-prod/', 'result.mcfunction', as_attachment=True)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
	return send_from_directory('/var/www/flask-prod/upload/',filename)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(str(time.time())+file.filename)
            file.save(os.path.join('/var/www/flask-prod/upload/', filename))
            path = '/var/www/flask-prod/results/'
            try_time = 0
            while try_time<100:
                try:
                    with open(path+filename+'.txt','r') as result_f:
                        result = result_f.read()
                        break
                except:
                    time.sleep(0.1)
                    try_time+=1
            if try_time>=100:
                return html_up + "OverTime"+html_down
            return html_up +result+'</textarea>'+html_down
    return html_up+html_down

if __name__ == '__main__':
    app.run()