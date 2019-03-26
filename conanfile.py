#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, AutoToolsBuildEnvironment, tools
from conans.errors import ConanInvalidConfiguration
import os


class XCBProtoConan(ConanFile):
    name = "xcb-proto"
    version = "1.13"
    description = "xcb-proto provides the XML-XCB protocol descriptions that libxcb uses to" \
                   "generate the majority of its code and API"
    topics = ("conan", "xcb-proto", "xcb", "x11")
    url = "https://github.com/bincrafters/conan-xcb-proto"
    homepage = "https://gitlab.freedesktop.org/xorg/proto/xcbproto"
    author = "Bincrafters <bincrafters@gmail.com>"
    license = "X11"
    exports = ["LICENSE.md"]
    settings = "os", "arch", "compiler", "build_type"
    _source_subfolder = "source_subfolder"
    _build_subfolder = "build_subfolder"

    def configure(self):
        del self.settings.compiler.libcxx
        if self.settings.os != "Linux":
            raise ConanInvalidConfiguration("only Linux is supported")

    def source(self):
        source_url = "https://www.x.org/archive//individual/xcb/%s-%s.tar.bz2" % (self.name, self.version)
        tools.get(source_url, sha256="7b98721e669be80284e9bbfeab02d2d0d54cd11172b72271e47a2fe875e2bde1")
        os.rename(self.name + "-" + self.version, self._source_subfolder)

    def build(self):
        with tools.chdir(self._source_subfolder):
            env_build = AutoToolsBuildEnvironment(self)
            env_build.configure()
            env_build.make()
            env_build.install()

    def package(self):
        self.copy(pattern="COPYING*", dst="licenses", src=self._source_subfolder)

    def package_id(self):
        self.info.header_only()
