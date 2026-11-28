# R1179：原 Gaussian CM 范数、圆单位与中间 Tate 矩

日期：2026-11-28（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。

**已证明，纸面，所有 $p>37$、$p\equiv3\pmod4$。**
本篇从 R1147 的同一个全点 theta 矩出发，沿 Gaussian CM
范数得到原未平均圆单位类。它给原四次矩中槽
$\mathcal J_p$ 的准确零判据，及八次矩中槽的相应判据。
没有把一个新矩分量增添为 actual good 角色，也没有假设
任何中央 correlation 为零。

先给出不涉及局部 Frobenius 坐标约定的实际类等式。
令 $I$ 为 Gaussian CM 自同态，$I^2=-1$，并用原 Weil pairing 定义
$q_I(v)=e_p(v,Iv)\in L_1=\mu_p$。将它作通常 symmetric-power
polarization，得到
$$
\boxed{\quad
(q_I^2)_*\mathsf M_4=-\frac12\gamma_3,\qquad
(q_I^4)_*\mathsf M_8=\frac52\gamma_5.
\quad}
\tag{GN.1}
$$
这里的 $\gamma_3,\gamma_5$ 是 R1147/R1148 的正 Kummer、
全轨道未平均圆单位类。两个系数均为 $p$ 单位。

在原 Gaussian 模型及原 Appell 核中，结论为
$$
\boxed{\quad
\mathcal J_p=0\ \Longleftrightarrow\ p\mid B_{p-3},\qquad
\mathcal A_{8,4}=0\ \Longleftrightarrow\ p\mid B_{p-5}.
\quad}
\tag{GN.2}
$$
$\mathcal A_{8,4}$ 是 R1168 的 syntomic 常数读数中
$\omega^4\eta^4$ 的系数；其定义和精确高 Hurwitz 读数在 §8 写出。
本篇证明零判据时不把该 syntomic 常数与另一约定下的
Hodge–Frobenius translation 无说明地等同。

## 1. 固定原全点矩、辅助 c 与正 Kummer 方向

记 $H=E[p]$、$L_j=\mu_p^{\otimes j}$。
原类严格是 R1147 (1147.1)
$$
\mathsf M_d=
\frac1{k_d(c)}
\operatorname{Cor}_{E[p]\setminus O\,/\,\operatorname{Spec}k}
 \bigl(P^d\otimes\kappa(\theta_c(P))\bigr),\qquad
k_d(c)=c^2-c^{-d},\qquad d=4,8.
\tag{GN.3}
$$
$\kappa$ 采用正根 cocycle $\sigma(\sqrt[p]{u})/\sqrt[p]{u}$。
原 theta 的 divisor 为 $c^2[O]-[E[c]]$，保原 trace-fixed
规范和全部有序非零点，不除 $p^2-1$、$4$ 或 $d!$。

R1147 §1 已证明该类与辅助数无关。本篇选一个辅助素数
$c\equiv1\pmod{12}$，且 $c\bmod p$ 为 primitive root；
CRT 与 Dirichlet 定理保证这样的 $c$。
于是 $c$ 与 $6p$ 互素，$k_4(c),k_8(c)$ 为 $p$ 单位。
这个选择还使 theta 在 Gaussian 的 $\mu_4$ 下作为函数不变。
特别，本篇不把 $\theta_2(P_0)$ 未经处理就称为 ray-field 元素：
在原短模型中 $\theta_2$ 的 $\mu_4$ 相位确实可能非平凡。
最后由 (GN.3) 的实际辅助独立性返回原 $c=2$ 读取。

圆单位规范为
$$
\begin{aligned}
\gamma_{r+1}
 &=\operatorname{Cor}_{\mathbb Q(\zeta_p)/\mathbb Q}
   \bigl(\kappa(1-\zeta_p)\otimes\zeta_p^{\otimes r}\bigr),\\
\gamma_{r+1}|_{\mathbb Q(\zeta_p)}
 &=\left(\sum_{b\in\mathbb F_p^\times}
        b^r\kappa(1-\zeta_p^b)\right)\otimes\zeta_p^{\otimes r},
 \qquad r=2,4 .
\end{aligned}
\tag{GN.4}
$$
换 $\zeta_p$ 为 $\zeta_p^a$ 时，加权和乘 $a^{-r}$，
Tate tensor 乘 $a^r$，所以 (GN.4) 不变。

