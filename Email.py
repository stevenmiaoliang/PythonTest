from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

from_addr = raw_input('From: ')
password = raw_input('Password: ')
to_addr = raw_input('To: ')
smtp_server = 'smtp.gmail.com'
#smtp_server = raw_input('SMTP server: ')


msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg = MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8')
msg = MIMEMultipart()
msg['From'] = _format_addr(u'Python Lover <%s>' % from_addr)
msg['To'] = _format_addr(u'Administrator <%s>' % to_addr)
msg['Subject'] = Header(u'Come from STMP Hello', 'utf-8').encode()

msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))


with open('lena.bmp', 'rb') as f:
    mime = MIMEBase('image', 'bmp', filename='lena.bmp')
    mime.add_header('Content-Disposition', 'attachment', filename='test.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)


smtp_port = 587
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()

#server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
print "End Server"