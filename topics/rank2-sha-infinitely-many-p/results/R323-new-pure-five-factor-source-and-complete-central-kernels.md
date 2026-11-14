# R323：新的纯三线五因子来源与完整原中央核

日期：2026-11-13。**状态：以下三条实际 exact companion 的低因子乘法身份、新的纯 plus 三线来源、全部五输入 $p$-core、相加 carry 的三阶返回，以及连接项的无逆参考乘积表达和原中央返回均已证明。本文保留完整中央导数；第一矩的单位性没有被替换成目标中央非零。**

固定 $E_b:y^2=x^3+b$、$b=17$，始终取原 $dz=dx/(2y)$、$y=-z^{-3}+\cdots$、$\sigma=z+\cdots$。写
$$
X=x^3,\quad d_0=X-8b,\quad
\Theta=x\sigma^2,\quad U=\Theta(z)\Theta(2z)^4.
\tag{1}
$$
本篇的 $C_A^U,C_X^U,C_Y^U$ 都带上标 $U$。R311 原来的纯三线 companion 仍单独记为 $C_X^{\rm old}$。

## 1. 三条真实有理 primitive 及新的乘积

沿 R320 的真实迹特征行，置
$$
\begin{aligned}
E_A&=X^{-1}+(4b)^{-1},\\
E_X&=1+60b/d_0+432b^2/d_0^2,\\
E_Y&=1+228b/d_0+4320b^2/d_0^2+20736b^3/d_0^3.
\end{aligned}
$$
原曲线微分直接给
$$
\boxed{\begin{aligned}
P_A&=-\frac{y}{4bx^2},&
P_A'&=E_A,\\
P_X&=-\frac{yx}{d_0},&
P_X'&=E_X,\\
P_Y&=-\frac{yx(X+16b)}{d_0^2},&
P_Y'&=E_Y.
\end{aligned}}
\tag{2}
$$
因此 $C_i^U=UP_i$ 是同一个原 degree-$34$ 线丛的全纯 odd 来源，准确为
$$
\boxed{\begin{aligned}
C_A^U&=-\frac1{4b}\sigma^{34}yX d_0^4,\\
C_X^U&=-\sigma^{34}yX^2d_0^3,\\
C_Y^U&=-\sigma^{34}yX^2(X+16b)d_0^2.
\end{aligned}}
\tag{3}
$$
原点首项分别为 $z/(4b),z,z$。它们在 $U$ 零点处的阶数由 (3) 直接支付，不能仅因有理 primitive 存在就略掉这一点。

取 $\omega^2+\omega+1=0$、$\delta=\sqrt{-3}=1+2\omega$。R319 的原 CM 三同源与原倍点 sigma 式给
$$
\begin{aligned}
\sigma(2z)&=-2y\sigma^4,\\
\Theta(2z)&=x(X-8b)\sigma^8,\\
\Theta(\delta z)&=(X+4b)\sigma^6
                 =\Theta(z)^3+4b\sigma(z)^6.
\end{aligned}
\tag{4}
$$
$1-\omega=\omega^2\delta$，而 $\Theta(\omega^2z)=\Theta(z)$，故改用 $1-\omega$ 时 (4) 的 $\Theta$ 来源准确相同。

(3)–(4) 现在给实际乘法身份
$$
\boxed{
C_X^U=\frac12\sigma(2z)\Theta(z)^3\Theta(2z)^3,}
\tag{5}
$$
$$
C_A^U=\frac1{8b}\sigma(2z)\Theta(2z)^3
       \{\Theta(\delta z)-12b\sigma(z)^6\}.
\tag{6}
$$
最有用的固定组合是
$$
\boxed{\begin{aligned}
V&:=C_X^U-\frac{4b}{3}C_A^U\\
 &=\frac13\sigma(2z)\Theta(2z)^3\Theta(\delta z)\\
 &=-\frac23\sigma^{34}yX(X+4b)(X-8b)^3.
\end{aligned}}
\tag{7}
$$
它的首项为 $2z/3$，五个低次因子的 theta 次数为 $4+3\cdot8+6=34$。所有零来自固定六挠点。式 (7) 没有未付的 Gaussian 或 sigma 符号。

## 2. 与原六条 CM 来源的精确比较

沿 R311 的真实原来源 $Y_j$，取
$$
I_+=\{5,11,17\},\qquad I_-=\{1,7,13\},
\qquad T_j^3-3T_j-1=0.
$$
每条 $Y_j$ 仍按首项 $z$ 归一。其真实多项式 $P_\pm(X,T)$ 已由原 Schwartz 和 CM13 的完整纤维支付；在每组内，$T_j$ 取同一实三次域的全部三个嵌入。

三条 (3) 的完整系数如下：

| 来源 | $j\in I_+$ 的系数 | $j\in I_-$ 的系数 |
|---|---:|---:|
| $C_A^U$ | $(T_j^2-T_j-5)/(36b)$ | $(T_j+1)^2/(18b)$ |
| $C_X^U$ | $-(T_j^2-T_j-5)/27$ | $2(T_j+1)^2/27$ |
| $C_Y^U$ | $-(3T_j^2+5T_j-27)/81$ | $2(T_j+1)^2/81$ |

证明是将这些系数乘 R311 的实际 $P_\pm$ 后作三次域迹，逐个 $X$ 系数比较。一般 $b$ 的多项式系数按 $b^{5-k}X^k$ 缩放；$C_A^U$ 再保留表中的 $1/b$。因此没有把 $b=1$ 的计算当作原 $b=17$ 的相同质量。

表中 minus 三条在 (7) 准确相消，得到
$$
\boxed{
V=\sum_{j\in I_+}v_jY_j,\qquad
v_j=-\frac2{27}(T_j^2-T_j-5).}
\tag{8}
$$
$T^2-T-5$ 与 $T^3-3T-1$ 互素，所以三个 $v_j$ 都非零。
又 $\operatorname{Tr}(T)=0$、$\operatorname{Tr}(T^2)=6$，故
$$
\sum_{j\in I_+}v_j=\frac23,
\tag{9}
$$
与 (7) 的原点首项完全一致。

R311 原纯来源的 plus 系数是
$-(T_j^2+T_j-8)/(10080b)$。它和 (8) 不成比例：比较 $T^2$ 与 $T$ 的系数即可核定，且次数小于三，不能借三次最小多项式消除差别。因此 (7) 是一条新的实际纯三线乘积。

还可同时核定
$$
\boxed{
C_X^{\rm old}
=\frac9{4480b}
 \left(C_Y^U-\frac{4b}{9}C_A^U\right).}
\tag{10}
$$
这保留了旧来源的准确归一，并给出新旧两条低因子行的共同原有限空间。

## 3. 五个实际输入的完整普通 $p$-core

固定普通 $p>7$、$p\equiv1\pmod3$。所有周期和角色沿 R311、R316，记
$$
\pi=\psi_{17}(\mathfrak p),\quad
\bar\pi=\psi_{17}(\bar{\mathfrak p}),\quad
\varepsilon=\psi_0(\mathfrak p)/\psi_{17}(\mathfrak p)\in\mu_6,
$$
$$
\varkappa=p/\bar\pi^2,\quad
\lambda_\Theta=\varepsilon/\bar\pi,\quad
\lambda_\sigma=\varepsilon^3/\bar\pi.
\tag{11}
$$
R316 的完整测度恒等式是
$$
\nu_\Theta|_{p\mathbf Z_p}
 =\lambda_\Theta[\varkappa]_*\nu_\Theta,\qquad
\nu_\sigma|_{p\mathbf Z_p}
 =\lambda_\sigma[\varkappa]_*\nu_\sigma.
\tag{12}
$$
这里 $\nu_G$ 的 Amice 变换为 $G(\Omega_p\log(1+Z))$，始终是同一原形式周期。

在五个变量 $(s,t_1,t_2,t_3,r)$ 上置
$$
y=2s+2(t_1+t_2+t_3)+\delta r,\qquad
\nu=\nu_\sigma\otimes\nu_\Theta^{\otimes4}.
$$
则 (7) 是完整加法卷积
$$
\boxed{\nu_V=\frac13y_*\nu.}
\tag{13}
$$
$\delta\in\mathbf Z_p^\times$ 取原普通嵌入。其缩放留在 $y$ 中；没有将五变量相加的单位条件换成各因子单位条件。

五个输入同时在 $p\mathbf Z_p$ 的准确系数为
$$
\boxed{\lambda_\sigma\lambda_\Theta^4
       =\frac{\varepsilon}{\bar\pi^5}.}
\tag{14}
$$
这同时保留 sigma 的三次角色和四条 $\Theta$ 的一次角色。

### 3.1 实际输出 carry 返回同三条原线

