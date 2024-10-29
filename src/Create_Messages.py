from langchain.schema import SystemMessage,HumanMessage,AIMessage 


def CreateSystemMessage(text:str):
    Message = SystemMessage(content = text)
    return Message

def CreateAIMessage(text:str):
    Message = AIMessage(content = text)
    return Message

def CreateHumanMessage(text:str):
    Message = HumanMessage(content = text)
    return Message
    
    