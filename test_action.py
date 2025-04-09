"""
action step 1:
{'go_to_url': {'url': 'http://192.168.30.101:8999/'}, 'interacted_element': None}
action step 2:
{'input_text': {'index': 3, 'text': 'ywq'}, 'interacted_element': DOMHistoryElement(tag_name='input', xpath='html/body/div/div/div/div/div[2]/form/div/input', highlight_index=3, entire_parent_branch_path=['div', 'div', 'div', 'div', 'div', 'form', 'div', 'input'], attributes={'class': 'form-control', 'type': 'text', 'autocomplete': 'off', 'name': 'account', 'id': 'account'}, shadow_root=False, css_selector='html > body > div > div > div > div > div:nth-of-type(2) > form > div > input.form-control[type="text"][autocomplete="off"][name="account"][id="account"]', page_coordinates=None, viewport_coordinates=None, viewport_info=None)}
action step 3:
{
    'input_text': {'index': 4, 'text': 'Jxtxfw@2025'},
    'interacted_element': DOMHistoryElement(tag_name='input', xpath='html/body/div/div/div/div/div[2]/form/div[2]/input', highlight_index=4, entire_parent_branch_path=['div', 'div', 'div', 'div', 'div', 'form', 'div', 'input'], attributes={'class': 'form-control', 'type': 'password', 'autocomplete': 'off', 'name': 'password', 'id': 'password'}, shadow_root=False, css_selector='html > body > div > div > div > div > div:nth-of-type(2) > form > div:nth-of-type(2) > input.form-control[type="password"][autocomplete="off"][name="password"][id="password"]', page_coordinates=None, viewport_coordinates=None, viewport_info=None)}
action step 4:
{'click_element': {'index': 6}, 'interacted_element': DOMHistoryElement(tag_name='button', xpath='html/body/div/div/div/div/div[2]/form/div[4]/button', highlight_index=6, entire_parent_branch_path=['div', 'div', 'div', 'div', 'div', 'form', 'div', 'button'], attributes={'class': 'toolbar-item primary btn', 'id': 'submit', 'type': 'submit'}, shadow_root=False, css_selector='html > body > div > div > div > div > div:nth-of-type(2) > form > div:nth-of-type(4) > button.toolbar-item.primary.btn[id="submit"][type="submit"]', page_coordinates=None, viewport_coordinates=None, viewport_info=None)}
action step 5:
{'click_element': {'index': 3}, 'interacted_element': DOMHistoryElement(tag_name='a', xpath='html/body/div/div/ul/li[4]/a', highlight_index=3, entire_parent_branch_path=['div', 'div', 'ul', 'li', 'a'], attributes={'data-pos': 'menu', 'data-app': 'project', 'href': '/index.php?m=project&f=browse', 'class': 'rounded show-in-app'}, shadow_root=False, css_selector='html > body > div > div > ul > li:nth-of-type(4) > a.rounded.show-in-app[href="/index.php?m=project&f=browse"]', page_coordinates=None, viewport_coordinates=None, viewport_info=None)}
action step 6:
{'click_element': {'index': 130}, 'interacted_element': DOMHistoryElement(tag_name='a', xpath='html/body/div/div/div/div[2]/a', highlight_index=130, entire_parent_branch_path=['div', 'div', 'iframe', 'html', 'body', 'div', 'div', 'div', 'div', 'a'], attributes={'class': 'toolbar-item ghost export btn btn-default', 'data-toggle': 'modal', 'href': '/index.php?m=project&f=export&status=doing&orderBy=order_asc'}, shadow_root=False, css_selector='html > body > div > div > div > div:nth-of-type(2) > a.toolbar-item.ghost.export.btn.btn-default[href="/index.php?m=project&f=export&status=doing&orderBy=order_asc"]', page_coordinates=None, viewport_coordinates=None, viewport_info=None)}
action step 7:
{'click_element': {'index': 190}, 'interacted_element': DOMHistoryElement(tag_name='button', xpath='html/body/div[2]/div/div/div[3]/div/div/form/div[6]/div/div/button', highlight_index=190, entire_parent_branch_path=['div', 'div', 'iframe', 'html', 'body', 'div', 'div', 'div', 'div', 'div', 'div', 'form', 'div', 'div', 'div', 'button'], attributes={'class': 'btn primary', 'type': 'submit', 'zui-init': '$element.off(\'.zin.on\');$element.on(\'click.zin.on\',function(event,args){\nconst $this = $(this);\nconst target = event.target;\n$(target).parent().addClass(\'disabled\');$(target).parent().attr(\'disabled\');$(target).closest(\'.form-actions\').append(\'<span class="text-gray">文件正在导出中，请耐心等待</span>\');;\n});', 'id': 'zin_project_export_h_31', 'z-zui-inited': ''}, shadow_root=False, css_selector='html > body > div:nth-of-type(2) > div > div > div:nth-of-type(3) > div > div > form > div:nth-of-type(6) > div > div > button.btn.primary[type="submit"][id="zin_project_export_h_31"]', page_coordinates=None, viewport_coordinates=None, viewport_info=None)}
action step 8:
{'wait': {'seconds': 10}, 'interacted_element': None}
action step 9:
{'done': {'text': '成功完成导出任务，并已下载文件。', 'success': True}, 'interacted_element': None}

"""
import time

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # 启动浏览器（推荐Chromium）
    browser = p.chromium.launch(
        headless=False,
        downloads_path="/downloads",
    )

    # 配置下载路径
    context = browser.new_context(
        accept_downloads=True
    )

    page = context.new_page()
    # action step 1:
    page.goto('http://192.168.30.101:8999/')
    time.sleep(0.5)
    # action step 2:
    page.locator(
        'html > body > div > div > div > div > div:nth-of-type(2) > form > div > input.form-control[type="text"][autocomplete="off"][name="account"][id="account"]').fill(
        'ywq')
    time.sleep(0.5)
    # action step 3:
    page.locator(
        'html > body > div > div > div > div > div:nth-of-type(2) > form > div:nth-of-type(2) > input.form-control[type="password"][autocomplete="off"][name="password"][id="password"]').fill(
        'Jxtxfw@2025')
    time.sleep(0.5)
    # action step 4:
    page.locator(
        'html > body > div > div > div > div > div:nth-of-type(2) > form > div:nth-of-type(4) > button.toolbar-item.primary.btn[id="submit"][type="submit"]').click()
    time.sleep(0.5)
    # action step 5:
    page.locator(
        'html > body > div > div > ul > li:nth-of-type(4) > a.rounded.show-in-app[href="/index.php?m=project&f=browse"]').click()
    time.sleep(0.5)
    # action step 6:
    page.locator(
        'html > body > div > div > div > div:nth-of-type(2) > a.toolbar-item.ghost.export.btn.btn-default[href="/index.php?m=project&f=export&status=doing&orderBy=order_asc"]').click()
    time.sleep(0.5)
    # action step 7:
    page.locator(
        'html > body > div:nth-of-type(2) > div > div > div:nth-of-type(3) > div > div > form > div:nth-of-type(6) > div > div > button.btn.primary[type="submit"][id="zin_project_export_h_31"]').click()
    time.sleep(0.5)
    # action step 8:
    time.sleep(10)
    # action step 9:
    print("成功完成导出任务，并已下载文件。")
