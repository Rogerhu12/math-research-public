# R317-direct-normal-moments

**数值记录。** 2026-11-28 17:02:55 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46168298645](https://github.com/Rogerhu12/math-research-public/actions/runs/46168298645), attempt 1；计算源码提交 `d22b64fc08b73267b9f5566742a8e7e37dc8ac60`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

针对R317/R319准确母线的新精密连续求值：12谐波短窗的24阶解析矩含严格余项，外半扇使用有限谐波原函数。物理归一化、两对称轴及实际法角反解含界；96个整角测试盒只是本项明列覆盖，不替代后继全外核Gram或reach。

```json
{
  "scale": [
    "902817449780889679/1152921504606846976",
    "14445079196494252117/18446744073709551616"
  ],
  "A": [
    "16656496291652076761/18446744073709551616",
    "16656496291652086773/18446744073709551616"
  ],
  "B": [
    "5099534778321584357/4611686018427387904",
    "5099534778321586451/4611686018427387904"
  ],
  "taylorDegree": 24,
  "TaylorRemainder": "sum |b_j| ((max |m+j|) w)^25/25!, 0<=both gates<=1",
  "normalizedPhysicalHalfPeriod": "pi/3",
  "sourceSHA256": "79ab0364deea643c13f332eadd880f179f2f310c8ab71f7fff36f784c2728d79",
  "closedTestBoxes": 96,
  "maxReferenceError": "6439128407181246849/590295810358705651712"
}
```


## 可重算输出的身份

- 2ecf-r317-directed-normal-angle-moments-and-inlet-jets.py: SHA-256 `79ab0364deea643c13f332eadd880f179f2f310c8ab71f7fff36f784c2728d79` (8284 bytes).
- 2ecf-r262-adjacent-low-ports-support-physical-cut.py: SHA-256 `94e64a7ee9ead3e1683663dfef5c8bd0b8473b088a11f17f1effb8523fb467f6` (12244 bytes).
- strict-normal-angle-moments.json: SHA-256 `afc35b6692793c7aae2e0ec70c800ed6a96f3a50b5b6d8f1b6826dfca613a16c` (651 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
