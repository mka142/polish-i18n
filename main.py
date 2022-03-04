from sys import argv
from rich import print as rprint
from rich.table import Table


from core import translate,utils


def parse_result(result):
    return '\n'.join([f'- {r}' for r in result])

if __name__ == '__main__':
    import sys
    if '--help' in sys.argv:
        with open('./usage.txt','r') as f:
            print(f.read())
        sys.exit()    
        
    data = utils.loadyaml('./translations.yaml')
    
    term = sys.argv[-1]
    
    table = Table(
        show_header=True,
        header_style="bold",
        show_lines=True)
    
    table.add_column(f'Terms for [blue]{term}[/blue]')
    table.add_column('results')
        
    if 'get' in sys.argv:
        result = translate.get(data,term)
        
        if(result):
            rprint(f'[bold]Result for [blue]{term}[/blue]: [green]{result}[/green][/bold]')
        sys.exit()
    
    elif 'find' in sys.argv:
        result = translate.find(data,term)
        table.add_row(term,parse_result(result))
    
    elif 'propose' in sys.argv:
        terms = translate.propose(data,term)
        
        for _term,result in terms.items():
            table.add_row(_term,parse_result(result))
        
    else:
        print('wrong option specified. Try --help to see options')
        sys.exit()
    
    rprint(table)
    