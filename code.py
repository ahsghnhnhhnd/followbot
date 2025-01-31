import requests,scratchapi,os,time
s = scratchapi.ScratchUserSession('scraatchcgn_',str(Scratchez123)) #PUT STUFF HERE
project_id = str(PROJECTIDHERE) #PUT STUFF HERE
def users():
  #vname = f'☁ follow'
  text = requests.get(f'https://clouddata.scratch.mit.edu/logs?projectid={project_id}&limit=100&offset=0').json()
  retlist = []
  for i in text:
    retlist.append(i['user'])
    #print(i['user'])
  return tuple(set(retlist))
def main():
  for i in users():
    s.users.follow(str(i))
    time.sleep(0.3)
  return 'done'

print(users())
