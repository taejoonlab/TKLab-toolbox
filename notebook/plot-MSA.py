#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('lsmagic', '')


# In[14]:


str_svg = '''
<svg width="100" height="100">
    <circle cx="50" cy="50" r="40" stroke="green" stroke-width="4" fill="yellow" />
</svg>
'''
print(str_svg)


# In[105]:


## to print SVG directly to output cell
from IPython.display import Markdown, display
def printmd(string):
    display(Markdown(string))

printmd(str_svg)


# In[17]:


get_ipython().run_cell_magic('html', '', '<svg width="100" height="100">\n    <circle cx="50" cy="50" r="40" stroke="green" stroke-width="4" fill="yellow" />\n</svg>')


# In[120]:


import gzip
import sys

def read_fasta(tmp_filename):
    seq_list = dict()
    f = open(tmp_filename, 'r')
    if tmp_filename.endswith('.gz'):
        f = gzip.open(tmp_filename, 'rt')

    for line in f:
        if line.startswith('>'):
            tmp_h = line.strip().lstrip('>')
            seq_list[tmp_h] = ''
        else:
            seq_list[tmp_h] += line.strip()
    f.close()
    return seq_list

filename_msa = 'ZymoD6300_standard_16S.msa.fa'
msa_list = read_fasta(filename_msa)

# check MSA data
msa_seqlen = 0
mismatch_list = dict()
for tmp_h in msa_list.keys():
    tmp_seqlen =len(msa_list[tmp_h])
    if msa_seqlen == 0:
        msa_seqlen = tmp_seqlen
    elif msa_seqlen != tmp_seqlen:
        sys.stderr.write('Different seq length: %s (%d vs. %s)\n' % (tmp_h, tmp_seqlen, msa_seqlen))
    
    mismatch_list[tmp_h] = ['=' for x in range(0, msa_seqlen)]

sys.stderr.write('Check seq, length: %d\n' % msa_seqlen)

seq_count = len(msa_list)
cons_seq_list = ["n" for i in range(0, msa_seqlen)]
for i in range(0, msa_seqlen):
    tmp_freq = dict()
    for tmp_h in msa_list.keys():
        tmp_n = msa_list[tmp_h][i]
        if tmp_n not in tmp_freq:
            tmp_freq[tmp_n] = 0
        tmp_freq[tmp_n] += 1
    
    rep_n = sorted(tmp_freq.keys(), key=tmp_freq.get)[-1]
    rep_n_freq = tmp_freq[rep_n]
    if rep_n_freq < seq_count * 0.5:
        rep_n = 'x'
    elif rep_n_freq > seq_count * 0.8:
        rep_n = rep_n.upper()
    else:
        rep_n = rep_n.lower()
        
    cons_seq_list[i] = rep_n
    
    # Compile mismatch_str for each sequence
    for tmp_h in msa_list.keys():
        tmp_n = msa_list[tmp_h][i]
        if tmp_n == '-':
            mismatch_list[tmp_h][i] = '-'
        elif rep_n_freq > seq_count * 0.8:
            mismatch_list[tmp_h][i] = '*'
        elif tmp_n != rep_n:
            mismatch_list[tmp_h][i] = tmp_n

cons_seq = ''.join(cons_seq_list)
sys.stderr.write('Consensus seq: %s ... %s' % (cons_seq[:50], cons_seq[-50:]))

for tmp_h in msa_list.keys():
    print(''.join(mismatch_list[tmp_h][:50]), tmp_h)
#for tmp_h in msa_list.keys():
#    print(''.join(msa_list[tmp_h][:50]), tmp_h)


# In[177]:


pos_y_init = 50
pos_y_grid = 25
pos_y_box_init = 50
pos_y_label_init = 46
pos_y_step = 22

pos_x_init = 10
pos_x_label_init = 620

width_box = 600
height_box = 16
height_grid = 4

fig_width = 850
fig_height = 50 + pos_y_step * seq_count

# Print the SVG style 
svg_header = '<svg height="%d" width="%d">' % (fig_height, fig_width)
svg_header += '''
  <style>
   .grid         { stroke:black; stroke-opacity:0.5; stroke-width:1 }
   .grid_label   { font:8px sans-serif; }
   .seq_id       { font:14px sans-serif; }
   .seq_box      { fill:grey; fill-opacity:0.1; stroke:darkgrey; stroke-width:1 }
   .seq_gap      { stroke:black; stroke-opacity:0.25; stroke-width:1 }
   .seq_mm       { stroke:red; stroke-opacity:0.25; stroke-width:1 }
   .seq_cons     { stroke:green; stroke-opacity:0.25; stroke-width:1 }
  </style>
'''

svg_body = ''

# Print scale
seq_scale = width_box / msa_seqlen

# Grid
svg_body += '  <line class="grid" x1="%d" x2="%d" y1="%d" y2="%d"/>\n' %              (pos_x_init, pos_x_init + width_box, pos_y_grid, pos_y_grid)
for i in range(0, msa_seqlen, 200):
    pos_x_grid = pos_x_init + i * seq_scale
    svg_body += '  <text x="%d" y="%d" class="seq_id"> %d </text>\n' % (pos_x_grid, pos_y_grid-height_grid, i)
    svg_body += '  <line class="grid" x1="%d" x2="%d" y1="%d" y2="%d" />\n' %                 (pos_x_grid, pos_x_grid, pos_y_grid+height_grid, pos_y_grid-height_grid)

# Print the seq box
pos_y = pos_y_box_init - height_box
pos_x = pos_x_init
for tmp_h in mismatch_list.keys():
    svg_body += '  <rect class="seq_box" x="%d" y="%d" width="%d" height="%d" />\n' % (pos_x, pos_y, width_box, height_box)

    for i in range(0, msa_seqlen):
        tmp_pos_idx = int(i * seq_scale)
        pos_x_mm = pos_x + tmp_pos_idx
        if mismatch_list[tmp_h][i] == '-':
            svg_body += '    <line class="seq_gap" x1="%d" x2="%d" y1="%d" y2="%d" />\n' %                             (pos_x_mm, pos_x_mm, pos_y, pos_y+height_box)
        elif mismatch_list[tmp_h][i] != '*':
            svg_body += '    <line class="seq_mm" x1="%d" x2="%d" y1="%d" y2="%d" />\n' %                             (pos_x_mm, pos_x_mm, pos_y, pos_y+height_box)
            
    pos_y += pos_y_step

# Consensus sequence
svg_body += '  <rect class="seq_box" x="%d" y="%d" width="%d" height="%d" />\n' % (pos_x, pos_y, width_box, height_box)
for i in range(0, msa_seqlen):
    tmp_pos_idx = int(i * seq_scale)
    pos_x_cons = pos_x + tmp_pos_idx
    if cons_seq_list[i] in ['A', 'T', 'G', 'C']:
        svg_body += '    <line class="seq_cons" x1="%d" x2="%d" y1="%d" y2="%d" />\n' %                             (pos_x_cons, pos_x_cons, pos_y, pos_y+height_box)

# Print the sequence labels
pos_y = pos_y_label_init
pos_x = pos_x_label_init
for tmp_h in mismatch_list.keys():
    svg_body += '  <text x="%d" y="%d" class="seq_id"> %s </text>\n' % (pos_x, pos_y, tmp_h)
    pos_y += pos_y_step

# Consensus sequence
svg_body += '  <text x="%d" y="%d" class="seq_id"> %s </text>\n' % (pos_x, pos_y, "Consensus")

svg_footer = '</svg>\n'

#print(svg_body)
printmd(svg_header+svg_body+svg_footer)
#print(cons_seq)


# In[ ]:




