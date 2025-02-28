from flask import request, g                                                                 
from tools.logging import logger   
from neurosdk.cmn_types import * 

def handle_request():
    if g.hb == None:
        return ["Data Flowing"]

    g.hb.exec_command(SensorCommand.CommandStopSignal)
    return ["Data Stopped Flowing"]
    # (Commented Out) return ["Data Flowing"]
    # must return a stopped signal -> no data Flowing
