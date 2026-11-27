# R150：原 S0 / Lt0 一般图的完整排除

**状态：已证明。** 已登记退化面之外的三值互异、$L\ne0$、$A_f\ne0$ 的原 S0 / Lt0 一般图无解。完整有理数覆盖的所有三个因子已返回，不留参数首项零纤维、不选取任何复嵌入。与该图此前已闭各边界合并，即关闭该 S0 / Lt0 分支。本稿不宣称一般 $LS\ne0$ 图、L0、R150 总目标或普通 Hilbert ISP 已完成。

会话：Astra-ISP-8542378f-20261127；AI-assisted GPT-6 Astra Pro。

## 1. 原参数及依赖的已付单位

沿用原 S0 / Lt0 的同点坐标

$$
e=u-1,\qquad k=Q/e,\qquad v=4kbc\,t,
$$
$$
j=k+2-2e,\quad x=k+4,\quad
D_3=4e^3-3e^2k-4e^2+ek^2+4ek+4e-k-4.
$$

在原图上 $\ell=j/k$、$T_0=-ex$、$bc=D_3/[4k(ek-1)]$。原 Frobenius 双点乘法始终是

$$
(vw)_1=v_0w_1+v_1w_0,
$$

所以原均值式中的 $-2(d^2)_1$ 为 $-4d_0d_1$。新源从正确原乘法重建全部输入，没有使用已作废的 scratch 投影。

本稿用到的非物理边界单位均有此前完整证明：

- $e-1$：`results/R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-Lt0-zero-base-weight-exclusion.md`，即整个 $u=2$、$\ell=1$、零 base 权支路。
- $4e-k-4$：`results/R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-Lt0-half-base-weight-exclusion.md`。
- $4e-k$：`results/R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-Lt0-mean-consistency-line-exclusion.md`。
- $v$：`results/R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-Lt0-zero-singleton-pairing-exclusion.md`。
- $\Omega=2e^2-ek+2$：`results/R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-Lt0-quadratic-invariant-curve-exclusion.md`。
- $2e-1$：`results/R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-Lt0-ehalf-original-exclusion.md`，完整 $u=3/2$ 纤维。

原物理和既定非零均值图已经支付 $e,k,j,D_3,ek-1,e+1$。$x$ 来自 $T_0=-ex$ 与已闭原 P1 双系数零面：在 Lt0 上，$T_0=0$ 会同时令 P1 的 f 系数为零，见 `results/R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-P1-zero-coefficients-exclusion.md`。特别是 $e=u-1\ne0$ 可由原 $2P_0=2\ell Qe\ne0$ 直接读取；$e+1=u\ne0$ 来自原非零孤立均值图。它们没有在本稿中被当作未知一般位置假设。

## 2. 四条完整原参数必要式

### 2.1 原五二次式的 F41 与原三次行的 U38、N42

五个原二次式为

$$
E1,\ EB_{\mathrm{even}},\ EB_{\mathrm{odd}},\ N1_{\mathrm{elim}},\ Qa.
$$

最后一个来自同一 $\eta$ 的原配对和范数恒等式

$$
D\,Qa=M_a(UD+2j\eta B)+2B^2M_n.
$$

所以它在每个原解处为零；这里没有另选范数根。每个二次式乘 $\lambda,f,v,1$，按全部 20 个总次数不超过 3 的单项式排列，构成原矩阵 $M$，且最后一个单项式为 1。源码重建全部 20 个原行，并验证一个完整的常数列 cofactor 身份

$$
cM=(0,\ldots,0,D_M).
$$

剥除已付因子后得到原必要曲线 $F=F_{41,33}$。其规范序列 SHA256 为

`ca1b9ef43348fdfa70bf1303051d4a5d9315a64a18c7b9b0f98c4ed1e2482144`。

将 $M$ 的最后一行 $Qa\cdot1$ 分别替换为原 `U_moment`、`NB_even`，再逐项构造并回乘相应的 20 项 cofactor，得到原必要曲线

$$
U=U_{38,31},\qquad N=N_{42,34}.
$$

忽略非零有理内容，完整分解为

$$
\begin{aligned}
D_U&\doteq e^4k^{10}j^6xD_3^{10}(4e-k-4)^2(4e-k)U,\\
D_N&\doteq e^4k^{10}j^5xD_3^{11}(4e-k-4)^2(4e-k)N.
\end{aligned}
$$

每一剥除乘积和有理内容均实际乘回。$U,N$ 的项数分别为 737、908，SHA256 分别为

- `b76f8e51881fd426200f19bc07cd3d0c0c24873016435d9782b46e56be8664a5`；
- `b200b0d88c5c45de4d077f68b213a271950fe982b9f4a860c74824409e79ddab`。

