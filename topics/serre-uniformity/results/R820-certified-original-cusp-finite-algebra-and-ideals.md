# R820 实际完成：原有限 cusp 代数与两个完整理想

2026-11-15。状态：**公开 Actions 准确成功，完整原产物与输入 IO 已核。**

## 1. 实际结论

本次在原 R805 正规基和实际铅笔 $\tau=e_0,\ \sigma=e_1+e_{73}$ 中，准确得到两个原约化尖点理想
$$
\mathcal C_\tau\subset\mathcal R_{\tau,0},\qquad
\mathcal C_\sigma\subset\mathcal R_{\sigma,0}.
$$
它们分别是原20维实 cyclotomic 尖点评价映射的**完整核**。按 R820 证明忠实扩张到原 $K$ 或 $L$ 后，就是原扭曲曲线的约化 cusp 理想，没有替换原模型、共轭、截面或基。

| 实际量 | tau 图 | sigma 图 |
|---|---:|---:|
| 原正规基秩 | 272 | 272 |
| 准确可达秩 | 20 | 20 |
| 准确非零 minor 阶数 | 20 | 20 |
| 逆序链实际候选数 | 292 | 292 |
| 完整首次关系数 | 272 | 272 |
| 实际商空间维数 / colength | 20 | 20 |
| 非 monic 非零系数数目 | 5380 | 5380 |
| 非 monic 系数位置界 | 5440 | 5440 |

实际两个对角次数列均为
$$
d_0=\cdots=d_{270}=0,\qquad d_{271}=20.
$$
这来自本次准确消元及非零 minor，没有从理论总长度20预填。所有272条关系在原有限代数的全部20坐标中乘回为零，monic、下三角及严格余项条件均已准确验证。完整核由包含与实际相等长度认证；没有只认证同一个支撑。

**原底坐标的实际推论。** 第一条逆序链就是 $e_{271},\alpha e_{271},\ldots,\alpha^{19}e_{271}$，其中 $\alpha=z(c)$；其真实20阶行列式非零。故 $e_{271}\ne0$，而原剩余代数是域 $F=\mathbf Q(\xi_{41}+\xi_{41}^{-1})$，乘 $e_{271}$ 是可逆的。因此 $1,\alpha,\ldots,\alpha^{19}$ 独立，实际 $\mathbf Q(\alpha)=F$。这是已成证书的纸面推论，不是新的秩运算。sigma 图同理。

因而两个下三角理想基都可直接按实际稀疏列消费：前271列的主对角是1，只有末行有低于20次的余项；末列是20次 monic 多项式乘末基元。具体有理系数保持在活跃原产物中，未抄入 Git。一般极理想不因此被假定有同一形状。

## 2. 真实公开来源

