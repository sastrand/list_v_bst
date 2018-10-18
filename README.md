## Data Structures
### Lab I of II: BST

Time how long it takes to accept or reject each IP address in the traffic file when the white list is stored in:
   * An unsorted list
   * A binary search tree built from an unsorted list   
   * A set
   
If there's time during lab, sort the input files and time how long it takes to accept or reject each IP address in the traffic file when the white list is stored in:
   * A sorted list
   * A binary search tree built from a sorted list

In the data directory are four files of IP addresses:
   * `traffic.txt` contains 1,048,576 IP address
   * `whitelist.txt` contains 1024 IP addresses
   * `traffic_test.txt` contains 16 IP addresses
   * `whitelist_test.txt` contains 4 IP addresses
   
These should be sufficient to show some trade-offs between these data structures, but you can use the `gen_ip.py` script to generate more or different files. Its command-line parameters are described in the comments at the top of the file.

For this lab, implement `firewall.py`.
