from setuptools import find_packages, setup

requirements = [
    'requests<3.0,>=2.25.1',
]

setup(
    name='lamadava',
    version='1.0.0',
    author='Lamadava',
    author_email='support@lamadava.com',
    license='MIT',
    url='https://lamadava.com',
    install_requires=requirements,
    keywords=[
        'instagram private api', 'instagram-private-api', 'instagram api', 'instagram-api', 'instagram',
        'instagram-scraper', 'instagram-client', 'instagram-stories', 'instagram-feed', 'instagram-reels', 'instagram-insights',
        'downloader', 'uploader', 'videos', 'photos', 'albums', 'igtv', 'reels', 'stories', 'pictures',
        'instagram-user-photos', 'instagram-photos', 'instagram-metadata', 'instagram-downloader', 'instagram-uploader'
    ],
    description='Instagram Private API SaaS client',
    packages=find_packages(),
    python_requires=">=3.6",
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]
)
