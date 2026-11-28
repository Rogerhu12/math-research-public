# R1169 — 原第二中央分量的完整 S/U 源、实际读数与同源未平滑

> **字典说明，[R1177](R1177-original-syntomic-to-Frobenius-sign-dictionary.md)。** 引用 R1168 的单个 PD 常数时，其物理 Frobenius 值为该 syntomic 常数的负值。本文两输入的完整双积与第二中央相关读式均保持；原几何系数、S/U filling 和同源运输不改。

**状态：已证明。** 日期：2026-11-28 Asia/Taipei。
会话：Astra-serre-24b8836b-20261126。

本篇接续 R1158–1168，将原实际构造推进到第二中央分量
$$
Z_2=\operatorname{Sym}^8H(4),\qquad
\Pi_2(v^4,w^8)=\langle v,w\rangle^2v^2w^6.
$$
$\Pi_2$ 是 R1163 (1163.20) 已校准的原 normalized contraction。
本篇给它自己的完整 raw relation、同根 correlation torsor、
在原两个 CM 模型上的全部指定 Frobenius 读数，
以及准确的同源运输和上链未平滑。
仍未把后者的算术局部值当成已求出的原 $F_0$。

## 1. 实际 degree-eight 填充式

保持原两个标记的作用
$$
S(X,Y)=(-Y,X),\qquad U(X,Y)=(-Y,X-Y).
$$
令
$$
\begin{aligned}
f(X,Y)&=X^2Y^6,\\
s(X,Y)&=XY(X-Y),\\
R(X,Y)&=(X+Y)(2X-Y)(X-2Y),\\
q(X,Y)&=X^2-XY+Y^2,\qquad Q_8=R\,s\,q .
\end{aligned}
$$
直接代入给 $Us=s$、$UR=R$、$Uq=q$，所以 $UQ_8=Q_8$。
另一方面，
$$
\begin{aligned}
Q_8-SQ_8
=XY(X^2-Y^2)\bigl(&
 (2X-Y)(X-2Y)(X^2-XY+Y^2)\\
 &-(2X+Y)(X+2Y)(X^2+XY+Y^2)\bigr)\\
= -14X^2Y^2(X^4-Y^4)
=14(f-Sf).
\end{aligned}
$$
因此
$$
\boxed{
A_8=\frac f2-\frac{Q_8}{28},\qquad
B_8=\frac{Q_8}{42},\qquad
f=(1+S)A_8+(1+U+U^2)B_8 .
}
\tag{1169.1}
$$
最后一式的右边恰为
$(f+Sf)/2+(Q_8-SQ_8)/28=f$。
全部分母只含 $2,3,7$，在 $p>37$ 时可逆。

对真正的原 $p$-点 $P,Q$，把本式乘以
$\langle P,Q\rangle^2$。
$S,U$ 在两个标记上的 determinant 均为一，
故原 Weil 因子严格不变。
此时左边准确是原 $\Pi_2(P^4,Q^8)$，不是一个另定标度的
degree-eight polynomial。
右边两权分别为
$$
\mathcal A_2(P,Q)=\langle P,Q\rangle^2A_8(P,Q),\qquad
\mathcal B_2(P,Q)=\langle P,Q\rangle^2B_8(P,Q).
\tag{1169.2}
$$
它们的总原 tensor degree 仍为十二；
两个 Weil 因子提供所需的额外 Tate $(2)$。

$Q_8$ 在 $P=0$、$Q=0$、$P=Q$ 时为零，
故三项 relation 不需读取 $\theta(0)$。
此外全部依赖点对的 Weil pairing 为零，
所以它们在本分量中确切没有贡献。
这个消失来自实际 $\Pi_2$ 系数，不删原最高分量的依赖点对。

## 2. 同一个实际 quotient 上的 raw correlation

