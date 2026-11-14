# 全部范数解析代数动作：返回第一 chaos 即迫循环

日期：2026-11-12（UTC）。独占稿：critical_kernel。
状态：**已证明。** 从 R117 的第一 chaos 乘子动作扩到任意 T∈𝓐，但结论表述为一个条件性循环判据；不声称所有第一 chaos 向量已循环。

## 1. 主定理

设

$$
0\ne h=a_*+\sum_{j\ge0}a_j\chi_j,\qquad a\in\ell^1.
$$

因此 h 是有界第一 chaos，R88 给实际乘子 X_h∈𝓐，X_h1=h。

**定理 1.1。** 若存在一个非标量 T∈𝓐，使

$$
Th\in H_{\le1},
\tag{1}
$$

则 h 对实际 A 循环。

等价地，若某个这样的 h 非循环，那么

$$
\boxed{\{T\in\mathcal A:Th\in H_{\le1}\}=\mathbb CI.}
\tag{2}
$$

其中标量算子当然都保持该向量位于第一层。这里不要求 T 的符号本身具有有限 Walsh 次数。

更精确地，设 k=Th、λ=c_0(T)。若 h(0)=0，则

$$
b:=k-\lambda h
$$

仍是有界第一 chaos，b(0)=0，其一次系数满足

$$
\boxed{|b_j|\le C\eta_{j-1}\quad(j\ge1),}
\tag{3}
$$

C 为固定常数。若 T 非标量，b≠0；由 R102，b 循环，继而 h 循环。

## 2. 归一化形式系数的平方和界

用 R32 的形式系数 λ_n(X)，记

$$
\widehat X(n)=W_n\lambda_n(X),\qquad W_n=\|A^n\|.
$$

**引理 2.1。** 对全部 X∈𝓐，

$$
\boxed{\sum_{n\ge0}|\widehat X(n)|^2\le\|X\|^2.}
\tag{4}
$$

可用 UHF 的单边移位表示证明；这里给一个只用已有等距圆作用的证明。

R32 的 γ_{e^{it}} 是范数连续等距作用，且 γ_{e^{it}}(A)=e^{it}A。
对任意单位向量 u，H 值函数 t↦γ_{e^{it}}(X)u 的第 n 个 Fourier 系数为 λ_n(X)A^nu。有限 Fourier Bessel 不等式给

$$
\sum_{n=0}^{N}|\lambda_n(X)|^2\|A^nu\|^2
\le
\frac1{2\pi}\int_0^{2\pi}
\|\gamma_{e^{it}}(X)u\|^2dt
\le\|X\|^2.
\tag{5}
$$

取 m 使 2^m>N，并令 u 为前 m 个物理位全0的归一化示性向量，后尾为 plus 常数。对 0≤n<2^m，实际 A^n 在这个输入上不发生 m 位边界进位，其权积精确为 W_n，故

$$
\|A^nu\|=W_n.
$$

代入 (5) 得任意有限部分和的界，令 N→∞ 即得 (4)。
这里不用把非 dyadic 的 γ 实现为当前表示中的酉。

## 3. 正阶因子相乘必在 dyadic 系数处支付一次完整进位

**引理 3.1。** 若 X,Y∈𝓐，c_0(X)=c_0(Y)=0，则对 j≥1，

$$
\boxed{
|\widehat{XY}(2^j)|
\le
\eta_{j-1}\|X\|\|Y\|.
}
\tag{6}
$$

对 1≤s<2^j，令 k=v_2(s)。二进位相加 s+(2^j−s)=2^j
从第 k 位一直进位到第 j 位。用 d_{\ell+1}/d_\ell²=η_\ell，得精确恒等式

$$
\frac{W_{2^j}}{W_sW_{2^j-s}}
=
\prod_{\ell=k}^{j-1}\eta_\ell
=
\frac{\alpha_j}{\alpha_k}
\le\eta_{j-1}.
\tag{7}
$$

