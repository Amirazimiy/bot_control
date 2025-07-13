import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from time import sleep
from pyperclip import copy
import requests
import os



# تابع شروع از UI
def start_bot():

    if not is_bot_enabled():
        messagebox.showwarning("غیرفعال", "ربات توسط مدیر غیرفعال شده است.")
        return
    driver = webdriver.Firefox(service=Service("geckodriver.exe"))
    username = entry_username.get()
    password = entry_password.get()
    date_from = entry_date_from.get()
    date_to = entry_date_to.get()
    

    if not username or not password or not date_from or not date_to:
        messagebox.showwarning("خطا", "لطفاً همه فیلدها را پر کنید.")
        return

    try:
        seleniumStarted(driver,username, password, date_from, date_to)
    except Exception as e:
        messagebox.showerror("خطا", f"اجرای ربات با خطا مواجه شد:\n\n{str(e)}")

    root.quit()
    os._exit(0)


def is_bot_enabled() -> bool:

    try:
        resp = requests.get("https://raw.githubusercontent.com/Amirazimiy/bot_control/main/status.txt")
        status = resp.text.strip().lower()
        return status == "on"
    except requests.RequestException:
        # خطای شبکه را هم به منزلهٔ غیرفعال بودن در نظر می‌گیریم
        return False


# تابع اصلی سلنیوم
def seleniumStarted(driver ,username, password, date_from, date_to):
    driver.get("https://s5.symfa.ir/")
    sleep(10)
    loginusername = driver.find_element_by_xpath('//*[@id="txt-username"]')

    loginusername.send_keys(username)

    sleep(2)

    loginpassword = driver.find_element_by_xpath('//*[@id="txt-password"]')

    loginpassword.send_keys(password)

    sleep(5)

    loginbtn = driver.find_element_by_xpath('//*[@id="btn-login"]').click()
    sleep(2)
    driver.find_element_by_xpath('/html/body/div/div/div[3]/div/div/div/div/div/div[2]/div/a[2]/div/div/div[2]')
    sleep(2)
    driver.get('https://s5.symfa.ir/Dashboard/TestCenterList')
    sleep(2)
    driver.find_element_by_xpath('/html/body/div/div/div[3]/div/div/div/div/div/div[2]/div/table/tbody/tr/td[13]/form/input[3]').click()
    sleep(5)
    driver.find_element_by_xpath('/html/body/div/div/div[3]/div/div/div/div/div/div[2]/div/div[1]/ul/li[5]/a').click()
    sleep(2)

    driver.find_element_by_xpath('//*[@id="dropdownMenuButton"]').click()

    sleep(2)

    driver.find_element_by_xpath('/html/body/div/div/div[3]/div/div/div/div/div/div[2]/div/div[6]/div/div[1]/div[2]/div/form/input[3]').click()
    sleep(2)

    firstdate = date_from


    firstdateinput = driver.find_element_by_xpath('//*[@id="datepicker-fromdate"]')

    firstdateinput.send_keys(firstdate)

    sleep(2)
    enddate = date_to

    enddateinput = driver.find_element_by_xpath('//*[@id="datepicker-todate"]')

    enddateinput.send_keys(enddate)
    sleep(2)
    driver.find_element_by_xpath('//*[@id="search-button"]').click()
    list1 = []
    for i in range(1,100000):
        try:
            element = driver.find_element_by_xpath(f'/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div[2]/div/table/tbody/tr[{i}]/td[2]')
            list1.append(element.text)
        except:
            pass

    new_list = []


    if list1:
        new_list.append(list1[-1])
    
    messagebox.showinfo("موفق", "ربات شما با موفقیت تمام کد های پذیرش را کپی کرد")


    sleep(2)
    driver.get("https://petrol.symfa.ir")
    sleep(5)
    usernameL = driver.find_element_by_xpath('//*[@id="UserName"]')
    usernameL.send_keys(username)
    sleep(1)

    passwordL = driver.find_element_by_xpath('//*[@id="Password"]')
    passwordL.send_keys(username)
    sleep(1)

    driver.find_element_by_xpath('/html/body/div[2]/div/div/section/form/div[3]/button').click()
    sleep(1)
    driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div[4]/div/ul/li[2]/a').click()
    sleep(1)
    driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div[4]/div/ul/li[2]/ul/li[1]/a').click()

    sleep(5)

    phon_number_list = []
    for i in list1:
        driver.get(f'https://petrol.symfa.ir/TestCenters/Receptions/Details?ReceptionId={i}')
        phone = driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/div/div[1]/div[2]/div[1]/div[2]/div/div[8]/div[2]')
        number_phone = phone.text
        phon_number_list.append(number_phone)
        sleep(1)        



        if i == new_list[0]:
            break

    copy(phon_number_list)



    



# UI
root = tk.Tk()
root.title("فرم ورود")

tk.Label(root, text="یوزرنیم:").grid(row=0, column=0, sticky="e", pady=5, padx=5)
entry_username = tk.Entry(root, width=30)
entry_username.grid(row=0, column=1)
entry_username.insert(0, "Mz23739255")



tk.Label(root, text="پسورد:").grid(row=1, column=0, sticky="e", pady=5, padx=5)
entry_password = tk.Entry(root, show="*", width=30)
entry_password.grid(row=1, column=1)
entry_password.insert(0, "13781378f")


tk.Label(root, text="از تاریخ:").grid(row=2, column=0, sticky="e", pady=5, padx=5)
entry_date_from = tk.Entry(root, width=30)
entry_date_from.grid(row=2, column=1)
entry_date_from.insert(0, "1403/01/01")


tk.Label(root, text="تا تاریخ:").grid(row=3, column=0, sticky="e", pady=5, padx=5)
entry_date_to = tk.Entry(root, width=30)
entry_date_to.grid(row=3, column=1)
entry_date_to.insert(0, "1403/01/01")


start_button = tk.Button(root, text="شروع", command=start_bot)
start_button.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
