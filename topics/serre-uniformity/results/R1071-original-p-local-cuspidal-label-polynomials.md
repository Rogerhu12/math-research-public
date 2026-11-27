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

## 11. 原 eigen-T 的有限 formal-log 读法

本节至 §15 是同一来源的后继证明，仍全部为纸面推导。

固定 §2 的 marked CM reference，写其 good short Weierstrass equation 为
$$
E_0:\ y^2=x^3+A x+B,\qquad
z=-x/y,\qquad
\omega=\frac{dx}{2y}=\left(\sum_{n\ge0}a_nz^n\right)dz,\quad a_0=1.
\tag{1071.30}
$$
同时将原 eigen-$T$ 的 tangent 归一为 $1$。
这里的 tangent 归一同时作用于原 full-level 参数，
不是只在计算 $\psi_c$ 时另换一个不相干参数。

### 11.1 低于 p² 的真正整对数

因为 $E_s$ supersingular，$\operatorname{Cartier}(\bar\omega)=0$。
在同一局部参数下逐系数读取，即
$$
a_{kp-1}\in pW\qquad(k\ge1).
$$
所以形式对数
$$
L(z)=\int_0^z\omega
 =\sum_{n\ge1}\frac{a_{n-1}}n z^n
\tag{1071.31}
$$
在所有 $n<p^2$ 次的系数均整：
若 $p\mid n$，只含一次 $p$，恰由 Cartier 零消去；
若 $p\nmid n$，分母是单位。

因此这些系数模 $p$ 由原 Weierstrass equation 模 $p^2$ 唯一决定。
对 $n=pk$ 必须先取 $a_{n-1}\bmod p^2$，除去 $p$ 后再约化；
只用特殊纤维的 $\bar\omega$ 会丢失这些系数。

原 reference 的不分歧二次 CM 作用包含 $\mu_e$。
同一 torus 在 $T$ 上是权一，在 $\omega$ 的 tangent 上也是权一。
由形式对数的唯一性，
$$
L([\xi]P)=\xi L(P),\qquad T([\xi]P)=\xi T(P).
$$
故 $L(z(T))$ 只含次数 $1\bmod e$，其 linear coefficient 为 $1$：
$$
\boxed{\quad L(z(T))=T+O(T^{p^2}).\quad}
\tag{1071.32}
$$
这支付了原 eigen-$T$ 与 formal-log 的真实来源。
不是仅由 tangent 相同就断言任意两参数有高阶相等。

为读全部 $A_d$，$d\le N$，取 $L$ 至 **$N+1$ 次** 即足够；
多取这一阶是因为 $\psi_c$ 在 $O$ 有 pole。
由于 $N+1<p^2$，(1071.31) 的整性范围完全足够。

### 11.2 不需要求出整个 CM reference

R1066 §3 对同一 marked supersingular curve 的每个 first lift
给出一个 $p$-prime conductor 的实际 CM lift。
因此可先选一个方便的 good equation $E_*/W\bmod p^2$，
再取与其同 marked first lift 的 CM reference。
二者的 invariant differential 系数模 $p^2$ 相同，
故 (1071.31) 的全部 $n<p^2$ 系数模 $p$ 相同。

模型与 differential 的标记必须一起运输。
这只免去计算 CM lift 的无限 $p$-adic 展开，
不把一个不同 first lift 的 formal log 当作同一个 reference。

当 $E_s/\mathbf F_p$ 且所选 first lift 在 $\mathbf Z_p/p^2$ 上时，
得到的有限 $L\bmod p$ 在 $\mathbf F_p$ 上且为 odd series。
R1066 的 actual arithmetic-stable CM reference 支付该下降。

## 12. 一个已支付的 source 坐标和无需 reversion 的 A_d

### 12.1 明确 source 归一，而不猜 λ

