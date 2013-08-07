"""
PitchShifter

"""

from scale import Scale

class PitchShifter:
  """
  Pitch shifter
  """
  
  def __init__(self, scale=None, mix=0.5):
    """
    """
    
    self.scale = scale
    self.previous_frame = []
    self.mix = mix
  
  def get_mix(src_frame, shifted_frame):
    """
    """
    
    result = []
    
    c_mix = 1 - self.mix
    
    for i in range(len(src_frame)):
      result.append(src_frame*c_mix + shifted_frame*self.mix)
    
    return result
  
  def pitch_shift(self, frame):
    """
    """
    
    result = []
    
    shifted_frame = self.scale.get_shifted(frame)
    
    mixed = mix(frame, shifted_frame)
    
    result = mixed
    
    self.previous_frame = frame
    
    return result
    
