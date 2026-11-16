# R271 附录：完整低旗返回源、全出生有限池比较与跨头 Schur 能量可和

日期：2026-11-16（UTC）。

作者：Astra-ISP-789f / root、boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：已证明。** 对原 N/Y 头和同一个固定物理首头 $f_1=e_1$，本稿证明实际返回源 $\mathfrak h=C^*r$ 严格属于 $\ker C^{2d-1}\ominus\ker C^2$。用完整 canonical 双 Fock 塔保留所有出生和零源，再将远孔截到 $\ell=2d-2$，得到这个**整个来源**的真实核 Schur 能量之跨 $m$ 平方和。此前二远孔结论只读取第三旗；本稿不再投掉 $\mathfrak h$ 的其余低旗分量。

关键低块与混合项由第一行 MP 的准确下界钉住，高层零源不会改变它们。跨头修复的 fresh 池与原有限核列正交，故只付修复范数的平方。

仍未支付的是 $\ker C^{2d-1}$ 外高旗短缩，以及从正则化源度量中去掉低阶正项；因此不把本稿能量改称无罚二远孔费、完整 $q_{\flat}$ 费或 $N=M$。

内积对第一变量线性。所有物理向量均属于原二进制 $\ell^2(\mathbb N_0)$，不更换无限张量积参考。

依据：

- [完整 canonical 双 Fock 塔与二次碰撞条件数](R271-appendix-bosonic-dual-fock-tower-and-quadratic-collision-conditioning.md)，§§1–4；
- [原一步 carry、fresh 池与跨头核比较](R271-appendix-cross-head-finite-prefix-kernel-comparison-and-summable-first-row-gain.md)，§§1–2、4、8；
- [偶强段的完整可达核与第二 Green](R271-appendix-even-strong-prefix-reachable-kernel-and-first-head-second-green-schur.md)；
- [完整二远孔核 Stieltjes Schur](R271-appendix-complete-two-far-hole-kernel-stieltjes-schur-and-flag-source.md)，§5；
- [真实低链与无罚两远孔来源](R271-appendix-true-low-chain-two-hole-range-and-unpenalized-return-source.md)；
- [原顶部源流与同一物理投影](R271-appendix-strong-tail-block-same-top-source-flow-and-exact-two-fee-budget.md)，§2。

## 1. 原参数、核旗和完整物理截断核

取 $m\ge m_0\ge10$，写 $d=2^m$。强位数 $R_m$ 为偶数，
$$
x_m=m+R_m,\qquad h_m=d+R_m,\qquad
C_m=A_m+D_{[m,x_m)},\qquad C_m^{h_m}=0.
$$
本稿采用原合法强位尺度，具体要求
$$
e^{(25/2)d^3}\le x_m\le e^{13d^3},\qquad
y_m=(m+1)^4d\,x_m,\qquad
y_m+6d\le x_{m+1}.
\tag{1.1}
$$
全部位置端点为整数。§7 核对原 $\tau_{14}$ 选择满足这些要求。

暂固定 $m$，省去下标。令
$$
b_i=(i+1)^{-2},\qquad z_i=b_i^2,\qquad
S=S_x=\sum_{i\ge x}z_i,\qquad D=D_{[x,\infty)}.
$$
强头空间是有限维的原前 $x$ 位空间，记
$$
\mathcal F_j=\ker C^j,\qquad K=\mathcal F_1,\qquad Z=\ker C^*.
$$
偶 $R$ 的已付真实结论是 $K\subset\operatorname{Ran}C$，亦即 $K\perp Z$。所有 $C$ 的 MP 均在完整原强头度量中取值，未换成 Jordan 坐标。

对整数 $p\ge0$，定义闭物理子空间
$$
\mathscr K_{p,\infty}
=\ker(C+D)\cap\{N_{\ge x}\le p\},\qquad
\Pi_{p,\infty}=P_{\mathscr K_{p,\infty}}.
\tag{1.2}
$$
对有限池 $[x,y)$，所有 $i\ge y$ 位取真空，得到
$$
\mathscr K_{p,y}
=\ker(C+D_{[x,y)})\cap\{N_{[x,y)}\le p\}
 \otimes\Omega_{[y,\infty)} .
