import os

import build
import setuptools

build.main()

long_description = '''
The PyQt5 wheels do not provide tools such as Qt Designer that
were included in the old binary installers.  This package aims
to provide those in a separate package which is useful for
developers while the official PyQt5 wheels stay focused on
fulfulling the dependencies of PyQt5 applications.
'''

setuptools.setup(
    name="pyqt5-tools",
    description="Tools to supplement the official PyQt5 wheels",
    long_description=long_description,
    url='https://github.com/altendky/pyqt5-tools',
    author="Kyle Altendorf",
    author_email='sda@fstab.net',
    license='GPLv3',
    classifiers=[
#        '{development_status}',
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Win32 (MS Windows)',
        'Intended Audience :: Developers',
        ("License :: OSI Approved :: "
         "GNU General Public License v3 (GPLv3)"),
        'Natural Language :: English',
        'Operating System :: Microsoft :: Windows',
        'Topic :: Software Development',
        'Topic :: Utilities'
    ],
    keywords='pyqt5 qt designer',
    packages=['pyqt5-tools'],
    set_requires=[
        'vcversioner==2.16.0.0',
        'requests==2.13.0',
        'pyqtdeploy==1.3.2',
    ],
    vcversioner={
        'version_module_paths': ['epyq/_version.py'],
        'vcs_args': ['git', '--git-dir', '%(root)s/.git', 'describe',
                     '--tags', '--long', '--abbrev=999']
    },
    include_package_data=True,
#    data_files=buildinfo.data_files()
#    scripts=[
#        {scripts}
#        'pyqt5-tools/designer.exe'
#    ]
)
