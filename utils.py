import os
import numpy as np
from datetime import date
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.ndimage import gaussian_filter1d

import seaborn as sns

from astropy.table import Table
import pyvo as vo

# Set plotting style:
sns.set_style('ticks')

def get_data(input_filename = None):
    """
    This function gets data from all transiting exoplanets from the NASA exoplanet arvhive
    """

    if input_filename is None:
        # Define filename to which we'll save the NASA Exoplanet Archive data:
        data_output = 'all_worlds_'+date.today().strftime('%d-%m-%Y')+'.txt'

    else:
        data_output = input_filename

    # First, if data not already in the CWD, query data from all transiting exoplanets smaller than 4 REarth, 
    # with equilibrium temperatures smaller than 1000 K from the NASA exoplanet archive (if this is the first time 
    # this is done, this will take a sec or two):
    if not os.path.exists(data_output):

        service = vo.dal.TAPService("https://exoplanetarchive.ipac.caltech.edu/TAP")

        # List of column names: https://exoplanetarchive.ipac.caltech.edu/docs/API_PS_columns.html
        sql_query = "SELECT pl_name,disc_facility,tic_id,pl_rade,pl_radeerr1, pl_radeerr2,pl_bmasse,pl_bmasseerr1, pl_bmasseerr2,pl_orbper,pl_eqt,pl_dens,pl_trandep,pl_trandur,sy_jmag,sy_tmag,st_teff,st_rad "+\
                    "FROM ps "+\
                    "WHERE tran_flag=1"

        results = service.search(sql_query)

        # Save to table:
        table = results.to_table()
        table.write(data_output, format = 'ascii')

    else:

        table = Table.read(data_output, format = 'ascii')

    return table
