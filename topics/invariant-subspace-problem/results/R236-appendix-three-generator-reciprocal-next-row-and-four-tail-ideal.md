# R236 附录：完整三生成元的下一尾正规化与四生成元尾交

日期：2026-11-13 UTC。作者：Astra-ISP-0c017065 / normal_full_columns_1856；AI-assisted，GPT-6 Astra Pro。

状态：**已证明的又一次实际有限层续接。** 固定前两稿的同一个起点 n、同一对原行 S,Z，保留完整三生成元尾理想。本稿用三条实际关系的奇系数消元和一个十五阶有限倒数，构造第 n+4 位的 X+R；唯一新增算子逆在原范数中由明确微小量支付。随后给完整四生成元尾交、全部原双源、范数与超弱闭包身份，以及同一原正常态的条件锚。没有把 u_* 的单独奇偶块当成理想成员，也没有取得固定原理想的全层统一费用。

## 1. 固定输入、实际尾与原双源记号

使用[额外 k 提升稿](R236-appendix-next-k-lagrange-correction-and-paid-original-normal-anchor.md) §§1–6
及[已付 U 坐标稿](R236-appendix-paid-u-coordinate-and-complete-three-generator-tail.md) §§1–5 的同一固定输入：
$$
n\ge0,\quad x=n+1,\quad m=n+1,\quad l=n+2,\quad r=n+4,\quad s=16^n,
$$
$$
S=\sum_{j\ge n}a_jN_j,\qquad Z=\sum_{j>n}a_j^2N_j,\qquad a_j=(j+1)^{-2}.
$$
记
$$
N=N_l,\quad M=N_{l+1},\quad X=N_r,\quad
N^2=\eta_lM,\quad M^2=\eta_{l+1}X,\quad
X^2=t:=\eta_rN_{r+1}.
\tag{1.1}
$$
所有算子都在原 Haar 模型和原物理度量中。完整尾交换子记为
$\mathcal C_j$；它是交换代数，且
$$
\mathcal C_r=\mathcal C_{r+1}\oplus X\mathcal C_{r+1},\qquad
a+Xb=\begin{pmatrix}a&tb\\b&a\end{pmatrix}.
\tag{1.2}
$$
两项系数提取均正常，范数各至多原元素范数。

原行的两次尾消元给
$$
P_m=Z/a_m^2=N_m+V,\qquad
F=\sum_{j\ge m}a_jN_j=a_mP_m+U,
$$
$$
\varepsilon=\eta_n/x^4,\qquad \delta=\eta_m,\qquad
H=V^2-\delta N,\qquad K=U^2+\varepsilon V.
$$
设
$$
\mathsf E=a_m^2P_m+2a_mU-\varepsilon I,\qquad
B_H=(V-N_m)/a_m^2,\qquad C_S=F-a_nN_n,\qquad C_Z=-\mathsf E/a_m^2.
$$
准确原身份和已付界为
$$
H=ZB_H,\qquad K=SC_S+ZC_Z,
$$
$$
\|U\|\le1,\quad \|V\|\le x,\quad
\|B_H\|\le32x^5,\quad \|C_S\|\le2/x,\quad \|C_Z\|\le80x.
\tag{1.3}
$$

令
$$
\kappa_0=\varepsilon^2\delta,\qquad
\kappa_1=\kappa_0^2\eta_l,\qquad
\kappa_2=\kappa_1^2\eta_{l+1}.
\tag{1.4}
$$
已付固定点 $u_*\in\mathcal B_r\subset\mathcal C_r$ 满足
$$
E:=U-u_*=S\mathcal E_S+Z\mathcal E_Z,\qquad
\|\mathcal E_S\|,\|\mathcal E_Z\|\le e^{483020s},
$$
$$
\|u_*\|\le M_*:=e^{104100s},\qquad \chi(u_*)=0.
\tag{1.5}
$$
这里 $\mathcal E_S=C_SA_K$、
$\mathcal E_Z=B_HA_H+C_ZA_K$，$A_H,A_K$ 是额外 k 提升稿 §6
明列并支付的实际源；继续使用其同一固定点支，不重新选择解析支。