令 $\mathcal D=\mathbf Z_p^5\setminus(p\mathbf Z_p)^5$，并对 $n\ge0$ 定义真实单位测度
$$
\mathfrak C_n=\frac13(y/p^n)_*
       \left(\mathbf1_{\mathcal D,\ v_p(y)=n}\nu\right).
\tag{15}
$$
$n=0$ 时它就是 $\nu_V^\times$。由 (8)，
$$
T_p\nu_{Y_j}=c_j\nu_{Y_j},\qquad
c_j=\xi_j(\mathfrak p),\qquad c_j^3=\varepsilon,
\tag{16}
$$
其中 $T_p=\bar\pi[\bar\pi^2]_*\psi_p$ 仍是原已付的完整算子。故
$$
\boxed{T_p^3\nu_V=\varepsilon\nu_V.}
\tag{17}
$$

对 $n\ge1$，(12)–(14) 准确给
$$
\boxed{
\mathfrak C_n=\bar\pi^{-n}[\bar\pi^{-2n}]_*
\left((T_p^n-\varepsilon\bar\pi^{-4}T_p^{n-1})
                           \nu_V\right)^\times.}
\tag{18}
$$
证明先取全部输出的第 $n$ 环带，再减去所有输入都在 $p$ 内的部分。后者由 (14) 是上一输出环带的
$\varepsilon\bar\pi^{-5}[\varkappa]_*$；
共同输出归一为 $\bar\pi^{-n}[\bar\pi^{-2n}]_*$ 后，括号中的系数正是
$\varepsilon\bar\pi^{-4}$。所以 (18) 不是对未知 carry 另行指定特征值。

从而
$$
\boxed{
\mathfrak C_{n+3}
=\varepsilon\bar\pi^{-3}[\bar\pi^{-6}]_*\mathfrak C_n
\qquad(n\ge1).}
\tag{19}
$$
这是实际五输入 carry 的三阶返回，所有输入与输出尺度均已保留。

### 3.2 完整 tame-one 行与中央质量

置 $d=p-1$，令
$$
\mathcal U_j(u)=
 \int_{\mathbf Z_p^\times}x\langle x\rangle^{du}\,d\nu_{Y_j}(x),
\quad
\mathcal U_V(u)=\sum_{j\in I_+}v_j\mathcal U_j(u).
$$
由 (18)，$\mathfrak C_n$ 的同一 tame-one 行准确为
$$
\boxed{
\bar\pi^{-3n}\langle\bar\pi\rangle^{-2ndu}
\sum_{j\in I_+}v_j
(c_j^n-\varepsilon\bar\pi^{-4}c_j^{n-1})\mathcal U_j(u).}
\tag{20}
$$
其中央导数必须逐项使用
$$
\mathcal U_j'(0)-2nd\log_p\bar\pi\,\mathcal U_j(0).
\tag{21}
$$
原质量是
$$
\mathcal U_j(0)=\Omega_p(1-c_j\pi/\bar\pi^2),
$$
因此
$$
\boxed{
\mathcal U_V(0)=\Omega_p
 \left(\frac23-\frac{\pi}{\bar\pi^2}\sum_jv_jc_j\right)
 \in\Omega_p\mathcal O^\times.}
\tag{22}
$$
这个单位性对全部当前普通 $p$ 成立，因为第二项在 $p\mathcal O$。
它是原 tame-one 第一矩；并不确定 $\mathcal U_V'(0)$。

