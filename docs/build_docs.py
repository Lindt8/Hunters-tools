'''
This script serves to automate production of HTML documentation for Hunters tools using [pdoc](https://github.com/pdoc3/pdoc) 
'''

import pdoc
import os
import sys

output_dir = os.path.dirname(os.path.abspath(__file__))  # this script is in /docs/
sys.path.insert(0, os.path.abspath(os.path.join(output_dir, '..')))

# Build documentation following pdoc instructions: https://pdoc3.github.io/pdoc/doc/pdoc/#programmatic-usage
modules = ['Hunters_tools'] 
context = pdoc.Context()
modules = [pdoc.Module(mod, context=context) for mod in modules]
pdoc.link_inheritance(context)

def recursive_htmls(mod):
    yield mod.name, mod.html(sort_identifiers=False)
    for submod in mod.submodules():
        yield from recursive_htmls(submod)

for mod in modules:
    for module_name, html in recursive_htmls(mod):
        if module_name == 'Hunters_tools':
            html_file_name = 'index.html'
        else:
            html_file_name = module_name + '.html'
        html = html.replace('width:70%;max-width:100ch;', 'width:70%;max-width:120ch;',1)  # make page contents wider
        # add version number
        #html = html.replace('</code></h1>','</code> <i><small>(v'+VERSION_NUMBER+')</small></i></h1>', 1)
        with open(os.path.join(output_dir, html_file_name), 'w') as f:
            f.write(html)