\tag{1.3}
$$
准确有 $\mathscr K_{p,y}\subset\mathscr K_{p,\infty}$。
令 $i_0g=g\otimes\Omega$。

原 $b\in\ell^1$，所以 $C+D$ 在整个原 Hilbert 空间有界。各固定远孔层及其有限直和均为闭空间；(1.2)–(1.3) 的核、正交投影和下文最小化因此有真正的 Hilbert 空间含义。

## 2. 全部出生、全部零源之后的完整源 Gram

对本节的有限或无限远池，记总平方权为 $S_\bullet$，最大平方权仍为 $z_x$。假设
$$
\epsilon_{\bullet,p}=\frac43\,\frac{z_x}{S_\bullet}\,p^2<1
\qquad(p\ge1).
\tag{2.1}
$$
原精确交换子给
$$
D_jD_j^*\succeq
[S_\bullet-2(j-1)z_x]I>0,\qquad 1\le j\le p.
$$
因此本节用到的每个完整 $D_j$ 都满射，$D_j^\dagger$ 有界；不是只在 primitive 范围使用一个形式右逆。

引用的 canonical 双塔定理给完整外部出生直和上的有界同构
$$
V_{\le p},\qquad
DV_{\le p}=V_{\le p}\mathfrak a,\qquad
I\preceq V_{\le p}^*V_{\le p}
\preceq(1-\epsilon_{\bullet,p})^{-1}I,
\tag{2.2}
$$
其中出生 $b$ 的第 $j-b$ 次降阶系数为 $\sqrt{(j-b)S_\bullet}$。这个界包含所有不同出生的交叉，不乘出生数。$C$ 只作用强头，故与整个 $V_{\le p}$ 对易。

设一个真实核列为 $v=(v_0,\ldots,v_p)$。其全部方程为
$$
Cv_j+Dv_{j+1}=0\quad(0\le j<p),\qquad Cv_p=0.
\tag{2.3}
$$
从顶端递推得 $C^{p+1}v_0=0$，所以其零远孔来源在 $\mathcal F_{p+1}$。

反过来，在 (2.2) 的准确出生坐标中，各出生独立满足
$$
y_{b,t}
=\frac{(-C)^t a_b}{\sqrt{t!\,S_\bullet^t}},
\qquad 0\le t\le p-b,\qquad
C^{p-b+1}a_b=0 .
\tag{2.4}
$$
对于任意 $a\in\mathcal F_{p+1}$，取 $a_0=a$、其余出生为零，再经 $V_{\le p}$ 返回，即得到零远孔为 $a$ 的真实核。因此零远孔取值映射的像准确为 $\mathcal F_{p+1}$，有有界右截面。

保留整个零远孔为零的核
$$
\mathscr Z_{p,\bullet}
=\{v\in\mathscr K_{p,\bullet}:v_0=0\}.
$$
令 $J_{p,\bullet}a$ 为所有 $v_0=a$ 的真实核列中的唯一最小范数者；等价地，
$J_{p,\bullet}a\perp\mathscr Z_{p,\bullet}$。定义完整源 Gram
$$
\mathcal H_{p,\bullet}=J_{p,\bullet}^*J_{p,\bullet}
\quad\text{于 }\mathcal F_{p+1}.
$$
它至少为恒等。这里所有非零出生、primitive 和其他零源均已真实最小化，并未被预先设为零。

定义比较矩阵
$$
H_{b,p}(S_\bullet)
=\sum_{j=0}^{p}\frac{(C^j|_{\mathcal F_{p+1}})^*
                         (C^j|_{\mathcal F_{p+1}})}
                        {j!\,S_\bullet^j}.
\tag{2.5}
$$
(2.4) 的外部出生本来正交；在固定 $a_0=a$ 时，其最小外部范数恰为 (2.5)，其余出生置零取等。用 (2.2) 的双边界，并允许全部出生进行物理最小化，得到
$$
\boxed{
H_{b,p}(S_\bullet)\preceq\mathcal H_{p,\bullet}
\preceq(1-\epsilon_{\bullet,p})^{-1}H_{b,p}(S_\bullet).
}
\tag{2.6}
$$
两端都是同一个完整源空间上的真二次型。