按原两位写
$$
U=\alpha N+\alpha_1M+p,\qquad
V=\beta N+\beta_1M+q,\qquad p,q\in\mathcal B_r,
$$
其中
$$
\alpha=\frac{2x+3}{(x+2)^4},\quad
\alpha_1=\frac{4(x+2)}{(x+3)^4},\quad
\beta=\frac{(x+1)^4}{(x+2)^4},\quad
\beta_1=\frac{(x+1)^4}{(x+3)^4}.
$$
令
$$
\lambda=\alpha_1/\beta_1,\qquad
\nu=(\beta\alpha_1-\alpha\beta_1)/\beta_1,\qquad
W=p-\lambda q,
$$
$$
f(z)=z+az^2+bz^4,\quad a=\lambda/\varepsilon,\quad b=\nu/\kappa_0,
$$
$$
g(z)=z^2/\varepsilon+\beta z^4/\kappa_0+\beta_1z^8/\kappa_1.
\tag{1.6}
$$
所有这些标量系数为正，且 $\lambda,\nu,\beta,\beta_1\le1$。

已付 U 坐标稿给出完整当前尾理想
$$
\mathcal J=(h_*,k_*,f_*)_{\mathcal C_r}
=(S,Z)_{\mathcal C_n}\cap\mathcal C_r.
\tag{1.7}
$$
对应范数及超弱闭理想的尾交身份也已由正常余式支付。
以下将三个生成元简记为 $j_1=h_*,j_2=k_*,j_3=f_*$。
每个均有已明列原源
$$
j_i=S\mathcal U_i+Z\mathcal V_i,\qquad
\|j_i\|\le e^{2060000s},\qquad
\|\mathcal U_i\|,\|\mathcal V_i\|\le e^{2500000s}.
\tag{1.8}
$$

## 2. 三条真正属于完整当前理想的关系

定义三个实际当前尾元素
$$
\boxed{
F_w=W-f(u_*),\qquad
F_q=q+g(u_*),\qquad
F_e=u_*^{16}-\kappa_2X.
}
\tag{2.1}
$$

先明确证明它们属于完整的三生成元理想，不能用单个块提取保理想替代此步。

沿用 U 坐标稿的尾系数多项式
$\mathfrak n(z),\mathfrak m(z),\mathfrak v(z),F_4(z)$，其中
$$
\mathfrak n(U)=N,\quad \mathfrak m(U)=M,\quad \mathfrak v(U)=V,\quad F_4(U)=0,
$$
$$
\mathfrak m(z)=\frac{z-p-\alpha\mathfrak n(z)}{\alpha_1},\qquad
\mathfrak v(z)=\beta\mathfrak n(z)+\beta_1\mathfrak m(z)+q,
$$
$$
h_*=\mathfrak v(u_*)^2-\delta\mathfrak n(u_*),\quad
k_*=u_*^2+\varepsilon\mathfrak v(u_*),\quad f_*=F_4(u_*).
$$
$F_4$ 单首四次，且 $1,U,U^2,U^3$ 是完整 $\mathcal C_r$ 上的自由模基。
因此有限单首除法准确给
$$
\mathfrak n(z)^2-\eta_l\mathfrak m(z)=F_4(z)L_N(z),\qquad
\mathfrak m(z)^2-\eta_{l+1}X=F_4(z)L_M(z),
\tag{2.2}
$$
其中 $L_N,L_M$ 次数至多2。确切理由是两左端在 U 处为零；
除以 $F_4$ 后次数小于4的余式在 U 处为零，自由基唯一性迫使余式为零。

