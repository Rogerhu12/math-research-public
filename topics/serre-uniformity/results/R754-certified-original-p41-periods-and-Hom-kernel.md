# R754：原 p=41 全部周期与完整 Hom 核的精确证书

日期：2026-11-14。状态：**已证明，并已在本公开仓库 GitHub Actions 完成精确计算。**

本篇将 [R751 的原周期公式](R751-original-period-compression-in-the-retained-degree-280-field.md) 和 [R754 完整有限方法](../notes/R754-original-periods-and-Hom-kernel-method.md) 接到实际成功产物。这里没有把有理 Hom 核冒充完整整数周期格。

## 1. 实际完成的结论

在原 $p=41$、原正 CM 目标 $C/L:y^2=x^3+b$、原六个 $\omega_j$、原 $c_0,c_1$ 及 R738 全部原闭链下，已经精确计算：

| 项目 | 实际完成值 |
|---|---:|
| 原归一加法周期 | 40 |
| 原相对 Manin 边 | 819 |
| 原整数闭链基 | 800 |
| 系数域 | $L=K(b)$，$[L:K]=7$ |
| 同一 $K=\mathbf Q(\zeta)$ 上的未知数 | 42 |
| 非恒定 $b$ 坐标约束 | 4800 |
| 约束的准确秩 | 36 |
| 完整核的 $K$ 维数 | 6 |
| 六个核向量逐一代回 | 全部 800 条原闭链通过 |

六个实际核基、全部 $800\times6$ 个 $K$ 周期、每个方向的真实整数清分母因子都已保存在完整产物中。六个因子的二进制位长依原顺序为

$$
336,\quad628,\quad917,\quad1210,\quad1502,\quad1791.
\tag{754.1}
$$

没有断言这些因子是 $41$ 单位。逐基清分母的子格也不被认作完整整数 Hom 格；后者由 R759 接续计算。

## 2. 运行、源码与成功记录

