# R150 补充：Phi 零碰撞图的 H4/H20 整纤维排除及原结式的 36 次 QQ 因子

日期：2026-11-27（Asia/Taipei）  
会话：Astra-ISP-8542378f-20261127

## 1. 结论

继续 [严格 68 点覆盖](R150-appendix-unit211-Phi-zero-rank-one-value-actual-residual-68-point-cover.md) 中的有序 $h=1$、$\Phi=0,z_n=0$ 原图，所有原物理单位及原八式保持。

令
$$
H_4=16\lambda^4-24\lambda^3+16\lambda^2-7\lambda+1,
$$
并按常数到最高次定义
$$
\begin{aligned}
H_{20}:\quad (&5,-86,751,-4320,18035,-57032,138416,-253716,\\
&325848,-204088,-230340,876048,-1346992,1230656,\\
&-511168,-330880,752576,-647168,325376,-94208,12288).
\end{aligned}
$$

**原图中 $H_4(\lambda)=0$ 与 $H_{20}(\lambda)=0$ 的全部复数纤维均为空。** 这保留每个复根、全部允许的 $\rho$ 与两条原 $\ell$ 根；不要求这些常数商代数是域，也未逐系数分拆一个有限域中的原方程。

此外，对同一真正的 27 阶原结式
$$
R=\operatorname{Res}_{\rho}(F,G)
$$
有
$$
H_4^4H_{20}\mid R\quad\text{于 }\mathbb Q[\lambda]. \tag{1.1}
$$
按首一规范计，新增因子总次数为 $4\cdot4+20=36$。与已付 $Q_{840}$ 合成得真正的首一 1069 次原覆盖。其进一步模公共因子尚由新的实际余式返回处理；本稿不从形式相除直接宣称 32 点界。

## 2. 精确原输入与常数商中的单位剥除

$F,G$ 分别为原 $(E_1,E_C)$ 与 $(N_1,\ell N_1)$ 对真实单位目标的完整清分母返回所得 primitive integer core。它们的双次数为 $(77,14),(75,13)$，整数输入 SHA256 分别为

- $F$：$\texttt{81798a00dd2c4be037737c974dea3b77563363789701dbfc5a0ad0b13769362c}$；
- $G$：$\texttt{20ae05561daf12c30208e46313cfa2d015d3792a97ce2040193ffdbb06872e64}$。

每一个实际原点都使这两条曲线在同一个 $(\lambda,\rho)$ 为零。使用的是原必要条件及已付单位目标身份，没有额外加上独立的系数为零假设。

对 $i=4,20$，把 $H_i$ 规范成首一 $\phi_i$，在
$$
A_i=\mathbb Q[\lambda]/(\phi_i)
$$
中逐个 $\rho$ 系数作精确除法。每次均核对 $p=q\phi_i+r$ 的完整 QQ 乘回。随后只除原图中已经非零的 $\rho,\rho-1,\rho+1$；所有商再次逐系数乘回。实际只发生：

- 在 $A_4[\rho]$ 中，$F,G$ 各除 $\rho^2$；
- 在 $A_{20}[\rho]$ 中，$F,G$ 各除 $\rho+1$。

除法之后，以 $\lambda$ 次数小于 $i$ 的规范系数提升回 $\mathbb Q[\lambda,\rho]$，清掉非零有理常数并取 primitive integer 规范，所得多项式记 $\widetilde F_i,\widetilde G_i$。于是存在非零有理常数 $s_{F,i},s_{G,i}$，使
$$
\begin{aligned}
\widetilde F_4&\equiv s_{F,4}F/\rho^2\pmod{\phi_4},&
\widetilde G_4&\equiv s_{G,4}G/\rho^2\pmod{\phi_4},\\
\widetilde F_{20}&\equiv s_{F,20}F/(\rho+1)\pmod{\phi_{20}},&
\widetilde G_{20}&\equiv s_{G,20}G/(\rho+1)\pmod{\phi_{20}}.
\end{aligned}
$$
这里分式仅表达已经在 $A_i[\rho]$ 中完成的整除；没有把 $\rho$ 或 $\rho+1$ 作为一个新未付单位。

因此，任何原点若还满足 $H_i(\lambda)=0$，就必在同一允许的 $\rho$ 处使 $\widetilde F_i,\widetilde G_i$ 同时为零。没有遗漏系数降阶或非约化常数商的纤维。

## 3. 两个固定原行列式的完整 Gauss 返回

定义真正的 QQ 整系数行列式
$$
D_i(\lambda)=\operatorname{Res}_{\rho}(\widetilde F_i,\widetilde G_i).
$$

实际数据如下：

| 常数纤维 | 两输入双次数 | 固定阶数 | 完整模行列式次数 | 与首一 $\bar\phi_i$ 的 Bézout 标签次数 |
|---|---|---:|---:|---|
| $H_4=0$ | $(3,12),(3,11)$ | 23 | 69 | $68,3$ |
| $H_{20}=0$ | $(19,13),(19,12)$ | 25 | 475 | $474,19$ |

