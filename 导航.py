from flask import Flask, render_template_string

app = Flask(__name__)

# 定义导航页的类别和链接
categories = [
    {
        "name": "日常",
        "links": [
            {"name": "云效链接", "url": "https://devops.aliyun.com/projex"},
            {
                "name": "加班申请表",
                "url": "https://alidocs.dingtalk.com/notable/share/form/v01ZWGl0w30ko8MO34Y_dv19yqvsgs3oebp3pcjys_1qX0QQ0",
            },
            {"name": "网盘", "url": "http://192.168.1.74:5000/"},
            {
                "name": "数数",
                "url": "https://ta.afafb.com/#/tga/event/-1?currentProjectId=9",
            },
            {
                "name": "日报",
                "url": "https://alidocs.dingtalk.com/i/nodes/dpYLaezmVNgdAvaAczrEbA0bJrMqPxX6?iframeQuery=sheet_range%3Dkgqie6hm_0_0_1_1",
            },
            {
                "name": "每日数据统计",
                "url": "https://alidocs.dingtalk.com/i/nodes/93NwLYZXWyb69K09Ilqm90reVkyEqBQm?iframeQuery=sheet_range%3Dst-6794df2e-87569_0_0_1_1",
            },
        ],
    },
    {
        "name": "文档",
        "links": [
            {
                "name": "安卓进度表",
                "url": "https://alidocs.dingtalk.com/i/nodes/qnYMoO1rWxbLvGRvI2q705DDJ47Z3je9?utm_scene=person_space",
            },
            {
                "name": "IOS进度表",
                "url": "https://alidocs.dingtalk.com/i/nodes/KGZLxjv9VGdO6PN6UrxYDj5eJ6EDybno?utm_scene=person_space",
            },
            {
                "name": "创意预分配表",
                "url": "https://alidocs.dingtalk.com/i/nodes/6LeBq413JAe3QPvQUy3xElaMJDOnGvpb?iframeQuery=sheet_range%3Dkgqie6hm_45_0_1_1",
            },
            {
                "name": "底板文档",
                "url": "https://alidocs.dingtalk.com/i/nodes/dQPGYqjpJYmQ5zO5uldglXLZJakx1Z5N?utm_scene=team_space",
            },
            {
                "name": "能力分层",
                "url": "https://alidocs.dingtalk.com/i/nodes/G1DKw2zgV2yb27Q2up6PqzmmWB5r9YAn?iframeQuery=sheet_range%3Dkgqie6hm_0_0_1_1",
            },
            {
                "name": "用例库",
                "url": "https://alidocs.dingtalk.com/i/nodes/20eMKjyp81Obp7Qpsoz7R3lxVxAZB1Gv?utm_scene=team_space",
            },
            {
                "name": "需求文档",
                "url": "https://alidocs.dingtalk.com/i/nodes/ydxXB52LJqeL6G26UmZbbr9KJqjMp697?utm_scene=team_space",
            },
            {
                "name": "创意用例目录",
                "url": "https://alidocs.dingtalk.com/i/nodes/amweZ92PV6y1mrLmu7BjaRo1WxEKBD6p?iframeQuery=sheet_range%3Dkgqie6hm_0_0_1_16",
            },
            {
                "name": "新方块用例目录",
                "url": "https://alidocs.dingtalk.com/i/nodes/dQPGYqjpJYmQ5zO5ug1rqprKJakx1Z5N?utm_scene=team_space",
            },
            {"name": "新方块链接(更新)", "url": "http://192.168.31.187:8080/"},
            {
                "name": "方案关卡表",
                "url": "https://alidocs.dingtalk.com/i/nodes/m9bN7RYPWdXm6od6IdlDE5ZaWZd1wyK0?iframeQuery=sheet_range%3Dkgqie6hm_0_0_1_1",
            },
            {
                "name": "常见问题",
                "url": "https://alidocs.dingtalk.com/i/nodes/lyQod3RxJKvd6P26UMnORbdlVkb4Mw9r?iframeQuery=sheet_range%3Dkgqie6hm_0_0_1_1",
            },
            {
                "name": "我的文件夹",
                "url": "https://alidocs.dingtalk.com/i/nodes/P7QG4Yx2Jp3m6Gp6TzvqkDMkV9dEq3XD?utm_scene=team_space",
            },
            {
                "name": "帮扶文档",
                "url": "https://alidocs.dingtalk.com/i/nodes/qnYMoO1rWxbLvGRvIv095l24J47Z3je9?doc_type=wiki_doc&utm_medium=main_vertical&utm_scene=team_space&utm_source=search",
            },
            {
                "name": "随机盘面库",
                "url": "https://alidocs.dingtalk.com/i/nodes/6LeBq413JAe3QPvQUMA71mENJDOnGvpb?iframeQuery=sheet_range%3Dst-052bf2b7-23273_0_0_1_1",
            },
        ],
    },
    {
        "name": "工具",
        "links": [
            {
                "name": "方案配置工具",
                "url": "http://192.168.21.8:8080/#/config/configdiff",
            },
            {
                "name": "时间戳转换工具",
                "url": "https://www.w3cschool.cn/tools/index?name=timestamptrans",
            },
            {
                "name": "方案配置查询",
                "url": "http://192.168.21.8:8080/#/config/configdiff",
            },
            {
                "name": "埋点管理平台",
                "url": "https://cs.afafb.com/auditing/#/eventManage/eventName",
            },
            {
                "name": "test_jenkins",
                "url": "http://192.168.31.224:8888/view/all/",
            },
            {
                "name": "自动化平台",
                "url": "http://192.168.21.85:3005/#/run",
            },
            {
                "name": "dev_tools",
                "url": "http:devtools://devtools/bundled/js_app.html?v8only=true&ws=192.168.16.176:6086/00010002-0003-4004-8005-000600070008",
            },
        ],
    },
    {
        "name": "服务器下发",
        "links": [
            {
                "name": "公司内网线上config",
                "url": "https://gametester.afafb.com/gametester_configs",
            },
            {
                "name": "线上config",
                "url": "http://datatester-test.afafb.com/lookup/gametester/get_configs",
            },
            {
                "name": "测试config",
                "url": "http://bbggt-test.afafb.com/game_tester_configs",
            },
        ],
    },
]
HTML_TEMPLATE = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>导航页</title>
    <style>
      body {
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 0;
        background-color: #f0f0f0;
      }
      .container {
            width: 100%; /* 可以根据需要调整宽度 */
            position: relative;
            margin: 20px auto; /* 居中显示 */
        }
      .box {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 0;
            padding-bottom: 100%; /* 高度为宽度的50% */
            background-color: #1E90FF;
            border-radius: 5px;
        }
      h1 {
        position: absolute;
        top: 0;
        left: 50%;
        transform: translateX(-50%);
        margin: 0;
        padding: 10px 20px;
        
        color: Black;
        border-bottom-left-radius: 5px;
        border-bottom-right-radius: 5px;
      }
      .category {
        margin-top: 60px; /* 确保内容不会被标题覆盖 */
        margin-bottom: 20px;
        text-align: left; /* 左对齐 */
        overflow: hidden; /* 清除浮动 */
      }
      .link {
        display: inline-block;
        width: calc(15% - 10px); /* 每个链接占约1/6宽度，减去一些间距 */
        margin: 10px;
        padding: 10px 20px;
        padding_
        text-decoration: none;
        color: white;
        background-color: #1E90FF;
        border-radius: 5px;
        transition: background-color 0.3s;
        box-sizing: border-box; /* 确保padding和border包含在width内 */
      }
      .link:hover {
        background-color: #A9A9A9;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <div class="image-container">
        <img src="{{ url_for('static', filename='images/login_logo.png') }}" alt="Example Image">
      </div>
      <h1>导航页</h1>
      {% for category in categories %}
      <div class="category">
        <h2>{{ category.name }}</h2>
        {% for link in category.links %}
        <a href="{{ link.url }}" class="link" target="_blank">{{ link.name }}</a>
        {% endfor %}
      </div>
      {% endfor %}
    </div>
  </body>
</html>
"""


@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE, categories=categories)


if __name__ == "__main__":
    app.run(debug=True)