R311 的完整 Katz 平方还给出
$$
\boxed{
\mathcal U_V'(0)=\frac12\sum_jv_j\mathcal U_j(0)
 \left\{\frac{\mathscr L_j'(0)}{\mathscr L_j(0)}
                       +d\log_p34\right\}.}
\tag{23}
$$
$\mathscr L_j$ 是相同三条实际高权 Hecke 支，所有周期和 smoothing 与 R311 一致。本文没有给这些对数导数赋一个未经证明的值。

### 3.3 全部输入环带与统一尾

完整输入重构使用 R316 的质量零测度
$$
\eta_\Theta=\nu_\Theta^\times-(1-\lambda_\Theta)\delta_0,
\qquad \eta_\sigma=\nu_\sigma^\times,
$$
$$
\nu_\Theta=\delta_0+\sum_{a\ge0}
 \lambda_\Theta^a[\varkappa^a]_*\eta_\Theta,\qquad
\nu_\sigma=\sum_{a\ge0}
 \lambda_\sigma^a[\varkappa^a]_*\eta_\sigma.
\tag{24}
$$
四条 $\Theta$ 输入可分别取零点项或一个环带；sigma 输入始终取环带。
将 (24) 代入 (13)，原 tame-one 的测试核是
$$
\mathbf1_{y\in\mathbf Z_p^\times}\,y\langle y\rangle^{du}.
\tag{25}
$$
所有 $2,\delta$ 系数留在 $y$ 中。

每个正深度输入的质量零性允许减去该变量为零的值。若环带指标为
$a_i>0$，这个有限差分至少贡献 $p^{a_i}$。具体展开在单位圆盘内进行；
多重 Taylor 项中，$\sum a_ik_i-\sum v_p(k_i!)\ge\sum a_i$，$k_i\ge1$。
因此总指标至少 $N$ 的尾在同一 $u$ 单位闭盘上属于
$p^N\mathcal O\langle u\rangle$，求中央导数后仍然如此。
这给五输入的完整重构，而不假设 $p$ 进测度对任意无穷分割具有实测度式可加性。

## 4. 连接输出的无逆参考乘积

令
$$
A_6=U/X,\qquad B_6=U/(X-8b),\qquad C_6=U/(X-8b)^2.
\tag{26}
$$
它们都是 R320 的原 degree-$34$ 全纯来源，质量零且从至少 $z^6$ 开始。由 (4)，准确有
$$
\boxed{\begin{aligned}
A_6&=\sigma(z)^6\Theta(2z)^2
       \{\Theta(\delta z)-12b\sigma(z)^6\}^2,\\
B_6&=\sigma(z)^6\Theta(z)^2\Theta(2z)^3,\\
C_6&=\sigma(z)^{12}\Theta(z)^3\Theta(2z)^2.
\end{aligned}}
\tag{27}
$$
“乘积”在此指各因子的指数非负；展开后每个系数的正负仍然保留。

同一个原连接 $\nabla_U=\partial_z-U'/U$ 给
$$
\boxed{
D_V:=\nabla_UV
=\frac23U-\frac{4b}{3}A_6+60bB_6+432b^2C_6.}
\tag{28}
$$
这是由 (2)、(7) 得到的特征零恒等式，且 $D_V(0)=2/3$。
它把原连接输出写成一份完整的低因子乘积表达，不留下一个待指定的逆 $U$ 操作。

原目标同时满足
$$
\boxed{
S+\frac{H_3+U}{336b}
=\frac{A_6}{168}-\frac{3B_6}{56}
                     +\frac{D_V}{112b}.}
\tag{29}
$$
原点质量左端为 $1/(168b)$，右端也为 $1/(168b)$。
$U/(336b)$ 必须保到完整中央质量修正之后。

(27) 的每个乘积都有一份完全明确的原加法卷积：将 $\sigma(z)^a$ 视为
$a$ 个 $\nu_\sigma$ 输入，将 $\Theta(cz)^a$ 视为 $a$ 个 $[c]_*\nu_\Theta$ 输入，
求和后再用 $\mathbf1_{\text{和为单位}}\langle\text{和}\rangle^{du}$ 积分。
第一式展开为
$$
A_6=\sigma^6\Theta(2z)^2\Theta(\delta z)^2
-24b\sigma^{12}\Theta(2z)^2\Theta(\delta z)
+144b^2\sigma^{18}\Theta(2z)^2.
\tag{30}
$$
每个输入都按 (12)、(24) 保留真实环带和角色。与 §3.3 相同的多重有限差分证明，总输入指标至少 $N$ 的尾仍有 $p^N$ 下界。因而 (28)–(30) 已给完整的原观察，并非只记录一个全纯来源的形式乘积。

## 5. 同一中央泛函的准确新关系

沿 R321 的普通规范，置
$$
m_U=M_U(0),\quad \ell_U=M_U'(0)/m_U,\quad
\mathcal C_U(T)=M_T'(0)-\ell_U M_T(0).
\tag{31}
$$
R320 已证明所有充分大的普通 $p$ 的 $m_U$ 为单位。
在惰性处使用同式 $M=\mathcal J$、$m_U=1$。
因此 $\mathcal C_U(U)=0$，且
$\mathcal C_U(S)$ 始终是原 $S$ 的同一个中央导数。

对完整 (29) 作相同质量修正，得到
$$
\boxed{
\mathcal C_U(S)+\frac{\mathcal C_U(H_3)}{336b}
=\frac{\mathcal C_U(A_6)}{168}
-\frac{3\mathcal C_U(B_6)}{56}
+\frac{\mathcal C_U(D_V)}{112b}.}
\tag{32}
$$
所有右端都在 (27)–(30) 给出的实际低因子核中；参考自身的未知斜率没有被提前设零。

普通处令 $q_U=U'/U$，并保留真实卷积
$$
K_{q_U,V}(u)=\iint
 \mathbf1_{x+y\in\mathbf Z_p^\times}
 \langle x+y\rangle^{du}\,d\nu_{q_U}(x)d\nu_V(y).
$$
R321 的同一完整转置给
$$
M_{D_V}(u)=\Omega_p^{-1}\mathcal U_V(u)-K_{q_U,V}(u),
\tag{33}
$$
$$
\boxed{\begin{aligned}
\mathcal C_U(D_V)
={}&\Omega_p^{-1}\{\mathcal U_V'(0)-\ell_U\mathcal U_V(0)\}\\
 &-\{K_{q_U,V}'(0)-\ell_UK_{q_U,V}(0)\}.
\end{aligned}}
\tag{34}
$$
在本篇的新来源上，整个连接卷积还有具体的无逆参考表达
$$
\boxed{\begin{aligned}
K_{q_U,V}(u)
={}&\Omega_p^{-1}\mathcal U_V(u)\\
&-\left\{\frac23M_U(u)-\frac{4b}{3}M_{A_6}(u)
                 +60bM_{B_6}(u)+432b^2M_{C_6}(u)\right\}.
\end{aligned}}
\tag{35}
$$
这是完整权变量中的身份。式 (23)、(27)、(30)、(34)、(35) 把新三条 Katz 行、五输入 carry 和原连接放在同一个已付观察中，不能把 (35) 当成额外的独立中央零条件。

惰性处取原 $d=p+1$、$\kappa_b=34c_b$，并令
$$
Z=V/z,\quad Z(0)=2/3,\quad
\widehat W=z\,\partial_z\log(e^{-\kappa_bz^d}U).
$$
R321 的完整 Newton 转置在这里准确成为
$$
\boxed{
\mathcal J_{D_V}(u)
=(du+1)\mathcal J_Z(u)
-du\mathcal J_Z(u-1)-\mathcal J_{\widehat WZ}(u),}
\tag{36}
$$
$$
\boxed{\begin{aligned}
\mathcal C_U(D_V)
={}&\mathcal J_Z'(0)-\frac23\mathcal J_U'(0)\\
&+d\{2/3-\mathcal J_Z(-1)\}
-\mathcal J_{\widehat WZ}'(0).
\end{aligned}}
\tag{37}
$$
其中 $\mathcal J_{D_V}$ 同时由 (28)、(27) 给出。$u-1$、$\widehat W$ 和首项 $2/3$ 均保留；没有用 ordinary 的第一矩代替这条惰性中央行。

## 6. 精确证书及所得接口

[check-jzero-new-pure-five-factor-central-source.py](../scripts/check-jzero-new-pure-five-factor-central-source.py)
及其 JSON 给出 **26 项精确检查全部 PASS**。证书由原曲线微分和 R311 已付的实际 $P_\pm$ 重建 (2)–(10)，同时核定原 $S,H_3$ 的全部系数与质量、五输入原 $p$-core 相位以及 (27)–(30)。三次域核定使用真实多项式迹，不以浮点谱拟合替代。

新增输入是 (7) 的独立纯三线五因子来源，及它的完整实际核 (18)、(27)、(32)–(37)。这些式子保留了原目标的每一个未知中央项；要证明主目标，仍需控制同一组原行的非零或给出真正独立的算术关系。来源数量、固定乘积和非零第一矩各自没有完成这一步。

直接依赖：
[R311](R311-jzero-original-odd-six-tame-one-core-and-pure-dyadic-companion.md)、
[R316](R316-jzero-low-degree-original-cores-and-complete-four-factor-carry.md)、
[R319](R319-jzero-ramified-three-minimal-unit-and-mixed-scaled-return.md)、
[R320](R320-fixed-six-torsion-five-dimensional-trace-and-full-central-matrix.md)、
[R321](R321-jzero-fixed-six-torsion-primitives-and-complete-u-frame-transpose.md)。

