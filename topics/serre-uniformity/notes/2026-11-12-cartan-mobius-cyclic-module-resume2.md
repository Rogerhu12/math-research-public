# 完整 Cartan 的 Möbius 恒等式与例外 Fourier 理想的循环模接口

日期：2026-11-12。状态：已证结构接口与明确未解步骤；不登记新 R 结果，不宣称一般素数无 exceptional。

恢复说明：原工作环境不可用，本文由此前已经完成并独立检查的推导及会话记录重建，不能保证与原暂存文件逐字相同。数学内容保留；另明确区分“由 U 与 w 生成的群包含 PSL₂”与“恰为 PSL₂”，并说明直接循环模证明只需特征不整除 3p。

## 1. 问题、来源与适用范围

令 p>37 为素数，p≡2 (mod 3)，取 z∈F_p^× 为非平方，
τ²=z，F_{p²}=F_p(τ)。取阶恰为 3 的乘法字符

\[
\chi:\mathbf F_{p^2}^{\times}\longrightarrow\{1,\omega,\omega^2\},
\qquad \omega^2+\omega+1=0.
\]

因为 3∤p−1，χ 在 F_p^× 上平凡。又 τ²∈F_p^×，故 χ(τ)=1。定义 P¹(F_p) 上的真 Cartan 颜色函数

\[
f(b)=\chi(1+b\tau)\quad(b\in\mathbf F_p),\qquad f(\infty)=1.
\tag{1.1}
\]

这里 χ 是有限域乘法字符，并非任选的三分割。将值域嵌入一个代数闭域 k，假设 char(k)=ℓ 不整除 3p；特征零的论证相同。取本原 p 次单位根 ξ∈k。

设 B_j={b∈F_p:f(b)=ω^j}，m=(p+1)/3。商 F_{p²}^×/F_p^× 的三个字符纤维各有 m 个射影点，且 ∞ 属于颜色 0，因此

\[
|B_0|=m-1,\qquad |B_1|=|B_2|=m.
\tag{1.2}
\]

χ(1−zb²)=1 给出

\[
f(-b)=f(b)^{-1},\qquad B_0=-B_0,\qquad B_2=-B_1.
\tag{1.3}
\]

本文针对 Studnia 预印本 arXiv:2507.20801v2 §3.1 的 exceptional 条件。其 Lemma 3.1.5/Proposition 3.1.6 将所需尖点微分单位条件与下述 U 生成模联系起来；这些论文结果的发表状态和条件仍须保留。本文的有限群恒等式及循环模论证在此完整给出，不把作者“无 exceptional”猜想当作定理。

原文：
https://arxiv.org/html/2507.20801v2

仓库接口：R66（实际 Tate 素数及小惯性三次角色）、R92（四个固定层的严格 Bézout 单位理想证书）、notes/2026-11-12-exceptional-pure-gauss-obstruction-resume2.md（纯 Gauss/Jacobi 恒等式不足以证明共同非零）。

## 2. 完整 Möbius 乘法恒等式

令

\[
w(b)=\frac1{zb},\qquad w(0)=\infty,\quad w(\infty)=0,
\qquad d_t=1-zt^2\quad(t\in\mathbf F_p).
\]

由于 z 非平方，所有 d_t 非零。对全部 b∈P¹(F_p)、t∈F_p，有

\[
\boxed{\ f(w(b)+t)=f(t)\,f(d_t b-t).\ }
\tag{2.1}
\]

这里仿射变换固定 ∞。证明如下。先取 b≠0,∞。乘以 bτ 不改变 χ 值，故

\[
f(w(b)+t)
=\chi((1+ztb)+b\tau).
\]

另一方面

\[
(1+t\tau)(1+(d_t b-t)\tau)
=d_t\big((1+ztb)+b\tau\big).
\]

因为 χ(d_t)=1，得到 (2.1)。b=0 时左侧为 1，右侧为 f(t)f(−t)=1；b=∞ 时两侧均为 f(t)。因此没有遗漏极点或零点。

取逆值也得

\[
f(w(b)+t)^{-1}=f(t)^{-1}f(d_t b-t)^{-1}.
\tag{2.2}
\]

特别 t=0 给出 f∘w=f，而不只颜色 0 保持。

这一恒等式使用真实有限域乘法。单有颜色大小、反演对称、纯 Gauss 和及 Jacobi 卷积，并不能推出它；上述纯 Gauss 障碍笔记已有保持那些较弱条件而发生共同 Fourier 零的非 Cartan 反例。

