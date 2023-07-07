# ply: ygen.py
#
# This is a support program that auto-generates different versions of the YACC parsing
# function with different features removed for the purposes of performance.
#
# Users should edit the method LRParser.parsedebug() in yacc.py.   The source code
# for that method is then used to create the other methods.   See the comments in
# yacc.py for further details.

import os.path
import shutil

def get_source_range(lines, tag):
    srclines = enumerate(lines)
    start_tag = '#--! %s-start' % tag
    end_tag = '#--! %s-end' % tag

    for start_index, line in srclines:
        if line.strip().startswith(start_tag):
            break

    for end_index, line in srclines:
        if line.strip().endswith(end_tag):
            break

    return (start_index + 1, end_index)

def filter_sectionion(lines, tag):
    filtered_lines = []
    include = True
    tag_text = '#--! %s' % tag
    for line in lines:
        if line.strip().startswith(tag_text):
            include = not include
        elif include:
            filtered_lines.append(line)
    return filtered_lines

def main():
    dirname = os.path.dirname(__file__)
    shutil.copy2(os.path.join(dirname, 'yacc.py'), os.path.join(dirname, 'yacc.py.bak'))
    with open(os.path.join(dirname, 'yacc.py'), 'r') as f:
        lines = f.readlines()

    parse_start, parse_end = get_source_range(lines, 'parsedebug')
    parseopt_start, parseopt_end = get_source_range(lines, 'parseopt')
    parseopt_notrack_start, parseopt_notrack_end = get_source_range(lines, 'parseopt-notrack')

    # Get the original source
    orig_lines = lines[parse_start:parse_end]

    # Filter the DEBUG sectionions out
    parseopt_lines = filter_sectionion(orig_lines, 'DEBUG')

    # Filter the TRACKING sectionions out
    parseopt_notrack_lines = filter_sectionion(parseopt_lines, 'TRACKING')

    # Replace the parser source sectionions with updated versions
    lines[parseopt_notrack_start:parseopt_notrack_end] = parseopt_notrack_lines
    lines[parseopt_start:parseopt_end] = parseopt_lines

    lines = [line.rstrip()+'\n' for line in lines]
    with open(os.path.join(dirname, 'yacc.py'), 'w') as f:
        f.writelines(lines)

    print('Updated yacc.py')

if __name__ == '__main__':
    main()
