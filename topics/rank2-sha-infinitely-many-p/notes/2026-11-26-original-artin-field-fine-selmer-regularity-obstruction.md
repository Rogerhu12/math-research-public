# 2026-11-26 — 原 Artin 场上的整场 regularity 不能代替最高分量的 fine Selmer 门

会话：Astra-rank2-Sha-7d29daa5-20261126 / global。
状态：原实际点给出的范围排除；不占新 R 号，不改变主目标未完成状态。

## 1. 本次核查的文献范围

Francesc Bars，
[On Jannsen's conjecture for Hecke characters of imaginary quadratic fields](https://mat.uab.cat/~francesc/JannHecke.pdf)，
Publ. Mat. (2007), 29–42，Definition 1.4、Lemma 1.6、Definition 2.2、
Proposition 2.4、Corollaries 2.6/2.8，已读原文。
其 ordinary regularity 不是 K 的类数为一；它是在相关 p-torsion 场上的
maximal pro-p extension 条件。Lemma 1.6 在 purely-local-type 条件及所列局部
coinvariant 消失下给全局 H² 消失。

同作者 [Weak Leopoldt's conjecture for Hecke characters](https://mat.uab.cat/~francesc/WLHecke.pdf)
的结论针对固定 p 的几乎所有 Tate twists，不指定本题的 h³(2)。
该量词不能换成固定 twist、无穷 p。

下面不尝试证明那种整场 regularity，而用本题已有的实际点说明，在为原
eta 加上必要固定域后，它会过强。

## 2. 原十八阶场已经包含秩二六次扭曲

沿 [R806 §2](../results/R806-original-type-four-order-eighteen-and-negative-two-katz.md)
(11)–(12)，令 H/K 是原 eta 的 cyclic18 场。已有准确身份
$$
\eta^3=\psi_{17}/\psi_0,\qquad
H^{I_2}=K(17^{1/6})\subset H. \tag{1}
$$
不是只从阶数猜测 Kummer 域。

设
$$
E_{17}:y^2=x^3+17,\qquad E_0:y^2=x^3+1,\qquad
F_p=H K(E_0[p]).
\tag{2}
$$
对原普通 p>211，令 S_p(F_p) 为 F_p 的 p 上素点。
由于 (1)，在 F_p 上有明确同构
$$
E_{17}\longrightarrow E_0,\qquad
(x,y)\longmapsto(x/\theta^2,y/\theta^3),\quad \theta^6=17.
\tag{3}
$$

[R294](../results/R294-jzero-exact-rank-two-by-rational-three-isogeny.md)
已经完整证明 E17(Q) 秩二，原 P=(-2,3)、Q=(-1,4) 独立。
它们在 E17(K) tensor Q 中还在 K 上独立。
确证：若 aP+bQ=0，写 a=a0+a1 delta、b=b0+b1 delta，a_i,b_i∈Q。
外部复共轭固定 P、Q、将 delta 变为 -delta。原等式与共轭式相减，再用
delta 是非零 CM 同源，得 a1P+b1Q=0；独立性迫 a1=b1=0，
同理 a0=b0=0。因此
$$
P,Q,\delta P,\delta Q
\quad\text{在 }E_{17}(K)\otimes\mathbf Q\text{ 中 Q-线性独立}.
\tag{4}
$$

## 3. 原点的 Kummer 类给整场 fine Selmer 非零

令 V17=V_pE17。由 Kummer 单射，(4) 给 H¹(K,V17) 中四维 Qp 子空间 W。
这些是原实际点的类，不依赖 Sha 有限。

在两个 p 上素点，局部连续 Kummer 像的维数各为一：
准确地使用 E17(K_v) 的 p 进完备化再 tensor Qp。
在有限 v 不在 p 上，局部 p 进完备化是有限群，tensor Qp 后为零。
复地方不贡献。因此 W 的完整局部化映射的像维数至多二，故
$$
\dim_{\mathbf Q_p}\ker\left(
 W\longrightarrow\prod_v H^1(K_v,V17)
\right)\ge2. \tag{5}
$$
特别这里的核在 p 的两个素点都为零，不是只用一个 ordinary 条件。

有限扩张的 restriction 在有理 H¹ 单射：corestriction 与 restriction 的复合
是非零整数 [F_p:K]。将 (5) 限制到 F_p，再用实际同构 (3)，保留至少二维
E0 点的 Kummer 类，并在 F_p 的全部地方仍局部为零。

E0 在 K(E0[p]) 上处处有良好约化：在原坏位其潜在良好约化惯性像有限，
而 p>211 时矩阵同余核是无挠 pro-p 群；E0[p] 已平凡，故有限惯性像为一。
这亦是 Bars 原文 §2 使用的同一 good-reduction 事实。
继续扩到 F_p 不破坏良好约化。于是上述点的 Kummer 类在 p 外未分歧，并属于
$$
H^1_{\mathrm{fine}}(F_p,V_pE_0)
:=\ker\left(
H^1(G_{F_p,S_p(F_p)},V_pE_0)
 \longrightarrow\bigoplus_{w\mid p}H^1((F_p)_w,V_pE_0)
\right).
$$
由此得到实际的无条件下界
$$
\boxed{
\dim_{\mathbf Q_p}H^1_{\mathrm{fine}}(F_p,V_pE_0)\ge2.
}
\tag{6}
$$
本篇没有把 (6) 投影到最高 lambda：它首先来自 E17 的 weight-one 字符，
这一点不能删除。

局部 H⁰((F_p)_w,V_pE0)=0，因为有限局部数域的椭圆曲线 p 幂挠群有限。
Weil 配对给 V_pE0^*(1)=V_pE0。
Poitou–Tate 的完整开头因此识别 fine H¹ 与相应全局 H² 的对偶，得到
$$
\boxed{
\dim_{\mathbf Q_p}H^2(G_{F_p,S_p(F_p)},V_pE_0)\ge2.
}
\tag{7}
$$
复地方使用通常的 modified local cohomology，为零。

## 4. 对实际候选输入的后果与边界

Fp 已包含 E0[p]，E0 的 p∞ 表示因而通过
G_{F_p,S_p(F_p)}(p)；并由良好约化在 p 外未分歧。
若这个 maximal pro-p Galois 群在某个 w|p 是 Bars Definition 1.4 的
purely local type，取 Lemma 1.6 中 S'=S=S_p(F_p)、
M=E0[p∞]、j=0。

所需 M(-1) 的局部 coinvariant 为零：其 Pontryagin 对偶是
(T_pE0)^*(1) 的局部 H⁰，借 Weil 配对即 T_pE0 的 H⁰，为零。
Lemma 1.6 遂给 H²(G_{F_p,S_p(F_p)},E0[p∞])=0，
并由该文 Lemma 1.2 给 H²(G_{F_p,S_p(F_p)},V_pE0)=0，
与 (7) 矛盾。

所以原必要 Artin 场加入后，这种整场 purely-local-type 输入不能成立。
不能因 K 类数一、E0(Q) 秩零、或先在 K(E0[p]) 看到了某个性质，
就不经证明将该性质搬到 Fp。

这只排一个过强的整场方法。它不证明原
rho=eta^e psi0³ epsilon_cyc^{-1} 的 H² 非零，也不否定某个最高
lambda 分量的 fine Selmer 消失；所需分量仍须单独处理。
R940/R945 的 c1≠0 条件、原 ordinary 门、以及无穷系数 p 均保持。

未执行数学程序；所用原曲线、原角色和原点均已有仓库完整证明。
