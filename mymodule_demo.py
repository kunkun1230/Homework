##import mymodule
##mymodule.sayhi()
##print('Version', mymodule.version)

#两种方式的结果相同

from mymodule import sayhi, version
# Alternative:
# from mymodule import *
sayhi()
print ('Version', version)
