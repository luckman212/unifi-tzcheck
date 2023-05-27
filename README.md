# unifi-tzcheck

### What?

A little Python script that dumps a sorted list of sites, and their timezone as a consistency check.

### Why?

There's no built-in way to view the Timezone setting across all sites of a Unifi controller.

Related forum thread: https://community.ui.com/questions/Is-there-a-way-to-set-the-default-time-zone-used-for-new-sites-in-the-controller/6ac47bb0-7143-41a4-8b8d-ed9b3f8ec06e

### How?

1. [Download][1] the tzcheck.py script and copy it to your Unifi controller
2. Run `chmod +x tzcheck.py` to make it executable
3. Run `./tzcheck.py`

[1]: https://raw.githubusercontent.com/luckman212/unifi-tzcheck/main/tzcheck.py