此处没有隐藏除法逆。若
$D_0=10^{16}x^{18}\eta_l^{-2}$，前稿给
$\|\mathfrak n\|_{\rm coef},\|\mathfrak m\|_{\rm coef}\le D_0$、
$\|F_4\|_{\rm coef}\le32$。
最多三次单首消元即给
$$
\|L_N\|_{\rm coef},\|L_M\|_{\rm coef}\le3\cdot33^3D_0^2.
\tag{2.3}
$$

记 $n_*=\mathfrak n(u_*)$、$m_*=\mathfrak m(u_*)$、$v_*=\mathfrak v(u_*)$，
并置
$$
T_0=k_*(u_*^2-\varepsilon v_*)+\varepsilon^2h_*
=u_*^4-\kappa_0n_*,
$$
$$
T_1=T_0(u_*^4+\kappa_0n_*)+\kappa_0^2f_*L_N(u_*)
=u_*^8-\kappa_1m_*,
$$
$$
T_2=T_1(u_*^8+\kappa_1m_*)+\kappa_1^2f_*L_M(u_*)
=u_*^{16}-\kappa_2X.
\tag{2.4}
$$
直接使用 $\nu-\lambda\beta=-\alpha$、
$\lambda\beta_1=\alpha_1$ 和
$u_*=p+\alpha n_*+\alpha_1m_*$，得到完整三源身份
$$
\boxed{
F_w=-ak_*-bT_0,\qquad
F_q=k_*/\varepsilon+\beta T_0/\kappa_0+\beta_1T_1/\kappa_1,\qquad
F_e=T_2.
}
\tag{2.5}
$$
所以三者均在 $\mathcal J$ 中。它们可冗余加入原三个生成元；本稿没有仅凭 (2.5)
将原完整三生成元理想换成由 $F_w,F_q,F_e$ 单独生成的理想。

### 2.1 较小的全部原双源

(2.5) 负责完整当前理想身份。为保留较小的原 $S,Z$ 来源，另使用以下实际差商身份。

记源对 $\mathbf H=(0,B_H)$、$\mathbf K=(C_S,C_Z)$、
$\mathbf E=(\mathcal E_S,\mathcal E_Z)$；一个源对 $(A,B)$ 表示实际元素 $SA+ZB$。
所有乘法逐分量进行。令
$$
\mathbf E_0=(U^2-\varepsilon V)\mathbf K+\varepsilon^2\mathbf H,
$$
$$
\mathbf E_1=(U^4+\kappa_0N)\mathbf E_0,\qquad
\mathbf E_2=(U^8+\kappa_1M)\mathbf E_1.
\tag{2.6}
$$
它们分别是 $U^4-\kappa_0N$、$U^8-\kappa_1M$、$U^{16}-\kappa_2X$ 的原源。
对标量多项式 $p$，$p^{[1]}(z,w)$ 总表示准确有限差商。
全部原双源为
$$
\boxed{
\mathbf W=-a\mathbf K-b\mathbf E_0+f^{[1]}(U,u_*)\mathbf E,
}
$$
$$
\boxed{
\mathbf Q=\varepsilon^{-1}\mathbf K+\beta\kappa_0^{-1}\mathbf E_0
+\beta_1\kappa_1^{-1}\mathbf E_1-g^{[1]}(U,u_*)\mathbf E,
}
$$
$$
\boxed{
\mathbf T=\mathbf E_2-(z^{16})^{[1]}(U,u_*)\mathbf E.
}
\tag{2.7}
$$
即 $F_w=S\mathbf W_S+Z\mathbf W_Z$，另两式同理。
这些式子保持实际 U 和 u_*，不只在商中计算。

## 3. 奇系数消元不要求奇偶块保理想

作实际物理分解
$$
u_*=A+XB,\qquad A,B\in\mathcal B_{r+1},\qquad
\|A\|,\|B\|\le M_*.
\tag{3.1}
$$
这里只将 A,B 用作尾乘子；**没有声称 A、B、E 的奇块或偶块属于任何原理想。**

