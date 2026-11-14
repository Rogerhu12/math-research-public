# R182：原始 Mellin 列的 Möbius 算子、十二阶旋转块与真实好特征核

日期：2026-11-13。

**状态：已证明的精确算子化及真实有限域边界；未解决单个原始类型的共同非零。**

本文接 R174/R177 和 `2026-11-13-composite-m-weil-character-matrix.md`。
它把合数 m 的原始 Mellin 列写成一个完整的 Weyl 算子；对 m=2^a，
给出准确的两个 cubic 非对角块，并在一个固定的、已处理过的层 p=47 上，
严格否证“这些方块在所有实际 Tate 特征下自动可逆”。
该反例不使实际两行共同消失，也不否证原始类型共同非零的目标。

本文不新增中心值非消失或秩零假设。将有限行用于实际分母时，
仍须保留 R169/R172/R173/R181 的真实有理投影及 Q 点有限前提。

## 1. 同一个有限 Cartan、实际频率与系数环

保留小惯性分支

$$p>37,\qquad p+1=6m,\qquad 3\nmid m.$$

固定同一个实际加性角色 $\psi$、非零频率 $a\in\mathbf F_p^\times$ 及 R177 的 Weyl 算子
$D_v$。令 $C$ 是阶 $6m$ 的非分裂 Weil Cartan，取生成元 $g$，
其在二维加法空间上的旋转为 $v\mapsto\nu_gv$。
令

$$B=C[6],\qquad H=C^3,\qquad
Q_1=\sum_{\kappa\in\mu_6}D_{a\kappa}.$$

记 $K_c$ 为 C 的 Weil 作用，$P_H$ 为 H 不变投影。
所有等式先在

$$\mathcal O=\mathbf Z[\zeta_{p(p+1)},1/(p(p^2-1))]$$

上成立，继而可在任一好特征 $\ell\nmid p(p^2-1)$ 及任一固定剩余嵌入下约化。
没有移动实际频率或指定剩余素理想。

R177 已证明：$P_H$ 是整幂等元，所有这些约化中的秩均为 2，
且像在 odd Weil 部分。C 的各非平凡特征投影 $\Pi_j$ 均秩一，
平凡投影为零。若 $\xi$ 为阶 $6m$ 的根，则

$$P_H=\Pi_{2m}+\Pi_{4m}.$$

在 $P_HQ_1$ 的两行中，可能非零的列分别为

$$j=i+6k\pmod{6m},\qquad
i\in\{2m,4m\},\quad k\in\mathbf Z/m\mathbf Z.\tag{182.1}$$

两个列集合不相交。R174 的同一 Cartan 参数核算将原始 $\theta$ 轨道
精确识别为 $(k,m)=1$；旧 Steinberg 两行识别为 $k=0$。

## 2. 全部精确阶的 Möbius 算子

对每个 $s\mid m$ 定义

$$Q_s=\frac1s\sum_{\kappa\in\mu_{6s}}D_{a\kappa}.\tag{182.2}$$

**定理 182.1。** 对任意 $e\mid m$，置

$$\mathcal R_{e,m}
=\sum_{s\mid e}\mu(s)Q_{(m/e)s}.\tag{182.3}$$

则 $P_H\mathcal R_{e,m}$ 恰为 $P_HQ_1$ 中满足
$\operatorname{ord}(k\bmod m)=e$ 的所有列，其他列为零。
特别

$$\boxed{\mathcal R_m:=\mathcal R_{m,m}
=\sum_{s\mid m}\mu(s)Q_s} \tag{182.4}$$

准确提取全部原始 Mellin 列，而 $\mathcal R_{1,m}=Q_m$ 提取旧两行。
因此原始列及旧行共同消失，准确等价于

$$P_H\mathcal R_m=0,\qquad P_HQ_m=0.\tag{182.5}$$

**证明。** 对 $s\mid m$，令 $h_s=g^{m/s}$，其阶为 $6s$。
Q1 被 B 共轭固定，故

$$\frac1s\sum_{u=0}^{s-1}K_{h_s}^uQ_1K_{h_s}^{-u}=Q_s.\tag{182.6}$$

左侧每个旋转六边形不重复；其并恰为 $a\mu_{6s}$。
在 (182.1) 的矩阵元上，平均因子为

$$\frac1s\sum_{u=0}^{s-1}\exp\left(-\frac{2\pi i ku}{s}\right)
=\mathbf1_{s\mid k}.$$

这是整根和等式，降到好特征仍成立，不使用复绝对值。
因此 (182.3) 在第 k 列的因子为

