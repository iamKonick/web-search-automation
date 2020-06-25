from selenium import webdriver

# location of the downloaded chromedriver as Path

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)
# opening the website
driver.get('https://konick.life')

# clicking the post continue reading button
reading = driver.find_element_by_xpath('//*[@id="post-216"]/div/div[2]/div/a')
reading.click()

# writing the comment in the form
writingComment = driver.find_element_by_xpath('//*[@id="comment"]')
writingComment.send_keys('Thank you for the javascript code')

# writing the name in the form
writingName = driver.find_element_by_xpath('//*[@id="author"]')
writingName.send_keys('Jack')

# writing the email in the form
writingEmail = driver.find_element_by_xpath('//*[@id="email"]')
writingEmail.send_keys('jack@whattodo.com')

# writing the website in the form
writingWebsite = driver.find_element_by_xpath('//*[@id="url"]')
writingWebsite.send_keys('http://whattodo.com')

# writing the comment in the form
postComment = driver.find_element_by_xpath('//*[@id="submit"]')
postComment.click()
