from ..common.chains import IELTSChain

def practice():
    print("This is the Writing practice section.")
    chain = IELTSChain().writing_chain()
    question = input("Enter your writing prompt: ")
    response = IELTSChain().run_chain(chain, question)
    print(response)