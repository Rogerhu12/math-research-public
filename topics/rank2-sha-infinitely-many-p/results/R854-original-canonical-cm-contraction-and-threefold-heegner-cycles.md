# R854 — 原三个 canonical 周期的精确 CM 图形收缩与固定三维 Heegner 来源

日期：2026-11-16。**状态：已证明。**

本篇在 [R814](R814-common-fixed-good-pair-and-three-original-aj-squares.md) 已固定的同一个 good pair、同一个 weight4 模形式 $g$、同一个有限 CM isogeny orbit 和三个有限角色 $\chi_j$ 上工作。通过一个定义在 $K$ 上的具体代数对应，把其实际负二配对使用的 mixed CM Tate 分量从五维 $W_2\times A_0^2$ 收缩到同一个 Kuga–Sato 三维 $W_2$。

这不是仅在 étale realization 中识别两个表示。对应、其分裂投影、逐 isogeny 的度数常数，以及原 de Rham 配对的 $-2\delta$ 常数都在下面给出。R817 的唯一固定普通素数检测因而证明三份收缩后的固定 Heegner cycle 非零。本文没有识别这个 Kuga–Sato 来源与 R831/R852 的原端点 cycle，也不由一次 AJ 非零推出其它 p 的 AJ 非零。

## 1. 原固定对象与记号

保留 R814 的全部选择：
$$
K=\mathbf Q(\omega),\qquad \delta=1+2\omega,\qquad \delta^2=-3,
\qquad A=A_0:\ y^2=x^3+1,
$$
$$
\omega_A=dx/(2y),\qquad
j\in\{4,10,16\},\qquad
\psi=\psi_{\rm b}\alpha,\qquad g=\theta_\psi,\qquad
\chi_j=\lambda_j/\psi.
\tag{1}
$$
辅助角色 $\alpha$、其导子、三个 $\chi_j$、全部 level 结构、有限轨道和 norm 权重都已先于 p 固定。尤其
$$
\chi_{10}=\chi_4\epsilon,\qquad
\chi_{16}=\chi_4\epsilon^2
\tag{2}
$$
仍是 R814 的原三次角色关系。

使用 BDP 的索引：$W=W_2$ 是两次 universal elliptic fibre product 的平滑 Kuga–Sato 三维，$X=X_2=W\times A^2$ 是五维。其投影子记为 $\epsilon_W,\epsilon_A$，后者按 [BDP, (1.4.4)] 为两个独立的 odd 投影再乘几何交换的 sign 投影。因此，在 $H^1(A)^{\otimes2}$ 的通常未分次记号下，它对应对称张量；不能把几何交换的 sign 删掉。

取一个包含 R814 全部固定数据的共同有限数域 $F\supset K$ 与共同系数域 $\mathcal E\supset K$。全文的 Chow 群取 $\mathbf Q$ 或 $\mathcal E$ 系数。所有实际 finite-character 操作只作用于 cycle 因子，不将系数嵌入一并共轭。

对原轨道中的每个 isogeny
$$
\varphi:A\longrightarrow B,\qquad d_\varphi=\deg\varphi,\qquad
\operatorname{End}(B)=\mathcal O_{c_B}=\mathbf Z+c_B\mathcal O_K,
\tag{3}
$$
保留原 level 结构与 $B^2\hookrightarrow W$ 的 fibre inclusion $i_B$。原 generalized cycle 为
$$
\Delta_\varphi
 =\epsilon_W\epsilon_A
  \bigl[(\varphi\times\varphi,\operatorname{id}_{A^2})(A^2)\bigr]
 \in\operatorname{CH}^3(X)_0.
\tag{4}
$$
这正是 [BDP, §2.3] 的两个图形乘积，按 $B^2\times A^2$ 排列坐标。原 conductor-34 orbit 中 $c_B=34$。

## 2. 固定 CM 图形除子及其真实 Tate 投影

CM 规范规定 $[\delta]^*\omega_A=\delta\omega_A$。定义
$$
D_\delta
 =[\Gamma_{[\delta]}]-[A\times\{0\}]
       -3[\{0\}\times A]
 \in\operatorname{CH}^1(A^2).
