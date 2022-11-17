# -*- coding: utf-8 -*-
#
# MIT Kerberos documentation build configuration file, created by
# sphinx-quickstart on Wed Oct 13 09:14:03 2010.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
#extensions = ['sphinx.ext.autodoc', 'sphinxcontrib.doxylink']
extensions = ['sphinx.ext.autodoc']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
if 'notice' in tags:
    master_doc = 'notice'
else:
    master_doc = 'index'

# General information about the project.
project = u'MIT Kerberos'
copyright = u'1985-2020, MIT'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
exec(open("version.py").read())
# The short X.Y version.
r_list = [r_major, r_minor]
if r_patch:
    r_list += [r_patch]
version = '.'.join(map(str, r_list))
# The full version, including alpha/beta/rc tags.
release = version
if r_tail:
    release += '-' + r_tail

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
today = ' '
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# html_theme = 'default'
html_theme = 'agogo'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = { "linkcolor": "#881f0d", "footerbg":  "#5d1509",
                       "bgcolor": "#5d1509", "documentwidth": "80%",
                       "pagewidth": "auto", "sidebarwidth": "20%" }

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "MIT Kerberos Documentation"

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
if os.environ.get('HTML_LOGO'):
    html_logo = os.environ['HTML_LOGO']

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
html_split_index = True

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g., ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'MIT Kerberos'

pointsize = '10pt'

# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
#latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('admin/index', 'admin.tex', u"Kerberos Administration Guide", u'MIT',
   'manual'),
  ('appdev/index', 'appdev.tex', u"Kerberos Application Developer Guide",
   u'MIT', 'manual'),
  ('basic/index', 'basic.tex', u"Kerberos Concepts", u'MIT', 'manual'),
  ('build/index', 'build.tex', u"Building MIT Kerberos", u'MIT', 'manual'),
  ('plugindev/index', 'plugindev.tex', u"Kerberos Plugin Module Developer Guide",
   u'MIT', 'manual'),
  ('user/index', 'user.tex', u"Kerberos User Guide", u'MIT', 'manual')
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Additional stuff for the LaTeX preamble.
#latex_preamble = ''

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True

if 'mansubs' in tags:
    bindir = '``@BINDIR@``'
    sbindir = '``@SBINDIR@``'
    libdir = '``@LIBDIR@``'
    localstatedir = '``@LOCALSTATEDIR@``'
    runstatedir = '``@RUNSTATEDIR@``'
    sysconfdir = '``@SYSCONFDIR@``'
    ccache = '``@CCNAME@``'
    keytab = '``@KTNAME@``'
    ckeytab = '``@CKTNAME@``'
elif 'pathsubs' in tags:
    # Read configured paths from a file produced by the build system.
    exec(open("paths.py").read())
else:
    bindir = ':ref:`BINDIR <paths>`'
    sbindir = ':ref:`SBINDIR <paths>`'
    libdir = ':ref:`LIBDIR <paths>`'
    localstatedir = ':ref:`LOCALSTATEDIR <paths>`'
    runstatedir = ':ref:`RUNSTATEDIR <paths>`'
    sysconfdir = ':ref:`SYSCONFDIR <paths>`'
    ccache = ':ref:`DEFCCNAME <paths>`'
    keytab = ':ref:`DEFKTNAME <paths>`'
    ckeytab = ':ref:`DEFCKTNAME <paths>`'

rst_epilog = '\n'

if 'notice' in tags:
    exclude_patterns = [ 'admin', 'appdev', 'basic', 'build',
                         'plugindev', 'user' ]
    exclude_patterns += [ 'about.rst', 'build_this.rst', 'copyright.rst',
                          'index.rst', 'mitK5*.rst', 'resources.rst' ]
    rst_epilog += '.. |copy| replace:: \(C\)'
