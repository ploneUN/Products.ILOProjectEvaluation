# -*- coding: utf-8 -*-
#
# File: CountryProgrammeEvaluation.py
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

from Products.ATContentTypes.content.file import ATFile
from Products.ATContentTypes.content.file import ATFileSchema
from Products.ILOProjectEvaluation.config import *

# additional imports from tagged value 'import'
from Products.ATContentTypes.content.event import ATEvent
from Products.ATContentTypes.content.event import ATEventSchema
from Products.ILOIntranetTypes.ILOIntranetBase import ILOIntranetBase
from Products.ILOProjectEvaluation import Project

##code-section module-header #fill in your manual code here
##/code-section module-header

copied_fields = {}
copied_fields['country'] = ILOIntranetBase.schema['country'].copy()
copied_fields['administrative_unit'] = ILOIntranetBase.schema['administrative_unit'].copy()
copied_fields['no_recommendations'] = Project.schema['no_recommendations'].copy()
schema = Schema((

    copied_fields['country'],

    IntegerField(
        name='dwcp_evaluation_year',
        widget=SelectionWidget(
            label="DWCP Evaluation Year",
            label_msgid='ILOProjectEvaluation_label_dwcp_evaluation_year',
            i18n_domain='ILOProjectEvaluation',
        ),
        vocabulary=[2008,2009,2010,2011,2012,2013,2014,2015],
        searchable=True,
    ),
    copied_fields['administrative_unit'],

    copied_fields['no_recommendations'],

    StringField(
        name='implementation_status',
        widget=SelectionWidget(
            label="Implementation Status",
            label_msgid='ILOProjectEvaluation_label_implementation_status',
            i18n_domain='ILOProjectEvaluation',
        ),
        vocabulary=['Completed','Partially Completed','Outstanding','No Action Planned'],
        searchable=1,
    ),
    TextField(
        name='cp_evaluation_notes',
        widget=TextAreaWidget(
            label="Notes",
            label_msgid='ILOProjectEvaluation_label_cp_evaluation_notes',
            i18n_domain='ILOProjectEvaluation',
        ),
        searchable=1,
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

CountryProgrammeEvaluation_schema = ATFileSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class CountryProgrammeEvaluation(ATFile):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.ICountryProgrammeEvaluation)

    meta_type = 'CountryProgrammeEvaluation'
    _at_rename_after_creation = True

    schema = CountryProgrammeEvaluation_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(CountryProgrammeEvaluation, PROJECTNAME)
# end of class CountryProgrammeEvaluation

##code-section module-footer #fill in your manual code here
##/code-section module-footer

