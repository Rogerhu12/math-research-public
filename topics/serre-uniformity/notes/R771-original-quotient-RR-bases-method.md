# R771：原商曲线 146／694／1514 维基的公开有限秩计算方法

日期：2026-11-14。状态：**预运行方法。** 本任务把已经证明的 R767 生成定理落实为原群上的具体 Eisenstein 配方、乘积基和非零有限域小行列式。本文没有预称计算已成功，没有预称已得到原映射的 $y$、$\beta$ 或实际高度。

使用原 $p=41$、$Y=X_1/\mu_3$、$t=a^3$、$K=\mathbf Q(\zeta)$、$s=\sqrt{-3}=1+2\zeta$、原参考 cusp 与
$$
q_Y=Q^3=e^{2\pi i\tau/82}.
$$
保持原 $c_1=4424$、$c_0$ 轨道和 R738／R745 的相位。程序不重新运行原拓扑、周期、Hom 核、整数格或映射次数。

## 1. 已存在的输入与本次真正执行的内容

理论输入是 [R767](../results/R767-original-quotient-low-weight-RR-basis-and-cusp-order-bound.md)，SHA-256 为
$\,\mathtt{33fb32458eaf62e1499de092b6139672304ceefe096eef4a5253a2d7637a940d}\,$。
它已经证明 $g(Y)=127$、20 个宽度 82 的 cusp，以及
$$
\mathcal L=K_Y+\mathcal D,\quad \deg\mathcal L=272,\qquad
h^0(\mathcal L)=146,\quad h^0(r\mathcal L)=272r-126\ (r\ge2).
\tag{771.1}
$$
程序仅读取下列已公开的小证书。

| 证书 | 原公开 run | SHA-256 |
|---|---:|---|
| R745 原 Hodge 输入 | 43616027318 | 7fdac934ab8be401afbe793c9dd6d790bba2dc1f39cdbb134fc51748870816be |
| R759 原整数格与次数 | 43625474728 | 7c2c611b9a5f43bc3a2a0007bf2cb5dd2fa8d10f133b663dbca0d054e1515de0 |

R745 的真实参考 cusp 六行指数是 $1,4,7,13,16,19$，在 $\ell=739$、$\xi_{41}=538$、$s=98$ 的行列式为 407。这里读取该结论，不重新计算它。R759 第 4 号原整数格基映射的实际次数是 1206，不声称其全局最短。

本次新的算术全部在公开仓库 GitHub Actions、Python 3.12、python-flint 0.9.0 中执行：

1. 按下节原群生成权一 Eisenstein 级数的有限表；
2. 逐个选出 146 个真实权二迹配方，输出实际非零小行列式；
3. 用原权二基的普通乘积选出各个 $H^0(r\mathcal L)$ 基；
4. 逐层补足两个椭圆点的主部，分别达到真实 $M_6$ 的 694 维与 $M_{12}$ 的 1514 维；
5. 保存所有精确符号配方、已算模 739 系数与完整来源；不将这些模系数猜测提升为特征零系数。

## 2. 原 level-82 群及配方完备性

取
$$
C=\begin{pmatrix}0&1\\1&1\end{pmatrix}\pmod2,\qquad
J=\begin{pmatrix}-1&-1\\0&1\end{pmatrix}\pmod{41},
$$
$$
T_{\pm}=
\left\{
\begin{pmatrix}a&-b\\b&a+b\end{pmatrix}:
a^2+ab+b^2=\pm1
\right\}.
$$
原 $\Gamma_Y$ 在模 82 的像为 CRT 群
$$
H_{82}=\langle C\rangle\times
\bigl(T_+\ \cup\ J T_-\bigr)\subset\operatorname{SL}_2(\mathbf Z/82).
\tag{771.2}
$$
两范数纤维各有 42 项，故模 41 部分有 84 项，$|H_{82}|=252$。程序对每个矩阵核对行列式为 1，并保留全部矩阵。$-I$ 在群内，故迹可通过 126 个 $\{\pm I\}$ 代表计算。

