
blog_body = '''
<html>
<head>
	<style>
            body {{
                font-size: 80%;
                font-family: "Courier New", Courier, monospace;
                letter-spacing: 0.15em;
                background-color: #efefef;}}
	
            #page {{
                    margin: 10px auto 10px auto;
                    width: 90%;
                    height: 1000%;
                    position: relative;
                    padding: 20px;
                    border: 4px double #000;
                    background-color: #ffffff;}}

            p {{
                    text-align: left;
                    width: 450px;
                    font-weight: normal;}}

            .text {{
                    float: left;
                    text-align: right;
                    padding-right: 9px;}}
            
	</style>
</head>
<body>
    <div id="page">
	<! -- body section />
	<p>{0}</p>
	<p>{1}</p>
	<! -- body section ends />
    </div>
</body>
</html>
'''

blog_form = '''
  <div id="blog_form">
  <form action="/cgi-bin/blog.py" method="post">
    <table><label for="title" class="title"><b>Title:</b></label>
    <input type=text name=title /><br>
    <input type=hidden name=action/>
    <label for="body" class="text"><b>Body:</b></label>
    <textarea id="body" name=body rows="10" cols="40"></textarea></table><br>
    <input type=submit />
  </form>
  </div>
  <hr>
'''

bp_temp = '''
<h2>{0}</h2>
<p>{1}</p>
<p>{2}</p>
<hr>
'''

header = '''Content-Type: text/html\n\n'''
