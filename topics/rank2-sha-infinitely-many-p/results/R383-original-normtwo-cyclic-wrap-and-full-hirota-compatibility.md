# R383：原 norm-two 的同核逐球式、完整循环行与全部普通素数的单位约束

日期：2026-11-14。**状态：以下真实 norm-two 逐球／卷积比较、全部循环项、对每个普通 $p>7$ 为单位的双线性行、与 R378 norm-three 的同一循环代数相容式，以及原 Hirota/Wronskian 的完整有限转置均已证明。原指定两个固定负矩联合非零尚未证明；本文保留全部中间项和临界质量，不把这些单位和替代指定两端。主目标未完成。**

## 1. 沿用的原对象与三种准确标签

固定
$$
E_b:y^2=x^3+b,\quad b=17,\quad
D=d/dz,\quad x=z^{-2}+\cdots,\quad y=-z^{-3}+\cdots,
$$
$$
\sigma=z+\cdots,\qquad \Theta=x\sigma^2,\qquad C=y\sigma^3.
\tag{1}
$$
仍取原普通 $p=6s+1>7$、周期 $\Omega$、真实 Frobenius
$\pi=\psi_b(\mathfrak p)$、$\pi\bar\pi=p$，
$$
H=\bar\pi\bmod p,\quad V=[\bar\pi]\bmod p,\quad
f=P(x^3),\quad \deg P=s,\quad \Omega^{p-1}=H^{-1}.
\tag{2}
$$
以下有限域等式均在同一个原整模型和剩余域中成立。

原完整 core 是
$$
\nu_G|_p=\lambda_G[\kappa]_*\nu_G,\qquad
\kappa=p/\bar\pi^2,\qquad G=\sigma,\Theta,C.
\tag{3}
$$
R345 已给绝对规范
$$
\boxed{\lambda_C=1/\bar\pi^\circ,\qquad
\pi^\circ=\psi_{1/4}(\mathfrak p),\qquad
\pi^\circ\equiv1\pmod{3\mathcal O_K}.}
\tag{4}
$$
这里 $\psi_{1/4}$ 属于固定曲线 $E_{1/4}:y^2=x^3+1/4$；
不是从一个 projective 三挠表示猜出的单位。

R378 的真实 AS 标签是
$$
c(q)=-\frac{\Omega}{H}\frac{D^2f(q)}{2Df(q)}
\quad(q\in\ker V\setminus\{0\}),\qquad c(0)=0.
\tag{5}
$$
它给 $\ker V\simeq\mathbf F_p$ 的加法同构。同一个 $q_c$ 在
$\sigma,\Theta,C$ 三个原 degree 中的标签分别是 $c,2c,3c$。

记
$$
s_c=\nu_\sigma(c+p)\bmod p,\quad
t_c=\nu_\Theta(c+p)\bmod p,\quad
u_c=\nu_C(c+p)\bmod p.
$$
沿用
$$
a_c=s_c/\lambda_\sigma,\qquad
b_c=t_{2c}/\lambda_\Theta,\qquad
h_c=u_{3c}/\lambda_C.
\tag{6}
$$
R376、R378 已完整支付
$$
(a_c,b_c,h_c)=
\left(\frac1{Df(q_c)},
\frac{x(q_c)^p}{Df(q_c)^2},
\frac{y(q_c)^p}{Df(q_c)^3}\right)\quad(c\ne0),
$$
$$
(a_0,b_0,h_0)=(0,1,-1).
\tag{7}
$$
因此 $a_c,b_c,h_c$ 在非零 $c$ 均非零；
$x,y$ 的零点分别为非零三挠点、二挠点，不能是非零 $p$ 核点。
所有 core、division 首项、原 theta lift 和 vertical factor
均保持 (3)–(7) 的规范。

## 2. 真正的二倍点核方程及其导数

本篇使用的原 sigma 二倍点式是
$$
\boxed{\sigma(2z)=-2y(z)\sigma(z)^4.}
\tag{8}
$$
负号由 $y=-z^{-3}+\cdots$、$\sigma=z+\cdots$ 确定，
不能换成无符号的标准除法多项式商。

