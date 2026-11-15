# R407：同三矩内区路径上的 self 外区刚性与全部镜点的真实通量表

日期：2026-11-15。**完整原式纸面证明；没有执行研究积分、符号程序、零点计数、数值秩或人工测试。**

[R405](R405-common-exterior-packets-and-local-ordered-currents-at-all-internal-degeneracies.md) 已构造共同外区的新十九根，并准确计算跨包项。本稿补上其中保留的同包项：在原三矩保持、变化只发生于固定内区的真实连通路径上，whole self 为零使 $S_u''$ 在两侧外区准确不变。这里没有把全部同矩纤维宣布为连通，也没有删除左侧仿射 history。

由此得到所有实际包两镜点的完整 $d/e$ 查询公式。实际仅付 whole-$E$ 时，右镜点保留两个真正整包通量；这些量可用一份有限自然查询表准确读出，无需假设全部紧输入的自然函数为零。仅在 signed $\ker(E,\Lambda_{\rm all})$ 上，才进一步得到全部镜点的公共有限系数表。有限生成数不是秩，也不授实际联合满射。

直接来源：[R56](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)、[R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R389](R389-ordered-total-fluxes-and-complete-flat-end-germs-for-the-rational-port.md)、[R394](R394-conditional-complete-period-and-finite-same-gauge-interface.md)、[R403](R403-one-pair-degeneracies-and-nineteen-exact-rational-targets-by-concentration.md)、R405。

## 1. 固定同一原成本与真实范围

首先沿原 $M=0$、同端口且闭 frame 的 canonical 路径证明，随后对这些真实成本的有限实组合线性延拓。保留原共同右锚 $r_*$、原 $s_0$ 初值、全部几何历史和同一个 canonical 恢复。记
$$
\mathscr K(A,B)=\mathscr P H(A,B),\qquad
Z(u,v)=\operatorname{Range}H(Y_u,Y_v),\qquad Z_u=Z(u,u).
$$
$\mathscr K$ 是完整 characteristic 周期的对称双线性配对，不是只取某个局部 forcing 或 ruling 的能量。

原 self 查询准确为
$$
S_{V,u}=V(u^2,0)=-\mathscr K(Z_u,Z_u).
\tag{1}
$$
这个不需要 $\pi V=0$ 的第一等式直接来自 R56 §8 的原第四 forcing：取 $\phi=0$、$D=u^2$ 时 $Y_\phi=0$，原 $YC$ 项为零，只剩负的二阶平方；等价地，在 R389(9)的原定义中作同一代入。只有后续 $-\mathscr K(Z_u,Z_u)=4\mathscr P H(Y_u,C(u;u^2))$ 才使用 whole pure。本稿的(1)始终保留原单包左尾。