\tag{5}
$$
这是图形的 $h^1\otimes h^1$ 分量。它在每个独立反射 $[-1]$ 下取负，在几何交换下也取负：
$$
\epsilon_A D_\delta=D_\delta.
\tag{6}
$$
后一等式可由 Rosati 对偶 $\delta^\vee=-\delta$ 及 Poincaré 除子对 endomorphism 的线性性得到；这里是对称 Néron–Severi 除子之间的 Chow 等式，而不只同调等式。等价地，对任意 $u\in\operatorname{End}(A)$，先取
$$
D_u=(\pi_1\otimes\pi_1)[\Gamma_u].
$$
交换把 $D_u$ 送到 $D_{u^\vee}$，且 $u\mapsto D_u$ 在 $\operatorname{End}(A)\otimes\mathbf Q$ 上线性。应用于 $u=\delta$ 即得(6)。

由图形和两坐标轴的交数，
$$
D_\delta^2=-6.
\tag{7}
$$
具体地，$\Gamma_\delta^2=(A\times0)^2=(0\times A)^2=0$，
$\Gamma_\delta\cdot(A\times0)=3$，
$\Gamma_\delta\cdot(0\times A)=1$，
$(A\times0)\cdot(0\times A)=1$，代入(5)即得(7)。

定义两个真实代数对应
$$
\begin{aligned}
\mathscr C_\delta:\operatorname{CH}^3(X)&\longrightarrow
       \operatorname{CH}^2(W),&
\mathscr C_\delta(Z)
 &=p_{W,*}\bigl(Z\cdot p_{A^2}^*D_\delta\bigr),\\
\mathscr I_\delta:\operatorname{CH}^2(W)&\longrightarrow
       \operatorname{CH}^3(X),&
\mathscr I_\delta(Y)&=Y\times D_\delta.
\end{aligned}
\tag{8}
$$
Intersection product 用 refined pullback 理解，因此不要求临时选择处处横截的代表。由投影公式和(7)，
$$
\boxed{\mathscr C_\delta\mathscr I_\delta=-6\,\operatorname{id}.}
\tag{9}
$$
于是
$$
\boxed{
\mathscr P_\delta=-\frac16\mathscr I_\delta\mathscr C_\delta,
\qquad \mathscr P_\delta^2=\mathscr P_\delta
}
\tag{10}
$$
是 $X$ 上实际的 mixed CM Tate 投影。它与 $\epsilon_W,\epsilon_A$、作用在 $W$ 上的原 Hecke/nebentypus 投影和固定 finite-character descent 交换。它不需要 Tate 猜想，也不需要由一维 Betti 实现反推 Chow 同构。

## 3. 每个原 isogeny 的精确度数常数

在 $B$ 上令
$$
h_B=[c_B\delta]\in\operatorname{End}(B),\qquad
D_{h_B}=[\Gamma_{h_B}]-[B\times0]-3c_B^2[0\times B].
\tag{11}
$$
由 CM isogeny 的相容性，
$$
h_B\varphi=[c_B]\varphi[\delta].
\tag{12}
$$
因此原图形的实际推前满足
$$
(\operatorname{id}_B\times[c_B])_*
 (\varphi\times\varphi)_*D_\delta
 =d_\varphi D_{h_B}.
\tag{13}
$$
这里的 $d_\varphi$ 是映射到图形 $\Gamma_{h_B}$ 的真实度数。两坐标轴的推前分别给 $d_\varphi[B\times0]$ 与
$3d_\varphi c_B^2[0\times B]$，所以没有遗漏 axis 项。

左边处于 $h^1(B)\otimes h^1(B)$ 的 divisor 子群，$(\operatorname{id}\times[c_B])_*$ 在该子群上就是乘 $c_B$。这是椭圆曲线的实际 Chow–Künneth／乘法恒等式；也可用 Poincaré 除子的双线性直接证明。故
$$
\boxed{
(\varphi\times\varphi)_*D_\delta
 =\frac{d_\varphi}{c_B}D_{h_B}.
}
\tag{14}
$$

将(8)应用于(4)。因为 $\epsilon_A$ 自伴且固定 $D_\delta$，可以将其从图形移到 divisor；而 $\epsilon_W$ 与(8)交换。于是
$$
\mathscr C_\delta(\Delta_\varphi)
 =\epsilon_W i_{B,*}
     (\varphi\times\varphi)_*D_\delta.
\tag{15}
$$
Scholl 的两个 $h^1$ 投影杀掉(11)中的坐标轴。若记
$$
H_B=\epsilon_W i_{B,*}[\Gamma_{[c_B\delta]}]
       \in\operatorname{CH}^2(W)_0,
