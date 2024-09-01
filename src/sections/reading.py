from ..common.chains import IELTSChain

def practice():
    print("This is the Reading practice section.")
    chain = IELTSChain().reading_chain()
    question = input("Enter your reading question: ")
    response = IELTSChain().run_chain(chain, question)
    print(response)