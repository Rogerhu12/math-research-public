# E89 原 degree178 来源及第五读者的实际公开执行

日期：2026-11-26；会话 Astra-rank2-Sha-7d29daa5-20261126。

## 1. 完整 CM 共同核

脚本 `scripts/check-r943-degree178-full-cm-source.py`，参数 `--workers=4`，python-flint 0.9.0；run [45764784007](https://github.com/Rogerhu12/math-research-public/actions/runs/45764784007)，job 139722963336，来源 `ab5d8cefd5ccfc294ebf85408e539a4565b3362f`，实际 success。

在原 norm7、norm13 运算和完整30维来源中，共同零质量核维数为1；所选规范向量的原首项阶为6。两个运算完整交换，共同稳定闭包的秩29保持为29。此处读取的是全部来源，不是两个特征值推测全局角色。

| 记录 | SHA-256 |
|---|---|
| 脚本 | `b5c2e3f6781e1a788e2d3fd749f10e2ecab9e6c58e2950aecc9acf727f237e67` |
| 原完整矩阵 | `6ee0222d90db6add172d6d6e650a2f8186b1776072661594a242b4e65c78d665` |
| stdout，2915 bytes | `bf8fb4b3536157c8ec802ee81050c9f40bbc81edbe483fda972836e44fa5b2e0` |
| 工具返回完整日志，UTF-8 保留 BOM，16132 bytes | `77459e236b632c74b6f3c6f821052692c259b0dad4bcc18a5a84089b6f5fa06e` |

## 2. 第五低轴、实际角帽和有限89范数

脚本 `scripts/check-r943-original-degree178-fifth-axis.py`，参数为空，python-flint 0.9.0；run [45766655437](https://github.com/Rogerhu12/math-research-public/actions/runs/45766655437)，job 139729057126，来源 `2063772449e2208962076fd740b714a7b2ad2bb8`，2026-11-26 06:13:33 UTC 实际 success。

本脚本在同一次 run 重生第1节的完整30维来源和矩阵，只在内存读取系数，不用已生成系数表作为输入。完整旧四轴锚点与新五轴返回均通过。按列 $w^5,\ldots,w$ 的五轴行列式为

$$
\det B_5=-\frac{104568614585465172496900768457847209984}
 {46188380197265625}\ne0.
$$

有限89处实际 $\tau(g)=g^{60}$ 的投影给 $C=5$，原常数 $\sqrt{89}-5$ 和范数平方 $45(89-5\sqrt{89})$ 非零。

实际新来源 $W_{178}$ **不属于**旧 $B_{89}$：原角因子在 $t=0$ 仅一重，旧归一化要求两重，且角次数29超过28。实际有 $S_{34}W_{178}\in B_{106}$，旧导子返回权为11086；这些是有成本的乘法关系，不能传播指定中央零。原 $S_{34}$ 也确实整除 $W_{178}$，商的 $X$ 次数24，同样不把两条中央条件合并。

| 记录 | SHA-256 |
|---|---|
| 第五读者脚本 | `c4226727954c4f5fc8477bb17987a49242ef73103049ff7de8e004d442698ec6` |
| stdout，1996 bytes | `48a39280ed06fd2e8579da8df6815287c68cfdd59b294d6e396ce83474f0e949` |
| 工具返回完整日志，UTF-8 保留 BOM，15034 bytes | `22cb81d7e811e3cc1d71dcdec8af241ac96de4b5fef7639511855675ae6b5137` |

## 3. 已付范围

以上只登记实际完整来源、低轴线性独立和局部投影。完整 E89 Schwartz、全局角色、周期、通常全 Selmer 桥及五轴后的真实原窗口已由 [R943](../results/R943-original-e89-fifth-central-full-selmer-and-five-axis-gate.md) 逐项证明。当前未由计算得到原深核、全局底非零、ordinary 或无穷素数结论。全部可重算输出和系数不入库。

## 4. 新来源环的固定角除子：本次公开请求

新增 `scripts/check-original-e89-angular-profile.py`（SHA-256 `e30590582a6ff26761bebd879133d9f139cdf99c1009eba0d65e4fdd3476aa36`），无参数；request `2026-11-26-original-e89-angular-profile-7d29`。独立小工作流 `rank2-sha-e89-angular-profile.yml`，ubuntu-latest、15分钟、python-flint 0.9.0；同次以 `--workers=4` 重生第1节完整原CM来源并核完整矩阵hash。只读取实际四角点及d的重数、完整多项式gcd及Bézout回乘、resultant摘要；不保存系数或输出。

实际 run [45773031338](https://github.com/Rogerhu12/math-research-public/actions/runs/45773031338)、job139749954422、来源 `d2856ef101891f008ef125d219468a226903bace`，于2026-11-26 07:08:16 UTC success；完整原来源在同job重生，22.55秒。

实际 $t,t-1,h_7$ 的两个几何根及 $d$ 都恰为一重，$\deg f_W=29$、$\deg(f_W/a)=25$。但是完整 $\gcd(H_{18},f_W/a)$ **次数为4**，完整Bézout回乘已核，resultant为零。因此仅 $U^{89},W^{68}$ 的无基点pencil分支不成立，先前条件分支中的1700次/28883导子候选没有获得证明。当前继续改用有成本的实际同权组合，并单独证明归一化、分式域及返回导子。

| 记录 | SHA-256 |
|---|---|
| stdout，2025 bytes | `a19ba0f2e4aaa541468a901bb8d7687677b22419f45ee89e5c80fae6b34e4e43` |
| 原角多项式摘要 | `7fbad6a6407c938654454c0c6c1fb8e221e02dfeab73b8fd55d192d76a045adb` |
| 完整Bézout恒等式摘要 | `941bafb79db5ea7f9abb4c2553451dd476bb5db131d18b2ed4f759270cd500fd` |
| 工具返回完整日志，UTF-8保留BOM，15083 bytes | `e66fdbf91c8eeb4c704bc6abffeb254c039b6c75073d46efa877be82f268a267` |

该PASS只对应固定角重数与完整gcd读者，不对应待证pencil、导子、原306除子或无穷中央非零。未保存任何可重算输出。

## 5. 保持同一原来源环的参数替换请求

接第4节实际gcd4，更新同一小reader为SHA-256 `483e259dc60b9778404ae68be4e632cf6e6166b4c71f1879d7951afd3b5a2229`，request `2026-11-26-original-e89-angular-profile-shear-7d29`，参数仍为空。保留第4节的全部原检查，另逐个检验 $c=0,\ldots,25$ 的 $U_c=U+cS^4$、$H_c=H/91+c a^3d^4/7^4$；全多项式gcd、Bézout回乘及resultant均对实际新参数进行。代换保持 $R[S,U_c,W]=R[S,U,W]$，但不赋予 $U_c$ 新中央零。

实际 run [45773737555](https://github.com/Rogerhu12/math-research-public/actions/runs/45773737555)、job139752282740、source `f9c9f614ea40a699e26a765b480aa51022830d1f`，于2026-11-26 07:14:04 UTC success。同次完整CM重生后，$c=0$ 的gcd仍为4，最小成功参数是 **$c=1$**，准确取 $U_+=U+S^4$。实际 $H_+=H/91+a^3d^4/7^4$ 与 $G=f_W/a$ 互素，也与 $ad$ 互素，角次数分别18/22，完整Bézout回乘及非零resultant已通过。

| 记录 | SHA-256 |
|---|---|
| stdout，3051 bytes | `47e60f4436fb873b805b24ea41856f2f9052a6818154e87498c8ca5ba6e10d70` |
| 新参数完整Bézout恒等式摘要 | `5845e05ef1e2284ad9e6092d74fe143d2a0d1aee1c57f8958f724482a96ff562` |
| 非零 $\operatorname{Res}(H_+,G)$ 摘要 | `b65bd1ec9cdfa4755e6416b5e5698d4fbd641b9c5657406bd1c31654259b0bac` |
| 完整日志UTF-8保留BOM，16174 bytes | `971c33d36dd6a5785ea045674fa86ff360c768266e0f9793968caba978a37dff` |

resultant分子1951bits、分母457bits；这里只保存摘要和重生方法，不保存生成值。6052同权pencil、1700/424分式次数及导子28883仍须完整代数证明，不能只凭脚本算出的候选数字宣称已付。单F旧运行保持，不触发第二次306。
