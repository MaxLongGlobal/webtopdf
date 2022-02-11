
import pdfkit

# if sys.argv[-1] != ASADMIN:
#     script = os.path.abspath(sys.argv[0])
#     params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
#     shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable,     lpParameters=params)
#     sys.exit(0)

# CLIENT_LOCATION 是定义的一个存放地址的属性
CLIENT_LOCATION = "E:\wkhtmltopdf\wkhtmltox-0.12.6-1.msvc2015-win64.exe"
# subprocess.Popen([CLIENT_LOCATION, ".out_2.pdf"])

'''将html文件生成pdf文件'''
def html_to_pdf(html, to_file):
    # 将wkhtmltopdf.exe程序绝对路径传入config对象
    path_wkthmltopdf = r".\path\wkhtmltopdf\bin\wkhtmltopdf.exe"
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    print('start to download ...')
    # 生成pdf文件，to_file为文件路径
    pdfkit.from_url(html, to_file, configuration=config)
    print('download 100%')


if __name__ == '__main__':
    title = input("Please input pdf_Name:")
    url = input("Please input pdf_URL:")

    html_to_pdf(url, title + '.pdf')