令
$$
\mathcal A=\{(a,b)\in(\mathbf Z/82)^2:(a,b)\not\equiv(0,0)\pmod{41}\}.
$$
被去掉的四项是零点与三个二挠标签，原奇权 Eisenstein 级数均为零。$\mathcal A$ 的 6720 个标签在 $H_{82}$ 下有 40 个轨道；程序保存实际轨道代表、矩阵与全部 3360 个标签模 $\pm1$ 的代表。

对标签 $\lambda,\mu$ 定义特征零模形式
$$
B_{\lambda,\mu}
=\frac12\sum_{g\in H_{82}}E_\lambda E_\mu\mid_2g
=\sum_{g\in H_{82}/\{\pm I\}} E_{\lambda g}E_{\mu g}.
\tag{771.3}
$$
作用是原行标签的**右作用**，而不是把两坐标或逆矩阵无说明地交换。$E_{-\lambda}=-E_\lambda$，所以半迹等式保留所有符号。

R767 所引用的 Khuri-Makdisi Theorem 5.1 适用于 full level $82\ge3$ 的所有权重 $k\ge2$，包括权二；它仅不声称权一尖点形式由 Eisenstein 生成。取有限群不变部后，所有 (771.3) 张成原 $M_2(\Gamma_Y)$。对于任意第一标签，先以一个 $g_0\in H_{82}$ 搬到其已保存轨道代表，第二标签同时右乘 $g_0$；迹的求和集合不变。第二标签改负号只给整个配方乘 $-1$。因此 40×3360 个候选覆盖全部张成空间，而不是随机截取某一部分轨道。

程序按可逆排列
$$
j\longmapsto 65537j+17\pmod{134400}
$$
逐一读取该有限集合；此排列仅改变枚举顺序，不改变配方集合。成功所需的是**实际达到秩 146**。若本次良素数或预算未使这点完成，保存当前独立配方和候选游标，明确报告未完成。

## 3. 原权一 Fourier 公式与有限域 specialization

取解析方向
$$
\xi_{41}=e^{2\pi i/41},\qquad
\xi_{82}=e^{2\pi i/82}=-\xi_{41}^{21}.
$$
使用 Zywina Lemma 4.7 的原归一：
$$
E_{a,b}
=c_0(a,b)
+\sum_{\substack{m,n\ge1\\m\equiv a\ (82)}}\xi_{82}^{bn}q_Y^{mn}
-\sum_{\substack{m,n\ge1\\m\equiv-a\ (82)}}\xi_{82}^{-bn}q_Y^{mn},
\tag{771.4}
$$
其中
$$
c_0(a,b)=
\begin{cases}
0,&a=b=0,\\
\dfrac{1+\xi_{82}^b}{2(1-\xi_{82}^b)},&a=0,\ b\ne0,\\
\dfrac12-\dfrac a{82},&0<a<82.
\end{cases}
\tag{771.5}
$$
两个带符号的整除和都保留，$m\equiv0$ 从 $m=82$ 开始。程序生成全部 $82^2$ 条有限级数至 $q_Y^{1640}$，并核查四个被去掉的标签确为零、所有标签满足奇性。

专用有限域点为
$$
\ell=739,\quad \xi_{41}\mapsto538,\quad
\xi_{82}\mapsto-538^{21},\quad s\mapsto98.
\tag{771.6}
$$
程序核对所需根阶与 $98^2=-3$。由于 $82\mid738$，该 specialization 保持原始 82 次根；$2$、$82$、$144$ 和全部 $1-\xi_{82}^b$（$b\ne0$）均为这个局部环的单位。故 (771.4)、(771.5)、(771.3) 及后述乘积的所有系数都可合法约化。

每一行始终附带**特征零的符号配方**。若一组配方在模 739 的系数矩阵中有非零小行列式，则其特征零行列式也非零，因而该组配方在特征零线性无关。结合已证明的维数，才能称其为特征零的完整基。单个模系数本身并不是重建出的特征零系数；本任务明确不做这种未经界限的提升。

权二检查使用指数 $0,\ldots,273$；$H^0(r\mathcal L)$ 使用 $0,\ldots,272r$。这些前缀至少达到相应线丛的次数，所以零前缀不可能隐藏一个非零截面。对于实际非零 minor，独立性本来就不要求额外的 Sturm 假设；次数界同时解释了完整基的有限可识别性。

