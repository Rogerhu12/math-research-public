# R150 附录：物理 lambda 坐标、四个完整二次头与 52 权例外

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

## 1. 完整原换坐标

在当前一般 LS、$\Delta=0$、$W=0$ 余图中，沿用
$$
u=e+1,\quad Q=ek,\quad V=uk+2,\quad
\ell=\frac{u((k+2)^2-2ek)}{kV}
$$
及原 $x,y,t$ Gram。原恢复式中的 $\lambda$ 对这三个变量是仿射的，且
$$
\lambda=\alpha_0+\alpha_xx+\alpha_yy+\alpha_tt,\qquad
\alpha_t=\frac{bcQ}{P_{02}}\in A^\times. \tag{1}
$$
所以整个当前 W 图上有无新首项的可逆换坐标
$$
t=\frac{\lambda-\alpha_0-\alpha_xx-\alpha_yy}{bcQ/P_{02}}. \tag{2}
$$
本次实际返回两个方向，并对完整
$$
E_1,\ E_{B,e},\ E_{B,o},\ N_1,\ N_S,\ P_S \tag{3}
$$
六原式逐个返回正向代入和反向恢复。没有倒置 $\lambda$、物理 $D$、范数或任何新二次头。其余原个别值条件始终保留。

令 $\widetilde E_i$ 为前四原式经过 (2) 后的多项式。仅清已付权分母及共有已付权内容后，得
$$
G_i=s_i\widetilde E_i\in\mathbb Q[e,k,x,y,\lambda],
\qquad s_i\in A^\times,\quad i=0,1,2,3, \tag{4}
$$
按 $(E_1,E_{B,e},E_{B,o},N_1)$ 排列。所有比例及其逆均实际付清。

## 2. 新权单位的准确来源

本稿的 $A$ 只是此前当前 W 原权域，未扩大其适用范围。除原 $e,k,u,V,Q,1-Q,bc,P_{02},\Phi$ 外，源码使用的权支付来源包括：

- [整个一般等权排除](R150-appendix-unit211-equal-weights-complete-original-exclusion.md)，以及
  $$(\ell-u)kV=u(k+2)(2-Q),$$
  支付 $\ell-u,k+2,Q-2$。
- [整个 W 的 u=Q 排除](R150-appendix-essential-four-unit-two-plus-one-plus-one-generic-LS-W-u-equals-Q-complete-original-exclusion.md)，支付 $u-Q$。
- [整个 W 的 u=1/2 排除](R150-appendix-essential-four-unit-two-plus-one-plus-one-generic-LS-W-u-half-complete-original-exclusion.md)，支付 $2e+1=2u-1$。
- [一般 ell=0 完整排除](R150-appendix-unit211-general-ell-zero-complete-original-exclusion.md)，在当前既有原域支付 $\ell$。
- [整个 C9](R150-appendix-essential-four-unit-two-plus-one-plus-one-generic-LS-W-C9-complete-original-exclusion.md)、[整个 J19](R150-appendix-unit211-W-J19-entire-original-weight-curve-exclusion.md)、[整个 D27](R150-appendix-unit211-W-D27-entire-original-exclusion.md)、[整个 G36](R150-appendix-unit211-W-G36-entire-original-exclusion-and-global-F-recovery.md) 的独立原排除定理。
- 旧 $k+1$ 与 $H_{\rm old}=4ek-k^2-4k-8$ 仍使用其已刊原整支支付，未把它们与新 $H_{265}$ 混同。

另外，由当前 W 权式直接展开，
$$
T_0V=-eu(k+2)(k+4),\qquad
(J-Q)V=-2e^2k(2e+1). \tag{5}
$$
因此源码中的 $T_0,J-Q$ 支付可以完全归结到上述当前 W 原单位，无须把一般 T0/JQ 定理外推到别的物理域。

## 3. 四个完整 QQ 二次头

