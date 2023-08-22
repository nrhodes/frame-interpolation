from setuptools import find_packages
from setuptools import setup

setup(
    name="film",
    version="0.0.4",
    description="Film interpolation",
    author="Google",
    author_email="neil@descript.com",
    url="https://github.com/bolasim/frame-interpolator",
    packages=["film"],
    install_requires=[
        "tensorflow==2.10.0", # The latest should include tensorflow-gpu
        "tensorflow-datasets==4.9.2",
        "tensorflow-addons==0.21.0",
        "absl-py==1.4.0",
        "gin-config==0.5.0",
        "parameterized==0.9.0",
        "mediapy==1.1.9",
        "scikit-image==0.21.0",
        "apache-beam==2.49.0",
        "google-cloud-bigquery-storage==2.22.0",
        "natsort==8.4.0",
        "gdown==4.7.1",
        "tqdm==4.66.1",
    ],
)
