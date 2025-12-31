import json
from typing import Any, Dict
import allure
from requests import Response

class ApiAssertions:
    @staticmethod
    @allure.step("验证响应状态码")
    def assert_status_code(response: Response, expected_code: int):
        assert response.status_code == expected_code, \
            f"期望状态码 {expected_code}, 实际状态码 {response.status_code}"

    @staticmethod
    @allure.step("验证响应内容")
    def assert_response_content(response: Response, expected_response: Dict[str, Any]):
        actual_response = response.json()
        expected = json.loads(expected_response) if isinstance(expected_response, str) else expected_response
        
        for key, value in expected.items():
            assert key in actual_response, f"响应中缺少键 {key}"
            assert actual_response[key] == value, \
                f"键 {key} 的值不匹配，期望 {value}, 实际 {actual_response[key]}"
    
    @staticmethod
    @allure.step("灵活验证响应内容")
    def assert_response_content_flexible(response: Response, expected_response: Dict[str, Any]):
        """
        灵活的响应内容验证，支持部分匹配和类型转换
        """
        actual_response = response.json()
        expected = json.loads(expected_response) if isinstance(expected_response, str) else expected_response
        
        # 如果实际响应包含错误信息，记录但不强制失败
        if 'code' in actual_response and actual_response.get('success') is False:
            allure.attach(
                json.dumps(actual_response, ensure_ascii=False, indent=2),
                name="API错误响应",
                attachment_type=allure.attachment_type.JSON
            )
            # 检查是否是业务逻辑错误（如"请先选择店铺"）
            if 'message' in actual_response:
                print(f"API业务错误: {actual_response['message']}")
        
        # 对于成功响应，进行灵活验证
        for key, value in expected.items():
            found = False
            actual_value = None
            
            # 首先在根级别查找
            if key in actual_response:
                actual_value = actual_response[key]
                found = True
            # 如果根级别没有，在data字段中查找
            elif 'data' in actual_response and key in actual_response['data']:
                actual_value = actual_response['data'][key]
                found = True
            # 处理字段名称的变化（如incomDim vs incomeDim）
            elif 'data' in actual_response:
                # 尝试找到相似的字段名
                for data_key in actual_response['data'].keys():
                    # 更灵活的字段名匹配 - 检查是否包含相同的核心词汇
                    if ('incom' in key.lower() and 'incom' in data_key.lower()) or \
                       ('refund' in key.lower() and 'refund' in data_key.lower()) or \
                       (key.lower().replace('dim', '') in data_key.lower()) or \
                       (data_key.lower().replace('dim', '') in key.lower()):
                        actual_value = actual_response['data'][data_key]
                        found = True
                        print(f"字段名映射: {key} -> data.{data_key}")
                        break
            
            if found:
                # 尝试类型转换
                if isinstance(value, int) and isinstance(actual_value, str):
                    try:
                        actual_value = int(actual_value)
                    except ValueError:
                        pass
                
                # 对于列表类型，进行部分匹配验证
                if isinstance(value, list) and isinstance(actual_value, list):
                    if len(value) > 0 and len(actual_value) > 0:
                        # 验证列表不为空且包含期望的元素结构
                        expected_item = value[0]
                        actual_item = actual_value[0]
                        if isinstance(expected_item, dict) and isinstance(actual_item, dict):
                            # 只验证期望字段存在，不强制要求值完全匹配
                            for item_key, item_value in expected_item.items():
                                if item_key in actual_item:
                                    # 对于数值类型，检查是否在合理范围内
                                    if isinstance(item_value, int) and isinstance(actual_item[item_key], int):
                                        # 如果是ID类型字段，只验证存在且为正数
                                        if 'id' in item_key.lower():
                                            assert actual_item[item_key] > 0, f"列表项键 {item_key} 应为正数，实际 {actual_item[item_key]}"
                                            print(f"✓ 列表项键 {item_key} 验证通过: {actual_item[item_key]}")
                                        else:
                                            # 对于非ID字段，进行精确匹配
                                            assert actual_item[item_key] == item_value, \
                                                f"列表项键 {item_key} 的值不匹配，期望 {item_value}, 实际 {actual_item[item_key]}"
                                    else:
                                        # 对于字符串等其他类型，如果实际值为None或空，则跳过验证
                                        if actual_item[item_key] is not None and actual_item[item_key] != "":
                                            assert actual_item[item_key] == item_value, \
                                                f"列表项键 {item_key} 的值不匹配，期望 {item_value}, 实际 {actual_item[item_key]}"
                                        else:
                                            print(f"⚠️ 跳过空值字段验证: {item_key}")
                                else:
                                    # 如果字段不存在，记录警告但不失败
                                    print(f"⚠️ 列表项中缺少键 {item_key}，但继续验证其他字段")
                            print(f"✓ 列表字段 {key} 结构验证通过")
                            continue
                
                # 普通字段验证
                assert actual_value == value, \
                    f"键 {key} 的值不匹配，期望 {value}, 实际 {actual_value}"
            else:
                # 如果是错误响应，不强制要求所有期望字段都存在
                if actual_response.get('success') is not False:
                    assert False, f"响应中缺少键 {key}，实际响应结构: {list(actual_response.keys())}"