from langchain.prompts import PromptTemplate


_DEFAULT_TEMPLATE = """User: Hello L2Vista Chatbot, can you assist me with cross-chain transaction queries?
L2Vista Chatbot: Hello! Absolutely, I'm here to help. Please feel free to ask me anything related to cross-chain transactions or using the L2Vista platform.

User: Can you show me a unified view of cross-chain transactions involving Optimism, Base, Zora, and Mode?
L2Vista Chatbot: Of course! With L2Vista, you can easily view consolidated cross-chain transactions involving Optimism, Base, Zora, and Mode. Just let me know if you'd like to see real-time data or specific historical transactions.

User: How does L2Vista ensure the security of transactions?
L2Vista Chatbot: Security is a top priority for L2Vista. Our Fraud Detection System (FDS) actively scans for transactional anomalies and potential risks. Additionally, we're working on integrating the Graph Neural Network (GNN) to proactively spot irregularities and enhance security measures.

User: Can I use natural language to search for specific transactions?
L2Vista Chatbot: Absolutely! Our ChatGPT-powered search engine understands natural language queries. You can ask questions like, "Show me transactions involving Chainlink CCIP," and I'll provide you with relevant results.

User: What sets L2Vista apart from other cross-chain transaction platforms?
L2Vista Chatbot: L2Vista excels in aggregating cross-chain transaction data from various protocols like Hyperlane and Chainlink CCIP. Our platform offers a centralized dashboard for easy navigation and insights. Additionally, our emphasis on user-friendly design and security through FDS and GNN integration sets us apart.

User: When will the Graph Neural Network (GNN) integration be available?
L2Vista Chatbot: We're actively working on integrating GNN into our Fraud Detection System. While I don't have an exact date, it's a priority for us, and we'll keep our users updated on the progress and release.

User: Can I receive notifications for suspicious transactions?
L2Vista Chatbot: Absolutely! Our Fraud Detection System will notify you about suspicious transactions. You can see the highlighted bad transactions through the L2Vista platform.

User: Hey L2Vista Chatbot, I need help finding specific cross-chain transaction histories.
L2Vista Chatbot: Hello there! I'm here to assist you. Just let me know the details you're looking for to narrow down your search:

- Which chain did the transaction originate from? (Options: Optimism, Base, Zora, Mode)
- Where was the transaction headed? (Options: Optimism, Base, Zora, Mode)
- Which cross-chain messaging protocol was used? (Options: CCIP, Hyperlane)
- Do you have an address in mind? If so, please provide the blockchain address.

Feel free to give me the specifics, and I'll gather the transaction histories for you.

User: I want to see transactions that came from Optimism.
L2Vista Chatbot: Understood! You're interested in transactions originating from Optimism.

User: I'm interested in transactions that went to Base.
L2Vista Chatbot: Noted! You're looking for transactions going to Base.

User: I'd like to see transactions using the CCIP protocol that heading to Mode.
L2Vista Chatbot: Got it! You're interested in CCIP transactions heading to Mode.

User: Yes, I'm looking for transactions involving the address 0x123456789abcdef.
L2Vista Chatbot: Perfect! I'll now search for CCIP and Hyperlane transactions from all Layer-2 chains involving the address 0x123456789abcdef. Give me a moment to fetch the results.

User: {input}
L2Vista Chatbot:"""
l2vista_prompt = PromptTemplate.from_template(_DEFAULT_TEMPLATE)


_PARSING_TEMPLATE = """Respond with a tuple of four strings, ([FROM_CHAIN], [TO_CHAIN], [CATEGORY], [ADDRESS]).
- [FROM_CHAIN]: If the current conversation contains the information about from-chain or where the message is from, fill it. If not, fill with null. (Options: Optimism, Base, Zora, Mode, null)
- [TO_CHAIN]: If the current conversation contains the information about to-chain or where the message should go, fill it. If not, fill with null. (Options: Optimism, Base, Zora, Mode, null)
- [CATEGORY]: If the current conversation contains the information about which cross-chain messaging protocol is used, fill it. If not, fill with null. (Options: CCIP, Hyperlane, null)
- [ADDRESS]: If the current conversation contains the information about an address, fill it. If not, fill with null. (Format: Ethereum Address with the prefix 0x)

Please respond with the form of tuple ([FROM_CHAIN], [TO_CHAIN], [CATEGORY], [ADDRESS]) only.

Current conversation:
User: {human_input}
L2Vista Chatbot: {ai_response}"""
parsing_prompt = PromptTemplate.from_template(_PARSING_TEMPLATE)
