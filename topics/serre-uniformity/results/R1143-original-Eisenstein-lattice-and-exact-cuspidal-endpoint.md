# R1143：原权六端点的整 Eisenstein 比较与精确尖点生成元

日期：2026-11-28（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。

**已证明，结论与范围。** 本文对每个 $p>37$，把 R1140 的同一个紧致端点 $c_{\rm Eis}$ 精确接到原 leading-normalized cuspidal 函数的 $p$-torsion 点。采用 R1140 的 $N(x,y)=x^2-\delta y^2$、$m=(p-1)/2$ 和路径 $0\to\infty$，结果是
$$
\boxed{\qquad
c_{\rm Eis}=-2016\delta^2P_{\chi_1},\qquad
P_{\chi_1}=\left[\frac1p\operatorname{div}(F_{\chi_1})\right],
\quad \chi_1=\omega^{-2}.
\qquad}
\tag{1143.1}
$$
这里的 Betti 类按原周期的 $1/p$ 比较送进 $J[p]$，$F_{\chi_1}$ 表示原规范函数的任一实际代表。显示系数对 $p>37$ 为单位，因而这个指定端点无条件非零。本文不以新的生成元替换原函数，不需要 $p\nmid B_{p-5}$。

证明使用 Banerjee–Merel 的真实零全纯周期 Eisenstein 链，完整支付其四阶整展开、原 degree-$p+1$ transfer、尖点边界的 $\{\pm1\}$ 因子、Abel–Jacobi 的负号和原 Siegel divisor 尺度。这个来源非零结论不表示其 motivic 读数非零，也不确定 R1141 的算术 cup 倍数；一般 $p$ 排点仍未完成。全文是纸面证明，没有数学程序执行。

## 1. 同一原曲线、同一端点和原规范函数

沿 R1140，置
$$
X=X_{\rm ns}^+(p),\quad K=\mathbf Q(\zeta_p),\quad
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
q=N\circ J=y^2-\delta x^2.
\tag{1143.2}
$$
记 $Z=X(p)_K$ 为原 fixed-Weil full-level 曲线，
$H=(N_{\rm ns}\cap\mathrm{SL}_2(\mathbf F_p))/\{\pm1\}$，
$H'=J^{-1}HJ$，所以 $|H|=|H'|=p+1$。
$f:Z\to X_K$ 是原有限商。R1136 的实际 symplectic-dual convention 先用 $J_*$ 运输，再用 $f_*/(p+1)$ 下降。

若 $g=(v,w)\in\mathrm{SL}_2(\mathbf F_p)$，$e_g$ 是从 $g0$ 到 $g\infty$ 的原 Manin 路径。采用通常终点减起点的边界：
$$
\partial e_g=[v]-[w].
$$
原端点为
$$
C_E=\frac1{2m^2}\sum_{g\in\mathrm{SL}_2(\mathbf F_p)}
       q(w)^2e_g,\qquad
c_E=\frac1{p+1}f_*J_*C_E .
\tag{1143.3}
$$
$1/2$ 仅消 simultaneous-sign 双计；$C_E$ 与 R1140 的 $C_{\rm Eis}$ 相同。该文已逐端点证明其模 $p$ 紧致性，并证明
$$
T_\ell c_E=(\ell^{-2}+\ell^3)c_E\qquad(\ell\ne p).
\tag{1143.4}
$$

本篇不用 R1062 中任意选择的 $c_1$ 来猜一个解析尖点。改取实际 q-expansion 尖点
$$
c_\infty=f(\infty)=f(J e_2),\qquad
D_\chi=e_\chi[c_\infty]\in\operatorname{Div}^0_\Sigma(X)\otimes\mathbf Z_p .
\tag{1143.5}
$$
因 $Je_2=-e_1$，最后两个尖点完全相同；$q(e_2)=1$。$e_\chi$ 是原实际 Galois projector。

原函数沿 R1064 (1064.15)–(1064.18) 固定：取 augmentation-zero 整数提升
$n_h\equiv m^{-1}\chi(h)^{-1}\pmod p$，raw product 为
$\prod_hG_h^{n_h}$；其 $V$ 类是 $u_\chi$。原 $F_\chi$ 为 $u_\chi^m/A(u_\chi)$ 的 Kummer 类。因 $A$ 是常数，$F_\chi$ 的 divisor 对原 raw divisor 恰乘 $m$，没有额外 $2$。真实 bar norm 的 $2u_\chi$ 只是另一计算手段，不在本篇再次乘入。

