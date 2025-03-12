from setuptools import setup, find_packages

setup(
    name="task_tracker_cli",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "task-tracker=task_tracker_cli:main",
        ],
    },
    author="Shreya Dhume",
    author_email="shreyadhume2310@gmail.com",
    description="A simple CLI task tracker",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/shdh23/task_tracker_cli",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
