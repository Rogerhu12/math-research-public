# R661 — 原 odd-five 全部有限型与 R653 两条 log 行的准确 Katz 返回

状态：已证明完整来源身份、同一角色线及两个显示的对数导数公式。本文不证明 $\ell_D$ 或 $\ell_{Z,1}$ 非零，也不把 R653 的完整 $W$ 失败支删去。

## 0. 两条真正原行

沿 R653/R655 的同一微分和 Amice 规范，置
$$
D_5=-x_\wp y_\wp\sigma_{17}^5,\qquad
Z_5=x_\wp^2\sigma_{17}^5,\qquad
\Sigma_5=\sigma_{17}^5.
$$
其首项分别为 $1,z,z^5$。本文处理的原测试准确是
$$
\ell_D=\int_{\mathbf Z_p^\times}\log\langle Q\rangle\,d\nu_{D_5}(Q),
\qquad
\ell_{Z,1}=\int_{\mathbf Z_p^\times}
 Q\log\langle Q\rangle\,d\nu_{Z_5}(Q).
\tag{1}
$$
没有额外 $\Omega_p$ 藏在 (1) 的定义中。

复用 R655 的 $K,\delta,\omega,s_0,\psi_0,\chi,\theta=17^{1/6}$。
该篇已付
$$
\chi((a))=[a]_5^4/t_2(a),\qquad
\psi_A=\chi^{-1}\psi_0,\qquad
A\simeq E_{80},\qquad I_{\Sigma_5,-1}\ne0.
$$
定义另一个准确的型 $(1,0)$ 角色和一个反圆分方向：
$$
\boxed{\psi_B=\chi^2\psi_0,\qquad
\rho=\chi\,\psi_0/\bar\psi_0.}
\tag{2}
$$
它们在素于五的原主理想上分别有
$$
\psi_B((a))=\frac{a}{\operatorname{sgn}_\delta(a)[a]_5^{16}},
\qquad
\rho((a))=\frac{a}{\bar a}[a]_5^4.
\tag{3}
$$
$\rho$ 的准确导子为 $(5)$，型为 $(1,-1)$，有理主理想上的值为一。
$\psi_B$ 是
$$
B:\ y^2+y=x^3+156
\quad\longleftrightarrow\quad E_{10000}:y^2=x^3+10000
\tag{4}
$$
的 Hecke 角色；其解析秩为零，见第 4 节。

令 $d=p-1$，在对应实际 tame 分量上设
$$
\mathscr K(m)=\mathcal L_{p,5\delta}^{\mathrm{prim}}(\psi_B\rho^m),\qquad
\mathscr K_D(u)=\mathscr K(du),\quad
\mathscr K_Z(u)=\mathscr K(1+du).
\tag{5}
$$
只在本篇使用的分量 $m\equiv0,1,5\bmod6$ 称 primitive；
并未给其它、可能降导子的分量删掉 Euler 因子。
这些方向都是 $\rho^{du}=(\psi_0/\bar\psi_0)^{du}$ 的真实反圆分方向，不是 cyclotomic height 方向。

在当前固定 ray，R655 已付 $\chi(\mathfrak p)=1$ 和
$\beta=1/\bar\pi_0=-\lambda$。准确结果是
$$
\boxed{
\frac{2\ell_D}{1-\beta}
 =\frac{\mathscr K_D'(0)}{d\,\mathscr K_D(0)}
    +\log\langle5\rangle,
}
\tag{6}
$$
$$
\boxed{
\frac{2\ell_{Z,1}}{\Omega_p(1-\beta\varkappa)}
 =\frac{\mathscr K_Z'(0)}{d\,\mathscr K_Z(0)}
    +\log\langle5\rangle.
}
\tag{7}
$$
两个分母中的 Katz 值均非零。共同已知的 $\log\langle5\rangle$ 不得删去。
同一角色线的第三个真实值是
$$
\boxed{\mathscr K(-1)
 =\mathcal L_{p,5\delta}^{\mathrm{prim}}(\bar\psi_A)
 =5c_5\theta^{11}\Omega_p I_{\Sigma_5,-1}^{\,2}\ne0.}
\tag{8}
$$
(8) 本身没有决定 (6)、(7) 的导数。

## 1. 完整 odd-five 的五个有限 Schwartz 型

R655 固定 $\alpha=5/2$、$\kappa_\infty=15\sqrt3/2$、
$\phi_2=-\chi_{-2}(2x)\mathbf1_{v_2(x)=-1}$ 和
$\phi_3=\mathbf1_{3^{-1}\mathbf Z_3}$。
对 $r=1,\ldots,5$，令
$$
j(r)=r-2\bmod6\in\{5,0,1,2,3\},\qquad
\Phi_{r,m}=\chi^r\psi_0^{2m+1},\qquad m\equiv j(r)\bmod6.
\tag{9}
$$
二处单位指数为 $r+2m+1\equiv0\bmod3$；三处 uniformizer 为
$i(-1)^{m+r}=i$。因此二、三处的**完整**角色及向量与 R655 相同，
不是只保剩余群相位。

五处单位角色变成 $[u]_5^{-4r}$，uniformizer 仍为 $-1$。
完整有限 Gauss 和为
$$
G_r=\sum_{u\in\mathbf F_{25}^\times}
 [u]_5^{4r}\exp\!\left(-\frac{2\pi i}{5}\operatorname{Tr}u\right)
 =5(-1)^r.
\tag{10}
$$
故 epsilon 是 $(-1)^{r+1}$，而 $\chi_{r,m,5}(\delta)=(-1)^r$；
乘积仍为 $-1$。同一个 $\alpha=5/2$ 对五型全部合法。

在 $e_b=\mathbf1_{b/5+\mathbf Z_5}$ 上，原矩阵准确是
$$
(M_r)_{ab}=\frac{\omega^r}{\sqrt5}
 \zeta_5^{-2(a^2+4ab+b^2)}.
\tag{11}
$$
取
$$
e^{(r)}=
\begin{cases}e_0,&r\ \text{奇},\\e_1-e_{-1},&r\ \text{偶},\end{cases}
\qquad
v_r=\frac{I+M_r+M_r^2}{3}e^{(r)}.
\tag{12}
$$
准确商环计算给 $M_r^3=I$、$M_r^*M_r=I$，
$v_r\ne0$、$M_rv_r=v_r$，且
$$
(v_r)_{-b}=(-1)^{r+1}(v_r)_b,\qquad (v_r)_b\in\mathbf R.
\tag{13}
$$
$-1$ 的完整作用是 $(-1)^{r+1}$ 乘反射，恰与 (13) 匹配。
主五单位仍平凡；故 (12) 对整个 $K_5^1$ 成立。
所有其余有限地方保持 R655 的标准 Schwartz，原 finite norm 为
$$
3n_r,\qquad n_r=\sum_b |(v_r)_b|^2>0.
\tag{14}
$$
这里 $n_2=2(v_2)_1$，
$$
n_3=\frac{1+2/\sqrt5}{3}.
\tag{15}
$$
$n_2$ 的完全准确值由 (11)、(12) 给出，证书列出其八个 $\mathbf Q(\zeta_{15})$ 坐标；
不需要另把该固定正代数数认成一个浮点近似。

## 2. 真周期与五个全函数身份

令
$$
a_{r,n}=\chi_{-2}(n)(v_r)_{n\bmod5},\qquad
b_{r,m}=\sum_n a_{r,n}
 H_m\!\left(\frac{\sqrt{15\sqrt3/2}}{30}n\right)
 e^{-\pi\sqrt3n^2/120}.
$$
所有 $a_{r,n}$ 都是实数，偶数 $n$ 时为零。
R655 的完整周期关系 $a_{n+20}=-a_n$、
$a_{n+10}=(-1)^{(n-1)/2}a_n$ 对每个 $r$ 原样成立。
所以原 reduced theta 全部仍在标准 odd $\mathcal S_5$，Gaussian 和 flat 特征都已支付。

基角色 $\psi_0\mathrm N^{-1/2}$ 的 finite $\omega$ 特征为 $\omega^{2-r}$。
global rational $\omega$ 不变性给 $m+2-r\equiv0\bmod3$；
由 $a_{r,-n}=(-1)^ra_{r,n}$ 再得到准确型 $j(r)$。
原空间的完整五条单重型线是

| $r$ | $j(r)$ | 原 $b=1$ 来源 $f_j$ | 首项 | 正权角色 |
|---:|---:|---|---|---|
| 1 | 5 | $\sigma_0^5$ | $z^5$ | $\psi_A^{2m+1}$ |
| 2 | 0 | $-x_\wp y_\wp\sigma_0^5$ | $1$ | $\psi_B^{2m+1}$ |
| 3 | 1 | $x_\wp^2\sigma_0^5$ | $z$ | $\psi_A^{2m+1}$ |
| 4 | 2 | $-y_\wp\sigma_0^5$ | $z^2$ | $\psi_B^{2m+1}$ |
| 5 | 3 | $x_\wp\sigma_0^5$ | $z^3$ | $\psi_A^{2m+1}$ |

该表的最后一列用 $\chi^6=1$ 直接验证，并未由一个好素数的相位认曲线。
这些型穷尽 $\mathcal S_5$，其型四空间为零。

置 $h=\sqrt{15\sqrt3/2}/(30\pi i)$。每个 Fourier 级数都非零，
于是全线丛和单重型给固定非零常数
$$
\sum_m b_{r,m}\frac{T^m}{m!}
 =C_j f_j(\Omega_0hT),\qquad
C_j=\frac{b_{r,j}}{j!(\Omega_0h)^j}.
\tag{16}
$$
$j$ 偶时 $C_j$ 实，$j$ 奇时 $C_j$ 纯虚。
这里特别 $D_5$ 与 $Z_5$ 的身份已经在完整全函数上支付。

## 3. 全权平方常数及实际普通测度

同 R655，$S_1=\{5\}$、$c(0)=5/6$，无二处 imprimitive 删除。
定义
$$
C_{{\rm Y},r}
 =\frac{2\pi\sqrt{15\sqrt3}}{45\sqrt3\,n_r},\qquad
\kappa_j=\frac{(-1)^j C_{{\rm Y},r}C_j^2}{\Omega_0}>0,\qquad
c_j=\frac{(-\omega)^j\kappa_j}{s_0}.
\tag{17}
$$
Yang 原范数为 $3n_r\,m!/(4\pi)^m/\sqrt{15\sqrt3}$，所以全部
$m\ge0,\ m\equiv j\bmod6$ 满足
$$
\boxed{
\frac{(2\pi/\sqrt3)^mL(\chi^r\psi_0^{2m+1},m+1)}
 {m!\varpi_0^{2m+1}}
 =c_j5^{-m}\bigl([z^m]f_j\bigr)^2.
}
\tag{18}
$$
各 $c_j$ 是固定非零代数数；(17) 固定其原尺度。
以下记 $c_D=c_0$、$c_Z=c_1$，故
$c_D=\kappa_0/s_0$、$c_Z=-\omega\kappa_1/s_0$。
首权分别为零和一，(18) 已证明对应两个复临界值非零。

$b=17$ 与 $b=1$ 的实际测度关系是
$$
f_{j,17}(z)=\theta^{-j}f_{j,0}(\theta z),\qquad
\nu_{f_{j,0}}=\theta^j\nu_{f_{j,17}},\qquad
\Omega_{p,0}=\theta\Omega_p.
\tag{19}
$$
尤其 $D_5$ 的测度不乘 $\theta$，$Z_5$ 的测度恰乘一次 $\theta$。
这决定下面两个不同的周期系数。

密集正权极限完全按 R655 §6 进行。对
$$
J_D(u)=\int_{\mathbf Z_p^\times}\langle Q\rangle^{du}\,d\nu_{D_5},
\qquad
J_Z(u)=\int_{\mathbf Z_p^\times}Q\langle Q\rangle^{du}\,d\nu_{Z_5},
$$
得到准确的整个解析支：
$$
\boxed{
\mathscr K_D(u)=c_D\theta\Omega_p
 \langle5\rangle^{-du}J_D(u)^2,
}
\tag{20}
$$
$$
\boxed{
\mathscr K_Z(u)=\frac{c_Z\theta^3\Omega_p}{5}
 \langle5\rangle^{-du}J_Z(u)^2.
}
\tag{21}
$$
两个普通 Euler 因子仍是
$1-\chi(\mathfrak p)^r\pi_0^m/\bar\pi_0^{m+1}$ 的平方。
在当前 ray $\chi(\mathfrak p)=1$，完整 odd-five core 是同一 $\beta$，故
$$
J_D(0)=1-\beta,\qquad
J_Z(0)=\Omega_p(1-\beta\varkappa).
\tag{22}
$$
$1-\beta=1+\lambda$ 的单位性由 R410 的原固定 ray 已付；
$1-\beta\varkappa$ 的单位性由 $v_p(\varkappa)=1$ 直接给。
因此 (20)、(21) 在零点都非零，可以合法作 logarithmic derivative。

不能在经典正整数公式中把不连续的 $p^m$ 当成一个任意 $m\in\mathbf Z_p$ 的可微函数。
(20)、(21) 是先经真实单位测度极限建立的解析函数；本篇只对此作微分。
由于 $J_D'(0)=d\ell_D$、$J_Z'(0)=d\ell_{Z,1}$，
它们准确给 (6)、(7)。

## 4. 两条完整算术分支

(3) 的 $\psi_B$ 是 R655 完整导子 $5\delta$ 分类中的第二条角色。
同时
$$
\frac{\psi_B}{\psi_A}=\chi^3,\qquad
\chi((a))^3=[a]_5^{12}
 =\left(\frac{\mathrm N(a)}5\right).
\tag{23}
$$
所以它是 $E_{80}$ 的 quadratic-$5$ 扭，短方程为
$y^2=x^3+10000$（$80\cdot5^3=10000$），经
$(x,y)=(4X,8Y+4)$ 得 (4)。
其 Hecke 导子仍为 $5\delta$、经典导子为 $225$。

取 $m=0$ 于 (18)，因 $D_5$ 的首项为一，得到
$L(\psi_B,1)>0$，所以这是一个实际解析秩零参考。
如需与该曲线的最小微分同步，令 $\rho_B=10000^{1/6}$，则
$$
\varpi_B=2\varpi_0/\rho_B,\qquad
\Omega_{p,B}=2\Omega_{p,0}/\rho_B.
$$
两周期同步，故不改变 (20) 所用的 Katz 函数。

另一方面，$\mathscr K_Z(0)$ 的角色是
$$
\chi^3\psi_0^2\bar\psi_0^{-1}
 =\psi_A^2\bar\psi_A^{-1}
 =\psi_A^3\mathrm N^{-1}.
\tag{24}
$$
其复插值是 $L(\psi_A^3,2)$，由 $Z_5$ 的首项为 $z$ 和 (18) 知严格非零。
它并不是 R655 的型 $(0,1)$ 共轭点；后者由
$\psi_B\rho^{-1}=\bar\psi_A$ 才得到 (8)。

因此三个原行落在同一固定角色线
$$
m\longmapsto\psi_B\rho^m
$$
的 $m=0,1,-1$ 处，但可能位于不同实际 tame 分量。
一个分量上的值非零不决定其它分量的导数。
R655 的 Rubin–BDP 非挠点 logarithm 平方用于 $m=-1$；
它没有把本篇两个反圆分 logarithmic derivative 化成 cyclotomic height。

## 5. 原 R653 四 $K$ 中的逐项返回

保留 R653 的实际冻结门
$$
G_0=\{C\in\mathbf Z_p^\times,\ D_0\in p^N\mathbf Z_p\},
$$
及其原 $Q$-independent 测试 $p_0,e_0$。
定义的真实系数是
$$
M_0=\int_{G_0}p_0\,d(\nu_4\otimes\nu_{F_{12}}),
$$
$$
H_-=\int_{G_0}A p_0\,d(\nu_4\otimes\nu_{X_5}),\qquad
H_+=\int_{G_0}e_0\,d(\nu_4\otimes\nu_{Z_5}),
\qquad b_F=\frac{5+6\omega}{5}.
\tag{25}
$$
其中 $\nu_4=-P_{6,C}\sigma^{\otimes4}/84$，所有输入与门保持原义。
没有额外 $\Omega_p$ 被吸入这些定义。

设
$$
\mathfrak d_D=
 \frac{\mathscr K_D'(0)}{d\mathscr K_D(0)}
   +\log\langle5\rangle,\qquad
\mathfrak d_Z=
 \frac{\mathscr K_Z'(0)}{d\mathscr K_Z(0)}
   +\log\langle5\rangle.
$$
R653 的两个真正第一轴项由 (6)、(7) 准确变成
$$
\boxed{K_{Y,0}=-\frac{M_0(1-\beta)}2\,\mathfrak d_D,}
\tag{26}
$$
$$
\boxed{
K_{Y,1}=6bH_- I_{\Sigma_5,-1}
 +\frac{3b_F\,\Omega_p(1-\beta\varkappa)}2
       H_+\mathfrak d_Z.
}
\tag{27}
$$
原 Mellin 导数外的 $d=p-1$ 因子仍按 R653 放置；(26)、(27) 没有再乘一次 $d$。

共同非齐次项还给准确差式
$$
2\left(\frac{\ell_D}{1-\beta}
 -\frac{\ell_{Z,1}}{\Omega_p(1-\beta\varkappa)}\right)
 =\frac1d\left(
 \frac{\mathscr K_D'(0)}{\mathscr K_D(0)}
 -\frac{\mathscr K_Z'(0)}{\mathscr K_Z(0)}\right).
\tag{28}
$$
$\log\langle5\rangle\ne0$，因为 $p$ 进 logarithm 在有理单位上的零核只含
有理根单位，而 $5\ne\pm1$。它在 (28) 中相消，但不能在 (26)、(27) 的各行中删除。

若将来从**完整实际补域关系**证明 $K_{Y,0}=0$ 且 $M_0\ne0$，
才可推出 $\mathscr K_D'(0)/(d\mathscr K_D(0))=-\log\langle5\rangle$。
当前并没有把原中央零直接提升成这一单项等式。
同样，(27) 的第一项虽由 R655 的负一矩非零控制，仍须保 $H_-$、
$H_+$ 和所有 $W$ 失败支，不能因此宣布总行非零。

## 6. 证明与复现范围

本文新增的是两条原 log 测试的完整有限角色、周期/Euler 规范、同一反圆分角色线，
以及它们在 R653 确定门内的准确非齐次返回。
两个 logarithmic derivative 的指定数值仍开；没有增加第三条 rank-two 中央零假设。

主要来源：

- [R655](R655-original-sigma-five-schwartz-and-rank-one-negative-moment.md)：$\alpha=5/2$ 的完整二、三处、实际半特征、Yang/Katz 规范、$E_{80}$ 身份及负一非零。
- R653：原五输入、冻结门及四个 $K$ 的真实分离。
- R410：当前 ray 的 $1+\lambda$ 单位及原 Frobenius 规范。
- Yang 1997 Theorem 1.11、Yang 1999 Proposition 1.2 / Proposition 1.5 / Appendix (A1)–(A3)，准确版本与作者链接见 R655。
- BDP 2012 Theorem 3.1 / Proposition 3.5，原期刊版本与作者链接见 R655。

[脚本](../scripts/check-r661-odd-five-all-types-and-original-log-rows.mjs) 与
[证书](../scripts/check-r661-odd-five-all-types-and-original-log-rows.json)
只用有理数和 $\mathbf Q(\zeta_{15})$ 的准确商环。
580 项检查覆盖五个完整矩阵、五个非零投影、所有有限 Gauss 和、
全 Fourier 周期与型、$\chi^3$ 的完整 quadratic-$5$ 身份。
这是固定完整有限数据的证书；没有扫描普通素数来猜 log 矩非零。
