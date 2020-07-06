import argparse

def say_hello(name):
    if name in ['jaxon', 'levi', 'jax', 'levi james']:
        print(f'you are the coolest kid {name}')
    elif name == 'mom' or name == 'dad':
        print(f'you are not even kids')
    else:
        print(f'i don\'t even know you {name}')

parser = argparse.ArgumentParser(description='Say hello to people')
parser.add_argument('name', help='The name of the person you want to say hello to')
args = parser.parse_args()
say_hello(args.name)