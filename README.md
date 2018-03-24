# Motivations
With the advent of artificial intelligence, I became more and more interested in this field.
I started doing some research. So to go faster in my research, I put forward my knowledge in <b><i>python</i></b>.
That is to say I did some data crawl in Internet with the <b>Scrapy framework</b>.

This first approach allowed me to retrieve many articles link on the site https://arxiv.org/list/cs.AI/recent
and save them to an .txt file for timely viewing.
I realized very quickly that it was much more convenient to download them on my computer. 
Downloading 167 articles is a boring thing, and as a lazy person, I couldn't afford it.
And then again, as if by magic, python will save my life. 
I decide to automate the download of all articles with IDM (Internet Download Manager). 
Here I simply put into practice some python modules that I have experienced with reading such as pyautogui, subprocess...

# Project architecture
  <h3>AI_research</h3>
This file contains, the work done with Scrapy to crawl links on the Internet.
<br/>
  <h3>Automate-boring-stuff</h3>
Here you have a urls.txt file that contains the link to all articles recover on https://arxiv.org/list/cs.AI/recent.
The main.py contains the source code to automate the download.
