## Copyright 2014 Youssuf ElKalay
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  	http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


"""
A pysvn callback handler module. This module is designed to implement all callback methods used in pysvn.
It's developed as a procedural Python module versus a class because of pysvn's requirement of having callback methods with specific parameters.
"""

cancel_command = False
rc = True
log_message = None
realm = None
username = None
password = None
'By default we do not want to save SVN credentials'
may_save = False
retcode = False
certfile = None
accepted_failures = 0


def cancel():
    return cancel_command

def get_log_message():
    return rc,log_message

def get_login(realm,username,may_save):
    if(username is not None and password is not None):
        retcode = True
    return retcode,username,password,may_save

def notify(event_dict):
    return

def ssl_client_cert_password_prompt(realm,may_save):
    return retcode,password,may_save

def ssl_client_cert_prompt(realm, may_save ):
    if (certfile is not None):
        retcode = True
    return retcode, certfile, may_save

def ssl_server_trust_prompt(trust_dict):
        if(username is not None and password is not None):
            retcode = True
        return retcode, accepted_failures, may_save


__author__ = 'yelkalay'