因为 $G_i$ 总几何次数至多二，它们在 $(x,y)$ 的三个二次头
$$
x^2,\quad xy,\quad y^2
$$
上的系数不含 $\lambda$。记这个 $4\times3$ 权矩阵为 $B$，定义
$$
\Delta_i=(-1)^i\det B_{\widehat i,*}. \tag{6}
$$
源码直接从完整有限原式提取 $B$，并实际返回三个列身份
$$
\sum_{i=0}^3\Delta_iB_{ij}=0,\qquad j=0,1,2. \tag{7}
$$

四个非零 $\Delta_i$ 分别剥**已付**权因子后，完整 QQ 因式分解都只有一个非恒定不可约因子，重数均为 1：

| 省去的原行 | 保留的三原行 | 未付不可约因子 | 双次数 $(e,k)$ | 总次数 | 项数 |
|---|---|---|---:|---:|---:|
| $E_1$ | $E_{B,e},E_{B,o},N_1$ | $F_{56}$ | $(7,10)$ | 13 | 56 |
| $E_{B,e}$ | $E_1,E_{B,o},N_1$ | $F_{86}$ | $(9,12)$ | 16 | 86 |
| $E_{B,o}$ | $E_1,E_{B,e},N_1$ | $F_{80}$ | $(8,12)$ | 15 | 80 |
| $N_1$ | $E_1,E_{B,e},E_{B,o}$ | $K_7$ | $(2,3)$ | 4 | 7 |

每个完整因式乘积均实际返回；四个未付因子都没有被宣布为原单位。前三者由 (4)–(6) 和冻结源码的唯一不可约因子定义，不另保存系数缓存。其规范因子定义 SHA-256 依次为
$$
\begin{aligned}
F_{56}:&\quad\texttt{5e66ec237cdb23432aeac07cd8afa9addf3427b0f4bc50eaa33ee72e291ca01f},\\
F_{86}:&\quad\texttt{f016a28c9c4a18688ee2e059d1c98a5dbdae23cd657643bff5bef2a5fd9da96c},\\
F_{80}:&\quad\texttt{2b83f9a9171e327ac8f5e5bc20f3c21829ca242e3c56fe365f1d934e678daab0}.
\end{aligned}
$$
最小因子有简短完整定义
$$
K_7=12e^2k^2-ek^3+8ek^2-k^3-4k^2-16k-16. \tag{8}
$$

## 4. 不倒头的完整原仿射关系

对四个实际乘子 $\Delta_i$ 取完整共有多项式因子 $g$，按源码固定常数归一得到 $c_i$，使
$$
\Delta_i=g\,c_i,\qquad c_i\in\mathbb Q[e,k].
$$
每个整除乘积都已返回。这里**同除的是全部四个原组合乘子**，不是无证地把一个原方程除以未付因子。因此
$$
L=\sum_{i=0}^3c_iG_i \tag{9}
$$
仍是整个当前原域的真实原组合，包含 $g=0$ 时的原点。

式 (7) 除去共同因子后仍是多项式恒等式，故 (9) 所有 $(x,y)$ 二次项都取消。本次完整返回
$$
L=L_0(\lambda)+L_x(\lambda)x+L_y(\lambda)y,\qquad
\deg_\lambda L_0\le2,\quad
\deg_\lambda L_x,\deg_\lambda L_y\le1. \tag{10}
$$
$L$ 实际非零。完整原组合在新旧两套坐标中都已乘回，而非只检查一个最高次模型。

实际共有乘子为
$$
g=-24\,kV\,M_{13}^2,
$$
其中 $M_{13}$ 是原 $M=\ell(2u-\ell Q)-u^2$ 恒等式
$$
M=-\frac{u^2M_{13}}{kV^2}
$$
中的十三项多项式。因此本次 $g$ 恰由原已付因子组成；但式 (9) 的完整多项式论证本身不依赖于把 $g$ 额外宣称为单位。

三个系数 $L_0,L_x,L_y$ 的实际分子 $(e,k,\lambda)$ 次数依次为
$$
(18,23,2),\qquad(17,22,1),\qquad(18,23,1),
$$
项数为 818、503、533，分母均为非零常数。其唯一精确定义就是 (4)、(6)、(9) 的固定原组合，详见小回执散列。

## 5. 三生成开图与至多 52 权的整降秩例外

