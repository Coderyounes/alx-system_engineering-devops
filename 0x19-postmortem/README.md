## Incident Report - Apache 500 Wordpress

<img src="http://www.quickmeme.com/img/b5/b51b1031af5d1517cdfe9421c9e6338aa1987615331e9b5e80b47ce110f468e1.jpg" alt="Gif" >

### Issue summary:
February 10th, 2024 from 10:00 WET (Casablanca time) to 12:30 WET.\
The Servers Down , the user are unable to Open the web appication.\
user affected 100%.\
Root cause typography in Code function file loaded in wp-setting.php
### Timeline:
The issue was detected in 10:03 (WET).\
datadog send a monitoring alert to enginner via pageduty.\
Start by Checking the last update before the deployement, then parse apache Logs.\
the incident was escalted to Younes Bousfiha Our Backend Enginner
He was able to resolve the issue from the stack traces using strace tool & tmux.
### Root Cause:
typography inside wp-settings.php.\
We create a new Core function for our wordpress store , after try to loading it we add a phpp extension in some file.
the issue was Fixed via puppet script, in which the script will detect each .phpp inside the wp-setting file then update it to .php.
### Corrective and preventative measures:
We need to Setup a control over the critical worpress files to protect us from such situation in the future.\
So we will Build a github action workflow that will Check our Critical wordpress files like wp-settings.php & make sure that there no extentions typo again.\
TODO:\
Read Documentation PHP CodeSniffer (PHPCS)
Create a Coding Standard using WPCS (WordPress Coding Standards)
Write script & integrate with Github actions
Test it.