\tag{16}
$$
则得到精确的 Chow 等式
$$
\boxed{
\mathscr C_\delta(\Delta_\varphi)
 =\frac{d_\varphi}{c_B}H_B.
}
\tag{17}
$$
这给出 [BDP, §2.4, printed p.1064] 所述“同一 rational Heegner 线”的完整常数。在本篇所有原 conductor-34 项上，它就是 $d_\varphi/34$，不是1，也不能只按有限角色丢掉该 norm 因子。

## 4. 三个原有限角色与所有 norm 权重逐项运输

把 R814 的固定 cycle 写成其原有限构造
$$
\Delta_j=\mathscr E_j\sum_{a\in\mathcal O}
          b_{j,a}\Delta_{\varphi_a}.
\tag{18}
$$
这里 $\mathcal O$ 是原固定 orbit，$b_{j,a}$ **就是**原构造的有限 $\chi_j$ 权及 norm 权，$\mathscr E_j$ 包含原 $g$-投影、level 向量、descent 和实际角色投影。式(18)只是记下已有有限构造，不重新挑选轨道、权重或局部 test vector。

定义
$$
\boxed{
\mathcal H_j=\mathscr C_\delta(\Delta_j)
 =\mathscr E_j\sum_{a\in\mathcal O}
     b_{j,a}\frac{d_{\varphi_a}}{34}\,H_{B_a}.
}
\tag{19}
$$
因为 $D_\delta$ 定义在 $K$ 上，(19)与原 cycle-factor 的 Galois action 和三份 finite-character projector 交换。特别是(2)仍给三个真实不同的角色，而不是把 contraction 后的权重改成无角色 trace。

(9)–(10)同时给出原实际 mixed component 的反向公式：
$$
\boxed{
\mathscr P_\delta\Delta_j
 =-\frac16\,\mathcal H_j\times D_\delta.
}
\tag{20}
$$
这是对该 mixed component 的完整 Chow identity。本文没有把 $\Delta_j$ 的所有其它 CM 分量也认成(20)。

所有 $\mathcal H_j$ 与对应(8)都先于 p 固定。在原好 p 上，34、6以及固定 isogeny degrees的所有例外只占已允许删除的有限集合。

## 5. 原 de Rham 规范与 $-2\delta$ 常数

按 [BDP, (1.4.1)–(1.4.2)]，取唯一 CM 补方向 $\eta_A$ 满足
$$
[\delta]^*\eta_A=-\delta\eta_A,\qquad
\langle\omega_A,\eta_A\rangle_A=1.
\tag{21}
$$
BDP 的对称乘积记号在 $r=2,j=1$ 时准确为
$$
s_A=\omega_A\eta_A
=\frac12\bigl(p_1^*\omega_A\wedge p_2^*\eta_A
             +p_1^*\eta_A\wedge p_2^*\omega_A\bigr).
\tag{22}
$$
因此几何交换在 $s_A$ 上取负，与(6)一致。

令 $e=p_1^*\omega_A\wedge p_2^*\eta_A$，
$f=p_1^*\eta_A\wedge p_2^*\omega_A$。
对图形的定义性配对
$$
\int_{A^2}[\Gamma_\delta]\wedge p_1^*\xi\wedge p_2^*\zeta
  =\int_A\xi\wedge[\delta]^*\zeta
$$
分别取 $(\xi,\zeta)=(\omega_A,\eta_A)$ 与
$(\eta_A,\omega_A)$，得到其 cross coefficients 都是 $-\delta$。
故
$$
\boxed{\operatorname{cl}_{\mathrm{dR}}(D_\delta)
       =-\delta(e+f)=-2\delta\,s_A.}
\tag{23}
$$
这也独立核对 $\int D_\delta^2=-6$。符号来自原
$\langle\omega_A,\eta_A\rangle=1$ 与 Künneth wedge 次序；没有通过换 CM period 吸收它。

