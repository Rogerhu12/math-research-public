# R613 — 两个真实 carry 的交域、完整二态与原算术返回

日期：2026-11-14。**状态：已证明。**

本篇继续 R611 的两个真实 carry，保留其共同的原 $C$ 输入。
两支的重叠准确等于三个正交轴上的“两深一单位”域。
所需整 theta 度数仅为 $36,396$：完整中心、half-period 相位和
绝对标量给出实际二态，而不是用边际猜一个矩阵。

相邻两个真实重叠域可以完整消去第二态，并经一个已付单位分母的
连续测试逆返回原 $S/T$ 总行。原未归一的 $q\ell$ 测试也全部写出；
它与这个算术测试的真实差，连同整个独占 carry 支一起保留。
不把归一中央零传给未经比较的 native 测试。

## 1. 原 B 来源和同一个正 carry 支

沿用
[R590](R590-original-six-carry-branches-and-sole-b-fibre.md)、
[R594](R594-two-source-six-carry-compensation-and-unit-z-rectangle.md)、
[R611](R611-original-three-sigma-reflection-and-same-depth-negative-five.md)
的全部原规范、射线和固定坏集：
$$
\omega^2+\omega+1=0,\quad\delta=1+2\omega,\quad b=17,\quad
\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2,\quad d_p=p-1,\quad\Omega\in\mathcal O^\times .
\tag{1}
$$
当前 $p\ge71$。保原隐藏输入 $C=v/\delta$，完整来源为
$$
\mu_0=\nu_{B_C}(C)\otimes\nu^\flat(Z,Q,r,c,d),\qquad
B_C(z)=B(z/\delta),\quad B=-y_\wp\sigma^3,
$$
$$
\nu^\flat=\frac1{42}
(\nu_{f_1}\otimes\nu_\Sigma-\nu_{f_3}\otimes\nu_\Theta)
\otimes\nu_\sigma^{\otimes3}.
\tag{2}
$$
$B_C$ 质量一、实际核心 $\beta$ 均已付。
原 $Y/W$ 不含 $C$，故
$\mu_0(\ell)=\mathcal T=J'_S-6\delta J'_T$，原 $\ell$ 仍各带自己的
单位指示。

本篇在 (2) 上保留 R594 同一个 $\zeta=1$ 正支：
$$
D_+=F-C,\quad E_+=F+13C,\qquad
q_{+,n}=\frac{1_{\Gamma_{+,n}}}{b\Omega^6}
 \widehat P_p(D_+/\kappa^n,E_+,G),
$$
$$
\Gamma_{+,n}=\{C,F\ {\rm unit},\ D_+\in p^n\}.
\tag{3}
$$
$\widehat P_p=\sum a_{kjl}(1+\lambda\kappa^j)^{-1}D^kE^jG^l$
仍是原已付完整九乘二十补偿多项式，系数不变。
R590/R594 的每支完整返回给
$$
\boxed{\mu_0(q_{+,n}f)=\beta^n\mu_0(f)\quad
                  \text{对任意完整 }\pi_4\text{ 测试 }f.}
\tag{4}
$$
尤其 $\mu_0(q_{+,n}\ell)=\beta^n\mathcal T$。

对不含 $C$ 的完整测试，R590 已证明在 (2) 中六支平均的积分等于
这一支，无额外 $1/6$。但下文的交域含 $C$：
这里始终使用显示的正支 (3)，不把六支平均逐点改成它。

R611 的 $\tau$ 固定 $C$。令
$q_{-,n}=q_{+,n}\circ\tau$、$\Gamma_{-,n}=\tau\Gamma_{+,n}$，
其参数为 $F_\tau,G_\tau$；整个 $\mu_0$ 满足
$\tau_*\mu_0=-\mu_0$。

## 2. 两支交域的完整正交框架