原 W,q 是纯线性尾，故准确写为
$$
W=W_0+w_1X,\qquad q=q_0+q_1X,
\quad W_0,q_0\in\mathcal B_{r+1},
$$
$$
w_1=\frac{2x+7}{(x+4)^4},\qquad
q_1=\frac{(x+1)^4}{(x+4)^4},\qquad
h:=w_1/q_1=\frac{2x+7}{(x+1)^4}.
\tag{3.2}
$$
有
$$
q_1>1/40,\qquad 0<h\le1.
\tag{3.3}
$$
此处 $q_0$ 是当前物理偶块，与早前正 k 枢轴中的标量正分母不是同一记号。

二项展开保留全部 $X^2=t$ 项：
$$
[f(A+XB)]_{\rm odd}=Bf'(A)+tR_f,\qquad
R_f=4bAB^3,
$$
$$
[g(A+XB)]_{\rm odd}=Bg'(A)+tR_g,
$$
$$
R_g=\frac{4\beta AB^3}{\kappa_0}
+\frac{\beta_1}{\kappa_1}
\left(56A^5B^3+56tA^3B^5+8t^2AB^7\right).
\tag{3.4}
$$
若 $d_w,d_q$ 是 $F_w,F_q$ 的奇系数，则
$$
d_w=w_1I-Bf'(A)-tR_f,\qquad
d_q=q_1I+Bg'(A)+tR_g.
$$
因此 B 项准确抵消：
$$
\boxed{
f'(A)d_q+g'(A)d_w=q_1D(A)+tE_o,
\qquad E_o=f'(A)R_g-g'(A)R_f,
}
\tag{3.5}
$$
其中
$$
D(z)=f'(z)+hg'(z)=1+c_1z+c_3z^3+c_7z^7,
$$
$$
c_1=2a+2h/\varepsilon,\qquad
c_3=4b+4h\beta/\kappa_0,\qquad
c_7=8h\beta_1/\kappa_1.
\tag{3.6}
$$
所有 $c_i>0$。下面既不倒转 B，也不直接倒转原奇系数 $d_w,d_q$。

## 4. 有限倒数将奇系数变成实际近单位

令 $J(z)$ 是 $D(z)^{-1}$ 在零点的十五阶 Taylor 截断：
$$
J(z)=\left[\sum_{k=0}^{15}(-c_1z-c_3z^3-c_7z^7)^k\right]_{\deg\le15}.
\tag{4.1}
$$
这只是有限多项式。准确有
$$
\boxed{
D(z)J(z)=1+z^{16}R_D(z),\qquad \deg R_D\le6.
}
\tag{4.2}
$$
定义
$$
S_{16}=\sum_{i=1}^{8}\binom{16}{2i}A^{16-2i}B^{2i}t^{i-1}.
$$
$F_e$ 的偶系数准确为 $A^{16}+tS_{16}$；其中 $-\kappa_2X$ 没有偶系数。

现在在原完整 $\mathcal J$ 中构造
$$
\boxed{
P_0=\big[F_qf'(A)+F_wg'(A)\big]J(A)/q_1
-XF_eR_D(A).
}
\tag{4.3}
$$
所有因子都是实际原尾算子。由 (3.5)、(4.2)，它的奇系数恰为
$$
\boxed{
Q_{\rm new}=I+t\Psi,\qquad
\Psi=E_oJ(A)/q_1-S_{16}R_D(A).
}
\tag{4.4}
$$
确切抵消为
$$
D(A)J(A)-A^{16}R_D(A)=I;
$$
其余所有 carry 项都在 $t\Psi$ 中。

