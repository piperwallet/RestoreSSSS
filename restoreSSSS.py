from secretsharing import PlaintextToHexSecretSharer 
done = False
parts = []
while not done:
	inVar = raw_input("Enter a part to restore: ")
	parts.append(inVar)
	inVar = raw_input("Done? (y/n): ")
	if(inVar.lower() == "y"):
		done = True



print PlaintextToHexSecretSharer.recover_secret(parts)