置
$$
L=(Z+3Q)/2,\qquad M=(Z-Q)/2,\qquad
u=(1-\omega)/3,\qquad \gamma_d=2+3\omega .
\tag{5}
$$
从 $(Z,Q)$ 到 $(L,M)$ 的行列式为 $-1$，保持
$\operatorname{diag}(6,2)$。
R611 的三 sigma 恒等式再次给这个坐标变换下来源的准确负号：
在 $(C,L,M,r,c,d)$ 中，(2) 写成
$$
-\frac1{42}\nu_{B_C}\otimes
 (\nu_{f_1}(L)\otimes\nu_\Sigma(M)
  -\nu_{f_3}(L)\otimes\nu_\Theta(M))
 \otimes\nu_\sigma^{\otimes3}.
\tag{6}
$$
这只是原 $\mu_0$ 的坐标表达，原总行没有换号。
$\tau$ 在这些坐标中恰为 $L\mapsto-L$，逐个固定其余五轴。

定义
$$
J=\omega M+\omega^2r+c+\gamma_d d,\qquad
A=J-C,\qquad H=J+11C .
\tag{7}
$$
准确有
$$
F=J+uL,\quad F_\tau=J-uL,\quad
D_\pm=A\pm uL,
$$
$$
E_\pm=-A/6+7H/6\pm uL .
\tag{8}
$$
原 $G$ 的两支也只在 $L$ 上不同。

为保全部其他输入，取
$$
R_1=M-2\omega^2c,\qquad
R_2=r-\omega c,\qquad
R_3=d+(1+3\omega)c .
\tag{9}
$$
在原物理度量 $\operatorname{diag}(1,6,2,1,1,1)$ 下，
$$
\boxed{
N(J)=11,\quad
\operatorname{Gram}(A,H,L)=\operatorname{diag}(12,132,6),\quad
A,H,L\perp R_1,R_2,R_3 .
}
\tag{10}
$$
完整框架 $(A,H,L,R_1,R_2,R_3)$ 的行列式为 $132$。
三个 $R$ 的内部 Gram 是
$$
\begin{pmatrix}
6&2\omega&2-4\omega\\
2\omega^2&2&-3-\omega\\
6+4\omega&-2+\omega&8
\end{pmatrix}.
\tag{11}
$$
其内部交叉项保留，不把它们改成三个独立标量来源。

完整逆由下列式子给出：
$$
C=(H-A)/12,\qquad J=(11A+H)/12,\qquad
c=(J-\omega R_1-\omega^2R_2-\gamma_dR_3)/11,
$$
$$
M=R_1+2\omega^2c,\quad r=R_2+\omega c,\quad
d=R_3+\bar\gamma_d c,\quad
Z=(L+3M)/2,\quad Q=(L-M)/2 .
\tag{12}
$$
所有分母均为当前单位；旧测试和原输入切集可以全部恢复。

由 (8)、$2u\in\mathcal O^\times$ 及 (12)，两个 carry 的真正交域是
$$
\boxed{
\mathscr X_n:=\Gamma_{+,n}\cap\Gamma_{-,n}
=\{A,L\in p^n,\ H\ {\rm unit}\},\qquad n\ge1.
}
\tag{13}
$$
当 $A,L$ 深时，$D_\pm$ 都深，$C$ 单位等价于 $H$ 单位，
并自动使 $F,F_\tau$ 单位。没有添加额外输入深条件。

## 3. odd11 与实际 even36 / even396 的全部半特征

(6) 中整个 $L$ 方向的两因子 $f_1,f_3$ 核心都为 $\beta$。
$J$ 的完整 first-axis 由一个 degree2 因子和三个 odd sigma
组成，度数 $2+1+1+7=11$。
三个 odd 乘子模二均非零，所以半特征正是标准 odd11。
(9) 与 $J$ 正交，故此结论保完整三个伴随，没有 Gaussian 交叉。

[R454](R454-original-odd33-core-and-exact-residual-slope-transport.md)
的原 ray 是 $\pi_0\equiv2\bmod11$，因而
$g_\pi=\pi_0/\bar\pi_0\equiv1\bmod22$。
同篇已付的奇中心规范遂给整个 $K_{11}$ 为 scalar。
固定 CM 拉回 $F(z)\mapsto F(\delta z)$ 把标准 odd11 放入
标准 odd33：$\delta\equiv1\bmod2$，半特征不变，
且当前 $\delta$ 是单位，真实普通核心与该拉回严格交换。
所以其绝对标量恰为 R454 的原 $\chi_p$。记为
$$
\boxed{K_{11}=\chi I,\qquad \chi=\chi_p,\qquad\chi^2=1.}
\tag{14}
$$
没有将它另选成 $\chi_{65}$ 或按需要猜符号。