下面 §5 在原范数中证明
$$
\|t\Psi\|\le e^{-85210181s}<1/2,\qquad
\|Q_{\rm new}^{-1}\|\le2.
\tag{4.5}
$$
故这是 $\mathcal B_{r+1}$ 中由实际 Neumann 级数支付的单位。
若 $C_0$ 是 $P_0$ 的偶系数，则
$$
\boxed{
P:=P_0Q_{\rm new}^{-1}=X+R,\qquad
R=C_0Q_{\rm new}^{-1}\in\mathcal B_{r+1},\quad \chi(R)=0.
}
\tag{4.6}
$$
字符结论从 (2.1)、(4.3) 的零字符和 $\chi(Q_{\rm new})=1$ 得到。

为把偶系数也完全明列，置
$$
\mathfrak e_d(A,B,t)=
\sum_{\substack{0\le i\le d\\i\ {\rm even}}}
\binom di A^{d-i}B^it^{i/2},
$$
$$
\mathfrak o_d(A,B,t)=
\sum_{\substack{1\le i\le d\\i\ {\rm odd}}}
\binom di A^{d-i}B^it^{(i-1)/2}.
$$
则
$$
c_w=W_0-A-a\mathfrak e_2-b\mathfrak e_4,\qquad
c_q=q_0+\mathfrak e_2/\varepsilon+\beta\mathfrak e_4/\kappa_0
+\beta_1\mathfrak e_8/\kappa_1,
$$
$$
d_e=\mathfrak o_{16}-\kappa_2I,\qquad
C_0=[c_qf'(A)+c_wg'(A)]J(A)/q_1-td_eR_D(A).
\tag{4.7}
$$
这包括 $-\kappa_2X$ 对 $-XF_eR_D(A)$ 偶块的全部影响。

全部原双源也立即明确：
$$
\boxed{
\mathbf P=
\left[
\mathbf Q\,f'(A)J(A)/q_1
+\mathbf W\,g'(A)J(A)/q_1
-\mathbf T\,XR_D(A)
\right]Q_{\rm new}^{-1}.
}
\tag{4.8}
$$
两个分量分别给 $P=S\mathbf P_S+Z\mathbf P_Z$。没有用源算子逆来推出这一身份。

## 5. 原 carry、全部差商和新单位的显式预算

原 carry 为
$$
u_j:=-\log\eta_j=1400\,16^j-630\,8^j+300\,2^j.
\tag{5.1}
$$
由 $\log x\le s$ 和前稿可取
$$
\varepsilon^{-1}\le e^{1404s},\qquad
\kappa_0^{-1}\le e^{25208s},\qquad
\kappa_1^{-1}\le e^{408816s}.
\tag{5.2}
$$
又 $\|U\|\le1\le M_*$、$\|A\|,\|B\|,\|u_*\|\le M_*$，所以
$$
\|f'(A)\|,\ \|f^{[1]}(U,u_*)\|\le e^{337511s},
$$
$$
\|g'(A)\|,\ \|g^{[1]}(U,u_*)\|\le e^{1137522s},
\qquad
\|(z^{16})^{[1]}(U,u_*)\|\le e^{1561503s}.
\tag{5.3}
$$
最后一式直接是 $16M_*^{15}$。
将 (1.3)、(1.5) 代入全部原源 (2.6)–(2.7)，得下表。
“原源”均指各自 S、Z 两个分量的最大值。

|实际元素|目标范数上界|每个原源范数上界|
|---|---:|---:|
|$F_w$|$e^{441610s}$|$e^{821000s}$|
|$F_q$|$e^{1241620s}$|$e^{1621000s}$|
|$F_e$|$e^{1665601s}$|$e^{2045000s}$|

例如第二行原源的最大项是
$e^{483020s}e^{1137522s}$；其余三项有严格余量。
第三行最大项是 $e^{483020s}16M_*^{15}$。
所以表中费用没有省去含 $\kappa_1^{-1}$ 的真实项。

