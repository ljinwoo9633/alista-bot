from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from urllib.request import urlretrieve
from urllib.error import HTTPError
from urllib.error import URLError

from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

import tkinter.messagebox

import time
import os
import random

def AliexpressCorePart(url):
    downloadDirectory = 'downloaded'
    baseUrl = url

    options = webdriver.ChromeOptions()
    options.add_argument('headless')

    driver = webdriver.Chrome(executable_path='chromedriver.exe', options=options)
    driver.get(baseUrl)
    driver.implicitly_wait(5)

    try:
        close_btn = driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/a')
    except NoSuchElementException as e:
        #close Btn 이 없는 경우
        driver.implicitly_wait(10)

        for i in range(1, 30):
            driver.execute_script("window.scrollTo(0, {})".format(1000*i))
            time.sleep(1)
        
        pageSource = driver.page_source
        bs = BeautifulSoup(pageSource, 'html.parser')
        
        image_tags = bs.findAll('img', {'src': True})
        
        image_urls = []

        for image_tag in image_tags:
            image_urls.append(image_tag['src'])
            
        string1 = '480x480'
        string2 = '50x50'
        string3 = '120x120'
        string4 = '200x200'
        string5 = '220x220'

        edited_urls1 = []
        edited_urls2 = []
        edited_urls3 = []
        edited_urls4 = []


        final_urls = []

        try:
            for image_url in image_urls:
                if string1 not in image_url:
                    edited_urls1.append(image_url)
            
            del(image_urls)
            
            for edited_url1 in edited_urls1:
                if string2 not in edited_url1:
                    edited_urls2.append(edited_url1)

            del(edited_urls1)

            for edited_url2 in edited_urls2:
                if string3 not in edited_url2:
                    edited_urls3.append(edited_url2)

            del(edited_urls2)

            for edited_url3 in edited_urls3:
                if string4 not in edited_url3:
                    edited_urls4.append(edited_url3)

            del(edited_urls3)

            for edited_url4 in edited_urls4:
                if string5 not in edited_url4:
                    final_urls.append(edited_url4)

        except UnboundLocalError as e:
            print('[-]Something Went Wrong! : {}'.format(e))
            tkinter.messagebox.showerror('ERROR', 'mow...')
            driver.quit()

        #Extract The Title
        productName_not_split = bs.find('div', {'class': 'product-title'}).get_text()
        productName_list = productName_not_split.split()
        productName = str(productName_list[0]) + '+' + str(random.randint(0, 1000)) + '+' + str(productName_list[1])

        video_tags = bs.findAll('video', {'src': True})
        
        video_urls = []

        for video_tag in video_tags:
            video_urls.append(video_tag['src'])

        #Download The Video
        if len(video_urls) == 0:
            print('[-]There Is No Video')
            pass
        else:
            #Make Video Directory And Download
            path = downloadDirectory + '/' + 'aliexpress' + '/' + str(productName) + '/' + 'video'
            if not os.path.exists(path):
                os.makedirs(path)

            video_number = 0
            for video_url in video_urls:
                video_number = video_number + 1
                try:
                    urlretrieve(str(video_url), './downloaded/aliexpress/{}/video/{}.mp4'.format(productName, video_number))
                except HTTPError as e:
                    print(e)
                    pass
                except URLError as e:
                    print(e)
                    pass
                except ValueError as e:
                    print(e)
                    pass
                else:
                    pass
                    print('[+]Video Download Is Complete!')


        #Make Image Directory And Download
        if len(final_urls) == 0:
            print('[-]There Is No Image In This Page')
        else:
            path = 'downloaded' + '/' + 'aliexpress' + '/' + str(productName) + '/' + 'img'
            if not os.path.exists(path):
                os.makedirs(path)

            number = 0
            for final_url in final_urls:
                number = number + 1
                try:
                    print(str(final_url))
                    if 'https://' not in final_url:
                        final_url = final_url.replace('//', 'https://')
                    urlretrieve(str(final_url), './downloaded/aliexpress/{}/img/{}.jpg'.format(productName,number))
                except HTTPError as e:
                    print(e)
                    pass
                except URLError as e:
                    print(e)
                    pass
                except ValueError as e:
                    print(e)
                    pass
                else:
                    pass
        print('[+]Turn End')
        driver.quit()
        
        

    else:
        #close Btn 이 있는 경우
        close_btn.click()
        driver.implicitly_wait(10)
        
        for i in range(1, 30):
            driver.execute_script("window.scrollTo(0, {})".format(1000*i))
            time.sleep(1)
        
        pageSource = driver.page_source
        bs = BeautifulSoup(pageSource, 'html.parser')
        
        image_tags = bs.findAll('img', {'src': True})

        #Extract the image_urls

        image_urls = []

        for image_tag in image_tags:
            image_urls.append(image_tag['src'])
            
        string1 = '480x480'
        string2 = '50x50'
        string3 = '120x120'
        string4 = '200x200'
        string5 = '220x220'

        edited_urls1 = []
        edited_urls2 = []
        edited_urls3 = []
        edited_urls4 = []


        final_urls = []

        try:

            for image_url in image_urls:
                if string1 not in image_url:
                    edited_urls1.append(image_url)
            
            del(image_urls)
            
            for edited_url1 in edited_urls1:
                if string2 not in edited_url1:
                    edited_urls2.append(edited_url1)

            del(edited_urls1)

            for edited_url2 in edited_urls2:
                if string3 not in edited_url2:
                    edited_urls3.append(edited_url2)

            del(edited_urls2)

            for edited_url3 in edited_urls3:
                if string4 not in edited_url3:
                    edited_urls4.append(edited_url3)

            del(edited_urls3)

            for edited_url4 in edited_urls4:
                if string5 not in edited_url4:
                    final_urls.append(edited_url4)
        
        except UnboundLocalError as e:
            print('[-]Something Went Wrong! : {}'.format(e))
            tkinter.messagebox.showerror('ERROR', 'mow...')
            driver.quit()

        #Extract The Title

        productName_not_split = bs.find('div', {'class': 'product-title'}).get_text()
        productName_list = productName_not_split.split()
        productName = str(productName_list[0]) + '+' + str(random.randint(0, 1000)) + '+' + str(productName_list[1])

        #Extract the video
        
        video_tags = bs.findAll('video', {'src': True})
        
        print(video_tags)
        
        video_urls = []

        for video_tag in video_tags:
            video_urls.append(video_tag['src'])

        #Download The Video
        if len(video_urls) == 0:
            print('[-]There Is No Video')
            pass
        else:
            #Make Video Directory And Download
            path = 'downloaded' + '/' + 'aliexpress' + '/' + str(productName) + '/' + 'video'
            if not os.path.exists(path):
                os.makedirs(path)

            video_number = 0
            for video_url in video_urls:
                video_number = video_number + 1
                try:
                    urlretrieve(str(video_url), './downloaded/aliexpress/{}/video/{}.mp4'.format(str(productName),video_number))
                except HTTPError as e:
                    print(e)
                    pass
                except URLError as e:
                    print(e)
                    pass
                except ValueError as e:
                    print(e)
                    pass
                else:
                    pass
                    print('[+]Video Download Is Complete!')


        #Make Image Directory And Download
        if len(final_urls) == 0:
            print('[-]There Is No Image In This Page')
        else:

            path = 'downloaded' + '/' + 'aliexpress' + '/' + str(productName) + '/' + 'img'
            if not os.path.exists(path):
                os.makedirs(path)

            number = 0
            for final_url in final_urls:
                number = number + 1
                try:
                    print(str(final_url))
                    if 'https://' not in final_url:
                        final_url = final_url.replace('//', 'https://')
                    urlretrieve(str(final_url), './downloaded/aliexpress/{}/img/{}.jpg'.format(str(productName),number))
                except HTTPError as e:
                    print(e)
                    pass
                except URLError as e:
                    print(e)
                    pass
                except ValueError as e:
                    print(e)
                    pass
                else:
                    pass
                    print('[+]Image Download Is Complete')
        print('[+]Turn End')
        driver.quit()

