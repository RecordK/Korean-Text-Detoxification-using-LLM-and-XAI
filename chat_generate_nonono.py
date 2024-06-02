from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain.schema import HumanMessage, SystemMessage
from langchain.prompts import (ChatPromptTemplate,FewShotChatMessagePromptTemplate)
from dotenv import load_dotenv
load_dotenv()

class ChatGenerator:
    def __init__(self) -> None:
        self.chat = ChatOpenAI(temperature=0, model_name = 'gpt-4-1106-preview')
    
        self.final_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", "너는 문장 스타일 변환을 하는 역할을 할거야. 기존 댓글의 문맥은 유지하면서 순화 댓글을 생성하는 것이 너의 임무야."),
                ("human", "원문 :{sentence}"),
            ]
        )
        
        self.chain = self.final_prompt | self.chat
    
    def covert_sentence(self,ori_setence):
        return self.chain.invoke({"sentence" : {ori_setence}})
