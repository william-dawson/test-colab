from os import system
_base = "https://github.com/william-dawson/test-colab/raw/main/packages/"
_pkg = "bigdft-suite-1.9.3_rc.2-mpi_openmpi_py37h008c211_0.tar.bz2"

def download():
    system("wget " + _base + _pkg)

def install_colab():
    system("pip install -q condacolab")

def setup_colab():
    import condacolab
    condacolab.install()

def install_bigdft():
   system("conda install " + _pkg + " ; conda update --all")

def fix_environment():
    from os import environ
    environ["BIGDFT_ROOT"] = "/usr/local/bin"