## 2. 原 theta 的 Gaussian 复解析表达式

置 $K=\mathbb Q(i)$、$\mathcal O_K=\mathbb Z[i]$。
先取一个标准 Gaussian CM 曲线
$E_0(\mathbb C)=\mathbb C/(\Omega\mathcal O_K)$，
$P_0=\Omega/p$，并记 $P_v=vP_0$。
同构缩放不会改变原 weight-zero theta。

在面积一格 $\mathcal O_K$ 上取 $\sigma'(0)=1$ 的 Weierstrass
sigma。它满足
$$
\sigma(iz)=i\sigma(z),\qquad \eta_1=\pi,\quad\eta_i=-i\pi.
$$
因此
$$
F(z)=\log|\sigma(z)|^2-\pi|z|^2
\tag{GN.5}
$$
是 $\mathcal O_K$-周期函数，$F(iz)=F(z)$，
且在零点有主部 $\log|z|^2$。
其分布 Laplacian 为
$$
\Delta F=4\pi(\delta_0-1).
\tag{GN.6}
$$
对 $c$ 为奇数，$\sigma(z)^{c^2}/\sigma(cz)$ 是真正椭圆函数，
divisor 正是 $c^2[0]-[c^{-1}\mathcal O_K/\mathcal O_K]$。
它在 $z\mapsto iz$ 下的因子为 $i^{c^2-1}=1$。

Kato theta 的相同 divisor、distribution 和 base-change 规范
给其与该 sigma ratio 相差一个共同常数。故
$$
\log|\theta_c(P_v)|^2
 =c^2F(v/p)-F(cv/p)+C_c .
\tag{GN.7}
$$
二次 completed 项精确相消。
下面每个加权和的 augmentation 都为零，因而 $C_c$ 精确消去；
没有为不同 $v$ 单独选择 leading constant。

## 3. shifted Epstein 的符号由热核与 Laplacian 自证

对 $z\notin\mathcal O_K$ 定义
$$
Z(z,s)=\sum_{\lambda\in\mathcal O_K}|\lambda+z|^{-2s}.
$$
设 $\Theta_z(t)=\sum_\lambda e^{-\pi t|\lambda+z|^2}$。
Poisson 公式给
$$
\Theta_z(t)=t^{-1}
 \sum_{m,n\in\mathbb Z}e^{-\pi(m^2+n^2)/t}
                e^{2\pi i(m\operatorname{Re}z+n\operatorname{Im}z)}.
$$
将 Mellin 积分在一处分开，并在小 $t$ 一端减去 $t^{-1}$，得到
$$
Z(z,s)=\frac{\pi^s}{\Gamma(s)}
 \left\{
 \int_1^\infty t^{s-1}\Theta_z(t)\,dt+
 \int_0^1t^{s-1}\bigl(\Theta_z(t)-t^{-1}\bigr)\,dt+
 \frac1{s-1}
 \right\}.
\tag{GN.8}
$$
两段积分在 $s=0$ 附近全纯；这直接给
$Z(z,0)=0$、$\operatorname{res}_{s=1}Z(z,s)=\pi$。
另一方面，在原收敛半平面逐项微分后作解析延拓，
$$
\Delta_z Z(z,s)=4s^2Z(z,s+1).
$$
因此 $z$ 离开格点时 $\Delta Z'(z,0)=4\pi$。
分离 $\lambda=0$ 的一项，还给
$Z'(z,0)=-\log|z|^2+O(1)$。