对 $A,H$ 必须保 $B_C$ 的真实覆盖。
用 $v=\delta C$ 后，整行是
$$
\delta A=\delta J-v,\qquad
\delta H=\delta J+11v .
$$
其实际 theta 度数分别为
$$
\boxed{N_A=36=33+3,\qquad N_H=396=33+11^2\cdot3.}
\tag{15}
$$
每个轴都是标准 odd33 与 odd3 半特征的乘积，故为标准 even；
两个整行正交。
从 $(J,v)$ 到这两个整行的行列式为 $12\delta$，当前可逆。
其余 $L,R_1,R_2,R_3$ 全保留。
物理条件仍是 $A,H$ 的原深度，因为 $\delta$ 是当前单位。

## 4. 完整 Heisenberg 核及同一来源的绝对标量

当 $N\equiv4\bmod8$，canonical 二挠第三 lift 的中心号为负。
在标准 Schrödinger 基上，若
$D e_j=(-1)^je_j$、$X_{N/2}e_j=e_{j+N/2}$，则
$$
\mathcal A_N=\frac12\sum_{t\in E[2]}\mathsf T_t^N
=\frac12(I+D+X_{N/2}-DX_{N/2}),
$$
$$
\boxed{\mathcal A_Ne_j=e_{(1+N/2)j},\qquad\mathcal A_N^2=I.}
\tag{16}
$$
这个负 cocycle 不能改成 degree 被八整除时的公式。

当前完整中心给
$$
g_\pi\equiv19\pmod{72},\qquad
g_\pi\equiv595\pmod{792}.
\tag{17}
$$
第二式由 $g\equiv3\bmod8$、$g\equiv1\bmod99$ 准确 CRT 得到；
后者只用现有模 $27,11$ 条件。
完整 Weyl 中心商分别为
$(19^2-1)/36=10$、$(595^2-1)/396=894$，均为偶数。
所以 (17) 的真实交织分别等于 (16) 的乘子 $19,199$，
不只比较模 $N$ 的点置换。

在 $N=36$ 上，非零原锚 $\sigma(6z)$ 的普通归一核心为 $-1$。
对 $t=\alpha/2\ne0$，其 canonical 二挠 lift 由周期 $3\alpha$
给符号 $-1$，所以 $\mathcal A_{36}\sigma(6z)=-\sigma(6z)$。
不可约性支付整个绝对式
$$
\boxed{K_{36}=\mathcal A_{36},\qquad K_{36}^2=I.}
\tag{18}
$$

还可在整个实际联合中比较两个二挠作用。
第一 $\delta A$ 平移 $t$ 给 $J$ 参数 $\delta t$、$v$ 参数 $-t$；
第一 $\delta H$ 平移给同一 $J$ 参数 $\delta t$、$v$ 参数 $11t$。
两者在 $v$ 上差 $12t=6\alpha$。
原 odd3 的这个整周期特征为 $+1$，
且 $E(-t,6\alpha)=0$，无剩余中心号。
由完整正交性，Gaussian 因子也逐项相合。
因此保所有 $L,R$ 有
$$
\boxed{\mathcal A_{396}\mu_0=\mathcal A_{36}\mu_0.}
\tag{19}
$$

原 $J,C$ 两个完整核心分别为 $\chi\lambda,\beta$，
所以它们同时深的系数为 $-\chi\lambda^2$。
同一域就是 $A,H$ 同时深；完整归一缩放也相同。
故
$$
K_AK_H\mu_0=-\chi\mu_0.
$$
以 (18) 消去 $K_A$，并用 (19) 和
$\mathcal A_{36}\mu_0\ne0$ 定剩余标量，得到整个空间的绝对式
$$
\boxed{K_{396}=-\chi\mathcal A_{396},\qquad K_{396}^2=I.}
\tag{20}
$$
这不需要猜一个 norm198 的单变量锚。
两个 whole 标量都由同一个原实际来源和原 $J/C$ 全深关系支付。

