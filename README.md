# Open Library module for Odoo

openlib module for creating a library.

### Prerequisites

First you need to get the Odoo 10.0 version from here: 

* [Odoo](https://github.com/odoo/odoo/tree/10.0)

Then download **openlib** module and copy it to **addons** folder. Remember if you copy it to another folder, you need to indicate your folder additively when starting the server.

### Running

If module is copied to the addons folder, you can run the Odoo server as usual with this command:

```
./odoo-bin --addons-path=addons
```

Or you can additively indicate your folder path:

```
./odoo-bin --addons-path=addons,<PATH>
```