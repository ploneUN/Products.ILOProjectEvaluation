# -*- coding: utf-8 -*-
#
# File: setuphandlers.py
#
# Copyright (c) 2010 by unknown <unknown>
# Generator: ArchGenXML Version 2.5
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'


import logging
logger = logging.getLogger('ILOProjectEvaluation: setuphandlers')
from Products.ILOProjectEvaluation.config import PROJECTNAME
from Products.ILOProjectEvaluation.config import DEPENDENCIES
import os
from Products.CMFCore.utils import getToolByName
import transaction
##code-section HEAD
##/code-section HEAD

def isNotILOProjectEvaluationProfile(context):
    return context.readDataFile("ILOProjectEvaluation_marker.txt") is None



def updateRoleMappings(context):
    """after workflow changed update the roles mapping. this is like pressing
    the button 'Update Security Setting' and portal_workflow"""
    if isNotILOProjectEvaluationProfile(context): return 
    wft = getToolByName(context.getSite(), 'portal_workflow')
    wft.updateRoleMappings()

def postInstall(context):
    """Called as at the end of the setup process. """
    # the right place for your custom code
    if isNotILOProjectEvaluationProfile(context): return
    site = context.getSite()



##code-section FOOT
##/code-section FOOT
