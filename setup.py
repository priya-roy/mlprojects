from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirement(file_path:str)->List[str] :
    '''
    This function will return all requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
                    requirements.remove(HYPEN_E_DOT)
            
    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Priya Roy',
    author_email='priyaroycowdhury11@gmail.com',
    packages=find_packages(),
    install_requires= get_requirement('requirements.txt')

)