(3.6) 给
$$
c_1\le e^{1406s},\qquad c_3\le e^{25211s},\qquad c_7\le e^{408819s}.
$$
(4.1) 中每个单项式 $c_1^ac_3^bc_7^c$ 满足 $a+3b+7c\le15$。
最大指数为
$$
1406a+25211b+408819c\le2\cdot408819+1406=819044.
$$
全部展开项数连同整数系数可由 $3^{16}$ 控制，故
$$
\|J\|_{\ell^1}\le e^{819100s},\qquad
\|R_D\|_{\ell^1}\le e^{1227922s}.
$$
对后者使用 (4.2)，删除前16个准确零系数及除以 $z^{16}$ 不增大系数绝对和。
于是
$$
\|J(A)\|\le e^{2380600s},\qquad
\|R_D(A)\|\le e^{1852522s}.
\tag{5.4}
$$

从 (3.4) 的全部二项项可取
$$
\|R_f\|\le e^{441610s},\qquad
\|R_g\|\le e^{1241621s},\qquad
\|E_o\|\le e^{1579133s}.
$$
同时
$$
\|S_{16}\|\le2^{16}M_*^{16}\le e^{1665612s}.
$$
结合 $q_1^{-1}<40<e^{4s}$，得到
$$
\boxed{\|\Psi\|\le e^{3959739s}.}
\tag{5.5}
$$
这是对完整实际 $\Psi$ 的上界，而不只是其主系数。
现在使用当前真实 carry，而不是一个抽象小参数：
$$
u_r=u_{n+4}\ge
(1400\cdot65536-630\cdot4096)s
=89169920s.
$$
因 $\|t\|=\eta_r$，故
$$
\boxed{
\|t\Psi\|\le e^{-(89169920-3959739)s}
=e^{-85210181s}<1/2.
}
\tag{5.6}
$$
这证明 (4.5)。

最后，(4.3) 三个乘因子的范数依次至多
$$
e^{2718115s},\qquad e^{3518126s},\qquad e^{1852522s}.
$$
使用上表和 $\|Q_{\rm new}^{-1}\|\le2$，可统一取
$$
\boxed{
\|P\|,\ \|R\|\le e^{4000000s},\qquad
\|\mathbf P_S\|,\ \|\mathbf P_Z\|\le e^{4350000s}.
}
\tag{5.7}
$$
$\|R\|\le\|P\|$ 也直接来自物理偶块提取，而不需要另损失一项。

### 5.1 变化起点族的较准确上型

仅在这一小节让 n 变化。由额外 k 提升稿 §7.1，同一个已选 $u_*$ 及其原源满足
$$
\log\max(1,\|u_*\|)\le P_c+O(\log(n+2)),\quad P_c=10u_n+4u_{n+1},
$$
$$
\log\max(1,\|\mathcal E_S\|,\|\mathcal E_Z\|)
\le C_E+O(\log(n+2)),\quad C_E=40u_n+19u_{n+1}.
$$
记
$$
C=u_n,\quad B_0=2u_n+u_{n+1},\quad
B_1=4u_n+2u_{n+1}+u_{n+2}.
$$
有限倒数中最大单项式的指数为 $2B_1+C+O(\log(n+2))$。
例如有一个 $c_7$ 时其最大竞争项为 $B_1+2B_0+2C$，
两者差为 $u_{n+2}-u_n>0$；没有 $c_7$ 时最大项为 $5B_0$，
同样更小。因此
$$
\log\|J(A)\|\le15P_c+2B_1+C+O(\log(n+2)),
$$
$$
\log\max(1,\|R_D(A)\|)
\le6P_c+3B_1+C+O(\log(n+2)).
$$
将实际三个目标与原源分别代入 (4.3)、(4.8)，最大项给
$$
\boxed{
\log\max(1,\|P\|,\|R\|)
\le275u_n+111u_{n+1}+3u_{n+2}+O(\log(n+2)),
}
$$
$$
\boxed{
\log\max(1,\|\mathbf P_S\|,\|\mathbf P_Z\|)
\le305u_n+126u_{n+1}+3u_{n+2}+O(\log(n+2)).
}
\tag{5.8}
$$
按实际当前位 $r=n+4$ 的 $16^r$ 尺度，上型分别不超过
$$
\boxed{\frac{493325}{8192},\qquad \frac{540575}{8192}.}
\tag{5.9}
$$
这里仍是**变化起点的指定原双行族**；固定 n 的一个原理想不能据此自动取得全部未来层的同一上型。

