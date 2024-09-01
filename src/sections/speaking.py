from ..common.chains import IELTSChain

def practice():
    print("This is the Speaking practice section.")
    chain = IELTSChain().speaking_chain()
    question = input("Enter your speaking topic: ")
    response = IELTSChain().run_chain(chain, question)
    print(response)