所有分数自由中间除法都在多项式环内整除并乘回，没有在点上倒置消元枢轴。故原系数首项为零时，上述三个必要式仍有效。自含源还完整再生第三条原 $P_{47,37}$ 和它的 20 项 cofactor；它不需要用于本次最终排除。

### 2.2 从原低行再生完整 G132

独立使用原 $N1$、原 `U_moment` 及三个原均值的两条准确重叠式。源码给出它们对原均值理想的显式组合，清除并验证已付分母后，每行对 $(\lambda,f,1)$ 线性。

由原 $3\times3$ 行列式得到 $P_{045},P_{035}$。两式的 $(e,k,v)$ 次数分别为 $(19,16,6)$、$(23,19,6)$，每个行列式都验证了原三行组合身份。随后计算完整

$$
R_G(e,k)=\operatorname{Res}_v(P_{045},P_{035}).
$$

其双次数为 $(180,155)$。源码只剥除已付 $k,D_3,x,u,4e-k-4,4e-k,\Omega$ 的相应幂，完整乘回；得到

$$
G=G_{132,109}(e,k)=0.
$$

这里没有倒置任何 $v$ 首项，所以全部 $v$ 降次纤维仍在覆盖内。规范 $G$ 的 SHA256 为

`eda457be0935386401451ddf8b2d09410dc6ea5a6d263c9a3e415de36eec1f96`。

因此，任一原点的同一个 $(e,k)$ 必须满足 $F=U=N=G=0$。本证明只用它们的必要性，没有声称任意参数交点可以提升为原物理解。

## 3. 完整 QQ 投影与全部 615 次剩余覆盖

在 $\mathbb Q[e]$ 中实际计算完整结式

$$
R(e)=\operatorname{Res}_k(F,U).
$$

原两个 $k$ 次数为 33、31；结果非零，$\deg R=1502$。全部原 $k$ 首项零点保留在这个完整 Sylvester 结式中。

精确剥除的已付部分恰为

$$
e^{98}(e-1)^{44}(e+1)^{555}(e-\tfrac12)^{190}.
$$

对应支付来源如下。

| 因子 | 原含义 | 已付原因 |
|---|---|---|
| $e$ | $u-1$ | 原 $2P_0=2\ell Qe\ne0$ |
| $e-1$ | $u-2$ | 整个零 base 权支路已闭 |
| $e+1$ | $u$ | 原非零孤立均值图 |
| $e-1/2$ | $u-3/2$ | 整个 ehalf 原纤维已闭 |

每次除法都乘回，余式 $C$ 为 615 次。完整因式分解及非零有理内容也乘回，给出

$$
C(e)\doteq C_2(e)C_{296}(e)C_{317}(e),
\qquad C_2=e^2+1.
$$

三个重数均为 1。后续只用这个精确乘积分解，不依赖它们的不可约性。没有只取平方自由支持或删去任何未知因子。

| 精确对象 | 次数 | SHA256 |
|---|---:|---|
| 完整 $R$ | 1502 | `d379086ccd80f7a1e41d390b5745ea0249ee0df7af8dce28e8107e417fe9bd6b` |
| 已付剥除后的 $C$ | 615 | `4a3942a867bc1745d8e3094bce8fe5acf696b6eb94338f80eca26d7ca66adef7` |
| $C_2$ | 2 | `ba96a490d05076d882fafacd51dbf0cfdf8468fe9886273e2ff353bd0331658d` |
| $C_{296}$ | 296 | `199b93f663d60c8990cf1cbc4477bf397b4716f38c01001f7da4cca4416cf91f` |
| $C_{317}$ | 317 | `f08a5fba7e9204886fb70147d627287673020a4683fa016a13c4d1099bb30dfc` |

## 4. 两个原完整投影的合法模返回

定义两个完整 QQ 一元结式

$$
S_N(e)=\operatorname{Res}_k(F,N),\qquad
S_G(e)=\operatorname{Res}_k(F,G).
$$

它们是原必要式，所以任一原解的 $e$ 必须使二者为零。为避免再次生成不需要的巨大 QQ 系数，直接计算这两个完整 Sylvester 结式模 1009 的约化；这一步的合法性由下列逐项检查保证。

1. $F,N,G$ 的每个有理系数分母在 1009 处为单位。
2. 消去变量 $k$ 的完整次数在约化前后分别保持 $33,34,109$。
3. 三个真实 QQ 覆盖因子的所有系数均可约化，且其首项在 1009 处为单位。规范首项的余数依次为 **1、594、33**，对应次数 **2、296、317**。
4. 源还实际除以该有理首项，核验每个单首项版本的所有系数都属于 $\mathbb Z_{(1009)}$。

故所计算的确为完整 QQ $S_N,S_G$ 的模约化，而不是换了 $k$ 次数后的结式。得到

