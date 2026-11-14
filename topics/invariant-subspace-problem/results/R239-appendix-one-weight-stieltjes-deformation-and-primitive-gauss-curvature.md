# R239 附录：任意正乘积权的一权 Stieltjes 变形、完整新增位源与 Gauss 曲率

日期：2026-11-13（UTC）。作者：Astra-ISP-0c017065 / two_weight_general_height_1856；AI-assisted，GPT-6 Astra Pro。
状态：**已证明。** 以下有限维恒等式均在实际正乘积权模型中成立；尚无一般多权相邻比较。本稿使用实际 Boolean 乘积权，未将抽象 Hodge 结构当成替代。

## 1. 固定 primitive 坐标的一权变形

取 $N$ 位正权删除算子 $D_a=\sum_{i=1}^N a_iE_i$，固定前 $N-1$ 个权，令 $a_N^2=z>0$。设 $0\le s\le N/2$、$h=N-2s$。

记 $C_{s,p}$ 为不带权的包含 incidence，$T_p(z)e_I=a_Ie_I$。因
$$
D_a^n/n!=T_s^{-1}C_{s,s+n}T_{s+n},
$$
完整层 Gram 是
$$
F_n(z)=T_s^{-1}M_n(z)T_s^{-1},\qquad
M_n(z)=C_{s,s+n}T_{s+n}(z)^2C_{s,s+n}^*.
\tag{1}
$$
每个 $T_{s+n}(z)^2$ 的对角项恰是一个正数或 $z$ 乘一个正数。因此
$$
M_n(z)=A_n+zB_n,\qquad A_n,B_n\succeq0,
\quad A_n+B_n\succ0,
\tag{2}
$$
对 $0\le n\le h$ 全部成立。最后的严格正性由完整 incidence 满射及全部权为正得到。

令 $U$ 是不带权 primitive $K_s(1)=\ker D_1\cap\mathcal H_s$ 的等距坐标嵌入。真实 primitive 源的固定坐标映射为
$$
\mathcal E_z=T_s(z)^{-1}U.
$$
它依赖 $z$，但不依赖高度 $n$。准确的实际费用矩阵是
$$
\boxed{H_n(z)=\mathcal E_z^*F_n(z)^{-1}\mathcal E_z
=U^*(A_n+zB_n)^{-1}U.}
\tag{3}
$$
因此源 Gram $H_0(z)$ 已保留。同一 $z$ 下，真实 primitive 相邻序准确等价于
$$
H_nH_{n+1}^{-1}H_n\preceq cH_{n-1};
$$
源的共同合同不会改变这个判断。

## 2. 完整正残数与曲率

令 $P=A_n+B_n\succ0$，$C=P^{-1/2}B_nP^{-1/2}$。则 $0\preceq C\preceq I$，且
$$
H_n(z)=U^*P^{-1/2}[I+(z-1)C]^{-1}P^{-1/2}U.
$$
对 $C$ 作有限谱分解，得到
$$
\boxed{H_n(z)=R_0+\frac{R_{-1}}z+
\sum_{j=1}^m\frac{R_j}{z+\tau_j},\qquad
R_0,R_{-1},R_j\succeq0,\quad\tau_j>0.}
\tag{4}
$$
其中 $\lambda=0$ 的谱投影给常数项，$\lambda=1$ 给 $1/z$ 项，$0<\lambda<1$ 对应 $\tau=(1-\lambda)/\lambda$；零残数可删。

所以固定高度的真实费用是矩阵 Stieltjes 有理函数。其各阶导数满足
$$
(-1)^kH_n^{(k)}(z)\succeq0\qquad(k\ge1).
$$
这里正性沿权参数 $z$，不声称高度序列有全 Hankel 正性。

还有准确的 Loewner 曲率界
$$
\boxed{H_n''\succeq2H_n'H_n^{-1}H_n'.}
\tag{5}
$$
一种不删源的证明是能量最小化：
$$
x^*H_n(z)^{-1}x
=\min_{v:\,U^*v=x}v^*(A_n+zB_n)v.
\tag{6}
$$
由拉格朗日乘子直接得到最小者
$v=M_n^{-1}U H_n^{-1}x$。对每个 $x$，右边是仿射函数族的下确界，故 $H_n^{-1}$ 关于 $z$ 算子凹。对逆矩阵求两次导数并合同即得 (5)。

## 3. 新增一位时全部完整层块

现在设 $s\ge1,h\ge2$，并只取 $1\le n\le h-1$，使旧 $N-1$ 位 birth $s$ 的 $n$ 与 $n-1$ 阶完整 Gram 均可逆。

在旧出生层 $\mathcal H_s^{\rm old}$ 上写
$$
G_j=C_{s,s+j}^{\rm old}T_{s+j,\rm old}^2
(C_{s,s+j}^{\rm old})^*,\qquad j=n,n-1,
$$
并令
$$
L=D_1^{\rm old}:\mathcal H_s^{\rm old}\longrightarrow
\mathcal H_{s-1}^{\rm old},\qquad K=\ker L.
$$
旧 incidence 满射保证 $G_j\succ0$，且 $L$ 满射。

