import sys
from parsing import parse
from eval import evaluate


def ep(input, debug=True):
    ast = parse(input)
    if debug:
        print ast
    val = evaluate(ast)
    if val is not None and debug:
        print(_to_scheme_str(val))


def repl(prompt='pypyscheme> '):
    """A prompt-read-eval-print loop."""
    while True:
        try:
            input = raw_input(prompt)
            ep(input)
        except Exception, e:
            print e


def _to_scheme_str(exp):
    """Convert a Python object back into a Scheme-readable string."""
    if isinstance(exp, list):
        return '(' + ' '.join(map(_to_scheme_str, exp)) + ')'
    else:
        return str(exp)


def test():
    ep('(begin (define fact (lambda (n) (if (<= n 1) 1 (* n (fact (- n 1)))))) (fact 120)))', debug=False)


if __name__ == '__main__':
    input_program = sys.argv[1] if len(sys.argv) >= 2 else ''
    repl() if not input_program else ep(test)

