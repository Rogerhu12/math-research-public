# R350：原双辅助的对角联合身份、六相位碰撞来源及叶深度补域

日期：2026-11-13。**状态：已证明。** R344 的真实挠点论证只需两个辅助坐标**同时**作一次 $\mu _6$ 平均。因此每一条 $L_r-\zeta L_s\in p^N$ 的相位管都准确返回原完整来源 $S$，不必先合并六个相位。本篇识别它们的全部一维差坐标来源：依次为 $\Theta^2,\Theta\Theta_\delta,-\Theta^2C,-\Theta C$。同时给出原五输入收缩下的准确管质量递推，保留 primitive 输入产生的双输出非单位边界，并将 R339 的实际范数三叶深度域及其完整补域写入同一个原中央等式。这里没有把辅助域上的总零传播到它的任意叶子域。

## 1. 固定原对象及记号

沿用 R297、R316、R333、R344 的同一曲线、sigma 和普通测度：
$$
E_b:y^2=x^3+b,\qquad b=17,\qquad
\omega^2+\omega+1=0,\qquad
\delta=1+2\omega,\qquad
\gamma=3+\omega,\quad\bar\gamma=2-\omega .
\tag{1}
$$
$\delta^2=-3$，$N(\gamma)=7$，$dz=dx/(2y)$，且
$$
x=z^{-2}+\cdots,\quad y=-z^{-3}+\cdots,\quad
\sigma=z+\cdots,\quad
\Theta=x\sigma^2,\quad C=y\sigma^3,\quad X=x^3.
$$
写 $\Theta_\delta(z)=\Theta(\delta z)$。原目标完整来源是
$$
\begin{aligned}
\boldsymbol c&=(1,2,\delta,2\delta,\gamma,\bar\gamma)^t,\\
S(z)&=-\frac1{84}\prod_{i=1}^6\sigma(c_i z)\\
&=\sigma^{34}x^2(X+b)(X-8b)
       \left(X^2-\frac{4b}{7}X+\frac{16b^2}{7}\right)
 =z^6+\cdots.
\end{aligned}
\tag{2}
$$
仍取 R344 的真实相交三元组
$$
\boldsymbol r=(1,\omega^2,1,0,0,0)^t,\qquad
\boldsymbol s=(1,0,0,-\omega^2,-\omega,0)^t.
\tag{3}
$$
在六个原 sigma 输入上，
$$
Y=\boldsymbol c^t\boldsymbol X,\qquad
L_r=\delta^{-1}\boldsymbol r^*\boldsymbol X,\qquad
L_s=\delta^{-1}\boldsymbol s^*\boldsymbol X.
\tag{4}
$$
特别
$$
\delta L_r=X_1+\omega X_2+X_3,\qquad
\delta L_s=X_1-\omega X_4-\omega^2X_5.
\tag{5}
$$
$\boldsymbol c^t\boldsymbol r=\boldsymbol c^t\boldsymbol s=0$，
$\boldsymbol r^*\boldsymbol s=1$。第六个原 sigma 不进入两个辅助坐标。

本篇测度结论对每个普通 $p>7$、$p\equiv1\pmod3$ 成立。
固定原 $p$-adic 嵌入和 R316 的单位周期 $\Omega$。记
$$
\nu=\nu_{\sigma,17},\quad
\pi=\psi_{17}(\mathfrak p),\quad
\pi\bar\pi=p,\quad
\varepsilon=\psi_0(\mathfrak p)/\psi_{17}(\mathfrak p),
$$
$$
\kappa=p/\bar\pi^2,\qquad
\lambda=\varepsilon^3/\bar\pi,\qquad
t_p=\lambda\kappa,\qquad
\nu|_{p\mathbf Z_p}=\lambda[\kappa]_*\nu .
\tag{6}
$$
$v_p(t_p)=1$，$\nu$ 整有界，$\nu(\mathbf Z_p)=0$，$\int x\,d\nu=\Omega$。
变换统一用 $\int e^{zx/\Omega}d\nu=\sigma(z)$。
置 $\eta_6=-\nu^{\otimes6}/84$，则 $Y_*\eta_6=\nu_S$。

