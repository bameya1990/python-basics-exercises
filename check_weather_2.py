weather = (input("What's the weather like?")).lower()

match weather:
	case "sunny":
		print("It's a beautiful day!")
	case "rainy":
		print("Let's get an umbrella")
	case _:
		print("Let's stay inside")