## 2. 整 Eisenstein 格与尖点 p-torsion 的精确比较

对任一紧致复曲线及有限尖点集 $\Sigma$，置
$$
L_{\mathbf Z}=H_1(X(\mathbf C),\Sigma;\mathbf Z),\quad
B_{\mathbf Z}=\operatorname{Div}^0_\Sigma(X),\quad
\Lambda_{\mathbf Z}=\operatorname{div}(U)\subset B_{\mathbf Z}.
$$
设 $E_{\mathbf Q}$ 是全纯微分的所有周期均为零的有理相对链空间，
$E_{\mathbf Z}=E_{\mathbf Q}\cap L_{\mathbf Z}$。
对本篇模曲线，Manin–Drinfeld 保证这个有理结构；Banerjee–Merel 的 Theorem 1 给出下节所需的实际链。

Abel 定理及整周期格准确给
$$
\partial:E_{\mathbf Z}\xrightarrow{\sim}\Lambda_{\mathbf Z}.
\tag{1143.6}
$$
若 $\partial e=D$ 且所有全纯周期为零，则 $D$ 的 Abel–Jacobi 类为零，所以 $D$ principal。反过来，principal $D$ 的任一整相对链 $\gamma_D$ 的周期等于某条整紧致链的周期；两者相减就给所需 $e$。零边界且零全纯周期的整紧致链为零，故该映射也单射。

$E_{\mathbf Z}$ 在 $L_{\mathbf Z}$ 中饱和。张量 $\mathbf Z_p$ 并约模 $p$ 后，得到
$$
\begin{aligned}
\ker(E_{\mathbf Z_p}/p\longrightarrow B_{\mathbf Z_p}/p)
&\simeq
  (\Lambda_{\mathbf Z_p}\cap pB_{\mathbf Z_p})/p\Lambda_{\mathbf Z_p}\\
&\simeq C_\Sigma[p].
\end{aligned}
\tag{1143.7}
$$
该核通过饱和注入落在真正的 $H_1(X,\mathbf F_p)$ 中。

必须核对其 Betti 号。若 $\partial e=pD$，取 $\partial\gamma_D=D$，
则 $e-p\gamma_D$ 是紧致链，且
$$
\frac1p\int_{e-p\gamma_D}\omega=-\int_{\gamma_D}\omega .
$$
因此按 R1140 的 Betti→$J[p]$ convention，
$$
\overline e\longmapsto-[D].
\tag{1143.8}
$$
这不是把通常 boundary 换成反向 boundary 后留下的未定号。

原全部尖点和 principal cusp 格在实际 Galois 群下稳定。
可通过 (1143.6) 把这个作用运输到 $E_{\mathbf Z_p}$；这里只在 Eisenstein 格上定义它，没有假造整个 Betti homology 的算术 Galois 作用。
在 (1143.7) 的核上，(1143.8) 表明它恰等于 $C_\Sigma[p]\subset J[p]$ 的实际 Galois 作用。因而在这个核上取原 $e_\chi$ 完全合法。后文将该作用扩张到 $E_{\mathbf Z_p}\otimes\mathcal O$ 时始终取 **$\mathcal O$-linear** 作用：$\lambda$ 只是 coefficient uniformizer，不同时施加 $\sigma(\lambda)$ 的 semilinear 作用。

以上各式与有限平坦系数扩张相容；约模 $\lambda$ 的 kernel 可由原 $\mathbf F_p$ 格识别，后文只有在实际 $\chi_1$ 主除子格为 $p$ 倍时才使用 $\partial/p$。特别，取
$\mathcal O=\mathbf Z_p[\zeta_p]$、$\lambda=\zeta_p-1$，
则 $E_{\mathbf Z_p}\otimes\mathcal O$ 在
$L_{\mathbf Z_p}\otimes\mathcal O$ 中仍饱和，约模 $\lambda$ 仍为
(1143.7)；没有把 $\lambda$ 和 $p$ 的除法混同。

## 3. Banerjee–Merel 原链及其自足边界

对非零 $P=(x,y)\in\mathbf F_p^2$，选整数代表满足 $x-y$ 为奇数，定义
$$
F(P)=-\frac14
 \frac{\cos(\pi x/p)+\cos(\pi y/p)}
      {\cos(\pi x/p)-\cos(\pi y/p)},\qquad
