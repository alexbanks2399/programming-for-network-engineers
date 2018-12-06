import pexpect

#establishing the connection
ip_address = raw("What IP address do you want to connect to? \n")

username = "admin"
password = "cisco"

#creating pexpect session
session = pexpect.spawn('telnet ' + ip_address, timeout = 20)
result = session.expect(['Username:', pexpect.TIMEOUT])


if result != 0:
    print("--- FAILURE CREATING SESSION FOR: ---", ip_address)
    exit()

session.sendline(username)
result = session.expect(["Password:", pexpect.TIMEOUT])

if result != 0:
    print("--- FAILURE ENTERING PASSWORD: ---", password)
    exit()

print ("Success connecting to: ", ip_address)
print ("Username: ", username)
print ("Password: ", password)
print ("\t*10 \n")


#terminate session
session.sendline("quit")
session.close()