远真空 forcing 与 $\mathscr Z_{p,\bullet}$ 正交，故对任意强头 $g$，
$$
\begin{aligned}
P_{\mathscr K_{p,\bullet}}i_0g
 &=J_{p,\bullet}\mathcal H_{p,\bullet}^{-1}
           P_{\mathcal F_{p+1}}g,\\
q_{p,\bullet}(g)
 :=\|P_{\mathscr K_{p,\bullet}}i_0g\|^2
 &=\left\langle P_{\mathcal F_{p+1}}g,\,
       \mathcal H_{p,\bullet}^{-1}P_{\mathcal F_{p+1}}g\right\rangle.
\end{aligned}
\tag{2.7}
$$
所有源矩阵有限维且严格正；无限远池不产生未说明的逆定义域。

## 3. 第一行钉住完整低块，也钉住混合项

本节只用真实核方程和第一远孔的 MP，不需要把高层最小源猜成单出生。

若 $a\in\mathcal F_2$，任何以 $a$ 为零远孔的真核列都满足
$Dv_1=-Ca$。由于
$$
D_1D_1^*=S_\bullet I,\qquad
D_1^\dagger t=t\otimes\omega_1/S_\bullet,
\quad \omega_1=D^*\Omega,
$$
必有
$$
\|v\|^2\ge\|a\|^2+\frac{\|Ca\|^2}{S_\bullet}.
$$
而
$$
\boxed{
J_{p,\bullet}a
=(a,\,-Ca\otimes\omega_1/S_\bullet,\,0,\ldots,0)
\qquad(a\in\mathcal F_2,\ p\ge1)
}
\tag{3.1}
$$
是真核且取等，因为 $C^2a=0$。因此高层零源不可能降低这个下界，准确有
$$
\boxed{
\mathcal H_{p,\bullet}|_{\mathcal F_2}
=H_1(S_\bullet)
=I_{\mathcal F_2}+\frac{(C|_{\mathcal F_2})^*
                                  (C|_{\mathcal F_2})}{S_\bullet}.
}
\tag{3.2}
$$

更强地，对任意 $a\in\mathcal F_2$、$b\in\mathcal F_{p+1}$，
记 $v=J_{p,\bullet}b$。由 $Dv_1=-Cb$ 与 (3.1)，
$$
\boxed{
\langle J_{p,\bullet}a,J_{p,\bullet}b\rangle
=\langle a,b\rangle+\frac{\langle Ca,Cb\rangle}{S_\bullet}.
}
\tag{3.3}
$$
这保留完整 $J_{p,\bullet}b$；没有假设它的高出生分量为零。

以下回到无限原池 $S=S_x$。置
$$
G=(CC^*)^\dagger,\qquad
\Gamma=P_KG|_K,\qquad
v=(I+S\Gamma)^{-1}e_0,\qquad
r=(I-P_K)Gv,\qquad \mathfrak h=C^*r.
\tag{3.4}
$$
原两型都准确有 $Ce_1=e_0$、$Ce_0=0$。
令 $\mathcal U_2=\mathcal F_2\ominus K$。由于 $K\subset\operatorname{Ran}C$，
$$
C_2=C|_{\mathcal U_2}:\mathcal U_2\longrightarrow K
$$
为双射，且
$$
C_2^{-1}=C^\dagger|_K,\qquad
\Gamma=(C_2^{-1})^*C_2^{-1}.
\tag{3.5}
$$
所以
$$
P_{\mathcal U_2}C^*\Gamma v=C^\dagger v,\qquad
P_KC^*\Gamma v=0.
$$
另一方面 $C^*Gv=C^\dagger v$。因此
$$
\boxed{
\mathfrak h=C^\dagger v-C^*\Gamma v
=-P_{\mathcal F_2^\perp}C^*\Gamma v
\in\mathcal F_2^\perp.
}
\tag{3.6}
$$

令
$$
a_1=e_1-C^\dagger v\in\mathcal F_2.
$$
则
$$
Ca_1=e_0-v=S\Gamma v,\qquad H_1(S)a_1=e_1.
\tag{3.7}
$$
最后一式在 $\mathcal F_2$ 内使用 (3.5)，并非把 $C^*$ 当成保旗算子。

