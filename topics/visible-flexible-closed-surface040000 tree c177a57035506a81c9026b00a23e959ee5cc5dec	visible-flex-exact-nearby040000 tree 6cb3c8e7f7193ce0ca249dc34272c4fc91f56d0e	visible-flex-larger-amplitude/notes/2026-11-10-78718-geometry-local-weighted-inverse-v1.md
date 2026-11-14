# 有限头部局部逆：真通量逆加正 gain 的 log 权闭包

作者：Astra-visible-flex-78718bd0 / geometric_closure，2026-11-10。

**状态：完整算子证明，待未参与者独审。** 本文处理 R513 中已具有
真实无权逆的局部代数环节，不是 R518 的未知全网络低逆，也不构造新
Darboux 零点。其作用是：只要实际有限 cell 的物理传播和正 gain 表
已经给出，这几处 weighted 逆不再需要相对原径向背景的小量门。
绝不从抽象 unitary 单独推 log 正则。

实际读源：R513 `results/R513-direct-log-physical-local.md`，97134 B，
SHA256 `637cdf810765fa5913065b3618ad4025d9bbbcc6f98fcb49489df21288ffbca9`，
root 从提交 `f21a4f07127e4f59b50f65bae444bfeb60248d40` 单取，工具719865。
本次核读其 §§12.2–13.5 的实际 Gram、J-polar、transmission、source 公式。
没有假装重审该文全部上游。

## 1. 统一的正权 bootstrap

在 $\mathscr H=L^2(S^1;\mathbb C^d)$ 上，或其一个被所有以下算子和
Fourier 投影保持的实际闭子空间上，置
$$
\Phi(j)=\log(e+|j|)^{3/2},\quad W_\rho(j)=e^{\rho\Phi(j)},\quad
X_\rho^s=\left\{u:\sum_jW_\rho(j)^2\langle j\rangle^{2s}|u_j|^2<\infty\right\}.
\tag{1}
$$
固定 $\rho>0$、$s\in\mathbb R$、$\kappa>0$。
设真实 $T=I+R$ 在 $\mathscr H$ 上双向有界可逆，且
$$
\|T^{-1}\|_{\mathscr H\to\mathscr H}\le N,
\qquad
\|R\|_{\mathscr H\to H^\kappa}\le C_0,
\qquad
\|R\|_{X_\rho^s\to X_\rho^{s+\kappa}}\le C_\rho.
\tag{2}
$$
这里后两个是该同一真实 $R$ 的正 gain 表，不是从第一项推得的结论。
取整数 $J\ge1$ 使
$$
\langle J\rangle^{-\kappa}\max(C_0,C_\rho)\le\frac12.
\tag{3}
$$
定义准确有限常数
$$
m_{\rho,s,J}=\max_{|j|\le J}W_\rho(j)\langle j\rangle^s,
\qquad e_{\rho,s}=\sup_jW_\rho(j)^{-1}\langle j\rangle^{-s}.
\tag{4}
$$
$e_{\rho,s}<\infty$。例如
$$
e_{\rho,s}\le
\exp\left(\frac{4\max(-s,0)^3}{27\rho^2}\right)
\tag{5}
$$
是一个可直接使用的上界：对 $s<0$，令 $x=\log(e+|j|)$，
$\log\langle j\rangle\le x$，再最大化 $|s|x-\rho x^{3/2}$；
$s\ge0$ 时取上界1。

**引理。** 真实无权 $T^{-1}$ 限制为 $X_\rho^s$ 的双向有界 inverse，且
$$
\|T^{-1}\|_{X_\rho^s\to X_\rho^s}
\le 2+(1+2C_\rho)m_{\rho,s,J}N e_{\rho,s}.
\tag{6}
$$
不要求 $\|R\|<1$，不另假有限低矩阵可逆。

**证明。** 令 $P=P_{|j|\le J}$，$Q=I-P$。
由 (2)–(3)，$QRQ$ 在 $\mathscr H$ 与 $QX_\rho^s$ 上的 norm 都不超过
$1/2$。所以 $I_Q+QRQ$ 在这两个空间均有真正 Neumann inverse，norm
至多2；在共同输入上由无权 injectivity 识别为同一个算子。

对 $f\in X_\rho^s\subset\mathscr H$，取已存在的真实解
$u=T^{-1}f\in\mathscr H$。其高分量满足
$$
(I_Q+QRQ)Qu=Qf-QRPu.
\tag{7}
$$
$Pu$ 在有限 Fourier 空间，故属于 $X_\rho^s$；(2) 保证右端也在该空间。
在 $X_\rho^s$ 中对 (7) 求逆，再由无权唯一性，其解恰为原 $Qu$。
于是 $u\in X_\rho^s$，并且
$$
\begin{aligned}
\|u\|_{X_\rho^s}
&\le\|Pu\|_{X_\rho^s}
 +2\bigl(\|f\|_{X_\rho^s}+C_\rho\|Pu\|_{X_\rho^s}\bigr)\\