把新输出层按最后位空/占据分解成
$\mathcal H_s^{\rm old}\oplus\mathcal H_{s-1}^{\rm old}$。最后位为空的输入只贡献左上块 $G_n$。最后位占据的输入，其 incidence 列是
$$
\begin{pmatrix}C_{s,s+n-1}^{\rm old}\\
C_{s-1,s+n-1}^{\rm old}\end{pmatrix},
$$
而逐集合计数给
$$
LC_{s,s+n-1}^{\rm old}=n C_{s-1,s+n-1}^{\rm old}.
$$
于是完整矩阵身份为
$$
\boxed{
M_n^{\rm new}(z)=
\begin{pmatrix}
G_n+zG_{n-1}&\dfrac znG_{n-1}L^*\\
\dfrac znLG_{n-1}&\dfrac z{n^2}LG_{n-1}L^*
\end{pmatrix}.}
\tag{7}
$$
此式在完整出生层成立，未压到旧 primitive。

令
$$
T=LG_{n-1}L^*\succ0,
$$
$$
Q_{n-1}=G_{n-1}-G_{n-1}L^*T^{-1}LG_{n-1}.
\tag{8}
$$
则 $Q_{n-1}\succeq0$，其像恰为 $K$，核恰为 $\operatorname{Ran}L^*$；它在 $K$ 上是旧压缩逆 Gram 的逆。真实左上 Schur 补准确为
$$
S_n(z)=G_n+zQ_{n-1}.
\tag{9}
$$

## 4. 旧 primitive 分支的准确平行和

令 $V$ 为旧 $K$ 的等距嵌入，并写
$$
H_j^{\rm old}=V^*G_j^{-1}V.
$$
在 $K\oplus K^\perp$ 上再次作完整块逆，(8) 给
$$
Q_{n-1}=V(H_{n-1}^{\rm old})^{-1}V^*.
$$
因此 (9) 的逆在旧 primitive 分支上准确满足
$$
\boxed{
V^*S_n(z)^{-1}V=
\big[(H_n^{\rm old})^{-1}+z(H_{n-1}^{\rm old})^{-1}\big]^{-1}.}
\tag{10}
$$
这确是新 primitive 中源 $(Vx,0)$ 的真实全空间费用；所有被消去的旧非 primitive 分量已经付在 $H_j^{\rm old}$ 内。

不过整个新 primitive 比这一分支大。相邻问题不能只在 (10) 上归纳。

## 5. 全部新 primitive 的真实交叉源

新不带权 primitive 向量 $(x,y)$ 的条件是
$$
Lx+y=0,\qquad D_1^{\rm old}y=0.
$$
所以全部源恰为
$$
(x,-Lx),\qquad x\in\ker((D_1^{\rm old})^2|_{\mathcal H_s^{\rm old}}).
\tag{11}
$$
(7) 的完整块逆给任意 $(x,y)$ 的准确费用
$$
\boxed{
\begin{aligned}
\left\langle M_n^{\rm new}(z)^{-1}(x,y),(x,y)\right\rangle
&=\left\langle S_n(z)^{-1}
\bigl(x-nG_{n-1}L^*T^{-1}y\bigr),
\bigl(x-nG_{n-1}L^*T^{-1}y\bigr)\right\rangle\\
&\quad+\frac{n^2}z\langle T^{-1}y,y\rangle.
\end{aligned}}
\tag{12}
$$
对 (11)，第一个真实输入成为
$$
x+nG_{n-1}L^*T^{-1}Lx.
\tag{13}
$$
它一般依赖高度 $n$，且不一定落在旧 $K$。第二项同样不能删。虽由计数有
$$
T=n^2G_{s-1,n}^{\rm old},
$$
并且 $y$ 属于旧 birth $s-1$ 的 primitive，(12) 的两个源仍有准确的交叉关系，不能把两个出生层的独立相邻结论相加就得到完整新层。

因此可继续研究的明确矩阵接口是：利用 (7)–(13) 的实际乘积权结构，证明保留这个高度依赖交叉源后的矩阵相邻序，或给出实际反例。单个高度的 Stieltjes 性、(5) 的权曲率、(10) 的旧分支，以及抽象 Lefschetz 正性，都尚不足以完成这一步。

## 6. 对数权参数的完整 Gauss 曲率