对合法原辅助数 $n$，交换商仍是 R1158 (1158.1)、(1158.4)
的全部 original 与 primed 四次、八次 theta moments。
只把其中央 bilinear law 改为
$$
b_{n,2}(v,v')
 =\Pi_2(x,y')-\operatorname{Tr}_C\Pi_2(x_C,y'_C).
\tag{1169.3}
$$
两个 primed 槽始终使用同一个实际 $C$。

取 R1158 §§2–5 已给定的共同 even 单位 quotient、
原 $S$ primitive 与原三角形 $U$ primitive。
沿同一个 quotient 取纤维积，
再以 (1169.2) 对各中央槽作实际 finite-étale trace。
逐槽重指标时，$S^{-1}=-S$ 的总次数为偶数，
而 $U$ 的标记域及两个 Weil 因子都保持；
(1169.1) 遂在两个独立输入上给
$$
\sum_{P,Q}\mathcal A_2(P,Q)B^S_{P,Q}
 +\sum_{P\ne Q}\mathcal B_2(P,Q)B^U_{P,Q}
 =b_{n,2}(\lambda(-),\lambda(-)).
\tag{1169.4}
$$
这里 $\lambda$ 是原全部有序 moment map，
不是只对外积或 cohomology 的 map。
所以共同 raw 群到
$G_{n,2}^{\rm corr}=V_n\oplus Z_2$
的线性中央 pushout 是真正的群同态。
原 all-vector 的 $P,-P$ 两项、原根相位、
closed-point transfer 和 same-coset 乘法全部沿原 morphisms 保留。

这给实际 $G_{n,2}^{\rm corr}$-torsor。
其 noncusp 延伸和全算术下降沿原 raw torsors 完成，
不对含 $p$ 的标记 cover 作群阶平均。
在全部 $p^r$ 层，(1169.1) 是同一整多项式身份；
用 R1147 §20 的实际连续 degree-twelve moment jet、
原 normalized pair projectors 和已固定兼容根执行同一构造。
因此各层约化相容；没有任选有限标记的 $T_pE$ 提升。
原 primitive/all-vector 固定单位尺度依 R1147 同时作用于两边。

## 3. 原 $n=2$ 对象的 ordinary 代表与实际低 normal

以下取原 cubic 或 Gaussian CM 模型，$p>37$，
以及 R1166–1168 的同一 $n=2$ source。
记所有 raw moments 的 second 槽为 $y$。
原 even $S$ primitive 的 scalar $\beta^S_{P,Q}$
在交换 $P,Q$ 下严格对称；
而 $Q_8$ 反对称，$\langle P,Q\rangle^2$ 对称。
所以完整 $\mathcal A_2\beta^S$ 求和中，
$Q_8$ 那一项严格相消。
在原 coefficient cone 中因此有
$$
\boxed{
h_{2,\rm corr}
  =(0,\tfrac12 b_{2,2}(y,y)+J_2),\qquad
J_2=\frac1{42}\sum_{P\ne Q}
       \langle x_P,x_Q\rangle^2Q_8(x_P,x_Q)\,
                                     \beta^U_{P,Q}.
}
\tag{1169.5}
$$
式中 $Q_8$ 只占剩余八个 tensor factors；
前两个 Weil factors 用 R1163 的 actual paired projector，
没有把原 coefficient object 换成一个裸标量配对。

R1166 §§20–21 已付每个原 $\beta^U$ 的同源
ordinary representative、零 first slot 和全部 whole-root
morphisms。把它乘以本篇的 actual $H^0$ coefficient 时，
同一 external-product homotopy 含 primitive first slot，
故这次乘法的修正为零。
随后仍作原 tame trace。

可以明确核准 $J_2$ 的常数项。
R1167 的原 $x_P$ 每个 $\omega$ 槽含
$z^p(1+\gamma_p)$，每个 $\eta$ 槽含 $zg$。
一次实际 pairing 恰消去一个 $\omega$ 和一个 $\eta$，
其 coefficient 有 $z^{p+1}g(1+\gamma_p)$。
因此原目标基 $\omega^{8-K}\eta^K$ 的每一项
在配对前共有 $K+2$ 个 $\eta$ 槽，
其因子为
$$
z^{j}(1+\gamma_p)^{10-K}g^{K+2},
\qquad j=p(10-K)+K+2,\qquad0<j<e=p^2-1 .
$$
ordinary $\beta^U$ 没有负 $z$ 次数，
所以零 $e$-block 从 $u^1$ 开始。准确得到
$$
\boxed{
(J_2)_{K,n}=0\quad(n<K+3),\qquad
\text{特别 }(J_2)_{K,0}=0.
}
\tag{1169.6}
$$
正 $\gamma_p$ carry 先保留，只能提高 normal 次数。
目标 coefficient 是 $(d,t)=(8,4)$：
在十二因子模型中的 weight 十四，经两个
$H^2(E)$ factors 后，正是 R1168 的
$\operatorname{Fil}^{12}(S_F\otimes M_8)$；
不是把它误写成 $\operatorname{Fil}^{14}(M_8)$。

原各 abelian 槽仍满足
$$
y_{d,k,n}=0\ (n<k+1),\qquad a=N_uy,\qquad\phi_d a=0 .
\tag{1169.7}
$$
其来源、原 $N_z=eN_u$ 和 log-trace 尺度均没有改变。

## 4. 全部第二中央相关 Frobenius 的实际双线性值

令 $U_k^{(d)}=\omega^k\eta^{d-k}$，并沿 R1168 的
raw 常数定义
$$
B_{k,l}
 =\mathcal A_{4,k}\mathcal A_{8,l}
  -\sum_i\mathcal A'_{i,4,k}\mathcal A'_{i,8,l}.
$$
这些系数已经由 R1168 (1168.49)–(1168.51) 具体给出。
本分量的完整结果是
$$
\boxed{
Z_{2,\rm corr}^{\rm BCH}
 =\sum_{k=0}^4\sum_{l=0}^8
   \frac{k-l}{2(k+l+2)}B_{k,l}\,
                       \Pi_2(U_k^{(4)},U_l^{(8)}).
}
\tag{1169.8}
$$
原 ordered 坐标为
$$
\boxed{
Z_{2,\rm corr}^{\rm ord}
 =\sum_{k=0}^4\sum_{l=0}^8
   \frac{k+1}{k+l+2}B_{k,l}\,
                       \Pi_2(U_k^{(4)},U_l^{(8)}).
}
\tag{1169.9}
$$

### 4.1. 完整 gauge 及唯一会进入的 normal 系数

沿原 R1168 收缩取 $R=T(y)$、$A=\mathcal R_V(y)$，
并写 $\phi R=A+U$。由 (1169.7)，
$U$ 的全部正 normal 次数至少为 $p$。
原 ordered gauge 的完整展开与 R1166 (1166.77) 相同，
将其中 $b_n,J_U$ 换为 $b_{2,2},J_2$ 即可。

本目标的 $\mathcal R_{8,4}$ 仅读 normal $0$ 与
$q_K=K+4\le12<p$，故含 $U$ 的项读数为零。
由实际 filtered paired product，
$$
b_{2,2}(R,R)\in\operatorname{Fil}^{12}(S_F\otimes M_8),
\qquad
\phi_{12}b_{2,2}(R,R)=b_{2,2}(\phi R,\phi R).
$$
这里两个 paired $H^2$ 的 Frobenius 因子已包含在原 map 中。
$\mathcal R$ 消真正的 $d_0$ boundary，遂给
$$
\mathcal R_{8,4}b_{2,2}(R,R)=b_{2,2}(A,A).
$$
因此原 whole Frobenius/Hodge frame 中
$$
H_{2,\rm corr}^{\rm const}
 =\tfrac12 b_{2,2}(A,A)+\mathcal R_{8,4}J_2,\qquad
Z_{2,\rm corr}^{\rm BCH}=-\mathcal R_{8,4}J_2.
\tag{1169.10}
$$
这里没有假定 $\mathcal R$ 是乘法映射。

由 (1169.5)、(1169.7) 的实际微分，
$$
N_uJ_2
 =\tfrac12\{b_{2,2}(y,N_uy)-b_{2,2}(N_uy,y)\}.
\tag{1169.11}
$$
输入 $\omega^{4-k}\eta^k$ 与
$\omega^{8-l}\eta^l$ 配对后，目标的 $\eta$ 下标是
$K=k+l-2$。若该项非零，则 $0\le K\le8$，且
$$
q_K=K+4=k+l+2 .
$$
故右边 normal $q_K$ 只由两个原 moments 的
normal $k+1,l+1$ 给出，系数仍是
$$
\frac{l-k}{2(k+l+2)}
       \binom{k+l+2}{k+1}.
$$
其余低层由 (1169.11) 强制为零，
而 $N_u$ 的高层核不进入指定读取；
normal 常数另由 (1169.6) 支付为零。

### 4.2. 实际 pairing 与 Frobenius 符号

目标 reader 的系数是
$$
\frac{b_E^{\,2K-8}}{(K+4)!}
             \sigma((J_2)_{K,K+4})
\quad\text{于 }\omega^K\eta^{8-K},
$$
因为这里 $t=4$ 为偶数。
$2K-8=2(k+l)-12$，恰与两份原 abelian reader 的
$b_E$ 指数相同，阶乘也按原二项系数完全相消。

交换 $\omega,\eta$ 使一次 alternating contraction 变号，
但这里有两次，故输入基的 $\Pi_2$ coefficient
与 Frobenius 后输出基的 coefficient 相同。
原两份 abelian reader 的负号相乘为正。
所以 (1169.11) 在 constant frame 中的读数
准确是 (1169.8) 的负值。
再由 (1169.10) 得 (1169.8)；
加 $b_{2,2}(A,A)/2$ 得 (1169.9)。

若要逐 monomial 展开，原 normalized polarization 给
$$
\begin{aligned}
\Pi_2(U_k^{(4)},U_l^{(8)})
  =\frac1{672}\bigl(&
   k(k-1)(8-l)(7-l)\\
 &-2k(4-k)l(8-l)
 +(4-k)(3-k)l(l-1)\bigr)
 \omega^{k+l-2}\eta^{10-k-l}.
\end{aligned}
\tag{1169.12}
$$
本式只在 $2\le k+l\le10$ 使用；其它项为零。
它是将
$\langle v,w\rangle^2v^2w^6$ 对两份 pure powers
分别 polarization 的结果：
归一因子为 $2!6!/(4!8!)=1/672$，
三个 Leibniz 项的系数为 $1,-2,1$。
原 $\omega,\eta$ 的 cup–trace 由
$\operatorname{Res}_O((\int\omega)\eta)=1$ 标定；
平方 pairing 的值为一，原 coevaluation 无新尺度。
所以 (1169.12) 没有另乘挑选 pair 的组合数。
所有显示分母均为 $p>37$ 的单位。

## 5. 原同源 map 的额外 Weil 因子

本节保原 R1159 §5 的 actual product、Norm 点和
$H=\ker L$，只换本篇的第二中央群。
在商曲线 $E/C$ 上，交换系数仍沿
$\operatorname{Sym}^4(\psi_C^{-1})$、
$\operatorname{Sym}^8(\psi_C^{-1})$ 运输。

因为 $\deg\psi_C=n$，原 Weil adjoint identity 给
$$
\langle\psi_C^{-1}P,\psi_C^{-1}Q\rangle_E
 =n^{-1}\langle P,Q\rangle_{E/C}.
$$
所以使整个群态射相容的中央 map 准确是
$$
\boxed{
\kappa_{C,2}
 =n^{-2}\operatorname{Sym}^8(\psi_C^{-1}):
      Z_2(E/C)\longrightarrow Z_2(E).
}
\tag{1169.13}
$$
原显式 Tate 因子沿同一规范；$n^{-2}$ 来自两次实际 Weil
收缩，不能遗漏，也不能再乘第二份同样因子。

在这个已经正确运输的 product 群上，
R1159 的 ordered 展开逐字适用于 $\Pi_2$。
实际 Norm reduction 给
$\sum_Cv_{C,d}=(n+n^{-d})v_{0,d}$，从而在两个独立输入上，
首槽 scalar 仍是 $n^4+n^{-11}$，
其它中央槽的群 map 仍为 $-n^2\sum_C$。
使用完整 $\mathcal M$ 上原
$H^0(Z_{2,r})=H^1(Z_{2,r})=0$ 最后识别本篇的
实际 correlation torsor，再以唯一 Hodge 点读取，得到
$$
\boxed{
Z_{2,\rm corr}(E)
 =(n^4+n^{-11})Z_2(E)
  -\sum_{C\subset E[n]}
     \operatorname{Sym}^8(\psi_C^{-1})\,Z_2(E/C).
}
\tag{1169.14}
$$
这里 $-n^2$ 与 (1169.13) 的 $n^{-2}$ 准确抵消。
同一式子在 BCH 坐标成立，因为实际群 map 保原 bilinear law。
商曲线的数值及全部 coefficient shear 都在运输后才求和；
$n=2$ 时使用 R1159 (1159.30)–(1159.31) 的整矩阵
及其原 exact 比较，不将 $\eta_i$ 当成原 $\eta$。

## 6. 上链未平滑及没有新增例外素数的 scalar

在本目标上定义实际 correspondence
$$
T_n^{(8)}
 =\operatorname{Cor}_C\operatorname{Sym}^8(\psi_C^{-1})q_C^*,
\qquad
\mathcal V_{n,2}
 =(n^4+n^{-11})\,\mathrm{id}-T_n^{(8)}.
$$
R1159 的两条 crossed projection-formula、root phases
和 $K_{a,b}$ 都在同一个 tensor coefficient 上；
把它们按实际 $\Pi_2$ 投影，准确给
$$
\begin{aligned}
J_{n,2}={}&n^{-7}\Pi_2\{\eta_4\cup b+R_{a^C,b}\}\\
 &+n^{-3}\Pi_2\{-a\cup\eta_8+L_{a,b^C}\}
       -n^{-12}\Pi_2K_{a,b}.
\end{aligned}
$$
由 (1169.13)，两个 cover 槽的 cup 被 transport 为
$n^{-2}T_n^{(8)}\Omega_2$，故
$$
\Omega_{2,\rm corr}=\mathcal V_{n,2}\Omega_2+dJ_{n,2},
\qquad
h_{\mathcal V_{n,2}}=h_{2,\rm corr}+J_{n,2},
\qquad dh_{\mathcal V_{n,2}}=-\mathcal V_{n,2}\Omega_2.
\tag{1169.15}
$$
其中 $\Omega_2=\Pi_2(a_4\cup a_8)$，没有改 ordered 符号。

原 geometric residue 线是 Tate $(3)$；
其实际 degree-eight moment 给
$T_n^{(8)}=n+n^{-8}$。
原绝对 Hochschild–Serre 识别于是使
$\mathcal V_{n,2}$ 在 $H^2$ 上作用为
$$
\boxed{
v_{n,2}
 =n^4+n^{-11}-n-n^{-8}
 =n^{-11}(n^3-1)(n^{12}-1).
}
\tag{1169.16}
$$
取原已付 $n=2$，得到
$$
v_{2,2}=\frac{7\cdot4095}{2^{11}}
       =\frac{3^2\cdot5\cdot7^2\cdot13}{2^{11}}.
$$
因此对全部 $p>37$ 都为单位，本分量无 $43,127$ 例外。

对给定
$\zeta_{n,2}=(\mathcal V_{n,2}-v_{n,2})\Omega_2$，
直接消费 R1160 的实际构造
$$
B_{n,2}=\mathcal B_{8,4}(\zeta_{n,2}),\qquad
dB_{n,2}=\zeta_{n,2}.
$$
原未平滑 primitive 因而准确为
$$
\boxed{
h_2=\frac{h_{2,\rm corr}+J_{n,2}+B_{n,2}}{v_{n,2}},
\qquad dh_2=-\Omega_2 .
}
\tag{1169.17}
$$
全部 finite differences、复共轭修正和原 conjugating paths
使用 R1160 的原指定公式；各 $p^r$ 层相容。
全 $\mathcal M$ 的唯一性识别到原四十三格的第二中央槽，
不新选一个同名局部 lift。

## 7. 当前实际关闭的范围

本篇已完成原 $\Pi_2$ 自己的 raw S/U filling、
整个相关对象、原 CM 点上全部 weighted Frobenius 读数，
以及原同源 $n^{-2}$ 因子和显式算术未平滑接口。
(1169.8)–(1169.12) 可直接使用 R1168
已经读取的 original/primed 系数，没有另留一份
未知的标量 $U$-和。

但 (1169.14) 是跨全部实际商曲线的功能方程；
(1169.16) 只给 cohomology scalar。
不能据此把 (1169.8) 除以 $v_{2,2}$ 当成原单点 $F_0$，
(1169.17) 的 $J_{n,2},B_{n,2}$ 局部值仍要实际读取。
最低 $\Pi_4$ 还带原 $\lambda_\infty a_4\gamma_5$，
本篇没有删除或完成该项。
原全局中央减法、全部深盘及 Serre 主标准继续。

## 来源与执行

- R1157–1158：原四线/SV、共同 even quotient、全部同根
  raw $S/U$ 对象与无群阶反除的算术下降。
- R1147、R1160：原三中央群、完整整塔、实际 residue 线、
  全 $\mathcal M$ 唯一性及显式算术下降。
- R1163：原 normalized $\Pi_2$、两个 paired factors、
  实际 Tate coevaluation 与 integral comparison。
- R1166–1168：同源 ordinary raw 代表、原 CM period、
  tame trace、全部 normal 支持、实际 nonlinear SDR 和矩系数。
- R1159 §5：给定 Norm 点的 product-kernel 群图与真实
  Hodge/Frobenius 比较；本篇独立保留额外 Weil 因子。

degree-eight 多项式恒等式、全部 normal/factorial 读数、
paired Frobenius、实际同源尺度和 $v_{n,2}$ 均在正文纸证。
global_route 同时核准原 Weil factor 方向和 scalar。
无数学程序执行。
