import os
import seed_tree
from anytree.exporter import DotExporter

os.makedirs('cache', exist_ok=True)
os.makedirs('cache/keywords', exist_ok=True)
os.makedirs('cache/papers', exist_ok=True)

DotExporter(seed_tree.tech_root).to_picture("crittech.png")