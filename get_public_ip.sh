#########################################################################
# File Name: get_ip.sh
# Author: averainy
# mail: averainy@gmail.com
# Created Time: 2013年01月25日 星期五 16时48分09秒
#########################################################################
#!/bin/bash
IP=$(curl http://ifconfig.me/ 2>/dev/null )
echo $IP;  