def AlibabaCorePart(baseUrl):
    downloadDirectory = 'downloaded'
    url = baseUrl
    options = webdriver.ChromeOptions()
    options.add_argument('headless')

    driver = webdriver.Chrome(executable_path='./chromedriver.exe',chrome_options=options)
    driver.get(url)
    time.sleep(5)

    pageSource = driver.page_source
    bs = BeautifulSoup(pageSource, 'html.parser')
    image_tags = bs.findAll('img', {'src': True})

    image_urls = []
    number = 0

    for image_tag in image_tags:
        image_urls.append(image_tag['src'])

    edited_urls1 = []
    edited_urls2 = []
    edited_urls3 = []
    edited_urls4 = []
    edited_urls5 = []
    edited_urls6 = []
    edited_urls7 = []
    edited_urls8 = []
    edited_urls9 = []
    final_urls = []

    string1 = '50x50'
    string2 = '100x100'
    string3 = 'placeholder'
    string4 = 'img.alicdn.com'
    string5 = '220x220'
    string6 = '120x120'
    string7 = 'webp=close'
    string8 = '350x350'
    string9 = 'atmgateway-client'
    string10 = 'upload/search/flags'

    try:
        for image_url in image_urls:
            #except string1
            if string1 not in image_url:
                edited_urls1.append(image_url)

        del(image_urls)

        for edited_url1 in edited_urls1:
            if string2 not in edited_url1:
                edited_urls2.append(edited_url1)

        del(edited_urls1)

        for edited_url2 in edited_urls2:
            if string3 not in edited_url2:
                edited_urls3.append(edited_url2)

        del(edited_urls2)

        for edited_url3 in edited_urls3:
            if string4 not in edited_url3:
                edited_urls4.append(edited_url3)

        del(edited_urls3)

        for edited_url4 in edited_urls4:
            if string5 not in edited_url4:
                edited_urls5.append(edited_url4)

        del(edited_urls4)

        for edited_url5 in edited_urls5:
            if string6 not in edited_url5:
                edited_urls6.append(edited_url5)

        del(edited_urls5)

        for edited_url6 in edited_urls6:
            if string7 not in edited_url6:
                edited_urls7.append(edited_url6)

        del(edited_url6)

        for edited_url7 in edited_urls7:
            if string8 not in edited_url7:
                edited_urls8.append(edited_url7)

        del(edited_url7)

        for edited_url8 in edited_urls8:
            if string9 not in edited_url8:
                edited_urls9.append(edited_url8)

        del(edited_url8)

        for edited_url9 in edited_urls9:
            if string10 not in edited_url9:
                final_urls.append(edited_url9)
    except UnboundLocalError as e:
        print('[-]Something Went Wrong! : {}'.format(e))
        tkinter.messagebox.showerror('ERROR', 'mow...')
        driver.quit()
    

    productName_not_split = bs.find('h1', {'class': 'ma-title'}).get_text()
    productName_list = productName_not_split.split()
    productName = str(productName_list[0]) + '+' + str(random.randint(0, 1000)) + '+' + str(productName_list[1])

    #Adding Video
    video_tags = bs.findAll('video', {'src': True})
    video_urls = []
    for video_tag in video_tags:
        video_urls.append(video_tag['src'])
    
    #Make Video Directory
    if len(video_tags) == 0:
        print('[-]There Is No Video In This Page...')
    else:
        print('[+]There is(are) Video(s) In The Page...!')
        path = downloadDirectory + '/' + 'alibaba'  +'/' + str(productName) + '/' + 'video'
        if not os.path.exists(path):
            os.makedirs(path)

        for video_url in video_urls:
            number = number + 1
            try:
                video_url = str(video_url).replace('//', 'https://')
                urlretrieve(video_url, './downloaded/alibaba/{}/video/{}.mp4'.format(productName, number))
            except HTTPError:
                print('[-]HTTP ERROR!')
                pass
            except URLError:
                print('[-]URL ERROR!')
                pass
            else:
                pass

    #Make Image Directory
    if len(final_urls) == 0:
        print('[-]There Is No Image In This Page...')
    else:
        path = downloadDirectory + '/'+ 'alibaba' + '/' + str(productName) + '/' + 'img'
        if not os.path.exists(path):
            os.makedirs(path)

        #change url to absolute Url
        for final_url in final_urls:
            number = number + 1
            try:
                final_image_url = str(final_url).replace('//', 'https://')
                urlretrieve(final_image_url, './downloaded/alibaba/{}/img/{}.jpg'.format(productName, number))
            except HTTPError:
                print('[-]HTTP ERROR!')
                pass
            except URLError:
                print('[-]URL ERROR!')
                pass
            else:
                pass
    print('[+]Alibaba Turn End!')

    driver.quit()


