from setuptools import setup, find_packages

setup(
    name='gevent_viz',
    version='0.1.0',
    author='',
    author_email='',
    description='Visualize Greenlet execution.',
    packages=find_packages(),
    install_requires=['gevent'],
    data_files=[],
    entry_points={
        'console_scripts': [
            'gevent_viz = gevent_viz:profiler.main',
        ]
    },
)
