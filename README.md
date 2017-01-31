# docker-volume-backup
Docker volume backup
# docker-commit-backup
⟫ Output example with export configuration:

        2017-01-31 21:17:13,378 - root - INFO - [ID: 4ae4b1045186fb313f21ae5742457b0ae116ad01b5a2e05cb0fcefd8e22da036] [Name: happy_fermat] [Image: ubuntu | Tag: latest] set for backup
        2017-01-31 21:17:13,379 - root - INFO - [ID: 59d4b23efb3b7361db50536d303c967cb86799751aecf33617d94c0059062376] [Name: sonarqube] [Image: sonarqube | Tag: 6.1] set for backup
        2017-01-31 21:17:13,379 - root - INFO - [ID: 9981dbc511185a0ed4b99caa700caa79d39b83c51d9d21265fb0e74b4e867342] [Name: mysql] [Image: mysql | Tag: latest] set for backup
        2017-01-31 21:17:13,379 - root - INFO - [ID: cf44749f5f636b72a4518bb2939be5203bf4c7deb88d8144928ba3557b6a843e] [Name: hello] [Image: hello-world | Tag: latest] set for backup
        2017-01-31 21:17:13,379 - root - INFO - [ID: 0eb0ea004035411d3509b9d2202ad74ae307aa3975f9793dc995e2117c5d9a43] [Name: naughty_easley] [Image: ubuntu | Tag: latest] set for backup
        2017-01-31 21:17:13,379 - root - INFO - [ID: dd76165771ecc8144eab39d0f15df37d8795d2776532cd7d0c5ae891ca14ea42] [Name: hopeful_goldwasser] [Image: ubuntu | Tag: latest] set for backup
        2017-01-31 21:17:13,379 - root - INFO - [ID: 68d76e39c7f0847a39978c672348f5012c465ff3028a405a4d0a98a9a9ad776c] [Name: dazzling_ride] [Image: ubuntu | Tag: latest] set for backup
        2017-01-31 21:17:13,379 - root - INFO - [naughty_easley] exporting to /tmp/naughty_easley-backup.tar
        2017-01-31 21:17:16,592 - root - INFO - [hopeful_goldwasser] exporting to /tmp/hopeful_goldwasser-backup.tar
        2017-01-31 21:17:17,468 - root - INFO - [dazzling_ride] exporting to /tmp/dazzling_ride-backup.tar
        2017-01-31 21:17:18,321 - root - INFO - [hello] exporting to /tmp/hello-backup.tar
        2017-01-31 21:17:18,858 - root - INFO - [sonarqube] exporting to /tmp/sonarqube-backup.tar
        2017-01-31 21:17:37,923 - root - INFO - [mysql] exporting to /tmp/mysql-backup.tar
        2017-01-31 21:17:43,890 - root - INFO - [happy_fermat] exporting to /tmp/happy_fermat-backup.tar
        2017-01-31 21:17:45,510 - root - INFO - Amount of containers backed up/exported: 7

⟫  Output example with commit configuration:

        2017-01-31 21:19:03,658 - root - INFO - [ID: 4ae4b1045186fb313f21ae5742457b0ae116ad01b5a2e05cb0fcefd8e22da036] [Name: happy_fermat] [Image: ubuntu | Tag: latest] set for backup
        2017-01-31 21:19:03,658 - root - INFO - [ID: cf44749f5f636b72a4518bb2939be5203bf4c7deb88d8144928ba3557b6a843e] [Name: hello] [Image: hello-world | Tag: latest] set for backup
        2017-01-31 21:19:03,658 - root - INFO - [ID: dd76165771ecc8144eab39d0f15df37d8795d2776532cd7d0c5ae891ca14ea42] [Name: hopeful_goldwasser] [Image: ubuntu | Tag: latest] set for backup
        2017-01-31 21:19:03,658 - root - INFO - [ID: 9981dbc511185a0ed4b99caa700caa79d39b83c51d9d21265fb0e74b4e867342] [Name: mysql] [Image: mysql | Tag: latest] set for backup
        2017-01-31 21:19:03,658 - root - INFO - [ID: 0eb0ea004035411d3509b9d2202ad74ae307aa3975f9793dc995e2117c5d9a43] [Name: naughty_easley] [Image: ubuntu | Tag: latest] set for backup
        2017-01-31 21:19:03,658 - root - INFO - [ID: 68d76e39c7f0847a39978c672348f5012c465ff3028a405a4d0a98a9a9ad776c] [Name: dazzling_ride] [Image: ubuntu | Tag: latest] set for backup
        2017-01-31 21:19:03,658 - root - INFO - [ID: 59d4b23efb3b7361db50536d303c967cb86799751aecf33617d94c0059062376] [Name: sonarqube] [Image: sonarqube | Tag: 6.1] set for backup
        2017-01-31 21:19:03,658 - root - INFO - [happy_fermat] backing up as happy_fermat:backup
        2017-01-31 21:19:03,764 - root - INFO - [naughty_easley] backing up as naughty_easley:backup
        2017-01-31 21:19:03,861 - root - INFO - [dazzling_ride] backing up as dazzling_ride:backup
        2017-01-31 21:19:03,977 - root - INFO - [hopeful_goldwasser] backing up as hopeful_goldwasser:backup
        2017-01-31 21:19:04,084 - root - INFO - [hello] backing up as hello:backup
        2017-01-31 21:19:04,186 - root - INFO - [mysql] backing up as mysql:backup
        2017-01-31 21:19:04,296 - root - INFO - [sonarqube] backing up as sonarqube:backup
        2017-01-31 21:19:05,089 - root - INFO - Amount of containers backed up/exported: 7
