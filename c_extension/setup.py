from distutils.core import setup, Extension

MOD = "template"  # 模块名
setup(name=MOD, ext_modules=[Extension(MOD, sources=['template.c'])],
      description="My C Extension Module Template")
