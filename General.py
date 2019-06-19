import Converters
from Converters import kg_to_lbs as yes
import ecommerce.shipping as shipping

shipping.calc_shipping()

print(yes(100))

print(Converters.kg_to_lbs(70))
exit(0)
