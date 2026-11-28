# R12 附录：增生复杂分母的同一头尾单位、真像与多项式对数费用

日期：2026-11-29（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127，stable_kernel_return。AI-assisted，GPT-6 Astra Pro。

**状态：完整的实际分母与同分子费用定理。** 本稿接[复杂增生逆幂与全旗来源](R12-appendix-accretive-complex-inverse-powers-flat-divisibility-layers-and-all-flag-sources.md)，证明其中每个固定复杂分母与任意纯尾分母相差一个费用至多为 $\log L$ 的固定次幂的有界单位；两者的实际像完全相同。若已有同一有界分子，本稿把它运输到每个纯尾平方方程并支付运输费用。未构造这样的分子。

## 1. 原算子与同一有限头

固定原 Haar 尾 $C=A^{(m_0)}$，$m_0\ge0$。沿用[真实行及 carry](R181-bounded-coefficient-bell-polynomial-spectrum-trichotomy.md)的
$$
N_j=C^{2^j}/d_j,\qquad d_j=\|C^{2^j}\|,\qquad
V_j=(I-N_j)(I+N_j)^{-1},\qquad a_j=(j+1)^{-1}.
$$
这里保留完整 $V_j$，不把它换成纯一位矩阵。记
$$
Z=I+\sum_{j\ge0}a_jV_j,\qquad
Z_L=I+\sum_{j\ge L}a_jV_j,\qquad
H_L=\sum_{j<L}a_jV_j,\qquad L\ge1.
\tag{1}
$$
两个无穷和均指原闭增生实现；$Z=Z_L+H_L$ 的准确域为
$$
D(Z)=D(Z_L).
\tag{2}
$$
它们都是最大增生算子，实部至少为 $I$，谱为空。$H_L$ 有界、增生，并与两者的实际域及预解式交换。原 $\|V_j\|<3$ 给
$$
h_L:=\|H_L\|\le3\sum_{j<L}\frac1{j+1}
\le3(1+\log L).
\tag{3}
$$
由原 dyadic 张量式，每个 $j\ge L$ 的 $V_j$ 只作用于第 $L$ 位起的尾，故
$$
Z_L=I_{<L}\otimes Z^{[L]}.
\tag{4}
$$
该恒等式含全部 carry；$Z^{[L]}$ 的系数为原 $a_L,a_{L+1},\ldots$，没有重新设成从 $1$ 开始的另一行。

对 $\operatorname{Re}\theta>0$，用前稿同一 Gamma 积分定义
$$
P_\theta=Z^{-\theta},\qquad Q_{\theta,L}=Z_L^{-\theta}.
\tag{5}
$$
它们是有界、单射稠值的原交换子，并保持全部原闭不变旗。特别
$$
\|P_\theta\|,\ \|Q_{\theta,L}\|
\le g_\theta:=\frac{\Gamma(\operatorname{Re}\theta)}{|\Gamma(\theta)|}.
\tag{6}
$$
相应正幂 $Z^\theta=P_\theta^{-1}$、$Z_L^\theta=Q_{\theta,L}^{-1}$ 均指实际闭逆。

定义唯一固定单位
$$
U_L=I+H_LQ_{1,L}.
\tag{7}
$$
$H_LQ_{1,L}$ 拟幂零，因为有界两因子交换且 $Q_{1,L}$ 拟幂零。因此 $\sigma(U_L)=\{1\}$，所有 $U_L^\theta$ 都取围绕 $1$ 的同一全纯对数芽。实际逆差还给
$$
U_L^{-1}=I-H_LP_1.
\tag{8}
$$

## 2. 先付真分数幂域及两向费用

设 $0<s:=\operatorname{Re}\alpha<1$。在公共域 (2) 上，原 Gamma 幂的 Balakrishnan 表示给
$$
Z^\alpha-Z_L^\alpha=B_{\alpha,L},
$$
其中右边有全域有界延拓
$$
B_{\alpha,L}
=\frac{\sin(\pi\alpha)}{\pi}
\int_0^\infty
t^\alpha(t+Z)^{-1}H_L(t+Z_L)^{-1}\,dt.
\tag{9}
$$
积分按算子范数收敛。实部下界给两预解式范数至多 $(1+t)^{-1}$，所以
$$
\|B_{\alpha,L}\|
\le b_\alpha h_L,\qquad
b_\alpha=
\frac{|\sin(\pi\alpha)|}{\pi}
\Gamma(1+s)\Gamma(1-s).
\tag{10}
$$
这里 $\int_0^\infty t^s(1+t)^{-2}dt=\Gamma(1+s)\Gamma(1-s)$。

