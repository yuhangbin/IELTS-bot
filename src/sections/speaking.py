from ..common.chains import IELTSChain

def practice():
    print("This is the Speaking practice section.")
    chain = IELTSChain().speaking_chain()
    context = ""
    while True:
        question = input("Enter your speaking topic: ")
        context += f"\nQuestion: {question}\n"
        response = IELTSChain().run_chain(chain, context)
        print(response)
        user_answer = input("Enter your answer: ")
        context += f"Answer: {user_answer}\n"
        feedback = IELTSChain().run_chain(chain, context)
        print(feedback)