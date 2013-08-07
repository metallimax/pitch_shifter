import argparse
import os
import wave

from pitchshifter import pitchshifter, scale

parser = argparse.ArgumentParser(description='Discrete distance based pitch shifter.')
parser.add_argument('-i', '--input-file', default='input.wav', help='Input file')
parser.add_argument('-o', '--output-file', default='output.wav', help='Output file')
args = parser.parse_args()


def process(**kw):
  """
  """
  
  in_f = wave.open(kw['input_file'], "r")
  out_f = wave.open(kw['output_file'], "w")
  (nchannels, sampwidth, framerate, nframes, comptype, compname) = params = in_f.getparams()
  out_f.setparams(params)
  
  in_f.close()
  out_f.close()

def check(**kw):
  """
  """
  
  return True

def main(**kw):
  """
  """
  
  checked = check(**kw)
  
  if checked is not True:
    print checked
  else:
    process(**kw)

if __name__ == '__main__':
  context = vars(args)
  main(**context)