为明确域的来源，Balakrishnan 式先对 $x\in D(Z)=D(Z_L)$ 使用：将
$Z(t+Z)^{-1}=I-t(t+Z)^{-1}$ 相减，准确逆差给 (9)。两端正幂与前稿的 Gamma 负幂互逆，可先在此域用 Beta 恒等式相乘核对。前稿的同一 Yosida 强单位又表明 $D(Z)$ 是 $Z^\alpha$ 的图核心，$D(Z_L)$ 是 $Z_L^\alpha$ 的图核心。故公共核心上的有界差经闭包给
$$
\boxed{D(Z^\alpha)=D(Z_L^\alpha),\qquad
Z^\alpha=Z_L^\alpha+B_{\alpha,L}.}
\tag{11}
$$
并没有从形式的分数幂乘法预设域相同。

于是实际算子
$$
W_\alpha=Z^\alpha Q_{\alpha,L}
=I+B_{\alpha,L}Q_{\alpha,L}
$$
全域有界。它的真正双向逆为
$$
W_\alpha^{-1}=Z_L^\alpha P_\alpha
=I-B_{\alpha,L}P_\alpha.
\tag{12}
$$
例如第一种乘积中，$Q_{\alpha,L}$ 的像恰为 (11) 的公共域；第二种乘积同样如此。两次相消均在已付域内。由 (6)、(10)，
$$
\|W_\alpha\|,\ \|W_\alpha^{-1}\|
\le1+D_\alpha h_L,\qquad D_\alpha=b_\alpha g_\alpha.
\tag{13}
$$

## 3. 核对同一个对数芽

不能仅凭无界形式 $Z^\alpha Z_L^{-\alpha}$ 声称它是 $U_L^\alpha$。这里直接保留同一路径。

令
$$
Z_\tau=Z_L+\tau H_L,\qquad 0\le\tau\le1,
\qquad
W_\alpha(\tau)=Z_\tau^\alpha Q_{\alpha,L}.
$$
所有 $Z_\tau$ 实部至少为 $I$。在每个实 $\tau$ 的一个复邻域中，其实部仍有固定正下界；有界交换扰动及 Gamma 积分使 $Z_\tau^{-\alpha}$ 按算子范数全纯，并给
$$
\frac d{d\tau}Z_\tau^{-\alpha}
=-\alpha H_L Z_\tau^{-1}Z_\tau^{-\alpha}.
\tag{14}
$$
(9) 的同一路径积分还给 $W_\alpha(\tau)$ 的范数可微性。对准确的有界身份
$$
Z_\tau^{-\alpha}W_\alpha(\tau)=Q_{\alpha,L}
$$
求导，再用 $Z_\tau^{-\alpha}$ 单射，得到
$$
W_\alpha'(\tau)
=\alpha H_L Z_\tau^{-1}W_\alpha(\tau)
=\alpha R_L(I+\tau R_L)^{-1}W_\alpha(\tau),
\quad R_L=H_LQ_{1,L},
\quad W_\alpha(0)=I.
\tag{15}
$$
有界算子常微分方程的唯一解为
$(I+\tau R_L)^\alpha$，其中对数沿谱 $\{1\}$ 的原芽取得。因此
$$
\boxed{W_\alpha=U_L^\alpha.}
\tag{16}
$$
这也同时核对了负幂所用的分支。

现固定任意 $\operatorname{Re}\theta>0$，取整数 $m>\operatorname{Re}\theta$，设 $\alpha=\theta/m$。前稿真实半群律与 (16) 都在有界交换子中成立，故
$$
P_\theta U_L^\theta
=(P_\alpha U_L^\alpha)^m=Q_{\alpha,L}^m
=Q_{\theta,L}.
$$
从而
$$
\boxed{P_\theta=Q_{\theta,L}U_L^{-\theta},\qquad
\|U_L^{\pm\theta}\|
\le B_{\theta,L}:=(1+D_{\theta/m}h_L)^m.}
\tag{17}
$$
特别，对固定 $\theta$ 和选定 $m$，
$$
B_{\theta,L}=O_\theta((1+\log L)^m).
\tag{18}
$$
这是同一个 $U_L$ 的两向实际费用，没有随正负幂更换单位。

