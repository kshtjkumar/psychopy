# -*- coding: utf-8 -*-
# Part of the PsychoPy library
# Copyright (C) 2012-2020 iSolver Software Solutions (C) 2021 Open Science Tools Ltd.
# Distributed under the terms of the GNU General Public License (GPL).

import psychopy.logging as logging

try:
    from psychopy_eyetracker_pupil_labs.pupil_labs.pupil_core.data_parse import (
        eye_sample_from_gaze_3d, 
        eye_sample_from_pupil,
        _binocular_eye_sample_from_gaze_3d,
        _monocular_eye_sample_from_gaze_3d,
        _monocular_eye_sample_from_pupil)
except (ModuleNotFoundError, ImportError, NameError):
    logging.error(
        "Pupil Labs eyetracker support requires the package "
        "'psychopy-eyetracker-pupil-labs' to be installed. Please install this "
        "package and restart the session to enable support.")

if __name__ == "__main__":
    pass
