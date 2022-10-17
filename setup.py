from setuptools import setup

with open('README.md', 'r') as arq:
  readme = arq.read()

setup(name='pacote_preco',
    version='0.0.1',
    license='MIT License',
    author='Mirian Ajiki Molicawa',
    long_description=readme,
    long_description_content_type="text/markdown",
    url='https://github.com/ajikisan/pacote_preco',
    author_email='ajikisan@hotmail.com',
    keywords='valor preco',
    description=u'Calculo de valor de preco',
    packages=['valor_preco'],
    python_requires='>=3.8',)