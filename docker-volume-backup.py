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
    backup_folders[container_name]['status'] = container.attrs['State']['Status']

    for mount in container.attrs['Mounts']:
        backup_folders[container_name]['mounts']['folders'] += [{mount['Source']: mount['Destination']}]


# print(backup_folders)

for container_name in backup_folders:
    # print(container_folders['mounts'])
    container_id = backup_folders[container_name]['id']
    container_status = backup_folders[container_name]['status']
    container_volume_count = len(backup_folders[container_name]['mounts']['folders'])
    if container_volume_count > 0:
        logging.info("[{}] Container '{}' (Status: {}): {} volume(s) found".format(
            container_id,
            container_name,
            container_status,
            container_volume_count
            )
        )
        for folders in backup_folders[container_name]['mounts']['folders']:
            logging.info("[{}]\tHas folders: {}".format(container_id, folders))
    else:
        logging.info("[{}] Container '{}' (Status: {}): No volumes found".format(
            container_id,
            container_name,
            container_status
            )
        )

# return_run = client.containers.run("ubuntu", "echo hello world", remove=True)

