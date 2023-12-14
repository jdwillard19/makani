from setuptools import setup, find_packages

setup(
    name="makani",
    version="0.1.0",
    description="A machine learning framework for climate modeling",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'cmake',
        'mpi4py',
        'h5py',  # Note: Might need custom installation due to specific flags
        'zarr',
        'netCDF4',
        'xarray',
        'pandas',
        'moviepy',
        'imageio',
        'wandb',
        'ruamel.yaml',
        'tqdm',
        'jsbeautifier',
        'numba',
        'xskillscore',
        'properscoring',
        # Dependencies from GitHub might need to be handled separately
        # 'git+https://github.com/romerojosh/benchy.git',
        # 'git+https://github.com/NVIDIA/mlperf-common.git',
        # 'git+https://github.com/tensorly/tensorly',
        # 'git+https://github.com/tensorly/torch',
        # 'git+https://github.com/NVIDIA/torch-harmonics.git'
    ],
    entry_points={
        'console_scripts': [
            'makani-inference=makani.inference:main',
            'makani-train=makani.train:main',
        ],
    },
    # include any additional non-code files
    package_data={
        'makani': ['config/*.conf', 'README.md'],
    },
)