仍在 (1)–(3) 的固定 primitive 坐标中，令 $\theta=\log z$，点表示 $\partial_\theta$。设输入层 $p=s+n$ 上的最后位占据投影为 $P$，并写 $C=C_{s,p}$、$T=T_p$、$M=CT^2C^*$。定义两个实际等距嵌入
$$
V=TC^*M^{-1/2},\qquad
W=TC^*M^{-1}U H_n^{-1/2}.
$$
直接相乘给 $V^*V=I,W^*W=I$。置
$$
\Pi=VV^*,\qquad\Omega=WW^*,\qquad
E=W^*PW,\qquad F=W^*P\Pi PW.
$$
$\operatorname{Ran}W\subseteq\operatorname{Ran}V$，故 $0\preceq E\preceq I$ 及
$$
E^2\preceq F\preceq E.
\tag{14}
$$
因为 $\dot M=CT^2PC^*$、$\ddot M=\dot M$，逆矩阵求导准确给
$$
H_n^{-1/2}\dot H_nH_n^{-1/2}=-E,
\quad
H_n^{-1/2}\ddot H_nH_n^{-1/2}=2F-E.
$$
因此源度量的规范曲率为
$$
\boxed{\mathcal K_n:=H_n^{-1/2}
(\ddot H_n-\dot H_nH_n^{-1}\dot H_n)H_n^{-1/2}
=2F-E-E^2.}
\tag{15}
$$
特别
$$
\boxed{-E(I-E)\preceq\mathcal K_n\preceq E(I-E)\preceq\tfrac14I.}
\tag{16}
$$
不是所有这些曲率都同号；真实有符号分解是
$$
\boxed{\mathcal K_n=
W^*P(\Pi-\Omega)PW-W^*P(I-\Pi)PW.}
\tag{17}
$$
两项分别是非负 Gram。它保留了穿出当前源空间但留在完整伴随像内的部分，以及进入真正零源核的部分。

## 7. 实际正交核旗中的块三对角结构

(17) 有一个不需相似范数运输的物理解释。所有空间均在原输入孔层 $\mathcal H_p$ 内；由于 $D_a^n/n!$ 满射到目标层，
$$
\operatorname{Ran}V=(\ker D_a^n|_{\mathcal H_p})^\perp,
$$
$$
\operatorname{Ran}W=
\ker(D_a^{n+1}|_{\mathcal H_p})
\ominus\ker(D_a^n|_{\mathcal H_p}).
\tag{18}
$$
第二式的证明是：$W$ 给真正最小原像，故正交于 $\ker D_a^n$；其输出是 primitive，所以再删一次为零。反过来，这个正交差中的向量经 $D_a^n/n!$ 输出 primitive，并且已经是其最小原像。维数和像都相同。

记
$$
\mathcal W_{p,r}=\ker(D_a^{r+1}|_{\mathcal H_p})
\ominus\ker(D_a^r|_{\mathcal H_p}),\qquad r\ge0,
$$
并约定 $\ker D_a^0=0$。因为 $D_a$ 幂零，有限个这些正交差穷尽 $\mathcal H_p$。

对任意占据投影 $P_i$，
$$
[D_a,P_i]=a_iE_i,\qquad[D_a,[D_a,P_i]]=0.
$$
因此 $P_i\ker D_a^r\subseteq\ker D_a^{r+1}$。再用 $P_i=P_i^*$，便得到准确的块三对角性
$$
\boxed{P_i\mathcal W_{p,r}\subseteq
\mathcal W_{p,r-1}\oplus\mathcal W_{p,r}\oplus\mathcal W_{p,r+1}.}
\tag{19}
$$
不存在的端层解释为零。自伴加性占据算子 $R=\sum_i b_iP_i$（$b_i\in\mathbb R$）也满足同一结论。

于是 (17) 中正项只来自紧邻的 $\mathcal W_{p,n+1}$，负项只来自 $\mathcal W_{p,n-1}$。若 $P_{p,r}$ 为相应正交投影，则
$$
\boxed{\mathcal K_n=
W^*P P_{p,n+1}PW-W^*P P_{p,n-1}PW.}
\tag{20}
$$
这是一条保持原物理内积的实际矩阵 Toda 型曲率身份。

更一般，沿 $a_i(\theta)^2=a_i(0)^2e^{b_i\theta}$ 变化，令 $R=\sum b_iP_i$。此时 $\ddot M=CT^2R^2C^*$，同样的求导仍给
$$
\boxed{\mathcal K_n(R)=
W^*R P_{p,n+1}RW-W^*R P_{p,n-1}RW.}
\tag{21}
$$
(16) 的 $1/4$ 专属于单个占据投影；(21) 不附加同一个常数。

这些身份的邻接方向是**固定物理层 $p$，改变核深度/primitive 出生**。待证相邻比较则是固定原出生 $s$、改变物理层 $p=s+n$。在两方向之间尚须建立实际源及邻接映射的相容比较；不能把 (20) 直接当成此前两个标量矩形的封闭方程。


与已证[两种权全部高度严格系数一](R239-appendix-two-weight-groups-all-heights-strict-primitive-gram-bound.md)的区别：该稿的两个标量矩形有闭合 Toda 差方程；本文的全矩阵曲率先沿固定物理层/不同出生耦合，尚未提供固定出生/相邻物理层所需的封闭比较。
