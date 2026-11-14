# R119 续篇：穿过实际双 bump 后的完整尾迹与长段精确匹配式

2026-11-13，visible-exact / tail_connector。

**状态：已证明。** 同一带 $\ell^1_{8192}$ 标签的 exact-tail chart 现在
穿过 R74 已经选择并安装的两个 bump，到达真正长径向段的 $u=B$。
本篇还把上一续篇解出的非线性 Dirichlet map 与这个实际尾迹写成同一个
明确方程，并证明该方程在原点的全部高频、完整两迹的相对横截常数
为 $2^{-40}$。mean 斜率兼容及平均高度输出都保留。

最后的非线性高输入逆仍未完成。特别，下面的原点相对横截界不等于
整个尾 chart 的相对导数扰动界；后者不能由绝对标签 $D^2$ 界直接推出。

## 1. 不改变已经选择的两个真实 bump

固定 [R74 §1.1](R74-actual-full-tail-robin-and-augmented-positive-cap.md)
非空闭集合中已选择的同一个参数。记
$$
 \psi(u)=s\phi_1(u)+\gamma_0\vartheta\phi_2(u),\qquad
 \gamma_0=2^{-17},\quad B=T-25/8,\quad T=2^{24}.
 \tag{B.1}
$$
这里 $\vartheta$ 是该固定选择，**不**随尾标签变动。
实际半径和高度为
$$
 a(u)=a_*e^{-\omega u-\psi(u)},\qquad z_u=a^2/4,
 \qquad \widetilde\omega=\omega+\psi_u.
 \tag{B.2}
$$
R74 给整个连续区间的准确界
$$
 7/5<\omega<3/2,\quad
 |\psi_u|\le15/16384,\quad |\psi_{uu}|\le3/16.
 \tag{B.3}
$$
因此 $a$ 严格单调。在物理半径上取正参考高度斜率，并由 $u=T$
向外取时间，得到
$$
 w=\frac{a}{4\widetilde\omega},\quad
 t=\log(a/a_T),\quad
 A=\frac{aw_a}{w}=1+\frac{\psi_{uu}}{\widetilde\omega^2}.
 \tag{B.4}
$$
例如 $\widetilde\omega>11/8$，故 $|A-1|<12/121<1/8$。
这里不是把实际正曲率段替换成常 $A=1$；(B.4) 的变系数完整进入
R119 (119.8) 的相对方程。

两个端点的 $\psi,\psi_u,\psi_{uu}$ 均为0，实际对数半径长度准确是
$$
 L_b=\omega(T-B)=25\omega/8<75/16.
 \tag{B.5}
$$
并且 $w/a<2/11<5/18$。所以 R119 已逐项证明的全部相对 PDE、完整
mean、能源常数32、角宽下降率16及物理水平重建预算都适用于这段。

## 2. 带权原标签的真实全部输出

使用 [整个 connector 续篇](R119-supplement-full-installed-connector-with-paid-label-weight.md)
已经明示支付的同一输入域
$$
 \|a\|_{\ell^1_{8192}}<1/4,
 \qquad X_\beta:=\|X^{[8192]}(a)\|<\frac{13}{4}\|a\|_{\ell^1_{8192}}<1.
 \tag{B.6}
$$
此处标签 $a$ 与物理半径 $a(u)$ 的角色由其下标/自变量区分。
在 $u=T$，原连续解于宽度大于 $\tau+2064$ 上满足
$N<2^{-8723}X_\beta$，其中 $\tau=5177/400$。
从已获得的宽度 $\tau+2048$ 启动这段相对演化。由于
$$
 16L_b<75,\qquad e^{32L_b}<e^{150}<2^{300},
$$
完整真解满足
$$
 \boxed{\quad
 N_{\tau+2048-16t}(t)<2^{-8423}X_\beta,
 \qquad 0\le t\le L_b.
 \quad}                                                     \tag{B.7}
$$
全过程仍在 $1/64$ 复相对球内。新的真实角宽表为

| 数据 | 已付原物理角宽 |
|---|---:|
| 双 bump 输入 | $\tau+2048$ |
| 连续相对状态最小宽度 | $>\tau+1973$ |
| $u=B$ 完整 raw 两迹 | $\tau+1968$ |
| $u=B$ 完整 grounded 两迹 | $\tau+1967$ |

这只是已有带权标签 chart 的继续，不增加标签域或改变绝对宽度合同。
全部非线性生成的高模继续保留。R119 的 $M_t=0$ 保留同一个 $M=1$
分支，平均高度仍按 $u_t=awK$ 积分，不在 $T$ 或 $B$ 重置。
完整二 jet 在两个端点按同一 PDE 接合。由 $w/a<5/18$ 及原物理估计，
新段上的完整水平/垂直 $C^2$ 改变量（除共同平移）小于
$2^{17}\sup N<2^{-8406}X_\beta$。