def corePart(event, AliexpressCorePart, AlibabaCorePart):
    baseUrls = str(url_entry.get())
    baseUrl_list = baseUrls.split('&&')
    for baseUrl in baseUrl_list:
        if 'alibaba.com/product-detail' in baseUrl:
            AlibabaCorePart(baseUrl)
        elif 'aliexpress.com/item' in baseUrl:
            AliexpressCorePart(baseUrl)
        else:
            tkinter.messagebox.showerror('ERROR', 'mow...')
    tkinter.messagebox.showinfo('Status', '!!!MOoooOW!!!')
    


# ===============Front End Part ====================


root = Tk()
root.title('Alistar Bot')
root.resizable(False, False)

main_image_path = './alistar-main-image.jpg'

#Image Setup
ImageFrame = Frame(root)
photo = ImageTk.PhotoImage(Image.open(main_image_path))
Label(ImageFrame, image=photo).grid(row=0, column=0, sticky=W)

ImageFrame.pack()

#URL Entry Setup
UrlFrame = Frame(root)
Label(UrlFrame, text="URL", font=('arial', 15, 'bold')).grid(row=0, column=0)
url_entry = Entry(UrlFrame, width=43)
url_entry.grid(row=1,column=0, padx=0, pady=(0,5))
UrlFrame.pack()

#Buttons Setup
ButtonFrame = Frame(root, relief=SUNKEN)

download_btn = Button(ButtonFrame,bg='red3', fg='white', text='!!!MOoooOW!!!', width=25, font=('arial', 15, 'bold'))
download_btn.bind('<Button-1>', lambda event: corePart(event, AliexpressCorePart, AlibabaCorePart))

download_btn.grid(row=0, column=0, pady=(0,2))

exit_btn = Button(ButtonFrame, bg='dim gray', fg='white', text='...MOoooOW...', width=25, font=('arial', 15, 'bold'), command=root.quit)
exit_btn.grid(row=1, column=0)

ButtonFrame.pack()

root.mainloop()
