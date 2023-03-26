from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
def main():
    options = Options()
    options.add_argument('headless')
    browser = webdriver.Chrome(options = options)
    #ブラウザを開く
    browser.get("https://login.microsoftonline.com/common/oauth2/authorize?response_mode=form_post&response_type=id_token+code&scope=openid&msafed=0&nonce=0e3256c4-2a24-4e44-b095-40cfe5ccbc82.637577201224842527&state=https%3A%2F%2Fforms.office.com%2FPages%2FResponsePage.aspx%3Fid%3DT6978HAr10eaAgh1yvlMhF__kSldrNpNvIWhwdsjjRJURUZEVjlIWjM1VjhXMlVaRVJaWVpEVjJZVCQlQCN0PWcu%26sid%3D024d4a30-9934-422e-a500-c9b15e8e3060&client_id=c9a559d2-7aab-4f13-a6ed-e7e9c52aec87&redirect_uri=https%3a%2f%2fforms.office.com%2fauth%2fsignin")
    #User ID Passwordを入力
    #右クリック→検証で対象のHTMLのコードができる。矢印のところをかざす。
    time.sleep(3)
    username_input = browser.find_element_by_id('i0116') 
    username_input.send_keys("")
    login_btn = browser.find_element_by_id("idSIButton9")
    login_btn.click()
    time.sleep(5)
    password_input = browser.find_element_by_id("passwordInput")
    password_input.send_keys("")
    sub_button = browser.find_element_by_id("submitButton")
    sub_button.click()
    time.sleep(3)
    yes_button = browser.find_element_by_id("idSIButton9")
    yes_button.click()
    time.sleep(3)

    vaccine_select = browser.find_element_by_name("rcf0d6c6b589745eea1be3c7cc10165c5")
    vaccine_select.click()
    time.sleep(3)
    button = browser.find_element_by_xpath("//button[@title='次へ']")
    button.click()
    time.sleep(2)
    email_select = browser.find_element_by_name("rc1e8d25040ac4f3d97e729dbef1505b8")
    email_select.click()
    campus_select = browser.find_element_by_name("r90d51a81a7334f2daef489720c271c85")
    campus_select.click()
    campus_submit = browser.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[3]/div[2]/div/div[3]/div/div[2]/div/div/input')
    campus_submit.send_keys("場所")
    temp_select = browser.find_element_by_name("r6bc496b7b0df41788aba61d57551f695")
    temp_select.click()
    time.sleep(3)
    symptom_select = browser.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[3]/div[2]/div/div[5]/div/div[2]/div/div[2]/div/label/input')
    symptom_select.click()
    final = browser.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[3]/div[3]/div[1]/button/div')
    final.click()
    time.sleep(5)
    browser.quit()
#ブラウザ
if __name__ == "__main__":
    main()