## 4. 原返回源的真正最高核旗

原 $C=A_m+D_{[m,x)}$ 的两部分及其伴随交叉对易。
对 $k\ge1$，
$$
\operatorname{ad}_C^k(C^*)
=\operatorname{ad}_{A_m}^k(A_m^*)
 +\operatorname{ad}_{D_{[m,x)}}^k(D_{[m,x)}^*).
\tag{4.1}
$$
对平方自由删除 $D_<:=D_{[m,x)}$，
$$
[D_<,D_<^*]=\sum_{m\le i<x}b_i^2(1-2n_i),\qquad
[D_<,[D_<,D_<^*]]=-2\sum_{m\le i<x}b_i^3E_i,
$$
所以 $\operatorname{ad}_{D_<}^3(D_<^*)=0$。

同时 $A_m^d=0$。在
$$
\operatorname{ad}_{A_m}^k(A_m^*)
=\sum_{j=0}^k(-1)^j\binom kj A_m^{k-j}A_m^*A_m^j
$$
中，$k\ge2d-1$ 时每项都有一个幂至少为 $d$，故为零。
由于 $d\ge2$，得到
$$
\operatorname{ad}_C^{2d-1}(C^*)=0.
$$
对 $\Gamma v\in K$，准确有
$$
C^kC^*\Gamma v=\operatorname{ad}_C^k(C^*)\Gamma v.
$$
再用 $C^\dagger v\in\mathcal F_2$，(3.6) 给出
$$
\boxed{
\mathfrak h\in\mathcal F_{2d-1}\ominus\mathcal F_2.
}
\tag{4.2}
$$
这里没有使用 $A_m$ 按物理孔数单降阶；它的非齐次 carry 全部包含在 (4.1) 中。此结论限制的是实际来源 $\mathfrak h$，不是任意完整 inverse 解。

现在取
$$
p=\ell_m=2d-2,\qquad
\mathcal U_m=\mathcal F_{\ell_m+1}\ominus\mathcal F_2 .
$$
将完整物理 $\mathcal H_{\ell_m,\infty}$ 按
$\mathcal F_2\oplus\mathcal U_m$ 分块：
$$
\mathcal H_{\ell_m,\infty}
=\begin{pmatrix}H_1&\mathcal B_m^*\\
                 \mathcal B_m&\mathcal D_m\end{pmatrix},
\qquad
\mathcal S_m=\mathcal D_m-\mathcal B_mH_1^{-1}\mathcal B_m^*>0.
\tag{4.3}
$$
(3.3)–(3.7) 与 (4.2) 准确给
$$
\boxed{\mathcal B_ma_1=-\mathfrak h.}
\tag{4.4}
$$
完整正块逆因此满足
$$
\boxed{
q_{\ell_m,m}(f_1)-q_{1,m}(f_1)
=\langle\mathfrak h_m,\mathcal S_m^{-1}\mathfrak h_m\rangle.
}
\tag{4.5}
$$
没有再对 $\mathfrak h_m$ 投到第三旗；(4.5) 读取其全部实际分量。零维 $\mathcal U_m$ 时两端均为零，按此惯例处理。

## 5. 全出生有限池截尾与精确投影损失

令 $S_f=S_x-S_y=(1-t)S$、$t=S_y/S_x$。若
$$
\epsilon_{f,p}=\frac43\,\frac{z_x}{S_f}\,p^2<1,
$$
有限和无限池的 (2.6) 在同一个 $\mathcal F_{p+1}$ 上给
$$
\mathcal H_{p,y}
\preceq(1-\epsilon_{f,p})^{-1}H_{b,p}(S_f)
\preceq\frac{H_{b,p}(S)}{(1-\epsilon_{f,p})(1-t)^p}
\preceq\frac{\mathcal H_{p,\infty}}
             {(1-\epsilon_{f,p})(1-t)^p}.