由 (GN.5)–(GN.6)，$Z'(z,0)+F(z)$ 是紧复 torus 上
无奇点的调和函数，故为常数：
$$
\boxed{\qquad Z'(z,0)=-F(z)+C.\qquad}
\tag{GN.9}
$$
这是本文所需的 shifted second-limit 身份及其负号的完整证明。
若将 Poisson 的欧氏相位改写为 alternating 格相位，
$mx+ny=\operatorname{Im}(iz\,\overline{m+in})$，
theta 参数写成 $iz$；(GN.5) 的 $F(iz)=F(z)$ 使两写法相同。
因此没有由该旋转引入字符的反向或未知相位。

对 $v\in(\mathcal O_K/p)^\times$，令
$$
Z_v(s)=\sum_{\alpha\equiv v\ (p)}N(\alpha)^{-s}
      =p^{-2s}Z(v/p,s).
$$
因为 $Z(v/p,0)=0$，(GN.9) 仍给
$Z_v'(0)=-F(v/p)+C$，没有额外的 $\log p$ 项。

## 4. 全点的四与圆单位的四，平滑反向由真实重指标锁定

令 $\chi$ 为非平凡偶 Dirichlet 字符，conductor 为 $p$。
$K$ 的 class number 为一，每个非零整 ideal 恰有四个生成元，
故原收敛半平面有
$$
4L_K(s,\chi\circ N)
 =\sum_{v\in(\mathcal O_K/p)^\times}\chi(Nv)Z_v(s).
$$
由 (GN.9) 及 $\sum_v\chi(Nv)=0$，
$$
\sum_v\chi(Nv)F(v/p)=-4L_K'(0,\chi\circ N).
$$
在 (GN.7) 的第二项作真实替换 $v\mapsto cv$，得到
$$
\boxed{
\sum_v\chi(Nv)\log|\theta_c(P_v)|^2
 =-4\bigl(c^2-\chi(c^2)^{-1}\bigr)
                  L_K'(0,\chi\circ N).
}
\tag{GN.10}
$$
这里的逆号来自标签重指标；不从某个 Artin-symbol 约定猜测。
加权使用 $\chi$，所得 unit component 的 Galois 角色是
$\chi^{-1}$。

记 $\epsilon=\chi_{-4}$。逐个 rational prime 的 Euler factors 给
$$
L_K(s,\chi\circ N)=L_{\mathbb Q}(s,\chi)L_{\mathbb Q}(s,\chi\epsilon).
$$
因为 $\chi$ 非平凡且偶，$L_{\mathbb Q}(0,\chi)=0$，
于是
$$
L_K'(0,\chi\circ N)
 =L_{\mathbb Q}'(0,\chi)L_{\mathbb Q}(0,\chi\epsilon).
\tag{GN.11}
$$
圆单位的对应规范是
$$
\sum_{b\ne0}\chi(b)\log|1-\zeta_p^b|^2
 =-4L_{\mathbb Q}'(0,\chi).
\tag{GN.12}
$$
例如由
$L(s,\chi)=p^{-s}\sum_b\chi(b)\zeta(s,b/p)$、
$\zeta'(0,x)=\log\Gamma(x)-\tfrac12\log(2\pi)$，
再把 $b,p-b$ 配对并用 Gamma reflection，即得 (GN.12)。
这里仍是全部 $p-1$ 个标签，而不是半点平均。
(GN.10) 与 (GN.12) 的两个四精确相消。

## 5. 真正 ray norm、全部嵌入与 p-local 根单位核

令 $F_p^{\rm ray}=K(p)$，$L=K(\zeta_p)$。
CM reciprocity 给
$$
G=\operatorname{Gal}(F_p^{\rm ray}/K)
 \simeq(\mathcal O_K/p)^\times/\mu_4,\qquad
G\longrightarrow\operatorname{Gal}(L/K)=\mathbb F_p^\times,\quad
[v]\longmapsto Nv .
\tag{GN.13}
$$
$\theta_c(P_0)\in F_p^{\rm ray}$，其 conjugates 为
$\theta_c(P_v)$、$v$ 按 $\mu_4$ 取商。
这使用 §1 中 $\mu_4$-不变的实际 theta，非只使用绝对值。

此处的方向还可从原格直接检查。
对与 $6cp$ 互素的 principal ideal $(a)$，CM reciprocity
把 $(p,c^{-1}p)$ 变成 $(a^{-1}p,a^{-1}c^{-1}p)$；
同时缩放格把其 theta 值变成原 $aP_0$ 处的值。
该 automorphism 在 $\zeta_p$ 上为 $\zeta_p\mapsto\zeta_p^{Na}$。
因此 (GN.13) 与 (GN.10) 的实际标签方向相同。

记
$$
H=\ker(N)/\mu_4,\quad |H|=(p+1)/4,\qquad
U_c=N_{F_p^{\rm ray}/L}\theta_c(P_0).
$$
在 unit 群的加法记号中，
$$
\sum_{v\ne0}\chi(Nv)[\theta_c(P_v)]
 =4\sum_{b\in\mathbb F_p^\times}\chi(b)\sigma_b[U_c].
\tag{GN.14}
$$
这是完整 norm；没有反除 norm-one 轨道的 degree。
Flach Lemma 2.2 的 integrality 部分说明这些值在 $p$ 外为单位。
$L$ 在 $p$ 上只有一个素点，故其 valuation 模块为平凡角色。
非平凡的 $\chi^{-1}$ 分量因而属于普通 unit 格。

下面说明不能省略的从复对数回到整 Kummer 的步骤。
取字符值域 $B=\mathbb Q(\chi)$。
由 (GN.10)–(GN.12)，
$$
\frac1{c^2-\chi(c^2)^{-1}}
       \sum_v\chi(Nv)[\theta_c(P_v)]
 -L_{\mathbb Q}(0,\chi\epsilon)
       \sum_{b\ne0}\chi(b)[1-\zeta_p^b]
\tag{GN.15}
$$
的 archimedean regulator 为零。
这不是只检查一个复数：对 $B$ 的每个嵌入重作同一
$\chi$ 的共轭公式，再对 $\sigma_b\in\operatorname{Gal}(L/K)$
重指标，得到所有 regulator 坐标为零。
$\operatorname{Gal}(L/K)$ 在 $L$ 的复 places 上传递；
复共轭的成对绝对值已包括在这些坐标中。
Dirichlet regulator 对普通 units 模 roots of unity 单射，
故 (GN.15) 在 $L^\times\otimes B$ 中为零。

现选 $B$ 在 $p$ 上的素点，使 $\chi\bmod p=\omega^r$，
$r=2$ 或 $4$。
平滑因子模 $p$ 是 $c^2-c^{-2r}=k_{2r}(c)$，为单位。
下一节证明 $L(0,\chi\epsilon)$ 为 $p$-整。
所以 (GN.15) 的两项原本就在 $p$-local
$\chi^{-1}$-unit 格中。
该格的 rationalization kernel 只有 roots of unity；
prime-to-$p$ roots 在此已被消掉，而 $p$-primary roots 的
Galois 角色为 $\omega$，不同于 $\omega^{-2}$、$\omega^{-4}$。
于是该 kernel 在本分量为零。

因此得到真正的整 unit 等式
$$
\boxed{
\frac1{c^2-\chi(c^2)^{-1}}
 \sum_v\chi(Nv)[\theta_c(P_v)]
 =
 L_{\mathbb Q}(0,\chi\epsilon)
       \sum_{b\ne0}\chi(b)[1-\zeta_p^b]
}
\tag{GN.16}
$$
在所指定的 $p$-local $\chi^{-1}$ 格中成立。
这一步不需要圆单位在全部 unit 格中的 index 为单位：
比较的是两份已在同一格中的元素，相等在 rationalization 后
由无 $p$-torsion 的本分量拉回。
也没有把未核准的 $\mu_p$ 相位默删。

## 6. 两个 Euler 因子的确切模 p 值

用 conductor $4p$ 的通常 Bernoulli 公式，
$$
L_{\mathbb Q}(0,\chi\epsilon)
 =-\frac1{4p}\sum_{a\bmod4p}a\,\chi(a)\epsilon(a).
$$
对每个 $b\ne0\bmod p$，取唯一的奇数 $a_b\in[1,2p)$、
$a_b\equiv b\bmod p$。
另一个奇数 lift 是 $a_b+2p$，它的 $\epsilon$ 号相反。
两项合成 $-2p\,\chi(b)\epsilon(a_b)$，故整地有
$$
L_{\mathbb Q}(0,\chi\epsilon)
 =\frac12\sum_{b\ne0}\chi(b)\epsilon(a_b).
\tag{GN.17}
$$
特别已付 $p$-整性，没有把含 $1/p$ 的式子直接约模 $p$。

对 $\chi\bmod p=\omega^r$、$r=2,4$，
$$
2L_{\mathbb Q}(0,\chi\epsilon)
 \equiv\sum_{j=0}^{p-1}(-1)^j(2j+1)^r\pmod p.
$$
其中 $2j+1=p$ 的一项为零。
只在次数小于 $p$ 的有限指数级数中使用
$$
\sum_{j=0}^{p-1}(-1)^j e^{(2j+1)T}
 =\frac{e^T(1+e^{2pT})}{1+e^{2T}}
 \equiv\operatorname{sech}T\pmod{(p,T^p)}.
$$
$T^2/2!$、$T^4/4!$ 的系数分别是 $-1,5$，所以
$$
\boxed{\qquad
L(0,\omega^2\epsilon)\equiv-\frac12,\qquad
L(0,\omega^4\epsilon)\equiv\frac52\pmod p.
\qquad}
\tag{GN.18}
$$
这里 $\omega^r$ 表示所选 Teichmüller lift；公式不靠小素数选号。

## 7. 返回原全点 moment 与实际 Tate 类

把 Weil pairing 写为相对于一个 $\zeta_p$ 的加法值。
若 $P_v=(a+bI)P_0$，则
$$
q_I(P_v)=N(v)\,q_I(P_0).
\tag{GN.19}
$$
这是由 $I^\vee=-I$ 和 Weil pairing 的 bilinearity 直接得到的
Gaussian norm form。

在标准 analytic basis $(\Omega/p,i\Omega/p)$ 中，
$q_I(P_0)=e_p(P_0,IP_0)$ 是 $e^{2\pi i/p}$ 或其 inverse；
唯一的二者差别取决于原 Weil orientation。
$r=2,4$ 为偶数，故这个号在 $q_I^r$ 中消失。
若原固定 $\zeta_p$ 是另一 primitive root，
(GN.4) 的重指标与 Tate tensor 同时运输，仍不产生额外单位。

在全点 splitting field 上，对 (GN.3) 施 $q_I^r$，
正好得到 (GN.16) 约模 $p$ 后再乘 $\zeta_p^{\otimes r}$。
结合 (GN.18)，就是 (GN.1)。
所有 restriction 域的 degree 都与 $p$ 互素：
Gaussian CM 的 $p$-torsion 像在 Cartan normalizer 内，
ray 部分的 degree 为 $(p^2-1)/4$。
所以 restriction 的单射把等式送回原底。

$I$ 在复共轭下变成 $-I$，而 $q_I^2,q_I^4$ 不变，
故两 coefficient maps 本身定义在 $\mathbb Q$ 上。
任意 Gaussian twist 与标准模型在 degree 至多四的扩域后同构；
原 theta、Weil pairing、全点 trace 与 CM map 都与该同构相容。
再次用 prime-to-$p$ restriction/corestriction，得到同一
Gaussian 原 fibre 上的 (GN.1)。
这包括本篇使用的原 good $p$-adic CM reference。

## 8. 原 de Rham 中槽、极化系数与真正的非零判据

取原模型
$$
E:\ y^2=x^3+ax,\qquad
\omega=dx/(2y),\quad\eta=x\omega,\quad
\beta=C_{\rm rel}(x\omega)/\omega'=-\delta\in\mathbb F_p^\times .
$$
沿 R1163 (1163.5)，$H$ 与 $H^1_{\rm et}(E)(1)$ 的识别
是第一槽 $v\mapsto e_p(v,-)$。
因此 CM 的 covariant $I$ 在该 cohomological realization 中
对应 $-I^*$，不能未经说明把两者当成同一个作用。
实际 $\omega,\eta$ 两条 CM 线的特征值仍是一对相反的 $\pm i$。

在这一已固定的整比较中，定义唯一的 $C$ 为
$$
q_{I,\rm dR}(x\,\omega\tau_1+y\,\eta\tau_1)
 =Cxy\,\tau_1 .
\tag{GN.20}
$$
它不是可自由选择的缩放。
原 cup/Weil pairing 在 $(\omega,\eta)$ 中完美，
所以 $C\ne0$。若其 trace 单位记为 $c_\omega$，
则第一槽/对偶 convention 至多改变 $C$ 的号，并有
$C^2=-4c_\omega^2$；特别不把该平方改成 $+4c_\omega^2$。
两条 CM 本征线各向同性，故纯 $\omega^2$、$\eta^2$ 项为零。

按 ordinary symmetric-power polarization，
$$
\begin{aligned}
q_I^2(\omega^2\eta^2\tau_1^5)&=\frac{C^2}{6}\tau_1^3,\\
q_I^4(\omega^4\eta^4\tau_1^9)&=\frac{C^4}{70}\tau_1^5.
\end{aligned}
\tag{GN.21}
$$
其余对应次数的 monomials 均映到零。
分母 $6=\binom42$、$70=\binom84$ 来自纯幂展开，
与 (GN.3) 没有 $d!$ 的规范一致。

R1168 (1168.28)–(1168.29) 的原 syntomic 常数读取给
$$
\begin{aligned}
\mathcal A_{4,2}
 &=2\beta^2G_{p^2-2p-3}
   =-\frac{\mathcal J_p}{2\beta},\\
\mathcal A_{8,4}
 &=14\beta^4G_{p^2-4p-5}.
\end{aligned}
\tag{GN.22}
$$
第一行最后一步是原 Gaussian two-digit note
(G2.39)、(G2.45)；该 note (G2.53) 也给
$$
\mathcal A_{8,4}
 =-\frac7{3\beta}[v^{p-5}]C_6(v).
\tag{GN.23}
$$
所有系数都有原整来源；这里没有把 $p^2$ 高权反射未经证明地
换成低权值。

R1163 的实际 tensor comparison 保 (GN.21)，
原未分歧 FL 范围足以比较两个 abelian quotients 和这些
coefficient maps。输出是 $L_3,L_5$，其局部有限 $H^1$
均为一维；(GN.21) 中的 scalars 是单位。
所以 (GN.1) 与 (GN.22) 直接给
$$
\begin{aligned}
\mathcal J_p=0
 &\Longleftrightarrow \operatorname{loc}_p(\gamma_3)=0,\\
\mathcal A_{8,4}=0
 &\Longleftrightarrow \operatorname{loc}_p(\gamma_5)=0.
\end{aligned}
\tag{GN.24}
$$
这里使用零/非零的 functorial 判据，
不依赖把 syntomic cone 的第二槽 $(0,m)$
命名为正向或反向 Hodge–Frobenius translation。
两种命名之间的数值负号必须由原 Kummer/period 字典另行运输；
本篇不以未支付的该符号给出 $\mathcal J_p=\pm\beta B_{p-3}$
之类的数值简式。

## 9. Bernoulli 判据对全部 p 的局部证明

令 $\chi_0=\omega^{-r}$，$r=2,4$，并置 $n=p-1-r$。
选 R1069 的原圆单位
$$
\eta_b=\zeta_p^{(1-b)/2}\frac{1-\zeta_p^b}{1-\zeta_p},
\qquad \beta_{\chi_0}=e_{\chi_0}[\eta_b].
$$
原 R1148 (1148.23) 的同一 projector 计算给
$$
\beta_{\chi_0}
 =(1-b^{-r})\sum_{a\ne0}a^r[1-\zeta_p^a].
\tag{GN.25}
$$
取 $b$ 使 $b^n\ne1$，则前因子为单位。
R1069 (1069.15) 的真实有限对数 leading coefficient 是
$$
\frac{B_n(b^n-1)}{n\,n!}.
\tag{GN.26}
$$
这一判据的 converse 也在当前局部角色内成立，说明如下。
在 $\mathbb Q_p(\zeta_p)$ 取 $\lambda=\zeta_p-1$。
$\log:1+\lambda^2\mathcal O\to\lambda^2\mathcal O$
是整群同构，$p$ 次方对应乘 $p$，
因而本单位 quotient 为
$\lambda^2\mathcal O/p\lambda^2\mathcal O$。
其 filtration indices 为 $2,\ldots,p$，
相应 graded characters 是 $\omega^j$。
非平凡偶角色 $\omega^n$ 在这些 indices 中只出现一次，即 $j=n$。
valuation 与 $\mu_p$ 的例外分别为平凡角色与 $\omega$，
不属于本角色。
所以这个一维 local Kummer 分量的 leading map 在 index $n$
是同构；(GN.26) 为零恰好等价于原局部类为零。

于是
$$
\operatorname{loc}_p(\gamma_{r+1})=0
 \ \Longleftrightarrow\ B_{p-1-r}\equiv0\pmod p,
\qquad r=2,4.
\tag{GN.27}
$$
这只使用局部 finite Kummer 与原有限对数，
没有使用 sufficiently-large-$p$ 的全局生成性。
结合 (GN.24) 得到 (GN.2)，对全部 $p>37$ 成立。

## 10. 对原 actual-mask 剩余分支的严格后果

原 Gaussian two-digit note (G2.42) 已付
$$
\mathcal J_p
 =\left[\frac16\partial^2\mathcal H_p
              -\frac{13a}{18}\mathcal H_p\right]_{b=0}.
$$
因此，在原 remaining good 分支 $p\nmid B_{p-3}$ 中，
$$
\boxed{\qquad
\mathcal H_p(a,0)=0
 \ \Longrightarrow\ 
(\partial^2\mathcal H_p)(a,0)\in\mathbb F_p^\times .
\qquad}
\tag{GN.28}
$$
这里的 $\partial$ 是原模参数 heat 导子，
先作用于完整 $(a,b)$ 多项式，最后取 $b=0$。
这不是沿函数域参数的导数。

此外，若原分支还有 $p\nmid B_{p-5}$，则
$$
[v^{p-5}]C_6(v)\ne0
\tag{GN.29}
$$
由 (GN.23)–(GN.27) 成立。
两条结论都来自原实际矩与原圆单位，不是另找的旁系数。

本文没有证明原 $\Delta_{\rm low}$ 非零，
没有把 (GN.28) 自动变成所有 good 行分离，
也没有将任一原中央 correlation 置零。
完整 Bernoulli mask、原两点及两 twist 的已付运输继续保留；
下一步仍须把这些实际非零输入作用于原联合条件。

## 来源与准确使用位置

- M. Flach, *Iwasawa Theory and Motivic L-functions*,
  **Pure and Applied Mathematics Quarterly 5 (2009), 255–294**，
  [正式 PDF](https://intlpress.com/site/pub/files/_fulltext/journals/pamq/2009/0005/0001/PAMQ-2009-0005-0001-a008.pdf)，
  [作者机构书目](https://resolver.caltech.edu/CaltechAUTHORS:FLApamq09)。
  使用 §2.2.2 Lemma 2.1 的原 theta divisor/norm/base change，
  §2.2.3 Lemma 2.2(a)–(c) 的 CM rationality、integrality、
  Galois action，以及其后 Remark 的实际 CM 点标签。
  本文 §3 自证所需 shifted limit 公式及符号，
  不按 Lemma 2.2(e) 的字符约定猜测 (GN.10) 的 inverse。
  正式端点读取受限时，亲读的是
  [同作者全文镜像](https://studylib.net/doc/7931909/iwasawa-theory-and-motivic-l-functions---mathematics)，
  对应作者稿 §§2.1–2.2.3、印刷稿 261–267 页。
- [R1147](../results/R1147-original-canonical-moment-Heisenberg-lift.md)
  §1、§§8–11：原全点 moment、辅助独立性、正圆单位及同根塔。
- [R1148](../results/R1148-original-canonical-cusp-Heisenberg-and-minus-one-Frobenius.md)
  (1148.23)、(1148.27)：原未平均 $\gamma_3,\gamma_5$ 与圆单位 projector。
- [R1069](../results/R1069-all-prime-good-cuspidal-characters-and-unique-global-labels.md)
  (1069.14)–(1069.16)：原有限对数、Bernoulli index 及局部角色。
- [R1163](../results/R1163-original-highest-moment-integral-syntomic-comparison.md)
  (1163.5)、§§3–4：实际第一槽 Weil 与整 tensor comparison。
- [R1168](../results/R1168-original-unramified-PD-contraction-and-CM-moment-readout.md)
  (1168.25)、(1168.28)–(1168.29)：原两矩的 syntomic 常数读取。
- [原 Gaussian two-digit note](../notes/2026-11-28-original-Gaussian-two-digit-Hurwitz-reduction.md)
  §§10–11：(G2.39)、(G2.42)、(G2.45)、(G2.53) 的
  全 carry 反射及原 heat 接口。

全篇没有数学程序执行，没有用小素数例子选择符号。


## 11. 接入正向 Frobenius 后的两个准确中槽数值

[R1177](R1177-original-syntomic-to-Frobenius-sign-dictionary.md)
(1177.1)、(1177.19) 已用原正 Kummer、左扭曲及同一个 Hodge
截面核定：若 $S_d$ 是 R1168 的 syntomic 常数向量，
真正的正向 Frobenius 一次向量是
$$
\mathsf A_d^\Phi=-S_d.
\tag{GN.30}
$$
这不改变原 $H^0$ Weil coefficient、全点矩或 (GN.1) 的类。
本节在这份已经固定的字典下支付 §8 暂未数值认同的最后一步。

仍用 (GN.20) 定义的同一个整单位 $C$，记
$$
\mathcal K_p=[v^{p-5}]C_6(v),\qquad
\beta_3^{\rm B}=\overline{B_{p-3}},\qquad
\beta_5^{\rm B}=\overline{B_{p-5}}.
$$
这里 $\beta=C_{\rm rel}(x\omega)/\omega'$ 继续是 Gaussian
Cartier 单位；两个带上标的量只是 Bernoulli 数的约化。
$v$ 是原 tangent-one 核参数。

由 (GN.22)–(GN.23) 和 (GN.30)，真正两个中槽为
$$
\boxed{\qquad
\mathsf A_{4,2}^\Phi=\frac{\mathcal J_p}{2\beta},
\qquad
\mathsf A_{8,4}^\Phi=\frac{7\mathcal K_p}{3\beta}.
\qquad}
\tag{GN.31}
$$
因此不能把 (GN.22) 的两个 syntomic 系数直接代入正向
Frobenius 的全局 labels。

令 $r,s$ 分别是原 $\gamma_3,\gamma_5$ 在 R1151/R1152
Tate frame 内的正向 Frobenius 一次坐标。
R1152 (1152.51) 已在同一未平均正 Kummer 规范中证明
$$
r=\frac23\beta_3^{\rm B},\qquad
s=\frac{24}{5}\beta_5^{\rm B}.
$$
这些是全局类比较后得到的实际坐标；即使其中一个局部类为零，
公式仍然成立，不需用非零局部值来选择一个缩放。
这里的 $r,s$ 已经是 physical 坐标，按 R1177 §5.2 不再取负。

现在对原类等式 (GN.1) 使用同一整 tensor comparison。
(GN.21)、(GN.31) 逐项给
$$
\frac{C^2}{6}\frac{\mathcal J_p}{2\beta}=-\frac r2,
\qquad
\frac{C^4}{70}\frac{7\mathcal K_p}{3\beta}=\frac{5s}{2}.
$$
于是准确得到
$$
\boxed{\begin{aligned}
\mathcal J_p
 &=-\frac{6\beta r}{C^2}
  =-\frac{4\beta}{C^2}\,\overline{B_{p-3}},\\
\mathcal K_p
 &=\frac{75\beta s}{C^4}
  =\frac{360\beta}{C^4}\,\overline{B_{p-5}}.
\end{aligned}}
\tag{GN.32}
$$
全部只反除已固定的 $C,\beta$ 和 $p$ 单位整数。
特别，本式不附加 $\beta_3^{\rm B}\beta_5^{\rm B}\ne0$ 的条件。

若用 §8 同一 cup/Weil trace 单位 $c_\omega$ 写
$C^2=-4c_\omega^2$，则 (GN.32) 等价于
$$
\boxed{\qquad
\mathcal J_p=\frac{\beta}{c_\omega^2}\,
                 \overline{B_{p-3}},\qquad
\mathcal K_p=\frac{45\beta}{2c_\omega^4}\,
                 \overline{B_{p-5}}.
\qquad}
\tag{GN.33}
$$
这里没有把 $c_\omega$ 改成任选的正负平方根；
其平方来自原 pairing 和原微分基。
同样，$I\mapsto-I$ 或反向 Weil orientation 改变 $C$ 的号，
不改变 (GN.32)–(GN.33)。

最后，把 (GN.32) 代回 (GN.28) 之前的原 heat 恒等式，得到
$$
\boxed{\qquad
(\partial^2\mathcal H_p)(a,0)
=\frac{13a}{3}\mathcal H_p(a,0)
 -\frac{24\beta}{C^2}\,\overline{B_{p-3}}.
\qquad}
\tag{GN.34}
$$
它仍是先对完整 $(a,b)$ 多项式作用、最后取 $b=0$ 的式子。
在原 $\mathcal H_p=0$、$p\nmid B_{p-3}$ 分支，
右边第二项准确为非零，而非只给一个未知非零倍数。

本节只把同一原类的符号与数值运输完毕。
它不将 $\mathcal J_p$ 认成低行 $c_2$，不增加一个 good 行，
也不把原 $\Delta_{\rm low}$ 或任何中央 correlation 的零性
改写为 (GN.32) 的中槽零性。原联合纤维问题继续保其完整条件。
全篇仍为纸面证明，无数学程序执行。
