# R1072：原 p47 全部 cuspidal 圆盘标签的认证有限结果

日期：2026-11-27（Asia/Taipei）。
会话：Astra-serre-24b8836b-20261126；root / global_route。

**已完成该有限计算。** 在完整原曲线 $X_{\rm ns}^+(47)$ 上，
全部 $235$ 个原 $\mathbf Q_{47}$ smooth 圆盘给出 $235$ 个彼此不同的
完整 cuspidal Kummer 全局候选向量。
实际 $V$ 恰有下述十个角色，且它们全部 Bernoulli-good：
$$
V=\bigoplus_{R\in\{26,28,30,32,34,36,38,40,42,44\}}V_{\omega^R}.
$$
每个角色保留 R1062/R1070 的原 cusp unit 与 R1069 的原
circular-unit 基，不是逐圆盘独立定标的向量。

这只认证全部原圆盘的标签及其互异性。
它没有证明每个圆盘内的有理点唯一，也没有完成 $p=47$ 有理点分类
或全 $p$ Serre 一致性。有效辅助素的同点完整向量排除继续。

## 1. 真实执行、固定来源和预算

- 公开 [run 45925829303](https://github.com/Rogerhu12/math-research-public/actions/runs/45925829303)，attempt 1；
- [job 140266778118](https://github.com/Rogerhu12/math-research-public/actions/runs/45925829303/job/140266778118)，名称 original_disks；
- source commit：91de38ca63948967904fc5a5a0d8f0a8717ca3ed；
- 数学程序：[original_p47_cuspidal_disks.py](../scripts/original_p47_cuspidal_disks.py)；
- 请求：[original-p47-cuspidal-disks-request.json](../notes/original-p47-cuspidal-disks-request.json)；
- 完整方法：[原 p47 cuspidal 全盘方法](../notes/2026-11-27-original-p47-cuspidal-disks-method.md)。

源码 SHA-256：
35a0035d4f238670309d19c9acec35b5f9610cf13f5676f96503c59048148f98。
请求 SHA-256：
6aca75b3cd8229709db915fabf426194a6faa181aa3c7416883c39a70840745b。
方法 SHA-256：
746f7cf39f649eb3805467c32e8d6b094b83fdb8cf47dd0fd391ec9200e1a658。

请求还固定两 README 和 R1062/R1069/R1070/R1071 的 SHA-256；
consumer 在导入算术前核实际 Actions 环境、仓库、所有 pins 和 source。
原算法及相位证明来自 [R1071](R1071-original-p-local-cuspidal-label-polynomials.md)
§§11–15，不由这次运行的数值结果反推。

单 job 预算 $600$ 秒，预留 $30$ 秒；算术回执耗时
$0.208807431$ 秒，状态 complete，全部预算内完成。
依赖为 python-flint 0.9.0，计算只用 exact modular arithmetic；
浮点数只用于 elapsed-time 元数据。
本地和 code-mode 没有执行这些数学程序。

## 2. 全部原角色与所有 supersingular 输入

实际角色按 R1062 的原
$S_\psi=-J(\psi,\eta)B_{2,\psi^2}/4$ 判定。
程序枚举全部偶角色，不仅预放 forced 列表。
广义 Bernoulli 的 $p$ 分母先保 Teichmuller lifts 模 $p^2$ 后处理；
$R=24$ 的 pole 特例按 R1070 §10 单独消去。
所列十个实际角色之外没有额外 $V$ 分量，
且各自普通 $B_R\bmod47$ 都非零。

实际角色回执 SHA-256：
880799848773da716df2dd4b5db76c07fcc0027e281baff963aff0eeeaf82014。

全部 $\mathbf F_{47}$-rational supersingular $j$ 是
$$
j=0,\ 9,\ 10,\ 36,\ 44,\qquad 36\equiv1728\pmod{47}.
$$
每一 $j$ 均由原 Hasse coefficient 判定，并以实际 trace-zero 点计数复核。
同一个 Cartan 模型始终为
$\mathbf F_{47^2}=\mathbf F_{47}(s)$、$s^2=5$；
原 smoothing integer 始终是 $c=5$。

下表的 $\gamma$ 是各模型真实 normalized Miller pairing 的
$h^{48}$ coefficient，$h^{2208}=47$；
不能将这些不同值统一改成一。

| 原模型 $y^2=x^3+Ax+B$ | $j$ | 原 $\gamma$ | fine 标签像大小 | 原 coarse 处理 |
|---|---:|---:|---:|---|
| $(A,B)=(0,1)$ | 0 | $20s$ | 47 | $t\mapsto t^3$ 在 $\mathbf F_{47}$ 双射 |
| $(1,32)$ | 9 | $20s$ | 47 | 全部 47 个 $t$ |
| $(12,8)$ | 10 | $26s$ | 47 | 全部 47 个 $t$ |
| $(1,0)$ | 36 | $11s$ | 24 | 按 $t\sim-t$ 商 |
| $(5,0)$ | 36 | $10s$ | 24 | 第二 quartic twist，按 $t\sim-t$ 商 |
| $(7,36)$ | 44 | $31s$ | 47 | 全部 47 个 $t$ |

两个 $j=36$ 模型的中心向量准确相同；
两个 $t=0$ 只计一次，其他原 coarse 点不重复。
因此它们合起来恰给 $47$ 个 coarse 圆盘，
总数是 $5\cdot47=235$。
不把两个 fine 模型的 $94$ 行当作 $94$ 个原点。

## 3. 原有限多项式与独立校验

每个 reference 用同 marked first lift 模 $47^2$。
形式对数只读至 $2113<47^2$；
在 $47$ 整除积分分母处先保模 $47^2$ 再除 $47$。
程序完整核原 Weierstrass 方程、invariant differential 和全部所需
$p$-block，并用 R1071 的原 residue 式读取 $A_d$。

真实相位用 normalized Miller lines、末步 vertical 和原 $(-1)^p$；
逐模型核全部低于 $h^{48}$ 的消失、$\gamma\ne0$、
$\gamma^{46}=-1$ 与真正双线性
$\gamma(P,2Q)=2\gamma(P,Q)$。
然后才按原 $b_\chi$ 归一，并使用 R1071 §14 的已付跨模型相位运输。

按 $R=26,28,\ldots,44$ 顺序，实际 fine 多项式次数如下：

| $j$/模型 | 十个原角色的实际 degree |
|---|---|
| 0 | $21,18,15,15,12,9,9,6,3,3$ |
| 9 | $21,19,17,15,13,11,9,7,5,3$ |
| 10 | $21,19,17,15,13,11,9,7,5,3$ |
| 36，两 twists 各自 | $20,18,16,14,12,10,8,6,4,2$ |
| 44 | $21,19,17,15,13,11,9,7,5,3$ |

所有 $j=0$ 的非三倍数系数，以及 $j=36$ 的奇次系数准确为零；
并非只核多项式的最高项。
Lucas 消去的其余形式项也逐项核二项式为零。

一个独立纸面校验是原 $j=0$ 的
$$
x(T)=T^{-2}+\sum c_nT^{6n-2},\qquad
c_1=-1/7,\quad
c_n=\frac{\sum_{a+b=n}c_ac_b}{(n-1)(6n+1)}.
$$
此原 ODE 路径给 $c_7=39$，故 $A_{42}=31\bmod47$；
本次 division-polynomial/residue 路径独立核得同值。
于是 $R=44$ 的原 cubic 斜率是 $5/b_{\omega^{44}}\ne0$，
所以在 $j=0$ coarse component 上，单这一角色就区分全部 47 个圆盘。
此校验不是旧 $f_N$ 或旧最低泛函的重新计算。

## 4. 全部共同向量的比较及准确证书范围

每个 coarse 圆盘只生成一个完整十维向量。
在这一个向量层面分组后，回执是
$$
\#\{\text{原 coarse 圆盘}\}=235,\qquad
\#\{\text{完整 global 候选向量}\}=235.
$$
全部纤维重数为一，collision class 数为零。
这同时包含不同 supersingular components 之间的比较，
不是只在每个模型内部做 injectivity。

完整 coarse-point 列表 SHA-256：
12025eb9c76692312c856360add6a4702cbe02ccaf51def477bafeaf5e06d1ee。
碰撞类 SHA-256：
4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945。
全部 payload 为 41027 bytes，SHA-256：
c661d8b06440067ef5a60894a5decfbfd81ca70b9b76b79a409eb5c136ae39e7。

各完整模型记录的哈希是：

| 模型 | SHA-256 |
|---|---|
| $j=0$ | 72f5a15ef4516cc79361d30d5836e4773e01e41d5f54b9f9efcdcc76ac4227b9 |
| $j=9$ | 001a88cc8d66fd94ac3b0f9e6e8a2ff82d91db2f24fcb8ca75570c7c9586bea9 |
| $j=10$ | 69154bb4db6bc80938e0a20b270b8fd307171f39fd50248520fbfdf787222342 |
| $j=36,(A,B)=(1,0)$ | f0c5a336ce0da12661b77d3ecfc371ac659309ff4daf06567ac999d2112e697d |
| $j=36,(A,B)=(5,0)$ | 88e4b3d6ee2d3bedf33029fc858a0751bcfb1755149cc30d5d65c03dd53ddcef |
| $j=44$ | bd9de168294f8bfc828d6a4b264ae08c928612e129df8a6bc6c748e12178d311 |

可重算的 coefficients、vectors 和碰撞数组仅留 runner scratch；
没有上传 artifacts、Release 或提交这些 raw arrays。
原程序、参数、真实运行与哈希足以重建供后继新筛选消费的输入。

按 R1067/R1069，每个全局有理点的完整原标签必属于这些候选。
按 R1070，$47$ 为 safe prime，只有 $\ell\equiv1\bmod47$ 的辅助素
对完整 $V$ 可见。下一实际输入是这类素处同一个原点的全部角色标签，
并须包括可约化到 cusp 的情形。
本结果不把“候选数有限”或“标签互异”当作有理点分类。
