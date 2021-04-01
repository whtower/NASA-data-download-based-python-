from selenium import webdriver as wbder
from selenium.webdriver.chrome.options import Options
import time


class NasaGet:
    def __init__(self, inputFilePath, outputFilePath, bz):
        self.inputFilePath = inputFilePath
        self.outputFilePath = outputFilePath
        self.bz = bz
        self.gner=''#ghelper账号/Ghelper account
        self.gpassw=''#ghelper密码/Ghelper password
        self.NASAusr=''#NASA账号/NASA's account
        self.NASApasse=''#NASA密码/NASA's password
    def done(self):
        import os
        opt = Options()
        isExists = os.path.exists(self.outputFilePath)
        if not isExists:
            os.makedirs(self.outputFilePath)
        prefs = {'profile.default_content_settings.popups': 0,  # 防止保存弹窗/Prevent saving pop-ups
                 'download.default_directory': self.outputFilePath,  # 设置默认下载路径/Set the default download path
                 "profile.default_content_setting_values.automatic_downloads": 1  # 允许多文件下载/Allows multiple file downloads
                 }
        opt.add_argument('-ignore-certificate-errors')
        opt.add_argument('-ignore -ssl-errors')
        opt.add_experimental_option('prefs', prefs)
        extension_path = './resource/Ghelper_2.5.5/ghelper_2.5.5.crx'  # ghelper
        opt.add_extension(extension_path)
        extension_path = './resource/mciiogijehkdemklbdcbfkefimifhecn/mciiogijehkdemklbdcbfkefimifhecn_0.11.1_chrome' \
                         '.zzzmh.cn.crx'  # chrono
        opt.add_extension(extension_path)

        f = True
        while f:
            driver = wbder.Chrome(chrome_options=opt)
            driver.set_window_size(300, 300)#浏览器窗口大小/Browser Window Size
            driver.get('chrome-extension://cieikaeocafmceoapfogpffaalkncpkc/options.html?/login')
            driver.implicitly_wait(30)
            driver.find_element_by_name('email').send_keys(self.gner)  
            driver.find_element_by_name('password').send_keys(self.gpassw)
            driver.find_element_by_css_selector("[class = 'btn btn-lg btn-primary btn-block']").click()
            time.sleep(2)
            linkOfNASA='http://'+self.NASAusr+':'+self.NASApasse+'@urs.earthdata.nasa.gov'
            js2 = 'window.open("{}");'.format(linkOfNASA)
            driver.execute_script(js2)
            windows = driver.window_handles
            driver.switch_to_window(windows[-1])
            driver.implicitly_wait(30)
            driver.find_element_by_id('username').send_keys(self.NASAusr)
            driver.find_element_by_id('password').send_keys(self.NASApasse)
            driver.find_element_by_css_selector("[class = 'eui-btn--round eui-btn--green']").click()
            driver.implicitly_wait(30)

            numOfTxt = 0
            # 数据下载部分/Data Download
            files = open(self.inputFilePath)
            filesOfData = os.listdir(self.outputFilePath)
            length = len(self.bz)
            if filesOfData:  # 删除下载中断的文件/Delete the file whose download was interrupted
                for k in filesOfData:
                    n = k[len(k) - length:len(k) + 1]
                    if n != self.bz:
                        p = self.outputFilePath + '\\' + k
                        if os.path.exists(p):
                            os.remove(p)
                            print(k, '--->Delete the success')
                        else:
                            print("The file does not exist")
            inte = True
            while inte:
                line = files.readline()
                line = line.rstrip("\n")
                if line:
                    numOfTxt += 1
                    if line.split('/')[-1] not in filesOfData:
                        js3 = 'window.open("{}");'.format(line)
                        driver.execute_script(js3)
                        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), '--------',
                              line.split('/')[-1])
                        driver.implicitly_wait(30)
                        time.sleep(5)
                else:
                    time.sleep(180)
                    filesOfData = os.listdir(self.outputFilePath)
                    if len(filesOfData) == numOfTxt:
                        print('The data has been loaded. Please check whether it has been downloaded in the download folder')
                        f = False
                    else:
                        print('WARNING!--->Data incomplete, continue downloading')
                    inte = False


if __name__ == '__main__':
    inputFilePath=''#存放数据链接的txt文件绝对路径/The absolute path to the TXT file that holds the data link
    outputFilePath=''#下载文件保存的绝对路径/The absolute path to save the download file
    bz=''#下载文件的后缀名,包含后缀名前的点 例如：.hdf     /The suffix name of the download file, including the dot before the suffix name such as:    .hdf
    n = NasaGet(inputFilePath=inputFilePath, outputFilePath=outputFilePath,
                bz=bz)
    n.done()
