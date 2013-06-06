from distutils.core import setup


setup(name='whirlwind-tornado',
      version='0.1',
      author='Mathieu Lecarme',
      author_email='mlecarme@bearstech.com',
      license='BSD',
      package_dir = {'': 'src'},
      packages= ['whirlwind',
                 'whirlwind.tornado',
                 'whirlwind.tornado.carbon',
                 'whirlwind.tornado.whisper'],
      scripts=['scripts/whirlwind'],
      requires=[
          'whirlwind'
          'whisper',
          'tornado(>=3.0)',
          'tornadoredis',
          'redis',
          'lust'
          ]
      )
