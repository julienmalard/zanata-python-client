# vim:set et sts=4 sw=4:
#
# Zanata Python Client
#
# Copyright (c) 2011 Jian Ni <jni@redhat.com>
# Copyright (c) 2011 Red Hat, Inc.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the
# Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA  02110-1301, USA.


from builtins import object
__all__ = (
    "ZanataResource",
)

from .docservice import DocumentService
from .glossaryservice import GlossaryService
from .projectservice import ProjectService
from .statservice import StatService
from .versionservice import VersionService


class ZanataResource(object):
    def __init__(self, base_url, http_headers):
        self.base_url = base_url
        self.projects = ProjectService(base_url, http_headers)
        self.documents = DocumentService(self.projects, base_url, http_headers)
        self.version = VersionService(base_url, http_headers)
        self.glossary = GlossaryService(base_url, http_headers)
        self.stats = StatService(base_url, http_headers)

    def disable_ssl_cert_validation(self):
        self.projects.disable_ssl_cert_validation()
        self.version.disable_ssl_cert_validation()
