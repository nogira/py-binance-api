import requests
from bs4 import BeautifulSoup, element

url = "https://binance-docs.github.io/apidocs/spot/en/#change-log"
x = requests.get(url)
soup = BeautifulSoup(x.text, "html.parser")
content_list = soup.find('div', class_="content").contents

out = {}

def reset_out():
    global out

    # initialise if empty
    if out == {}:
        out['pyFile'] = ''

    # reset
    out['requestType'] = ''    # GET, POST, DELETE
    out['securityType'] = ''   # 'API+sig', 'API'
    out['title'] = ''
    out['endpoint'] = ''
    out['upperInfo'] = ''
    out['weight'] = ''
    out['paramsPresent'] = False
    out['paramTable'] = {}
    out['paramsInput'] = ''
    out['mandParamsDict'] = ''
    out['optParamsDict'] = ''
    out['lowerInfo'] = ''

# initialise out
reset_out()

# ----------get function names----------
# open file
func_text = open('/'.join(__file__.split('/')[:-1])+'/function names.md').read()
import re
# remove all headings
func_text = re.sub("#.*\n", "", func_text)
# split into ref+name
split1 = func_text.split('\n\n')
# split ref and name into dict
functionnames = {}
for elem in split1:
    func_key, func_val = elem.split('\n')
    functionnames[func_key] = func_val.replace('`', '')

# import api core
core = open('/'.join(__file__.split('/')[:-1])+'/core.py').read()
out['pyFile'] += core+"\n\n"

# function that adds the function to the file
def add_func_to_pyFile():
    global out

    print(out['title'])

    # set security type
    type1 = 'TRADE' in out['title'] or 'MARGIN' in out['title']\
        or 'USER_DATA' in out['title'] or '(HMAC SHA256)' in out['endpoint']

    if type1:
        out['securityType'] = 'API+sig'
    else: 
        out['securityType'] = 'API'

    # --------------------------START ADDING TO pyFile--------------------------

    if out['title'] != '' and out['requestType'] != '':
        
        out['pyFile'] += f"def {functionnames[out['title']]}({out['paramsInput']}):\n"\
                    f"    \"\"\"# {out['title']}\n"\
                    f"#### `{out['endpoint']}`\n"\
                    f"{out['upperInfo']}\n"\
                    f"### {out['weight']}\n"

        # -------------------------TABLE-------------------------
        if out['paramTable'] != {}:
            col_names = list(out['paramTable'].keys())
            num_cols = len(col_names)
            tbl = '\t|'.join(col_names)+\
                  '\n'+'--------|'*(num_cols-1) + '--------\n'
            for i in range(len(out['paramTable'][col_names[0]])):
                temp_list = [out['paramTable'][col][i] for col in col_names]
                tbl += '\t|'.join(temp_list)+'\n'

            out['pyFile'] += "### Parameters:\n\n"\
                            f"{tbl}"
        else:
            out['pyFile'] += "### Parameters:\nNONE"

        # -------------------------------------------------------
        if out['lowerInfo'] != '':
            out['pyFile'] += "\n"+out['lowerInfo']
        
        # -------------------------------------------------------
        out['pyFile'] += "    \"\"\"\n"

        # modify endpoint so can use it in function
        out['endpoint'] = out['endpoint'].replace('GET ', '')\
                                        .replace('POST ', '')\
                                        .replace('Post ', '')\
                                        .replace(' (HMAC SHA256)', '')\
                                        .strip()

        out['pyFile'] += f"    endpoint = '{out['endpoint']}'\n"\
                        "    params = {\n"\
                        f"{out['mandParamsDict']}\n"\
                        "    }\n"\
                        f"{out['optParamsDict']}\n"


        if out['requestType'] == 'GET':
            if out['securityType'] == 'API+sig':
                out['pyFile'] += f"\n    return getbinancedata_sig(endpoint, params)\n\n\n"
            else:
                out['pyFile'] += f"\n    return getbinancedata(endpoint, params)\n\n\n"

        elif out['requestType'] == 'POST':
            out['pyFile'] += f"\n    return postbinancedata_sig(endpoint, params)\n\n\n"
        
        elif out['requestType'] == 'DELETE':
            out['pyFile'] += f"\n    return deletebinancedata_sig(endpoint, params)\n\n\n"


start = False

html_list_len = len(content_list)