$$
取真正正逆并用 (2.7)，对所有完整强头 $g$ 得
$$
\boxed{
q_{p,y}(g)\ge(1-\epsilon_{f,p})(1-t)^p q_{p,\infty}(g).
}
\tag{5.1}
$$
由于两个空间在原物理内积中真的嵌套，
$$
\begin{aligned}
\|(\Pi_{p,\infty}-\Pi_{p,y})i_0g\|^2
&=q_{p,\infty}(g)-q_{p,y}(g)\\
&\le(\epsilon_{f,p}+pt)\|g\|^2 .
\end{aligned}
\tag{5.2}
$$
这里完整 canonical 比较已经支付所有出生；没有先以单列估计替代全 Gram，也没有将有限池和无限池的 primitive 空间作未经证明的等距认同。

对 (1.1) 和 $p=\ell_m<2d$，连续尾积分界
$$
\frac1{3(x+1)^3}\le S_x\le\frac1{3x^3},\qquad
\frac{z_x}{S_x}\le\frac3{x+1}
$$
给
$$
t_m\le\left(\frac{x_m+1}{y_m}\right)^3
\le\frac8{d^3(m+1)^{12}}\le\frac12 ,
$$
$$
\boxed{
\epsilon_{f,\ell_m}\le\frac{32d^2}{x_m+1},\qquad
\ell_mt_m\le\frac{16}{d^2(m+1)^{12}}.
}
\tag{5.3}
$$
在 (1.1) 下，$\epsilon_{f,\ell_m}<1/2$，其无限池版本也小于 $1/2$。

## 6. fresh 修复的正交性与完整跨头可和增益

取固定 $f_1=e_1$，$\|f_1\|=1$，令
$$
k_m=\Pi_{\ell_m,y_m}f_1,\qquad
q_{\mathrm{fin},m}=\|k_m\|^2.
$$
这是支撑于原有限位置 $[0,y_m)$ 的完整真实 $L_m$ 核列。

为说明修复仍保持所有高层来源，复写其有限公式。按新 bit $m$ 分组，
$$
A_0=A_m+b_mE_m,\quad A_1=A_{m+1},\quad
D_{\rm old}=D_{[m+1,y_m)},\quad
\Delta_m=A_1-A_0 .
$$
原两型的一步完整块预算是
$$
\|\Delta_m\|\le18\kappa_{m-1},\qquad
-\log\kappa_{m-1}=\frac{175}{2}d^4-\frac{315}{4}d^3+150d.
\tag{6.1}
$$
它来自所引跨头稿 §2 的真实 $Z_{i,m}$ 权比和 Y 型 Cayley 交叉；不是以全 $T-L_m$ 尾和代替一步。

设 $\xi_m=\Delta_mk_m$、$B=A_1+D_{\rm old}$。
由 $(A_0+D_{\rm old})k_m=0$ 和独立尾交换，
$$
D_{\rm old}^j\xi_m=\Delta_m(-A_0)^jk_m,\qquad
A_0^{d+1}=0,\quad A_1^{2d}=0,\qquad B^{3d}\xi_m=0 .
\tag{6.2}
$$
故这个终止阶数与 $k_m$ 的远孔上界无关。

在 fresh 池 $[y_m,y_m+6d)$ 上取 $N=6d$，定义
$$
v_q=\frac{(N-q)!}{N!}
\sum_{\substack{I\subset[y_m,y_m+N)\\|I|=q}}b_I^{-1}e_I,
\qquad 0\le q\le3d .
$$
逐位计数与原权下界给
$$
D_{\rm fresh}v_q=v_{q-1},\qquad
\|v_q\|^2\le\frac{(N-q)!}{N!\,q!}\,(y_m+6d)^{4q}.
$$
因此
$$
U\xi_m=\sum_{j=0}^{3d-1}(-B)^j\xi_m\otimes v_{j+1},
\qquad (B+D_{\rm fresh})U\xi_m=\xi_m,
$$
$$
\|U\xi_m\|\le\delta_m\|k_m\|,\qquad
\delta_m=18\kappa_{m-1}\sqrt{3d}\,14^{3d}(y_m+6d)^{6d}.
\tag{6.3}
$$
这里不同 fresh 孔层正交。由于新增 $y_m$ 只多了一个因子 $d$，
$$
\log(y_m+6d)
\le13d^3+\log d+4\log(m+1)+\log2 .
$$
将它代入 (6.3)，对 $m\ge10$，
$$
\begin{aligned}
\log\delta_m
\le{}&-\frac{19}{2}d^4+\frac{315}{4}d^3
 +6d\log d+24d\log(m+1)\\
