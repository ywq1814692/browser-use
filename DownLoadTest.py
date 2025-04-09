from playwright.sync_api import sync_playwright
import os
import time
from pathlib import Path


def export_file_with_playwright(
        url: str,
        trigger_selectors: list[str],
        download_dir: str = "downloads",
        timeout: int = 30,
        headless: bool = True
) -> str:
    """
    使用Playwright自动导出文件的完整解决方案

    参数：
    url: 目标网页地址
    trigger_selector: 触发下载的按钮/元素CSS选择器
    download_dir: 文件保存目录（默认downloads）
    timeout: 下载超时时间（秒）
    headless: 是否使用无头模式

    返回：
    下载文件的完整路径
    """
    with sync_playwright() as p:
        # 创建下载目录
        Path(download_dir).mkdir(exist_ok=True)

        # 启动浏览器（推荐Chromium）
        browser = p.chromium.launch(
            headless=headless,
            downloads_path=download_dir,
        )

        # 配置下载路径
        context = browser.new_context(
            accept_downloads=True
        )

        page = context.new_page()

        try:
            # 导航到目标页面
            page.goto(url, timeout=60000)
            print(f"已加载页面：{page.title()}")

            # 注册下载监听
            with page.expect_download(timeout=timeout * 1000) as download_info:
                # 触发下载操作
                for selector in trigger_selectors:
                    page.click(selector)
                print("已触发下载操作")

            # 获取下载对象
            download = download_info.value

            # # 等待下载完成
            start_time = time.time()
            # while not download.is_finished():
            #     if time.time() - start_time > timeout:
            #         raise TimeoutError("下载超时")
            #     time.sleep(0.5)

            # 获取临时文件路径并移动
            while not os.path.exists(download.path()):
                if time.time() - start_time > timeout:
                    raise TimeoutError("下载超时")
                time.sleep(0.5)
            temp_path = download.path()
            filename = download.suggested_filename
            final_path = os.path.join(download_dir, filename)

            # 确保文件移动成功
            download.save_as(final_path)
            print(f"文件已保存到：{final_path}")

            return final_path

        except Exception as e:
            print(f"操作失败：{str(e)}")
            raise
        finally:
            # 清理资源
            context.close()
            browser.close()


# 使用示例 - 导出GitHub仓库的代码(ZIP)
if __name__ == "__main__":
    exported_file = export_file_with_playwright(
        url="https://github.com/microsoft/playwright",
        trigger_selectors=[
            'button[data-variant="primary"][aria-haspopup]:has-text("Code")',
            'span:has-text("Download ZIP")'
        ],  # 实际使用时需要根据目标页面调整选择器
        download_dir="my_downloads",
        headless=False
    )
    print("导出完成：", exported_file)
