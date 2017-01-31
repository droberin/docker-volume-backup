# -*- coding: utf-8 -*-

import docker
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

client = docker.from_env()

containers = client.containers.list(all=True)
backup_folders = dict()
for container in containers:
    container_name = container.attrs['Name']
    backup_folders[container_name] = dict()
    backup_folders[container_name]['id'] = container.attrs['Id']
    backup_folders[container_name]['mounts'] = dict()
    backup_folders[container_name]['mounts']['folders'] = list()
    
    for mount in container.attrs['Mounts']:
        backup_folders[container_name]['mounts']['folders'] += [{mount['Source']: mount['Destination']}]


# print(backup_folders)

for container_name in backup_folders:
#    print(container_folders['mounts'])
    container_id = backup_folders[container_name]['id']
    if len(backup_folders[container_name]['mounts']['folders']) > 0:
        logging.info("[{}] Container: {}".format(container_id,container_name))
        for folders in backup_folders[container_name]['mounts']['folders']:
            logging.info("[{}]\tHas folders: {}".format(container_id, folders))
    else:
        logging.info("[{}] '{}' No volumes found".format(container_id, container_name))

#    for mounts in container_folders['mounts'].keys():
#        for supreme_index in mounts:
#            print(container_folders['mounts'][supreme_index])

#    print("[{}] Backing up volume {}".format(folder['vol'], backup_folders[folder]))

# containers = client.containers.run("ubuntu", "echo hello world", remove=True)

