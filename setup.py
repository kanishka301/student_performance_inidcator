from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)-> List[str]:
    """This function will return the list of requirements"""
    requiremts=[]
    with open(file_path) as file_obj:
        requiremts=file_obj.readlines()
        requiremts=[req.replace('\n','') for req in requiremts]
        # removing -e . from the list of requirements
        if HYPHEN_E_DOT in requiremts:
            requiremts.remove(HYPHEN_E_DOT)

    return requiremts

setup(
name='mlproject',
version='0.0.1',
author='Kanishka',
author_email='203.kanishka@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)