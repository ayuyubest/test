# 税务申报配置API测试说明

## 概述

本目录包含税务申报配置相关的API自动化测试用例，基于CSV测试用例数据生成。

## 测试文件说明

### 1. test_tax_declare_config.py
- **功能**: 包含税务申报配置相关的结构化测试用例
- **测试类**:
  - `TestTaxDeclareConfig`: 店铺主体关系设置相关测试
  - `TestExpenseConfig`: 报送场景费用项设置相关测试
  - `TestPredictConfig`: 预测申报金额设置相关测试

### 2. test_csv_driven.py
- **功能**: 基于CSV数据驱动的参数化测试
- **特点**: 直接从CSV文件读取测试数据，支持动态测试用例生成

## 测试用例覆盖

### 店铺主体关系设置
- **TC050001**: 基础数据初始化_正常流程
- **TC050002**: 基础数据初始化_无权限访问
- **TC050003**: 新增主体_正常流程

### 报送场景费用项设置
- **TC051001**: 基础数据初始化_正常流程

### 预测申报金额设置
- **TC052001**: 基础数据初始化_正常流程

## 运行方式

### 1. 运行所有测试
```bash
# 使用pytest直接运行
pytest testcases/

# 使用自定义脚本运行
python run_tax_declare_tests.py
```

### 2. 按测试类型运行
```bash
# 只运行正向测试用例
python run_tax_declare_tests.py --type positive

# 只运行负向测试用例
python run_tax_declare_tests.py --type negative

# 运行CSV驱动的测试
python run_tax_declare_tests.py --type csv_driven
```

### 3. 按功能模块运行
```bash
# 只运行税务申报配置测试
python run_tax_declare_tests.py --type tax_declare

# 只运行费用项配置测试
python run_tax_declare_tests.py --type expense_config

# 只运行预测配置测试
python run_tax_declare_tests.py --type predict_config
```

### 4. 使用pytest标记运行
```bash
# 运行正向测试用例
pytest -m positive

# 运行负向测试用例
pytest -m negative

# 运行高优先级测试用例
pytest -m critical
```

## 测试数据

测试数据来源于 `data/test_cases_fixed.csv` 文件，包含以下字段：
- `test_case_id`: 测试用例ID
- `test_case_name`: 测试用例名称
- `api_name`: 接口名称
- `method`: 请求方法
- `url`: 请求URL
- `headers`: 请求头
- `request_data`: 请求数据
- `expected_status_code`: 期望状态码
- `expected_response`: 期望响应
- `test_type`: 测试类型
- `priority`: 优先级
- `description`: 测试描述
- `tags`: 标签

## 报告生成

### Allure报告
```bash
# 运行测试并生成Allure报告
python run_tax_declare_tests.py

# 手动生成报告
allure generate allure-results --clean --output allure-report
allure open allure-report
```

### HTML报告
```bash
# 生成HTML报告
pytest --html=report.html --self-contained-html
```

## 环境配置

### 1. 环境变量
```bash
# 设置测试环境
export TEST_ENV=test
```

### 2. 配置文件
修改 `config/config.yaml` 中的环境配置：
```yaml
env:
  test:
    base_url: "https://hjytest.ali2.huice.cc/huice/api/recon"
    timeout: 30
```

## 注意事项

1. **认证**: 测试需要有效的认证token，通过 `auth_token` fixture提供
2. **环境**: 确保测试环境可访问且数据准备完整
3. **依赖**: 运行前确保安装所有依赖包：`pip install -r requirements.txt`
4. **权限**: 部分测试用例需要特定权限，确保测试账号权限配置正确

## 扩展测试用例

### 1. 添加新的CSV测试用例
在 `data/test_cases_fixed.csv` 文件中添加新行，遵循现有格式

### 2. 添加新的结构化测试
在相应的测试类中添加新的测试方法，使用allure装饰器标记

### 3. 自定义断言
在 `core/assertions.py` 中添加新的断言方法

## 故障排除

### 常见问题
1. **认证失败**: 检查登录凭据和token获取逻辑
2. **网络超时**: 调整 `config.yaml` 中的timeout设置
3. **数据格式错误**: 检查CSV文件格式和JSON数据格式
4. **权限不足**: 确认测试账号具有相应接口访问权限

### 调试技巧
1. 使用 `-s` 参数查看详细输出
2. 检查 `logs/api_test.log` 日志文件
3. 在Allure报告中查看请求和响应详情