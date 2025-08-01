from setuptools import setup

package_name = 'twitchgo'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/resource', ['resource/traps.yaml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mikic202',
    maintainer_email='01168876@pw.edu.pl',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'main = twitchgo.main:main'
        ],
    },
)
