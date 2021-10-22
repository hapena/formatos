import xml.etree.ElementTree as et
import re
xml = et.parse ("myfile.xml")
root = xml.getroot()

ns = re.match ('{.*}', root.tag) .group (0)
editconf = root.find ("{}edit-config".format (ns))
defop = editconf.find ("{}default-operation".format (ns))
testop = editconf.find ("{}test-option".format (ns))

print ("La operación predeterminada contiene: {}".format(defop.text))
print ("La opción de prueba contiene: {}".format(testop.text))
