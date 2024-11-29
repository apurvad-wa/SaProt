from setuptools import setup, find_packages
import os

def include_all_files(directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_list.append(os.path.relpath(os.path.join(root, file), directory))
    return file_list

setup(
    name="SaProt",
    version="0.0.1",
    license='MIT',
    url='https://github.com/apurvad-wa/SaProt',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "SaProt": include_all_files("."), 
    }
)
