# R150：同一原 sigma 的二生成值商、十六个原小行列式与消元理想平方界

日期：2026-11-29（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。GPT-6 Astra Pro（AI-assisted）。

**状态：已证明；完整纸面身份，无新执行。** 将完整 NV、两个完整个别奇 N/P 及第三矩放在同一个原二矩代数中，得到真正的 $2\times8$ 原乘法呈示。其28个最大子式由16个显示多项式生成；每个都有原方程组合，不倒值头、不倒 D。固定全部系数的代数闭点上，它们同时为零，当且仅当四条原值条件与二矩有同一个 sigma 解。

这只完整处理本文列出的原值条件；其余原 Gram 均值、加权条件和物理局部化仍须保留。本文没有整 Phi/W/HK 排空、权有限性或普通 ISP 的完成结论。

## 1. 原环与四条同点值条件

令 $\mathcal A$ 为当前原图的系数环，包含权和原 Gram 几何系数，已支付 $2,\ell,M,\delta$。所有下列分母都限于这些旧单位；涉及旧 Low 的比较才另用已付 m。可取一般原图，也可作正确 Phi 或 W 的同点仿射恢复。没有使用错 compact E1 或错 Rbar。

取
$$
\rho^2=\delta,\quad
\ell=b+c,\quad m=\rho(b-c),\quad
M=4bc\delta=\ell^2\delta-m^2,
$$
$$
A_\lambda=2\lambda^2-2\lambda+1,\qquad
B_\lambda=4\lambda^3-6\lambda^2+3\lambda-1,
$$
$$
D=\ell A_\lambda-T^2,\qquad
K=\ell^2B_\lambda-3\ell TA_\lambda+2T^3,\qquad
A_0=1+T/\ell.
$$
原一次矩的完整同点参数化为
$$
h=A_0+(m/\ell-\rho)\sigma,\qquad
k=A_0+(m/\ell+\rho)\sigma.
\tag{1}
$$
这里始终是同一个 sigma；不为不同误差分别选择根。置
$$
d=D/M,\qquad q_0=\sigma^2-d,\qquad q=Mq_0.
$$
原第二、第三移位矩误差满足
$$
q=\ell E_2,\qquad
H:=K-2mD\sigma=(3T+2m\sigma)q-\ell^2E_3.
\tag{2}
$$
因此，在已付 ell、M 的原环，$(q_0,H)$ 与 $(E_2,E_3)$ 完整等价。

依[完整 NV 三短式](R150-appendix-unit211-general-scaled-entire-N4-three-compact-identities.md)，写整个缩放值形式
$$
\mathcal N=\ell^2N_4(\mathbf V)
=Z_0+Z_1\sigma+Z_2\sigma^2.
\tag{3}
$$
其中 $\mathbf V=(1,\lambda-1-T,h,k)$，三个 $Z_i$ 来自整个原二次型；没有选取某个坐标或最高齐次项。

依[完整个别奇 N/P](R150-appendix-unit211-general-original-odd-NP-two-direct-sextic-norms.md)，令 $N_b,P_b$ 为两共轭 singleton 原形式的奇坐标。完整误差为
$$
E_N=N_b+4\lambda P_{02}(A_0+m\sigma/\ell)\sigma,
$$
$$
E_P=P_b+P_{02}\left[
3(A_0+m\sigma/\ell)^2\sigma+\delta\sigma^3\right].
\tag{4}
$$
它们分别是两个原 singleton 误差之差除以 $2\rho$。$\rho^{-1}=\rho/\delta$ 已付；保留原加权误差后，由 ell 单位可恢复两个个别误差。本文不丢弃这些加权误差。

用 $i=V,N,P,H$ 标记四条线性余式
$$
L_i=a_i+b_i\sigma.
$$
其全部系数是
$$
\begin{aligned}
a_V&=Z_0+dZ_2,& b_V&=Z_1,\\
a_N&=N_b+\frac{4\lambda P_{02}mD}{\ell M},
&b_N&=4\lambda P_{02}A_0,\\
a_P&=P_b+\frac{6P_{02}A_0mD}{\ell M},
&b_P&=P_{02}\left[3A_0^2+
 \left(\frac{3m^2}{\ell^2}+\delta\right)d\right],\\
