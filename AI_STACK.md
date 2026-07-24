# AI Stack Report

_Generated: 2026-07-24T11:28:58.739291Z_  
_Scanner mode: hybrid_  
_Scanned 1264 Python file(s), found 180 distinct component(s)._

## LLM Providers

| Component | Confidence | Deployment | Occurrences | Example location |
|---|---|---|---|---|
| OpenAI GPT-4 family (string literal) | low | Cloud | 438 | `lib/cli/src/crewai_cli/constants.py:354` |
| Anthropic Claude family (string literal) | low | Cloud | 32 | `lib/cli/tests/test_model_catalog.py:43` |
| OpenAI | high | Cloud | 21 | `lib/crewai-files/src/crewai_files/uploaders/openai.py:168` |
| Google Gemini family (string literal) | low | Cloud | 20 | `lib/crewai-files/tests/processing/test_constraints.py:232` |
| LiteLLM (multi-provider proxy) | high | Cloud | 17 | `lib/crewai/pyproject.toml:90` |
| OpenAI GPT-3.5 family (string literal) | low | Cloud | 16 | `lib/crewai/tests/agents/test_agent.py:1354` |
| Google Gemini / Vertex AI | high | Cloud | 12 | `lib/crewai-files/src/crewai_files/uploaders/gemini.py:120` |
| Generic LLM client (verify provider) | medium | Cloud | 11 | `lib/cli/src/crewai_cli/plus_api.py:47` |
| Meta Llama family (string literal) | low | Cloud | 10 | `lib/cli/tests/test_model_catalog.py:90` |
| OpenAI o-series (string literal) | low | Cloud | 9 | `lib/cli/tests/test_model_catalog.py:88` |
| Anthropic | high | Cloud | 8 | `lib/crewai-files/src/crewai_files/uploaders/anthropic.py:52` |
| OpenAI client | high | Cloud + Unknown (verify manually) | 8 | `lib/crewai-files/src/crewai_files/uploaders/openai.py:170` |
| Google GenAI client | high | Cloud | 5 | `lib/crewai-files/src/crewai_files/uploaders/gemini.py:122` |
| Anthropic client | high | Cloud | 2 | `lib/crewai-files/src/crewai_files/uploaders/anthropic.py:54` |
| Anthropic client (async) | high | Cloud | 2 | `lib/crewai-files/src/crewai_files/uploaders/anthropic.py:68` |
| Google Vertex AI | high | Cloud | 2 | `lib/crewai/src/crewai/rag/embeddings/providers/google/genai_vertex_embedding.py:123` |
| OpenAI client (async) | high | Cloud | 2 | `lib/crewai-files/src/crewai_files/uploaders/openai.py:184` |
| Anthropic (env var configured) | low | Cloud | 1 | `lib/crewai-tools/src/crewai_tools/tools/stagehand_tool/.env.example:1` |
| Azure OpenAI client | high | Cloud | 1 | `lib/crewai-tools/src/crewai_tools/tools/mongodb_vector_search_tool/vector_search.py:125` |
| Hugging Face Transformers | medium | Cloud | 1 | `pyproject.toml:214` |
| OpenAI (env var configured) | low | Cloud | 1 | `lib/crewai-tools/src/crewai_tools/tools/stagehand_tool/.env.example:2` |

## MCP (Model Context Protocol)

| Component | Confidence | Occurrences | Example location |
|---|---|---|---|
| Model Context Protocol SDK | high | 19 | `lib/crewai-tools/pyproject.toml:102` |
| MCP client session | high | 4 | `lib/crewai-tools/src/crewai_tools/tools/brightdata_tool/brightdata_dataset.py:498` |

## Tools / Function Calling