将 (8) 与原
$\sigma(\bar\pi z)=\bar\pi\sigma(z)^p f_{\bar\pi}(z)$
按两种次序复合再约化，因 $(-2)^p=-2$，得到
$$
f(2P_0)=H^3\,\frac{y(VP_0)}{y(P_0)^p}\,f(P_0)^4.
\tag{9}
$$
R336 给
$$
H^2x(VP_0)=\frac{(Df)^2-fD^2f}{f^2}.
$$
对其求导并用 $V^*dz=Hdz$，准确有
$$
H^3y(VP_0)
=\frac{3f(Df)(D^2f)-2(Df)^3-f^2D^3f}{2f^3}.
\tag{10}
$$
因此整个真实有理核方程是
$$
\boxed{
f(2P_0)=\frac{f(P_0)}{2y(P_0)^p}
\left(3f(Df)(D^2f)-2(Df)^3-f^2D^3f\right).
}
\tag{11}
$$

在非零简单核点 $q$ 求导。只有括号中 $-2(Df)^3$ 的项留下，
左边的链式法则仍有二：
$$
\boxed{2Df(2q)=-\frac{Df(q)^4}{y(q)^p}.}
\tag{12}
$$
整数二在真实 étale 标签上作用为 $c\mapsto2c$；
这里 $\bar 2=2$，与 norm-three 的 $\delta\mapsto\bar\delta$
方向没有冲突。于是 (7)、(12) 给
$$
\boxed{a_{2c}=-2a_ch_c\qquad(c\in\mathbf F_p).}
\tag{13}
$$
$c=0$ 的两边也均为零。

## 3. 保留 2c、3c、4c 的原卷积比较

(8) 的同一测度身份是
$$
[2]_*\nu_\sigma=-2(\nu_\sigma*\nu_C).
\tag{14}
$$
有限剩余类上即
$$
s_{c/2}=-2(s*u)(c).
$$
而 (13) 按 (6) 写成
$$
s_{2c}=-\frac2{\lambda_C}s_cu_{3c}.
$$
所以准确的逐球乘法／加法卷积比较为
$$
\boxed{(s*u)(4c)=\lambda_C^{-1}s_cu_{3c}.}
\tag{15}
$$
这是同一原测度的身份：$4c$ 是真正的范数四输出，
$3c$ 是 degree-three 原标签，不是可以略去的单位缩放。

## 4. 全部循环项与一条新的单位和

与 R378 相同，置
$$
S_i=\int_{\mathbf Z_p^\times}x^{6i+1}\,d\nu_\sigma(x),
\qquad
U_j=\int_{\mathbf Z_p^\times}x^{6j}\,d\nu_C(x),
\qquad 0\le i,j<s,
\tag{16}
$$
以下等式表示模 $p$ 约化。实际零球质量给
$$
\boxed{S_0=\Omega,\qquad U_0=\lambda_C-1.}
\tag{17}
$$
第二式来自原全质量 $C(0)=-1$ 与零球质量 $-\lambda_C$，
不能改成 $-1$ 或 $1-\lambda_C$。

对 $c\ne0$，真实乘法 Fourier 反演是
$$
s_c=-\sum_iS_ic^{-(6i+1)},\qquad
u_{3c}=-\sum_j3^{-6j}U_jc^{-6j}.
$$
对 (15) 乘 $c^{6k+1}$ 后求和，再用 (14)，得到
$$
\boxed{
\sum_{\substack{0\le i,j<s\\i+j\equiv k\pmod s}}
3^{-6j}S_iU_j
=\frac{\lambda_C}{4}\,64^{-k}S_k,
\qquad 0\le k<s.
}
\tag{18}
$$
为逐项核符号，原卷积的 $r$ 阶矩是
$-2^{r-1}M_r(\sigma)$；
将 $4c$ 换元给
$\sum c^rs_cu_{3c}=-\lambda_C2^{-r-1}M_r(\sigma)$。
有限 Fourier 求和再给一个负号，正好是 (18) 的正右边。

