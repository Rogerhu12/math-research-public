# R1071：完整原曲线的实际 p-local cuspidal 标签多项式

日期：2026-11-27（Asia/Taipei）。
会话：Astra-serre-24b8836b-20261126；global_route，o2 独立纸核。

**已证明。** 对每个 $p>37$，在完整原曲线 $X_{\rm ns}^+(p)$ 的每个
实际 $p$-local smooth component 上，原 cuspidal $p$-Kummer 标签的每个
非零角色都有一个显式的、次数小于 $p$ 的完整模 $p$ 多项式。
其系数来自同一个实际 supersingular reference 的有限 division-polynomial
Taylor 数据；保留 full-$p$ 参数、Cartan 标记、Weil root 和 circular-unit
尺度。公式覆盖整个实际 $V=C_\Sigma[p]$，不只 forced 子模块。

在 R1069 的 Bernoulli-good 角色上，除以明确非零的原 circular-unit 系数，
就得到该 $p$-local 标签的**唯一全局候选**在原单位基中的坐标。
这使 R1065–R1066 的有限候选集有了真实的有限系数读法。
尚未证明这些候选在有效辅助素处只剩全局 CM 标签。

本文全部是纸面证明；未运行数学程序，也未触发 CI。

## 1. 原角色、原单位及归一化

设
$$
X=X_{\rm ns}^+(p),\qquad
F=\mathbf Q(\zeta_p)^+,\qquad
G=\mathbf F_p^\times/\{\pm1\},\qquad
m=(p-1)/2,\qquad e=p^2-1.
\tag{1071.1}
$$
使用 R1062 的真实模块 $V=U_p/pU\simeq C_\Sigma[p]$，
以及同一全部 cusp leading-coefficient 归一化 $\Phi$。
R1070 §10 已证明实际 $V$ 没有 $\chi^2=1$ 分量。
因此每个非零角色唯一写成
$$
\chi=\omega^R,\qquad
2\le R\le p-3,\quad R\text{ 为偶数},\quad R\ne m.
\tag{1071.2}
$$
这里并未声称 (1071.2) 中每个角色都出现；只对实际 $V_\chi\ne0$ 使用它。

选择一个奇数 $c$，满足 $(c,6p)=1$，且其模 $p$ 类生成
$\mathbf F_p^\times$。置
$$
\kappa_\chi=c^2-\chi(c^2).
\tag{1071.3}
$$
R1070 §10 对整个实际 $V$ 证明 $\kappa_\chi$ 是 $p$-单位。
若 $n_h\in\mathbf Z$ 是该文保留的原 exponent lift，
则
$$
\sum_{h\in G}n_h=0,\qquad
n_h\equiv \frac1m\chi(h)^{-1}\pmod p.
$$
在同一原 $\mathbf F_{p^2}$-Cartan 标记中定义
$$
M_\chi=\prod_{v\in\mathbf F_{p^2}^\times/\{\pm1\}}
          \psi_c(P_v)^{-n_{[Nv]}}.
\tag{1071.4}
$$
此处 $\psi_c$ 是原椭圆曲线的 division polynomial，
$P_v$ 是该标记下的实际非零 $p$-torsion。
R1070 已逐相位证明 $M_\chi\in F(X)^\times$，其总 cusp leading 类是
$p$ 次幂，并且
$$
\Phi_y(u_\chi)=\frac m{\kappa_\chi}[M_\chi(y)]
       \quad\text{in }F_{\mathfrak p}^\times/F_{\mathfrak p}^{\times p}.
\tag{1071.5}
$$
不对 Siegel products 取 $12p$ 次幂；不替换原 $u_\chi$ 的尺度。

以下记
$$
N=(p+1)R,\qquad
I=\left\lfloor\frac{N}{p-1}\right\rfloor
=\begin{cases}R,&R<m,\\ R+1,&R>m,\end{cases}
\qquad d_i=N-(p-1)i.
\tag{1071.6}
$$
于是
$$
0<N<e,\qquad I\le p-2,\qquad
d_I=\begin{cases}2R,&R<m,\\2R-(p-1),&R>m,\end{cases}>0.
\tag{1071.7}
$$

## 2. 同一个实际 supersingular reference 和两个尺度

固定 R1065 的一个 $\mathbf F_p$-rational supersingular 标记 $s$。
先在原 prime-to-$p$ fine 问题上工作，选 R1066 §3–4 的实际
arithmetic-stable、不分歧二次 CM reference。
其 good deformation 参数记为 $u$，reference 是 $u=0$。
原 $\mathbf Q_p$ good deformation 写成
$$
u=pt,\qquad t\in\mathbf Z_p
\tag{1071.8}
$$
；额外 automorphism 的全部下降支路在 §8 保留。

