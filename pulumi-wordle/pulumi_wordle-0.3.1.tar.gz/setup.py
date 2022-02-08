# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import errno
from setuptools import setup, find_packages
from setuptools.command.install import install
from subprocess import check_call


VERSION = "0.3.1"
PLUGIN_VERSION = "0.3.1"

class InstallPluginCommand(install):
    def run(self):
        install.run(self)
        try:
            check_call(['pulumi', 'plugin', 'install', 'resource', 'wordle', PLUGIN_VERSION, '--server', 'https://github.com/aaronfriel/pulumi-wordle/releases/download/v${VERSION}'])
        except OSError as error:
            if error.errno == errno.ENOENT:
                print(f"""
                There was an error installing the wordle resource provider plugin.
                It looks like `pulumi` is not installed on your system.
                Please visit https://pulumi.com/ to install the Pulumi CLI.
                You may try manually installing the plugin by running
                `pulumi plugin install resource wordle {PLUGIN_VERSION}`
                """)
            else:
                raise


def readme():
    try:
        with open('README.md', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "wordle Pulumi Package - Development Version"


setup(name='pulumi_wordle',
      version=VERSION,
      description="Stand up Wordle while you stand up infrastructure",
      long_description=readme(),
      long_description_content_type='text/markdown',
      cmdclass={
          'install': InstallPluginCommand,
      },
      keywords='pulumi wordle category/Fun category/Utility',
      url='https://github.com/aaronfriel/pulumi-wordle',
      project_urls={
          'Repository': 'https://github.com/aaronfriel/pulumi-wordle'
      },
      license='Apache-2.0',
      packages=find_packages(),
      package_data={
          'pulumi_wordle': [
              'py.typed',
              'pulumi-plugin.json',
          ]
      },
      install_requires=[
          'parver>=0.2.1',
          'pulumi>=3.0.0,<4.0.0',
          'semver>=2.8.1'
      ],
      zip_safe=False)
