# -*- coding: utf-8 -*-
#
# File: Project.py
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
from Products.ILOIntranetTypes.ILOIntranetBase import ILOIntranetBase
from Products.ATContentTypes.content.event import ATEvent

##code-section module-header #fill in your manual code here
##/code-section module-header

copied_fields = {}
copied_fields['title'] = ATFileSchema['title'].copy()
copied_fields['title'].widget.description = "Project title. eg. Corporate social responsibility in the Chinese textile industry"
copied_fields['description'] = ATFileSchema['description'].copy()
copied_fields['description'].schemata = "default"
copied_fields['country'] = ILOIntranetBase.schema['country'].copy()
copied_fields['administrative_unit'] = ILOIntranetBase.schema['administrative_unit'].copy()
copied_fields['technical_unit'] = ILOIntranetBase.schema['technical_unit'].copy()
copied_fields['file'] = ATFileSchema['file'].copy()
copied_fields['file'].widget.description = "Upload the updated project Evaluation follow up Plan"
schema = Schema((

    IntegerField(
        name='eval_no',
        widget=IntegerWidget(
            label="Evaluation No.",
            label_msgid='ILOProjectEvaluation_label_eval_no',
            i18n_domain='ILOProjectEvaluation',
        ),
    ),
    copied_fields['title'],

    copied_fields['description'],

    copied_fields['country'],

    LinesField(
        name='project_code',
        widget=LinesField._properties['widget'](
            label="Project Code",
            description="eg. PAK/06/51/NET. One project code per line",
            label_msgid='ILOProjectEvaluation_label_project_code',
            description_msgid='ILOProjectEvaluation_help_project_code',
            i18n_domain='ILOProjectEvaluation',
        ),
        searchable=1,
    ),
    IntegerField(
        name='evaluation_year',
        widget=SelectionWidget(
            label="Evaluation Year",
            description="Year project evaluation was conducted",
            label_msgid='ILOProjectEvaluation_label_evaluation_year',
            description_msgid='ILOProjectEvaluation_help_evaluation_year',
            i18n_domain='ILOProjectEvaluation',
        ),
        searchable=True,
        vocabulary=[2008,2009,2010,2011,2012,2013,2014,2015],
    ),
    IntegerField(
        name='aer',
        widget=SelectionWidget(
            label="AER",
            description="Please select the ending Annual Evaluation Report (AER) Year",
            label_msgid='ILOProjectEvaluation_label_aer',
            description_msgid='ILOProjectEvaluation_help_aer',
            i18n_domain='ILOProjectEvaluation',
        ),
        vocabulary=[2008,2009,2010,2011,2012,2013,2014,2015],
        searchable=1,
    ),
    LinesField(
        name='donor',
        widget=MultiSelectionWidget(
            label="Donor",
            description="Select donors for this project. Hold down CTRL to select multiple entries.",
            label_msgid='ILOProjectEvaluation_label_donor',
            description_msgid='ILOProjectEvaluation_help_donor',
            i18n_domain='ILOProjectEvaluation',
        ),
        multiValued=1,
        searchable=1,
        vocabulary=['Australia', 'Banks', 'Belgium', 'Brazil', 'Canada', 'Denmark', 'Direct Trust Funds', 'European Commission', 'Finland', 'Flanders', 'France', 'Germany', 'International Organisation for Migration', 'Ireland', 'Italy', 'Japan', 'Luxembourg', 'Multi Donors', 'Netherlands', 'New Zealand', 'Non-State Actors', 'Norway', 'Republic of Korea', 'Secretariat of the Pacific Community', 'Spain', 'Sweden', 'Switzerland', 'UNDP', 'Other UN', 'United Kingdom', 'United States'],
    ),
    IntegerField(
        name='no_recommendations',
        default=0,
        widget=IntegerWidget(
            label="No. of Recommendations",
            label_msgid='ILOProjectEvaluation_label_no_recommendations',
            i18n_domain='ILOProjectEvaluation',
        ),
    ),
    copied_fields['administrative_unit'],

    copied_fields['technical_unit'],

    StringField(
        name='followup_status',
        widget=SelectionWidget(
            label="Followup Status",
            description="Follow up status on recommendations. Completed (100%), Partially Completed (75%), Outstanding (>50%), No Action Planned",
            label_msgid='ILOProjectEvaluation_label_followup_status',
            description_msgid='ILOProjectEvaluation_help_followup_status',
            i18n_domain='ILOProjectEvaluation',
        ),
        vocabulary=['Completed','Partially Completed','Outstanding','No Action Planned'],
        searchable=1,
    ),
    TextField(
        name='proj_eval_notes',
        widget=TextAreaWidget(
            label="Notes",
            label_msgid='ILOProjectEvaluation_label_proj_eval_notes',
            i18n_domain='ILOProjectEvaluation',
        ),
        searchable=1,
    ),
    copied_fields['file'],


),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Project_schema = ATFileSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Project(ATFile):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IProject)

    meta_type = 'Project'
    _at_rename_after_creation = True

    schema = Project_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(Project, PROJECTNAME)
# end of class Project

##code-section module-footer #fill in your manual code here
##/code-section module-footer

