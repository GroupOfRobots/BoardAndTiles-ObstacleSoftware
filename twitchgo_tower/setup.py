from setuptools import setup

package_name = 'twitchgo_tower'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='nowickid',
    maintainer_email='01149375@pw.edu.pl',
    description='TwitchGo - controlling a tower',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'main = tower.main:main'
        ],
    },
)