## 2. 只作同时平均的完整原联合身份

定义原三个复变量的整个函数
$$
\mathcal F(z;v,w)
=-\frac1{84}\prod_i
 \sigma\left(c_i z+\frac{\bar r_i v+\bar s_i w}{\delta}\right),
\tag{7}
$$
以及较弱的同时平均
$$
\mathcal A_\Delta(z;v,w)
=\frac16\sum_{\xi\in\mu_6}\mathcal F(z;\xi v,\xi w).
\tag{8}
$$
这里没有分别对 $v,w$ 平均。令
$$
\psi_\Delta(v,w)=[z^6]\mathcal F(z;v,w).
\tag{9}
$$

**命题。** 有全部权的整个恒等式
$$
\boxed{\mathcal A_\Delta(z;v,w)=S(z)\psi_\Delta(v,w).}
\tag{10}
$$
而且 $\psi_\Delta(\xi v,\xi w)=\psi_\Delta(v,w)$、$\psi_\Delta(0,0)=1$。

**证明。** 下面逐项说明 R344 挠点证明在同时平均下仍然适用。

对等调和 reduced sigma，$z$ 的准周期交叉项分别含
$\sum\bar c_i\bar r_i=\sum\bar c_i\bar s_i=0$。
故 (7)、(8) 对固定 $v,w$ 都是实际 $\mathcal O(34O)$ 截面；
没有留下辅助 Gaussian。又
$$
\mathcal F(\xi z;v,w)=\mathcal F(z;\xi^{-1}v,\xi^{-1}w)
\tag{11}
$$
因为六个 sigma 的总单位相位为 $\xi^6=1$。
因此仅 (8) 就已使 $z$ 的 $\mu_6$ 型平凡。
未移位的第六因子 $\sigma(\bar\gamma z)$ 使原点质量为零。
故
$$
\mathcal A_\Delta\in
 \sigma^{34}x^2\{P(X):\deg P\le4\}.
\tag{12}
$$

为保留其真实挠点零，使用以下原换代表：
$$
\begin{aligned}
\boldsymbol u_\gamma&=(1,\omega^2,\omega^2,\omega,0,-\omega^2),\\
\boldsymbol u_2&=(1,0,-1,0,\omega^2,\omega),\\
\boldsymbol u_6&=(1,2,\delta,0,\omega^2,\omega).
\end{aligned}
\tag{13}
$$
它们分别与 $\boldsymbol c$ 模 $\gamma,2,2\delta$ 同余，次数分别为
$5,4,10$，并且 $\boldsymbol u_6\equiv\boldsymbol u_2\pmod2$。
每一个向量仍同时垂直于 $\boldsymbol r,\boldsymbol s$。

若 $\boldsymbol c-\boldsymbol u=\alpha\boldsymbol d$，$T\in E[\alpha]$，
逐因子原 sigma 准周期给
$$
\mathcal F_{\boldsymbol c}(T;v,w)
=e_{\boldsymbol c,\boldsymbol u}(T)
       \mathcal F_{\boldsymbol u}(T;v,w),
\tag{14}
$$
其中 $e$ 非零，且其两个辅助指数分别含
$\sum d_i r_i=\sum d_i s_i=0$，所以 $e$ 独立于 $v,w$。
这是**平均之前**的身份，当然也与同时平均 (8) 相容。
完整常数就是 R344(12)，没有新的相位选择。

各换代表的第六因子仍未移位且非零；其同时平均仍是 $\mu_6$ 不变、
原点质量零的整个截面。degree 四和五的不变空间分别只有
$\Theta^2$、$\Theta C$，原点质量为 $1,-1$，所以二者的质量零空间都为零。
degree 十的质量零空间恰为 $\mathbf C\,\sigma^{10}x^2$。
由 $\boldsymbol u_6\equiv\boldsymbol u_2\pmod2$，该最后一条线在非零
二挠点也必须为零；但 $\sigma^{10}x^2$ 在这些点非零。
所以三条换代表的同时平均全为零。