a_H&=K,&b_H&=-2mD.
\end{aligned}
\tag{5}
$$
为显示完整原来源，另记
$$
\begin{aligned}
c_V&=Z_2,\\
c_N&=4\lambda P_{02}m/\ell,\\
c_P(\sigma)&=P_{02}\left[
 6A_0m/\ell+\left(3m^2/\ell^2+\delta\right)\sigma\right],\\
c_H&=0.
\end{aligned}
$$
令 $(F_V,F_N,F_P,F_H)=(\mathcal N,E_N,E_P,H)$，则有完整多项式身份
$$
\boxed{\quad F_i=L_i+c_iq_0,\qquad i=V,N,P,H.\quad}
\tag{6}
$$
这里使用的是 $q_0$；若用原 $q=Mq_0$，各 $c_i$ 必须除以 M。这个尺度区别不能省略。

## 2. 真正的二生成商与八列

环境代数
$$
\mathcal B=\mathcal A[\sigma]/(q_0)
$$
因 $q_0$ 首一而在 $\mathcal A$ 上自由，基为 $(1,\sigma)$。定义整个本文值商
$$
\mathcal M=\mathcal B/(L_V,L_N,L_P,L_H)
\cong
\mathcal A[\sigma]/(q_0,\mathcal N,E_N,E_P,H).
\tag{7}
$$
式(7)是环同构，来自(6)的双向替换。完整原物理商还须加其余原条件；本文并不称它自由或平坦。

对每个 i，理想中全部 $\mathcal B$ 倍数由实际两列 $L_i,\sigma L_i$ 生成，因为每个环境元素恰为 $r+s\sigma$。在上述自由基中这两列为
$$
v_i=\binom{a_i}{b_i},\qquad
w_i=\binom{db_i}{a_i}.
\tag{8}
$$
第二列来自真正乘法 $\sigma(a_i+b_i\sigma)=db_i+a_i\sigma$，不是任意凑合的二列模型。因此
$$
\boxed{
\mathcal A^8\xrightarrow{\ \mathscr P\ }\mathcal A^2
\longrightarrow\mathcal M\longrightarrow0,\qquad
\mathscr P=(v_V,w_V,v_N,w_N,v_P,w_P,v_H,w_H)
}
\tag{9}
$$
是完整有限呈示。没有通过某个 $a_i,b_i,D$ 的逆缩成一条根，也没有把三均值的非自由商当作自由乘法代数。

## 3. 28个最大子式的16个生成元

定义四个范数型式、六个交叉式和六个混合式：
$$
n_i=a_i^2-db_i^2,\qquad i=V,N,P,H,
\tag{10}
$$
$$
c_{ij}=a_ib_j-a_jb_i,\qquad
s_{ij}=a_ia_j-db_ib_j,\qquad i<j.
\tag{11}
$$
这里的大小顺序固定为 $V<N<P<H$；名称中的 $c_{ij}$ 与(6)的单下标 $c_i$ 不同。

直接取(8)的行列式：
$$
\begin{aligned}
\det(v_i,w_i)&=n_i,\\
\det(v_i,v_j)&=c_{ij},\\
\det(v_i,w_j)&=s_{ij},\\
\det(w_i,v_j)&=-s_{ij},\\
\det(w_i,w_j)&=-d\,c_{ij}.
\end{aligned}
\tag{12}
$$
故零阶 Fitting 理想恰是
$$
\boxed{
\mathfrak F=\operatorname{Fitt}_0^{\mathcal A}(\mathcal M)
=(n_i,\ c_{ij},\ s_{ij}).
}
\tag{13}
$$
等号只说16个显示式生成全部28个最大子式；不说这些生成元独立或最少，也不说 Fitting 理想已经等于整个消元理想。

每个生成元都返回原理想，不只在点集上消失：
$$
\boxed{
\begin{aligned}
n_i&=(a_i-b_i\sigma)L_i+b_i^2q_0,\\
c_{ij}&=b_jL_i-b_iL_j,\\
s_{ij}&=a_jL_i-b_i\sigma L_j+b_ib_jq_0.
\end{aligned}}
\tag{14}
$$
再把 $L_i=F_i-c_iq_0$ 代入，实际原乘子为
$$
\begin{aligned}
n_i&=(a_i-b_i\sigma)F_i+
 [b_i^2-(a_i-b_i\sigma)c_i]q_0,\\
