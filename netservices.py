#
# RTEMS Project (https://www.rtems.org/)
#
# Copyright (c) 2021 Regents of University of Colorado
# Written by Vijay Kumar Banerjee <vijay@rtems.org>.
# All rights reserved.
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions
#  are met:
#  1. Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
#  2. Redistributions in binary form must reproduce the above copyright
#     notice, this list of conditions and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
#  A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
#  OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#  SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
#  LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
#  DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
#  THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#  OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from rtems_waf import rtems
import bsp_drivers
import os

source_files = []
include_files = {}

def find_node(bld, *paths):
    path = os.path.join(*paths)
    return os.path.relpath(str(bld.path.find_node(path)))

def install_file_list(*paths):
    path = os.path.join(*paths)
    file_list = [os.path.join(path, f) for f in os.listdir(path)]
    return file_list

def build(bld):
	include_path = []

	for root, dirs, files in os.walk("."):
	    dirs.append(os.path.join('telnetd'))
	    include_files[root[2:]] = []
	    for name in files:
	        ext = os.path.splitext(name)[1]
	        if ext == '.c':
	            source_files.append(os.path.join(root, name))
	        if ext == '.h':
	            include_files[root[2:]].append(os.path.join(root, name))