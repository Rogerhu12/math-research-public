# R449：相对第二余核与原两条 carry 带的完整精确序列

日期：2026-11-14。**状态：已证明。** 本篇在完全相同的来源预算中，将 R444 的可见首像缺口准确识别为相对 \(C_2(J)\) 商掉真实 carry 像后的空间，并分解原 \(d_2(M)\)。因此，\(\gamma>0\) 与真第二核同时存在，仍不足以使实际 Miller 修正可见：若相对 \(J\) 满有理行秩且全部 Smith 指数至多一，整个修正仍可在第三精度吸收。原 \(M\) 此时可能真有 \(p^2\) 因子；其数目和完整 \(d_2\) 均由两条 carry 带明确给出，不混同相对 \(J\) 的 \(p^2\) 缺陷。

## 1. 同一原矩阵的精确两块形式

保持 R444 的

\[
p=6s-1>83,\quad 1\le\ell<s-13,\quad L=2s+\ell,
\quad V=\mathcal W_{D,J},\quad 0\le J\le16,
\]

以及同一个原整评价 \(J:V\to\Gamma_L\) 与

\[
\mathsf M^{\rm orig}=c_*U_0m_{13}J:V\to\Gamma_{L+13}.
\tag{1}
\]

先用整个 \((c_*U_0)^{-1}\) 运输目标，包括 \(P_{134}\)、theta、Gaussian 与原第三坐标，再按真实 \(m_{13}\) 的对角幂排列行。相对目标准确分为

\[
\Gamma_L=A_{\mathcal O}\oplus B_{\mathcal O},\qquad
\operatorname{rank}A_{\mathcal O}=L-26,\quad
\operatorname{rank}B_{\mathcal O}=26.
\]

\(B\) 恰为相对下标

\[
[s-13,s-1]\ \cup\ [2s-13,2s-1]
\tag{2}
\]

这两条完整 carry 带；\(A\) 是其余全部行。写 \(J=(J_A,J_B)\)。原目标最初十三行组成一个完整零行直和项 \(F_{13}\)，其余矩阵准确为

\[
\boxed{M=\begin{pmatrix}J_A\\pJ_B\end{pmatrix}.}
\tag{3}
\]

后文先对 (3) 计算，再把 \(F_{13}\) 和整个 \(c_*U_0\) 放回。这里并没有在模 \(p\) 之前删除 carry 行或先将其除以 \(p\)。

以下不加下标的 \(A,B,V\) 表示模 \(p\) 向量空间。置

\[
K_A=\ker\bar J_A,\quad K=\ker\bar J,
\quad C=\operatorname{coker}\bar J,\quad
G=\operatorname{coker}\bar J_A.
\tag{4}
\]

该 \(G\) 正是 R444 的 \(I_{13}/\operatorname{im}\bar M\)，故 \(\dim G=\gamma\)。

## 2. 原 carry 像与相对首提升

令

\[
H=\operatorname{im}(B\longrightarrow C).
\tag{5}
\]

它有准确表示

\[
H=B/\bar J_B(K_A).
\]

由投影到 \(A\)，得到同一预算中的短正合列

\[
\boxed{0\longrightarrow H\longrightarrow C
\xrightarrow{\pi}G\longrightarrow0.}
\tag{6}
\]

确实，\((0,b)\) 在 \(C\) 中为零，恰等价于存在 \(P\in K_A\) 使 \(\bar J_BP=b\)；投影的满性及其余核由 (4) 直接得到。

相对首 Bockstein 是真实提升映射

\[
\beta_J:K\longrightarrow C,
\qquad \beta_J(\bar P)=[J(P)/p].
\tag{7}
\]

令

\[
\boxed{\delta_A=\pi\beta_J:K\longrightarrow G.}
\tag{8}
\]

它也可直接由 \([J_A(P)/p]\) 在 \(G\) 中读取。改变 \(P\) 的整提升只增加 \(\bar J_AQ\)，所以 (8) 不需要另选不相容的首核提升。

## 3. 真正原第二核的完整识别

用 \(K_2^{\rm red}(F)\) 表示模 \(p^2\) 核向量在 \(V/pV\) 中的像；这正是 \(\ker\beta_1^F\)，不是整个模 \(p^2\) 核的长度。

**定理 1。** 对 (3)，准确有

\[
\boxed{K_2^{\rm red}(M)=\ker\delta_A\subset K.}
\tag{9}
\]

从而

\[
\boxed{
0\longrightarrow K_2^{\rm red}(J)
\longrightarrow K_2^{\rm red}(M)
\xrightarrow{\beta_J}\operatorname{im}\beta_J\cap H
\longrightarrow0.
}
\tag{10}
\]

**证明。** 若 \(MP_2\in p^2\)，(3) 的第二块先给 \(J_BP_2\in p\)，第一块也给 \(J_AP_2\in p\)，所以 \(\bar P\in K\)。能够进一步修正 \(P\mapsto P+pQ\) 使第一块属于 \(p^2\)，恰等价于 \([J_A(P)/p]=0\) 于 \(G\)，即 (9)。第二块已有一个外面的 \(p\)，此时不再要求 \(J_BP_2\in p^2\)。反向同样构造这个真实首次修正，证明 (9)。

