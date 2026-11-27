# R150 Lt0：修正后原低次不变量输入与 QQ 证书门

日期：2026-11-27。会话：Astra-ISP-8542378f-20261127 / r150_open_geometry。

**这是已完成前置恒等式核验的新输入，尚不是排空结论。** [自含源](../notes/2026-11-27-unit211-S0-Lt0-low-invariant-original-QQ-8542.py) 本地 build-only 已实际通过；只有后续 Singular 在 QQ 多项式环中取得证书且 `matrix(I)*cert` 实际等于 `[1]` 才可登记排空。本源不读取旧 scratch 均值数据，不重跑作废的 374/580 次投影或旧高系数 PRS。

## 1. 从原 Frobenius Gram 生成四式

使用原基数 2+1+1 的双点乘法

$$
(vw)_0=v_0w_0,\quad (vw)_1=v_0w_1+v_1w_0,\quad
(vw)_B=v_Bw_B,\quad(vw)_C=v_Cw_C.
$$

在形式参数 (ell,u,Q,lambda,f,t) 中令 r²=1−Q、p=1+r、q=1−r，

$$
b=\ell/2+\frac{u-\ell}{2(1-Q)}r,\quad c=\ell-b,
\qquad bc=\frac{2\ell u-u^2-\ell^2Q}{4(1-Q)}.
$$

直接使用原 W1/W2 重建 Gram，并生成 E1、EB 的偶部/奇部，以及

$$
N_{01}-\frac{4\lambda}{3}P_{01}.
$$

最后一式由原 P01=3wP02、N01=4lambda wP02 消去同一 w 而来。源先验证原 F2=2f、E0=0、P(K0)=P02、N(K0)=2lambda P02，所有平方和乘积均使用 `vm`，包括关键的 (d·d)1=2d0d1。E1 的奇部实际为零，EB 与 EC 实际互为同一 r 的共轭。

每个原有理分母都实际按 Q、1−Q、bc 的原分子剥除至非零常数。因此以下原分母清除都只使用现有物理单位，不以独立范数排除某个嵌入。

## 2. Lt0 的可逆低次坐标

令

$$
e=u-1,\quad k=Q/e,\quad j=k+2-2e,\quad x=k+4.
$$

这里 k 是新的不变量坐标，与 U 值的 k 名称无关。原 Lt0 恒等式给出

$$
\ell=j/k,\quad u=e+1,\quad Q=ek,\quad T_0=-e(k+4).
$$

这里 ell 的非零没有借用 L0 的零权和结论。原未除法身份为

$$
P_{02}-2\ell Q(u-1)
=-u\{T_0+4(u-1)+Q\}.
$$

Lt0 令花括号为零，而原物理 $P_{02}=2P_0\ne0$，所以 ell、Q、u−1 都非零，j=ell·k 也非零。u 非零来自已闭的 [整个零基点 mean 分支](R150-appendix-essential-four-unit-two-plus-one-plus-one-zero-base-mean-exclusion.md)。这一步保留了全部 S0 图，未把其他分层的支付挪用过来。

再记

$$
D_3=4e^3-3e^2k-4e^2+ek^2+4ek+4e-k-4.
$$

源逐项检查

$$
bc=\frac{D_3}{4k(ek-1)}.
$$

故取 v=4kbc·t，即 t=(ek−1)v/D3，是原单位上的可逆变换。代入并只清除已付单位后，四式对 (lambda,f,v) 总次数均不超过 2，项数分别为

```
E1 103；EB_even 227；EB_odd 174；N1elim 94。
```

全部系数转换都实际乘回，E1 与 N1elim 的 v² 系数分别为 j/8、j/4。j=ell·k 为原单位，因此这里没有未付的 E1 二次首项零分支。

设 C 为前三式对 (lambda²,lambda f,f²) 的系数矩阵。源逐项检查九条 C·adj(C)=det(C)I 身份及

$$
\det C=-512e(e+1)(4e-k-4)k^2(-j)^3D_3^3.
$$

唯一原单位外的因子 4e−k−4 与 ell−1/2 等价，已由 [整个半 base 权支路](R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-Lt0-half-base-weight-exclusion.md) 关闭。由第四行减去其前三列的 Cramer 组合得到一个对 lambda、f 合计一次的 205 项原必要式 Lsmall。源明确检查

$$
A_{\rm paid}L_{\rm small}=\sum_{i=1}^4w_iP_i,
$$

Apaid 只含 e、k、j、D3 的已付幂；并核对每一次除法。它与四原式在原单位局部化中的关系完整保留。

## 3. 同一 S0 值参数，不丢 Bv=0 或 w=0

令 s=2lambda−3、A=2lambda²−2lambda+1、C0=−4lambda²+5lambda−2、R0=3−4lambda，并定义

$$
T_n=x^2-2j^2-2\lambda jx-4xf,\quad T_d=2jk,
$$
$$
Z_n=sT_n-2jkA,\quad Z_d=2j^2,
\quad\Delta_n=s^2Z_d-4Z_n.
$$

