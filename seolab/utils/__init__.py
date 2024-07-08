import os


def update_environ_path(paths: list, append=True):
    """Update environment variable PATH"""

    _sep = os.path.pathsep
    existing_paths = os.environ["PATH"].split(_sep)

    if append:
        # Append paths to the end of the existing paths
        updated_paths = existing_paths + paths
    else:
        # Prepend paths to the beginning of the existing paths
        updated_paths = paths + existing_paths

    os.environ["PATH"] = _sep.join(updated_paths)