## 3. U 循环模及共同 Fourier 零

令

\[
V=\left\{v:\mathbf P^1(\mathbf F_p)\to k:
\sum_{b\in\mathbf P^1(\mathbf F_p)}v(b)=0\right\}.
\]

restriction 到有限点是 k-线性同构 V≅k^{F_p}，因为 ∞ 的值由有限点之和确定，故 dim V=p。由 (1.2)，f 和 f^{-1} 均在 V，且

\[
\sum_{b\in\mathbf F_p}f(b)
=\sum_{b\in\mathbf F_p}f(b)^{-1}=-1.
\tag{3.1}
\]

定义算子

\[
(T_t v)(b)=v(b+t),\qquad
(D_d v)(b)=v(db),\qquad
(Wv)(b)=v(w(b)).
\]

T_t,D_d 固定 ∞；W 交换 0,∞。它们保持 V。令 U={T_t:t∈F_p}，并设

\[
M=\operatorname{span}_k\{T_t f,T_t f^{-1}:t\in\mathbf F_p\}
\subseteq V.
\tag{3.2}
\]

对 a∈F_p，写

\[
S(a)=\sum_{b\in\mathbf F_p}f(b)\xi^{ab}.
\tag{3.3}
\]

f^{-1} 的对应 Fourier 坐标等于 S(−a)。因为 ℓ≠p，U 的 p 个字符互异，Fourier 变换可逆。因此第 a 个 U 特征线出现在 M 中，当且仅当 S(a),S(−a) 不同时为零。a=0 的坐标由 (3.1) 恒非零。故

\[
Z=\{a\in\mathbf F_p^\times:S(a)=S(-a)=0\},
\qquad
\dim M=p-|Z|.
\tag{3.4}
\]

若 P_j(X)=Σ_{b∈B_j}X^b，则对 a≠0，

\[
P_0(\xi^a)+P_1(\xi^a)+P_2(\xi^a)=0,
\]

\[
S(a)=P_0(\xi^a)+\omega P_1(\xi^a)+\omega^2P_2(\xi^a),
\]

\[
S(-a)=P_0(\xi^a)+\omega^2P_1(\xi^a)+\omega P_2(\xi^a).
\]

三阶 Fourier 矩阵的行列式在 char≠3 时非零，因而

\[
S(a)=S(-a)=0
\iff P_0(\xi^a)=P_1(\xi^a)=P_2(\xi^a)=0.
\tag{3.5}
\]

所以一般无 exceptional 的所需结论正是 M=V；对于固定的 k、ξ，也可只问相应的 a 是否属于 Z。

## 4. Weyl 稳定性恰好等价于共同非零

### 命题 4.1

在上述设定中，下列三项等价：

1. M=V；
2. WM=M；
3. 对每个 t∈F_p，D_{d_t}f 与 D_{d_t}f^{-1} 均属于 M。

证明。由 (2.1)、(2.2)，

\[
WT_t f=f(t)\,D_{d_t}T_{-t}f,\qquad
WT_t f^{-1}=f(t)^{-1}D_{d_t}T_{-t}f^{-1}.
\tag{4.1}
\]

并有 D_d T_s=T_{s/d}D_d。M 对所有 T_s 稳定，故 (4.1) 给出 2⇔3；包含 WM⊆M 即已因 W²=1 成为相等。

若 3 成立，则对每个 d=d_t，D_d 将 M 的全部平移生成元送入 M，故 D_d M⊆M。D_d 可逆且 dim M 有限，因此 D_d M=M。

集合

\[
\mathcal D=\{1-zt^2:t\in\mathbf F_p\}
\]

含恰好 (p+1)/2 个非零元素。F_p^× 的任意真子群至多有 (p−1)/2 个元素，所以 D 生成全部 F_p^×。于是 M 对每个非零乘子稳定。Fourier 支撑也随乘子作用稳定，故其缺失集合 Z 要么为空，要么等于 F_p^×。

后者将迫使 f 在有限点上只有第 0 个 Fourier 坐标，即 f 在 F_p 上为常数。但 (1.2) 中三个颜色均出现，且 char(k)≠3 时 1,ω,ω² 互异，矛盾。因此 Z=∅，M=V。1⇒2 显然。证毕。

直接证明仅用 ℓ∤3p，不需 Maschke 或 Hecke 投影的整性。在本题真实 Tate 素数 ℓ>p+1 时，也可另用群表示论检查：U 与 w 共轭得到上下三角幺幺元，故它们生成的群包含 PSL₂(F_p)；当 w 的行列式平方类不平凡时还包含额外的 PGL₂ 元，不能一律写成“恰为 PSL₂”。PSL₂ 在 P¹ 上二重传递；ℓ 不整除其阶时，增广表示绝对不可约，因而一个非零的 W、U 稳定子模必为 V。

