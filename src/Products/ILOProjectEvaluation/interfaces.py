# -*- coding: utf-8 -*-

from zope.interface import Interface

##code-section HEAD
##/code-section HEAD

class IProject(Interface):
    """Marker interface for .Project.Project
    """

class IProjectEvaluationFolder(Interface):
    """Marker interface for .ProjectEvaluationFolder.ProjectEvaluationFolder
    """

class ICountryProgrammeEvaluationFolder(Interface):
    """Marker interface for .CountryProgrammeEvaluationFolder.CountryProgrammeEvaluationFolder
    """

class ICountryProgrammeEvaluation(Interface):
    """Marker interface for .CountryProgrammeEvaluation.CountryProgrammeEvaluation
    """

##code-section FOOT
##/code-section FOOT