# WordClock
First RPi Project. Doing a word clock

Trying my luck with the RPi and a Word clock. Saw it some days ago and I was fascinated. Decided to do one. 

At the beginning I did a research and lots of stuff were already done. Nevertheless, I will try to use some stuf, but do some stuff by my own. First thing i've used, was the generic algorithm of [dCandi](http://dcandi.com/post/genetic-algorithms-deap/). You can download it on his page or use my modified one. He found it in [Alessios](http://miniaturegiantspacehamster.blogspot.com/2011/03/building-word-clock-part-1-genetic.html) note but did a python version of it. I prefer everything over java :-). However, these 2 articles were the first i found and based my work on.

# GenericAlg
This algorithm is thoroughly explained by the other 2 guys. They got links and everything. I just took the file.
Put you language that you want in the "hours list". There you put the hours in. the restring = [] part is the time you want to display. So, if you wanna just display every 15min, you can put there for h in hours: restrings.append("QUARTER.+PAST.+"+h) according to the language you chose. The simply run the code and it will display you the character matrix in form of xxxxxxxxxx # xxxxxxxxxx # ... where # signals eol. For more details, please consult the pages of Alessio and dCandi.
