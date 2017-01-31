# -*- coding: utf-8 -*-
import docker
import logging


def get_running_containers(docker_client, search_filter=None):
    if not search_filter:
        containers = docker_client.containers.list(all=True)
    else:
        containers = docker_client.containers.list(filters=search_filter)
    backup_containers = dict()
    for container in containers:
        container_name = container.attrs['Name']
        backup_containers[container_name] = dict()
        backup_containers[container_name]['id'] = container.attrs['Id']
        backup_containers[container_name]['image'] = dict()
        image_values = container.attrs['Config']['Image'].split(":")
        if len(image_values) is 2:
            backup_containers[container_name]['image']['name'] = image_values[0]
            backup_containers[container_name]['image']['tag'] = image_values[1]
        else:
            backup_containers[container_name]['image']['name'] = image_values[0]
            backup_containers[container_name]['image']['tag'] = "latest"
        backup_containers[container_name]['status'] = container.attrs['State']['Status']
    return backup_containers


# @commit_filter: only names are valid
def commit_backup_containers(docker_client, backup_containers,
                             commit_filter=list(),
                             test=False,
                             use_export_instead=False,
                             export_folder="/tmp"):
    my_commit_backup_containers = dict()
    logging.debug("commit called")
    for container in backup_containers:
        container_name = container[1:]
        if len(commit_filter) < 1 or container_name in commit_filter:
            container_id = backup_containers[container]['id']
            image_tag = backup_containers[container]['image']['tag']
            image_name = backup_containers[container]['image']['name']
            if image_tag == "backup":
                logging.warning("Found container running with a backup image: {}"
                                ". You might wanna fix this".format(
                                    image_name)
                                )
            elif image_tag is "latest" or not None:
                logging.info("[ID: {}] [Name: {}] [Image: {} | Tag: {}] set for backup".
                             format(container_id, container_name, image_name, image_tag))
                my_commit_backup_containers[container_name] = dict()
                my_commit_backup_containers[container_name]['name'] = container_name
                my_commit_backup_containers[container_name]['origin'] = container_id
                my_commit_backup_containers[container_name]['destination_name'] = container[1:]
                my_commit_backup_containers[container_name]['destination_tag'] = 'backup'
            else:
                logging.info("Found a non tagged container... weird: {}:{}".format(container, image_tag))
        else:
            logging.debug("Container {} is out of the backup filter".format(container_name))
    if test is True:
        logging.info("commit_backup_containers: testing is set to true. Doing no commit")
        return None
    else:
        for to_backup in my_commit_backup_containers:
            backup_doing = my_commit_backup_containers[to_backup]
            if use_export_instead:
                export_destination = export_folder +\
                                     "/" +\
                                     backup_doing['destination_name'] +\
                                     "-" +\
                                     backup_doing['destination_tag'] +\
                                     ".tar"
                logging.info("[{}] exporting to {}".format(
                    backup_doing['name'],
                    export_destination,))

                with open(export_destination, "wb") as export_fd:
                    my_commit = export_fd.write(docker_client.api.export(backup_doing['name']).data)
            else:
                logging.info("[{}] backing up as {}:{}".format(
                    backup_doing['name'],
                    backup_doing['destination_name'],
                    backup_doing['destination_tag']))
                my_commit = docker_client.api.commit(
                    backup_doing['origin'],
                    backup_doing['destination_name'],
                    backup_doing['destination_tag'])
            logging.debug(my_commit)
        return len(my_commit_backup_containers)

if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)
    client = docker.from_env()
    my_filter = list()
    # my_filter.append("helloa")
    export_instead_of_commit = False
    my_containers = get_running_containers(client)
    logging.info("Amount of containers backed up/exported: {}"
                 .format(commit_backup_containers(
                        client, my_containers, commit_filter=my_filter, use_export_instead=export_instead_of_commit,)))