for i in range(html_list_len):
    content = content_list[i]
    
    # wait for the starting h1 tag
    if not(start) and type(content) == element.Tag and content.has_attr('id'):
        if 'wallet-endpoints' in content['id']\
             or 'spot-account-trade' in content['id']\
                 or 'savings-endpoints' in content['id']:
            start = True


    if start:
    
        # set contents
        if type(content) != element.NavigableString and\
        len(content.contents) > 0:
            content_i0 = str(content.contents[0])

        # skip blank lines
        if content == '\n':
            pass

        # find h1 title for start of new docs section
        elif content.name == 'h1':
            
            # pause adding to pyFile if reaches websocket section
            if 'websocket-market-streams' in content['id']\
                or 'user-data-streams' in content['id']:
                start = False

            # end looping if it reaches the first heading which has no APIs
            if str(content) == '<h1 id="error-codes">Error Codes</h1>':
                break

            # only run if adding to pyFile not paused
            if start:
                line = f"# {'-'*78}\n\n"
                space_len = ' '*int((80 -len(content_i0)) /2 - 2)
                out['pyFile'] += f"{line}# {space_len}{content_i0}\n\n{line}"

        elif content.name == 'h2':

            # add previous function to pyFile----------
            add_func_to_pyFile()

            # reset everything for start of new function
            reset_out()

            # set new title
            out['title'] = content_i0

        elif content.name == 'p':

            isRIGHTaftertitle = out['title'] != '' and out['endpoint'] == ''
            isrequest = ('GET /' in content_i0 or 'Get /' in content_i0\
                        or 'POST /' in content_i0 or 'DELETE /' in content_i0)

            isaftertitlebeforeparam = out['title'] != '' and out['paramTable'] == {}

            isafterparam = out['paramTable'] != {}

            # -------------------GET ENDPOINT-------------------
            if isRIGHTaftertitle and isrequest:
                out['endpoint'] = content_i0\
                    .replace('<code>\n', '')\
                    .replace('\n</code>', '')\
                    .replace('<code>', '')\
                    .replace('</code>', '')
                
                indexoffirstspace = out['endpoint'].find(' ')
                out['requestType'] = out['endpoint'][:indexoffirstspace].upper()

            # ---------------BETWEEN ENDPOINT AND TABLE---------------
            elif isaftertitlebeforeparam:
                # print("test->", content_i0)

                if 'Weight' in content_i0:
                    for tag in content:
                        out['weight'] += str(tag).replace('<strong>', '')\
                                                .replace('</strong>', '')

                elif 'Parameters' in content_i0:
                    out['paramsPresent'] = True
                else:
                    for tag in content:
                        out['upperInfo'] += str(tag).replace('<code>', '`')\
                                                    .replace('</code>', '`')

            elif isafterparam:
                out['lowerInfo'] += content_i0

            else: print('??????', content_i0)

        #                                        only get the params table
        elif content.name == 'table' and out['paramsPresent'] and out['paramTable'] == {}\
            and 'Name' in str(content):
            

            # ------------------TITLES------------------
            col_titles = content.select('thead>tr>th')
            if len(col_titles) > 1:
                for title in col_titles:
                    # conv to str and remove 'th' tags on either side of string
                    title = str(title)[4:-5]
                    out['paramTable'][title] = []

            # ------------------ENTRIES------------------
                col_entries = content.select('tbody>tr>td')
                num_rows = int(len(col_entries) / len(col_titles))

                for i in range(num_rows):   # run once per row

                    for col in out['paramTable'].keys():
                        # conv to str and remove 'th' tags on either side of str
                        entry = str(col_entries.pop(0))[4:-5]
                        out['paramTable'][col] += [entry]

            # ---------------SETUP PARAMS-----------------
                mand_list = []; opt_list = []
                for num, name in enumerate(out['paramTable']['Name']):
                    # timestamp is built into the function so need to remove
                    if name != "timestamp":
                        if out['paramTable']['Mandatory'][num] == 'YES':
                            mand_list.append(name)
                        else:
                            opt_list.append(name)

                if len(mand_list) > 0:
                    out['paramsInput'] += ', '.join(mand_list)

                    temp_list = [f'        "{param}": {param}' for param in mand_list]
                    out['mandParamsDict'] += ',\n'.join(temp_list)

                    if len(opt_list) > 0:
                        out['paramsInput'] += ', '

                if len(opt_list) > 0:
                    out['paramsInput'] += '="", '.join(opt_list)+'=""'

                    temp_list = [f'    if {param} != "": params["{param}"] = {param}' 
                                    for param in opt_list]
                    out['optParamsDict'] += '\n'.join(temp_list)

        # to make sure the function gets added even if its right before a new set 
        # of functions, or is the very last function (the very last function is 
        # right before a h1)
        if content_list[i+1].name == 'h1':
            add_func_to_pyFile()

            # reset everything for start of new function
            reset_out()


# just some tweaks to formatting
out['pyFile'] = out['pyFile'].replace('<a href="#email-address">', '')\
                            .replace('</a>', '')

           # get filepath for current folder
with open('/'.join(__file__.split('/')[:-1])+'/pybinanceapi/generated.py', 'w') as file:
    file.write(out['pyFile'])