&+(6\log2+3\log14)d+\log18+\tfrac12\log(3d)
\le-9d^4 .
\end{aligned}
\tag{6.4}
$$
末步可先将所有正项合并为 $80d^3$，再用 $80d^3\le d^4/2$；
$m\ge10$ 时 $d\ge1024$，这些整数边界均满足。

由 (1.1)，
$$
\widetilde k_m=k_m-U\xi_m\in
\mathscr K_{0,m+1}=\ker C_{m+1}\otimes\Omega_{\ge x_{m+1}}.
$$
现在使用此前未用的准确正交性：
$k_m$ 和 $f_1$ 在整个 fresh 池是真空，而 $U\xi_m$ 每项的 fresh 孔数至少一。因此
$$
\langle k_m,U\xi_m\rangle=\langle f_1,U\xi_m\rangle=0,
$$
$$
\langle f_1,\widetilde k_m\rangle=q_{\mathrm{fin},m},
\qquad
\|\widetilde k_m\|^2
=q_{\mathrm{fin},m}+\|U\xi_m\|^2
\le(1+\delta_m^2)q_{\mathrm{fin},m}.
$$
以这个真实新核向量测试投影；若 $q_{\mathrm{fin},m}=0$，下式直接成立，否则除以其范数平方：
$$
q_{0,m+1}\ge\frac{q_{\mathrm{fin},m}}{1+\delta_m^2}.
$$
结合 (5.1)，得到
$$
\boxed{
q_{0,m+1}\ge
\frac{(1-\epsilon_{f,\ell_m})(1-t_m)^{\ell_m}}
     {1+\delta_m^2}\,q_{\ell_m,m}
\ge q_{\ell_m,m}-E_m,
}
\tag{6.5}
$$
其中可取
$$
E_m=\frac{32d_m^2}{x_m+1}
  +\frac{16}{d_m^2(m+1)^{12}}+e^{-18d_m^4}.
\tag{6.6}
$$
这只付有限池误差及修复误差的平方，没有经过向量差的平方根三角估计。

同一 $m$ 的物理核嵌套给
$0\le q_{0,m}\le q_{1,m}\le q_{\ell_m,m}\le1$。
对 (6.5) 望远镜，并保同一个固定物理 $f_1$：
$$
\boxed{
\begin{aligned}
\sum_{m\ge m_0}(q_{\ell_m,m}-q_{0,m})
&\le1-q_{0,m_0}+\sum_{m\ge m_0}E_m\\
&\le1+4^{1-m_0}<2 .
\end{aligned}}
\tag{6.7}
$$
最后用 (1.1) 逐项得 $E_m\le3d_m^{-2}$，故
$\sum_{m\ge m_0}E_m\le3\sum_{m\ge m_0}4^{-m}=4^{1-m_0}$。

结合 (4.5)，这支付了整个实际低旗来源：
$$
\boxed{
\sum_{m\ge m_0}
\langle\mathfrak h_m,\mathcal S_m^{-1}\mathfrak h_m\rangle
\le1+4^{1-m_0}<2 .
}
\tag{6.8}
$$
这不是仅第三旗投影的预算，也没有取 $\|\mathcal S_m^{-1}\|$ 的环境上界。

## 7. 与原 Q 母窗、全部 h 段和真帽门的相容

可直接使用原 $\tau_{14}$ 切点：
$$
\tau_{14,m}
=\frac{\Lambda_{m-1}+14d_m^3+\log16}{d_m/2-1},
\qquad
R_m=2\lceil2e^{\tau_{14,m}}\rceil,\qquad x_m=m+R_m .
$$
所引跨头稿 §8 已逐原权证明
$$
\frac{25}{2}d_m^3\le\tau_{14,m}\le\frac{51}{4}d_m^3,
\qquad \log x_m\le13d_m^3,\qquad
\tau_{14,m+1}\ge100d_m^3 .
$$
而
$$
\log(y_m+6d_m)
\le13d_m^3+\log d_m+4\log(m+1)+\log2
<14d_m^3<100d_m^3 .
$$
故本稿多出的因子 $d_m$ 仍保 $y_m+6d_m\le x_{m+1}$。
全部 (1.1) 条件都由同一个原参数选择实现。

