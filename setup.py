from cx_Freeze import setup, Executable
 
buildOptions = dict(packages=[], excludes = [])
 
exe = [Executable('C:\\logy\\Mediapipe-VR-Fullbody-Tracking\\bin\\mediapipepose.py')]
 
setup(
    name='vrlogy',
    version='0.0.1',
    author='kook',
    description = 'description',
    options = dict(build_exe = buildOptions),
    executables = exe
)