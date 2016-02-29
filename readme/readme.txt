plugin for CudaText.
Formats YAML code (needs lexer "YAML") using library
  http://pyyaml.org
  
currently not supports config file (I cannot find info about config values..)
needs correction of original yaml lib: you need to find all places of "inf_value", "nan_value"
and del crappy code (comment it and set inf_value/nan_value to e.g. 1e300/1e400).


Author: Alexey T.
