name = raw_input()
if "." not in name:
    extension = raw_input()
else:
    extension = name[name.index(".") + 1:]
    name = name[:name.index(".")]
extension = extension.lower()

print '"' + name + '"' + " - " + extension 