实际公开运行：[GitHub Actions run 43620862489](https://github.com/Rogerhu12/math-research-public/actions/runs/43620862489)。

- source commit：b36d2c58b39f42a694236d48f64444bb6fe1d0af；
- 核心程序：[R754_original_periods_and_Hom_kernel.py](../scripts/R754_original_periods_and_Hom_kernel.py)；
- 核心 SHA-256：f196cb805d1ca91e8995866032a0a3ec3f96aac06e03b67a7c1f196fff759251；
- Python-FLINT 固定为 0.9.0；
- 核心实际秒数：2183.2586161159998；
- 完成时刻：2026-11-14T18:00:15.710710+00:00；
- 进程退出码 0，完整运行和全部原链验证均成功。

小证书直接保存在仓库：

- [最终数学证书](../computations/R754-original-p41-periods-and-Hom-kernel/43620862489-1/p41-original-period-and-Hom-kernel-certificate.json)；
- [核心回执](../computations/R754-original-p41-periods-and-Hom-kernel/43620862489-1/core-receipt.json)；
- [实际执行回执](../computations/R754-original-p41-periods-and-Hom-kernel/43620862489-1/run-receipt.json)；
- [全部产物清单](../computations/R754-original-p41-periods-and-Hom-kernel/43620862489-1/full-outputs-manifest.json)；
- [原输入复用回执](../computations/R754-original-p41-periods-and-Hom-kernel/43620862489-1/retained-inputs-receipt.json)；
- [逐阶段真实日志](../computations/R754-original-p41-periods-and-Hom-kernel/43620862489-1/public-actions-run.log)。

最终证书的 SHA-256 为

da4ef0eeac285da5cf32ad1372155dbb9d03917c18044b81b8236fac6e51107c，

完整产物清单的 SHA-256 为

fd2bece7381df111a03ad6f3a7585e8c442196f2772aebd3d5f50e2aa3422c53。

首个运行 43620409119 曾在读入旧 15726 位整数时遇到 Python 3.12 的 4300 位十进制解析限。它在首个新数学阶段之前失败；只在公开仓库执行 guard 后允许可信整数解析，得到本节绑定的核心版本。失败回执仍保留，没有丢弃已经完成的新阶段再重算。

## 3. 六个原输入没有替换或重算

以下 SHA 均由实际输入回执及最终配置绑定：

| 原输入 | SHA-256 |
|---|---|
| R735 原 CM state | 9cd5f6731c7cfa76cd118b5f3a8ab1efb12d0d69ba95ab08817fcb80c2073427 |
| R735 原 torsion modulus | 7063eacd17ffec4c68dea5d8c3a2cab278286653fd12aae07f1c955bb1ad94fb |
| R735 原 model certificate | 752aa03f9cbe7d3174a7c508fce3043e21e8e85fd087e01acc4bca82a5cbd574 |
| R738 原 cosets and markings | 6a73cb699abb5e53328a040ec86bea2c4cac7ef690a29984912c43417cfd0161 |
| R738 原 integral compact Manin cycles | d4dcbac16cc24cefd378fc7afea02fcd34b8043d255c1e84407ff7d21bd257cf |
| R745 原 six Hodge expansions | a629d550bd2f3102111bbb58fe707470081e2062da10221ab778fe3ba71b53dd |

原标记依旧为

$$
g(X)=400,\qquad c_1=4424,\qquad c_0=\{2876,2822,2823\}.
\tag{754.2}
$$

原模型、拓扑、torus 平均及已有 $L$ 值均没有重新生成。

## 4. 从原周期公式到实际完整约束

R751 从原有限右 slash 作用、原 tame 2/3 分量和原 CRT 逆元推导每条原边的准确周期。R754 按同一公式执行：

1. 在 R735 保留的 $K(U)$ 中求原 Miller 配对，保留正 $\xi=e^{2\pi i/41}$。
2. 通过原七次子域与六次角色塔形成同一周期线。
3. 保留 $P'=D_u(\Omega_0/p)$ 的原负实 $U$ 分支及实目标的 $-\zeta$ 运输。
4. 用七个完整有理 trace 泛函和四十个 $\xi$ 幂得到原 40 个归一加法周期。
5. 以原 Weyl/有限向量、原方向和全部分母形成 819 条原边的六个精确周期。

所有域运算都是有理系数商域中的精确运算。没有近似周期拟合、任意根选择、额外平均因子，或在复域数值结果后猜测代数系数。

令六个归一边微分的闭周期为 $\Pi_{ij}\in L$，$1\le i\le800$、$0\le j\le5$。待求微分写为

$$
h_v=\sum_{j=0}^5v_j\omega_j,\qquad
v_j=\sum_{t=0}^6x_{jt}b^t,\qquad x_{jt}\in K.
\tag{754.3}
$$

要求每条原闭周期属于 $K$，等价于

$$
[b^r]\sum_{j=0}^5v_j\Pi_{ij}=0,
\qquad1\le i\le800,\quad1\le r\le6.
\tag{754.4}
$$

$1,b,\ldots,b^6$ 是实际 $L/K$ 基，故 (754.4) 是充分且必要条件。它给出恰好 4800 行、42 列的 $K$ 线性系统，没有丢掉非恒定坐标。

实际源码按原闭链保存顺序处理全部行。每一新行先由既有准确主元消元；新非零行归一为主元一，再清除旧行的该列。完整阶段保存原独立行位置和约化行基。实际最后主元数为 36，所有 4800 行均已处理。因此

$$
\dim_K\ker(754.4)=42-36=6.
\tag{754.5}
$$

这不是在少量闭链上取到六维后便停止；其余全部行也已经精确消元。

## 5. 全部原闭链的第二次代回与整数周期

令实际自由列为六个位置。对每个自由列置一、其余自由列置零，再用准确约化行基求主元坐标，得到六个核向量。源码先逐约化行验证这些向量，再将其恢复为六个实际 $L$ 微分向量。

随后对每个向量、每条原闭链，重新在 $L$ 中计算 $\sum_jv_j\Pi_{ij}$。全部六个非恒定 $b$ 坐标都必须严格等于零，留下准确的

$$
a_{i\ell}+b_{i\ell}\zeta,\qquad a_{i\ell},b_{i\ell}\in\mathbf Q.
\tag{754.6}
$$

实际保存了全部 $800\times6$ 个有理坐标对，并对每个方向取所有分母的最小公倍数 $D_\ell$。对全部 800 条链再次检查

$$
D_\ell a_{i\ell},\quad D_\ell b_{i\ell}\in\mathbf Z.
\tag{754.7}
$$

因 R738 的 800 条链是完整整数同调基，(754.7) 保证 $D_\ell h_\ell$ 的所有周期都属于同一原目标格。于是以原 $c_0$ 为基点的积分定义真实代数映射到 $C$。它由微分和基点值唯一刻画，按 R732/R762 下降到原 $L$。

反过来，任何在该原六维正 Hodge 空间内、定义于 $L$ 的实际映射微分，其归一周期属于 $K$，故必满足 (754.4)。因此本次得到该原空间中完整的有理 Hom 核，没有遗漏额外 $K$ 方向。

这些结论没有给出完整整数周期格的基。不同方向的有理线性组合可能在上述逐方向清分母子格之外仍有整数周期。R759 必须对全部 1600 个有理整数条件求完整 HNF 双包含，不能只沿用六个 $D_\ell$。

## 6. 完整坐标保存及后继输入

全部精确坐标保存在公开 Actions artifact：

serre-global-R754-original-p41-periods-and-Hom-kernel-43620862489-1。

实际 artifact ID 为 14125735974，ZIP 大小 26339734 字节，ZIP SHA-256 为

9a58e842bc80654f77800f6e0db7f90655483e6c6469fc7791addb0db40c4ed1。

后继所用的关键完整文件是：

| 文件 | 字节数 | SHA-256 |
|---|---:|---|
| R754-exact-normalized-additive-periods.json.gz | 540739 | f424860b1e91b13ee133b2cc48509355cec58505712e0462a7a59f86968631dd |
| R754-original-relative-periods.json.gz | 10558658 | 510a6928725df736d29d812513110c8d2542f191d8ca9bfcf0feb14ac1931ec2 |
| R754-streamed-original-period-constraints.json.gz | 10262516 | c057408b0b3c218c4a33b3b2d526bb35d6c4bc920f885e2b8d8a0e6793c121f8 |
| R754-all-original-closed-period-verification.json.gz | 759454 | fc300cb79a3299bb896ce6ae5a1ec577248750692202d1993c27a69d3886672b |

全部十八个数学阶段的完整 SHA 在最终证书和全产物清单中，不只保存本表摘要。大可复现表没有提交到 Git。

R759 正式请求使用本次实际成功 run、source、artifact、完整 manifest SHA、最终证书与闭周期 SHA；旧 R738 同调交配仍直接复用。新任务只计算完整整数周期格、实际映射次数及原有界函数恢复输入，不重做本篇周期或 Hom 核。

原有理函数 $x,y$、原 $\beta=f(c_1)$ 坐标、真实高度 jets 和全 $p$ 排除尚未得到。本结论不改变主 README 的完成标准。