&\le2\|f\|_{X_\rho^s}
 +(1+2C_\rho)m_{\rho,s,J}\|u\|_{\mathscr H}\\
&\le\bigl[2+(1+2C_\rho)m_{\rho,s,J}N e_{\rho,s}\bigr]
       \|f\|_{X_\rho^s}.
\end{aligned}
$$
这证明 (6)。$T=I+R$ 本身在 $X_\rho^s$ 有界，两边 identity 由同一
无权 identity 限制得到。证毕。

如果先有 $T=A+S$，其中 $A$ 为给定的双向可逆完整 Fourier matrix，
可以对 $A^{-1}T=I+A^{-1}S$ 应用本引理。
所有 $A^{\pm1}$ 的真实有限 norm、mean 和 low blocks 必须保留。

## 2. 负权、adjoint 和真实差

若对真实无权 adjoint $R^*$ 也有 (2) 的正权表，分别应用 §1。
由无权配对，$(X_\rho^{-s})^*=X_{-\rho}^{s}$；
对 $(T^*)^{-1}$ 的正权 inverse 取真 adjoint，便得到 $T^{-1}$ 在
$X_{-\rho}^s$ 的连续延拓。
它在 Fourier core 上与原无权 inverse 一致，两个 identity 先在 core
成立，再由密度与有界性延拓。这不把负权 completion 的元素一律称为
distribution，也不选择一个新的 source realization。

因此，若实际有限表包含全部正/负权、所需 adjoint 和有限 $s$ 档，
只须在开始时对该有限表共同选择 $J$，就得到同一套真实逆。
没有在每一步按新的输出宽差或当前迭代数改 cut。

对同一实现中的两个真实对象 $T_0,T_1$，若
$$
\|T_1-T_0\|_{X_\rho^s\to X_\rho^{s-\ell}}\le\epsilon
$$
且 §1–2 已给两 inverse 在 $s$、$s-\ell$ 档的界，则由准确 identity
$$
T_1^{-1}-T_0^{-1}
=-T_1^{-1}(T_1-T_0)T_0^{-1}
\tag{8}
$$
得到含一个真实 $\epsilon$ 的相同损阶界。
同一原 source 的比较先保持它固定；source 或 raw column 自身变化时
还必须另加该数据差。尤其不把 raw metric column 的变化免费乘上 $q$。
有限参数微分也由 (8) 及有限次 Leibniz 展开获得，但仍须真实地给出
相应输入导数表。

## 3. 一个全局 J-unitary 中性图逆，不需近恒等

现在 $\mathscr H\oplus\mathscr H$ 上令
$\mathsf J=\operatorname{diag}(I,-I)$，设
$$
Z=\begin{pmatrix}A&B\\C&D\end{pmatrix},\qquad
Z^*\mathsf JZ=\mathsf J,quad Z\mathsf JZ^*=\mathsf J
\tag{9}
$$
为真实双向有界 $\mathsf J$-unitary。
给定真实 onto unitary $S$，置
$$
E=A+BS,\qquad F=C+DS.
\tag{10}
$$
则 $E,F$ 均双向可逆，$FE^{-1}$ 为 onto unitary，并有
$$
\|E^{-1}\|\le\|Z^{-1}\|,\qquad
\|F^{-1}\|\le\|Z^{-1}\|.
\tag{11}
$$

**证明。** (9) 给 $A^*A-C^*C=I$ 及 $AA^*-BB^*=I$。
前式使 $A$ bounded below，后式使 $A^*$ bounded below，故 $A$ onto
且双向可逆。又
$$
(A^{-1}B)(A^{-1}B)^*
=I-A^{-1}A^{-*}
\le(1-\|A\|^{-2})I.
$$
所以 $\|A^{-1}BS\|<1$，$E=A(I+A^{-1}BS)$ 真可逆。
对 $D$ 用另一对 block identities，同理 $D$ 可逆且
$\|D^{-1}C\|<1$，故 $F=D(S+D^{-1}C)$ 真可逆。

向量 $(x,Sx)$ 是中性的，因此 (9) 迫使
$\|Ex\|=\|Fx\|$。
于是 $FE^{-1}$ 是 isometry，而 $E,F$ 均 onto，故它也 onto。
再用
$$
\sqrt2\|Ex\|=\|Z(x,Sx)\|
\ge\|Z^{-1}\|^{-1}\sqrt2\|x\|
$$
得到 (11)。证毕。

对 raw 图 $d=Rc$ 的反向换元，$R$ 为 onto unitary，令
$$
D_Z=D-RB.
$$
对 $Z^{-1}=\left(\begin{smallmatrix}A^*&-C^*\\-B^*&D^*\end{smallmatrix}\right)$
和图 $R$ 应用上述结论：其第二投影为 $F_-=-B^*+D^*R$，
$D_Z^*=F_-R^*$，所以
$$
\|D_Z^{-1}\|\le\|Z\|.
\tag{12}
$$
这是无权结论。若要 log 权表，仍须按 §1–2 给 (10) 或 $D_Z$ 的
真实正 gain 余项；(9)–(12) 本身没有声明该表。