$k=0$ 时，保留 (17) 后得到
$$
\boxed{
\sum_{j=1}^{s-1}3^{-6j}S_{s-j}U_j
=\left(1-\frac{3\lambda_C}{4}\right)\Omega.
}
\tag{19}
$$
以下证明其右端对全部当前普通素数为单位。

## 5. 所有普通 p>7 的单位性：准确的 norm19 排除

令
$$
a^\circ_p=\pi^\circ+\bar\pi^\circ\in\mathbf Z.
$$
若 (19) 的括号为零模 $p$，由 (4) 和
$\pi^\circ=0\bmod\mathfrak p$，得到
$$
4a^\circ_p-3=kp\qquad(k\in\mathbf Z).
\tag{20}
$$
左边为奇数，故 $k$ 为奇数。Hasse 界及 $p\ge13$ 给
$$
|4a^\circ_p-3|\le8\sqrt p+3<3p.
$$
所以 $k=\pm1$。又 $\pi^\circ\equiv1\bmod3$ 给
$a^\circ_p\equiv2\bmod3$，而 $p\equiv1\bmod3$。
(20) 遂迫 $k\equiv2\bmod3$，即
$$
k=-1,\qquad p=3-4a^\circ_p.
\tag{21}
$$

令 $\beta=\pi^\circ+4$。由 (21)，
$$
N\beta=p+4a^\circ_p+16=19,\qquad
\beta\equiv2\pmod{3\mathcal O_K}.
\tag{22}
$$
写 $\beta=2+3\gamma$，置
$$
t=\operatorname{Tr}\gamma\in\mathbf Z,\qquad
n=N\gamma\in\mathbf Z_{\ge0}.
$$
(22) 等价于
$$
2t+3n=5.
\tag{23}
$$
虚二次范数不等式 $4n\ge t^2$ 给
$3t^2+8t-20\le0$，所以 $-4\le t\le1$。
(23) 又给 $t\equiv1\bmod3$，只剩
$$
(t,n)=(-2,3)\quad\text{或}\quad(1,1).
$$
第一对不存在于 $\mathcal O_K$：
在 $K=\mathbf Q(\sqrt{-3})$ 中，
$t^2-4n=-3v^2$，其中 $v\in\mathbf Z$；
此处判别式为 $-8$，不是这种形式。
第二对使 $\gamma$ 为 $X^2-X+1$ 的根，即 $-\omega$ 或 $-\omega^2$。
因此
$$
\operatorname{Tr}\beta=4+3t=7,\qquad
N\pi^\circ=N(\beta-4)=19-4\cdot7+16=7,
$$
与 $p>7$ 矛盾。这证明
$$
\boxed{1-3\lambda_C/4\in\mathcal O_p^\times
       \quad\text{对每个普通 }p>7.}
\tag{24}
$$
这里不是从有限素数样本判断单位，也没有把原 $\pi^\circ$ 的
primary 条件改成任意范数 $p$ 的生成元。

由 (19)、(24)，对每个当前 $p$ 存在 $1\le j\le s-1$ 使
$$
\boxed{
\int_{\mathbf Z_p^\times}x^{1-6j}\,d\nu_\sigma,\qquad
\int_{\mathbf Z_p^\times}x^{-6(s-j)}\,d\nu_C
\quad\text{同时为单位。}
}
\tag{25}
$$
权仍随 $p$ 变化，不能从增长的范围推出固定权的无穷结论。

## 6. 与原固定负矩同位置的两条完整行

记
$$
I_\sigma=\int_{\mathbf Z_p^\times}x^{-5}\,d\nu_\sigma,\qquad
I_C=\int_{\mathbf Z_p^\times}x^{-6}\,d\nu_C.
$$
它们模 $p$ 是 $S_{s-1},U_{s-1}$。原首系数
$$
C=-1-\frac{3b}{10}z^6+\cdots
$$
给
$$
S_1=24b\Omega^7,\qquad U_1=-216b\Omega^6.
\tag{26}
$$
故 $s\ge3$ 时，(19) 的两个端点准确是
$$
\boxed{
-\frac8{27}b\Omega^6I_\sigma
+17496b\Omega^7I_C
+\sum_{j=2}^{s-2}3^{-6j}S_{s-j}U_j
=\left(1-\frac{3\lambda_C}{4}\right)\Omega.
}
\tag{27}
$$
$s=2$ 只有一个端点项，不重复计数。