等价地，W_sW_{2^j-s}=d_k²∏_{\ell=k+1}^{j-1}d_\ell；逐次使用 d_{\ell+1}=η_\ell d_\ell² 即可验证。

R32 的形式卷积和两个零常数给

$$
\widehat{XY}(2^j)
=
\sum_{s=1}^{2^j-1}
\widehat X(s)\widehat Y(2^j-s)
\frac{W_{2^j}}{W_sW_{2^j-s}}.
$$

用 (7)、Cauchy–Schwarz 和 (4)，得到 (6)。这比逐项范数估计中的
2^j 因子更强。j=0 的 1 阶系数直接为零。

## 4. 第一 chaos 的 dyadic 系数恢复

对有界第一 chaos

$$
b=b_*+\sum_jb_j\chi_j,\qquad (b_j)\in\ell^1,
$$

R88 给

$$
X_b=b(0)I-2\sum_jb_jY_j.
\tag{8}
$$

由 Y_\ell=N_\ell(I+N_\ell)^{-1} 的真实解析展开，对 j≥0，

$$
\boxed{
\widehat{X_b}(2^j)
=
-2b_j+
2\sum_{\ell<j}b_\ell\kappa_{\ell j},
}
\tag{9}
$$

其中

$$
\kappa_{\ell j}
=
\frac{d_j}{d_\ell^{2^{j-\ell}}}
=
\|N_\ell^{2^{j-\ell}}\|.
$$

当 ℓ<j，指数 2^{j−ℓ} 为偶数，所以 Y_\ell 在该阶的符号为负，
再乘 (8) 的 −2 给 (9) 的正号。

不断进位给

$$
\kappa_{\ell j}
=
\eta_\ell^{2^{j-\ell-1}}
\eta_{\ell+1}^{2^{j-\ell-2}}\cdots\eta_{j-1}
\le\eta_{j-1}.
$$

因此

$$
|b_j|
\le
\tfrac12|\widehat{X_b}(2^j)|
+\eta_{j-1}\sum_\ell|b_\ell|
\qquad(j\ge1).
\tag{10}
$$

j=0 时为 b_0=−widehat(X_b)(1)/2。

## 5. 从返回动作得到已知循环类

先说明 k=Th 若在第一 chaos，就自动有 ℓ¹ 系数：
T X_h 是有界交换子，且 (T X_h)1=k。由 1 循环，它是 k 的唯一实际有界乘子。R88 的第一 chaos 有界乘法判据于是给 k 的一次系数属于 ℓ¹，且

$$
X_k=T X_h.
\tag{11}
$$

若 h(0)≠0，X_h 的字符非零，直接可逆，h 已循环。以下设 h(0)=0。

令 λ=c_0(T)、b=k−λh。由 (11)，

$$
X_b=(T-\lambda I)X_h.
\tag{12}
$$

两个因子的字符都为零，故由 (6)，

$$
|\widehat{X_b}(2^j)|
\le
\eta_{j-1}\|T-\lambda I\|\|X_h\|.
$$

结合 (10)，

$$
|b_j|
\le
\eta_{j-1}
\left(
\tfrac12\|T-\lambda I\|\|X_h\|
+\sum_\ell|b_\ell|
\right).
$$

这证明 (3)。同时 b(0)=c_0(X_b)=0。

实际权满足

$$
\eta_{j-1}\le e^{-770\,16^{j-1}},
\qquad
-\log\alpha_j\le\Lambda_j\le100\,16^j.
$$

故例如存在固定 C'，使

$$
|b_j|\le C'\alpha_j^{1/4}.
\tag{13}
$$

有限的早期项不影响此结论。R102 已证明任何非零临界第一 chaos 向量，若其系数受 C'α_j^θ（某个 θ>0）控制，则对全 H 循环。因此只要 b≠0，b 循环。

若 b=0，则由 (12)，

$$
(T-\lambda I)X_h=0.
$$

