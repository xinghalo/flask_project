import app
import argparse

if __name__ == '__main__':

    # 定义参数解析器
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)

    # 创建参数 mode
    parser.add_argument(
        '--mode',
        '-m',
        type=str,
        required=True,
        help = "deploy mode: dev, test, pre, online"
    )

    PARAMS = parser.parse_args()

    # 启动应用
    app.run(PARAMS.mode)