取足够大的不分歧系数环 $W$，并在同一 full-level extension 中选
$$
\varpi^e=p,\qquad \rho=\varpi^{p-1},\qquad \rho^{p+1}=p.
\tag{1071.9}
$$
$\rho$ 是 R1066 的 EP finite-point 尺度。
不能将它换成一个 $(p-1)$ 次根；两者给不同的 normal 次数。

使用 R1021 的**同一个** universal formal-group eigenparameter $T$。
它满足 $x=T(P),y=T(Q)$，framing torus 在 $x,y,T$ 上有同一权一，
$T(-P)=-T(P)$。R1066 §4.2 已把这一来源付清到任意 supersingular
fine 点；它不是只在原 $j=0$ cubic family 可用的自同构参数。

在 diagonal Cartan 坐标中，选择同一 actual norm 标记
$v\in\mathbf F_{p^2}$，使 reference 的有限 full-level 点是
$\widetilde\alpha=0,\widetilde\beta=\beta_0\ne0$。
$v$ 在下文幂式中指 Teichmüller lift；整数 linear coefficient 与它的差
含 $p$。R1021 的全部 level 作用模 $p$ 正是原线性作用，因此
$$
T(P_v)=\varpi\beta_0(v+r v^p)+O(p\varpi).
\tag{1071.10}
$$
其中 $r=\widetilde\alpha/\widetilde\beta$，
$\beta_0\in W^\times$ 取同一 Moore branch 的单位提升。

这里的 $\beta_0$ 不能任设为 $1$。
它来自同一 full-level 点，并与稍后的 Weil root 相位配套。

### 2.1 原 source 给出 r 的准确一阶

R1066 (1066.20) 在这个原 affine 邻域给
$$
u=\rho^p(c_D\mathcal D+pR_0),\qquad
c_D\in W^\times,\qquad R_0\text{ 正则}.
\tag{1071.11}
$$
此 $pR_0$ 的精度来自实际 framing 齐次次数
$p(p-1)+j(p^2-1)$，不是仅从根的 linear leading 猜得。

同一 Moore 分支模 $p$ 的方程给
$\widetilde\beta^{p+1}(1-r^{p+1})=$ 固定非零常数。
而 source Dickson 函数在该坐标中是非零常数倍的
$$
\widetilde\beta^{p(p-1)}
       \frac{r(1-r^{p^2-1})}{1-r^{p+1}}.
$$
它在 $r=0$ 简单为零。由 (1071.11) 和 (1071.8) 得 $r\in\rho\mathcal O$。
于是 $r^{p+1}\in p\mathcal O$，
$$
\widetilde\beta/\beta_0=1+O(p),\qquad
r=\lambda\rho t+O(p),\qquad \lambda\in W^\times.
\tag{1071.12}
$$
$\lambda$ 是同一 source Dickson 导数及 $c_D$ 的实际逆单位。
本文保留它，不把 $u$ 偷换成另一个归一化参数。
(1071.12) 只声称 $O(p)$，不需要额外声称 $O(p\rho)$。

因此，在整个所需 affine disk 上可使用
$$
\widetilde T_v=\varpi\beta_0(v+\lambda\rho t\,v^p),
\qquad
T(P_v)/\widetilde T_v\in1+p\mathcal O.
\tag{1071.13}
$$
这里 $\widetilde T_v/\varpi$ 是单位。

## 3. 实际 ψ 单位和 Teichmüller 权替换

原 reference 上的 Laurent expansion 可准确写成
$$
\psi_c(T)=c\,a_c\,T^{1-c^2}F_c(T),\qquad
a_c\in W^\times,\qquad
F_c(T)\in1+T W[[T]].
\tag{1071.14}
$$
若将 $T$ 的 tangent 归一为原 Weierstrass 参数，则 $a_c=1$；
不作此归一时，同一个 $a_c$ 在全部 $v$ 上相同并被 augmentation 杀掉。
$c$ 为奇数且 $T(-P)=-T(P)$，故 $F_c$ 是偶函数。

