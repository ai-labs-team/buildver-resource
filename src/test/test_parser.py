from ..buildver.parser import CheckVersion


payload_build_on_all = {
    'source': {
        'build_on': 'all'
    },
}


payload_build_on_patch = {
    'source': {
        'build_on': 'patch'
    },
}


payload_build_on_minor = {
    'source': {
        'build_on': 'minor'
    },
}


payload_build_on_major = {
    'source': {
        'build_on': 'major'
    },
}


# test cases for build_on all
def test_build_on_all_version_has_changed():
    assert CheckVersion(payload_build_on_all).check_for_new_version('1.0.0','1.0.1-pre.1') == '1.0.1-pre.1'


def test_build_on_all_version_has_not_changed():
    assert CheckVersion(payload_build_on_all).check_for_new_version('1.0.0','1.0.0') == ''


# test cases for build_on patch
def test_build_on_patch_version_has_prerelease_tag():
    assert CheckVersion(payload_build_on_patch).check_for_new_version('1.0.0','1.0.0-pre.1') == ''


def test_build_on_patch_version_has_not_changed():
    assert CheckVersion(payload_build_on_patch).check_for_new_version('1.0.0','1.0.0') == ''


def test_build_on_patch_version_has_changed():
    assert CheckVersion(payload_build_on_patch).check_for_new_version('1.0.0','1.0.1') == '1.0.1'


# test cases for build_on minor
def test_build_on_minor_version_has_prerelease_tag():
    assert CheckVersion(payload_build_on_minor).check_for_new_version('1.0.0','1.0.0-pre.1') == ''


def test_build_on_minor_version_has_not_changed():
    assert CheckVersion(payload_build_on_minor).check_for_new_version('1.1.0','1.1.0') == ''


def test_build_on_minor_version_has_patch_change():
    assert CheckVersion(payload_build_on_minor).check_for_new_version('1.0.0','1.0.1') == ''


def test_build_on_minor_version_has_minor_change():
    assert CheckVersion(payload_build_on_minor).check_for_new_version('1.0.0','1.1.0') == '1.1.0'


# test cases for build_on patch
def test_build_on_major_version_has_prerelease_tag():
    assert CheckVersion(payload_build_on_major).check_for_new_version('1.0.0','1.0.0-pre.1') == ''


def test_build_on_major_version_has_not_changed():
    assert CheckVersion(payload_build_on_major).check_for_new_version('1.1.0','1.1.0') == ''


def test_build_on_major_version_has_patch_change():
    assert CheckVersion(payload_build_on_major).check_for_new_version('1.0.0','1.0.1') == ''


def test_build_on_major_version_has_minor_change():
    assert CheckVersion(payload_build_on_major).check_for_new_version('1.0.0','1.1.0') == ''


def test_build_on_major_version_has_major_change():
    assert CheckVersion(payload_build_on_major).check_for_new_version('1.0.0','2.0.0') == '2.0.0'
