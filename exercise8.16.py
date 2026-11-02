# 1. import module_name
import shirt
shirt.make_shirt('small', 'Hello')

# 2. from module_name import function_name
from shirt import make_shirt
make_shirt('medium', 'Hi there')

# 3. from module_name import function_name as fn
from shirt import make_shirt as ms
ms('large')

# 4. import module_name as mn
import shirt as s
s.make_shirt(message='Python rocks')

# 5. from module_name import *
from shirt import *
make_shirt('small')