c_{ij}&=b_jF_i-b_iF_j+
 (b_ic_j-b_jc_i)q_0,\\
s_{ij}&=a_jF_i-b_i\sigma F_j+
 [b_ib_j-a_jc_i+b_i\sigma c_j]q_0.
\end{aligned}
\tag{15}
$$
最后用(2)将 $q_0,H$ 返回 $E_2,E_3$，就得到原第二矩、第三矩、完整 NV 及两对个别误差的组合。所有原分母已列出；D=0、各 $a_i=0,b_i=0$ 或任何新首项为零的整面均受(15)覆盖。

## 4. 与真正消元理想的平方夹逼

置
$$
\mathfrak J=
(q_0,\mathcal N,E_N,E_P,H)\cap\mathcal A.
$$
因为 $\mathcal M$ 是含单位的商代数，
$$
\mathfrak J=\operatorname{Ann}_{\mathcal A}(\mathcal M).
\tag{16}
$$
确实，标量杀死整个代数必杀死其1；反过来标量在代数中为0便杀死全部元素。

每个最大子式用两列伴随矩阵便杀死 $\operatorname{coker}\mathscr P$，或直接用(15)，得 $\mathfrak F\subseteq\mathfrak J$。还有统一的反向平方包含：
$$
\boxed{\qquad
\mathfrak J^2\subseteq\mathfrak F\subseteq\mathfrak J.
\qquad}
\tag{17}
$$
完整证明如下。任取 $a,b\in\mathfrak J$。因为它们杀死余核中 $(1,0)$ 与 $(0,1)$ 的像，存在 $x,y\in\mathcal A^8$ 使
$$
\mathscr P x=\binom{a}{0},\qquad
\mathscr P y=\binom{0}{b}.
$$
对 $2\times2$ 矩阵 $\mathscr P(x,y)$ 作 Cauchy–Binet 展开，
$$
ab=\det\bigl(\mathscr P(x,y)\bigr)
=\sum_{r<s}\det(\mathscr P_{r,s})
              \det\begin{pmatrix}x_r&y_r\\x_s&y_s\end{pmatrix}\in\mathfrak F.
$$
任意 $\mathfrak J^2$ 元素是此类乘积的和，(17)得证。这是原二生成呈示给出的精确幂界，没有借剩余模计算或对某个目标猜幂。

尤其
$$
\sqrt{\mathfrak F}=\sqrt{\mathfrak J}.
\tag{18}
$$
但(17)不准把 $\mathfrak F=\mathfrak J$ 写成无条件结论，也不准在非约化商中直接删平方。该平方界针对本文值消元理想；不据它推整个原几何商或普通 ISP 的幂零界。

## 5. 固定全部系数时准确的同根判据

任取使原已付单位均非零的代数闭特征零系数点 $\xi$。将(9)右正合地张量到剩余域 $\mathbb C$，得到
$$
\mathcal M_\xi\cong
\mathbb C[\sigma]/
(q_{0,\xi},L_{V,\xi},L_{N,\xi},L_{P,\xi},L_{H,\xi})
=\operatorname{coker}(\mathscr P_\xi).
$$
因此下列条件严格等价：

1. 本文16个多项式在 $\xi$ 全部为零；
2. $\operatorname{rank}\mathscr P_\xi<2$；
3. $\mathcal M_\xi\ne0$；
4. 存在同一个 $\sigma\in\mathbb C$，同时满足原二矩、第三矩、完整 NV 与两个完整奇 N/P 条件。

前三项是二行矩阵的秩判据。第3到第4项因为非零有限维含单位 $\mathbb C$ 代数有最大理想，剩余域只能是 $\mathbb C$；把 sigma 投到该剩余域即可。反向由同一 sigma 的取值映射给非零商。

这里没有先选定哪个范数来自哪个根。仅取各个 $n_i=0$ 不充分：抽象二次代数 $d=1$ 中，$L_1=1+\sigma,L_2=1-\sigma$ 的两个范数都为0，但二者没有共同零点，且 $c_{12}=-2$。这个例子只说明代数差别，不声称是实际 Phi/W 权点。

