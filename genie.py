import os
import requests
import discord
from bs4 import BeautifulSoup
from keep_alive import keep_alive

client = discord.Client()


def python(message):
  #code for python, C, C++, C#, Java & Swift
  
  m1 = message
  message = str(m1[4:]).replace(" ", "+")
  url = 'https://google.com/search?q=programiz+' + message
  request = requests.get(url).text
  soup = BeautifulSoup(request, 'html.parser')
  for a in soup.find_all('a', href=True):
      if 'https://www.programiz.com/' in a['href']:
          page=a['href'].strip('/url?q=').split('&')
          page=page[0]
          break;
      

  #programiz
  request = requests.get(page)
  soup = BeautifulSoup(request.text , 'html.parser')

  cont = str(soup.find('div',class_= 'content').text)
  cont = cont[1:500] + "...\nVisit page:" + page
  return(cont)


def web(message):
  #Code for JS, HTML, CSS, SQL & PHP

  message = message[4:].replace(" ", "+")
  url = 'https://google.com/search?q=w3+' + message
  request = requests.get(url).text
  soup = BeautifulSoup(request, 'html.parser')
  for a in soup.find_all('a', href=True):
      if 'https://www.w3schools.com/' in a['href']:
          page=a['href'].strip('/url?q=').split('&')
          page=page[0]
          break;
      

  #w3
  request = requests.get(page).text
  soup = BeautifulSoup(request, 'html.parser')
  heading=soup.find('h1').text
  material=(str(soup.find('div', id = 'main').text))[1:500] + "...\nVisit page:" + page
  return(material)


def issue(message):
  
  message = (message[6:]).replace(" ","+")
  msg = message.find("+")
  response = requests.get("https://github.com/search?l={}&q={}&type=Issues".format(message[:msg], message[msg+1:]))

  soup = BeautifulSoup(response.text , 'html.parser')

  best_result = str(soup.find('a', class_ = 'Link--muted color-text-tertiary'))

  start = best_result.find('href="')
  end = best_result.find('">#')
  num_end = best_result.find("</a")
  link_str = best_result[start+6:end]
  link_num = best_result[end+3:num_end]

  response1 = requests.get("https://github.com" + link_str + "/" + link_num)
  #print(response1.text)
  soup1 = BeautifulSoup(response1.text, 'html.parser')
  #print(soup1)
  question = soup1.find('td', class_ = "d-block comment-body markdown-body js-comment-body")
  cont = (question.text)[1:500] + "\nBest result: https://github.com" + link_str + "/" + link_num + "\nMore results: https://github.com/search?l={}&q={}&type=Issues".format(message[:msg], message[msg+1:])
  return(cont)


def help():
  cont = 'Hi! I am Genie. I give solutions to all your coding problems. Here is how you can give commands to me:\ndoc_<programming_language> <your_doubt>  -for documentation\nEg: To get the documentation of for loop in java, the command should be "doc`_java for loop" \n' + 'issue`_<programming_language> <your_issue>  -for getting solutions to your errors/questions\nEg: To get suggestions to solve syntax error in python, command should be "issue_python syntax error"\nFor help, give "help".\nIf there is no response from me, give me a proper command.\nHappy coding! :)'
  return(cont)




@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('doc_python') or message.content.startswith('doc_c') or message.content.startswith('doc_cpp') or message.content.startswith('doc_csharp') or message.content.startswith('doc_java') or message.content.startswith('doc_swift'):
    await message.channel.send('>>> ' + python(message.content)) 

  if message.content.startswith('doc_js') or message.content.startswith('doc_html') or message.content.startswith('doc_css') or message.content.startswith('doc_sql') or message.content.startswith('doc_php'):
    await message.channel.send('>>> ' + web(message.content))

  if message.content.startswith('issue_'):
    await message.channel.send('>>> ' + issue(message.content)) 
  
  if message.content == 'help':
    await message.channel.send('>>> ' + help())
  
keep_alive()
my_secret = os.environ['TOKEN']
client.run(my_secret)
