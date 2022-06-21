


import glob
from pathlib import Path
from Ankit.utils import load_plugins
import logging
from Ankit import Ankit

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

path = "Ankit/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))
    
print("Successfully Started Bot!")
print("Made With 💞 By ©ANKIT™")

if __name__ == "__main__":
    Ankit.run_until_disconnected()