| 原完整投影 | 保持的原/模 $k$ 次数 | 模 1009 结果次数 | 模结果 SHA256 |
|---|---:|---:|---|
| $S_N$ | (33,34) | 1691 | `6a3eb8ff5df05ffe5ea939271b1c207a24ce1fa7ad2c5bba84a1f76a31d77cac` |
| $S_G$ | (33,109) | 5294 | `51667346f8198d4e7d3c6f39d1f44657a0c4c56f8e0aca3670307bd3db1c78b0` |

最终原 G 是从同一 Gram/均值重新生成的规范，故这里使用最终源实际输出的模结果 SHA；不借用缓存旧归一化的模哈希。

## 5. 三条实际 Bézout 身份与提升论证

在 $\mathbb F_{1009}[e]$ 中实际计算并逐项验证

$$
\begin{aligned}
a_2\overline C_2+b_2\overline S_N&=1,\\
a_{296}\overline C_{296}+b_{296}\overline S_G&=1,\\
a_{317}\overline C_{317}+b_{317}\overline S_N&=1.
\end{aligned}
$$

每条都计算了两个乘积及其和，并断言准确等于 1；不是仅打印 gcd=1。

| 原覆盖因子 | 原支持投影 | 两 Bézout 系数次数 | 两系数合并 SHA256 |
|---|---|---:|---|
| $C_2$ | $S_N$ | (1690,1) | `9eaaa63dd4a7a8f969566125d472f98e8fa14a49429e4d2cf81ab55091e7d652` |
| $C_{296}$ | $S_G$ | (5293,295) | `1cc0c615e36e1bf1155e5bddace9d4e74eab512dfbbf769c3455ab5c30d94721` |
| $C_{317}$ | $S_N$ | (1690,316) | `0d7f4c6c4a521878adddb813525a67bccfa5e91aa78ffdb8007be22d1b2ca437` |

逐个因子的 QQ 提升如下。假设某个 $C_i$ 与其对应的完整 QQ $S$ 有共同复根。取该根在 QQ 上的单首项最小多项式 $h$。由于 $C_i$ 的单首项版本属于 $\mathbb Z_{(1009)}[e]$，Gauss 引理给出 $h\in\mathbb Z_{(1009)}[e]$。又 $S$ 的系数也在这个环中，除以单首项 $h$ 的多项式长除法仍在该环内。因此约化后的 $\bar h$ 同时整除 $\overline C_i$ 和 $\overline S$。$h$ 单首项，故 $\bar h$ 仍有正次数，与上列实际 Bézout 等式矛盾。

这个论证对各因子的所有复嵌入同时成立，并不需要选一个代数根。特别地，二次因子 $e^2+1$ 的两个嵌入都排除。这里使用的是一个已实际取得的完整一元 QQ 覆盖及其首项单位；不是从任意多变量模单位推断 QQ 单位。

于是 $C_2,C_{296},C_{317}$ 的所有零点都不可能来自原解。第 3 节已完整覆盖所有可能的 $e$，所以剩余原 S0 / Lt0 一般图为空。

## 6. 自含源与真实执行

完整源：

`notes/2026-11-27-unit211-S0-Lt0-complete-original-cubic-cover-return-8542.py`

源从原 Frobenius Gram 重新生成输入；不读取仓库外多项式缓存。所有原 cofactor、均值组合、Cramer 行列式、已付因子剥除、完整 QQ 覆盖、三个因子乘积、首项单位及三个 Bézout 回乘都在一次执行中完成。

- 源 SHA256：`9d0c77892ae07bb04ee6c3e596b48e543310004c65962000a93204db10d226ea`；33625 字节。
- 实际参数：无；Python 3.12.14 / python-flint 0.9.0。
- 实际 exit **0**；墙钟 **163.600807 秒**；源内完成时刻 163.467205 秒；峰值 RSS **124232 KiB**。
- 原界限：360 秒，4 GiB 地址空间。
- 标准输出 22893 字节；SHA256 `48c45766eee40365bc9ec3c935d666ee27041472a19e26a15912f655175f908a`。
- 小回执：`notes/2026-11-27-unit211-S0-Lt0-complete-original-cubic-cover-execution-8542.json`。
- 最终输出 `wholeRemainingS0Lt0Excluded=true`、`ordinaryISPClaim=false`。

最初用于选路的模 1031 探针有实际首项降次：完整 QQ 投影为 1502 次，模结果为 1501 次。该探针没有被提升为排空证明；最终证书改在 1009 处对实际 QQ 因子逐个核验全部首项单位和完整 $k$ 次数。此前单独启动的三变量 QQ 门保留其真实运行日志；本证明不以该门的运行状态或结果作为任何前提。

## 7. 完成范围

本稿关闭的是上述原 S0 / Lt0 一般图。此前各退化面均已有独立完整返回，与之合并可登记整条 S0 / Lt0 支路关闭。一般 $LS\ne0$ 四参数 atlas、L0 以及 R150 的其他型仍按 open 保留；原几何排除也不自动提供 Bell 自然幂或算子桥。
