# vim: set filetype=python :

def configure(conf):
    conf.load('tex')
    conf.load('pandoc', tooldir='.')

def build(bld):
    sources = """
        Introduction.pd
        ch_First/chapter.latex
        ch_First/sec_Intro.pd
        ch_First/sec_Moar.pd
        ch_First/sec_Solutions.pd
        ch_First/sec_Tools.pd
        ch_Second/chapter.latex
        ch_Second/sec_Bioc.pd
        ch_Second/sec_Web.pd
        ch_Second/sec_Python.pd
        ch_Second/sec_Backend.pd
        ch_Second/sec_Frontend.pd
        ch_Third/chapter.latex
        ch_Third/sec_RBlock.pd
        ch_Third/sec_Python.pd
        ch_Third/sec_Frontend.pd
        ch_Third/sec_Outro.pd
        Conclusion.pd
        Extras.pd
    """
    bld(features='pandoc-merge', source=sources + ' bib.bib', target='main.latex',
            disabled_exts='fancy_lists', 
            flags='-R -S --latex-engine=xelatex --listings --chapters',
            linkflags='--toc --chapters -R', template='template.latex')

    # Outputs main.pdf
    bld(features='tex', type='xelatex', source='main.latex', prompt=True)
    bld.add_manual_dependency(bld.bldnode.find_or_declare('thesis.pdf'),
                              bld.srcnode.find_node('utf8gost705u.bst'))