由 (6)，\(\delta_A(P)=0\) 等价于 \(\beta_J(P)\in H\)。该映射的核是 \(\ker\beta_J=K_2^{\rm red}(J)\)，像准确是显示的交，得到 (10)。\(\square\)

所以原真第二核包括两种确切来源：相对真正第二核，以及相对首提升落进 carry 像的方向。后者不能误称为相对 \(J\) 已有 \(p^2\) 缺陷。

## 4. 可见余核恰为相对 C2 商掉 carry

原 \(C_1(M)\) 在 (3) 中准确为 \(G\oplus B\)。对 \(P\in K_A\)，首 Bockstein 的两块是

\[
\beta_M(P)=
\left([J_A(\widetilde P)/p],\ \bar J_BP\right).
\tag{11}
\]

首分量在 \(G\) 中读取。特别，\(\beta_M(P)\) 落在 \(G\) 内，恰当 \(P\in K\)，其首分量就是 (8)。因此 R444 的可见空间满足

\[
\boxed{G_2=\operatorname{im}(G\to C_2(M))
=\operatorname{coker}\delta_A.}
\tag{12}
\]

记 \(\overline H\) 是 \(H\) 在相对
\(C_2(J)=C/\operatorname{im}\beta_J\) 中的像。由 (6)–(8)，进一步得到

\[
\boxed{G_2\simeq C_2(J)/\overline H.}
\tag{13}
\]

这不是把 carry 方向免费删去：\(H\) 是通过整个相对首像实际计算的商 (5)，\(\overline H\) 还须经过真实 \(\beta_J\) 的像。

完整原第二余核另有短正合列

\[
\boxed{0\longrightarrow G_2\longrightarrow
C_2(M)\longrightarrow H\longrightarrow0,}
\tag{14}
\]

恢复原最初十三行后，右侧的 \(C_2(M)\) 应替换为
\(C_2(\mathsf M^{\rm orig})/F_{13}\)。

**证明。** 将 (11) 的第二分量商掉 \(\bar J_B(K_A)\)，得到到 \(H\) 的满射。它的核正是 \(G\) 的像，即 (12)，所以得到 (14)。式 (13) 则是
\(G/\pi(\operatorname{im}\beta_J)=C/(H+\operatorname{im}\beta_J)\)。\(\square\)

尤其

\[
\dim C_2(\mathsf M^{\rm orig})
=13+\dim G_2+\dim H.
\tag{15}
\]

有 \(\gamma>0\) 而 \(G_2=0\) 完全可能；真正的低轴修正只通过 (13)。

## 5. 原 d2 的 carry 部分和相对第二部分

令 \(d_2^M\)、\(d_2^J\) 均按真实首次提升并商去各自完整首 Bockstein 像定义。

**定理 2。** 对同一个 \(P\in K_2^{\rm red}(M)\)，(14) 的投影满足

\[
\boxed{\operatorname{pr}_H(d_2^M(P))=\beta_J(P)\in H.}
\tag{16}
\]

若进一步 \(P\in K_2^{\rm red}(J)\)，则 \(d_2^M(P)\) 落在 (14) 的 \(G_2\) 中，而且

\[
\boxed{d_2^M(P)=
\operatorname{pr}_{G_2}\bigl(d_2^J(P)\bigr),}
\tag{17}
\]

其中右边使用 (13)。因此真正原第三核的约化准确是

\[
\boxed{K_3^{\rm red}(M)=
\ker\left(K_2^{\rm red}(J)
\xrightarrow{d_2^J}C_2(J)\longrightarrow G_2\right).}
\tag{18}
\]

**证明。** 对 (9) 的真实提升，取 \(J_AP_2\in p^2\)、\(J_BP_2\in p\)。于是

\[
MP_2/p^2=
\bigl(J_AP_2/p^2,\ J_BP_2/p\bigr).
\]

相对 \(JP_2/p\) 在 \(C\) 中约化为
\((0,\overline{J_BP_2/p})\)，其类正是 (7) 的 \(\beta_J(P)\)，得到 (16)。所有第一次提升的差均按 (11) 商去。

若 \(P\in K_2^{\rm red}(J)\)，可选更强的 \(JP_2\in p^2\)。此时上式第二分量模 \(p\) 为零，首分量是相对 \(d_2^J\) 的 \(A\) 投影。其真实目标商正是 (13)，得到 (17)。最后，(16) 使 \(d_2^M(P)=0\) 必先迫 \(\beta_J(P)=0\)，再由 (17) 得 (18)。\(\square\)

(18) 仍使用原 \(M\bmod p^3\)；没有将主课题的完整中央第三位从有限矩阵中删除。

## 6. γ>0 时仍全部吸收的准确范围

R444 的实际修正是

\[
\mathsf M-\mathsf M^\sharp
=p^2A_0\,\bar{\mathsf M}\mathcal E_{\rm tot}\pmod{p^3}.
\]

它的整个第二障碍像通过 \(G_2\)。结合 (13)，得到一般判据