### 这里尚未证明什么

f 与 f^{-1} 本身确实都被 W 固定。但是

\[
Wf=f,\quad Wf^{-1}=f^{-1}
\]

不能推出 W 稳定它们的 U 张成空间。W 不与 U 交换；公式 (4.1) 恰把这个缺口写成“需要控制额外的乘子 D_{d_t}”。

试图通过 Fourier 插值将 D_d f 写成 U 平移组合时，会在第 a 个频率除以 S(a) 或 S(−a)。这些正是待证明不共同为零的数。未经独立证明的这种插值是循环论证。

同样，完整群作用的不可约性只保证由所有群元生成 f 可得 V，不保证仅用 U 的轨道就已生成 V。Maschke 不会补上这一步。

因此命题 4.1 是精确等价接口，没有消除 exceptional 素数。若将来能不依赖待证非零性地证明这些乘子保持 M，就能真正完成所需一般 Fourier 步骤。

## 5. 实际 Tate 素数的精确 Frobenius 条件

令 E/Q 的 mod p 像在完整非分裂 Cartan 正规化子中，K 为正规化子商二次域。设 ℓ≠p 且 v_ℓ(j(E))<0。Tate 模型及其二次扭曲使 Frobenius 的两个特征值在共同符号之外为 1,ℓ。

非分裂 Cartan 中拥有 F_p 特征值的半单元素必须为标量；正规化子外陪集的矩阵迹为零。因此实际条件为

\[
\boxed{\ \ell\equiv\varepsilon_K(\operatorname{Frob}_\ell)
       \pmod p,\quad
\varepsilon_K(\operatorname{Frob}_\ell)\in\{1,-1\}.\ }
\tag{5.1}
\]

正规化子的阶不含 p，也排除 Tate 参数的非平凡模 p 幺幺惯性。这里保留 R66 的完整局部前提，不把任意 ℓ≡±1 (mod p) 都称为实际分母素数。

因为 p>37，素数 ℓ≡±1 (mod p) 必满足

\[
\ell\ge2p-1>p+1,\qquad \ell\nmid 3p(p^2-1).
\tag{5.2}
\]

令 e∈{±1} 为 ℓ mod p，d∈{±1} 为 ℓ mod 3。对任何 a∈F_p，在特征 ℓ 中逐项取 Frobenius 得

\[
\boxed{\ S(a)^\ell=S(de\,a).\ }
\tag{5.3}
\]

当 d=1 时，这是 ξ^\ell=ξ^e；当 d=−1 时，再用 f(b)^{-1}=f(−b) 即得。该公式只用取值与反演对称，并非额外的完整 Cartan 乘法结论。

若 de=−1，S(a) 与 S(−a) 是 F_{ℓ²}/F_ℓ 共轭，故一个为零等价于两个均为零。但是它仍是一个二次域元素的两个 F_ℓ 坐标同时为零的问题，没有自动得到非零。

若 de=1，两者各自属于 F_ℓ，仍可能同时为零，不能仅凭它们位于基础域便排除。

只有在 K=Q(√−3) 时，才有 ε_K(Frob_ℓ)=d；于是 e=d，实际分母进一步满足

\[
\ell\equiv1\pmod{3p}\quad\hbox{或}\quad
\ell\equiv-1\pmod{3p},
\tag{5.4}
\]

且两处符号相同。对于变化的 K，不能把这一特殊约束推广为一般结论。

## 6. 对当前主问题的准确贡献与剩余任务

本笔记给出两个可以复用的严格接口：

- 完整 Cartan 的乘法条件具体成为 (2.1) 的 Möbius 变换律；它比纯 Gauss/Jacobi、颜色平衡或反演对称更强。
- 无共同 Fourier 零恰等价于 M 的 Weyl 稳定性；所缺步骤具体是将 D_{1-zt²}f 与其逆色函数纳入 U 生成模，而不是泛称“还需更多整性”。

R92 的四个固定层证书依然只处理那些层。作者的广泛数值检验以及一般无 exceptional 猜想不提供全 p 的证明。实际 Tate Frobenius (5.3) 没有自行消除上述共同零。即使将来完成这一 Fourier 步骤，三次 Brandt 周期的非消失条件仍是另一个需要分别处理的全局缺口。
