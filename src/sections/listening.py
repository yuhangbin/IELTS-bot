from ..common.chains import IELTSChain

def practice():
    print("This is the Listening practice section.")
    chain = IELTSChain().listening_chain()
    question = input("Enter your listening question: ")
    response = IELTSChain().run_chain(chain, question)
    print(response)