from setuptools import setup, find_packages

setup(
    name="qa-chatbot",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "farm-haystack==1.15.0",
        "transformers==4.28.1",
        "torch==1.13.1",
        "elasticsearch==7.17.9"
    ],
    entry_points={
        "console_scripts": [
            "run-chatbot=scripts.run_chatbot:main",
        ],
    },
    author="Sujit Shelar",
    author_email="shelarsujit44@gmail.com",
    description="A Q&A chatbot with an external knowledge base",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/shelarsujit/qa_chatbot",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)