# -*-coding: utf-8 -*-
"""
    @Author : panjq
    @E-mail : pan_jinquan@163.com
    @Date   : 2019-06-12 20:13:04
"""
import os
import basetrainer
import pypandoc
from setuptools import setup, find_packages

root = os.path.dirname(__file__)
long_description = pypandoc.convert('README.md', 'rst')
setup(name='basetrainer',
      version=basetrainer.__version__,
      description='basetrainer',
      long_description=long_description,
      url='https://github.com/PanJinquan/Pytorch-Base-Trainer',
      author='PanJinquan',
      author_email='pan_jinquan@163.com',
      license='MIT',
      packages=find_packages(where=".",
                             exclude=["build", "configs", "data", "dist", "basetrainer.egg-info", "test",
                                      '.idea', ".gitignore",
                                      ]),  # 为空为全部
      package_data={
          # 如果包中含有.txt文件，则包含它
          'pjq': ['*.jpg'],
          # 包含demo包data文件夹中的 *.dat文件
          'demo': ['data/*.dat']
      },
      install_requires=[
          # 'pandas>=0.20.0',  # 所需要包的版本号
          # 'numpy>=1.14.0'  # 所需要包的版本号
      ],
      zip_safe=False)