再取 (18) 的最后一行，保留 $U_0$，得
$$
\boxed{
729\Omega I_C+
\sum_{j=1}^{s-2}3^{-6j}S_{s-1-j}U_j
=(15\lambda_C+1)I_\sigma.
}
\tag{28}
$$
$3^{-6(s-1)}=729$、$64^{-(s-1)}=64$ 准确给这些系数。
本篇没有将 $I_C$ 与 R378 的 $I_\Theta$ 相认。

## 7. 同一循环代数中的 norm-two／norm-three 相容

置
$$
\mathscr S(W)=\sum S_iW^i,\quad
\mathscr T(W)=\sum T_iW^i,\quad
\mathscr U(W)=\sum U_iW^i
$$
于同一个 $k[W]/(W^s-1)$。令
$$
A=-1/27,\qquad B=1/64,\qquad A^2=3^{-6}.
$$
R378 和 (18) 是
$$
\boxed{
\begin{aligned}
\mathscr S(W)\mathscr T(BW)
  &=-\frac{\lambda_\Theta}{3}\mathscr S(AW),\\
\mathscr S(W)\mathscr U(A^2W)
  &=\frac{\lambda_C}{4}\mathscr S(BW).
\end{aligned}}
\tag{29}
$$
这些等式保留整个 $W^s-1$ 的 wrap，不以无截断的幂级数等式代替。

这里 $\mathscr S$ 确为这个有限代数的单位，可以合法消去。
证明是 R376 的原逐球单位性：
对 $c\in\mathbf F_p^\times$，Fourier 反演给
$$
\mathscr S(c^{-6})=-c\,s_c\ne0.
$$
$c^{-6}$ 跑遍 $W^s=1$ 的所有根，且这些根互异。
这没有声称 $\mathscr S$ 的任一个指定系数非零。

对 (29) 按 $A,B$ 两种次序复合，取消同一单位 $\mathscr S(W)$，
得到真实混合 norm-six 相容式
$$
\boxed{
\mathscr T(BW)\mathscr U(A^3W)
=\mathscr U(A^2W)\mathscr T(B^2W).
}
\tag{30}
$$
全部常数 $\lambda_\Theta,\lambda_C$ 在两条相同路径中才相消；
没有从相同 core 擅自认同两个测度。

## 8. 原 Hirota／Wronskian 的完整有限接口

