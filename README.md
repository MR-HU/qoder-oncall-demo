# Qoder On-call Demo Repository

这是用于演示 Qoder Cloud Agents 研发值班助手的最小 Python 项目。

## 场景

`error.log` 记录了订单金额异常。`order_service.py` 中的 `calculate_total` 错误地将折扣比例直接从订单金额中减去，正确行为应当是按折扣比例计算折后金额。

## 运行测试

```bash
python3 -m pytest -q
```

当前测试预期失败，后续由 Qoder Agent 分析并修复。