## 5. 实际二态、完整矩形及交域归一

定义实际第二态
$$
\mu_1=K_A\mu_0=\frac12\sum_{t\in E[2]}\mathsf T^{36}_{A,t}\mu_0 .
\tag{21}
$$
这里 $A,t$ 按第一整行 $\delta A$ 的 canonical 规范理解。
$\mu_1$ 是完整有界来源，也可由原 $A$ 深限制的归一化直接定义。
不假定它仍在旧 $C/J$ 小张量格或拥有新的曲线中央零。

在完整 $(A,H,L,R)$ 格上，两态的归一核准确为
$$
\boxed{K_A=X,\qquad K_H=-\chi X,\qquad K_L=-I,}
\tag{22}
$$
其中 $X$ 交换 $\mu_0,\mu_1$。
最后一式由 $L$ 与 $A,H$ 正交及 (6) 的两条 $\beta$ 核给出。

用 $P_{A,s},P_{H,s},P_{L,s}$ 表示这些实际正交轴的物理缩放。
对任意 $a,h,l\ge0$，完整矩形为
$$
\boxed{
\mu_i|_{\{A\in p^a,H\in p^h,L\in p^l\}}
=(-\chi)^h(-1)^l\lambda^{a+h+l}
(P_{A,\kappa^a}P_{H,\kappa^h}P_{L,\kappa^l})_*
\mu_{i+a+h\ ({\rm mod}\ 2)} .
}
\tag{23}
$$
三个 $R$ 坐标及其完整内部 Gram 逐个保持。

令 $P_n=P_{A,\kappa^n}P_{L,\kappa^n}$，
并对实际交域 (13) 作规范化：
$$
M_n=(-1)^n\lambda^{-2n}(P_n^{-1})_*(\mu_0|_{\mathscr X_n}).
$$
逆映射只在显示的深域使用，输出全部整。
由 $H$ 单位限制
$\mu_i|_{H\ {\rm unit}}=\mu_i+\chi\lambda(P_{H,\kappa})_*\mu_{1-i}$，
得到
$$
\boxed{
M_n=\mu_{n\bmod2}
       +\chi\lambda(P_{H,\kappa})_*\mu_{1+n\bmod2}.
}
\tag{24}
$$
这是完整六变量来源式，没有先忘 $H$ 或三个 $R$。

## 6. 两个真实交域完整返回原算术行

当 $n\ge2$ 为偶数，(24) 准确消去第二态：
$$
\boxed{
M_n-\chi\lambda(P_{H,\kappa})_*M_{n+1}
=(I-\lambda^2(P_{H,\kappa^2})_*)\mu_0 .
}
\tag{25}
$$
原 R410 已付 $1-\lambda^2\in\mathcal O^\times$。

对任意完整连续有界测试 $f$，令
$f_0=f|_{H=0}$，其他五坐标保持。
真正的整连续右逆为
$$
\boxed{
\mathscr R_H f=
\frac{f_0}{1-\lambda^2}
+\sum_{j\ge0}\lambda^{2j}
 (f\circ P_{H,\kappa^{2j}}-f_0).
}
\tag{26}
$$
原物理变量空间是紧的 $\mathbf Z_p^6$，故连续性给一致收敛，所有项和常数分母均整；
望远镜相消直接证明
$(I-\lambda^2S_{H,\kappa^2})\mathscr R_Hf=f$。
$f_0$ 一般依赖另外五轴，不能因为总质量零而删除。

把 (26) 代入 (25)，得到只含原 $\mu_0$ 的真实两个域：
$$
\boxed{
\begin{aligned}
\mu_0(f)={}&
\lambda^{-2n}\int_{\mathscr X_n}
  (\mathscr R_Hf)(P_n^{-1}\mathbf x)\,d\mu_0\\
&+\chi\lambda^{-2n-1}\int_{\mathscr X_{n+1}}
 (\mathscr R_Hf)(P_{H,\kappa}P_{n+1}^{-1}\mathbf x)\,d\mu_0 ,
\qquad n\ge2\ {\rm even}.
\end{aligned}}
\tag{27}
$$
所有混合单位条件通过显示的测试一起转置。