取原
$$
Q_m=d_m^2h_m .
$$
则 $4d_m\le Q_m<e^{14d_m^3}<e^{(1601/64)d_m^3}$，且
$Q_m\ge R_m+\ell_m$。所以 $\mathscr K_{\ell_m,\infty}$ 的每个向量都是原同一 $K_{m,Q_m}$ 中的真核向量：强尾至多 $R_m$ 孔，远尾至多 $\ell_m$ 孔。修复后的向量支撑于 $[0,x_{m+1})$，同样属于下一原 $K_{m+1,Q_{m+1}}$。

原 matched 来源仍用全部 $h_m$ 段，不以 $\ell_m$ 代替其 nilpotent 长度。原真帽 cut 可继续取
$$
Q_m/2\le n\le Q_m-R_m-2h_m-1 ,
$$
所以 $n+2h_m+R_m<Q_m$ 严格保持。正 Riordan / 逆伴随 / 外部帽投影只在其原已付范围使用。本稿的核投影增益并不自动成为原返回范数；这里核的是新真核能够进入原同窗正交关系。

## 8. 同一来源的完整 bosonic 正度量，以及准确未付的去正则化

令 $H_{b,\ell_m}(S_m)$ 在
$\mathcal F_2\oplus\mathcal U_m$ 上的 Schur 为 $\mathcal S_{b,m}$。
它的低块和混合项与 §3 完全相同。由 (2.6) 的真正 Schur 单调性，
$$
\mathcal S_{b,m}\preceq\mathcal S_m
\preceq(1-\epsilon_{\infty,\ell_m})^{-1}\mathcal S_{b,m}.
$$
因此 (6.8) 还给
$$
\boxed{
\sum_m\langle\mathfrak h_m,\mathcal S_{b,m}^{-1}\mathfrak h_m\rangle
\le2(1+4^{1-m_0})<4 .
}
\tag{8.1}
$$
这里 $\epsilon_{\infty,\ell_m}<1/2$；逆序没有颠倒。

把这个正度量展开即可看清尚未消失的项。设
$$
J=C|_{\mathcal F_2},\qquad T=C|_{\mathcal U_m},
\qquad
M_{2,m}=\sum_{j=2}^{\ell_m}
 \frac{(C^j|_{\mathcal U_m})^*(C^j|_{\mathcal U_m})}{j!S_m^j}.
$$
$M_{2,m}>0$，因为 $\ker C^2\cap\mathcal U_m=\{0\}$。完整低块消元准确给
$$
\boxed{
\mathcal S_{b,m}
=M_{2,m}+I_{\mathcal U_m}
 +T^*(S_m I+JJ^*)^{-1}T .
}
\tag{8.2}
$$
(8.1) 支付的是 (8.2) 整体逆在同一 $\mathfrak h_m$ 上的二次型。
它不允许去掉 $I_{\mathcal U_m}$ 或最后的正项后仍使用同一个上界。

此外，完整无罚来源
$$
q_{\flat}=(C^{*2})^\dagger\mathfrak h,\qquad
\gamma_{\flat}^2=\|\omega_2\|^2\|q_{\flat}\|^2
$$
仍在整个强头上取最小范数。即便 $\mathfrak h$ 满足 (4.2)，其最小解也未证明留在 $\mathcal F_{2d-1}$。全高度 positive-far coherent Gram 对更高旗的完整 Schur 同样不能由本稿低旗压缩替换。正压缩取逆与全逆的次序必须保留。

因此新增结论是：**整个实际 $\mathfrak h=C^*r$ 在其真实低旗核 Schur 中的跨头能量已可和，且完整 bosonic 正度量也已支付。** 去正则化、外部高旗返回和原帽费用仍是后续目标，$N=M$ 未证明。