## 4. 从 146 维权二基得到普通乘积基

$\deg\mathcal L=272>2g(Y)+1$，R767 已证明普通乘法的正常生成。程序从所选 146 个配方出发，依次枚举
$$
B_i\,F_j^{(r-1)},\qquad
0\le i<146,\quad 0\le j<h^0((r-1)\mathcal L),
\tag{771.7}
$$
直至实际达到以下秩。

| $r$ | 1 | 2 | 3 | 4 | 5 | 6 |
|---:|---:|---:|---:|---:|---:|---:|
| $h^0(r\mathcal L)$ | 146 | 418 | 690 | 962 | 1234 | 1506 |

$r=2$ 仅去掉交换所得的重复候选 $j<i$。其余所有原乘积都在有限枚举内；没有预设某两个选定截面构成无基点 pencil。每个新配方保存左右因子的原索引及整条模 739 级数，后续可以按这个表达式在特征零展开。

为保证保存的是**原候选配方**，选基时对行矩阵的转置作 RREF，取其主元列对应的原候选行，而不是把有限域消元系数误作特征零线性组合。每次批次保留此前全部已选独立行。完成某空间后，另从原行矩阵选出系数列，计算并保存那个真正的方阵行列式。

## 5. 椭圆点补方向、分母和最终 RR 基

原两个椭圆点记为 $P_0$、$P_1$，分别位于 $t=0,1$。R767 已保留它们的真实主部和 $s$ 相位，证明
$$
M_6=H^0(3\mathcal L)+E_4H^0(\mathcal L)
+\langle E_6,\eta_{\rm Ded}^{12}\rangle,
\tag{771.8}
$$
$$
M_{12}=H^0(6\mathcal L)+E_4H^0(4\mathcal L)
+E_6H^0(3\mathcal L)+E_4E_6H^0(\mathcal L)
+\langle E_6^2,E_6\eta_{\rm Ded}^{12}\rangle.
\tag{771.9}
$$
这些是空间之和，不把其中重叠部分当成直和。程序从已有普通乘积基开始，在 (771.8) 的每层实际增加 2 维，得到 690→692→694；在 (771.9) 每层实际增加 2 维，得到 1506→1508→1510→1512→1514。每层都算出非零 minor，而不是只记录理论期望。

采用原参数的标准展开
$$
E_4=1+240\sum_{n\ge1}\sigma_3(n)q_Y^{82n},\qquad
E_6=1-504\sum_{n\ge1}\sigma_5(n)q_Y^{82n},
$$
$$
\eta_{\rm Ded}^{12}=q_Y^{41}\prod_{m\ge1}(1-q_Y^{82m})^{12}.
\tag{771.10}
$$
程序在已保存前缀核对 $E_4^3-E_6^2=1728\eta_{\rm Ded}^{24}$。原
$$
t=\frac12-\frac{sE_6}{144\eta_{\rm Ded}^{12}}
$$
给出
$$
D_*:=t^2\Delta
=\left(\frac{\eta_{\rm Ded}^{12}}2-\frac{sE_6}{144}\right)^2,
\qquad D_*(0)=-\frac1{6912}.
\tag{771.11}
$$
这里 $\eta_{\rm Ded}$ 不是映射恢复中 $h/a$ 所记的微分。R767 的原除子恒等式为
$$
\operatorname{div}_{6\mathcal L+4P_0+4P_1}(D_*)=2(t)_0.
$$
因此若公开计算实际完成了 1514 个 $F_i\in M_{12}$，则
$$
\left\{\,\frac{F_i}{D_*}:1\le i\le1514\,\right\}
\tag{771.12}
$$
就是原 $\mathcal L(2(t)_0)$ 的具体特征零基。所存配方的系数域为 $\mathbf Q(\xi_{82})$，置于原 $M=K(U)$；(771.11) 的 $s$ 使用同一 $K$ 嵌入。此处不预称完成了进一步向 $K$ 或原 $L$ 的算术下降。