$$\mathbf1_{m/e\mid k}\sum_{s\mid(k/(m/e),e)}\mu(s)
=\mathbf1_{\operatorname{ord}(k)=e}.$$

这证明全部断言。证毕。

旧行在这里确为等价条件，而不只是一个方向。若 $\chi$ 是 C 的两个
三次字符之一，直接用 $\operatorname{Tr}(K_tD_a)=-\psi(ta)$ 得

$$\Pi_\chi Q_m\Pi_\chi
=-\frac1m\left(\sum_{t\in\mathbf F_p}\chi(c_t)^{-1}\psi(ta)\right)\Pi_\chi.$$

括号就是同一实际根下的两条旧三色和之一（两个标签可能互换）。
由于 m 是单位，$P_HQ_m=0$ 准确等价于这两条旧行都为零。

这些列投影互不相交，并满足

$$P_HQ_1=\sum_{e\mid m}P_H\mathcal R_{e,m}.\tag{182.7}$$

也可将原始算子写成 Ramanujan 和形式：

$$\mathcal R_m
=\frac1m\sum_{u=0}^{m-1}c_m(u)
\sum_{\kappa\in\mu_6}D_{a\nu_g^u\kappa},\qquad
c_m(u)=\sum_{t\mid(m,u)}t\mu(m/t).\tag{182.8}$$

(182.8) 只是 (182.4) 的重新分组，没有补入缺失的非原始字符。

## 3. 素数幂时是一个旋转差问题

设 $m=r^b$，其中 r 为素数。由 Möbius 函数直接得到

$$\mathcal R_m=Q_1-Q_r.\tag{182.9}$$

原始列消失等价于 $P_HQ_1$ 仅保留 $r\mid k$ 的列。
它也等价于

$$[P_HQ_1,K_{g^{m/r}}]=0.\tag{182.10}$$

确实，(182.1) 的列与行在这个旋转下的特征比为
$\exp(2\pi i k/r)$，故交换子准确消去且仅消去 $r\mid k$ 的列。
这仍不是 $P_HQ_1=0$。

加上旧行消失后，所余的精确阶是

$$r,r^2,\ldots,r^{b-1}.$$

因此 R177 的 full-type 单位理想仍只保证其中至少一个精确阶可检测，
没有把它指定为最高阶 $r^{b-1}$ 或任一个固定阶。

## 4. m=2^b 的准确十二阶反变块

现在设 $m=2^b$。在本题 $p>37$ 的范围，$b\ge3$；以下代数对
$b\ge1$ 同样成立。令

$$h=g^{m/2},\qquad \nu=\nu_h,\qquad \operatorname{ord}(h)=12,$$

并置

$$R=Q_1-Q_{\nu a},\qquad
Q_{\nu a}=\sum_{\kappa\in\mu_6}D_{\nu a\kappa}.
\tag{182.11}$$

由于 $\nu^2\in\mu_6$，

$$2\mathcal R_m=R,\qquad
K_hRK_h^{-1}=-R.\tag{182.12}$$

所以原始列消失准确等价于 $P_HR=0$。

### 4.1 两个实际 cubic 块

在 odd Weil 空间内，$K_{h^2}$ 的三个特征值是 $1,\beta,\beta^2$，
其中 $\beta$ 为三次单位根。对其两个非平凡特征块，可分别选择一个
三次根 $\gamma\in\{\beta,\beta^2\}$，使该块分为

$$E_\gamma\oplus E_{-\gamma},\qquad
E_\gamma=\ker(K_h-\gamma),\qquad
\dim E_\gamma=\dim E_{-\gamma}=m/2.\tag{182.13}$$

两种 $\gamma$ 给两个不同的 cubic 块；$K_{h^2}$ 在其中的特征值为
$\gamma^2$。这些维数由 C 的完整特征列直接数出：h 的特征指数
为 $4,8,10,2\pmod{12}$，每个出现 $6m/12=m/2$ 次，且没有被删去的
平凡 C 列。

由 (182.12)，R 在每个块中具有形状

$$R=\begin{pmatrix}0&A_\gamma^{\dagger}\\A_\gamma&0\end{pmatrix}.
\tag{182.14}$$

这里 $\dagger$ 为非退化双线性 Gram 形式的伴随，而不是改变指定剩余
素理想的复共轭。R177 的标准 Schrödinger 基中，$K_c$ 与 $Q_s$ 均对称：
$D_{x+y\tau}^{\mathsf t}=D_{-x+y\tau}$，各范数圆和各 $a\mu_{6s}$ 对此反射
稳定。因此两个矩形块互为伴随，秩相同。特征投影的整幂等分解保证
Gram 形式在好局部环上非退化；不从一个模 $\ell$ 的迹来推秩。