## 6. 保留完整理想后的四生成元尾交

令 $\mathcal D=\mathcal C_{r+1}$。在同一物理分块中准确写
$$
j_i=c_i+Xd_i,\qquad c_i,d_i\in\mathcal D,\qquad
\|c_i\|,\|d_i\|\le\|j_i\|,\quad i=1,2,3.
$$
因为 $P\in\mathcal J$ 且旧三个生成元继续保留，
$$
\mathcal J=(P,j_1,j_2,j_3)_{\mathcal C_r}.
\tag{6.1}
$$
这里添加了一个已付成员，不需要任意未知反向源单位。

定义四个实际下一尾生成元
$$
\boxed{
h_{\rm next}=R^2-t,\qquad
k_i=c_i-Rd_i\quad(i=1,2,3),
}
\qquad
\mathcal L=(h_{\rm next},k_1,k_2,k_3)_{\mathcal D}.
\tag{6.2}
$$
其准确原双源为
$$
\boxed{
h_{\rm next}=(R-X)P,\qquad
k_i=j_i-Pd_i;
}
\tag{6.3}
$$
即
$$
\mathbf H_{\rm next}=(R-X)\mathbf P,\qquad
\mathbf K_i=(\mathcal U_i,\mathcal V_i)-d_i\mathbf P.
\tag{6.4}
$$
根据 (1.8)、(5.7)，
$$
\|h_{\rm next}\|\le e^{8000001s},\qquad
\|\mathbf H_{{\rm next},S}\|,\|\mathbf H_{{\rm next},Z}\|
\le e^{8350001s},
$$
$$
\|k_i\|\le e^{6060001s},\qquad
\|\mathbf K_{i,S}\|,\|\mathbf K_{i,Z}\|\le e^{6410001s}.
\tag{6.5}
$$
因此全部新目标可统一用 $e^{8100000s}$，全部原源可统一用 $e^{8400000s}$ 控制。

### 6.1 代数、范数与超弱闭包的正反身份

正常有界余式为
$$
\mathfrak r(a+Xb)=a-Rb,\qquad
\|\mathfrak r\|\le1+\|R\|\le e^{4000001s}.
\tag{6.6}
$$
它在 $\mathcal D$ 上为恒等，而且
$$
Y-\mathfrak r(Y)=Pb\in\mathcal J
\quad\text{若 }Y=a+Xb.
\tag{6.7}
$$
正反身份完整为
$$
\boxed{
\mathcal J\cap\mathcal D=\mathcal L,\qquad
\mathcal J=\mathfrak r^{-1}(\mathcal L).
}
\tag{6.8}
$$
证明不仅是形式余式：对 $c,d\in\mathcal D$，
$$
\mathfrak r\big(P(c+Xd)\big)=-h_{\rm next}d,
$$
$$
\mathfrak r\big(j_i(c+Xd)\big)=k_i(c-Rd)-h_{\rm next}d_id.
\tag{6.9}
$$
故 $\mathfrak r(\mathcal J)\subseteq\mathcal L$。
反向 $\mathcal L\subseteq\mathcal J\cap\mathcal D$ 来自 (6.3)，再用 (6.7) 即得两式。