else:
    exclude_patterns += [ 'notice.rst' ]
    rst_epilog += '.. |bindir| replace:: %s\n' % bindir
    rst_epilog += '.. |sbindir| replace:: %s\n' % sbindir
    rst_epilog += '.. |libdir| replace:: %s\n' % libdir
    rst_epilog += '.. |kdcdir| replace:: %s\\ ``/krb5kdc``\n' % localstatedir
    rst_epilog += '.. |kdcrundir| replace:: %s\\ ``/krb5kdc``\n' % runstatedir
    rst_epilog += '.. |sysconfdir| replace:: %s\n' % sysconfdir
    rst_epilog += '.. |ccache| replace:: %s\n' % ccache
    rst_epilog += '.. |keytab| replace:: %s\n' % keytab
    rst_epilog += '.. |ckeytab| replace:: %s\n' % ckeytab
    rst_epilog += '''
.. |krb5conf| replace:: ``/etc/krb5.conf``
.. |defkeysalts| replace:: ``aes256-cts-hmac-sha1-96:normal aes128-cts-hmac-sha1-96:normal``
.. |defetypes| replace:: ``aes256-cts-hmac-sha1-96 aes128-cts-hmac-sha1-96 aes256-cts-hmac-sha384-192 aes128-cts-hmac-sha256-128 des3-cbc-sha1 arcfour-hmac-md5 camellia256-cts-cmac camellia128-cts-cmac``
.. |defmkey| replace:: ``aes256-cts-hmac-sha1-96``
.. |copy| unicode:: U+000A9
'''

# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('user/user_commands/kinit', 'kinit', u'obtain and cache Kerberos ticket-granting ticket', [u'MIT'], 1),
    ('user/user_commands/klist', 'klist', u'list cached Kerberos tickets', [u'MIT'], 1),
    ('user/user_commands/kdestroy', 'kdestroy', u'destroy Kerberos tickets', [u'MIT'], 1),
    ('user/user_commands/kswitch', 'kswitch', u'switch primary ticket cache', [u'MIT'], 1),
    ('user/user_commands/kpasswd', 'kpasswd', u'change a user\'s Kerberos password', [u'MIT'], 1),
    ('user/user_commands/kvno', 'kvno', u'print key version numbers of Kerberos principals', [u'MIT'], 1),
    ('user/user_commands/ksu', 'ksu', u'Kerberized super-user', [u'MIT'], 1),
    ('user/user_commands/krb5-config', 'krb5-config', u'tool for linking against MIT Kerberos libraries', [u'MIT'], 1),
    ('user/user_config/k5login', 'k5login', u'Kerberos V5 acl file for host access', [u'MIT'], 5),
    ('user/user_config/k5identity', 'k5identity', u'Kerberos V5 client principal selection rules', [u'MIT'], 5),
    ('user/user_config/kerberos', 'kerberos', u'Overview of using Kerberos', [u'MIT'], 7),
    ('admin/admin_commands/krb5kdc', 'krb5kdc', u'Kerberos V5 KDC', [u'MIT'], 8),
    ('admin/admin_commands/kadmin_local', 'kadmin', u'Kerberos V5 database administration program', [u'MIT'], 1),
    ('admin/admin_commands/kprop', 'kprop', u'propagate a Kerberos V5 principal database to a replica server', [u'MIT'], 8),
    ('admin/admin_commands/kproplog', 'kproplog', u'display the contents of the Kerberos principal update log', [u'MIT'], 8),
    ('admin/admin_commands/kpropd', 'kpropd', u'Kerberos V5 replica KDC update server', [u'MIT'], 8),
    ('admin/admin_commands/kdb5_util', 'kdb5_util', u'Kerberos database maintenance utility', [u'MIT'], 8),
    ('admin/admin_commands/ktutil', 'ktutil', u'Kerberos keytab file maintenance utility', [u'MIT'], 1),
    ('admin/admin_commands/k5srvutil', 'k5srvutil', u'host key table (keytab) manipulation utility', [u'MIT'], 1),
    ('admin/admin_commands/kadmind', 'kadmind', u'KADM5 administration server', [u'MIT'], 8),
    ('admin/admin_commands/kdb5_ldap_util', 'kdb5_ldap_util', u'Kerberos configuration utility', [u'MIT'], 8),
    ('admin/conf_files/krb5_conf', 'krb5.conf', u'Kerberos configuration file', [u'MIT'], 5),
    ('admin/conf_files/kdc_conf', 'kdc.conf', u'Kerberos V5 KDC configuration file', [u'MIT'], 5),
    ('admin/conf_files/kadm5_acl', 'kadm5.acl', u'Kerberos ACL file', [u'MIT'], 5),
    ('user/user_commands/sclient', 'sclient', u'sample Kerberos version 5 client', [u'MIT'], 1),
    ('admin/admin_commands/sserver', 'sserver', u'sample Kerberos version 5 server', [u'MIT'], 8),
]
