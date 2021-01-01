from setuptools import setup, find_packages

with open("README.md", mode="r", encoding="utf-8") as readme_file:
    readme = readme_file.read()



setup(
      name="AutoClassify",
      version="0.0.1",
      author="A. Ali Heydari",
      author_email="aliheydari@ucdavis.edu",
      description="Automatic Classification of Single Cell Data",
      long_description=readme,
      long_description_content_type="text/markdown",
      license="MIT",
      url="https://github.com/SindiLab/Auto-Cell-Classification",
      download_url="https://github.com/SindiLab/Auto-Cell-Classification",
      packages=find_packages(),
      install_requires=[
                        'tqdm==4.47.0',
                        'numpy==1.18.5',
                        'torch==1.5.1',
                        'scanpy==1.6.0',
                        'tensorboardX==2.1',
                        ],
      classifiers=[
                   "Development Status :: 1 - Beta",
                   "Intended Audience :: Science/Research",
                   "License :: OSI Approved :: MIT Software License",
                   "Programming Language :: Python :: 3.6",
                   "Topic :: Scientific/Engineering :: Artificial Intelligence :: Bioinformatics :: Deep Learning"
                   ],
      keywords="Single Cell RNA-seq, Automatic Classification, Neural Networks, Transfer Learning"
      )