\mathcal E_P=\sum_{g\in\mathrm{SL}_2(\mathbf F_p)/\{\pm1\}}
                   F(g^{-1}P)e_g .
\tag{1143.9}
$$
这是 Banerjee–Merel 的原定义，$F(-P)=F(P)$，$F(SP)=-F(P)$。
其 Theorem 1 / Proposition 12 证明每个 $\mathcal E_P$ 的全纯周期严格为零。

为避免把该文不同边界记号或 $\mu$ 的正负代表混用，下面从 (1143.9) 自算本篇的边界。固定尖点 $Q$ 的一个非零向量代表。由 $S$ 反对称，$[Q]$ 的系数为
$$
2\sum_{\substack{g/\{\pm1\}\\ge_1=Q}}F(g^{-1}P).
$$
其中条件以所选 $Q$ 代表唯一选择矩阵的正负。当 $P=\mu Q$ 时，恰有 $p$ 个矩阵，系数为 $2pF(\mu,0)$。

当 $P,Q$ 独立时，$g^{-1}P$ 的第二坐标非零，第一坐标跑遍 $\mathbf F_p$，而
$$
\sum_{u\in\mathbf F_p}F(u,v)=-p/4\qquad(v\ne0).
\tag{1143.10}
$$
可直接验证：置 $a=(p+1)/2$、$z=\zeta^{au}$、$w=\zeta^{av}$，
$$
F(u,v)=-\frac14+
 \frac12\,\frac{w+w^{-1}}{z+z^{-1}+w+w^{-1}}.
$$
第二项中分母为 $(z+w)(z+w^{-1})/z$。
利用 $\sum_{z^p=1}(z+w)^{-1}=p/(2w)$，部分分式的两个和精确抵消；$w\ne w^{-1}$，没有分母例外。故离线系数为 $-p/2$。

于是对本篇真实路径，有精确式
$$
\boxed{\quad
\partial\mathcal E_P
 =p\sum_{\mu\in\mathbf F_p^\times}
      \left(F(\mu,0)+\frac14\right)[\mu^{-1}P]
   -\frac p2\sum_{Q\in\Sigma(Z)}[Q].
\quad}
\tag{1143.11}
$$
这里 $\mu$ 遍历全部 $p-1$ 个非零元素；$[\mu^{-1}P]=[-\mu^{-1}P]$。
因此前系数是 $p$，不是再乘二的 $2p$。
若只取 $\mu/\{\pm1\}$，相同式的前系数才为 $2p$。
$P=\mu Q$ 同时固定了逆号，后文不再更换这项 convention。

## 4. p-adic 四阶展开和整个 normalizer 平均

只为计算有限系数，写
$$
Z=\lambda-\lambda^2/2+\lambda^3/3-\lambda^4/4
       \pmod{\lambda^5}.
$$
这只是形式 $\log(1+\lambda)$ 的截断，绝不把真正
$\log\zeta_p=0$ 当作非零解析参数。因 $x-y$ 为奇数，
两个 cos 在 $p$-adic residue 中符号相反，
$\zeta_{2p}=-\zeta_p^{(p+1)/2}$ 给
$$
F(x,y)\equiv
 -\frac{x^2-y^2}{64}Z^2
 +\frac{x^4-y^4}{1536}Z^4
 \pmod{\lambda^5}.
\tag{1143.12}
$$
这里分母均为单位。把 $(p+1)/2$ 换成 $1/2$ 只产生 $p$ 倍误差，其 $\lambda$-阶至少 $p-1>4$，所以 (1143.12) 是所需真实有限精度。原 $F$ 的 $p$-adic 分母从一开始就是单位。