定义真正有限系数
$$
\frac{F_c'(T)}{F_c(T)}
   =\sum_{d\ge1}A_dT^{d-1},\qquad A_d\in W,
$$
$$
\log F_c(T)=\sum_{d\ge1}\ell_dT^d,\qquad
d\ell_d=A_d.
\tag{1071.15}
$$
特别 $A_d=0$ 当 $d$ 为奇数。
本篇只需要 $d\le N$ 的 $A_d\bmod p$。
它们必须按原 eigen-$T$ 计算；任意 Weierstrass 参数下的同名系数
不能直接代入。

### 3.1 完整 augmentation-zero 产品是原局部单位

对任意整数 norm-exponent vector $(b_h)$，只要 $\sum b_h=0$，
R1070 的实际 $N_{\rm ns}$ 和实下降证明仍适用；
它不要求此 vector 已给 $p$ 倍 divisor。
因此对应的 $\psi_c$ 产品严格属于 $F(X)^\times$。

在当前 full-level affine 邻域，全部
$T(P_v)/\varpi$ 都是单位，且非零 $p$-torsion 不属于 $E[c]$。
(1071.14) 表明所有因子的 valuation 相同，
而
$$
\sum_{v/\pm}b_{[Nv]}=(p+1)\sum_hb_h=0.
$$
所以共同的 $\varpi$ 次数准确抵消；产品及其逆均在该邻域正则。
下降到原 smooth formal disk 后，它是 $\mathcal O_{F_{\mathfrak p}}$ 的单位。
其约化在整个 $\mathbf A^1$ 上亦为无零无极单位，故是非零常数。

置 $K=F_{\mathfrak p}$。因为
$e(K/\mathbf Q_p)=m<p-1$，
单位去 Teichmüller 部分后，其 $p$-adic log 属于
$\mathfrak p_K$；log/exp 在这里互逆。

现在可将 (1071.4) 的原整数权替换为精确权
$$
\widetilde n_v=\frac1m\omega(Nv)^{-R}
             =\frac1m v^{-N}.
\tag{1071.16}
$$
两组权的差属于 $p\mathbf Z_p[G]_0$。
用整数 augmentation-zero vectors 逼近其商，
上一段使 log 的差属于 $p\mathfrak p_K$，
其 $\varpi$ 阶严格大于 $e$。
这比 $N<e$ 高，故不改变下面的 leading 读数。

这是对**完整、已下降的单位产品**作替换；
不逐个把有 pole 的 $\psi_c(P_v)$ 当成单位。

### 3.2 参数和曲线的 O(p) 误差不会回流

由 (1071.13)–(1071.14)，
$$
\frac{\psi_c(T(P_v))}{\psi_c(\widetilde T_v)}\in1+p\mathcal O.
$$
其 log 的 $\varpi$ 阶至少为 $e$。
将曲线的 $u=pt$ 系数改为 reference 的 $u=0$ 时，
$F_c$ 的系数差也含 $p$，相对比同样在 $1+p\mathcal O$。
共同 leading 常数仍由 augmentation 消去。

因此所有这些实际误差在总 log 中均高于 $N$。
这里使用相对单位的 log 乘法，已一次性包含任意高 log 分母；
不能先只估某一个 Taylor 单项再忽略其它分母。

## 4. Pole log 精确消失，完整高分母逐项排除

把 (1071.14) 的 pole 与 unit 分开。
$\log c,\log a_c,\log\varpi,\log\beta_0$ 的共同项均被 augmentation 杀掉；
$\log v=0$。剩余 pole 项是
$$
(1-c^2)\sum_{v/\pm}\widetilde n_v
       \log(1+\lambda\rho t\,v^{p-1}).
\tag{1071.17}
$$
第 $i\ge1$ 项的根和只有在
$-N+(p-1)i\equiv0\bmod e$ 时可能非零。
模 $p-1$，这要求 $2R\equiv0\bmod p-1$，
正被实际 $\chi^2\ne1$ 排除。
所以 (1071.17) **严格为零**，不只是忽略一个 pole leading。

对 unit-log 的 $d$ 次项作二项式展开，令
$$
D=d+(p-1)i,\qquad 0\le i\le d.
$$
由于实际偶性，可把半向量和写成全非零向量和的一半。
根正交准确给
$$
\sum_{v/\pm}\widetilde n_v v^{d+(p-1)i}
 =\begin{cases}
 p+1,&D\equiv N\bmod e,\\
 0,&\text{否则}.
 \end{cases}
\tag{1071.18}
$$
非零项写成 $D=N+s e$，$s\ge0$。
归一化前的系数是
$\ell_d\binom di\varpi^D\beta_0^d\lambda^i t^i$。

### 4.1 i>0 的全部高层

由
$$
\ell_d\binom di
  =\frac{A_d}{d}\binom di
  =A_d\frac{\binom{d-1}{i-1}}i
\tag{1071.19}
$$
得分母同时受 $p^{v_p(d)}$ 和 $p^{v_p(i)}$ 控制。
若 $s\ge1$ 的项能降至 $\varpi^N$ 或更低，
必有 $p^s\mid d$ 和 $p^s\mid i$，从而
$$
D=d+(p-1)i\ge p^{s+1}.
$$
当 $s\ge2$ 时，这与
$D=N+s e<(s+1)p^2<p^{s+1}$ 矛盾。
当 $s=1$ 时，
$$
D\equiv R-1\not\equiv0\pmod p,
$$
也矛盾。故所有 $s\ge1$ 的 $i>0$ 项都高于 $N$。

### 4.2 i=0 的全部高层

此时 $d=N+s e$，分母只可能含 $p^{v_p(d)}$。

- $s=1$：$d\equiv R-1\not\equiv0\bmod p$。
- $s=2$：若 $R\ne2$，$d\equiv R-2\ne0\bmod p$；
  若 $R=2$，则 $d=2p(p+1)$，准确 $v_p(d)=1<2$。
- $s\ge3$：$d<(s+1)p^2<p^s$，故 $v_p(d)<s$。

所以这些项也不能回到 $N$。
这单独处理了全 $V$ 扩展中的 $R=2$ 边界，
并未把 forced 范围的非零同余硬套给它。

双重展开收敛，因为 $d/e-v_p(d)\to+\infty$；
以上排除涵盖全部高次，不是有限数值截断观察。

## 5. 完整 leading 多项式

只剩 $D=N$。
此时 $0\le i\le I<p$，$d=d_i>0$；
$i>0$ 的分母用 (1071.19)，$i=0$ 则 $p\nmid N$。
由原 $M_\chi$ 的负 exponent，得到
$$
\boxed{
\begin{aligned}
\mathcal P_{\chi,s}(t)
&=\overline{\varpi^{-N}\log M_\chi(t)}\\
&=-(p+1)\left(
 \overline{\beta_0}^{\,N}\frac{\overline{A_N}}{N}
 +\sum_{i=1}^{I}
  \overline{\beta_0}^{\,d_i}\overline{\lambda}^{\,i}
  \overline{A_{d_i}}\,
  \frac{\binom{d_i-1}{i-1}}{i}\,t^i
 \right).
\end{aligned}}
\tag{1071.20}
$$
式中分母按 $\mathbf F_p$ 解释，均为单位；
若 $p\mid d_i$，仍必须用所显示的 $1/i$ 形式，
不能改回一个未经除尽的 $1/d_i$。

这给出完整 leading coefficient，而不只一个低次近似。
特别没有隐藏的 $t^p$ 项：
$$
\deg_t\mathcal P_{\chi,s}\le I\le p-2.
\tag{1071.21}
$$
没有宣称 (1071.20) 恒非零、为常数、单射或只在 CM 中心取某个值。
这些都是需要继续对原系数证明的实质问题。

## 6. 原 Weil root 与 circular-unit 读数

固定同一 full-$p$ basis 的真实 Weil pairing
$$
\zeta_p=e_p(P,Q),\qquad
\gamma=\overline{\frac{\zeta_p-1}{\varpi^{p+1}}}\ne0.
\tag{1071.22}
$$
不能独立改变 (1071.20) 的 Cartan basis 后仍沿用旧 $\gamma$。

取一个奇整数 $a$，其类生成 $G$。
原 real circular unit 是
$$
\eta_a=\zeta_p^{(1-a)/2}\frac{\zeta_p^a-1}{\zeta_p-1}.
\tag{1071.23}
$$
在实际 $\chi$ 空间取原单位类 $\beta_\chi=e_\chi[\eta_a]$。
其 leading log 系数准确为
$$
\boxed{\quad
b_\chi=
 \frac{B_R(a^R-1)}{R\,R!}\,\gamma^R.
\quad}
\tag{1071.24}
$$

为明确精度，置 $\lambda_{\rm cyc}=\zeta_p-1$。
$\eta_a/a-1\in\lambda_{\rm cyc}^2\mathcal O$。
其 log 中第 $n\ge p$ 项的 cyclotomic valuation 至少
$2n-(p-1)v_p(n)\ge p+1$，
不影响 $2,\ldots,p-3$ 阶。
在这些阶内，形式变量
$z=\log(1+\lambda_{\rm cyc})$ 的截断满足
$z=\lambda_{\rm cyc}+O(\lambda_{\rm cyc}^2)$，
并在 $\sigma_b$ 下变成 $bz$。
普通有限形式恒等式给
$$
\log(\eta_a/a)\equiv
\sum_{\substack{2\le r\le p-3\\r\ {\rm even}}}
 \frac{B_r(a^r-1)}{r\,r!}z^r
 \pmod{\lambda_{\rm cyc}^{p-1}}.
$$
投影到 $\omega^R$ 后只留所示最低项，
再用 $N=(p+1)R$ 即得 (1071.24)。
这里绝没有把真正的 $p$-adic $\log\zeta_p=0$
当作一个非零解析参数。

若 $p\nmid B_R$，则 $a^R-1\ne0\bmod p$，
故 $b_\chi\ne0$。
于是原 Kummer 标签在 $\beta_\chi$ 基中的坐标为
$$
\boxed{\qquad
c_{\chi,s}(t)=
 \frac{m}{\overline{\kappa_\chi}\,b_\chi}\,
      \mathcal P_{\chi,s}(t).
\qquad}
\tag{1071.25}
$$
$\beta_0,\lambda,\gamma$ 三个实际尺度全部保留。
换原 full basis 或 compatible framing 会同时运输这些量和
$t$；(1071.25) 仍读同一个规范 $\Phi$，不是任意同构源。

## 7. 这确读完整 local 类和唯一 global 候选

R1062 §9 给
$$
U_1(K)/U_1(K)^p
 \simeq\mathfrak p_K\mathcal O_K/p\mathfrak p_K\mathcal O_K.
$$
每个非平凡偶角色准确一维，其最早 cyclotomic 阶是 $R$。
所以 (1071.25) 读的是整个该角色的 local Kummer 类，
不只是丢失其余 $p$-adic 信息的一个任意近似。

对 R1069 的真实
$$
W_{\rm good}=\bigoplus_{\substack{V_\chi\ne0\\p\nmid B_R}}V_\chi,
$$
$p$-only global localization 在每个角色都是同构。
因此向量
$$
\mathbf c_s(t)=
  \bigl(c_{\chi,s}(t)\bigr)_{\chi\subset W_{\rm good}}
\tag{1071.26}
$$
准确给这个原 $p$-local disk 的唯一全局候选。
不需要 regular $p$ 或 Vandiver；
forced-good 角色仍给 R1069 的无条件 $\Omega(p/\log p)$ 维下界。

当 $t$ 位于实际 arithmetic descent line 时，
(1071.25) 的值在 $\mathbf F_p$。
在选定的 $\mathbf F_p$ 参数中，次数小于 $p$，
故其系数也在 $\mathbf F_p$：
系数 Frobenius 差在全部 $p$ 个参数值为零，
而该差的次数小于 $p$。

## 8. 原 coarse components 和全部 twist 支路

R1066 §4.3 的额外稳定子为
$$
e_s=1,\ 3,\ 2
$$
，分别对应一般 $s$、supersingular $j=0$、supersingular $j=1728$。

在 $j=0$ reference，实际 $\mu_6$ 作用与原 eigen-$T$ 相容。
$\psi_c(\xi T)=\xi^{1-c^2}\psi_c(T)$，
所以 $F_c$ 不变，$A_d=0$ 除非 $6\mid d$。
又 $p\equiv2\bmod3$，故 $N\equiv0\bmod6$，
$d_i=N-(p-1)i$ 的条件迫 $3\mid i$。
于是 (1071.20) 是 $t^3$ 的多项式。

在 $j=1728$ reference，同理 $\mu_4$ 使 $4\mid d$，
$p\equiv3\bmod4$ 迫 $i$ 为偶数。
于是 (1071.20) 是 $t^2$ 的多项式。

将同一几何 fine frame 按原 arithmetic descent 运输，
得到原 coarse 参数
$$
T_{\rm coarse}=t^{e_s},\qquad
\deg_{T_{\rm coarse}}c_{\chi,s}
 \le\left\lfloor I/e_s\right\rfloor.
\tag{1071.27}
$$
这些是同一个原标签函数的 compatible 表达。

- $e_s=1$：原 fine $\mathbf F_p$ line 给全部 coarse 值。
- $e_s=3$：$p\equiv2\bmod3$，cube 在 $\mathbf F_p$ 上双射。
- $e_s=2$：必须保 R1066 的两种实际 quartic-twist descent lines。
  在共同几何坐标中分别是 $t^p=t$ 和 $t^p=-t$；
  二者一起覆盖全部 $T_{\rm coarse}\in\mathbf F_p$。

不能只取一个固定 twist 的平方像。
每条 twist 的 $\beta_0,\lambda,\gamma$ 按实际同构一起运输；
在公共 coarse 坐标中的多项式仍在 $\mathbf F_p[T_{\rm coarse}]$，
因为它来自原 $X$ 上同一个规范标签。

## 9. 完整有限候选集与必须保留的辅助约束

综上，R1065 的全部 $p\,n_{\mathbf Q_p}(p)$ 个原 smooth residue disks
给出完全明确的有限候选集
$$
\mathscr C_p^{\rm good}
 =\bigcup_{\substack{s\text{ supersingular}\\s\in\mathbf F_p}}
   \{\mathbf c_s(T):T\in\mathbf F_p\}.
\tag{1071.28}
$$
每个坐标使用 (1071.15) 中至 $N< p^2-1$ 的原有限数据，
以及 (1071.22) 的同一 Weil phase。
重复标签保留为集合中的同一项；
不把不同 CM representative 的 norm 平均冒充这个单一 embedding 的值。

对任何非 cusp $x\in X(\mathbf Q)$，
它在 $W_{\rm good}$ 上的同一个全局 $\Phi_x$ 必须是
(1071.28) 中某一候选，并且在每个有效辅助素 $\ell\ne p$ 上满足
$$
\bigl(\operatorname{red}_{\mathfrak q}\Phi_x\bigr)_{\mathfrak q\mid\ell}
 =
\bigl(\Psi_{\mathfrak q}(y_\ell)\bigr)_{\mathfrak q\mid\ell}
\quad\text{对同一个 }y_\ell\in X(\mathbf F_\ell).
\tag{1071.29}
$$
右边按 R1070 的原 $\psi_c$ 公式，在全部真实 necklaces、
全部 twists 和全部 $\mathfrak q$ 的 Galois 关联上求取。
不能逐角色各挑一个不同 $y_\ell$。

R1070 §10 的精确 visibility 仍适用：
若 $\operatorname{ord}_p(\ell)$ 为偶数，或
$p\equiv3\bmod4$ 且该阶为 $(p-1)/2$，
整个实际 cuspidal cover 在该辅助素没有筛选力。
特别 safe prime 情形只能在 $\ell\equiv1\bmod p$ 处寻找此种约束。

本文没有证明 (1071.29) 排除所有非 CM 候选，
没有宣称候选向量恒定、最高或最低系数为单位，
也没有将局部 bounded-discriminant CM representative 当成全局有理 CM 点。
真正下一问题是同一候选与有效辅助原像的共同相容。

## 10. 来源、验证与范围

- [R1021](R1021-actual-full-p-affine-tail-rigidity-and-quotient-parameter.md)
  §§1–4：同一 universal $T(P),T(Q)$、实际 framing 和 affine 模 $p$ 精度。
- R1062 §§1–3、§9：原角色方向、实际 cusp 模块、原 circular-unit leading。
- [R1066](R1066-original-p-local-disks-and-bounded-CM-representatives.md)
  §4.1–4.3：所有 supersingular 点、$\rho^{p+1}=p$、
  source Dickson、原 coarse 和全部 twist 支路。
- [R1067](R1067-original-cuspidal-labels-supported-only-at-p.md)：
  实际全局标签只支撑 $p$。
- [R1069](R1069-all-prime-good-cuspidal-characters-and-unique-global-labels.md)：
  全 $p$ 的 good 角色唯一全局标签，不用 regular/Vandiver。
- [R1070](R1070-original-cuspidal-labels-by-division-polynomial-values.md)
  §§4–8、§10：原 $M_\chi$ 相位、$\kappa_\chi$、全部 cusp leading、
  整个实际 $V$ 的 $\chi^2\ne1$ 和精确辅助 visibility。

root 逐式独核原 source、normal 次数、两个高分母分支、全部相位、
原负 exponent 与 $m/\kappa$ 的总尺度、全角色及 coarse/twist 范围。
global_route 给出完整来源、根和、有限多项式及尺度证明；
o2 独立纸核全部高 log 分母、$R=2$ 边界、$O(p)$ 相对单位误差、
原 augmentation-zero 下降单位和 Weil/circular-unit 读数。
没有数学执行或新 CI。主目标的无条件全局排除仍开放。
