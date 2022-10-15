from cx_Freeze import setup, Executable

buildOptions = dict(packages = ['os', 'pytube','sys'], 
                    excludes = ["tkinter", "numpy"])

exe = [Executable('download.py')] 
setup(
    name='YoutubeDown',
    version='0.0.1',
    description='YoutubeDown',
    options=dict(build_exe=buildOptions),
    executables=exe
)
