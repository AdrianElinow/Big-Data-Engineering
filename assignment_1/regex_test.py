
import re

def breakdown( entry ):

    test = re.search(r'(?P<month>\w+) +(?P<day>\d+) (?P<time>\d+:\d+:\d+) [\D ]+\[(?P<proc>\d+)\]: (?P<msg>[\S ]*)', entry).groupdict()
    return test

def extract_msg_info( entry ):

    if entry['msg'].startswith('Failed'):
        return re.search(r'(?:for)?(?P<user>\w+|) from (?P<ip>\d+.\d+.\d+.\d+) port (?P<port>\d+)', entry['msg']).groupdict()
    elif entry['msg'].startswith('Invalid'):
        return re.search(r'(?P<user>\S+) from (?P<ip>\d+.\d+.\d+.\d+) (?:port )?(?P<port>\d+)?', entry['msg']).groupdict()
    
    return {}



def main():
    

    with open('auth_log/auth.log.2') as logfile:

        head = [ next(logfile) for _ in range(20) ]

        for line in head:
            elements = breakdown(line)
            #if elements:
            extracted = extract_msg_info(elements)

            print(elements['msg'])
            if extracted:
                #print(elements['msg'])
                print('\t',extract_msg_info(elements))
                #pass



        

if __name__ == '__main__':
    main()