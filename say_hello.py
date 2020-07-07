import argparse

def say_hello(name):
    if name in ['arther','dingo']:
        print(f'you are the funnest {name}')
    elif name == 'dad' or name == 'levi':
        print(f'your not so fun {name}')
    
parser = argparse.ArgumentParser(description='Say hello to people')
parser.add_argument('name', help='The name of the person you want to say hello to')
args = parser.parse_args()
say_hello(args.name) 





































































