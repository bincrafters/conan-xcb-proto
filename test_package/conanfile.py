#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

from conans import ConanFile
import os


class TestPackageConan(ConanFile):
    def test(self):
        assert os.path.isfile(os.path.join(self.deps_cpp_info["xcb-proto"].rootpath, "share", "xcb", "xproto.xml"))
