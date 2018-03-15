# Buildver Resource

This concourse plugin allows builds to be triggered by a semver file.

Currently only S3 is supported

## Source Configuration
* `driver` : _Required_. The driver used to access the the file containing the version.
* `build_on` : _Optional_. _Default_ `all` When the build should be triggered. The following options are available.
    * `all` : _Default_. Build on all version changes.
    * `patch` : Build on patch or higher version changes.
    * `minor` : Build on minor or higher version changes.
    * `major` : Build on major version changes only.

### s3 Driver
* `bucket` : _Required_. The name of the bucket.
* `key` : _Required_. The key used to access the object.
* `access_key` : _Required_. The AWS Key used to access the bucket.
* `secret_access_key` : _Required_. The AWS access key used to access the bucket.

## Example

Configuration with a build on patch:
```
resource_types:
- name: buildver-resource
  type: docker-image
  source:
    repository: lukaszz/buildver-resource

resources:
- name: build-develop-version
  type: buildver-resource
  source:
    bucket: version.tracking
    access_key: ((s3-key-id))
    secret_access_key: ((s3-access-key))
    file: env/version/api.txt
    driver: s3
    build_on: patch
```

## Behavior

__`check` : Check for changes in the version number__

* Checks for new version numbers by reading the file. A new version will be reported if it is newer or older than the current versions. As long as the version constrains to the `build_on` flag.
* The various `build_on` flags decide when a build constrains to a correct version with some regexes, they are:
    * `all`: Checks only for a different version string
    * `patch` : `r"-.*"`, Checks for a pre release tag
    * `minor` : `r"\d\.\d\.0"` and `r"-.*"`, Checks that the last position has a 0 as well as checking for prerelease tags
    * `major` : `r"\d\.0\.0"` and `r"-.*"`, Checks that the 2 last positions has a 0 as well as checking for prerelease tags

__`in` : Provide the version file__

Provides the version file as `version.txt`

## Contributing

Please see Contrib.md