固定点上，
$$
\dim_\mathbb C\mathcal M_\xi=2-\operatorname{rank}\mathscr P_\xi\le2.
\tag{19}
$$
若 $D_\xi\ne0$，二次环境裂为 $\mathbb C\times\mathbb C$，所以其任意商约化，非零值纤维长度为1或2。若 $D_\xi=0$，环境是双数 $\mathbb C[\sigma]/(\sigma^2)$，长度2的幂零纤维仍保留；可能再被原线性式缩成长度1或零。

(19)只计固定全部系数后的 sigma 值纤维，不计仍自由的权、其它 Gram 几何变量、原整体归一尺度或其它覆盖。不能由它推出整个原权集有限。

## 6. 已刊原范数、Low 与真正的新交叉

四个(10)与已刊源的尺度恰为
$$
\begin{aligned}
M^2 n_V&=(MZ_0+DZ_2)^2-MDZ_1^2=C_{NV},\\
M n_N&=C_N,\qquad M n_P=C_P,\\
M n_H&=MK^2-4m^2D^3=R_6.
\end{aligned}
\tag{20}
$$
M 是已付单位，所以这些只是同一原来源的准确尺度，不能把三个独立范数误作同根充分条件。

在另已付 m 的原图，定义
$$
\operatorname{Low}_i=D a_i+\frac K{2m}b_i.
$$
便有
$$
a_Hb_i-a_ib_H=K b_i+2mD a_i
=2m\operatorname{Low}_i.
\tag{21}
$$
$i=N,P$ 时这是已刊 $N_{\rm low},P_{\rm low}$；$i=V$ 时，因为本页用 $\mathcal N=\ell^2N_4(\mathbf V)$，它是旧未缩放 $V_{\rm low}$ 的 ell 平方倍。这个尺度保留，不能把缩放与未缩放系数混用。

因此与 H 的三个交叉是旧 Low。新的 NV–N、NV–P 交叉来自其它两个 $c_{ij}$；其原(15)不需 H、D 或值头的逆。新独立源 b53edcc91babd2931dac68ef482744c6027f20f1 正计算它们的正确 Phi 普通三均值迹和一个预定三原行标量，本页不预报该执行结果。

以 lambda、T 和原 Gram 线性几何变量的总次数计，
$$
\deg a_i\le3,\qquad \deg b_i\le2,\qquad \deg d\le2.
$$
因此全部交叉至多五次，全部范数和混合式至多六次。正确同点仿射恢复保持这些上界；分母只在旧纯权系数中。此处不宣称各式必非零、达到上界、不可约或互素。

## 7. 使用范围与来源

本文用(6)、(8)、(12)、(15)和 Cauchy–Binet 完成全证明，无新整数执行或验收门。特别没有恢复旧错 Rbar，也没有续算任何冻结的 Q 主分量、旧权投影或旧首项输入。

- [一般完整 N4 三短式](R150-appendix-unit211-general-scaled-entire-N4-three-compact-identities.md)，原完整二次型及三个 $Z_i$。
- [正确 I10 的同点原矩、个别 N/P 与完整 NV](R150-appendix-unit211-Phi-zero-corrected-individual-NP-full-NV-I10-and-two-decics.md)，blob ef4bad0b9f5a762c57c9e54695fd4a4247111f32。
- [完整 NV 直接二矩范数](R150-appendix-unit211-Phi-zero-corrected-whole-NV-two-moment-norm-and-quadratic-t-head.md)，blob31b5ba4c5629015696df5aff93802f5ac3b599ce。
- [两个完整个别奇 N/P 直接范数](R150-appendix-unit211-general-original-odd-NP-two-direct-sextic-norms.md)，blob74709b1c4d26365ec1edc1a050fdc992d5d5de83。
- [旧完整低 D 次原来源](R150-appendix-unit211-W-original-odd-NP-full-NV-lower-D-ideal-compression.md)，blob f4e6d79b9956e5a8b39e4a4f88bfbe17eee945f0。

剩余工作仍是把这些同点原条件同其余原均值、原局部化和实际算子桥同时支付。有限值商、同根支撑及消元理想平方夹逼均不等于普通不变子空间问题的完成。