特别取原 $f=\ell$，右侧准确为
$\mathcal T=J'_S-6\delta J'_T$。
这是一条合法的原算术返回；没有给 $\mu_1(\ell)$ 赋零。
其完整归一观察在第一积分中为
$$
Y_R-\frac{\omega\kappa^{2j}H}{44}
+\frac{\delta L}{2\kappa^n}-\frac{\omega A}{4\kappa^n},
\qquad W=Y+2R_3,
\tag{28}
$$
以及 (26) 的 $H=0$ 项。
第二积分相应把 $2j,n$ 换成 $2j+1,n+1$。
(28) 的逆幂只在原交域中使用。
它们与下节的未归一旧 $Y/W$ 是不同的真实测试。

## 7. 同一 native q ell 在交域上的全部表达

为准确写原测试，令
$$
g_J=(20+17\omega)/11,\qquad g_L=-(37+14\omega)/6,
$$
$$
G_R=\frac{-65-182\omega}{22}R_1
+\frac{234-13\omega}{11}R_2
+\frac{143+78\omega}{11}R_3,
$$
$$
Y_R=\frac{-61-6\omega}{22}R_1
+\frac{25+44\omega}{11}R_2
+\frac{13-3\omega}{11}R_3 .
\tag{29}
$$
完整原行是
$$
G_\pm=G_R+g_J(11A+H)/12\pm g_LL,
$$
$$
\boxed{
Y=Y_R-\omega H/44+\delta L/2-\omega A/4,\qquad
W=Y+2R_3.
}
\tag{30}
$$
特别共同缩放 $A,L$ 并不保持原 $Y$；
原两个单位条件始终要按 (30) 移动。

在 (24) 的规范坐标中，原两支多项式和原两个观察准确是
$$
\begin{aligned}
D_\pm/\kappa^n&=A\pm uL,\\
E_{\pm,n}&=7H/6+\kappa^n(-A/6\pm uL),\\
G_{\pm,n}&=G_R+g_JH/12
 +\kappa^n(11g_JA/12\pm g_LL),\\
Y_{\pm,n}&=Y_R-\omega H/44
 +\kappa^n(\pm\delta L/2-\omega A/4),\\
W_{\pm,n}&=Y_{\pm,n}+2R_3 .
\end{aligned}
\tag{31}
$$
置
$$
\mathcal P_{\pm,n}
=(b\Omega^6)^{-1}
 \widehat P_p(A\pm uL,E_{\pm,n},G_{\pm,n}),
$$
$$
\ell_{\pm,n}=d_p\{
1_{Y_{\pm,n}\ {\rm unit}}\log\langle Y_{\pm,n}\rangle
-1_{W_{\pm,n}\ {\rm unit}}\log\langle W_{\pm,n}\rangle\}.
\tag{32}
$$
原 $\widehat P_p$ 的所有 $a_{kjl}$、
$(1+\lambda\kappa^j)^{-1}$ 及负归一幂均保留。

于是，例如同一正支的整个 native 交域积分是
$$
\boxed{
Q_n^\cap:=
\int_{\mathscr X_n}q_{+,n}\ell\,d\mu_0
=(-1)^n\lambda^{2n}
\int\mathcal P_{+,n}\ell_{+,n}\,
d\{\mu_{n\bmod2}+
 \chi\lambda(P_{H,\kappa})_*\mu_{1+n\bmod2}\}.
}
\tag{33}
$$
右侧的完整有符号测度支持在 $H$ 单位域；
将其展开成两项时仍要保两项的真实抵消。
式 (33) 不以 (27) 的规范测试替换原 (32)。