原 P1 与第二 U 矩给出 T=Tn/Td、z=Zn/Zd。所有分母 j、k、x 均已支付；未除 Bv、w。引入 eta=theta·Delta，以下四个多项式保持同一参数、同一配对：

$$
M_1=Z_nT_n-C_0Z_dT_d,
$$
$$
M_2=(ek+2e-2)\Delta_n-2j\eta(T_n-j^2s),
$$
$$
M_3=\eta^2Z_d-(1-ek)\Delta_n.
$$

前者是原 zT=C0；后两者分别为

$$
(u-\ell)\Delta=\eta B_v,\qquad \eta^2=(1-Q)\Delta,
\quad B_v=2T-\ell s.
$$

这不是独立取范数：同一 eta 同时进入配对式和范数式，Bv=0、u=ell 及 w=0 均保留。

记

$$
E_n=2j^2+T_n,\quad W_n=(\lambda-1)T_d-T_n,
\quad Y_n=j[j+k(e+1)]s-T_n-j^2\eta.
$$

第四个原必要式为

$$
M_4=2k^2x(R_0Z_d-Z_n)f-2ekE_nZ_n-xW_nY_n.
$$

它是原 N(V) 的低次清分母形式。源分别乘回验证其与

$$
2(R_0-z)f-\frac{4\ell(\ell+T)Qz}{x}
-w[(\ell+u)s-2T-\ell\eta]
$$

的精确关系。为核对原 N(V) 的来源，源还在完全独立的原 (lambda,z,theta,f) 多项式环中重建 K、原 P1 分子 Fnum，并验证

$$
2V N_{\rm lin}-K
=z^3(R_0-z)(4VT_nf-F_{\rm num}).
$$

右边就是原 P1 的倍数。该检查在任何参数商之前执行。

## 4. 实际 QQ 门与执行身份

最终环为

```
QQ[invUnit,eta,v,f,lam,k,e]
```

使用九个已清分母的原必要式，加一个 invUnit·S−1。S 的每个原子都有明示支付来源：e、k、u、j、x、ek−1、D3、lambda、z、Delta、L、Af，以及已关闭的 a=0、a=1/2、M 的两个首项零谱因子。没有新增未处理的首项零或除法。

当时冻结源拟用 Singular `liftstd(I,cert,"modstd")`，先在同一 QQ 环核一个小单位的证书乘回，再运行新输入。最终严格检查

```
size(GB)==1, GB[1]==1,
nrows(matrix(I)*cert)==1,
ncols(matrix(I)*cert)==1,
(matrix(I)*cert)[1,1]==1.
```

软件接口依据 [Singular 官方 liftstd 文档](https://www.singular.uni-kl.de/Manual/latest/sing_294.htm) 与 [算法选择文档](https://www.singular.uni-kl.de/web/docs/tutor-computing-groebner-and-standard-bases-1a4737bf.html)。模块运算的实际证书回乘是唯一排空判据；模素数发现、普通 gcd=1、只返回 basis 的日志都不代替它。

源 SHA256：

```
05e7694122dc8ac6c94ba7a1f1093efa1ac79f00919adab1cd01f136fd27f6ba
```

[实际 build-only 回执](../notes/2026-11-27-unit211-S0-Lt0-low-invariant-build-execution-8542.json)：Python 3.12.14、python-flint 0.9.0，exit 0，0.352856 秒。生成 Singular 输入 20,366 字节，SHA256：

```
b324e3e541d95f66cd5c5098628f14f87c9ce3aeb6761b496cea1795ca5fbeb2
```

本次本地没有 Singular，因此该 build 回执明确 `singularActuallyRun=false, claimExcluded=false`。新源内部证书门为 1200 秒、8 GiB 地址空间；后续 Actions 的真实退出、stdout SHA 与单位乘回必须另记。输入未出单位时继续换输入，不能将 build-only 成功写成数学排空。

专用 Actions `invariant-subspace-Lt0-low-invariant-8542.yml` 固定此源的提交与 Git blob，父进程上限1400秒；实际退出、完整stdout摘要与I*C=1身份另记。启动运行本身不构成排空结论。

### 2026-11-27 实际回执更新

run `45890460154` / job `140151553412` 已结束，见[准确回执](../notes/2026-11-27-unit211-S0-Lt0-low-invariant-actual-execution-8542.json)。driver 实际 1200.425908 秒、RSS 2665480 KiB、source exit 1。小 `modstd` smoke 在通过标志出现前已触约 8 GiB 虚拟内存、tasks 类型错误及 signal 11；重启后变量未定义，后来完整 BEGIN 标志不代表证书入口已有效。全程无小单位或原单位的有效回乘，未判空。此源冻结不重跑；转入[新增原 P/N 的三参数 Cramer 必要系统](R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-Lt0-original-Cramer-minor-system.md)，并换直接 `std` / `slimgb` 入口。
