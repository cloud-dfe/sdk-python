from setuptools import setup, find_packages

setup(
    name="sdk-cloud-dfe",
    version="1.0.0",
    author="Integra Notas",
    author_email="comercial@cloud-dfe.com.br",
    description="SDK para comunicar com API Integra Notas.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="",
    packages=find_packages(),
    install_requires=[
        # Adicione aqui as dependências do seu SDK, se houver
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires=">=3.6",
)