令
$$
\mathcal E_H(P)=\frac1{p+1}\sum_{h\in H'}\mathcal E_{hP}.
\tag{1143.13}
$$
它的二阶系数约模 $p$ 为零，因此该项实际至少在 $\lambda^{p+1}$ 中：norm-one torus 的二阶平均只剩 $q(P)$ 的倍数，而 determinant-one normalizer 的另一 coset 把 $q(P)$ 送到 $-q(P)$。

四阶则保留。对任意 $w$，
$$
\frac1{|H'|}\sum_{h\in H'}\det(hP,w)^4
 =\frac{3}{8\delta^2}q(P)^2q(w)^2
       \quad\text{in }\mathbf F_p .
\tag{1143.14}
$$
为核尺度，在 $\mathbf F_{p^2}$ 取 $s^2=\delta$，写
$A(v)=y+sx$、$B(v)=y-sx$，则
$q(v)=A(v)B(v)$、$2s\det(v,w)=A(v)B(w)-B(v)A(w)$。
torus 把 $A(P),B(P)$ 乘 $t,t^{-1}$。
第四次幂中只有常项存活，其系数是
$6/(16\delta^2)=3/(8\delta^2)$；
另一个 coset 不改 $q(P)^2$。$p>37$ 排掉低次数与 torus 阶的碰撞。

$g^{-1}P$ 的两个坐标是
$\det(P,w),\det(v,P)$。将 (1143.14) 代入 (1143.12)，再用
$S$ 重指标和 $e_{gS}=-e_g$，得到
$$
\mathcal E_H(P)\in\lambda^4
      \bigl(L_{\mathbf Z_p}(Z)\otimes\mathcal O\bigr),\qquad
\lambda^{-4}\mathcal E_H(P)
 \equiv\frac{m^2q(P)^2}{2048\delta^2}\,C_E
       \pmod\lambda .
\tag{1143.15}
$$
具体地，四阶系数首先为
$q(P)^2(4096\delta^2)^{-1}
 \sum_{g/\pm}(q(w)^2-q(v)^2)e_g$；
两个和互为负号，故得 (1143.15)。
这里完整保留 $\mathrm{SL}_2/\{\pm1\}$ 与原 $1/(2m^2)$ 的区别。

$F(P)$ 在复嵌入中为实代数数，而 Banerjee–Merel 的实零周期空间具有上述有理结构，故 $\mathcal E_H(P)$ 属于有理 Eisenstein 空间的系数扩张；
饱和性遂使 (1143.15) 的除法仍在
$E_{\mathbf Z_p}(Z)\otimes\mathcal O$ 中。

## 5. 真正原 c_E 无条件属于 cuspidal p-torsion

从此固定 $P=e_2$，令
$$
\mathscr E=
 \frac1{(p+1)\lambda^4}\,f_*J_*\mathcal E_H(e_2)
 \in E_{\mathbf Z_p}(X)\otimes\mathcal O .
\tag{1143.16}
$$
$f_*J_*\mathcal E_{hP}=f_*J_*\mathcal E_P$，所以计算边界时只需原
$\mathcal E_P$ 一份；没有第二个平均因子。
由 $q(e_2)=1$ 及原同一 transfer，
$$
\overline{\mathscr E}
 =\frac{m^2}{2048\delta^2}\,c_E .
\tag{1143.17}
$$
右边已紧致，故 (1143.7)–(1143.8) 证明
$c_E$ 的 Betti 像无条件属于原 $C_\Sigma[p]$。
这一步只用真实整 Eisenstein 链和尖点格，不使用 Calegari 的 DVR 条件。

每个原 cusp $p$-torsion 角色都是偶角色，且 R1062 证明 trivial 角色缺席。
在角色 $\omega^r$ 上，Eichler–Shimura 与 good-reduction specialization 给
$$
T_\ell=\ell^r+\ell^{1-r}\qquad(\ell\ne p)
\tag{1143.18}
$$
的实际作用，方向同 R1131 的 arithmetic Frobenius。
与 (1143.4) 对所有 $\ell$ 比较，由 Dirichlet 与
$\mathbf F_p^\times$ 上不同角色的线性独立性，必须有
$\{r,1-r\}=\{-2,3\}$。唯一偶数解为 $r=-2$。
所以
$$
c_E\in C_\Sigma[p]_{\chi_1}
       \quad\text{无条件，}\qquad\chi_1=\omega^{-2}.
\tag{1143.19}
$$
此时允许取第2节的真实 cusp projector；不需要先假设
$c_E\ne0$，也没有把任何其他 Jacobian $p$-torsion 当作 cuspidal。

## 6. 原尖点 Galois 方向和边界首项

对任意 analytic full cusp vector $P$，在原 Cartan 商中记
$c(P)=f(JP)$。准确有
$$
c(\mu P)=\sigma_{\mu^{-2}}c(P).
\tag{1143.20}
$$
可以在 Tate cusp 直接核：scaling vector 对应
$\operatorname{diag}(\mu,\mu^{-1})$ 的标记变化；
去掉原 normalizer 内的共同 scalar $\mu$ 后，
剩余 $\operatorname{diag}(1,\mu^{-2})$，其常数作用为
$\zeta_p\mapsto\zeta_p^{\mu^{-2}}$。
等价地，full-level 中 central $\mu I$ 的函数域作用在常数上是
$\sigma_{\mu^2}$，且
$\operatorname{ord}_\infty((\mu I)f)
 =\operatorname{ord}_{\mu e_1}f$，
所以其对 analytic cusp 的逆作用是 (1143.20)。
中心与 $J$ 及任意 level 变换交换，故该式适用于每个 $P$。
这与 Carlucci 用 $\sigma^{-1}(\infty)$ 标记 cusp 的 convention 相同；
不能把 norm 标签直接当作无逆的 Galois 标签。

当 $P=e_2$，$c(P)=c_\infty$。因而
$$
e_{\chi_1}[c(\mu^{-1}P)]
 =\omega(\mu)^{-4}D_{\chi_1}.
\tag{1143.21}
$$
(1143.11) 的最后一个全 cusp 和在非平凡 projector 下为零。
因此
$$
\frac1p\partial(e_{\chi_1}\mathscr E)
 =\frac1{(p+1)\lambda^4}
   \sum_{\mu\ne0}\omega(\mu)^{-4}
       \left(F(\mu,0)+\frac14\right)D_{\chi_1}.
\tag{1143.22}
$$
全常数和严格为零。二阶及三阶项的整数 power sums 在模 $p$ 为零，
故除以 $\lambda^4$ 后仍有正赋值，因为 $v_\lambda(p)=p-1$。
四阶项中
$\sum_{\mu\ne0}\omega(\mu)^{-4}\mu^4\equiv-1\pmod p$。
于是 (1143.12) 精确给
$$
\frac1p\partial(e_{\chi_1}\mathscr E)
 \equiv-\frac{D_{\chi_1}}{1536(p+1)}
       \pmod\lambda .
\tag{1143.23}
$$
本式的左边整性也由下一节的
$\Lambda_{\chi_1}=p\mathbf Z_pD_{\chi_1}$ 得到。
这里没有在 $p$ 整格上将 $\lambda^4$ 误作 $p$。

## 7. S_{ω²}/p 与原函数的尺度

R1062 的原格给
$$
(C_\Sigma\otimes\mathbf Z_p)_{\chi_1}
 =\mathbf Z_p/(S_{\omega^2}),\qquad
S_{\omega^2}=-\frac14J(\omega^2,\eta)B_{2,\omega^4},
\quad \eta=\omega^{(p-1)/2}.
\tag{1143.24}
$$
Gauss 乘积准确给
$J(\omega^2,\eta)J(\omega^{-2},\eta)=p$。
模 $p$ 的反向 Jacobi 和只有一个 $p-1$ 次幂，故
$$
J(\omega^{-2},\eta)\equiv-\binom m2=-3/8,\qquad
J(\omega^2,\eta)/p\equiv-8/3.
$$
广义 Kummer 同余为
$B_{2,\omega^4}/2\equiv B_6/6=1/252$。
所以
$$
\boxed{\qquad S_{\omega^2}/p\equiv1/189\pmod p.\qquad}
\tag{1143.25}
$$
特别 $v_p(S_{\omega^2})=1$，该原 cusp 分量的整个 $p$-primary 阶恰为 $p$，且
$\Lambda_{\chi_1}=S_{\omega^2}\mathbf Z_pD_{\chi_1}=p\mathbf Z_pD_{\chi_1}$。

下面直接用实际 q-product 钉住 $D_{\chi_1}$ 的尺度。
在 $\mathbf Z_p$ 完成的原 augmentation-zero unit 格上用准确 Teichmüller 权
$n_h=m^{-1}\chi_1(h)^{-1}$。
它是原整数提升的同一模 $p$ 类，而不是定义新的函数。
原 raw product 在 $c_\infty$ 的阶为
$$
\operatorname{ord}_{c_\infty}f_{\chi_1}^{\rm raw}
 =\frac p{2m}\sum_{z/\{\pm1\}}
    \chi_1(Nz)^{-1}B_2(Tz/p)
 =\frac{S_{\omega^2}}m .
\tag{1143.26}
$$
其 divisor 纯属 $\chi_1$，而
$D_{\chi_1}=e_{\chi_1}[c_\infty]$ 在 $c_\infty$ 的系数为 $1/m$。
因此
$$
\operatorname{div}f_{\chi_1}^{\rm raw}
  =S_{\omega^2}D_{\chi_1},\qquad
P_{\chi_1}=\frac{mS_{\omega^2}}p[D_{\chi_1}]
          =\frac m{189}[D_{\chi_1}]
       \quad\text{in }C_\Sigma[p].
\tag{1143.27}
$$
这里第二个等号是模 $p$；$m$ 来自原
$u_{\chi_1}^m/A(u_{\chi_1})$，常数 $A$ 没有 divisor。
改变原整数指数提升只改变这个点一个 principal divisor，
所以 (1143.27) 是原固定 $P_{\chi_1}$ 的尺度。
不把 raw bar norm 的 $2$ 再乘入，也不把任意 $c_1$ 默认为这个解析尖点。

## 8. 负 Abel 号、两个归一因子和最终读数

由 (1143.19)，$e_{\chi_1}\overline{\mathscr E}
 =\overline{\mathscr E}$。
将 (1143.23) 代入 (1143.8) 的负 Abel 号，并用 (1143.17)，得到
$$
\frac{m^2}{2048\delta^2}c_E
 =\frac1{1536(p+1)}[D_{\chi_1}] .
\tag{1143.28}
$$
即
$$
c_E=\frac{4\delta^2}{3m^2(p+1)}[D_{\chi_1}].
\tag{1143.29}
$$
再代入原函数尺度 (1143.27)，
$$
c_E
 =\frac{252\delta^2}{m^3(p+1)}P_{\chi_1}
 =-2016\delta^2P_{\chi_1}
       \quad\text{in }J[p].
\tag{1143.30}
$$
最后只用了 $m\equiv-1/2$、$p+1\equiv1\pmod p$。
$2016=2^5\cdot3^2\cdot7$，故显示系数对 $p>37$ 为单位。
这证明 R1140 原指定端点非零，并把 §14.3 的条件式定位升级为无条件精确式。

本篇没有将 $c_E\ne0$ 升级为
$\Psi(c_E)\ne0$，没有移除 R1140 / R1139 对其他 target 部分的混合 Bernoulli 门，也没有决定 R1141–R1142 的 MW/Pic 或实际算术 cochain。
它支付的是同一个原 source 的整尺度和非零性。

## 9. 原始来源与核查范围

- D. Banerjee、L. Merel，*The Eisenstein cycles as modular symbols*，
  J. London Math. Soc. 98 (2018), 329–348，
  [DOI](https://doi.org/10.1112/jlms.12136)，
  [作者全文](https://arxiv.org/pdf/1609.04140)。
  亲读原定义、Theorem 1、Proposition 12、§9 的实际边界计算。
  本文 (1143.11) 从原定义按自己的路径方向自证，完整写出全 $\mu$ 与 $\mu/\{\pm1\}$ 的区别；不依赖将有理 retraction 中的 $1/p$ 直接约模 $p$。
- J. S. Milne，*Abelian Varieties*，v2.0 (2008)，
  [作者全文](https://www.jmilne.org/math/CourseNotes/AV.pdf)，
  §18，Theorems 18.2、18.4及其后 Abel–Jacobi 描述，
  印刷72–73页、PDF78–79页。
  第2节将所需整格及负号逐项证明。
- [R1062](R1062-original-full-nonsplit-cuspidal-kummer-descent.md)：
  完整 cusp/principal 格、真实 Galois 作用与 $S_\psi$。
- [R1064](R1064-original-cuspidal-cover-descent-and-auxiliary-character-visibility.md)、
  [R1070](R1070-original-cuspidal-labels-by-division-polynomial-values.md)：
  原 Siegel 指数、bar norm、leading 归一与完整 $m$ 尺度。
- [R1136](R1136-original-forced-compact-Manin-sources.md)、
  [R1140](R1140-original-low-weight-Manin-source-reduction.md)：
  同一 $J$、$H'$、实际 transfer、Manin 路径和原 Hecke 特征。

没有数学程序执行；本文所有有限和与整格比较均为纸面证明。