同一正常余式准确给
$$
\boxed{
\overline{\mathcal J}^{\|\cdot\|}
=\mathfrak r^{-1}\!\left(\overline{\mathcal L}^{\|\cdot\|}\right),\qquad
\overline{\mathcal J}^{uw}
=\mathfrak r^{-1}\!\left(\overline{\mathcal L}^{uw}\right).
}
\tag{6.10}
$$
从左到右使用余式连续性或正常性；从右到左将
$\mathcal L$ 中逼近 $\mathfrak r(Y)$ 的网加上固定的 $Y-\mathfrak r(Y)\in\mathcal J$。
此证明没有交换任意闭包与尾交，也没有偷偷假定原右源的一致范数。
结合 (1.7) 的已付前层正常余式，即给同一原 $(S,Z)$ 理想的完整下一尾交与其相应闭包。

还可将任意给定的下一尾表示明确送回原双源。
若 $Y=a+Xb$ 且
$$
\mathfrak r(Y)=h_{\rm next}b_0+\sum_{i=1}^3k_ib_i,
$$
则
$$
Y=Pb+h_{\rm next}b_0+\sum_{i=1}^3k_ib_i,
$$
原两个源各自的范数均至多
$$
\boxed{
e^{4350000s}\|Y\|
+e^{8400000s}\sum_{i=0}^3\|b_i\|.
}
\tag{6.11}
$$
这里 $b$ 是实际物理奇系数，$\|b\|\le\|Y\|$。
(6.11) 支付已给分解的全部返回费用，不声称每个尾元素自动存在统一有界的四源分解。

## 7. 同一原正常态与非零条件锚

若同一个原正正常 $\rho$ 湮灭 $S\mathcal A'+Z\mathcal A'$，
则 (2.7)、(4.8)、(6.4) 保证它湮灭本文所有实际目标的全部完整右倍数。
经过当前尾和下一尾的部分迹时一直使用这个固定 $\rho$；没有选择新的态，
也没有把余式映射当成正映射。

设 $e=2^{-1/2}(1,1)$ 是当前物理位的原真空向量，定义
$$
\Theta=2P(I+X)^{-2}.
$$
从 $X^2=t$，
$$
(I+X)^{-2}=\big((I+t)I-2X\big)(I-t)^{-2},
\qquad e^*Xe=(I+t)/2.
$$
因此直接二乘二计算给
$$
\boxed{e^*\Theta e=I,\qquad \omega_r(\Theta)=1.}
\tag{7.1}
$$
其中 $\omega_r$ 是原条件真空测试；它与被保留的湮灭态 $\rho$ 不是重新替换的同一个角色。
实际原双源就是 (4.8) 的两个分量右乘 $2(I+X)^{-2}$，且
$$
\|2(I+X)^{-2}\|\le\frac8{(1-\eta_r)^2}<9.
$$
由 (5.7)，
$$
\|\Theta\|\le e^{4001000s}.
\tag{7.2}
$$
所以将 $\Theta$ 归一到单位范数后，这个条件锚至少为 $e^{-4001000s}$。
这是一个明确非零但仍依赖 n 的实际锚；没有得到全层统一正下界，
也没有给正常 $\rho$ 的尾误差强加一个未经证明的衰减率。

## 8. 本步已经闭合与继续保留的范围

在同一固定原双行及其完整三生成元尾中，本步完成了：

1. 三条实际关系 $F_w,F_q,F_e$ 的完整当前理想来源与较小原双源。
2. 无需倒转奇块 B 的实际 $X+R$ 正规化，含全部 carry 项及实际 Neumann 单位。
3. 完整下一尾的四个生成元、正常余式、代数和两种闭包的正反身份及原来源费用。
4. 固定原正常态的全部完整右测试，以及显式非零条件锚。

所得下一尾四生成元一般不再是两条纯线性 $N_j$ 行。
未证明可将本步的有限倒数、次数和费用无损复制到固定起点的所有未来层；
未证明统一正常锚；也未把一般 gauge 双行自动化为这里的指定 S,Z。
下一实际输入是 (6.2) 的完整四生成元，或与它们明确等价且已付的实际关系系统。