## 4. 实际像相同及低位矩阵作用

(17) 的有界可逆因子给
$$
\boxed{\operatorname{Ran}P_\theta
=\operatorname{Ran}Q_{\theta,L}
=H_{<L}\otimes\operatorname{Ran}(Z^{[L]})^{-\theta}.}
\tag{19}
$$
末端 $H_{<L}$ 有限维，故这里的张量像就是有限个实际尾像的直和；不是把像换成闭包。

因此每个低 $L$ 位有界矩阵 $E=E_{<L}\otimes I$ 都保持同一个源域 $\operatorname{Ran}P_\theta$。准确运输为
$$
E P_\theta=P_\theta K_{E,L},\qquad
K_{E,L}=U_L^\theta E U_L^{-\theta},
\qquad
\|K_{E,L}\|\le B_{\theta,L}^2\|E\|.
\tag{20}
$$
于是对 $x\in\operatorname{Ran}P_\theta$，
$$
P_\theta^{-1}Ex=K_{E,L}P_\theta^{-1}x.
\tag{21}
$$
这给源域上的真正图范数控制。一般低位矩阵 $E$ **不属于** $C'$；(20) 只付它对这个分母源域的作用，不声称它保持原未知不变子空间，也不声称它与原算子交换。

## 5. 纯尾源确实强*趋于单位

令 $\Lambda=I+\mathcal N$ 为原物理孔数权，$X_{\ge L}=Z_L-I$。R181 的完整 carry 估计给
$$
\|X_{\ge L}u\|
\le D_0\|a_{\ge L}\|_2\|\Lambda u\|,
\qquad u\in D(\Lambda).
\tag{22}
$$
其最大增生半群为收缩，故
$$
\|(e^{-tX_{\ge L}}-I)u\|
\le t\|X_{\ge L}u\|.
$$
代回 (5) 的 Gamma 积分，得到对 $s=\operatorname{Re}\theta>0$ 的准确向量界
$$
\boxed{
\|(Q_{\theta,L}-I)u\|
\le
\frac{\Gamma(s+1)}{|\Gamma(\theta)|}
D_0\|a_{\ge L}\|_2\|\Lambda u\|.
}
\tag{23}
$$
原 $J$ 对称性、$J\Lambda=\Lambda J$ 给伴随的同一估计（参数取共轭）。由于 (6) 一致有界且 $D(\Lambda)$ 稠密，
$$
\boxed{Q_{\theta,L}\longrightarrow I\quad\text{强*}.}
\tag{24}
$$
每个固定原不变旗商采用其固定正交代表空间压缩，(24) 也传给该商；乘法恒等式依原旗不变性传递。这里不需要所有纯尾域彼此有统一逆范数。

## 6. 同一未知分子的准确尾平方方程

现在只作下列条件陈述。若存在一个实际有界 $Y\in C'$ 满足
$$
Y^2=C P_\theta^2,
\tag{25}
$$
则对每个 $L$ 定义
$$
Y_L=Y U_L^\theta.
$$
所有因子均在同一原交换代数中，故
$$
\boxed{
Y_L^2=C Q_{\theta,L}^2,\qquad
\|Y_L\|\le B_{\theta,L}\|Y\|.
}
\tag{26}
$$
右边的同一分母在范数有界且强*趋于 $I$；对 $u\in D(\Lambda)$，(6)、(23) 还给
$$
\|(Y_L^2-C)u\|
\le
\|C\|(g_\theta+1)
\frac{\Gamma(s+1)}{|\Gamma(\theta)|}
D_0\|a_{\ge L}\|_2\|\Lambda u\|.
\tag{27}
$$
即 (25) 若有解，会产生保同一 $Y$、费用仅为 (18) 的全部真尾平方来源。每个 $Q_{\theta,L}$ 被低 $L$ 位的原有限循环相位固定，故 (26) 也给同一低位归一化；没有把 $Y_L$ 替换成自由选择的有限矩阵根。

(19)–(21) 是分母的源域结论。它们不推出 $Y_L$ 保持低位矩阵、不推出未知最大根域被所有这些矩阵保持，也不把多项式对数范数上界提升为 $Y_L\Omega$ 的强紧性。(25) 的有界平方分子尚未得到，原普通 ISP 仍未完成。