令 $\mathcal N$ 作用在有限剩余类函数上为
$$
(\mathcal Nv)_c=c\,v_c.
$$
它是加法卷积的导子，且 $\mathcal N^p=\mathcal N$。
原 $D=d/dz$ 在同一测度上是 $\Omega^{-1}\mathcal N$。
因此以下都是整个有限加法群上的准确等式：
$$
\boxed{
t=\Omega^{-2}\bigl((\mathcal Ns)*(\mathcal Ns)
                         -s*(\mathcal N^2s)\bigr),
}
\tag{31}
$$
$$
\boxed{
u=-\frac1{2\Omega^3}
\bigl(s*s*(\mathcal N^3s)
 -3s*(\mathcal Ns)*(\mathcal N^2s)
 +2(\mathcal Ns)*(\mathcal Ns)*(\mathcal Ns)\bigr).
}
\tag{32}
$$
它们分别来自
$\Theta=\sigma'^2-\sigma\sigma''$ 和
$$
C=-\tfrac12(\sigma^2\sigma'''-3\sigma\sigma'\sigma''
                                    +2\sigma'^3).
$$
另有同一来源的一阶关系
$$
\sigma\Theta'-2\sigma'\Theta=2C,\qquad
\sigma C'-3\sigma'C=3\Theta^2,
$$
故
$$
\boxed{
s*(\mathcal Nt)-2(\mathcal Ns)*t=2\Omega u,\qquad
s*(\mathcal Nu)-3(\mathcal Ns)*u=3\Omega(t*t).
}
\tag{33}
$$
这些式子包括零剩余类，不能先把所有输入限制成单位。

为明确临界项没有消失，可在 (32) 读 $p-1$ 阶矩。
定义内项
$$
\mathcal W=
\frac1{2\Omega^3}
\sum_{\substack{i+j+\ell=s\\0\le i,j,\ell<s}}
\frac{(p-1)!S_iS_jS_\ell}
{(6i+1)!(6j+1)!(6\ell+1)!}\,\mathcal B_{i,j,\ell},
$$
$$
\mathcal B_{i,j,\ell}=
(6\ell+1)(6\ell)(6\ell-1)
-3(6j+1)(6\ell+1)(6\ell)
+2(6i+1)(6j+1)(6\ell+1).
\tag{34}
$$
这里全部阶乘分母小于 $p$，因而为单位。
这只是 $i,j,\ell<s$ 的内项；不能把尚余的临界位置默默删去。

临界位置恰有一个 sigma 矩指数等于 $p$，其真实有限值是
$M_p(\sigma)=M_1(\sigma)=\Omega$。
在 (32) 括号的三个来源中，这些位置的贡献依次为
$$
2\Omega^3,\qquad3\Omega^3,\qquad6\Omega^3.
$$
第一项来自 $(1,1,p-3)$ 的多项式系数
$(p-1)(p-2)=2$；
第二项来自 $(1,0,p-2)$ 的系数 $-1$ 再乘 $-3$；
第三项有三个 $(p-1,0,0)$ 位置，再乘二。
因此原临界全式是
$$
M_{p-1}(C)=-\mathcal W-\frac{11}{2}.
$$
另一方面 $M_{p-1}(C)=U_0=\lambda_C-1$，而不是原全质量 $-1$。
准确相减给
$$
\boxed{\mathcal W=-\lambda_C-\frac92.}
\tag{35}
$$
这与 R349 的临界常数 $9/2$ 一致。若再改用其 Faber Laurent 坐标，
仍须保留该文的 $pt_0=-H$ 和 $y^p$ 修正；
(32)–(35) 是从原有限测度计算这些 carry 的接口，不是免除它们的理由。

## 9. 后续需要真正消去的项

(19)、R378 的单位双线性行，以及 (30)–(35)
如今在同一原核、同一原周期和同一个有限卷积代数中联立。
但 (27)–(28) 含有 $I_C$ 与全部中项，
R378 的对应式含 $I_\Theta$ 与其全部中项。
这里没有证明 $I_\sigma=I_\Theta=0$ 会迫这些中项或 $I_C$ 为零。

剩余的具体任务是把这组完整循环式和原 Hirota 关系真正消元，
或给出能控制指定两条 Faber 观察的其它算术输入。
任一单独单位和、整个循环多项式的可逆性、某个随 $p$ 变化的单位负矩，
都不被本篇计为固定两负矩或原中央导数的非零结论。

## 仓库输入

- [R316](R316-jzero-low-degree-original-cores-and-complete-four-factor-carry.md)：原 sigma/Theta、同一周期及完整 core。
- [R336](R336-ordinary-original-zeta-as-verschiebung-and-two-full-negative-rows.md)：真实可分 $p$ 同源、核多项式及原对数导数。
- [R345](R345-original-degree-three-absolute-core-phase-and-middle-cartier-row.md)：$\lambda_C$ 的真实曲线身份、primary 条件和绝对相位。
- [R349](R349-critical-faber-cubic-row-and-complete-norm-three-projections.md)：完整临界 Faber carry。
- [R376](R376-original-additive-ball-theta-group-formula-and-integral-torsion-values.md)：原整逐球公式与 sigma 非零球单位。
- [R378](R378-original-etale-ball-normthree-and-unit-bilinear-wrap.md)：AS 原标签、norm-three 共轭方向及整个原循环行。
