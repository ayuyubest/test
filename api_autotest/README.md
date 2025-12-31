# API自动化测试项目

基于Python + pytest + requests + allure的接口自动化测试框架，根据CSV测试用例文件自动生成测试代码。

## 项目结构

```
项目根目录/
├── conftest.py              # pytest配置文件
├── pytest.ini              # pytest配置
├── requirements.txt        # 项目依赖
├── README.md               # 项目说明
├── run_tax_declare_tests.py # 测试运行脚本
├── config/
│   ├── __init__.py
│   ├── config.yaml        # 环境配置文件
│   └── config.py          # 配置读取类
├── core/
│   ├── __init__.py
│   ├── api_client.py      # 请求客户端封装
│   ├── logger.py          # 日志工具
│   └── assertions.py      # 断言工具
├── data/
│   └── test_cases_fixed.csv     # 测试用例数据
├── testcases/
│   ├── __init__.py
│   ├── conftest.py        # 测试用例共享fixture
│   ├── test_tax_declare.py      # 税务申报测试
│   ├── test_expense_config.py   # 费用项配置测试
│   └── test_predict_config.py   # 预测配置测试
└── utils/
    ├── __init__.py
    ├── data_handler.py    # 数据处理工具
    └── common.py          # 通用工具函数
```

## 安装依赖

```bash
pip install -r requirements.txt
```

## 配置环境

1. 修改 `config/config.yaml` 中的环境配置
2. 设置环境变量（可选）：
   ```bash
   set TEST_ENV=test
   ```

## 运行测试

### 运行所有测试
```bash
# 从项目根目录运行
pytest testcases/

# 或者使用运行脚本
python run_tax_declare_tests.py
```

### 运行指定模块测试
```bash
pytest testcases/test_tax_declare.py
pytest testcases/test_expense_config.py
pytest testcases/test_predict_config.py
```

### 运行指定标签的测试
```bash
pytest -m positive
pytest -m negative
pytest -m boundary
```

### 运行指定优先级的测试
```bash
pytest -k "high"
pytest -k "medium"
pytest -k "low"
```

## 生成测试报告

### HTML报告
```bash
pytest --html=report.html --self-contained-html
```

### Allure报告
```bash
# 运行测试并生成allure数据
pytest --alluredir=./allure-results

# 生成并打开allure报告
allure serve allure-results
```

## 测试用例说明

测试用例通过CSV文件驱动，包含以下字段：
- `test_case_id`: 测试用例ID
- `test_case_name`: 测试用例名称
- `api_name`: 接口名称
- `method`: 请求方法
- `url`: 请求URL
- `headers`: 请求头（JSON格式）
- `request_data`: 请求参数（JSON格式）
- `expected_status_code`: 期望状态码
- `expected_response`: 期望响应（JSON格式）
- `test_type`: 测试类型（positive/negative/boundary）
- `priority`: 优先级（high/medium/low）
- `description`: 测试描述
- `preconditions`: 前置条件
- `postconditions`: 后置条件
- `tags`: 标签（逗号分隔）

## 日志查看

测试运行时会在 `logs/api_test.log` 文件中记录详细日志。

## 注意事项

1. 首次运行前请确保网络连接正常
2. 如需修改基础URL，请编辑 `config/config.yaml`
3. 测试数据敏感信息已做脱敏处理
4. 建议在测试环境中运行，避免影响生产数据