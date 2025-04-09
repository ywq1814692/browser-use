import asyncio
import json
import logging

from browser_use.agent.views import ActionResult

from browser_use.controller.service import Controller
from langchain_ollama import ChatOllama

from browser_use.browser.context import BrowserContextConfig, BrowserContext

from browser_use.browser.browser import Browser, BrowserConfig

from browser_use.agent.service import Agent
from langchain_openai import ChatOpenAI
import os
from lmnr import Laminar
from lmnr import observe

logger = logging.getLogger(__name__)
os.environ["ANONYMIZED_TELEMETRY"] = "false"

Laminar.initialize(project_api_key="eFBMZsKRd1VREHNPh1ZeXh9ewWeX5RHcDDrX5JLV7XQPK4DP4CFeD8MKfS1QqDix")


def default_serializer(obj):
    if hasattr(obj, 'to_dict'):
        return obj.to_dict()
    elif hasattr(obj, '__dict__'):
        return obj.__dict__
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")


@observe()
async def main():
    config = BrowserContextConfig(
        viewport_expansion=0,
        wait_for_network_idle_page_load_time=1,
        save_recording_path="records/",
        disable_security=True,
        save_downloads_path="downloads/",
    )
    browser = Browser(
        # config=BrowserConfig(
        #     # chrome_instance_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        #     # new_context_config=config,
        # ),
    )
    # browser = Browser()
    context = BrowserContext(browser=browser, config=config)
    # task = """
    #         1.打开我的禅道，网址：http://192.168.30.101:8999/
    #         2.登录禅道，用户名：x_username，密码：x_password
    #         3.选中并打开“IPV6流量监控系统V1.0”项
    #         4.选中并打开需求选项卡
    #         5.点击提研发需求按钮，新增研发需求
    #         6.在新增研发需求表单页面，填写内容：评审人选择“刘江涛”，研发需求名称：“测试browseruse”，优先级选择“2”，工时：“10”，描述：“测试browseruse能否执行表单填写”，验收标准：“成功执行”
    #         8.保存
    # """
    # page = await context.get_current_page()
    # await page.goto("http://192.168.30.101:8999/")
    controller = Controller(exclude_actions=[
        'search_google',
        'switch_tab',
        'extract_content',
        'scroll_down',
        'scroll_up',
        'send_keys',
        'scroll_to_text',
        'get_dropdown_options',
        'select_dropdown_option',
    ])
    controller = Controller(exclude_actions=['search_google', ])

    @controller.action('If a captcha is required, ask human for help, do not try it yourself!')
    # @controller.action('如果需要验证码，请用户输入验证码')
    async def ask_human_for_captcha(index: int, browser: BrowserContext, question: str):
        captcha = input(f'\n{question}\nInput:')
        if index not in await browser.get_selector_map():
            raise Exception(f'Element index {index} does not exist - retry or use alternative actions')

        element_node = await browser.get_dom_element_by_index(index)
        await browser._input_text_element_node(element_node, str(captcha))
        msg = f'⌨️  Input captcha {str(captcha)} into index {index}'
        logger.info(msg)
        logger.debug(f'Element xpath: {element_node.xpath}')
        return ActionResult(extracted_content=msg, include_in_memory=True)

    sensitive_data = {'x_username': 'ywq', 'x_password': 'Jxtxfw@2025'}
    task = """
1.访问 http://192.168.30.101:8999/
2.输入用户名 ywq，密码 Jxtxfw@2025 → 登录
3.点击菜单栏中的 ‌“项目”‌
4.点击 ‌“导出”‌ 按钮打开导出页面
5.点击导出页面的“导出”按钮导出文件
6.确认导出完成 → 结束任务
    """
    # sensitive_data = {'x_username': 'wangjj36', 'x_password': 'wangjj86355799'}
    task = """1.访问 https://shad.samr.gov.cn/#/login
    2.输入用户名 x_username,密码 x_password，验证码 → 点击登录
    3.登录成功
    4.结束任务
    # """
    task = """
1.访问 http://192.168.30.103:17003/exam-app/a/login/welcome
2.输入用户名："superadmin" 密码："1" 点击登录按钮登录
3.点击"考生管理"菜单
4.点击"考生信息"
5.点击"导出"按钮导出考生信息
6.结束
    """
    # #     task = """1. Navigate to https://shad.samr.gov.cn/#/login
    # 2.input Username x_username and password x_password
    # 3.ask human for captcha
    # 4.click login
    # 5.wait for successful login
    # 6.End the task
    #     """
    # task = """
    #         1.打开我的禅道，网址：http://192.168.30.101:8999/
    #         2.登录禅道，用户名：ywq，密码：Jxtxfw@2025
    #         3.完成
    # """

    # task = """打开www.baidu.com,搜索AI
    # """
    # 阿里云
    # base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1"
    # model_name = 'deepseek-r1-distill-llama-70b'
    # api_key = "sk-b7c4b52357124032b0bde95b88a04e39"

    # deepseek
    base_url = "https://api.deepseek.com"
    api_key = "sk-65aba92d4e96461bb7ca59ea607b1de4"
    # model_name = "deepseek-r1"
    model_name = "deepseek-chat"

    # 私有云14b
    # base_url = "http://47.95.42.198:1234/v1"
    # model_name = "lmstudio-community/deepseek-r1-distill-qwen-14b"
    # api_key = "123"
    llm = ChatOpenAI(
        base_url=base_url,
        # model='deepseek-r1',
        model=model_name,
        temperature=0.2,
        api_key=api_key,
        # max_tokens=200,
        frequency_penalty=0.5,
        top_p=0.9,
        # model_kwargs={
        #     "top_p": 0.9,
        #     # "top_k": 50,
        # },
        # streaming=False,
    )
    # planner_llm = ChatOpenAI(
    #     base_url='https://dashscope.aliyuncs.com/compatible-mode/v1',
    #     model='deepseek-r1-distill-llama-70b',
    #     temperature=0.2,
    #     # max_tokens=200,
    #     top_p=0.9,
    #     frequency_penalty=0.5,
    #     # model_kwargs={
    #     #     "top_p": 0.9,
    #     #     # "top_k": 50,
    #     # },
    #     api_key=api_key,
    #     streaming=True,
    # )
    # llm = ChatOpenAI(
    #     base_url='http://192.168.30.139:1234/v1',
    #     # model='deepseek-r1-distill-qwen-14b',
    #     model='deepseek-r1-distill-llama-8b',
    #     api_key=api_key,
    #     temperature=0.2,
    #     # max_tokens=200,
    #     top_p=0.9,
    #     streaming=True,
    # )
    # planner_llm = ChatOpenAI(
    #     base_url='http://192.168.30.139:1234/v1',
    #     model='deepseek-r1-distill-llama-8b',
    #     temperature=0.2,
    #     # max_tokens=200,
    #     top_p=0.9,
    #     api_key=api_key,
    #     streaming=True,
    # )
    # planner_llm = ChatOllama(
    #     base_url='http://localhost:11434/',
    #     model='deepseek-r1:latest',
    # )
    agent = Agent(
        task=task,
        browser_context=context,
        # browser=browser,
        llm=llm,
        max_actions_per_step=3,
        use_vision=False,
        # planner_llm=planner_llm,
        # use_vision_for_planner=False,
        # planner_interval=3,
        save_conversation_path="logs/conversation",
        # sensitive_data=sensitive_data,
        controller=controller,
        extend_system_message="Answer with Chinese except for your JSON responses."
    )

    result = await agent.run()
    # logger.info(action for action in result.model_actions())
    print(type(result.model_actions()))
    for index, action in enumerate(result.model_actions()):
        # logger.info(action)
        logger.info(f"action step {index + 1}:")
        print(type(action))
        logger.info(str(action))
        action_json = json.dumps(action, default=default_serializer, ensure_ascii=False, indent=4)
        logger.info(f"action json: {action_json}")
        if action['interacted_element']:
            xpath = action['interacted_element'].css_selector
        else:
            xpath = None
        logger.info(f"xpath: {xpath}")
    print(result.is_done())
    # logger.info(result.history())
    # logger.info(result.model_thoughts)
    # logger.info(result.conversation)
    await browser.close()
    await context.close()


asyncio.run(main())
