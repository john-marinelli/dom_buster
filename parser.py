import argparse

def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("--intext", action="store_false")
    parser.add_argument("--inattr", action="store_false")
    #TODO add help argument