由 (14)，原 (8) 保留全部 $E[2]$、$E[2\delta]$、$E[\gamma]$ 零；
未移位第六因子还保留 $E[\bar\gamma]$ 零。
在 (12) 中，这四组零给四个两两不同的角根
$$
-b,\qquad 8b,\qquad \frac{2-6\delta}{7}b,\qquad
                         \frac{2+6\delta}{7}b.
$$
次数至多四的多项式只能是 (2) 中多项式的倍数。
故 $\mathcal A_\Delta=S\psi$。
由 (11)，$[z^6]\mathcal F$ 已对 $(v,w)\mapsto(\xi v,\xi w)$ 不变，
所以 $[z^6]\mathcal A_\Delta=[z^6]\mathcal F=\psi_\Delta$。
又 $s_6=1$，得到 (10) 和全部归一。$\square$

这不是由低阶系数外推整条身份。关键改变是：原挠点证明只用 (11)，
不需要两个辅助各自不变。

## 3. 原二维测度及较强的域返回

在联合输出上只对 $(L_r,L_s)\mapsto(\xi L_r,\xi L_s)$ 平均，
记为 $\mathsf P_\Delta$。设
$$
\mathcal J_\Delta=\mathsf P_\Delta(Y,L_r,L_s)_*\eta_6,
$$
$$
\Xi_\Delta=
 \frac1{6!\Omega^6}(\operatorname{pr}_{L_r,L_s})_*
                          (Y^6\mathcal J_\Delta).
\tag{15}
$$
$6!\Omega^6$ 是单位。因此 $\Xi_\Delta$ 是实际整有界测度。
(10) 和变换单射性给
$$
\boxed{\mathcal J_\Delta=\nu_S\otimes\Xi_\Delta.}
\tag{16}
$$

与 R344 的关系准确为
$$
\boxed{\Xi=\mathsf P_{\mathrm{ind}}\Xi_\Delta,}
\tag{17}
$$
其中 $\mathsf P_{\mathrm{ind}}$ 才是分别旋转两个辅助。
$\Xi_\Delta$ 质量为一，同时 $\mu_6$ 不变；两个边缘仍是
$$
\rho_2=-[\delta^{-1}]_*\nu_C.
\tag{18}
$$
(18) 来自令 (9) 的一个辅助为零，再用 R341 的单辅助身份。
R345 已付 $\rho_2|_p=\lambda_C[\kappa]_*\rho_2$，
$\lambda_C=1/\bar\pi_{1/4}$，以及所有本篇普通素数的
$1-\lambda_C$ 为单位。这里不把边缘身份当作二元独立性。

对任何仅要求**同时** $\mu_6$ 不变的有界连续函数 $h(u,v)$，
(16) 已能在未平均原核上测试：
$$
\boxed{
Y_*\{h(L_r,L_s)\eta_6\}=\Xi_\Delta(h)\nu_S.
}
\tag{19}
$$
因此它保留全部 $Y$ 的单位/非单位域、tame 和任意 Mellin 权。
尤其每一条相位条件 $L_r-\zeta L_s\in p^N$ 都可单独使用。
没有将 R341 的两个不交换原输入投影换序。

## 4. 原五输入核与全部输出 carry

设 $Y_5=\sum_{i=1}^5 c_iX_i$。
第六原输入的六阶以下矩只有第一矩 $\Omega$ 非零，所以从 (15) 得到
$$
\boxed{
\Xi_\Delta=-\frac{\bar\gamma}{84\cdot5!\Omega^5}
       (L_r,L_s)_*(Y_5^5\nu^{\otimes5}).
}
\tag{20}
$$
这里不再需要分别辅助平均，甚至不需另写同时平均：
$\psi_\Delta$ 的同时不变性已证明，故 (20) 本身就同时不变。
所有五个输入仍是原 sigma 测度。

令 $\Xi_\Delta^{\mathrm{prim}}$ 为 (20) 限制至少一个原输入为单位后
保留**整个**二维输出所得的测度。全输入在 $p$ 时原五次权给 $\kappa^5$，
五个 core 给 $\lambda^5$，故
$$
\boxed{
\Xi_\Delta=\Xi_\Delta^{\mathrm{prim}}
             +t_p^5[\kappa,\kappa]_*\Xi_\Delta.
}
\tag{21}
$$
准确的范数收敛展开为
$$
\Xi_\Delta=\sum_{j\ge0}t_p^{5j}[\kappa^j,\kappa^j]_*
                  \Xi_\Delta^{\mathrm{prim}},\qquad
