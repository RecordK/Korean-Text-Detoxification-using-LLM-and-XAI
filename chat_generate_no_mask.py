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
        self.chat = ChatOpenAI(temperature=0,model_name = 'gpt-4-1106-preview')
        self.example =  [
            {
            "sentence" : "쪽바리앞잡이야 너거나라가라 꺼져.",
            "answer":
            '''
            일본앞잡이야 너희들나라로 가라
            '''
            },
            {
            "sentence" : "미친 씨발 개슬람년아 그럼 한국에 오질 말든가",
            "answer":
            '''
            이슬람 여성들아 그럼 한국에 오질 말든가.
            '''
            },           
            {"sentence" : "음주운전하는 새끼들은 진짜 대가리에 뭐가 든건지... 다 무기징역 시켜라",
            "answer":
            '''
            음주운전하는 사람들은 진짜 머리에 뭐가 든건지... 다 무기징역 시켜라
            '''
            },
            {
            "sentence" : "좌빨 영화 납시요 개돼지들 선동시키기 딱이요",
            "answer":
            '''
            좌파 영화 납시요. 사람들 부추기기 딱이요
            '''
            }
        ]
        
        self.example_prompt = ChatPromptTemplate.from_messages(
                        [
                ("human", "원문 :{sentence}"),
                ("ai", "순화 문장 : {answer}"),
            ]
        )
        self.few_shot_prompt =  FewShotChatMessagePromptTemplate(
            example_prompt=self.example_prompt,
            examples=self.example,
        )
        
        self.final_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", "너는 문장 스타일 변환을 하는 역할을 할거야. 예시를 참고해서, 원문의 의미는 유지하면서 순화댓글을 생성하는 것이 너의 임무야."),
                self.few_shot_prompt,
                ("human", "원문 :{sentence}"),
            ]
        )
        
        self.chain = self.final_prompt | self.chat
    
    def covert_sentence(self,ori_setence):
        return self.chain.invoke({"sentence" : {ori_setence}})
