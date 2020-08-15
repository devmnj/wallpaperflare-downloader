# from wallspyder import unsplash
#
# unsplash.search().filter_by_tag('travel')
import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'README.md')
print(my_file)