v_p(\text{截到 }j=M\text{ 后的尾})\ge5(M+1).
\tag{22}
$$
这适用于所有有界整的输出测试。
$\Xi_\Delta^{\mathrm{prim}}$ 总质量为 $1-t_p^5$。

primitive 输入可以产生两个同时非单位的辅助输出。
后文把这个边界明确保留；不能由 (21) 给它免费添一个 $p^5$。

## 5. 六条相位差的完整低次来源

对 $\zeta\in\mu_6$ 定义整个函数和实际差坐标测度
$$
D_\zeta(t)=\psi_\Delta(\delta t,-\zeta\delta t),\qquad
\mathfrak d_\zeta=(u-\zeta v)_*\Xi_\Delta.
\tag{23}
$$
则 $[\delta]_*\mathfrak d_\zeta$ 的变换就是 $D_\zeta$。

**六相位来源定理。**
$$
\boxed{
\begin{array}{c|c|c}
\zeta&N_\zeta&D_\zeta\\ \hline
1&4&\Theta^2\\
-1&8&\Theta\Theta_\delta\\
\omega,\omega^2&7&-\Theta^2C\\
-\omega,-\omega^2&5&-\Theta C
\end{array}}
\tag{24}
$$
这些都是原整函数的真实正乘积（带所列常符号），每条质量为一。

**证明。** 令
$$
\boldsymbol d_\zeta=\overline{\boldsymbol r}
                         -\zeta\overline{\boldsymbol s}.
$$
将 (23) 代入 (7)，得到
$$
D_\zeta(t)=[z^6]\left\{-\frac1{84}
                  \prod_i\sigma(c_i z+d_{\zeta,i}t)\right\}.
\tag{25}
$$
由于 $\sum_i\bar d_{\zeta,i}c_i=0$，$t$ 的全部交叉准周期项消失。
故 (25) 是真实 $\mathcal O(N_\zeta O)$ 截面，其中
$$
N_\zeta=\sum_i|d_{\zeta,i}|^2
                      =6-\zeta-\bar\zeta.
\tag{26}
$$
CM sigma division 给出的线丛没有额外二挠 twist：
在 $\mathbf Z[\omega]$ 中，奇度核的点和为零；偶度 CM 核包含全部二挠，
其二初级部分也没有唯一的二阶元素，故点和仍为零。
因此相应 pullback 正是 $\mathcal O(N_\zeta O)$。
提取 $[z^6]$ 不改变此线丛，因为交叉项已准确为零。

由同时不变性，$D_\zeta(\xi t)=D_\zeta(t)$，且 $D_\zeta(0)=1$。
实际不变空间为
$$
\begin{array}{c|c}
N&\sigma^N L(NO)^{\mu_6}\\ \hline
4&\mathbf C\,\Theta^2\\
5&\mathbf C\,\Theta C\\
7&\mathbf C\,\Theta^2C\\
8&\mathbf C\,\Theta^4\oplus\mathbf C\,\sigma^6\Theta .
\end{array}
\tag{27}
$$
这是直接由基 $\sigma^Nx^ay^e$、极阶 $2a+3e\le N$ 和型
$N-2a-3e\equiv0\pmod6$ 得到。
前三行已由质量 $1$ 唯一给出 (24)。

对 $\zeta=-1$，写 $D_{-1}=\Theta^4+a b\sigma^6\Theta$。
原 sigma 的准确首项
$$
\sigma(z)=z+\frac b{210}z^7+\cdots
$$
代入 (25)，有限聚合给
$$
[t^6]D_{-1}=\frac{52}{15}b.
\tag{28}
$$
附录给不含任何无穷截尾的有限整数和。
另一方面 $[t^6]\Theta^4=-8b/15$、$\sigma^6\Theta=t^6+\cdots$，
所以 $a=4$。真实 norm3 division 又给
$$
\sigma(\delta t)=\delta x\sigma^3,\qquad
x(\delta t)=-\frac{X+4b}{3x^2},\qquad
\Theta_\delta=\sigma^6(X+4b).
\tag{29}
$$
故 $\Theta^4+4b\sigma^6\Theta=\Theta\Theta_\delta$，证明最后一行。
整个 (24) 因而由有限维空间及准确归一得到。$\square$

