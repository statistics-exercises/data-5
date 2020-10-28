import unittest
from main import *

class UnitTests(unittest.TestCase) :
   def test_xvals(self) : 
      fighand=plt.gca()
      figdat = fighand.get_lines()[0].get_xydata()
      this_x, this_y = zip(*figdat)
      for i in range( len(this_x) ) :
        self.assertTrue( np.abs(i+1 - this_x[i])<1e-7, "One or more of the x-coordinates in your graph are not correct." )
  
  def test_sorted(self) : 
      fighand=plt.gca()
      figdat = fighand.get_lines()[0].get_xydata()
      this_x, this_y = zip(*figdat)
      for i in range(1,len(this_x) ) :
        self.assertTrue( this_y[i-1]<=this_y[i], "The data plotted on the y-axis is not ascending order." )
  
