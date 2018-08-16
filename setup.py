from skbuild import setup

setup(
    name="prox_tv",
    version="3.2.1",
    description="Toolbox for fast Total Variation proximity operators",
    long_description="proxTV is a toolbox implementing blazing fast implementations of Total Variation proximity operators. While the core algorithms are implemented in C to achieve high efficiency, Matlab and Python interfaces are provided for ease of use. The library provides efficient solvers for a variety of Total Variation proximity problems, with address input signals of any dimensionality (1d, images, video, ...) and different norms to apply in the Total Variation term.",
    packages=['prox_tv'],
    install_requires=[
        'numpy>=1.6.2',
        'cffi>=1.0.0',
    ],
    setup_requires=[],
    package_data={
        'prox_tv': ['demos/*']
    },
    author="Alvaro Barbero, Suvrit Sra, Josip Djolonga (python bindings)",
    author_email="alvaro.barbero@uam.es",
    url='https://github.com/albarji/proxTV',
    license='BSD',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'Operating System :: POSIX :: Linux',
        'Topic :: Scientific/Engineering :: Mathematics',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    keywords='total variation image processing machine learning',
    test_suite="nose.collector",
    cmake_args=[
        '-DproxTV_INSTALL_DEVELOPMENT:BOOL=0',
        '-DBUILD_SHARED_LIBS:BOOL=1',
        '-DproxTV_INSTALL_BIN_DIR:STRING=prox_tv',
        '-DproxTV_INSTALL_LIB_DIR:STRING=prox_tv'
    ]
)
