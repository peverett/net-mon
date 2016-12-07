# Network Monitoring Bash Scripts
 
In order to monitor my home broadband internet connection, I set up my
Raspberry Pi (Model B+) with some simple scripts to capture net work logs
- Speed test - for download and upload speed
- Ping test - for ping times and packet loss

## System Configuration 
### Hardware and OS setup
* Raspberry Pi Model B+ - should work for any Raspberry Pi.
* [Raspbian GNU/Linux 8 (jessie)](http://www.raspbian.org)  4.4.21+ #911 Thu Sep 15 14:17:52 BST 2016 
* Initially set up your Pi using a keyboard and screen - but if you configure
  SSH you won't need them after the initial config.
* Connect the Pi directly to the broadband router by an Ethernet cable - do
  not use WiFi, speed tests can be limited by your WiFi speed and won't be
  accurate.

### Software setup
1. Before you begin, make a note of the Pi's IP address in order to connect
   via SSH later, `$ ifconfig eth0`. 
* Enable the SSH server on the Pi:
    1. On the command line `$ sudo raspi-config`
    2. Select *Advanced options*
    3. Select *SSH* 
    4. In the dialog  'Would you like to enable the SSH server' - select *Yes*
    5. Back in the main menu, select *Finish* 
    6. Reboot for changes to take effect `$sudo shutdown -r now`
* Use an SSH client to connect remotely to the Pi, I like [PuTTY](https://www.chiark.greenend.org.uk/$sgtatham/putty/)
* Install Speedtest-cli - this is a command line speedtest app written in Python, it works in the same way as the [speedtest.net](http://www.speedtest.net) website. To install it:
    1. sudo apt-get install python-pip
    2. sudo pip install speedtest-cli

## Scripts

* *speedtest.sh* - This runs the speedtest-cli Python script and stores the 
  output in a filename with a date and time stamp e.g. speedtest.161205-1530,
  results are stored in ~/results/.
* *pingtest.sh* - Like the previous shell script, this runs a ping command 
  against the Google DNS server address (8.8.8.8) for a count of 60 e.g. an 
  ICMP ping packet every second for 60-seconds. Again, results are stored 
  in a file with the date and time stamp in the name e.g. 
  pintest.161205-1551. These are also saved to the ~/results/ directory.
* *collate_speed.py* - collates all the speedtest download and upload results
  into a Comma Separated Value (CSV) format summary - the resulting file can 
  then be easily imported into a spreadsheet for analysis or graphs.
* *collage_ping.py* - collates ping test results into two CSV files, one for
  just the packet loss statistics and one for all the other ping stats.

## Run scripts as a cron job
1. Edit the system cron jobs using the command `$ crontab -e`
2. This is an example of how I configured it:
   ```
    # Edit this file to introduce tasks to be run by cron.
    # 
    # Each task to run has to be defined through a single line indicating with different fields when the task will be run and what command to run for the task
    # 
    # To define the time you can provide concrete values for minute (m), hour (h), day of month (dom), month (mon), and day of week (dow) or use '*' in these fields 
    # (for 'any').# Notice that tasks will be started based on the cron's system daemon's notion of time and timezones.
    # 
    # Output of the crontab jobs (including errors) is sent through email to the user the crontab file belongs to (unless redirected).
    # 
    # For example, you can run a backup of all your user accounts at 5 a.m every week with: 0 5 * * 1 tar -zcf /var/backups/home.tgz /home/
    # 
    # For more information see the manual pages of crontab(5) and cron(8)
    # 
    # m h dom mon dow command
    */10 * * * 2 /home/pi/cookbook/net-mon/pingtest.sh && /home/pi/cookbook/net-mon/speedtest.sh
   ```
   With this configuration, the ping test is run every 10-minutes and the
   speedtest is run after it finishes. The tests only run on a Tuesday 
   (day 2 in Days Of Week (dow).

