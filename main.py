from SimpleCLI import SimpleCLI
import functions as functions

SimpleCLI(functions)




#commands list
#help : show all commands
#new/touch/mk -priority issue : make new issues
#l/ls/dir -c -a/d: show current issues, c shows closed issues only, s sorts
#append/add # value: add something to the issue
#amend/edit # -# value : # change priority, string changes description
#close/release/rel/cl # : close issue

#current version will overwrite the json file on every change, might change
#to something more efficient later on, but since this is used for personal
#projects, I'll hold off on it. Might also add push support to a remote directory
