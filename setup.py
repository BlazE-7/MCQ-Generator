from setup import find_packges, setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='smit prajapati',
    author_email='smitprajapati094@gmail.com',
    install_requires=["langchain", "streamlit", "huggingface_hub", "transformers", "dotenv", "PyPDF2"],
    packages=find_packges()
)