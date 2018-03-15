import re


debug = False
def printc(string):
    if debug:
        print(string)

class CheckVersion():

    config = {}

    def __init__(self, stream):
        """
            Initialize the version parser and set defaults

            Keyword arguments:
            stream -- the stdin from concourse
        """
        self.config = stream['source']

        if self.config['build_on'] is None:
            self.config['build_on'] = 'all'

    def check_for_new_version(self, old_ver, new_ver):
        """
            Perform a series of checks to see if a new build should be triggered
        """

        # Check if the version is different
        if (old_ver == new_ver):
            return ""

        printc('Current Build Target: ' + self.config["build_on"])

        if self.config["build_on"] == "all" or \
            self.check_if_patch_applied(old_ver, new_ver) or \
            self.check_if_minor_applied(old_ver, new_ver) or \
            self.check_if_major_applied(old_ver, new_ver):
            return new_ver
        
        return ""

    def check_if_patch_applied(self, old_ver, new_ver):
        if self.config["build_on"] != "patch":
            return False

        if not self.check_for_optional_prerelease(new_ver):
            return True

        return False

    def check_if_minor_applied(self, old_ver, new_ver):
        if self.config["build_on"] != "minor":
            return False

        if not self.check_for_optional_prerelease(new_ver) and \
            self.check_for_minor_release(new_ver):
            return True

        return False

    def check_if_major_applied(self, old_ver, new_ver):
        if self.config["build_on"] != "major":
            return False

        if not self.check_for_optional_prerelease(new_ver) and \
            self.check_for_major_release(new_ver):
            return True

        return False

    def check_for_optional_prerelease(self, version):
        check_pre = re.search(r"-.*", version)
        return False if check_pre is None else True

    def check_for_minor_release(self, version):
        check_minor = re.search(r"\d\.\d\.0", version)
        return False if check_minor is None else True

    def check_for_major_release(self, version):
        check_major = re.search(r"\d\.0\.0", version)
        return False if check_major is None else True