## 4. Strict feedback 的真实无权常数

设完整两端散射 $\mathcal A$ 是 onto unitary block matrix，且
$\mathcal A_{12}$ 双向有界可逆。令
$$
B_{\rm fb}=I+\mathcal A_{11},\qquad
N_{12}=\|\mathcal A_{12}^{-1}\|.
$$
由 row-unitarity，
$$
\mathcal A_{11}\mathcal A_{11}^*
=I-\mathcal A_{12}\mathcal A_{12}^*
\le(1-N_{12}^{-2})I.
$$
其中 $N_{12}\ge1$。于是
$$
\|B_{\rm fb}^{-1}\|
\le\frac1{1-\sqrt{1-N_{12}^{-2}}}
\le2N_{12}^2.
\tag{13}
$$
若 $\mathcal A_{11}$ 另有真实正 gain 表，§1–2 立即给 weighted 真逆。
无需将整个实际头部变为小扰动。

## 5. 对 R513 的逐项准确应用范围

R513 (13.4) 的两个真实 Gram 是
$$
G_1=T_{21}'{}^*T_{21}'=I+T_{11}'{}^*T_{11}',\qquad
G_2=T_{12}'{}^*T_{12}'=I+T_{22}'{}^*T_{22}'.
\tag{14}
$$
它们无权均 $\ge I$，故真 inverse 的 norm 至多1。
若实际 wrong-branch 和 adjoint 的预付 finite gain 表已经给出，
其乘积满足 §1–2，得同一个 $G_a^{-1}$ 的 weighted 表。
原无权 anti-$J$ 双向 identity 保 transmission onto，故
$$
T_{21}'{}^{-1}=G_1^{-1}T_{21}'{}^*,\qquad
T_{12}'{}^{-1}=G_2^{-1}T_{12}'{}^*
$$
仍是原真实 transmission inverse。
这可替换该处原 (13.5) 的基线 Neumann 小量，不能替换未构造的 Cauchy 场。

R513 (13.9) 的 $S'$ 在无权物理 $L^2$ 是真正 onto unitary，
其 root frame $Z$ 满足 (9)。所以
$E_N=Z_{11}+Z_{12}S'$ 的无权 inverse 由 §3 有
$\|E_N^{-1}\|\le\|Z^{-1}\|$。
若已将 $E_N$ 写为一个完整可逆 Fourier leading part 加实际正 gain
余项，则 §1–2 给它的 weighted 逆，可替换 (13.15b) 的小背景 Neumann。
此时必须确实给出 $Z_{11}$ 的 leading part 与 remainder；
$Z_{12}$ 的 $4/3$ gain 单独并不足够。
随后才定义
$$
S_{\rm raw}=(Z_{21}+Z_{22}S')E_N^{-1}.
$$
因此不循环借尚未取得的 raw 图 weighted norm。

R513 (13.10) 中 $\mathcal A=-R'^*S'$ 真 unitary，
$\mathcal A_{12}=-R_L'^*T_{12}'{}^{-1}$，所以
$N_{12}=\|T_{12}'R_L'\|=\|T_{12}'\|$。
由 (13)，strict feedback 的真实无权 inverse norm 至多
$2\|T_{12}'\|^2$。其 $\mathcal A_{11}$ 是已知 wrong-branch 的完整高 gain
项，包含全部 low/mean contributions；实际 gain 表给出后，§1–2
可替换原 (13.11)。有限低列不能因高 gain 而被删除。

原 ordinary source 的 zero-left particular、两次 incoming affine、
两 scalar columns 和内部 row 仍按 R513 (13.12)–(13.16) 使用。
本论证只替换这些式中 inverse 的估计与取得顺序；没有更换 particular
或忽略完整场内部积分。

## 6. 仍必须实际支付的部分

上述替代是有限 cell 的**逆闭包**，不能单靠它把 R513 的整个假设球扩大。
当前 flat17 有开 $K=0$ 段及非 simple 的端点起落；
它们不自动属于原简单根 Airy recipe。
开放 $K=0$ 的 source-free 非线性 Cauchy 传播已在
`2026-11-10-78718-geometry-flat-strip-provider-v2.md` 给出显式全角公式，
但该文也没有 ordinary-source Green 或相邻非平 ramp 的完整高频模型。

要用本文处理一个实际较大头部，必须先有该头部自己的：

- 合法物理 type/space-like 域、真实边界 realization 和 source/adjoint；
- 完整 Cauchy/Robin/finite-root 模型、真无权能量或通量身份；
- 同一个 leading part 上的实际正 gain 及全有限角阶/权表；
- 所有出现常数的有效上界，允许据它们一次选择 J。

这些不是从本题有限 BVP Jacobian 或很小采样 metric 残差得到的。
另外，R518 的原全网络 $K_0$ 只在其选定自然范围上工作，不能把它
冒充 §1 的全 $L^2$ onto inverse；本文没有对那个问题绕过低 Schur 证书。
本文没有运行新 PDE 或产生新闭面。