特别，R344 的分别平均差坐标
$\mathfrak d=(u-v)_*\Xi$ 满足
$$
\boxed{
[\delta]_*\mathfrak d
=\frac16\left(\nu_{\Theta^2}+\nu_{\Theta\Theta_\delta}
              -2\nu_{\Theta^2C}-2\nu_{\Theta C}\right).
}
\tag{30}
$$
本篇 (24) 比 (30) 保留了每条原相位，而没有将六条质量相同误写成
它们在原碰撞域上等质量。

## 6. 差坐标的所有尺度与 Mellin 规范

记 $d=p-1$，$\omega_p$ 为普通 Teichmüller 角色，定义
$$
M_{\mu,\ell}(u)=
 \int_{\mathbf Z_p^\times}\omega_p(x)^\ell
                     \langle x\rangle^{du}\,d\mu(x).
$$
(23)、(24) 是完整测度身份，因而
$$
\boxed{
M_{\mathfrak d_\zeta,\ell}(u)
 =\omega_p(\delta)^{-\ell}\langle\delta\rangle^{-du}
                         M_{\nu_{D_\zeta},\ell}(u).
}
\tag{31}
$$
中央导数中的尺度项完整为
$$
M'_{\mathfrak d_\zeta,\ell}(0)
 =\omega_p(\delta)^{-\ell}
 \left(M'_{\nu_{D_\zeta},\ell}(0)
                  -d\log_p(\delta)M_{\nu_{D_\zeta},\ell}(0)\right).
\tag{32}
$$
对深度域 $p^N\mathbf Z_p$，$\delta$ 是单位，所以其质量不变。
这与删除 Mellin 的 $\delta$ 尺度项是两件不同的事。

本篇没有把 (24) 的正乘积作乘法 Mellin，也没有预设
$\Theta C$ 或 $\Theta^2C$ 的新线性 core 标量。
它们的完整测度由原加法卷积定义。

## 7. 每一碰撞相位的准确质量递推

对 $N\ge0$ 记
$$
d_{\zeta,N}
 =\Xi_\Delta\{u-\zeta v\in p^N\mathbf Z_p\}
 =\nu_{D_\zeta}(p^N\mathbf Z_p),\qquad d_{\zeta,0}=1 .
\tag{33}
$$
对 $N\ge a\ge1$，定义真实的双输出非单位边界
$$
\begin{aligned}
e_{\zeta;a,N}
 &=\Xi_\Delta\{u,v\in p^a\mathbf Z_p,\
                          u-\zeta v\in p^N\mathbf Z_p\},\\
e^{\mathrm{prim}}_{\zeta;a,N}
 &=\Xi_\Delta^{\mathrm{prim}}
       \{u,v\in p^a\mathbf Z_p,\
                          u-\zeta v\in p^N\mathbf Z_p\}.
\end{aligned}
\tag{34}
$$
并置 $e_{\zeta;0,N}=d_{\zeta,N}$。
原 (21) 对该域逐项给
$$
\boxed{
e_{\zeta;a,N}
=e^{\mathrm{prim}}_{\zeta;a,N}
                     +t_p^5 e_{\zeta;a-1,N-1}.
}
\tag{35}
$$
因此完整有限递推为
$$
\boxed{
e_{\zeta;a,N}
=\sum_{j=0}^{a-1}t_p^{5j}
          e^{\mathrm{prim}}_{\zeta;a-j,N-j}
                    +t_p^{5a}d_{\zeta,N-a}.
}
\tag{36}
$$
$\kappa/p$ 为单位，故每次把两深度和差深度各减一没有隐藏相位。

