from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'vision_bot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name,'meshes'),glob('meshes/*')),
       (os.path.join('share', package_name,'urdf'),glob('urdf/*')) ,
    (os.path.join('share', package_name,'launch'),glob('launch/*'))
     ,
    (os.path.join('share', package_name,'world'),glob('world/*'))]
  ,
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='abdullah',
    maintainer_email='asoyero@student.h.lautech.edu.ng',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            
                'publisher_node = vision_bot.publisher:main',
                'subscriber_node = vision_bot.subscriber:main',
        ],
},
)
