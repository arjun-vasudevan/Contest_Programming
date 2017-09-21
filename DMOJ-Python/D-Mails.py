import re

for _ in range(input()):
    orig = raw_input()
    senders = []
    
    if re.search('.*'.join('elpsycongroo'), orig) is not None:
        senders.append('Okabe')
    if re.search('.*'.join('tuturu'), orig) is not None:
        senders.append('Mayuri')
    if re.search('.*'.join('superhacker'), orig) is not None:
        senders.append('Daru')
    if re.search('.*'.join('myfork'), orig) is not None:
        senders.append('Kurisu')

    if len(senders) == 0:
        print 'SERN spy!'
    else:
        print ' or '.join(senders)
