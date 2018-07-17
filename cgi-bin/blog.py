import cgi
import cgitb
import sqlite3
from re import split
from datetime import datetime
from cgi_templates import *

cgitb.enable()

def strfmt_ts(timestr):
    '''helps format raw datetime str eg. July, 16, 2018 4.00pm'''
    ts_arg = [int(x) for x in split("-|\s|:", timestr)[:-1]]
    dateobj = datetime(*ts_arg)
    strfmt = dateobj.strftime("%b, %d, %Y %I:%M%p")
    return strfmt

def retrieve_post_data(title="", body=""):
    '''function to post and retrieve well sorted and formated data'''
    cxn = sqlite3.connect(r'c:\Users\HP-USER\Desktop\simpleBlogPost\Ablog.db')
    cur = cxn.cursor()
    cur.execute("SELECT * FROM blogpost")
    
    rows = [(row[0],strfmt_ts(row[1]), row[2]) for row in
            sorted(cur.fetchall(), key=lambda i: i[1], reverse=True)[:10]]

    if title and body: #check for storage fields!
        try:
            if (rows[0][0],rows[0][2])!=(title,body):
                cur.execute("INSERT INTO blogpost VALUES(?, ?, ?)",
                       (title, datetime.now(), body))
        except(IndexError):
            cur.execute("INSERT INTO blogpost VALUES(?, ?, ?)",
                       (title, datetime.now(), body))
        finally:
            rows.insert(0, (title, strfmt_ts(str(datetime.now())), body))
            cxn.commit()
    cur.close()
    cxn.close()
    return rows;

def main():
    ord_rows = retrieve_post_data()
    form = cgi.FieldStorage()
    if 'title' and 'body'  in form:
        title = form['title'].value
        body = form['body'].value
        ord_rows = retrieve_post_data(title, body)

    # generate dynamic html for showing timestamps and titles and body for blogs!
    all_blog_body = ''
    for row in ord_rows:
        all_blog_body += bp_temp.format(*row)
        
    print(header+blog_body.format(blog_form, all_blog_body))

main()

