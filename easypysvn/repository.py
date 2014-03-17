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

from pysvn import Client
from workingcopy import WorkingCopy
import handler

class Repository(object):
    def __init__(self,repo_url,**kwargs):
        self.repo_url = repo_url
        self.kwargs = kwargs
        self.svn_client = Client()

    def is_auth_needed(self):
        pass

    def set_get_login_callback(self):
        handler.username = self.kwargs.get('svn_username')
        handler.password = self.kwargs.get('svn_password')
        self.svn_client.callback_get_login = handler.get_login()

    def checkout(self):
        wc_path = self.kwargs.get('working_copy_path')
        return WorkingCopy(wc_path)

    def export(self):
        pass

    def delete(self):
        pass

    def get_commit_log(self):
        pass


__author__ = 'yelkalay'
