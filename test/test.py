'''
Created on Nov 22, 2014

@author: arusekar
'''
import pyrax
import pyrax.identity
import ConfigParser

import ConfigParser

config =  ConfigParser.ConfigParser()
print r"C:\rackspace\config.cfg"
config.read(r"C:\rackspace\config.cfg")
pyrax.set_setting("identity_type", config.get('detail','identity_type'))
pyrax.set_setting("tenant_id", config.get('detail','tenant_id'))
pyrax.set_setting("auth_endpoint", config.get('detail','auth_endpoint'))
pyrax.set_setting("region", config.get('detail','region'))
pyrax.set_credential_file(r"C:\rackspace\password.txt")

cf= pyrax.cloudservers

print cf.list_flavors()
print cf.list_base_images()
print cf.list_images()

print "completed"