对原 $\omega'_g$ 的 Abel–Jacobi functoriality 现在给
$$
\operatorname{AJ}_{W,p}(\mathcal H_j)(\omega'_g)
 =\operatorname{AJ}_{X,p}(\Delta_j)
       \bigl(\omega'_g\wedge\operatorname{cl}(D_\delta)\bigr).
\tag{24}
$$
记左边为 $\mathcal B_{j,p}$，右边的原混合配对正是 R814(19)
的 $\mathcal A_{j,p}$，得到
$$
\boxed{\mathcal B_{j,p}=-2\delta\,\mathcal A_{j,p}.}
\tag{25}
$$
(24)使用原 algebraic de Rham cycle class 与其 Tate normalization；
$\omega_A$ 已固定为 $dx/(2y)$，不额外更换任何 $2\pi i$、
p-adic period 或 Artin 基。

## 6. 原负二值、固定素数检测和精确收益

代入 R814(31)，因为 $(-2\delta)^2=-12$，有
$$
\boxed{
\mathcal B_{j,p}^{\,2}
 =\frac{12\cdot34^4c_j\theta^9\Omega_p^4E_p^{\log}}
 {\mathfrak d_{j,p}\mathfrak u_{j,p}(0)
   E^{\mathrm{Iw}}_{j,p}E^{\mathrm{BDP}}_{j,p}}
 I_{j,-2,p}^{\,2}.
}
\tag{26}
$$
右端所有符号完全沿用 R814：原30平滑、$\sqrt{17}$ Artin基、
$\theta^9\Omega_p^4$、两种 ordinary Euler 和两真实换基因子均未删去。
各显示因子非零；不声称它们在全部目标 p 都是整数单位。
式(26)在值为零时仍成立，没有对可能为零的 AJ 或 L 值取比。

于是对每个原好 ordinary p，
$$
\boxed{
I_{j,-2,p}\ne0
\iff\mathcal B_{j,p}\ne0
\iff\mathcal A_{j,p}\ne0.
}
\tag{27}
$$
R817 在唯一固定普通素数7993的三条真实负二余值全部非零，
故本篇三份 **固定** $\mathcal H_j$ 均在
$\operatorname{CH}^2(W_F)_0\otimes\mathcal E$ 中非零。
它们处于同一有限扩域上三个互异的实际 $\chi_j$ eigensector；
对 cycle 因子施对应的有限群幂等元，证明三者在共同 Chow 模中线性独立。
这一论证不让系数同时随 Galois 共轭，也不由数值的不同大小推线性独立。

新增收益是：原三个负二值的指定 canonical mixed component，
现在有同一个先于 p 固定的 **三维普通 Heegner cycle 来源**，
并且有(17)、(20)、(25)的实际代数对应和准确常数。
不再仅说五维 generalized cycle 与某个抽象三维表示同构。

仍未支付的主门是：
- 这些 $W$ 上的 $\mathcal H_j$ 与 R831/R852 原端点 cycle 的实际对应；
- 非 Dirichlet CM 模形式 $g$ 的 Scholl Chow projector 到原
  $E_0^3$／$P_9$ 的指定、cycle-compatible 运输；
- 任意其它目标 p 的 $\mathcal B_{j,p}\ne0$；
- 原三个中央 Mellin 导数同时为零的排除。

## 7. 原文与所用范围

1. M. Bertolini, H. Darmon, K. Prasanna,
   *Generalized Heegner cycles and p-adic Rankin L-series*,
   Duke Math. J. **162** (2013), 1033–1148,
   [作者存档的发表全文](https://sites.lsa.umich.edu/kartikp/wp-content/uploads/sites/1326/2024/07/BDP1.pdf),
   DOI [10.1215/00127094-2142056](https://doi.org/10.1215/00127094-2142056).
   - (1.4.1)–(1.4.6), pp.1051–1053：CM splitting、cup normalization、
     几何 sign projector 及真实对称乘积；
   - (2.1.2)、(2.2.1)、§2.3：原 Scholl/projected graph cycles；
   - §2.4, p.1064：图形 $\sqrt{-d_K}$ 的 generalized-to-classical
     代数 correspondence。其 proportionality 常数由本篇§3自含计算；
   - §3.4：原 de Rham Abel–Jacobi 规范。
2. R814：共同固定 good pair、三份有限角色／norm 权重、原两 Euler、
   period及完整 AJ 平方式。
3. R817：唯一固定素数7993的三条实际非零检测。本篇不复跑、不扩大素数样本。
4. 椭圆曲线的 Chow–Künneth／Poincaré 除子双线性，亦可用
   [R852](R852-original-schoen-correspondence-and-exact-chow-inverse.md)
   已引用的 abelian-motive multiplication 与 actual CM line decomposition。

本文无新增数值计算、无新素数扫描、无可重算数据文件。
