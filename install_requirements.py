import subprocess
import sys
import pkg_resources


def check_requirements(requirements_file='requirements.txt'):
    with open(requirements_file, 'r', encoding='utf-8') as file:
        requirements = [line.strip() for line in file.readlines()]

    installed_packages = {pkg.key: pkg.version for pkg in pkg_resources.working_set}

    for requirement in requirements:
        req = pkg_resources.Requirement.parse(requirement)
        if req.key not in installed_packages:
            install_package(requirement)


def install_package(requirement):
    subprocess.check_call([sys.executable, "-m", "pip", "install", requirement])
    print(f"The requirement '{requirement}' has been installed.")


check_requirements()