在同一 universal eigen-$T$ 中，取
$$
u_*=[T^p]\,[p](T),\qquad t_*=u_*/p.
\tag{1071.33}
$$
$p$-series 的 $T^p$ coefficient 是 Hasse 的简单参数，
其 framing 权准确为 $1-p$。
所以 $u_*$ 是原 $u$ 的整可逆参数变换，CM reference 仍是 $0$；
它不是一个仅在抽象 formal group 上定义的替代 deformation。

由 framing，所需初项为
$$
[p](T)=pT+u_*T^p+g_0T^{p^2}+\text{更高 normal 项},
\qquad g_0\in W^\times.
\tag{1071.34}
$$
取 $a=\varpi\beta_0$，使 $a^e=-p/g_0$。
代入 $T=a(v+r v^p)$，$pT$ 与 $g_0T^{p^2}$ 的 $v$ 项抵消；
$v^p$ 项给
$$
r=-a^{p-1}t_*+O(p)
  =-\beta_0^{p-1}\rho t_*+O(p).
\tag{1071.35}
$$

误差精度可逐类核定。无 $u_*$ 的下一次数是 $2p^2-1$；
一次 $u_*$ 的下一次数是 $p+e$；
至少二次 $u_*$ 的项含 $u_*^2$。
除去主尺度 $pa$ 后，这三类的 normal 次数均至少为 $e$。
$u_*T^p$ 中的 $r^p$ 项也在除去 $pa$ 后至少为 $e$；
其余二项式项多一个 $p$。
所以 (1071.35) 确有 $O(p)$ 精度。
这正给原 §5 的
$$
\lambda=-\beta_0^{p-1}
\tag{1071.36}
$$
在这个**明确指定**的 source 坐标中的约化值。

因为 $E_s/\mathbf F_p$ supersingular 且 $p>3$，
其 arithmetic Frobenius 满足 $\pi^2=[-p]$。
原 odd $\mathbf F_p$ 参数 $T$ 上 $\pi$ 是 $T\mapsto T^p$，
所以
$$
[p](T)\bmod p=-T^{p^2}.
$$
可在同一 $\varpi$ 上选实际 torsion root branch，
令 $\bar\beta_0=1$。这给 $\bar\lambda=-1$。
选择这个 branch 并没有删除 Weil 相位；下一节仍真实计算它。

在此坐标下 (1071.25) 变成
$$
c_{\chi,s}(t_*)=
\frac1{2\bar\kappa_\chi b_\chi}
\left(
 \frac{\bar A_N}{N}
 +\sum_{i=1}^{I}
   (-1)^i\bar A_{d_i}
   \frac{\binom{d_i-1}{i-1}}i\,t_*^i
\right).
\tag{1071.37}
$$
这里使用 $-m(p+1)=1/2$ 于 $\mathbf F_p$，
原负 exponent 的符号完全保留。

### 12.2 原 finite Weierstrass 数据的直接公式

