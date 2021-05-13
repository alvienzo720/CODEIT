import pandas  as pd
from yahoo_fin import stock_info
from plotly.offline import plot, init_notebook_mode
init_notebook_mode()
import cufflinks as cf
%matplotlib inline
cf.set_config_file(offline=True)