实际双方单位相位管为
$$
\mathcal H_{\zeta,N}
=\{u,v\in\mathbf Z_p^\times,\ u-\zeta v\in p^N\mathbf Z_p\},
\qquad N\ge1.
$$
令 $q_{\zeta,N}=\Xi_\Delta(\mathcal H_{\zeta,N})$。
在差坐标属于 $p^N$ 时，两辅助要么都为单位、要么都在 $p$，
所以
$$
\boxed{
q_{\zeta,N}
=d_{\zeta,N}-t_p^5d_{\zeta,N-1}
                   -e^{\mathrm{prim}}_{\zeta;1,N}.
}
\tag{37}
$$
这是每条原相位的完整质量式。
最后一项是原 primitive 输入产生的双方非单位 carry；
它不因名字中出现 $p$ 就可被删掉或赋予五阶额外精度。

六次碰撞管恰为不交并
$$
\{u,v\in\mathbf Z_p^\times,\ v_p(u^6-v^6)\ge N\}
       =\coprod_{\zeta\in\mu_6}\mathcal H_{\zeta,N}.
\tag{38}
$$
因为 $p>7$，六个单位根的差均为单位，分解没有交叠重数。
其总质量是 $\sum_\zeta q_{\zeta,N}$；不假定六个 $q_{\zeta,N}$ 相等。
按 (17)，原分别平均 $\Xi$ 在 (38) 上给同一质量；
它在单个分支上读到的是六条原分支的平均。

## 8. 每条相位管都返回同一完整中央

$\mathcal H_{\zeta,N}$ 对同时单位旋转不变。
由 (19)，对全部 tame 有
$$
\boxed{
J_{\zeta,N;\ell}(u)=q_{\zeta,N}J_{S,\ell}(u),\qquad
J'_{\zeta,N;0}(0)=q_{\zeta,N}J'_S(0).
}
\tag{39}
$$
左侧是在原六输入核上加 $\mathcal H_{\zeta,N}(L_r,L_s)$，
再保留原输出 $Y\in\mathbf Z_p^\times$ 的完整 Mellin。
这不是把 $L_r-\zeta L_s$ 当作原 $Y$；两者测试不同。

(39) 没有另添质量斜率或 $\delta$ 的导数项，因为 $Y$ 没有缩放，
$q_{\zeta,N}$ 是与 $u$ 无关的常标量。
(31)、(32) 处理的是另外的一维差输出，故与此不冲突。

若 $J'_S(0)=0$，每条完整相位管的中央导数确实为零。
以下准确写出 R339 叶域与这些相位管之间仍需处理的补域。

## 9. 在同一个原范数三核中写叶深度域

将原第二个因子作长度 $m$ 的真实 norm3 展开：
$$
\sigma(2z)=\delta^m\sigma(2\delta^{-m}z)
                \prod_{h=1}^m\Theta(2\delta^{-h}z).
\tag{40}
$$
每一个 $\Theta$ 使用同一个原 sigma 的二输入身份
$$
\nu_\Theta=-\frac1{2\Omega^2}(A+B)_*
                           ((A-B)^2\nu\otimes\nu).
\tag{41}
$$
在原叶变量
$$
X_1,X_3,X_4,X_5,X_6,\ Z,\ (A_h,B_h)_{1\le h\le m}
$$
上，完整核为
$$
d\mathscr M_m
=-\frac{\delta^m}{84}
 \prod_{h=1}^m\left(-\frac{(A_h-B_h)^2}{2\Omega^2}\right)
       d\nu(X_1)d\nu(X_3)\cdots d\nu(X_6)d\nu(Z)
       \prod_hd\nu(A_h)d\nu(B_h).
\tag{42}
$$
定义第二个原因子的真实 root 输入
$$
U_0=\delta^{-m}Z+
           \sum_{h=1}^m\delta^{-h}(A_h+B_h).
\tag{43}
$$
则 (42) 经
$$
Y=X_1+2U_0+\delta X_3+2\delta X_4+\gamma X_5+\bar\gamma X_6
$$
的 pushforward 仍准确是原 $\nu_S$。
原两个辅助也必须使用
$$
\delta L_r=X_1+\omega U_0+X_3,\qquad
\delta L_s=X_1-\omega X_4-\omega^2X_5.
\tag{44}
$$
因此 (19)、(39) 对这一**完整**展开后的核仍成立。
原因是 (40)、(41) 先给全部 root 测度身份；
没有对其叶域作未经证明的逐项分解。