## 3. 真实尾与非线性正段的相同单位

在 $u=B$，记真实尾给出的相对非mean高度和斜率为
$$
 f_B(a)=\frac{(v_B)_\perp}{a_Bw_B},\qquad
 k_B(a)=\frac{(v_a)_\perp(B)}{w_B},\qquad
 \lambda_B(a,\lambda)=(v_B)_0.
 \tag{B.8}
$$
其中共同高度平移 $\lambda$ 独立保留。$P=(f_B)_\theta$，
$U=(f_B)_{\theta\theta}$，因此在任何 $\sigma\le\tau+1968$ 上
$$
 \sum_{m\ne0}e^{\sigma|m|}|m|^2|(f_B)_m|
 \le N<2^{-8423}X_\beta.
 \tag{B.9}
$$
而 $k_B$ 的加一角导范数由同一个 $V=K_\theta$ 控制。

现在给外端非mean Dirichlet 数据 $f_*$，取实际物理角宽
$\sigma=1/512$，并要求
$$
 \sum_{m\ne0}e^{\sigma|m|}|m|^2|(f_*)_m|\le2^{-26}.
 \tag{B.10}
$$
由 (B.6)、(B.9)，两端边界 norm 严格小于 $2^{-25}$。
所以 [长段非线性 Dirichlet 续篇](R119-supplement-actual-long-radial-nonlinear-dirichlet-problem.md)
给真实完整解 $h=\mathcal D(f_B(a),f_*)$；不是重新假设一个 Dirichlet map。
记该篇长段时间为 $\widehat t=\omega(B-u)$，长度
$L=\omega B$，$\widehat t=0$ 就是同一物理 $u=B$。

为避免隐藏 mean 方程，完整接合条件可准确分成：

1. 非mean高度已由 Dirichlet 条件等同。
2. 全部非mean斜率满足
   $k_B(a)=2f_B(a)+h_{\widehat t}(0)$。
3. 平均高度在内端取 $v_0(0)=\lambda_B(a,\lambda)$。
   外端平均高度输出为
   $\lambda_B+\int_0^L awK_0\,d\widehat t$。
4. mean 斜率无需再任意指定：一旦前两项成立，两侧有完全相同的
   $P,U,K_\perp,V$，而且都用同一 $M=1$ 小根，所以 $K_0$ 准确相同。

最后一项是由真实 holonomy 唯一性得到的等式，不是删除 mean 行。
外端平均高度及其通量仍要与主体的增广 mean/regular 方程联立。

## 4. 全频非线性匹配算子的准确形式

对 $M=|m|\ge4$ 定义对角算子
$$
 (\mathsf C_L f)_m=M\coth(ML)f_m,
 \qquad
 (\mathsf S_L f)_m=M e^{2L}\operatorname{csch}(ML)f_m.
 \tag{B.11}
$$
它们来自真实有限区间的两端 lift，保留全部反射项。
若 $h_D$ 是完整线性 Dirichlet 解，准确有
$$
 2f_B+(h_D)_{\widehat t}(0)=-\mathsf C_L f_B+\mathsf S_L f_*.
 \tag{B.12}
$$
定义已构造的非线性输出
$$
 \mathcal E_D(f_B,f_*)=(h-h_D)_{\widehat t}(0),\qquad
 \|\mathcal E_D\|_{\sigma,1}\le2^{13}\|h\|_{\mathcal Y_\sigma}^2.
 \tag{B.13}
$$
$\|g\|_{\sigma,1}=\sum_{m\ne0}e^{\sigma|m|}|m||g_m|$。
系数 $2^{13}$ 仍是前篇为**两端合计**支付的常数，故这里可直接使用。

于是全部非mean匹配是一个具体的已定义 map：
$$
 \boxed{\quad
 \mathcal F(a,f_*):=
 k_B(a)+\mathsf C_L f_B(a)-\mathsf S_L f_*
       -\mathcal E_D(f_B(a),f_*)=0.
 \quad}                                                     \tag{B.14}
$$
所有项来自同一 metric、同一物理切口、同一已选双 bump；没有接入一个
方便的人工 Robin 行。真实 normal/grounded 两迹通过 R119
(119.31)–(119.34) 的完整水平位移及 shear 转换取得，两侧 outward 符号相反。

## 5. 原点的实际全频相对两迹横截，不假设高度非零

