# This entrypoint file to be used in development. Start by reading README.md
from arithmetic_arranger import arithmetic_arranger
from unittest import main


#print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

#print(arithmetic_arranger(["3213 + 698", "1234 + 356"], True))
# Run unit tests automatically
main(module='test_module', exit=False)