令除 $X_1$ 外的 $5+2m$ 个叶变量按任意固定顺序记为 $V_j$。
R339 的独立深度域具有形式
$$
\mathcal D_{\boldsymbol n}
=\{X_1\in\mathbf Z_p^\times,\quad
                          V_j\in p^{n_j}\mathbf Z_p\ (\forall j)\}.
\tag{45}
$$
若所有 $n_j\ge N\ge1$，(43) 给 $U_0\in p^N$，从而
$$
\boxed{
\mathcal D_{\boldsymbol n}
 \subset \mathcal H_{1,N}(L_r,L_s),\qquad
Y\in\mathbf Z_p^\times\ \text{在 }\mathcal D_{\boldsymbol n}\text{ 上恒成立}.
}
\tag{46}
$$
这是固定的 $\zeta=1$ 分支，不能用分别平均后的任意单分支代替；
本篇 (10)、(19) 恰好支付了它。

## 10. 真实补域的全部分块及中央等式

在 (42) 的同一叶空间中，写
$\mathcal H=\mathcal H_{1,N}(L_r,L_s)$。
因为 (46)，其补域可作以下准确不交分解：
$$
\mathcal H\setminus\mathcal D_{\boldsymbol n}
=\mathcal E_0\ \coprod\ \coprod_j\mathcal E_j,
\tag{47}
$$
其中
$$
\begin{aligned}
\mathcal E_0&=\mathcal H\cap\{X_1\in p\mathbf Z_p\},\\
\mathcal E_j&=\mathcal H\cap\{X_1\in\mathbf Z_p^\times,\
 V_i\in p^{n_i}\ (i<j),\ V_j\notin p^{n_j}\}.
\end{aligned}
\tag{48}
$$
后面的叶变量在 $\mathcal E_j$ 中没有额外限制。
每条输出测试仍保留 $Y$ 的单位指标，不能因 $\mathcal D_{\boldsymbol n}$
上的输出自动为单位，就删除补域上的该指标。

令
$$
\mathcal L_p(\mathcal E)
=(p-1)\int_{\mathcal E}
        \mathbf1_{\{Y\in\mathbf Z_p^\times\}}
                    \log_p\langle Y\rangle\,d\mathscr M_m .
$$
由完整 (39)、(47)，得到同一个原中央上的恒等式
$$
\boxed{
\mathcal L_p(\mathcal D_{\boldsymbol n})
+\mathcal L_p(\mathcal E_0)+\sum_j\mathcal L_p(\mathcal E_j)
                           =q_{1,N}J'_S(0).
}
\tag{49}
$$
这里每项都是原同一带二次权叶核的真实积分，全部输入相位和输出 carry
均在 (42)–(48) 中明确。没有把任何一项改为一个无权环境测度。

补域确实不是空的几何集合。原六输入中取
$$
(X_1,X_2,X_3,X_4,X_5,X_6)=(1,0,0,0,0,-1)
$$
便有 $L_r=L_s=1/\delta$，而 $Y=1-\bar\gamma=\omega-1$，
其范数为三，故对本篇所有普通素数都为单位。
该点在所有 $\mathcal H_{1,N}$ 中，却不在要求 $X_6$ 深的叶域中。
在实际展开 (42) 中，也可取 $Z=X_3=X_4=X_5=0$、
$A_h=p^N,B_h=2p^N$、$X_1=1,X_6=-1$。
所有二次权 $(A_h-B_h)^2$ 非零，(43)、(44) 仍给相同相位管和单位输出，
但仍违反 $X_6$ 的深度要求。这仅说明完整补域及其核不能几何删除；
不由非空性推断有符号测度质量非零。

