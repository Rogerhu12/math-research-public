# R809 原 S5 正规坐标公开执行与输入 IO
会话：serre-public-astra-20261115。数学契约见 [R809 方法](R809-original-S5-normal-coordinate-consumer-method.md)，证明见 [原正规向量](../results/R809-original-normal-vectors-for-function-and-Hodge-inputs.md)。
本记录只有来源、参数、源码和纯 IO 摘要；新 minor、坐标及运行结果须待公开 Actions，未预填。

## 冻结执行
- core：82768B，SHA256 dedb5d6149a3c3ae86ad09e51f30c1424951a09010bf48afd948d2628e1ec21d。
- wrapper：42021B，SHA256 3616aac1b7d5dc373f0599c7ca023ef300f647fa204cd874a9655ca55b9607ea。
- active request：8482B，SHA256 508b0f8619058f35527618557bde3ac4a71e99d415deab0352807e8c6293d4f8。
- workflow：3108B，SHA256 a7c6cb8ebf4aa1f55405e4a33749d7e120b06c600c15e1b9c3b0aaeb443c00a1。
- proof SHA256 68793d3f3911d6c2ab3d530575634a70953580c221c4c4fed5fa542a2ed88a40；method SHA256 88aed12d9e958601faeb45a47e46097942801d69a5ce4aacb4bce6c4ca9153ce。

固定 qY_count=69、S5=1234、full rows=1380、prime start=1000000007、每 Dixon 组7列、每8位尝试严格矩形重构、数学预算300分钟。首 scope 仅 C0,…,C5，共84个 Q 右端；R787真实 A/B 到达后只加两目标，公共基身份与已成列不改。当前6目标不依赖尚未成功的R787。
root 已全文审 core/wrapper/证明/方法，最终变更只修原R803前690行的真实引用 schema，并将消费者接口/manifest改为内容身份不可变命名，防追加目标的中断窗。语法仅AST解析。

## 真实原输入
冻结 wrapper 的 prepare 只用 JSON/大小/SHA/配置/schema；不导入数学 core，不运行新的数学。所选原文件共4117：
| 原 producer | run | source | 所选文件 |
|---|---|---|---:|
| R786 | 43682100611 | dd262672a8b1e2af82277b15e0fa766038609670 | 3457 |
| R803 | 43702905620 | 2a3f5be764ecd335e7980557800d15959574bc8e | 19 |
| R805 | 43705580592 | 9f960b8e0b2fa825ab1391e86db4e1383ffdd700 | 629 |
| R807 | 43707939269 | 2c44d02595d57c22b5ea2c10defa93f63252061d | 12 |

完整原 manifests、receipts、来源提交、core SHA 及所选文件逐项核验。R786原3450条degree1…5行保留；R805全部619条已成新monomial前缀直接复用；R803六组已成坐标只读；R807实际新pair尾数为0，不要求虚构尾。原 sigma n=1、theta 的lambda3/lambda4=0均来自真实producer。

纯IO测试所建临时输入包279222934B，SHA256 49848da935883713c59dd22ade543002be22ec9f10fcbe251cc425eeffb899e5；正式Actions重建tar时mtime元数据可能改变包字节，成员原SHA不变。该包不入Git/Release。

继续同核时完整stage不重算，每个Dixon组只保最新完整向量与小SHA历史；六目标及以后A/B各自全1380行终验。输出只保一日活跃artifact，不自动入Git/Release。实际S5 minor、正规向量、极理想、eta和高度此刻均未报告完成。
