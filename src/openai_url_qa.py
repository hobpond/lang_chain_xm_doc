from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma

from utils import Utils

import os

load_dotenv()
api_key = os.getenv("openai.api_key")
MODEL = "gpt-3.5-turbo-0613"

urls = [
    "https://help.xmatters.com/ondemand/userguide/roles/user.htm",
    "https://help.xmatters.com/ondemand/mobile/get-the-mobile-app.htm",
    "https://help.xmatters.com/ondemand/what-is-xmatters.htm",
    "https://help.xmatters.com/ondemand/userguide/commontasks/signing_in.htm",
    "https://help.xmatters.com/ondemand/userguide/commontasks/xmod_dashboards.htm",
    "https://help.xmatters.com/ondemand/user/devices.htm",
    "https://help.xmatters.com/ondemand/mobile/get-the-mobile-app.htm",
    "https://help.xmatters.com/ondemand/userguide/receivingalerts/alertsintro.htm",
    "https://help.xmatters.com/ondemand/user/details.htm",
    "https://help.xmatters.com/ondemand/user/schedule.htm",
    "https://help.xmatters.com/ondemand/user/temporary-replacements.htm",
    "https://help.xmatters.com/ondemand/user/subscriptions.htm",
    "https://help.xmatters.com/ondemand/user/apikeys.htm",
    "https://help.xmatters.com/ondemand/user/roles.htm",
    "https://help.xmatters.com/ondemand/userguide/roles/message-sender.htm",
    "https://help.xmatters.com/ondemand/workflows/send-message-using-form.htm",
    "https://help.xmatters.com/ondemand/workflows/schedule_message.htm",
    "https://help.xmatters.com/ondemand/userguide/conferencebridging/start-manage-conf-bridge.htm",
    "https://help.xmatters.com/ondemand/installadmin/reporting/alerts-report.htm",
    "https://help.xmatters.com/ondemand/userguide/roles/supervisor.htm",
    "https://help.xmatters.com/ondemand/services/services.htm",
    "https://help.xmatters.com/ondemand/userguide/users/userspage.htm",
    "https://help.xmatters.com/ondemand/userguide/roles/supervisor.htm",
    "https://help.xmatters.com/ondemand/groups/manage_dynamic_teams.htm",
    "https://help.xmatters.com/ondemand/groups/dynamic-team-details.htm",
    "https://help.xmatters.com/ondemand/userguide/receivingalerts/subscriptions/sharingsubscriptions.htm",
    "https://help.xmatters.com/ondemand/userguide/performance/recipientperformance.htm",
    "https://help.xmatters.com/ondemand/incidentmgmt/incident-management.htm",
    "https://help.xmatters.com/ondemand/incidentmgmt/incidents-list.htm",
    "https://help.xmatters.com/ondemand/incidentmgmt/initiate-incident.htm",
    "https://help.xmatters.com/ondemand/incidentmgmt/incident-mgmt-console.htm",
    "https://help.xmatters.com/ondemand/incidentmgmt/incident-mgmt-mobile.htm",
    "https://help.xmatters.com/ondemand/userguide/roles/developer.htm",
    "https://help.xmatters.com/ondemand/workflows/manage-workflows.htm",
    "https://help.xmatters.com/ondemand/workflows/formcreatingmanagingnew.htm",
    "https://help.xmatters.com/ondemand/workflows/scenariosconfiguring.htm",
    "https://help.xmatters.com/ondemand/workflows/subscriptionforms.htm",
    "https://help.xmatters.com/ondemand/workflows/designexamples.htm",
    "https://help.xmatters.com/ondemand/installadmin/systemadministration/intelligent-event-management.htm",
    "https://help.xmatters.com/ondemand/userguide/roles/how-to-integrate.htm",
    "https://help.xmatters.com/ondemand/agent/theagents.htm",
    "https://help.xmatters.com/ondemand/flowdesigner/flow-designer.htm",
    "https://help.xmatters.com/ondemand/workflows/manage-workflows.htm",
    "https://help.xmatters.com/ondemand/incidentmgmt/incidents-list.htm",
    "https://help.xmatters.com/ondemand/workflows/scenariosconfiguring.htm",
    "https://help.xmatters.com/ondemand/workflows/subscriptionforms.htm",
    "https://help.xmatters.com/ondemand/workflows/designexamples.htm",
    "https://help.xmatters.com/ondemand/installadmin/systemadministration/intelligent-event-management.htm",
    "https://help.xmatters.com/ondemand/userguide/roles/how-to-integrate.htm",
    "https://help.xmatters.com/ondemand/agent/theagents.htm",
    "https://help.xmatters.com/ondemand/flowdesigner/flow-designer.htm",
    "https://help.xmatters.com/ondemand/flowdesigner/create-flow.htm",
    "https://help.xmatters.com/ondemand/flowdesigner/flow-app-triggers.htm",
    "https://help.xmatters.com/ondemand/flowdesigner/builtinapps.htm",
    "https://help.xmatters.com/ondemand/flowdesigner/create-custom-step.htm",
    "https://help.xmatters.com/ondemand/flowdesigner/manage-custom-steps.htm",
    "https://help.xmatters.com/ondemand/flowdesigner/inject-data.htm",
    "https://help.xmatters.com/ondemand/userguide/roles/administrator.htm",
    "https://help.xmatters.com/ondemand/installadmin/configure-company.htm",
    "https://help.xmatters.com/ondemand/installadmin/systemadministration/device_management.htm",
    "https://help.xmatters.com/ondemand/installadmin/systemadministration/roles.htm",
    "https://help.xmatters.com/ondemand/userguide/users/import-users.htm",
    "https://help.xmatters.com/ondemand/installadmin/systemadministration/useruploadintro.htm",
    "https://help.xmatters.com/ondemand/installadmin/reporting/notificationsreport.htm",
    "https://help.xmatters.com/ondemand/installadmin/reporting/conferences-report.htm",
    "https://help.xmatters.com/ondemand/installadmin/reporting/signals_report.htm",
    "https://help.xmatters.com/ondemand/installadmin/reporting/syncreport.htm",
    "https://help.xmatters.com/ondemand/userguide/users/managing_web_service_users.htm"
]
loader = UnstructuredURLLoader(urls=urls)
documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
texts = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings(model=MODEL, openai_api_key=api_key)
db = Chroma.from_documents(texts, embeddings)

retriever = db.as_retriever()

llm = ChatOpenAI(model = MODEL, temperature = 0.0, openai_api_key=api_key, max_tokens=1000)

prompt_template = '''
Your name is Don Clark. You are an expert at using xMatters and is extremely helpful.
Use the following pieces of context to answer the users question. 
If you don't know the answer, just say that you don't know, don't try to make up an answer.
Always answer from the perspective of being Don Clark.
----------------
{context}

Question: {question}
'''

prompt = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"]
)
chain_type_kwargs = {"prompt": prompt}

qa_chain = RetrievalQA.from_chain_type(llm=llm,
                                  chain_type = "stuff",
                                  retriever = retriever, 
                                  return_source_documents = True,
                                  chain_type_kwargs = chain_type_kwargs)

while True:
    query = input("Question: ")
    Utils.process_llm_response(Utils.count_tokens(qa_chain, query))
