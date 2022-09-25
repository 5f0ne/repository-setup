import argparse

from src.Controller import Controller

parser = argparse.ArgumentParser()
parser.add_argument("--path", "-p", type=str, required=True, help="Example path")
args = parser.parse_args()

c = Controller()