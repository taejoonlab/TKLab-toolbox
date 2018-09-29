from ete3 import Tree,TreeStyle,TextFace

t = Tree('tagfrog.phy')
for node in t.traverse():
    node.img_style['size'] = 3
    if node.is_leaf():
        name_face = TextFace(node.name)
ts = TreeStyle()
ts.show_scale = True
t.render('tagfrog.pdf')