现在只计算 (B.14) 的真实原点线性化。R74 的真实尾线
$\Lambda_M(B)$ 在状态 $Y=(y,y_u/M)$ 中与 $(1,\omega)$ 满足
$|\sin\angle|\ge\epsilon_*=2^{-39}$。
R74 的真实北向高度变分公式为
$$
 C=4(\omega y-y_u/M^2).
$$
本篇正参考高度扰动为 $v=-C$。在同一端点用 $a_u=-\omega a$、
$w=a/(4\omega)$ 微分，得到
$$
 \begin{pmatrix}f_B\\ k_B/M\end{pmatrix}
 =-\frac{16\omega}{a_B^2}
 \underbrace{\begin{pmatrix}\omega&-1/M\\ \omega/M&-1\end{pmatrix}}_{\mathsf J_M}
 \begin{pmatrix}y\\y_u/M\end{pmatrix}.
 \tag{B.15}
$$
这个共同负号保留真实北帽高度约定，不改变以下角距界。
式子同时包含高度与径向迹，且矩阵行列式
$-\omega(1-M^{-2})$ 不为0。
设 $x=(f_B,k_B/M)$，$Y$ 位于真实尾线。因
$$
 (1,1)\mathsf J_M=(1+1/M)(\omega,-1),\qquad
 \|\mathsf J_M\|_2\le\sqrt{(1+\omega^2)(1+M^{-2})},
$$
且 $(1+1/M)^2\ge1+M^{-2}$，所以 R74 的真实角距给
$$
 |f_B+k_B/M|\ge\epsilon_*\,|x|_2.
 \tag{B.16}
$$
这里没有除以 $f_B$，故包含高度可能为0的全部频率。

实际 $L>16$。利用 $M\ge4$、$e>2$，
$$
 0<\coth(ML)-1
 =\frac{2e^{-2ML}}{1-e^{-2ML}}
 <4\,2^{-128}=2^{-126}<\epsilon_*/2.
$$
把这个准确有限长度反射项加入 (B.16)，得到
$$
 \boxed{\quad
 \left|k_B/M+\coth(ML)f_B\right|
 \ge2^{-40}\left(|f_B|^2+|k_B/M|^2\right)^{1/2}.
 \quad}                                                     \tag{B.17}
$$
因此原点线性匹配对每条真尾线有相对逆常数 $2^{40}$，并且可在任何
固定 $\sigma$ 对全部模乘 $M^2e^{\sigma M}$ 后求和；没有删高模。
例如只给外端 $f_*$ 时，真实线性内端两迹满足
$$
 \left(|f_B|^2+|k_B/M|^2\right)^{1/2}
 \le2^{42}e^{-(M-2)L}|(f_*)_m|
 \le2^{42}e^{-ML/2}|(f_*)_m|.
 \tag{B.18}
$$
这证明长正段给的是完整两迹筛选，而非只筛选高度。
从这个真实状态回到内部标签，仍须使用 R15 已证明的真实标签权；
本篇并未把各模内部标签当成单位切口高度。

## 6. 非线性逆还缺的相对估计

(B.17) 完整支付了 (B.14) 在原点的两迹方向，并不能把非线性尾迹
直接替换为这条直线。一个足够但尚未证明的下一门是：在适当的完整
轨迹/边界 Banach 空间中，用 (B.17) 的真实线性逆预条件后，证明
$$
 \left\|[D_a\mathcal F(0,0)]^{-1}
       \big(D_a\mathcal F(a,f_*)-D_a\mathcal F(0,0)\big)\right\|<1,
 \tag{B.19}
$$
并支付该逆在同一内部标签域以及实际 ordinary-source 输入上的范围。
也可以用有明确角宽/阶数损失的另一完整迭代定理替代 (B.19)，但其假设
必须对本处 $\mathcal F$ 实际证明。

现有 $D^2X$ 的绝对标签 norm 和 $2^{-8423}$ 输出小量不证明 (B.19)：
高模线性标签到切口的幅度本身可很小，预条件会除去该幅度。
R15 的 $e^{391M}$ 标签费用只把这一逆费用量化，没有把固定角宽损失
变成同宽有界算子。混合段的高频相位也不能由小系数扰动自动得到
全频 operator-norm 小差。

本篇因而完成了实际尾+整个 connector+双 bump 的全部两迹，并给出
真实非线性 BVP 的唯一剩余匹配方程；未把尚缺的全高邻域门隐去。

[准确算术程序](../scripts/fourfold_two_bumps_matching_20261113.py) 与
[完整报告](../notes/2026-11-13-R119-two-bumps-matching-budget.json)
核所有有理长度、角宽、相对球、真实两迹矩阵与横截费用。