h≠0 使 X_h≠0；R32 的代数内无零因子迫 T=λI，与非标量假设矛盾。因此 b≠0，b 循环。

最后 b=(T−λI)h 属于 h 的闭 A 循环子空间，因为 T−λI∈𝓐 是多项式的范数极限。该子空间又包含 b 的全部 A 多项式轨道，所以 h 循环。定理得证。

## 6. 与 R117、R104 以及实际缺口的关系

R117 对任何非恒定第一 chaos 输入（允许仅 ℓ² 系数）与有界第一 chaos 乘子给出更具体的次数刚性：重叠位会产生无限次数，不重叠时产生非零二阶项。

本稿把作用算子扩大到全部 𝓐，但输入要求是有界第一 chaos；
结论是“存在一次非标量返回动作就迫 h 循环”，并没有分类所有一般 T 对指定 h 的动作。

若固定 g≠0 的消去空间中存在非零有界第一 chaos h，
则 h 不可能循环。于是任何 T∈𝓐 若把这个 h 送回第一层，都必须是标量。
这精确排除了用现成非标量 𝓐 作用在第一层内部制造无限族的路线，但不证明该消去空间没有 h。

本稿不覆盖一般无界第一 chaos 输入，也不自动覆盖
T∈{A}'\𝓐。完整第一 chaos 循环性、A 的普通不变格及 Hilbert ISP 仍未解决。

## 7. 有限和版本与代数平方的严格不闭性

令 𝔪=ker c_0⊂𝓐，𝔪² 指有限和 span{XY:X,Y∈𝔪}，不在定义中取闭包。

**推论 7.1。** 若一个第一 chaos 符号 b 的实际乘子可写成

$$
X_b=\sum_{\ell=1}^L X_\ell Y_\ell,
\qquad X_\ell,Y_\ell\in\mathfrak m,
\tag{14}
$$

则 b 的一次系数满足 |b_j|≤Cη_{j−1}（j≥1）。若 b≠0，则 b 对全 H 循环。

**证明。** (14) 本身给有界乘子，所以若开始仅知 b∈H≤1，R88 也自动给 b 的系数属于 ℓ¹。由引理3.1，

$$
|\widehat{X_b}(2^j)|
\le\eta_{j-1}
\sum_{\ell=1}^L\|X_\ell\|\|Y_\ell\|.
$$

再用 (10) 即得系数界。字符为零，所以 b(0)=0；非零时由 (13) 和 R102 得循环性。证毕。

**推论7.2。** 𝔪² 是 I_2=closure(A²𝓐) 的真稠密子空间。存在明确非零 S，使其闭主理想恰为 I_2，但 S∉𝔪²。

取任意 c>0，设 a_0=0、a_j=e^{-c(j+1)^4}（j≥1），并令

$$
S=\sum_{j\ge1}a_jY_j.
\tag{15}
$$

其首非零阶为2；降序系数满足Γ(a)=+∞，故R116给

$$
\overline{S\mathcal A}=I_2.
\tag{16}
$$

而 S1=∑_{j≥1}a_jx_j 的第一Walsh系数为 −a_j/2。若S∈𝔪²，推论7.1将迫a_j≤Cη_{j−1}。但

$$
\frac{a_j}{\eta_{j-1}}
\ge
\exp\!\left[770\,16^{j-1}-c(j+1)^4\right]
\longrightarrow\infty,
$$

矛盾。因此S∉𝔪²。

最后，𝔪²⊂I_2 来自两个零字符因子的形式阶；另一方面
A²𝓐⊂𝔪²，因为A²U=A(AU)，两因子均在𝔪。取闭包给

$$
\boxed{\overline{\mathfrak m^2}=I_2,
\qquad\mathfrak m^2\ne I_2.}
\tag{17}
$$

这精确区分闭主理想标准与有限个正阶因子的代数分解。这里不把它扩大成关于一般不连续导数或所有闭理想的结论。

内部依赖：R32、R88、R102、R116；与 R117 的独立逐式核验结论一致。