\[
\boxed{\overline H=C_2(J)
\ \Longrightarrow\ \text{全部实际低轴/Miller 修正为零}.}
\tag{19}
\]

这里不要求 \(G=0\)。两条来源的原 \(P_{134}/U_0\)、完整中央基准和已选 \(A_0\) 都固定不动。

**整吸收说明。** 若 (19) 成立，两个矩阵模 \(p^2\) 相同，其真实 \(d_2\) 也相同。因此存在源、目标的整基变换，均模 \(p\) 为恒等，将二者模 \(p^3\) 相互送到；这些变换保持同一个模 \(p^2\) 映射。一般不能加强为 R444 在 \(\gamma=0\) 时的单独来源变换 \(1+p^2C\)。

为核这一断言，可对共同模 \(p^2\) 矩阵先用同一整基分离单位块与 \(p\) 单位块。\(p^2\) 扰动碰到单位块时，以 \(p^2\) 倍的源、目标行列加法消去；碰到 \(p\) 单位块时，以 \(p\) 倍的行列加法消去。这些操作均不改变共同模 \(p^2\) 映射。唯一剩余块正是从真正 \(K_2^{\rm red}\) 到 \(C_2\) 的 \(p^2\) 扰动；(19) 及 R444 使它为零。故整个第三精度扰动都被吸收。

特别，若相对 \(J\) 满有理行秩，且其所有非单位 Smith 因子恰为 \(p\)，则

\[
C_2(J)=0,
\]

所以 (19) 自动成立。此时真原 \(P_2\) 仍可能非零：它们可由 (10) 的非零 carry 商给出，而不是被不存在的相对 \(p^2\) 因子产生。

## 7. 这一范围中的完整原 Smith 因子

继续假设 \(J\) 满有理行秩且相对 Smith 指数至多一。令

\[
\gamma=\dim G,\qquad h=\dim H.
\]

由 (6)，相对 \(J\) 的 \(p\) 因子数为 \(\gamma+h\)。原 \(M\) 的完整非零 Smith 因子准确为

\[
\boxed{
L-26-\gamma\text{ 个单位},\quad
26+\gamma-h\text{ 个 }p,\quad
h\text{ 个 }p^2.
}
\tag{20}
\]

原目标另外仍有十三个自由方向。若来源维数为 \(N\)，整来源核秩为 \(N-L\)。

**证明。** 首单位数是 \(\operatorname{rank}\bar J_A=L-26-\gamma\)。由 (13)–(15)，\(C_2(M)\) 的有限部分维数恰为 \(h\)，所以至少二次的 Smith 因子数为 \(h\)。又相对像含 \(p\Gamma_L\)，乘 (3) 的对角 \((1,p)\) 后，饱和像中的余核被 \(p^2\) 杀死；不存在更高因子。其余非单位数于是为 (20) 中间项。\(\square\)

在 (20) 中，(16) 还给

\[
K_2^{\rm red}(M)/K_2^{\rm red}(J)
\xrightarrow[\ d_2^M\ ]{\sim}H
=C_2(M),
\tag{21}
\]

式末的 \(C_2(M)\) 指剥去原十三自由行后的有限部分。因相对 \(\beta_J\) 满射到 \(C\)，(10) 的像正为整个 \(H\)。这说明纯 carry 产生的每个 \(p^2\) 方向都有完整、非零的原 \(d_2\)，并不依赖 Miller 修正。

R417 的结构是 \((\gamma,h)=(1,0)\)，故出现二十七个 \(p\) 而没有 \(p^2\)。R428 在唯一 carry 线且 \(\eta_p\ne0\) 的结构是 \((\gamma,h)=(0,1)\)，故出现二十五个 \(p\) 和一个 \(p^2\)。这两份已付原计算是 (20) 的不同实际分布；不能仅由 \(C_2(M)\) 非平凡倒推 \(C_2(J)\) 有相同缺陷。

## 8. 对下一真正双侧窗口的要求

对满有理行秩的相对 \(J\)，若要让实际低轴修正在同一原预算内非零，必须有

\[
C_2(J)/\overline H\ne0.
\]

因此先要有相对 \(J\) 真正的 \(p^2\) 或更深 Smith 因子，而且该方向不能完全来自 (5) 的 carry 像。原真第三核则还须通过 (18) 的相对第二障碍测试。这是比 \(\gamma>0\) 和“真 \(P_2\) 非零”更准确的双侧接口。

这些必要条件没有由原两条完整中央失败自动付清。它们的实际基准、第二位 Hensel 参数及第三中央权仍需保持；相对 \(C_2(J)\) 的存在或消失都不是 Sha 有限的充分条件。本篇没有扩大有限素数扫描，也没有宣称全部低预算相对矩阵已经排除 \(p^2\) 缺陷。

依赖：R338/R351 的真实提升定义；R403 的同一实际第三精度比较；R412/R417 的完整原 Smith 格；R428/R434 的唯一 carry 接口；R444 的首像理想与可见修正。全部序列来自 (1)–(3) 的同一个实际整矩阵，恢复公共载体后逐项运输。
