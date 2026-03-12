# langchain 
Build : LangChain gives developers a framework to construct LLM‑powered apps easily.

Observe : LangSmith gives visibility into what’s happening with your LLM-powered app, whether it's built with LangChain or not, so you know how to take action and improve quality. ( monitoring, )

Deploy : LangServe makes serving an API for your LangChain application turnkey.


Here’s a one-liner description for key **LangChain components**:

---

**1. LLMs:**
`LLMs` interface with large language models like OpenAI or HuggingFace to generate responses.

**2. PromptTemplates:**
`PromptTemplate` defines reusable templates for prompts with dynamic input variables.

**3. Chains:**
`Chains` link multiple components (like LLMs, prompts, tools) to perform complex tasks in sequence.

**4. Agents:**
`Agents` use LLMs to decide which tools to call and in what order, based on dynamic input.

**5. Tools:**
`Tools` are functions (like search, calculator, DB query) that agents can call to assist reasoning.

**6. Memory:**
`Memory` stores previous interactions in a conversation to provide context and continuity.

**7. Document Loaders:**
`Document Loaders` extract text and metadata from various data sources (PDFs, websites, etc).

**8. Text Splitters:**
`TextSplitters` break long documents into smaller, manageable chunks for better processing.

**9. VectorStores:**
`VectorStores` store text embeddings to enable similarity search for retrieval-augmented generation.

**10. Retrievers:**
`Retrievers` fetch relevant documents from a `VectorStore` based on user queries.

---

Let me know if you want a diagram or markdown table version too.


