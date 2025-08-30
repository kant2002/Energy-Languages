import sys, os
from subprocess import call, check_output, Popen, PIPE
from lazyme.string import color_print

path = '.'
action = 'compile'

def file_exists(file_path):
    if not file_path:
        return False
    else:
        return os.path.isfile(file_path)

def main():
  has_error = False
  for root, dirs, files in os.walk(path):
    if "_opam" in root:
      continue
    if "node_modules" in root:
      continue
    if "/bin" in root:
      continue
    if "/obj" in root:
      continue
    print('Checking ' + root)
    if file_exists(os.path.join(root, ".runignore")):
      print('Skipping ' + root + ' since it is ignore using .runignore')
      continue
    if file_exists(os.path.join(root, "..", ".runignore")):
      print('Skipping ' + root + ' since it is ignore using parent .runignore')
      continue
    makefile = os.path.join(root, "Makefile")
    if file_exists(makefile):
      cmd = 'cd ' + root + '; make ' + action
      #cmd = 'ls -la'
      pipes = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
      std_out, std_err = pipes.communicate()
      
      if (action == 'compile') | (action == 'run'):
        if pipes.returncode != 0:
          # an error happened!
          err_msg = "%s. Code: %s" % (std_err.strip(), pipes.returncode)
          color_print('[E] Error on ' + root + ': ', color='red', bold=True)
          print(err_msg)
          has_error = True
        elif len(std_err):
          # return code is 0 (no error), but we may want to
          # do something with the info on std_err
          # i.e. logger.warning(std_err)
          color_print('[OK]', color='green')
        else:
          color_print('[OK]', color='green')
      if action == 'measure':
        call(['sleep', '5'])
  if has_error:
    sys.exit(1)

if __name__ == '__main__':
  if len(sys.argv) == 2:
    act = sys.argv[1]
    if (act == 'compile') | (act == 'run') | (act == 'clean') | (act == 'measure'):
      color_print('Performing \"' + act + '\" action...', color='yellow', bold=True)
      action = act
    else:
      color_print('Error: Unrecognized action \"' + act + '\"', color='red')
      sys.exit(1)
  else:
    color_print('Performing \"compile\" action...', color='yellow', bold=True)
    action = 'compile'
  
  main()
    
