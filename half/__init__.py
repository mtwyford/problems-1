import check50
import check50.c
import re

@check50.check()
def exists():
    """half.c exists"""
    check50.exists("half.c")

@check50.check(exists)
def compiles():
    """half.c compiles"""
    # Check if student code compiles
    check50.c.compile("half.c", lcs50=True)
    
@check50.check(compiles)
def encrypts_a_as_b():
    """Prints correct with 12.50 bill, 8.875\% tax, 20\% tip"""
    check50.run("./half").stdin(12.50, 8.875, 20).stdout("You will owe $\i*8.17 each!, "You will owe $8.17 each!\n").exit(0)

