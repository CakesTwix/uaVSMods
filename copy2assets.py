import os
import shutil

directory = 'vs'


for filename in os.listdir(directory):
    if filename.endswith(".json"):
        with open(os.path.join(directory, filename), 'r') as file:
            if file.read() == "{}":
                print(f"Skipping file {filename}")
                continue

        modname = filename.split("-")[0]
        # assets/modname/lang/uk.json
        new_path = os.path.join('assets', modname, 'lang', 'uk.json')

        os.makedirs(f"assets/{modname}/lang", exist_ok=True)
        shutil.move(os.path.join(directory, filename), new_path)

        print(f"File {filename} to {new_path}")