两个支的交域由 $\tau$ 保持，且 $\tau$ 只将 $L$ 反号，
所以 (31)–(32) 的正负支真正互换。
保持 R611 的固定 $c_\tau=(-323-360\omega)/343$ 后，
还有整个 native 测试的准确关系
$$
\boxed{
\int_{\mathscr X_n}
 (q_{-,n}\ell\circ\tau-c_\tau q_{+,n}\ell)\,d\mu_0
=-(1+c_\tau)Q_n^\cap .
}
\tag{34}
$$
它是全来源反射与真实相同交域的结论，不是从来源矩阵推出的
局部中央零。

## 8. 独占支与完整原总行的同源补偿

令
$$
\mathscr E_n=\Gamma_{+,n}\setminus\Gamma_{-,n},\qquad
Q_n^{\rm ex}=\int_{\mathscr E_n}q_{+,n}\ell\,d\mu_0 .
$$
正支完整分成两个不交真域，因此 (4) 给
$$
\boxed{\beta^n\mathcal T=Q_n^\cap+Q_n^{\rm ex}.}
\tag{35}
$$
负支的独占域是 $\tau\mathscr E_n$。
按 (34) 相同的完整换元，两独占域对 R611 测试的贡献是
$-(1+c_\tau)Q_n^{\rm ex}$；
因此 (34) 与 (35) 正好保整个原算术总行。

令 $f_{n,0}$、$f_{n,1}$ 分别是 (27) 在 $f=\ell$ 时的两个
完整被积测试，已包括 $\lambda^{-2n}$、
$\chi\lambda^{-2n-1}$。
因 $\mathscr X_{n+1}\subset\mathscr X_n$，
对每个正偶数 $n$ 可将整个独占支准确返回为
$$
\boxed{
Q_n^{\rm ex}
=\int_{\mathscr X_n}
 \{\beta^n f_{n,0}-q_{+,n}\ell
       +\beta^n1_{\mathscr X_{n+1}}f_{n,1}\}\,d\mu_0 .
}
\tag{36}
$$
(36) 保同一个原来源、同一个正 carry、多项式权与原两个
Mellin 单位条件；完整差测试在 (26)、(28)、(31)–(32) 已显示。
它不是把 native 交域积分与规范中央直接相认。

R594 已知非零的五变量矩形 (5) 满足 $L\equiv Z/2\bmod p^n$，
故 $L$ 单位。在其原正 carry 纤维
$C\in F+p^n$ 上，$D_--D_+=-2uL$ 为单位，
所以该真实非零子管位于 $\mathscr E_n$，与 $\mathscr X_n$ 不交。
其积分仍是原已付的 $v_p=n$；
(36) 没有把这个值移给全部独占支或全部交域。

若原两中央同时为零，(35) 只给
$Q_n^{\rm ex}=-Q_n^\cap$，而 (27) 的两个规范积分之和为零。
(33)、(36) 中的真实测试差仍须比较。
没有删除原已知非零子管之外的独占补域。

最后，(9) 的 $R_3=(W-Y)/2$ 正是
[R539](R539-original-degree8-mixed-st-core-and-amplified-central-domain.md)
的原 norm8 轴。它与 $A,H,L$ 正交，
故该篇已付的完整偶深返回可与 (23) 的矩形同时使用；
其对其他 $R$ 的实际移动仍按原矩阵保留。
这里没有另造一个新的低轴，也未将奇深第二态赋新的算术身份。

## 9. 精确文件及范围

- [check-r613-original-reflected-carry-intersection-and-two-state-return.js](../scripts/check-r613-original-reflected-carry-intersection-and-two-state-return.js)
- [check-r613-original-reflected-carry-intersection-and-two-state-return.json](../scripts/check-r613-original-reflected-carry-intersection-and-two-state-return.json)

BigInt 的 $\mathbf Q(\omega)$ 证书保整个六轴矩阵、逆与 Gram、
全部原观察和两支 $D/E/G$ 的坐标、36/396 全部 Schrödinger 列、
完整中心与相位比较所需整数。
标准半特征、odd11 与原 odd33 的绝对比较、非零联合定标、
全部无限深度矩形、连续逆和原完整补偿由正文证明。
未重算 R594 的右逆，未给第二态或余补域新的中央零。
