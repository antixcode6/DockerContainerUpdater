import docker
import subprocess



#declare docker object
client = docker.from_env()



#Identify current running containers and store them in file
def identify_containers():
    subprocess.call(docker pull <URL to updated repo>
    running_containers = client.containers.list(all=True)

    file_path = '/etc/path/to/file/containernames.txt'

    container_list = open(file_path,'w')

    container_list.write(running_containers)
    standup_containers()


#runs the linux command to stand up new containers
def standup_containers():
    for i in range(5):
        subprocess.call("docker run -e 'MINION_LOCATION_KEY=mykey' -v /tmp:/tmp:rw -v /var/run/docker.sock:/var/run/docker.sock:rw <updated repo URL>")
    teardown_containers()

#kills and prunes containers from previous function
def teardown_containers():
    container_list = []

    with open('/etc/path/to/file/containernames.txt') as fp:

        for line in fp:

            container_list.append(line)

    container_obj = docker.APIClient()

    for containers in container_list:

        container_obj.kill(container=containers)


        
if __name__ == "__main__":
  identify_containers()
  logrotate()
