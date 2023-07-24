# Import the Secret Manager client library.
from google.cloud import secretmanager

# GCP project in which to store secrets in Secret Manager.
project_id = "ultranslator"

# ID of the secret to create.
secret_id = "ultranslator_speech_to_text"

# Create the Secret Manager client.
client = secretmanager.SecretManagerServiceClient()

# Build the parent name from the project.
parent = f"projects/{project_id}"

# Create the parent secret.
secret = client.create_secret(
    request={
        "parent": parent,
        "secret_id": secret_id,
        "secret": {"replication": {"automatic": {}}},
    }
)

# Add the secret version.
version = client.add_secret_version(
    request={"parent": secret.name, "payload": {"data": b"hello world!"}}
)

# Access the secret version.
response = client.access_secret_version(request={"name": version.name})

# Print the secret payload.
#
# WARNING: Do not print the secret in a production environment - this
# snippet is showing how to access the secret material.
payload = response.payload.data.decode("UTF-8")
print(f"Plaintext: {payload}")


# projects/724367844932/secrets/ultranslator_speech_to_text/versions/1



# {
#   "type": "service_account",
#   "project_id": "ultranslator",
#   "private_key_id": "312fe495121750b7f65f8ef605474a0540bbf342",
#   "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCSdcRjMw4hKCFb\nirG0eP4IiGwO8Xbdjp/WdXz7oQaPI+y3Y0a1PtyEcJ9CgcevVM/thq2OuxmqxwVW\nhjb9Z+aK1p6UIxawIT87Nm4RNfUfJkpmGB2UwKVELRiE2lTSgc4D+oOm3pCCpMn8\n5TiTbIV9exP3fdZQ1VYOgnRCG//TEBPKMvqXtxVNydlzGscJWh1prA8o0P0k+OZX\nUNS5KaMUYw/JwO+83WW4wGrHlVZtXQDavs3lbX1o9YWeGVTB1h7lxMfsHK9obW4Y\n7Zbgphy6jxaQe0Sk+3lM2tCnZ3wfa+9fxb+3z7RcvdA7/txy3Hw2RHVBJmNGT+73\nD4QMYDTHAgMBAAECggEAEYyEOuapMME1jgRxBTuMz3TujbPSbFBknTZ4AqaUD0lc\nrx9Oykon826TMU2KTFs7NtjGVFiIMMr8EWwE4W7g/uMhyS+TI7ONd14u6L0Ftp/I\nllxutEjeWexACIXTWA3Zo5G8KJ3Obvj+guDsWy3LqPIQaGfu6sHv4nkwePi7OeIq\n0fatf71CbyjHPYW1B9n/bpXiBTispWSHPqhj1X4xg+16+Fd5jmEHfrkRHBfINM6T\n7QNIHqosYRKaQt0soPF9qH7ujaTpnXJgG9bjww0d+xj9WmR/LC6Z4crS6XPBAg8+\ndlB5u9IJRGJTaowAtYOhRoFK14fyiMFSqVHkoOLWUQKBgQDLZuJbBqe+AyuBWTQO\nKLk9D8yzJ7q38dV5bZs9v5aS+FvHvD1VU2yeb9eIlYrmgLfgRAB6mh1G+myZo1v8\n0Ph0uTBfqmuHGUC3n1O2pjW09+dJuXp4H8fX3uF8LA/wNZNUD0q+yFPlgfL8naDk\nX7hFr0DIzN5SkpsljxqiiOBwewKBgQC4VVtKUFskYLQsYpdKIy/GwGmFloxJvWml\ny2cjHe8SYzeLUvXLeCgmHdZOiwhRvSzO1yTqGvfgAAfu0nxVSRmx7vesgMfDR6In\nZVAU5AT22Owoywhl6maScTuSoYGWBpHYype74NIp4gr4DyPP/fY+EIapXOn0505w\nxvrAK7DpJQKBgQC5gaTx9djosEVuW+fg/f0rloxP3O0rNFFIxNEv+NsgQYibWq/p\ncQOAYGqHdDPRVBXfYMW7C3GmOWDwoo+TvRbMhdV7epdFCKAAmDwmOeKDoRD9KT9r\n7Tg7RlgKArmqj4JFyQiXhWcWy3TMNgr2HeKXE2YXfNlLH9CF6cUV9ZYUnwKBgQCh\nqRo6/mYwbS8WjhCo0FsiL7Vbl0DJmviAkvaM8b+tnJ4l7kfqfiKX6yr8DyropMQb\nUsvpFGW3ac+LP8YS9d03E6DbBMYtGTG44z1sVN2Vr4DN9eITn5L9c5kPa90+OdzH\nCEYyW2V1neyIyJ5b1xqSK+QtvHLiecltVtSqnKa2kQKBgHEjgsG0CZgpBjKZj96G\nb0MEMKaZ0uFN5Qxx6nhAbo/BZkoSHDoA7LWjk72zPnV4FrwFbla+Lu3w8dYMR4zJ\n6WQzrybyD9nA79EQtpywgDyo6t3fqyat/j/YOBNGtAXsZ1gfEYRXGyNn3TfYs1X1\n+KJAx4+SCvD1zR8BoY5Aggrk\n-----END PRIVATE KEY-----\n",
#   "client_email": "augurybot@ultranslator.iam.gserviceaccount.com",
#   "client_id": "107393471182122002657",
#   "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#   "token_uri": "https://oauth2.googleapis.com/token",
#   "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#   "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/augurybot%40ultranslator.iam.gserviceaccount.com",
#   "universe_domain": "googleapis.com"
# }
