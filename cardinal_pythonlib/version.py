#!/usr/bin/env python
# cardinal_pythonlib/version.py
# Copyright (c) Rudolf Cardinal (rudolf@pobox.com).
# See LICENSE for details.


VERSION = '0.2.12'
# Use semantic versioning: http://semver.org/

RECENT_VERSION_HISTORY = """

- 0.2.7, 2017-04-28
  Fixed bug in rnc_extract_text that was using get_file_contents() as a
  converter when it wasn't accepting generic **kwargs; now it is.
  
- 0.2.8, 2017-04-28
  Fixed DOCX table processing bug, in docx_process_table().
  
- 0.2.10, 2017-04-29
  Text fetch (for converters) was returning bytes, not str; fixed.

- 0.2.11, 2017-04-29
  Encoding auto-detection for text extraction from files.

- 0.2.12, 2017-05-02
  More file types support for simple text extraction.

"""