置 $q=z^2$、$w=q x$。从原 short equation 得
$$
w^3-w^2+Aq^2w+Bq^3=0,\qquad w(0)=1,
$$
$$
\frac{\omega}{dz}=1-\frac{q w'}w,\qquad
L(z)=zU(q),\qquad
U_n=\frac{[q^n](1-qw'/w)}{2n+1}.
\tag{1071.38}
$$
其中 $U_n$ 按 §11 的模 $p^2$ 后除 $p$ 规则读取。
$w$ 的方程在 $w=1,q=0$ 的导数为单位，
因此所有所需系数由有限整递推给出。

令
$$
H(q)=\frac{z\psi_c'(z)}{\psi_c(z)}.
$$
对每个所需的偶数 $d$，形式 residue 换元给出准确式
$$
\boxed{\qquad
\bar A_d=[q^{d/2}]\,\bar H(q)\,\bar U(q)^{-d}.
\qquad}
\tag{1071.39}
$$
证明是
$$
A_d=\operatorname{Res}_{T=0}T^{-d}\,d\log F_c(T)
   =\operatorname{Res}_{z=0}L(z)^{-d}\,d\log\psi_c(z).
$$
归一化因子 $T^{c^2-1}$ 的贡献为
$(c^2-1)\operatorname{Res}T^{-d-1}dT=0$。
这个论证没有除以 $d$，因此 $p\mid d$ 时仍合法。
代 $L=zU(q)$ 即得 (1071.39)。

若 $d=ap+b$，$0\le b<p$，则在实际 $\mathbf F_p$ first lift 上
$$
\bar U(q)^{-d}
 =\bar U(q)^{-b}\,\bar U(q^p)^{-a}.
\tag{1071.40}
$$
可用有限 unit powers 与稀疏卷积读取；
无需在 characteristic $p$ 作含 $1/n$ 的形式 log/exp 或高阶 reversion。

例如新固定 $p=47$ 可取 $c=5$：
$(5/47)=-1$ 且 $46=2\cdot23$，$5\not\equiv-1$，故它是 primitive。
其原 division polynomial 可直接由
$$
\begin{aligned}
\psi_5={}&32(x^3+Ax+B)^2
 (x^6+5Ax^4+20Bx^3-5A^2x^2-4ABx-8B^2-A^3)\\
&-(3x^4+6Ax^2+12Bx-A^2)^3
\end{aligned}
\tag{1071.41}
$$
给出。若
$V(q)=q^{12}\psi_5(w/q)/5$，则
$$
H(q)=-24+2qV'(q)/V(q).
$$
这里只给有限原算法，没有报告任何未执行的数值结果。

## 13. 原 Weil 相位的有限 Miller 计算

固定同一个
$$
\mathbf F_{p^2}=\mathbf F_p(s),\qquad s^2=\delta
$$
，其中 $\delta$ 为固定非平方。
在所有 supersingular references 和后续 auxiliary 比较中，
保留同一 norm 标记，不任意改 $\delta$。

置 $h=\varpi$。在 §12 的实际 branch 上取
$$
T(P)=h+O(ph),\qquad T(Q)=s h+O(ph).
\tag{1071.42}
$$
这给两个真正线性无关的 $p$-torsion 点。
由 §11 的 $L^{-1}$ 至 $p+2$ 次，把它们写成原 Weierstrass Laurent 点。
不需要求整个 ramified $p$-torsion extension 的高精度根。

CM torus 还给
$$
T([n]P)=nT(P)+O(T(P)^{p^2}),\qquad 1\le n<p.
\tag{1071.43}
$$
因此在所需精度内，binary Miller 中的倍点可用 $T=nh$ 或 $ns h$。

### 13.1 规范 Miller 来源与符号

使用 Miller 已发表论文 [M] §4.1 Definition 4–6、Lemma 2 的
$O$-leading $1$ 规范。
对 short equation、参数 $z=-x/y$：

- 非竖直 line 取
  $-(y-y_A-\lambda_{A,B}(x-x_A))$；
- 竖直 line 取 $x-x_A$。

线除以 $A+B$ 的竖直线给原 $g_{A,B}$，
于是
$$
f_{a+b,P}=f_{a,P}f_{b,P}g_{aP,bP},\qquad
\operatorname{div}f_{p,P}=p[P]-p[O].
$$
最后一次 $A+B=pP=O$ 直接使用竖直线。
不把一个被截断成近零的 affine 分母拿来相除。

[M, Proposition 8, Eq. (11), printed pp.245–246] 在实际
characteristic zero 点上准确给
$$
e_p(P,Q)=(-1)^p\frac{f_{p,P}(Q)}{f_{p,Q}(P)}.
\tag{1071.44}
$$
这里的 $(-1)^p$ 不能删除。
该已发表命题先用于原 characteristic zero 曲线；
下面才将这一个真实等式降到有限 characteristic-$p$ series。
没有把其 prime-to-characteristic 假设硬套到 nilpotent $p$-torsion。

### 13.2 每个因子都是可控的 Laurent 单位

在 $T=ah$、$a\ne0$ 处写
$$
x(ah)=h^{-2}X_a(h),\qquad
y(ah)=h^{-3}Y_a(h),
$$
其中 $X_a(0)=a^{-2}$、$Y_a(0)=-a^{-3}$。
Miller 的每个非末步只涉及 $a,b\in\mathbf F_p^\times$，
评价点的参数比例是 $s\notin\mathbf F_p$。

去掉显式 $h$ 次数后：

- 非竖直 line 的 leading 三个根为
  $a,b,-a-b$；切线时允许重复根；
- 竖直 line 的 leading 根为 $\pm a$；
- 非竖直分母的 leading 非零，除非 $a=-b$，
  而该情况已用竖直分支单独处理。

所以在 $s$ 处所有归一化因子都是单位。
计算 $f_{p,Q}(P)$ 时，比例 $1/s\notin\mathbf F_p$，
同一论证适用。

实际输入与有限近似的相对误差是 $O(h^e)$，
由 (1071.42)、(1071.43) 及 reference 模 $p$ 曲线系数得到。
单位乘除和平方不会降低该阶。
两条 Miller function 的共同 $h^{-p}$ 因子最终抵消，
不能把它误认为额外损失 $p$ 阶精度。

因此只在 $\mathbf F_{p^2}((h))$ 中计算相对精度 $h^{p+2}$，
就得到原式
$$
\boxed{\quad
(-1)^p f_{p,P}(Q)/f_{p,Q}(P)
 =1+\gamma_s h^{p+1}+O(h^{p+2}).
\quad}
\tag{1071.45}
$$
其 $\gamma_s$ 正是 (1071.22)，包括真实 principal-polarization 单位。

独立性及 Weil 非退化给 $\gamma_s\ne0$。
由原 primitive $p$-th root 的 cyclotomic 方程，
$\gamma_s^{p-1}=-1$；因有限计算在 $\mathbf F_{p^2}$ 中，
$\gamma_s^p=-\gamma_s$。
这个恒等式可核验相位，但不能代替 (1071.45) 计算它。

## 14. 全局相位对齐及有限输入范围

若两个 actual references 的 Weil roots 满足
$\zeta_s=\zeta_0^a$，则
$$
\gamma_s=a\gamma_0,\qquad a\in\mathbf F_p^\times.
$$
选择原 Cartan 乘法 $b$，$Nb=a^{-1}$，
可把该 basis 改到固定 Weil root $\zeta_0$。
同一个原 source 的数据随之变为
$$
\beta_0\mapsto b\beta_0,\qquad
\lambda\mapsto b^{p-1}\lambda.
$$
(1071.20) 的整个括号乘
$b^N=(Nb)^R=a^{-R}$。
这与 (1071.24) 中 $\gamma_s^R=a^R\gamma_0^R$
的分母完全相配。

所以用各自**真实计算**的 $\gamma_s$ 读出的 (1071.37)，
已经等于固定原 global basis 下的坐标。
没有缺一个随 supersingular 点变化的未定标量。
若换 quadratic-extension 模型或 norm 标记，仍须作同样的实际运输；
不能把它们逐点重新任意编号。

全部有限输入至此为：

1. 同 marked good reference 的 Weierstrass equation 模 $p^2$；
2. 由其原 $\omega$ 得 $L$ 至 $N+1<p^2$ 次，除 $p$ 前保模 $p^2$；
3. 同一个原 $\psi_c$ 和 (1071.39) 的有限 coefficients；
4. source $u_*=[T^p][p](T)$，以及 (1071.35) 的已支付坐标改变；
5. (1071.45) 的真实 Miller 相位，至相对 $h^{p+2}$。

额外 automorphism 和全部 twist 支路仍按 §8 运输。
例如在 $j=1728$ 不能只计算一个 quartic twist 的平方参数；
两支必须一起覆盖原 coarse $\mathbf A^1$。

[M] V. S. Miller, *The Weil Pairing, and Its Efficient Calculation*,
J. Cryptology **17** (2004), 235–261，
[正式 DOI](https://doi.org/10.1007/s00145-004-0315-8)，
[已刊全文](https://link.springer.com/content/pdf/10.1007/s00145-004-0315-8.pdf)。
实际亲读 §4.1、Definition 4–6、Lemma 2 和 Proposition 8；
这里只调用 characteristic zero 上的已发表公式，
其所需有限降模精度由 §13.2 完整证明。

## 15. Lucas 消去、真实低阶上界与首个非零来源

(1071.20) 的次数界还可严格缩短。
首先，非零二项式要求 $i\le d_i$，即
$$
pi\le N,\qquad i\le R.
$$
因此原 $R>m$ 时形式上存在的 $i=R+1$ 项本来就是零。

又 $i<p$，且
$$
d_i-1\equiv R+i-1\pmod p.
$$
若 $R+i>p$，其低 $p$ 位是 $R+i-p-1<i-1$，
由 Lucas 或直接比较分子中唯一的 $p$ 因子，
$$
\binom{d_i-1}{i-1}\equiv0\pmod p.
$$
若 $R+i\le p$，该二项式的低位读数非零。
所以准确有
$$
\boxed{\qquad
\deg_t\mathcal P_{\chi,s}\le \min(R,p-R).
\qquad}
\tag{1071.46}
$$
所有保留下来的二项式系数都是 $p$-单位；
进一步的消失只能来自原 $A_{d_i}$。

特别 forced 角色 $\chi_j=\omega^{-2j}$ 给
$$
\deg_t\mathcal P_{\chi_j,s}\le2j+1.
\tag{1071.47}
$$
最前一条 $j=1$ 的真实 fine 多项式至多三次。
在 supersingular $j=0$ 上它只含 constant 与 $t^3$；
在 supersingular $j=1728$ 上只含 constant 与 $t^2$。
故这两个原 coarse component 上该坐标都至多一次。
是否有非零斜率仍须核原 $A_d$，不由 degree 一自动得出。

### 15.1 顶项的真正 Cartier 降阶

若 $R<m$，顶部 $i=R$ 读取 $d_i=2R<p$，
二项式 $\binom{2R-1}{R-1}$ 是单位。

若 $R>m$，顶部为 $i=p-R$，并且
$$
d_i=pK,\qquad K=2R-p+1>0,\qquad
\binom{d_i-1}{i-1}\equiv(-1)^{i-1}.
$$
原 $F_c$ 是一个实际 formal unit，
所以其 logarithmic differential 满足 Cartier 固定性：
$$
\bar A_{pn}=\bar A_n^{\,p}.
\tag{1071.48}
$$
在本节的实际 $\mathbf F_p$ reference 上，这就是
$\bar A_{pn}=\bar A_n$。
因 $R$ 为偶数、$i=p-R$ 为奇数，
(1071.37) 的顶部系数准确为
$$
-\frac{\bar A_K}{2\bar\kappa_\chi b_\chi(p-R)}.
\tag{1071.49}
$$

没有 $K=0$：那对应已排除的 $R=m$。
若 $K=2$，则 $p\equiv3\bmod4$、
$R=m+1$，正是 R1070 §10 已证明实际 $V$ 中不存在的角色。
$R=2$ 则位于 $R<m$，此处读 $A_4$；
其高 log 边界已经在 §4.2 单独处理。
所以没有丢掉低 $R$、$d=0$ 或共振边界。

### 15.2 原低权系数和确切非零范围

由 (1071.32)，低次计算确在同一个原 invariant-log 参数上。
原 short equation 的展开为
$$
x(T)=T^{-2}-\frac A5T^2-\frac B7T^4+\cdots.
$$
使用 R1070 已支付的 theta/sigma division-polynomial identity，
或直接把上述展开代入原 $\psi_c$，得到
$$
\boxed{\quad
A_4=\frac{(c^4-c^2)A}{15},\qquad
A_6=\frac{(c^6-c^2)B}{35}.
\quad}
\tag{1071.50}
$$
例如 $\log(\sigma(T)/T)=AT^4/60+BT^6/210+\cdots$，
而 $\psi_c=\sigma(cT)/\sigma(T)^{c^2}$ 的共同 leading constant
不影响 $d\log F_c$。这里不是将任意 eigenparameter 未经核对替换成 log。

若 $p\equiv1\bmod4$，最大 forced $j$ 对应 $R=m+2$，$K=4$。
若该角色 Bernoulli-good 且 $A\ne0\bmod p$，
原候选坐标有确切 degree $p-R$，
顶部为 $A/(30b_\chi(p-R))$。

若 $p\equiv3\bmod4$，最大 forced $j$ 对应 $R=m+3$，$K=6$。
若该角色 Bernoulli-good 且 $B\ne0\bmod p$，
原候选坐标有确切 degree $p-R$，
顶部为 $B/(70b_\chi(p-R))$。

不假设这些 particular 角色对每个 $p$ 都 good。
未除 circular-unit 基以前，
$\bar A_4$ 或 $\bar A_6$ 的相应原 local-log 非零断言不需要此假设。
$A=0$ 或 $B=0$ 的额外自同构点必须另算，
不能由 generic 顶项单位覆盖。

以上短 degree 和有限原相位为实际跨盘候选比较提供新输入；
仍未证明 (1071.29) 只剩全局 CM 标签。

root 已亲读 [M] 的上述实际命题，并逐式独核 §§11–15 的 first-lift 精度、source 归一、residue 换元、Miller 逐单位误差与相位运输、Lucas 全部边界及低权系数。后继计算尚未在本文执行。


## 16. 原 j=0 第一 forced 角色的准确 Hurwitz 斜率

本节固定同一个 supersingular $j=0$ reference，因此 $p\equiv2\bmod3$。
写 $E:y^2=x^3+B$、$\omega_1=dx/(2y)$，$B$ 是单位。
为避免与 §11 的 Weierstrass 参数混淆，将同一 additive logarithm 记为
$z_{\rm add}$；原 eigen-$T$ 满足
$z_{\rm add}(T)=T+O(T^{p^2})$。
定义同一 differential 的原 lattice-sum 规范
$$
x(z_{\rm add})=z_{\rm add}^{-2}
 +\sum_{\substack{d\ge4\\d\ {\rm even}}}
       (d-1)G_d\,z_{\rm add}^{d-2}.
\tag{1071.51}
$$
以下只读 $d=p-5$，其所有所需系数 $p$-整，$d,d-1$ 是单位。
没有把此读数替换成第一共振 $G_{p+1}$。

### 16.1 原 division identity 与 regularizer 的准确相消

取同一 $\sigma$，$\sigma'(0)=1$。对奇数 $c$，
$$
\psi_c(z_{\rm add})
 =\frac{\sigma(cz_{\rm add})}{\sigma(z_{\rm add})^{c^2}}.
\tag{1071.52}
$$
两边是同一椭圆函数，divisor 均为
$[c]^{-1}(O)-c^2(O)$，在 $O$ 的首项均为
$c z_{\rm add}^{1-c^2}$，故比为一。
这里同时固定 differential 和函数的 leading normalization。

由 $(\log\sigma)''=-x$，
$$
\log(\sigma(z_{\rm add})/z_{\rm add})
 =-\sum_{\substack{d\ge4\\d\ {\rm even}}}G_dz_{\rm add}^d/d.
$$
原 $F_c(T)$ 的同一 $d\log$ 因而给
$$
A_d=-(c^d-c^2)G_d\qquad(d=p-5).
$$
$z_{\rm add}(T)/T$ 的首修正在 $p^2-1$，不影响本节；
不把这个边界也纳入无修正范围。
原 leading constant $a_c$ 的 $d\log$ 为零。

对第一 forced 角色 $\chi=\omega^{p-3}$，
$$
\boxed{\quad
A_{p-5}=\kappa_\chi G_{p-5},\qquad
\kappa_\chi=c^2-c^{-4}\ne0.
\quad}
\tag{1071.53}
$$
这是原 $\mathbf F_p$ reference、同一 tangent 下的模 $p$ 身份。
不能独立更换 $\psi_c$ 的 period 或实际 Weil root。

### 16.2 完整 coarse affine 标签

置 $R=p-3$。§15 的 Lucas 消去去掉所有 $i\ge4$；
$j=0$ 的 $\mu_6$ 对称又只允许 $3\mid i$。
所以 §5 的完整 fine 多项式只有 $i=0,3$，
在原 coarse 参数 $T_{\rm coarse}=t^3$ 上准确为 affine。

其 $i=3$ 项满足
$$
d_3=p(p-5),\qquad
\binom{d_3-1}{2}\equiv1,\qquad
A_{p(p-5)}=A_{p-5}.
$$
最后一步是同一原 $d\log F_c$ 的 Cartier 固定性，
在当前 $\mathbf F_p$ reference 上 Frobenius 固定系数。
保留 §2 的全部 $\beta_0,\lambda$，准确得到
$$
\mathcal P_{\chi,s}(T_{\rm coarse})-\mathcal P_{\chi,s}(0)
 =-\frac{\beta_0^{p(p-5)}\lambda^3\kappa_\chi G_{p-5}}3
       T_{\rm coarse}.
\tag{1071.54}
$$
若这一实际角色 Bernoulli-good，则除以原 circular-unit 系数并用
$m\equiv-1/2$，有
$$
\boxed{
c_{\chi,s}(T_{\rm coarse})-c_{\chi,s}(0)
 =\frac{\beta_0^{p(p-5)}\lambda^3G_{p-5}}{6b_\chi}
       T_{\rm coarse}.
}
\tag{1071.55}
$$
原 regularizer $c$ 的 $\kappa_\chi$ 完全相消；
$\beta_0,\lambda$ 以及 $b_\chi$ 中真实 $\gamma$ 的作用全部保留。
这些外因子是单位，所以该原 coarse 斜率非零准确等价于
$G_{p-5}\ne0$。本节尚未证明后者对全部 $p$ 成立。

### 16.3 同一原系数的有限七次积分读数

置 $n=(p-5)/6$、$w=x^{-1/2}\sim z_{\rm add}$。
原模型给
$$
\omega_1=(1+Bw^6)^{-1/2}dw,\qquad
z_{\rm add}=wF(Bw^6),
$$
$$
F(Z)=\sum_{j\ge0}\frac{\binom{-1/2}{j}}{6j+1}Z^j
={}_2F_1(1/6,1/2;7/6;-Z).
$$
Lagrange 反演在原 $x=w^{-2}$ 上给
$$
[z_{\rm add}^{6n-2}]x
 =-\frac{2B^n}{6n-2}[Z^n]F(Z)^{2-6n}.
$$
前 $n$ 项所有分母 $6j+1\le p-4$ 都是单位。
因为 $n<p$，$F(Z)^{-p}\equiv1\pmod{p,Z^{n+1}}$。
用 $6n=p-5$ 并除以 (1071.51) 的 $6n-1$，得到
$$
\boxed{\qquad
G_{p-5}=-\frac{B^n}{21}[Z^n]F(Z)^7\pmod p.
\qquad}
\tag{1071.56}
$$
它是同一原 $\omega_1$ 的有限读数，没有未知高尾或被除掉的 $p$；
没有由其形状宣称指定系数为单位。

### 16.4 已认证输入及未关闭范围

R1072 的已认证 $p=47$ 原模型给 $G_{42}=17$、$A_{42}(c=5)=31$。
代入同一 $\beta_0=1,\lambda=-1,\gamma=20s$，
(1071.55) 的原 coarse 斜率是 $5/b_\chi$。
本节只消费该已登记回执，不新增运行或窗口。

全 $p$ 的 $G_{p-5}$ 单位性仍开；
它与原 $f_N=[z^{p-1}]x\sigma^6$、Gaussian $C_N$ 是不同的读数，
不能未经来源桥而互相替代。
o1_theta 付原 sigma/division、$d\log$ 与 $\kappa$ 相消；
global_route 付同源 $F^7$ 反演，root 独核全部尺度、边界和 finite identity。
本节没有数学程序执行。
