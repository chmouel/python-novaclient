def authenticate(cls, auth_url):
    """Authenticate against the Rackspace auth service."""
    body = {"auth": {
        "RAX-KSKEY:apiKeyCredentials": {
            "username": cls.user,
            "apiKey": cls.password,
            "tenantName": cls.projectid}}}
    return cls._authenticate(auth_url, body)