| Component | Confidence | Occurrences | Example location |
|---|---|---|---|
| Tool definition (@tool) | high | 70 | `lib/crewai-tools/tests/base_tool_test.py:9` |
| Custom Tool (subclasses BaseTool): MyCustomTool | high | 9 | `lib/cli/src/crewai_cli/templates/crew/tools/custom_tool.py:10` |
| Custom Tool (subclasses BaseTool): TestTool | high | 9 | `lib/crewai/tests/test_crew.py:576` |
| Custom Tool (subclasses BaseTool): TypedSearchTool | high | 5 | `lib/crewai/tests/agents/test_native_tool_calling.py:1206` |
| Custom Tool (subclasses BaseTool): CalculatorTool | high | 3 | `lib/crewai/tests/agents/test_lite_agent.py:45` |
| Custom Tool (subclasses BaseTool): CodeTool | high | 3 | `lib/crewai/tests/agents/test_native_tool_calling.py:1149` |
| Custom Tool (subclasses BaseTool): FailingTool | high | 3 | `lib/crewai/tests/agents/test_native_tool_calling.py:69` |
| Custom Tool (subclasses BaseTool): LimitedTool | high | 3 | `lib/crewai/tests/tools/test_tool_usage_limit.py:10` |
| Custom Tool (subclasses BaseTool): AnotherTestTool | high | 2 | `lib/crewai/tests/test_crew.py:694` |
| Custom Tool (subclasses BaseTool): AsyncTool | high | 2 | `lib/crewai/tests/tools/test_async_tools.py:21` |
| Custom Tool (subclasses BaseTool): MarkdownSearchTool | high | 2 | `lib/crewai/tests/tools/test_base_tool.py:602` |
| Custom Tool (subclasses BaseTool): MockTool | high | 2 | `lib/crewai-tools/tests/test_generate_tool_specs.py:30` |
| Custom Tool (subclasses BaseTool): SearchTool | high | 2 | `lib/crewai/tests/agents/test_native_tool_calling.py:1274` |
| Custom Tool (subclasses BaseTool): SlowAsyncTool | high | 2 | `lib/crewai/tests/tools/test_async_tools.py:152` |
| Custom Tool (subclasses BaseTool): SyncTool | high | 2 | `lib/crewai/tests/tools/test_async_tools.py:10` |
| Custom Tool (subclasses BaseTool): AIMindTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/ai_mind_tool/ai_mind_tool.py:23` |
| Custom Tool (subclasses BaseTool): AddImageTool | high | 1 | `lib/crewai/src/crewai/tools/agent_tools/add_image_tool.py:16` |
| Custom Tool (subclasses BaseTool): ApifyActorsTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/apify_actors_tool/apify_actors_tool.py:14` |
| Custom Tool (subclasses BaseTool): ArxivPaperTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/arxiv_paper_tool/arxiv_paper_tool.py:27` |
| Custom Tool (subclasses BaseTool): AsyncCodeExecutorTool | high | 1 | `lib/crewai/tests/tools/test_base_tool.py:626` |
| Custom Tool (subclasses BaseTool): AsyncResultTool | high | 1 | `lib/crewai/tests/test_flow_from_definition.py:108` |
| Custom Tool (subclasses BaseTool): BaseAgentTool | high | 1 | `lib/crewai/src/crewai/tools/agent_tools/base_agent_tools.py:15` |
| Custom Tool (subclasses BaseTool): BedrockInvokeAgentTool | high | 1 | `lib/crewai-tools/src/crewai_tools/aws/bedrock/agents/invoke_agent_tool.py:26` |
| Custom Tool (subclasses BaseTool): BedrockKBRetrieverTool | high | 1 | `lib/crewai-tools/src/crewai_tools/aws/bedrock/knowledge_base/retriever_tool.py:26` |
| Custom Tool (subclasses BaseTool): BlockedTool | high | 1 | `lib/crewai/tests/utilities/test_agent_utils.py:1224` |
| Custom Tool (subclasses BaseTool): BraveSearchTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/brave_search_tool/brave_search_tool.py:28` |
| Custom Tool (subclasses BaseTool): BraveSearchToolBase | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/brave_search_tool/base.py:82` |
| Custom Tool (subclasses BaseTool): BrightDataDatasetTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/brightdata_tool/brightdata_dataset.py:402` |
| Custom Tool (subclasses BaseTool): BrightDataSearchTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/brightdata_tool/brightdata_serp.py:64` |
| Custom Tool (subclasses BaseTool): BrightDataWebUnlockerTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/brightdata_tool/brightdata_unlocker.py:46` |
| Custom Tool (subclasses BaseTool): BrowserBaseTool | high | 1 | `lib/crewai-tools/src/crewai_tools/aws/bedrock/browser/browser_toolkit.py:82` |
| Custom Tool (subclasses BaseTool): BrowserbaseLoadTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/browserbase_load_tool/browserbase_load_tool.py:12` |
| Custom Tool (subclasses BaseTool): CodeExecutorTool | high | 1 | `lib/crewai/tests/tools/test_base_tool.py:253` |
| Custom Tool (subclasses BaseTool): ComposioTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/composio_tool/composio_tool.py:10` |
| Custom Tool (subclasses BaseTool): ContextualAICreateAgentTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/contextualai_create_agent_tool/contextual_create_agent_tool.py:18` |
| Custom Tool (subclasses BaseTool): ContextualAIParseTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/contextualai_parse_tool/contextual_parse_tool.py:26` |
| Custom Tool (subclasses BaseTool): ContextualAIQueryTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/contextualai_query_tool/contextual_query_tool.py:19` |
| Custom Tool (subclasses BaseTool): ContextualAIRerankTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/contextualai_rerank_tool/contextual_rerank_tool.py:21` |
| Custom Tool (subclasses BaseTool): CouchbaseFTSVectorSearchTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/couchbase_tool/couchbase_tool.py:37` |
| Custom Tool (subclasses BaseTool): CountingTool | high | 1 | `lib/crewai/tests/agents/test_native_tool_calling.py:1008` |
| Custom Tool (subclasses BaseTool): CrewAIMCPTool | high | 1 | `lib/crewai-tools/src/crewai_tools/adapters/mcp_adapter.py:56` |
| Custom Tool (subclasses BaseTool): CrewAIPlatformActionTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/crewai_platform_tools/crewai_platform_action_tool.py:18` |
| Custom Tool (subclasses BaseTool): CustomTool | high | 1 | `lib/crewai/tests/tools/test_structured_tool.py:317` |
| Custom Tool (subclasses BaseTool): DallETool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/dalle_tool/dalle_tool.py:17` |
| Custom Tool (subclasses BaseTool): DatabricksQueryTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/databricks_query_tool/databricks_query_tool.py:73` |
| Custom Tool (subclasses BaseTool): DaytonaBaseTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/daytona_sandbox_tool/daytona_base_tool.py:16` |
| Custom Tool (subclasses BaseTool): DeleteFilesTool | high | 1 | `lib/crewai-tools/src/crewai_tools/aws/bedrock/code_interpreter/code_interpreter_toolkit.py:285` |
| Custom Tool (subclasses BaseTool): DictAnnotatedSearchTool | high | 1 | `lib/crewai/tests/tools/test_base_tool.py:401` |
| Custom Tool (subclasses BaseTool): DirectoryReadTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/directory_read_tool/directory_read_tool.py:20` |
| Custom Tool (subclasses BaseTool): E2BBaseTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/e2b_sandbox_tool/e2b_base_tool.py:16` |
| Custom Tool (subclasses BaseTool): EnterpriseActionTool | high | 1 | `lib/crewai-tools/src/crewai_tools/adapters/enterprise_adapter.py:21` |
| Custom Tool (subclasses BaseTool): ErrorTool | high | 1 | `lib/crewai/tests/utilities/test_events.py:433` |
| Custom Tool (subclasses BaseTool): ExaSearchTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/exa_tools/exa_search_tool.py:44` |
| Custom Tool (subclasses BaseTool): ExecuteCodeTool | high | 1 | `lib/crewai-tools/src/crewai_tools/aws/bedrock/code_interpreter/code_interpreter_toolkit.py:138` |
| Custom Tool (subclasses BaseTool): ExecuteCommandTool | high | 1 | `lib/crewai-tools/src/crewai_tools/aws/bedrock/code_interpreter/code_interpreter_toolkit.py:191` |
| Custom Tool (subclasses BaseTool): ExplicitSearchTool | high | 1 | `lib/crewai/tests/tools/test_base_tool.py:376` |
| Custom Tool (subclasses BaseTool): FileCompressorTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/files_compressor_tool/files_compressor_tool.py:30` |
| Custom Tool (subclasses BaseTool): FileReadTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/file_read_tool/file_read_tool.py:25` |
| Custom Tool (subclasses BaseTool): FileWriterTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/file_writer_tool/file_writer_tool.py:32` |
| Custom Tool (subclasses BaseTool): FirecrawlCrawlWebsiteTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/firecrawl_crawl_website_tool/firecrawl_crawl_website_tool.py:23` |
| Custom Tool (subclasses BaseTool): FirecrawlScrapeWebsiteTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/firecrawl_scrape_website_tool/firecrawl_scrape_website_tool.py:23` |
| Custom Tool (subclasses BaseTool): FirecrawlSearchTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/firecrawl_search_tool/firecrawl_search_tool.py:21` |
| Custom Tool (subclasses BaseTool): GenerateCrewaiAutomationTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/generate_crewai_automation_tool/generate_crewai_automation_tool.py:19` |
| Custom Tool (subclasses BaseTool): GetTaskTool | high | 1 | `lib/crewai-tools/src/crewai_tools/aws/bedrock/code_interpreter/code_interpreter_toolkit.py:380` |
| Custom Tool (subclasses BaseTool): HyperbrowserLoadTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/hyperbrowser_load_tool/hyperbrowser_load_tool.py:20` |
| Custom Tool (subclasses BaseTool): InferredSearchTool | high | 1 | `lib/crewai/tests/tools/test_base_tool.py:385` |
| Custom Tool (subclasses BaseTool): InvokeCrewAIAutomationTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/invoke_crewai_automation_tool/invoke_crewai_automation_tool.py:15` |
| Custom Tool (subclasses BaseTool): IteratingTool | high | 1 | `lib/crewai/tests/tools/test_base_tool.py:212` |
| Custom Tool (subclasses BaseTool): JinaScrapeWebsiteTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/jina_scrape_website_tool/jina_scrape_website_tool.py:16` |
| Custom Tool (subclasses BaseTool): LinkupSearchTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/linkup/linkup_search_tool.py:18` |
| Custom Tool (subclasses BaseTool): ListFilesTool | high | 1 | `lib/crewai-tools/src/crewai_tools/aws/bedrock/code_interpreter/code_interpreter_toolkit.py:253` |
| Custom Tool (subclasses BaseTool): LiveLookupTool | high | 1 | `lib/crewai/tests/test_tool_cache_default.py:33` |
| Custom Tool (subclasses BaseTool): LlamaIndexTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/llamaindex_tool/llamaindex_tool.py:9` |
| Custom Tool (subclasses BaseTool): MCPNativeTool | high | 1 | `lib/crewai/src/crewai/tools/mcp_native_tool.py:16` |
| Custom Tool (subclasses BaseTool): MCPStyleTool | high | 1 | `lib/crewai/tests/utilities/test_agent_utils.py:245` |
| Custom Tool (subclasses BaseTool): MCPToolWrapper | high | 1 | `lib/crewai/src/crewai/tools/mcp_tool_wrapper.py:16` |
| Custom Tool (subclasses BaseTool): MergeAgentHandlerTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/merge_agent_handler_tool/merge_agent_handler_tool.py:21` |
| Custom Tool (subclasses BaseTool): MinimalTool | high | 1 | `lib/crewai/tests/utilities/test_agent_utils.py:158` |
| Custom Tool (subclasses BaseTool): MockIntermediateBase | high | 1 | `lib/crewai-tools/tests/test_generate_tool_specs.py:62` |
| Custom Tool (subclasses BaseTool): MockMCPTool | high | 1 | `lib/crewai/tests/agents/test_lite_agent.py:670` |
| Custom Tool (subclasses BaseTool): MongoDBVectorSearchTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/mongodb_vector_search_tool/vector_search.py:57` |
| Custom Tool (subclasses BaseTool): MultiOnTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/multion_tool/multion_tool.py:11` |
| Custom Tool (subclasses BaseTool): MyCacheTool | high | 1 | `lib/crewai/tests/tools/test_structured_tool.py:65` |
| Custom Tool (subclasses BaseTool): NL2SQLTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/nl2sql/nl2sql_tool.py:211` |
| Custom Tool (subclasses BaseTool): NoSchemaTool | high | 1 | `lib/crewai/tests/utilities/test_agent_utils.py:75` |
| Custom Tool (subclasses BaseTool): OCRTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/ocr_tool/ocr_tool.py:29` |
| Custom Tool (subclasses BaseTool): OxylabsAmazonProductScraperTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/oxylabs_amazon_product_scraper_tool/oxylabs_amazon_product_scraper_tool.py:54` |
| Custom Tool (subclasses BaseTool): OxylabsAmazonSearchScraperTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/oxylabs_amazon_search_scraper_tool/oxylabs_amazon_search_scraper_tool.py:56` |
| Custom Tool (subclasses BaseTool): OxylabsGoogleSearchScraperTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/oxylabs_google_search_scraper_tool/oxylabs_google_search_scraper_tool.py:59` |
| Custom Tool (subclasses BaseTool): OxylabsUniversalScraperTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/oxylabs_universal_scraper_tool/oxylabs_universal_scraper_tool.py:50` |
| Custom Tool (subclasses BaseTool): ParallelLocalSearchOne | high | 1 | `lib/crewai/tests/agents/test_native_tool_calling.py:166` |
| Custom Tool (subclasses BaseTool): ParallelLocalSearchThree | high | 1 | `lib/crewai/tests/agents/test_native_tool_calling.py:190` |
| Custom Tool (subclasses BaseTool): ParallelLocalSearchTwo | high | 1 | `lib/crewai/tests/agents/test_native_tool_calling.py:178` |
| Custom Tool (subclasses BaseTool): ParallelSearchTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/parallel_tools/parallel_search_tool.py:47` |
| Custom Tool (subclasses BaseTool): PatronusEvalTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/patronus_eval_tool/patronus_eval_tool.py:11` |
| Custom Tool (subclasses BaseTool): PatronusLocalEvaluatorTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/patronus_eval_tool/patronus_local_evaluator_tool.py:33` |
| Custom Tool (subclasses BaseTool): PatronusPredefinedCriteriaEvalTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/patronus_eval_tool/patronus_predefined_criteria_eval_tool.py:29` |
| Custom Tool (subclasses BaseTool): QdrantVectorSearchTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/qdrant_vector_search_tool/qdrant_search_tool.py:41` |
| Custom Tool (subclasses BaseTool): RagTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/rag/rag_tool.py:126` |
| Custom Tool (subclasses BaseTool): RandomNumberTool | high | 1 | `lib/crewai/tests/tools/test_tool_usage.py:43` |
| Custom Tool (subclasses BaseTool): ReadFileTool | high | 1 | `lib/crewai/src/crewai/tools/agent_tools/read_file_tool.py:24` |
| Custom Tool (subclasses BaseTool): ReadFilesTool | high | 1 | `lib/crewai-tools/src/crewai_tools/aws/bedrock/code_interpreter/code_interpreter_toolkit.py:222` |
| Custom Tool (subclasses BaseTool): RecallMemoryTool | high | 1 | `lib/crewai/src/crewai/tools/memory_tools.py:25` |
| Custom Tool (subclasses BaseTool): RememberTool | high | 1 | `lib/crewai/src/crewai/tools/memory_tools.py:75` |
| Custom Tool (subclasses BaseTool): RootSearchTool | high | 1 | `lib/crewai/tests/tools/test_base_tool.py:393` |
| Custom Tool (subclasses BaseTool): S3ReaderTool | high | 1 | `lib/crewai-tools/src/crewai_tools/aws/s3/reader_tool.py:15` |
| Custom Tool (subclasses BaseTool): S3WriterTool | high | 1 | `lib/crewai-tools/src/crewai_tools/aws/s3/writer_tool.py:16` |
| Custom Tool (subclasses BaseTool): SayHiTool | high | 1 | `lib/crewai/tests/utilities/test_events.py:372` |
| Custom Tool (subclasses BaseTool): ScrapeElementFromWebsiteTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/scrape_element_from_website/scrape_element_from_website.py:32` |
| Custom Tool (subclasses BaseTool): ScrapeWebsiteTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/scrape_website_tool/scrape_website_tool.py:30` |
| Custom Tool (subclasses BaseTool): ScrapegraphScrapeTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/scrapegraph_scrape_tool/scrapegraph_scrape_tool.py:47` |
| Custom Tool (subclasses BaseTool): ScrapflyScrapeWebsiteTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/scrapfly_scrape_website_tool/scrapfly_scrape_website_tool.py:27` |
| Custom Tool (subclasses BaseTool): SecretLookupTool | high | 1 | `lib/crewai/tests/agents/test_lite_agent.py:22` |
| Custom Tool (subclasses BaseTool): SeleniumScrapingTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/selenium_scraping_tool/selenium_scraping_tool.py:51` |
| Custom Tool (subclasses BaseTool): SerpApiBaseTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/serpapi_tool/serpapi_base_tool.py:9` |
| Custom Tool (subclasses BaseTool): SerperDevTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/serper_dev_tool/serper_dev_tool.py:110` |
| Custom Tool (subclasses BaseTool): SerperScrapeWebsiteTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/serper_scrape_website_tool/serper_scrape_website_tool.py:21` |
| Custom Tool (subclasses BaseTool): SerplyNewsSearchTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/serply_api_tool/serply_news_search_tool.py:18` |
| Custom Tool (subclasses BaseTool): SerplyScholarSearchTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/serply_api_tool/serply_scholar_search_tool.py:19` |
| Custom Tool (subclasses BaseTool): SerplyWebSearchTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/serply_api_tool/serply_web_search_tool.py:18` |
| Custom Tool (subclasses BaseTool): SimpleTool | high | 1 | `lib/crewai/tests/tools/test_base_tool.py:299` |
| Custom Tool (subclasses BaseTool): SingleStoreSearchTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/singlestore_search_tool/singlestore_search_tool.py:34` |
| Custom Tool (subclasses BaseTool): SnowflakeSearchTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/snowflake_search_tool/snowflake_search_tool.py:77` |
| Custom Tool (subclasses BaseTool): SpiderTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/spider_tool/spider_tool.py:41` |
| Custom Tool (subclasses BaseTool): StagehandTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/stagehand_tool/stagehand_tool.py:92` |
| Custom Tool (subclasses BaseTool): StartCommandTool | high | 1 | `lib/crewai-tools/src/crewai_tools/aws/bedrock/code_interpreter/code_interpreter_toolkit.py:349` |
| Custom Tool (subclasses BaseTool): StaticSearchTool | high | 1 | `lib/crewai/tests/test_flow_from_definition.py:87` |
| Custom Tool (subclasses BaseTool): StopTaskTool | high | 1 | `lib/crewai-tools/src/crewai_tools/aws/bedrock/code_interpreter/code_interpreter_toolkit.py:411` |
| Custom Tool (subclasses BaseTool): StrictTool | high | 1 | `lib/crewai/tests/agents/test_native_tool_calling.py:1344` |
| Custom Tool (subclasses BaseTool): SumNumbersTool | high | 1 | `lib/crewai/tests/llms/google/test_google.py:622` |
| Custom Tool (subclasses BaseTool): TavilyExtractorTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/tavily_extractor_tool/tavily_extractor_tool.py:28` |
| Custom Tool (subclasses BaseTool): TavilyGetResearchTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/tavily_get_research_tool/tavily_get_research_tool.py:30` |
| Custom Tool (subclasses BaseTool): TavilyResearchTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/tavily_research_tool/tavily_research_tool.py:50` |
| Custom Tool (subclasses BaseTool): TavilySearchTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/tavily_search_tool/tavily_search_tool.py:26` |
| Custom Tool (subclasses BaseTool): TempTool | high | 1 | `lib/crewai/tests/tools/test_base_tool.py:726` |
| Custom Tool (subclasses BaseTool): Tool | high | 1 | `lib/crewai/src/crewai/tools/base_tool.py:507` |
| Custom Tool (subclasses BaseTool): TypedInputsTool | high | 1 | `lib/crewai/tests/test_flow_from_definition.py:95` |
| Custom Tool (subclasses BaseTool): UnlimitedTool | high | 1 | `lib/crewai/tests/tools/test_tool_usage_limit.py:31` |
| Custom Tool (subclasses BaseTool): ValidTool | high | 1 | `lib/crewai/tests/tools/test_tool_usage_limit.py:74` |
| Custom Tool (subclasses BaseTool): VisionTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/vision_tool/vision_tool.py:37` |
| Custom Tool (subclasses BaseTool): WeatherTool | high | 1 | `lib/crewai/tests/agents/test_native_tool_calling.py:58` |
| Custom Tool (subclasses BaseTool): WeaviateVectorSearchTool | high | 1 | `lib/crewai-tools/src/crewai_tools/tools/weaviate_tool/vector_search.py:52` |
| Custom Tool (subclasses BaseTool): WebSearchTool | high | 1 | `lib/crewai/tests/agents/test_lite_agent.py:30` |
| Custom Tool (subclasses BaseTool): WriteFilesTool | high | 1 | `lib/crewai-tools/src/crewai_tools/aws/bedrock/code_interpreter/code_interpreter_toolkit.py:316` |
| Custom Tool (subclasses BaseTool): ZapierActionTool | high | 1 | `lib/crewai-tools/src/crewai_tools/adapters/zapier_adapter.py:17` |

## Agent & Orchestration Frameworks

| Component | Confidence | Occurrences | Example location |
|---|---|---|---|
| CrewAI | high | 3361 | `conftest.py:196` |
| Agent (verify framework) | medium | 628 | `lib/cli/src/crewai_cli/templates/flow/crews/content_crew/content_crew.py:18` |
| CrewAI Crew | high | 397 | `lib/cli/src/crewai_cli/templates/flow/crews/content_crew/content_crew.py:55` |
| LangChain | high | 4 | `lib/crewai-tools/pyproject.toml:93` |
| Instructor (structured outputs) | high | 3 | `lib/crewai/pyproject.toml:16` |
| LlamaIndex | high | 3 | `lib/crewai-tools/src/crewai_tools/tools/llamaindex_tool/llamaindex_tool.py:29` |
| LangChain AgentExecutor | high | 1 | `lib/crewai/src/crewai/agent/core.py:1457` |

## Vector Stores / Memory

| Component | Confidence | Occurrences | Example location |
|---|---|---|---|
| Chroma | high | 47 | `lib/crewai-tools/src/crewai_tools/rag/core.py:7` |
| Qdrant | high | 12 | `lib/crewai-tools/pyproject.toml:89` |
| Weaviate | high | 7 | `lib/crewai-tools/pyproject.toml:47` |
| LanceDB | high | 3 | `lib/crewai-tools/src/crewai_tools/adapters/lancedb_adapter.py:7` |
| Chroma client | medium | 1 | `lib/crewai-tools/src/crewai_tools/rag/core.py:59` |

<details><summary>Skipped files (parse errors)</summary>

- `lib/cli/src/crewai_cli/templates/crew/crew.py`
- `lib/cli/src/crewai_cli/templates/crew/main.py`
- `lib/cli/src/crewai_cli/templates/flow/main.py`
- `lib/cli/src/crewai_cli/templates/tool/src/{{folder_name}}/__init__.py`
- `lib/cli/src/crewai_cli/templates/tool/src/{{folder_name}}/tool.py`

</details>