R339 证明：对每个普通 $p$ 和任意最低深度，可以选实际长度和深度使
$\mathcal L_p(\mathcal D_{\boldsymbol n})\ne0$。
如果同时假设 $J'_S(0)=0$，(49) 的准确后果是
$$
\mathcal L_p(\mathcal E_0)+\sum_j\mathcal L_p(\mathcal E_j)
                       =-\mathcal L_p(\mathcal D_{\boldsymbol n})\ne0.
\tag{50}
$$
当前没有把这些补域逐一化成 (19) 中的辅助函数，因此 (50) 是必须继续控制的
实际补偿，不能当作矛盾。原固定曲线与无穷素数的完成标准没有改变。

## 11. 有限系数的精确证书

(28) 只需一次 sigma 的七次项，没有未估计的尾。
令 $L_i(z,t)=c_i z+d_{\zeta,i}t$。由于总次数为十二，
$$
[t^6]D_\zeta
=-\frac b{84\cdot210}
 [z^6t^6]\sum_{i=1}^6 L_i(z,t)^7\prod_{j\ne i}L_j(z,t).
\tag{51}
$$
全部 $c_i,d_{\zeta,i}$ 都是 $\mathbf Z[\omega]$ 中的整数。
六个准确整数和为
$$
\begin{array}{c|r|c}
\zeta&
[z^6t^6]\sum_iL_i^7\prod_{j\ne i}L_j&
[t^6]D_\zeta/b\\ \hline
1&4704&-4/15\\
-1&-61152&52/15\\
\omega,\omega^2&-588&1/30\\
-\omega,-\omega^2&-2940&1/6
\end{array}
\tag{52}
$$
这些数可仅按
$(a+b\omega)(c+d\omega)=(ac-bd)+(ad+bc-bd)\omega$
和有限二项式展开复算；计算没有目标素数样本。
例如 $\zeta=-1$ 时
$$
\boldsymbol d_{-1}=(2,\omega,1,-\omega,-\omega^2,0).
$$
(51) 中六项的 $\mathbf Z[\omega]$ 系数依次是
$$
-35308+700\omega,\quad -7672+1288\omega,\quad
-1470+882\omega,\quad -25032-18648\omega,\quad
8330+15778\omega,\quad 0.
$$
它们的和恰为 $-61152$。这给 (28) 的完整有限证书。
除 degree 八的一次归一外，(24) 的其余整条身份仅由质量和一维空间决定；
(10) 则由真实挠点零证明，与此有限系数计算逻辑独立。

## 12. 已支付内容与继续接口

本篇新增的是：

1. 原重叠双辅助的**同时**单位平均已足以分离原 $Y$ 与整个辅助对；
   因而单个相位域也有完整中央返回。
2. 六相位差坐标准确落到 (24) 的四条原低次来源，保留所有真实尺度。
3. 碰撞管质量满足 (35)–(37)，primitive 输入的双方非单位边界明确保留。
4. R339 独立叶深度域、实际二次权及完整补域在同一个原中央式 (49) 中聚合。

下一步必须支付 (49) 的实际补域控制，或者证明这些域与更多真实联合身份
具有所需相容性。仅比较 (24) 的质量、只使用边缘 core，或以 R339 的某个叶域非零
代替原总和非零，都不足以完成课题。

### 引用

- [R297：实际原来源及 CM7 因式](R297-jzero-actual-cm13-mass-kernel-cm7-product-and-angular-source.md)。
- [R316：原低次数测度及全部 core](R316-jzero-low-degree-original-cores-and-complete-four-factor-carry.md)。
- [R333：六个原 sigma 输入](R333-six-original-sigma-inputs-and-two-quadratic-negative-moment-return.md)。
- [R339：同一原来源的非零叶深度族](R339-original-normthree-depth-family-and-a-unit-negative-moment-coefficient.md)。
- [R340：真实范数三联合测度](R340-original-ternary-fourier-joint-measure-and-collision-domains.md)。
- [R341：原混合坐标与三次来源](R341-original-active-triple-joints-degree-three-core-and-overlap-source.md)。
- [R344：完整双辅助挠点因子化](R344-overlapping-original-pair-full-torsion-factorization-and-contracting-kernel.md)。
- [R345：原三次来源的绝对 core 相位](R345-original-degree-three-absolute-core-phase-and-middle-cartier-row.md)。
