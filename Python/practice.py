with open("temp_not.txt","w") as file:
    subprocess.run(['ls','-lart','/Users/balrams/Desktop/Learnings/Python/20180716','notdire'], stdout=file, stderr=subprocess.STDOUT)
