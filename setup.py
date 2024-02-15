from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Writing programs with ease in python'
LONG_DESCRIPTION = 'This library is in development and not in released state. If you counter any bugs please report it to the owner!'

# Setting up
setup(
    name="PyKeasy",
    version=VERSION,
    author="Soumeswar Bhuty",
    author_email="<soumeswarbhuty@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['pyscreenshot', 'pywhatkit', 'pillow', 'pytube', 'qrcode', 'openai'],
    keywords=['python', 'video', 'stream', 'video stream', 'camera stream', 'sockets'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)