实际 $P_H$ 的两条直线分别位于 $E_\beta$ 与 $E_{\beta^2}$。
故所需问题是

$$\operatorname{im}(P_H)\subseteq\ker R\quad\text{是否可能。}\tag{182.15}$$

仅知道 $A_\gamma$ 奇异不足以得到 (182.15)；仅知道某处有一个单位列也
不足以排除指定两条直线。

### 4.2 不可遗漏的平凡 B 块

第三个 odd 块的维数为 $m-1$，在 $K_h$ 的特征值 $1,-1$ 下的维数为
$m/2-1,m/2$。R 仍交换这两部分，所以该块无论特征零还是好特征，
都至少有一维核。

这解释了为何不能套用“整个 R 可逆”的论证。实际两条 H 直线位于
另外两个 cubic 块，不能用这个必有的平凡块核替代它们。

### 4.3 实际 Tate Frobenius 没有补齐精确阶

实际分母素数满足 $\ell\equiv s\pmod p$，$s\in\{1,-1\}$。
复合矩阵笔记已证明：固定该剩余嵌入，Frobenius 在列标签上作用为
$k\mapsto s\ell k$，并按 $s\ell\pmod3$ 保持或交换两条 cubic 行。
它保持 $\gcd(k,m)$，因而保持每个精确阶。

行交换时，两个行支撑不交且总非零确迫秩二；但这既不把非原始列
变成原始列，也不保证两个 $A_\gamma$ 可逆。

## 5. 一个真实 Tate 特征中的奇异方块

**定理 182.2。** 存在满足全部好特征及实际 Tate 同余条件的

$$p=47,\qquad m=8,\qquad \ell=1409\equiv-1\pmod{47},$$

使 (182.14) 的一个真实 cubic 方块奇异，但 $P_HR$ 的秩仍为 2。

这不是对原始列共同非零的反例，只是否证所有方块自动可逆。

### 5.1 全部数据

本例取实际频率 $a=1$。在 $\mathbf F_{47^2}=\mathbf F_{47}(i)$ 中取 $i^2=-1$，并取

$$\nu=6+24i,\qquad \nu^{12}=1,\quad\nu^6=-1.$$

系数域取

$$k=\mathbf F_{1409}[\xi]/(\xi^2+724\xi+1),\qquad
\psi=\xi^3,\qquad\beta=\xi^{47}.\tag{182.16}$$

该二次多项式不可约；$\xi$ 的阶恰为 141，故 $\psi$ 的阶为 47，
$\beta$ 的阶为 3。固定 (182.16)，不在不同剩余嵌入之间移动。

用标准基 $e_j$，$j\in\mathbf F_{47}$，明确取

$$D_{x+yi}e_j=\psi^{2xy+4yj}e_{j+x},\qquad
K_t=-\frac1{47}\sum_{v\in\mathbf F_{47^2}}\psi^{tNv}D_v,\qquad
K_\infty=1.\tag{182.17}$$

参数关系为 $\nu_t=(t-i)/(t+i)$。
R 与其投影均由这些公式直接生成，不调用数值特征向量或近似值。

对 $\gamma\in\{\beta,-\beta,\beta^2,-\beta^2\}$ 取

$$\Pi_\gamma=\frac1{12}\sum_{j=0}^{11}\gamma^{-j}K_{\nu^j}.$$

完整精确行约化给

| $K_\nu$ 特征值 | $\operatorname{rank}\Pi_\gamma$ | $\operatorname{rank}(R\Pi_\gamma)$ |
|---|---:|---:|
| $\beta$ | 4 | 3 |
| $-\beta$ | 4 | 3 |
| $\beta^2$ | 4 | 4 |
| $-\beta^2$ | 4 | 4 |

取同一范数一群的生成元 $g=37+29i$，其阶为 48，$g^4=\nu$，
$H=\langle g^3\rangle$。这与 §4 的 $h=g^{m/2}$ 完全对齐。
同时有

$$\operatorname{rank}P_H=2,\qquad
\boxed{\operatorname{rank}(P_HR)=2.}\tag{182.18}$$

$E_\beta$ 的核线在 H 不变空间上的投影非零，但该核线本身不是
H 不变线；$E_{-\beta}$ 的核线在 H 不变空间上的投影为零。
这说明“核有非零 H 投影”也不能替代 (182.15)。
此例 $s=-1$ 且 $s\ell\equiv1\pmod3$，实际剩余 Frobenius 保持两条
cubic 行；它不迫两个不同的 cubic 方块同时奇异。

