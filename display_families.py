'''Scripts to display family trees using dot
'''

from findfamilies import construct_family_components, find_nuclear_families

OUTPUT_DIR = 'families_dot'
MAX_FILE_NODES = 50

def main():
    train = TitanicDataSet.get_train()
    test = TitanicDataSet.get_test()
    families = construct_family_components(train, test)
    return

    acc = []
    i = 0
    for c in families:
        if len(c.nodes) == 1:
            continue
        tune_family_relations(c)
        if sum(len(c.nodes) for c in acc) > 40:
            display_graph('families/%d.png' % (i,), acc)
            i += 1
            acc = []
        acc.append(c)
    if acc:
        display_graph('families/%d.png' % (i,), acc)

__name__ == '__main__' and main()