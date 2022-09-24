from setuptools import setup

setup(
    name='Meoli',
    version='0.0.1',    
    description='Getting the value of K in a KNN model',
    url='https://github.com/shadmeoli/finding_k.git',
    author='intech',
    author_email='shadcodes@gmail.com',
    license='MIT',
    packages=['Meoli']
    install_requires=['mpi4py>=2.0',
                      'rich'                    
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10'
    ],
)