M6 的 694 维基也同时保存，供若日后实际找到 $d\le693$ 的映射时使用。对 $D=(t)_0$，RR 只立即给出
$h^0(D-(y)_\infty)\ge694-d$；**只有 $d\le567$ 时**，由次数严格大于 $2g-2=252$ 才可直接写成等号。本任务没有将现有 $d=1206$ 的非特殊除子结论机械移到新的次数。

## 6. 与真正映射恢复的精度接口

本次只生成用于选基的模 739 前缀至 1640。对当前已经实际存在的 $d=1206$ 映射，下一步的特征零展开仍须做到 R767 已证明的完整精度：
$$
F_i/D_*\text{ 至 }q_Y^{2846},\qquad
h/dQ\text{ 至 }Q^{8557}.
\tag{771.13}
$$
真实尖点阶 $e\le19$ 来自未重算的 R745 六行系数证书。实际求解时读取该映射的真实 $e$，在
$$
-e\le n\le2846-e
$$
的全部 2847 个系数上求解 $A-yB$。R767 已证明这强迫全局恒等式；$\deg(2(t)_0-(y)_\infty)=434>252$，故该实际 $d=1206$ 系统的预期核维数 308 有理论依据。**本次 R771 不执行这个特征零核，不预称其实际返回。**

## 7. 文件、断点与公开执行

核心文件为
`scripts/R771_original_quotient_RR_bases.py`；
公开包装为
`scripts/R771_public_quotient_RR_bases.py`；
请求为
`notes/R771-public-quotient-RR-bases-request.json`；
workflow 为
`.github/workflows/serre-p41-quotient-rr-bases.yml`。

首次运行只读取仓库中已存在的两个小证书，不下载或重算旧大表。全部新的算术由核心的公开仓库守卫限制在本仓库 Actions。请求固定 source SHA、方法 SHA、R767 SHA、实际输入 SHA、flint 版本、辅助素数和截断。

Eisenstein 表按第一坐标分成 82 个 gzip 检查点；完成一行后立即原子保存。普通选基按批次保存原配方、系数、当前秩及候选游标；乘积空间和主部层各自保存完整阶段。一致配置的完成阶段在续算时直接解码，不重复求基或重算 minor。中断时至多舍弃尚未保存的一个批次，已有完整及部分阶段全部保留。

默认数学预算为 80 分钟。达到预算、异常或秩不足都不注册成功结论，而是保留错误凭据、日志、当前阶段及全部 SHA，供同一配置的后续 Actions 续算。包装不以增加临时预算假装任务已完成；真实成功门是 146、694、1514 的全部实际非零 minor 和对应阶段文件一致。

全部可复现的 Eisenstein 系数表、乘积表和各阶段基状态只上传 artifact。Git 仅保存小输入凭据、运行凭据、核心凭据、小最终证书、短日志和完整文件 SHA 清单。小最终证书保存 146 个原种子、三个最终实际 minor、各阶段 SHA 与明确的尚未计算项。失败时同样保留完整 artifact 和小失败凭据。发布复用仓库已有的 `p41_public_actions_recovery.py`，其推送前会检查两个 README 的差异并使用既有非快进重试流程。

## 8. 原始依据

- [Khuri-Makdisi, Moduli interpretation of Eisenstein series](https://arxiv.org/pdf/0903.1439)，Theorem 5.1：full level $N\ge3$、所有权 $k\ge2$ 的生成结论；不是只对高权，也不是生成全部权一尖点形式。
- [Zywina, Explicit open images for elliptic curves over Q](https://pi.math.cornell.edu/~zywina/papers/ExplicitOpenImage.pdf)，Lemma 4.7、Theorem 4.9、Corollary 4.10：原权一 Fourier 公式、标签右作用、权二乘积的 cyclotomic 结构。
- [python-flint 0.9.0 nmod_poly](https://python-flint.readthedocs.io/en/latest/nmod_poly.html) 与 [nmod_mat](https://python-flint.readthedocs.io/en/latest/nmod_mat.html)：本次仅使用确定的 `mul_low`、`truncate`、`left_shift`、`rref`、`transpose` 和 `det` 接口。
