# -*- coding: utf-8 -*-
#
# File: CountryProgrammeEvaluationFolder.py
#
# Copyright (c) 2010 by unknown <unknown>
# Generator: ArchGenXML Version 2.5
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
import interfaces

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.ILOProjectEvaluation.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((


),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

CountryProgrammeEvaluationFolder_schema = BaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class CountryProgrammeEvaluationFolder(BaseFolder, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.ICountryProgrammeEvaluationFolder)

    meta_type = 'CountryProgrammeEvaluationFolder'
    _at_rename_after_creation = True

    schema = CountryProgrammeEvaluationFolder_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(CountryProgrammeEvaluationFolder, PROJECTNAME)
# end of class CountryProgrammeEvaluationFolder

##code-section module-footer #fill in your manual code here
##/code-section module-footer

