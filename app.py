import os
from flask import Flask, jsonify

# 初始化 Flask 应用
app = Flask(__name__)

# 示例接口：可替换为你自己的业务逻辑
@app.route('/')
def index():
    return jsonify({
        "code": 200,
        "message": "服务已在 Render 上成功部署",
        "port": os.environ.get("PORT", "5000")
    })

# 启动配置：严格遵循 Render 要求
if __name__ == '__main__':
    # 读取 Render 动态分配的 PORT 环境变量，本地默认 5000
    port = int(os.environ.get("PORT", 5000))
    # 监听 0.0.0.0，允许外部网络访问
    app.run(host="0.0.0.0", port=port)