### 5.2 独立标准库证书

配套文件：

- `verify_r182_mobius_and_order12_blocks.py`；
- `r182_mobius_order12_block_certificate.json`。

核验器仅用 Python 标准库。它自行检验 47、1409 的素性、Tate 同余、
二次域不可约性、根的准确阶、全部投影的幂等性、指定特征值、
反变关系 $K_\nu R+RK_\nu=0$，再进行完整精确高斯消元。
两条核向量以 47 个有限域坐标完整保存在 JSON 中，核验器从头恢复并
逐项核 $Rv=0$、$P_Hv$ 及 (182.18)。

在课题目录运行以下命令即可比对：

```bash
python scripts/verify_r182_mobius_and_order12_blocks.py --check --certificate scripts/data/r182_mobius_order12_block_certificate.json
```

省略 `--certificate` 时，默认读取核验器同目录的 `data/` 子目录；
没有硬编码工作区或临时目录路径。
无需 PARI、浮点数、经验截断或素数窗口。这是一个固定的结构性反例，
不是新的实际椭圆曲线候选。

## 6. 为什么原来的三对角递推不直接转移

R177 对 $Q_1$ 在指定 Schrödinger 基给出了有单位邻项的三对角递推，
所以其 odd 左核维数至多一。R 不是同一个算子。

还可以准确排除一个常见的换基捷径。

**引理 182.3。** 对 $p>3$ 的十二点差 (182.11)，任何线性辛坐标变换
及其 Weil 换基，都不能使 R 在相应 Schrödinger 基中只含循环三对角
位移 $\{0,\pm c\}$，$c\ne0$。

**证明。** 取阶三根 $\zeta\in\mathbf F_{p^2}$，两向量 $a,a\zeta$
构成 $\mathbf F_p$ 基。可将第二个六边形写为

$$\nu a\mu_6=\frac{1-\zeta}{\sqrt3}\,a\mu_6.$$

此处 $\sqrt3\in\mathbf F_p$：$p=6\cdot2^b-1\equiv11\pmod{12}$，
或直接由阶十二根的和 $\nu+\nu^{-1}$ 取得。

任一 Schrödinger 位移是一个非零线性泛函 L。
若第一六边形只给 $0,\pm c$，除以 c 后记
$A=L(a)/c,B=L(a\zeta)/c$，则

$$A,B,A+B\in\{0,1,-1\}.$$

二者不同时为零。对 p>3，这些可能性迫第二六边形的位移值中同时
出现 $\pm u$ 和 $\pm2u$，其中 $u=1/\sqrt3$，符号不影响结论。
若它们也都在 $\{0,1,-1\}$，则 $u=\pm1$ 且 $2u=\pm1$，
迫 p=3，矛盾。

Weyl 算子 $D_v$ 在好特征仍为矩阵空间的一组基，且这里十二个非零
系数为单位。因此不可能由不同位移的相消消去上述多余对角线。
证毕。

这个引理只排除线性辛/Schrödinger 三对角化。它不排除尚未找到的
Cartan 特征基上的另一种递推、整 Bézout 关系或直接针对 H 直线的证明。
定理 182.2 进一步说明，任何这样的新论证必须允许真实好特征中出现
方块核，不能先假定全部方块可逆。

## 7. 保留下来的准确未解接口

对 $m=2^b$，一个原始轨道加旧 Steinberg 行仍待排除的条件就是

$$R\,\operatorname{im}(P_H)=0,\qquad P_HQ_m=0.$$

对一般合数 m，准确条件是 (182.5)，其剩余列由 (182.3) 逐精确阶分开。
R177 全类型定理不允许所有精确阶同时失效，但不指定是哪一个阶。
实际 Frobenius 保持精确阶，不能填补这一缺口。

在几何方面，R181 已证明充分大的 p 每个所需阶都有实际非 CM 候选商；
中心值非零与对应有理点有限仍须逐项处理。本文没有把有限类型存在、
方块非零或某个其他频率非零转成指定实际分母的排除。

接下来真正需要的是对 $\ker\mathcal R_m\cap\operatorname{im}P_H$ 的控制，
并同时利用旧行条件；或取得缺失精确阶的实际非零中心值。

## 8. 依赖与可复核性

代数输入仅为 R174 的同一频率/Cartan 识别、R177 的整 Weil 表示和
全类型单位理想，以及已保存的复合 m 特征矩阵。本文的新等式
(182.2)–(182.12)、块维数与引理 182.3 均已在正文证明。
唯一数值实例由本篇标准库证书独立覆盖；不调用外部未发表非消失结果。