两个 $\rho$ 次数在 1009 下均保持；因此计算得到的是同一固定 QQ Sylvester 行列式的真实约化。两次均已完整乘回
$$
a_i\bar\phi_i+b_i\overline{D_i}=1. \tag{3.1}
$$
模行列式的 SHA256（按本源完整系数列表序列化）依次为
$$
\begin{gathered}
\texttt{7313d993971ccf8ce126b236a48f7203b2569969a27fd0150f7b725f43606ace},\\
\texttt{1b8d76583afe6be4973b283b8410bda50ca56a98b0585aa588a09f1085387977}.
\end{gathered}
$$

$\phi_i$ 是首一的 $\mathbb Z_{(1009)}$ 多项式，次数在约化后保持。如果 $\phi_i,D_i$ 有非平凡首一 QQ 公因子，则该因子是 $\phi_i$ 的首一因子，故为 1009 整；其约化保持次数，并由首一除法同时整除 (3.1) 的两个模输入，矛盾。因此
$$
\gcd_{\mathbb Q[\lambda]}(\phi_i,D_i)=1.
$$

任何共同有限 $\rho$ 根都给固定 Sylvester 的幂列核向量，即使最高系数在该 $\lambda$ 处退化也一样。所以原 $H_i=0$ 纤维不可能存在。此论证没有从一般多变量模空性直接推 QQ 空性，也没有倒置常数商代数的范数。

## 4. 已付系数身份直接给出 (1.1)

本节使用此前 [同 rho 与精确 QQ 边界记录](../notes/2026-11-27-unit211-Phi-zero-rank-one-value-same-rho-exact-boundary-observation-8542.md) 和本次实际系数除法；不再计算一次 QQ 局部行列式。

先给一个通用整数对偶。设两原 $\rho$ 多项式的固定次数为 $m,n\ge r$，其第 $j$ 个系数均整除 $\phi^{\max(r-j,0)}$。在其固定 $(m+n)$ 阶 Sylvester 中，两类第 $s$ 个移位行取整数权
$$
a_s=-\max(r-s,0),
$$
第 $k$ 列取
$$
b_k=\max(2r-k,0).
$$
某个非零项来自第 $j$ 系数时 $k=s+j$，直接有
$$
a_s+b_{s+j}\le\max(r-j,0).
$$
于是每个行列式单项都含至少
$$
2\sum_{s=0}^{r-1}(-(r-s))
+\sum_{k=0}^{2r-1}(2r-k)
=-r(r+1)+r(2r+1)=r^2
$$
个 $\phi$ 因子。故 $\phi^{r^2}$ 整除真正 QQ 行列式。这个论证是逐项整除，不要求 $\phi$ 不可约，也不要求首项单位。

对于 $H_4$，旧完整 QQ 边界 gcd 已实际给出
$$
H_4^2\mid F(\lambda,0),\qquad H_4^2\mid G(\lambda,0).
$$
本次在 $A_4[\rho]$ 中各除 $\rho^2$ 的完整返回又给出其 $\rho^1$ 系数均含 $H_4$。故取 $r=2$，上述对偶总权 $4$，得到 $H_4^4\mid R$。

对于 $H_{20}$，旧原 $\rho=-1$ QQ gcd 或本次除 $\rho+1$ 均给出
$$
H_{20}\mid F(\lambda,-1),\qquad H_{20}\mid G(\lambda,-1).
$$
同时以 $\rho\mapsto\rho-1$ 平移两原多项式；结式不变。取 $r=1$，对偶总权 $1$，得 $H_{20}\mid R$。

已实际给出的 QQ 因式分解显示 $H_4,H_{20}$ 是不同的不可约因子，且与 $Q_{840}$ 的所有一次、二次因子互素。因此 (1.1) 可与原 $Q_{840}$ 整除相乘。取各因子首一规范后，所得商仍为 1009 整，且由原 1945 次首项保持知商的次数恰为 $1945-840-36=1069$。全部新除去因子的原复纤维已由第 3 节排除。

## 5. 唯一实际执行与可再生源

源：[H4/H20 原整纤维 Gauss](../notes/2026-11-27-unit211-Phi-zero-rank-one-value-H4-H20-original-fiber-Gauss-8542.py)。

- source blob：$d21ef0e62e314fa6f89ede877b6ff7e0719d9009$；
- SHA256：$cce290a5c97eefc094e9b9ae831005f64e5579302f32a1220cc7a804c608882c$；
- Actions run/job：46001850994 / 140515236745；
- 实际内层 exit：0；3.620285527 秒；52624 KiB；
- stdout：20719 字节，SHA256 $0d5ead6461f8b907f05549096861c932b33f3edf297792cf48a859a00c7f272b$；
- main：$7bd543fbd1218460bc7cb96113d678bddd165014$；
- 12:49:32.844083 UTC 实际 pull 后两 README blob 均无变。

H4 案件实际核对 627 次系数除法和 118 个单位除法系数返回；H20 为 480 次和 61 个。每案首个原 F/G 投影即返回 1，因此没有启动额外组合或 NB/PB 后备门。

尚未排空整个 $\Phi=0$ 面或碰撞图；ordinary ISP 未宣称完成。
