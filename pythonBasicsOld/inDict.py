# in function use in dictionary

port = {80: "HTTP", 23 : "Telnet", 443 : "HTTPS"}

key = eval(input("Please enter key: "))
if key in port:
    print(port[key])
elif key not in port:
    print("Nothing present at provided key in port", port[key])