- run [43721747750](https://github.com/Rogerhu12/math-research-public/actions/runs/43721747750)，job132835042638；compute 与 verify 均成功。
- source commit `7890fde180ffabee056de2ce8dd241b189a893a2`。
- 实际 core 时间 `36.41190155299999` 秒；不含下载、安装和上传。
- 原数学 producer 始终为 R805 run43705580592/source9f960b8e 与 R806 run43707290840/source75b1d56c。
- R813 run43715253991/source74f5296a 仅作原输入载体，没有冒充数学 producer。

只读取273条已经生成并认证的原 S3 常数项：272个正规基元对应的 $j=0$ 行以及唯一底变量分子行。所有原同权 $82^6$ 尺度、原 $\tau^3$ 分母和20维实坐标保持。准确求逆乘回、$\alpha\alpha^{-1}=1$、全部272个两图评价运输与两个20阶乘法矩阵均在这次公开计算中验证。

| 文件或接口 | 字节数 | SHA256 |
|---|---:|---|
| R820_original_cusp_finite_algebra_ideals.py | 30680 | 25f5582ed0c6dae2cf29d5eb288469067c09d917bfe1f565fb042978ea9b173c |
| R820_public_original_cusp_finite_algebra_ideals.py | 31360 | 64da695501afe93d1e41987cc1932d6f8fb58795fe085bbab6b242140157af65 |
| R820-original-cusp-finite-algebra-ideals-method.md | 5082 | 24072e143dd52517e9eb47b913d0516ff7b16bdb55bce321a2087656b90f6429 |
| 原公开 request | 4879 | 6eb90ef0491a5f78c02ac98f18a61f2dfbf1210408f518911037649c4b5d0326 |
| 原 workflow | 3271 | 795ae79acba13d12a7901602b7a76b62ef2553fe184f52279616cf33821157ce |
| p41-original-cusp-finite-algebra-ideals-certificate.json | 6047 | a2e629d05d561e1144e6989612213b33990075400a21f7c1c2f0c2eb825152b4 |
| full-outputs-manifest.json | 154422 | 2877dd3dbe604f07a58c8774897085d1de90a6faa38a6d2ed78a5bb9d7f79a8f |
| R820-stage-manifest-14d0564a3c407f21095b987a.json.gz | 31391 | 93064680035284daf511842401420f27e9b6da85cb6726a93c650a1b42b42900 |
| R820-original-selected-cusp-q0.json.gz | 88216 | 1916960fca14683c8cdf314aa942637f33d2e7aac064e23525084c597904a7e2 |
| R820-original-cusp-finite-field-interface.json.gz | 328768 | b58ec39994113b232ae6e1b4549d598352298a8071159eebef62d3901e0169cc |
| R820-retained-producer-inputs.tar.gz | 5531995 | 0fb4ae9b40aabf67ae1c6c116e8ecb525ec0efd7975ff29010e09ce674ada2f4 |
| R820-chart-tau-cusp-Hermite-index.json.gz | 17060 | df8c00e8fb5962a3481d1b07cbefd54e7a5ea51fc54e03e12d39a25354af8365 |
| R820-chart-tau-actual-reachable-minor.json.gz | 3605 | 3da1b5c478aa3a98395f739f4560fe9db5e96b12298446b7fd7487ee4871f380 |
| R820-chart-sigma-cusp-Hermite-index.json.gz | 17119 | 48e434d4387b8a4065827191fa97f53eda5cf51295f5fac6d4336d0f40528ebd |
| R820-chart-sigma-actual-reachable-minor.json.gz | 3587 | 75bc9f98fe29695fafa4c5821f19cbf758455672b547b983230de99f72492551 |

## 3. 完整只读核验与保留

实际 artifact14164872449，19737373字节；ZIP SHA256 为 `d09c6d70facec7870121cba30b13371bb672fbfd83cd9914e29ee1cfb1e9d11c`，到期2026-11-16 13:58:47 UTC。

本地只读审计核了全部600个ZIP文件、598项完整manifest、590个完成stage、289个原输入bundle成员（R805282项、R8067项），以及实际source的core/wrapper/request/workflow SHA。冻结的公开wrapper.verify原样退出0。审计没有import数学core或flint，也未重新执行任何字段、秩或矩阵算术。root另读原job成功日志、实际完整摘要与两图index，并核ZIP实际长度/哈希。

纯IO摘要6094字节，SHA256 `db60cdea9ca806657b0a41494b0a95f2dc450d77e97760a4fdca6d617c771ac3`；纯IO脚本SHA256 `cfe54277e07090fbcf11f23b414b01dedf4f085f44b9586f34adf884a28f6252`。可重算raw、输入包和机器证书均不进Git或Release；一日活跃artifact供直接后继使用。

公开bundle是5531995字节/SHA0fb4ae9b；准备期本地IO bundle是5531989字节/SHA157ebfb6。两者原289成员逐项SHA相同，压缩归档封装分别生成；本篇引用公开实际bundle，不将本地封装字节误当Actions原件。

## 4. 接回当前任务

[R814](R814-original-cusp-zero-ideal-and-exact-multiplicity-peeling.md)所需的原 $\mathcal C$ 已有两个完整实际基，可直接消费本次输出，不必等导子矩阵后再对大像矩阵消元。R815仍负责原 $M_g,\Gamma$；一般极理想 $I$ 及其降重数、三重数部分、原主函数/eta、规范高度仍缺，未由本次小任务自动完成。

不重复原Fourier、R806乘法、R813 Wronskian或已登记的p41有理点分类；一般p的同标签单位与Serre一致性主目标仍OPEN。
