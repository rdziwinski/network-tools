from ipaddress import *
import os, sys

def main():
	filename = sys.argv[1]
	#ipki = os.popen("cat ip | grep 79.110 | awk '{print $1}' | sort -t . -k 2,2n -k 3,3n -k 4,4n").read()

	command = "cat "+filename+" | grep 79.110 | awk '{print $1}' | sort -t . -k 2,2n -k 3,3n -k 4,4n"
	ipki = os.popen(command).read()
	print(command)
	ipki = list(filter(None, str(ipki).split("\n")))


	i = 1
	j = 0
	while i < len(ipki) - 1:
		net = ip_network(ipki[i])
		next_net = str(ip_network(ipki[i+1]))
		next_pool = str(net.broadcast_address + 1)


		if str(next_pool.split('/', 1)[0]) != str(next_net).split('/', 1)[0]:
			#ret = str(next_net)
			print(net) 
			free = "                  | Free: " + next_pool + "/?"
			print(free)
			print(next_net)
			j+=1
		i+=1

	free_summary = "Minimal number of free pool:" + str(j)
	print(free_summary)

main()