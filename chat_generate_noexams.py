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
                ("system", "너는 문장을 순화하는 역할을 할거야. 원문과 함께 해당 문장이 유해한 문장으로 판단되는데 중요한 영향을 미친(=feature importance가 높은) 단어를 [mask] 처리한 마스킹 문장이 주어지면, 두 문장을 바탕으로 원문의 의미는 유지하면서 순화 댓글을 생성하는 것이 너의 임무야."),
                ("human", "원문 :{sentence}\n 마스킹 문장 : {masking_sentence}"),
            ]
        )
        
        self.chain = self.final_prompt | self.chat
    def covert_sentence(self,ori_setence,mask_sentence):
        return self.chain.invoke({"sentence" : {ori_setence},
                                  "masking_sentence" : {mask_sentence}})