在 $K_7\ne0$ 上，$G_0,G_1,G_2$ 的三二次头 determinant 全部已付。由真实 adjugate 公式可得三条原规则
$$
x^2=a_0(\lambda)+a_1(\lambda)x+a_2(\lambda)y,
$$
$$
xy=b_0(\lambda)+b_1(\lambda)x+b_2(\lambda)y,\qquad
y^2=c_0(\lambda)+c_1(\lambda)x+c_2(\lambda)y. \tag{11}
$$
其中常数列的 $\lambda$ 次数至多二，其余两列至多一，分母只含权单位及明确的 $K_7$。每次 (11) 替换严格降低 $x,y$ 总次数，所以该图的原商在 $A[K_7^{-1}][\lambda]$ 上由
$$
1,\ x,\ y \tag{12}
$$
生成，不要求自由。

第四原式 $N_1$ 仍通过完整 (9)–(10) 保留：其组合系数 $c_3$ 在这个开图是单位，因此三条规则和 $L$ 与完整四原二次式生成同一理想。其余 NS/PS、原值条件不因三生成而删除。这一段是由本次已完整返回的头因式及原组合推出的解析定理；未声称新三规则或新乘法矩阵已经另行执行展开。

同理，四个 $\Delta_i$ 的 principal open 分别给出三生成图。它们未覆盖的**整个二次头降秩权支**满足
$$
K_7=F_{56}=F_{80}=F_{86}=0.
$$
特别满足 $K_7=F_{56}=0$。本次完整 QQ 因式分解证明 $K_7,F_{56}$ 都不可约，而总次数分别为 4、13，所以它们互素但未被称为无共同点。平面 Bézout 给出包含重数的有限权环境
$$
\dim_{\mathbb Q}\mathbb Q[e,k]/(K_7,F_{56})\le52. \tag{13}
$$
继续局部化原权单位并取其余头条件商只会降低长度。

当前全 W 的已付 C9 六规则给每个这个权环境至多六个均值生成元，故五坐标必要环境长度至多 $6\cdot52=312$。再加 $\rho$ 与 $H_A$ 两个首一二次式得到至多 1248 的必要环境；保完整 $H_B$ 且沿用当前 $D_{\rm phys}\ne0$、$\ell-u\ne0$ 时，原 $\zeta$ 由
$$
\zeta=\frac{T+uK_{\rm val}/(2(u-\ell)D_{\rm phys})}{\ell}
$$
唯一恢复，其中 $K_{\rm val}=\ell^2B_3-3\ell T A_2+2T^3$。因此这个降秩支的完整七规范原坐标商长度至多 624。此处与多项式 $K_7$ 区分记号，两个 K 不是同一对象。有限 Artin 局部化保重数、不增加维数；没有把环境点反称为原解。

## 6. 唯一真实运行

源：
`notes/2026-11-28-unit211-W-original-physical-lambda-four-heads-and-affine-identity-8542.py`

- Git blob：`0b261ecc3cb4ef012ed9dce5b9403723edccd7e4`。
- SHA-256：`bc02ab0525d4d32910ecc8a0264af16a089df1f339fb94078a5fb3c1572e3433`。
- run 46070958468；job 140747521972；源提交 `c961e30e596e3b2c43f367bf84c1b6801f7e20e2`。
- 源内部 1.047370768 秒；驱动 1.092022892 秒；RSS 45396 KiB；内层真实退出 0。
- stdout 7382 字节，SHA-256 `27aa551c0ff473a5eca28fa2f3564633c9d87dd0ab1c545674dadc7b68b7513e`。
- 2026-11-27 21:32:39.674223 UTC 真实 pull 后两 README blob 未变。

只执行旧 C9 源的 7224 字节原 Gram 必要前缀，SHA-256 `be7af2ffd4e73d716847c7fa6286170ec18702ea8c84a7cb964e8fcd5622ae4f`；旧六列、95 秒行列式、Gaussian 或规范大值返回均未运行。本结果保留整个 $K_7=0$ 及其它全部未付头零面，继续其原同点返回。