三矩及其极化为
$$
\mu(u)=\left(\int (u'')^2,\ \int x(u'')^2,\
 \int\{x^2(u'')^2+2(u')^2\}\right),
$$
$$
m(u,v)=\left(\int u''v'',\ \int xu''v'',\
 \int\{x^2u''v''+2u'v'\}\right).
\tag{2}
$$
whole self 条件 $\mathcal QV=0$ 表示：对全部真实紧输入 $u$，(1)原左尾的二次系数为零。只在一个有限投影 $P_LE$ 上为零不够。

第2—4节在上述 $M=0$/同端口闭 frame 的路径范围内，只再需要这个 whole self 条件及原 canonical 二阶归一；不额外要求 $\pi V=0$ 或某个指定的第三 hook。尤其(9)的 $s$ 端项相消使用原周期场，并非任意非零 $M$ 的路径恒等。接完整 mixed 圆时再用
$$
M=0,\qquad T=\tau_{\rm hook}\mathfrak H,\quad
\tau_{\rm hook}\ne0,\qquad
E(V)=(\pi V,\mathcal QV)=0.
\tag{3}
$$
(3)必须是同一个实际成本或同一个真实 signed 类的条件；不由十九根自动继承，也不从旧几何、Morse 或某个 gauge 结论转移。

## 2. 同三矩的内区变化使完整极化二阶场双侧为零

设 $t\mapsto u_t$ 是一个光滑紧 profile 路径，变化 $\dot u_t$ 全部支撑于固定严格内区 $J$，且
$$
\mu(u_t)=\mu(u_0).
\tag{4}
$$
两侧外区上的 $u_t$ 本身因此不变。由(2)，
$$
m(u_t,\dot u_t)=0
\tag{5}
$$
是三个完整标量身份，包含第三矩中的 $2u_t'\dot u_t'$。

forcing $H(Y_{u_t},Y_{\dot u_t})$ 在 $J$ 外准确为零。仍须检查其恢复场的左尾，不能仅凭 forcing 支撑便宣告局部性。

R73(2)、(10)—(12)的原二阶恢复给左尾
$$
P_{\rm left}(s)
=\frac{(1+d^2)m_0+2hdm_1+h^2m_2}{8h},
\qquad
W_{\rm left}(s,x)=\Phi_{m(s)}(u_t,\dot u_t)\big|_{\rm left}.
\tag{6}
$$
这里 $m(s)=\int_{s_0}^sM$ 是原八维历史；式(6)左边的三个 profile 矩全部按(5)取零。$W_{\rm left}$ 对这些矩线性，故整条真实历史都为零。局部的 $B$ 为零，R56(6)左外区的 $\eta_0=-P_s/2$ 也为零。右端仍是原右锚和零初值。

所以得到完整场身份
$$
\boxed{Z(u_t,\dot u_t)=0\quad\text{在 }J\text{ 的两侧外区、对全部 }s.}
\tag{7}
$$
没有把单包 $Z_{u_t}$ 宣告为左紧，也没有重置任何 $s$ 段首值。在 $M=0$ 的原闭路径上，这仍是同一归一的周期场。

## 3. self 的 cap 二阶导数沿该路径准确不变

原 range 对 forcing 线性，故
$$
\partial_tZ_{u_t}=2Z(u_t,\dot u_t).
$$
由(1)得到完整四次变分
$$
\boxed{
\partial_tS_{V,u_t}
=-4\mathscr K\bigl(Z_{u_t},Z(u_t,\dot u_t)\bigr).
}
\tag{8}
$$
系数 $4$ 同时来自二阶极化和平方微分。

由(7)，式(8)的整个 forcing 支撑于 $J$。在 $J$ 左方，R56 的 $B,T_s$ 为零，而 $P$ 是真实的 $x$ 常数；原周期输出为
$$
\int_{\rm path}(K_0P-\lambda P_s)\,ds
=\int_{\rm path}(K_0+\lambda_s)P\,ds.
\tag{9}
$$
使用的是同一完整周期，原端点项按周期性相消。$K_0$ 至多二次、$\lambda_s$ 至多一次，故(9)是实际二次多项式。在 $J$ 右方，整个输出准确为零。

whole $\mathcal QV=0$ 对每个 $u_t$ 都成立。因此 $\partial_tS_{V,u_t}$ 的原左二次系数也为零。式(9)在整个左外区是同一个多项式，遂得
$$
\boxed{
\partial_tS_{V,u_t}''=0
\quad\text{在 }J\text{ 的两侧外区}.
}
\tag{10}
$$
积分后
$$
\boxed{
S_{V,u_1}''=S_{V,u_0}''
\quad\text{在共同两侧外区}.
}
\tag{11}
$$

这正是需要的 self cap 身份。它没有证明左侧的 $S$ 或 $S'$ 不变：两者仍可改变一个真实仿射多项式。没有 whole self 条件时，(8)—(9)只给左侧二阶导数的变化为一个常数；这个常数不能删除。

## 4. R405 的每个最终包都有所需的真实连通路径

R405 的新母包为 $u_0=\psi_3+v_0$，$v_0$ 与全部纠正方向 $e_\ell$ 都支撑于 $(-1/2,1/2)$。对一个最终基本包，
$$
U_{i,N,z}
=u_0+z\,w_{N,b_i}
+\sum_\ell c_{i\ell,N}(z)e_\ell,\qquad
\mathcal F_{\rm rat}(U_{i,N,z})=\mathcal F_{\rm rat}(u_0).
\tag{12}
$$
原 $\mathcal F_{\rm rat}$ 包含全部三矩。

在选择最终有限 $N$ 时，把低阶 IFT 的固定幅度盒取为同时包含 $0$ 和十九根所在正盒的紧盒。脉冲在这个盒中一致为 $C^2$ 小量。R405 的真最大限制秩和同一有限 minor 使(12)的纠正映射在整个盒上定义，且 $c_{i\ell,N}(0)=0$。增大有限 $N$ 满足这条一致性不改变原十九量的 $C^1$ 极限或有限根证明。

对最终的有限幅度 $z_i^N$，取
$$
U_{i,t}
=u_0+t z_i^N w_{N,b_i}
+\sum_\ell c_{i\ell,N}(t z_i^N)e_\ell,
\qquad 0\le t\le1.
\tag{13}
$$
这是实际光滑连通路径。它准确保持整个 $\mathcal F_{\rm rat}$，特别保持(4)，且所有变化都在固定内区。中间 $t$ 不需要保持十九量为零；本段只把它作为同一 universal 输入空间中的恒等式路径。真正研究圆仍取 $t=1$ 的准确十九根。

保留每个实际宽度与中心：
$$
u_i(x)=U_i((x-\xi_i)/w_i),\qquad
v_{\xi_i,w_i}(x)=u_0((x-\xi_i)/w_i),\qquad w_i>0.
\tag{14}
$$
正仿射变换对(2)是可逆三角输运，因此(13)在物理坐标中仍保持全部三矩；变化支撑于 $\xi_i+w_i(-1/2,1/2)$。

由(11)，所有实际包满足
$$
\boxed{
S_{V,u_i}''(x)=S_{V,v_{\xi_i,w_i}}''(x)
\quad\text{当 }\tfrac12\le |(x-\xi_i)/w_i|<1.
}
\tag{15}
$$
这里 self 的参考输入是完整的固定 $u_0$，不能只凭共同外区就把它换成具有另一内区的 $\psi_3$。该替换需要另一条真实同矩路径，本文没有假设它存在。

结论只沿(13)所构造的连通部分成立，不从一个一阶核身份外推到整个可能不连通的同矩纤维。

## 5. 两侧 self cap 与原跨包 cap 的共同数据

原两个退化点为
$$
x_i^\pm=\xi_i\pm w_i a_*,
\qquad \ell_i=\xi_i-w_i,\quad r_i=\xi_i+w_i.
$$
定义两个有向均为从左到右的参考 self cap 积分
$$
s_V^-(\xi,w)
=\int_{\xi-w}^{\xi-wa_*}v_{\xi,w}'S_{V,v_{\xi,w}}'',
$$
$$
s_V^+(\xi,w)
=\int_{\xi+wa_*}^{\xi+w}v_{\xi,w}'S_{V,v_{\xi,w}}''.
\tag{16}
$$
由(15)及共同外区，实际 $u_i$ 的相应两个积分正好等于(16)。

跨包采用 R405(23)、(27)的原函数
$\mathcal U_{V,n}=4Q_{V,n}$。在(3)下，它的二阶导数是明确局部式；保留 R405(37)的两个 cap 量
$$
L_V^-(\xi,w,n)
=\int_{\xi-w}^{\xi-wa_*}v_{\xi,w}'\mathcal U_{V,n}(v_{\xi,w})'',
$$
$$
L_V^+(\xi,w,n)
=\int_{\xi+wa_*}^{\xi+w}v_{\xi,w}'\mathcal U_{V,n}(v_{\xi,w})''.
\tag{17}
$$
本式改用完整 $u_0$ 作参考，与 R405 用 $\psi_3$ 的值相同，因为该二阶导数是局部式且 cap 准确一致。这一点与 self 的(15)证明不同。

所有量都是原成本的线性查询，系数保留完整 $s$ history。相同真实宽度的包使用同一组 $(s^\pm,L^\pm)$；不同宽度必须继续保留显示参数 $w$。

## 6. 全部实际内部点的两个通道，而不是只有消 self 组合

写
$$
f=\sum_i a_i u_i,\qquad g=\sum_i b_i u_i,\qquad
R_i=a_i^2-b_i^2,\quad T_i=a_ib_i,
$$
并定义真实有序 suffix
$$
n_{R,i}=\sum_{j>i}R_j\mu(u_j),\qquad
n_{T,i}=\sum_{j>i}T_j\mu(u_j).
\tag{18}
$$
全部幅度、正宽、五块/八副本/十二副本及最后实际位置都在(18)中，不换成裸 cell 平均。

R389 的完整函数身份为
$$
V_d=\sum_i a_i^2\{R_iS_i+\mathcal U_{V,n_{R,i}}(u_i)\},
$$
$$
V_e=-\sum_i a_i^2\{T_iS_i+\mathcal U_{V,n_{T,i}}(u_i)\}.
\tag{19}
$$
在当前包上，其他 outer 包只贡献右零或真左仿射尾，其二阶导数由 whole self 条件为零。令原未扣平台的查询
$$
H_{d,i}^{\pm}=\int_{\ell_i}^{x_i^\pm}f'V_d'',\qquad
H_{e,i}^{\pm}=\int_{\ell_i}^{x_i^\pm}f'V_e''.
\tag{20}
$$
左镜点完整值因而是
$$
\boxed{
H_{d,i}^{-}
=a_i^3\{R_i s_V^-(\xi_i,w_i)+L_V^-(\xi_i,w_i,n_{R,i})\},
}
$$
$$
\boxed{
H_{e,i}^{-}
=-a_i^3\{T_i s_V^-(\xi_i,w_i)+L_V^-(\xi_i,w_i,n_{T,i})\}.
}
\tag{21}
$$

为右镜点保留真实总量
$$
\omega_i(V)=\int u_i'''S_i=\Lambda_{u_i}(V),\qquad
\mathcal A_{V,u_i}(n)=\int u_i'''\mathcal U_{V,n}(u_i).
\tag{22}
$$
这里 natural 等于 raw 的一步使用实际 $\pi V=0$ 及 R389 的完整有序 pure 极化；一般成本上不能直接使用这个等号。

定义两组原 mixed 整包通量
$$
\mathcal T_{d,i}
=a_i^3\{R_i\omega_i+\mathcal A_{V,u_i}(n_{R,i})\},
$$
$$
\mathcal T_{e,i}
=-a_i^3\{T_i\omega_i+\mathcal A_{V,u_i}(n_{T,i})\}.
\tag{23}
$$
它们准确等于 $\int_{\ell_i}^{r_i}f'V_{d/e}''$。所以
$$
\boxed{
H_{d,i}^{+}
=\mathcal T_{d,i}
-a_i^3\{R_i s_V^+(\xi_i,w_i)+L_V^+(\xi_i,w_i,n_{R,i})\},
}
$$
$$
\boxed{
H_{e,i}^{+}
=\mathcal T_{e,i}
+a_i^3\{T_i s_V^+(\xi_i,w_i)+L_V^+(\xi_i,w_i,n_{T,i})\}.
}
\tag{24}
$$
右侧换端花掉的是(23)，不是一个可自行选择的常数。

因此在 whole-$E=0$ 的实际背景上，两个镜点的四个原 partial 条件，等价于(21)右边为零以及(24)中的两条准确等式。若还要求解析平端的两组整包条件为零，便另取 $\mathcal T_{d,i}=\mathcal T_{e,i}=0$；不能先将它们删除。

对 R394 的实际目标 $G_{d/e}=-V_{d/e}^{\,c}/(2\tau_{\rm hook})$，所加 incoming $L_f$ 项在简单 $A_f$ 点的原 partial 通量为零。因此(20)仍按这个明确非零因子给所需内部兼容条件，不产生新的 gauge 自由。

## 7. 有限原自然查询已能准确承载全部整包债务

式(23)不需要 universal $\Lambda_{\rm all}=0$。其数据本来属于一个明确有限原查询集合。

在所有实际包右方、原右锚之前的一个共同空区间，选三个固定同形同宽、不同中心的实包 $v_1,v_2,v_3$。其真实矩
$$
\nu_\alpha=\mu(v_\alpha)
$$
构成 $\mathbb R^3$ 的一组基，依据是原同宽三中心 Vandermonde；这些是 universal 查询的辅助输入，不是添加到当前研究圆中的控制块。

对任意 $n$，写 $n=\sum_\alpha q_\alpha(n)\nu_\alpha$。R389 原有序 $3+2$ 身份在 $\pi V=0$ 上给
$$
\Lambda_{u_i+t v_\alpha}(V)
=\Lambda_{u_i}(V)
+t^2\mathcal A_{V,u_i}(\nu_\alpha)
+t^5\Lambda_{v_\alpha}(V).
$$
所以准确得到
$$
\boxed{
\mathcal A_{V,u_i}(n)
=\sum_{\alpha=1}^3q_\alpha(n)
\left\{\frac{\Lambda_{u_i+v_\alpha}(V)+
\Lambda_{u_i-v_\alpha}(V)}2-\Lambda_{u_i}(V)\right\}.
}
\tag{25}
$$
没有多一个极化因子 $2$，也没有丢掉右包自然值；后者由 $t=\pm1$ 的五次奇性准确相消。

因此全部 $\omega_i,\mathcal T_{d,i},\mathcal T_{e,i}$ 可由至多
$$
\{\Lambda_{u_i},\ \Lambda_{u_i+v_\alpha},\
 \Lambda_{u_i-v_\alpha}:1\le i\le n,\ 1\le\alpha\le3\}
\tag{26}
$$
这 $7n$ 个**固定实际输入**的自然值线性读出。它们是生成上界，不是独立读出数，也不声称每个给定自然值都有一个共同正成本控制器。

这把实际问题限制在真正需要的有限 totals：无需、也不将“所有紧输入的自然函数同时为零”当作可构造的几何背景。两个既有固定自然查询与(26)一般不同；不能沿用它们的实际 joint 结论支付本集合。

## 8. 公共 cap 表的一个保守完整平移上界

固定一个实际宽度 $w$，在 $x=\xi+wy$ 中看参考输入 $v_{\xi,w}$，把 $\xi$ 作为平移参数。以下估计只用于生成上界，不要求 profile 函数基独立。

由 R56/R73 原分子逐层可取：
| 真实对象 | 关于 $\xi$ 的保守次数 |
| --- | ---: |
| 一阶分子 $V_Y$ | $1$ |
| 二阶 forcing 的 $P,B,T_s,T_{sx}$ | $2$ |
| 二阶恢复的 $\eta_0$ | $3$ |
| 完整 $W=\Phi_{m(s)}(v,v)$ | $4$ |
| 完整二阶分子 $V_Z=(A,zP+B,eA-hW)$ | $5$ |

例如 $\eta_0$ 的 $e_sP_x$ 至多三次；$W_s$ 的 $K_0P$ 至多四次。$A=W_x/2+\eta_0/h$ 至多四次，再乘 $e$ 至多五次。R73 的八矩原式和全部真实 $m(s)$ 初值给同一个界。$s$、$x$ 导数不增加平移参数次数。

于是平方 forcing 的 $P_{ZZ},B_{ZZ},T_{s,ZZ}$ 次数至多十。原 R56(5)中
$$
K_0P_{ZZ},\quad-\lambda(P_{ZZ})_s,\quad
(K_0/z)B_{ZZ},\quad-\gamma(B_{ZZ})_s/h^2
$$
分别至多十二、十一、十一、十次；没有被省略的 $1/z$ 或另选历史。对 cap 上一点取原右积分时，包右方场本来为零，故可在母坐标中把右上限写成固定的 $y=1$。这只改写同一个右锚积分，不截去任何左尾。

因此 $S_{V,v_{\xi,w}}$、它在 cap 上的二阶导数以及(16)的两个积分，对 $\xi$ 均为次数至多十二的多项式：
$$
s_V^\pm(\xi,w)=\sum_{\ell=0}^{12}s_{\pm,\ell}(V;w)\xi^\ell.
\tag{27}
$$
R405 原(23)—(27)已给
$$
L_V^\pm(\xi,w,n)
=\sum_{\ell=0}^{6}\sum_{j=0}^2
c_{\pm,\ell j}(V;w)\xi^\ell n_j.
\tag{28}
$$
这些是同一原成本和同一参考 $u_0$ 的线性系数，不是自由参数。

设实际不同正宽度集合为 $\mathscr W$。全部 cap 数据至多使用
$$
\boxed{(2\cdot13+2\cdot7\cdot3)|\mathscr W|
=68|\mathscr W|}
\tag{29}
$$
个共同生成系数。本稿既不称它为秩，也不称原有限响应模块在其中满射。

真实 suffix 仍按(18)取值。母矩保持 $m(1,0,\nu)$ 时，
$$
\mu(u_i)=w_i^{-3}m(1,\xi_i,\xi_i^2+w_i^2\nu).
\tag{30}
$$
若共同平移整个布局，还必须输运 $n_1\mapsto n_1+dn_0$、
$n_2\mapsto n_2+2dn_1+d^2n_0$。因此(28)沿整个布局的真实共同平移可到次数八；(27)仍至多十二。宽度、实际方差、原顺序和全部复制幅权没有冻结错位。

## 9. signed 全自然核与 actual 有限目标的不同用途

在真正的 signed $\ker(E,\Lambda_{\rm all})$ 上，R389 给
$$
\omega_i=0,\qquad
\mathcal A_{V,u_i}(n)=0\quad\text{对任意 }n.
$$
所以(21)、(24)的全部镜点值都由同一张(27)—(29)表确定。这是原 R399/R401 及其他已证核响应的一个准确共同目标空间；它不要求这个 universal 核中存在某条正的完整实际几何。

[R406](R406-complete-weight-zero-natural-fluxes-and-canonical-joint-obstruction.md) 给出的正字符结论还表明：原正时长、同端口闭 frame、$M=0$ 的 canonical 实际成本不能使 universal $\Lambda_{\rm all}$ 为零。因此本节 signed 化简不是一个等待免费安装的实际背景。该禁止结论不排(23)这些固定有限整包目标同时为零；必须对它们的真实共同像另作证明。

对实际 whole-$E=0$ 几何，应始终使用
$$
\boxed{\text{共同 cap 数据(27)—(28)}\quad+\quad
\text{原有限整包数据(23)，由(25)—(26)读出}.}
\tag{31}
$$
即使一个响应方向处于 $\ker(E,\Lambda_{\rm all})$，它也只能改变(31)的 cap 部分，不能改变既有的整包债务。实际目标的(23)不为零时，单加这些方向无法支付全部 period 端条件。

本稿证明了(15)、全部两通道原式(21)/(24)，以及有限 totals 的准确原查询表达(25)。它没有支付全局平台的仿射值、$k$ 值闭合、R394 的十三行同规范系统或(31)的实际共同像。后续必须在同一固定 profiles、同一原成本中处理这些条件，不能以各自的线性 span 或不同几何上的已付目标拼成一个完整解。
