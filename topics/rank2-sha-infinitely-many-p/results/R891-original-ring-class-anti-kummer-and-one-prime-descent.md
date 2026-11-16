# R891. 原环类系统的 anti-Kummer、单侧有限—奇异关系与条件 Selmer 秩一

日期：2026-11-16。**状态：正文的 anti-Kummer 辅助引理、附录 A 的原一侧有限—奇异关系，以及附录 B 的有条件 balanced Selmer 秩一定理均已证明。** 全文保留原十七处角色、任意指定的 p-adic 深度、此前的整个 p 环类层和两个共轭素点。秩一定理的前提是原端点底类非零；没有由此证明该前提或指定 ordinary 局部化非零。

## 1. 固定原来源及两个不同的辅助集合

沿 [R886](R886-original-highest-cm-auxiliary-units-and-base-preserving-normalization.md)，
$K=\mathbf Q(\omega)$，固定原普通 ray 的 $p>211$。原 $E_0:y^2=x^3+1$ 的两个 CM Tate 角色为 $\psi_0,\bar\psi_0$，且 $\psi_0\bar\psi_0=\varepsilon_{\rm cyc}$。原有限角色 $\eta$ 的阶为十八，三个指定最高角色是
$$
\rho_i=\eta^{e_i}\psi_0^3\varepsilon_{\rm cyc}^{-1},
\qquad (e_4,e_{10},e_{16})=(5,17,11).
\tag{1}
$$
保留原一次固定的系数格及全部旧副本、Artin 系数。

R886 附录 A 的真实十七惯性元 $\gamma$ 满足
$$
\eta(\gamma)=-1,\qquad
\psi_0(\gamma)=\bar\psi_0(\gamma)=1,\qquad
\varepsilon_{\rm cyc}(\gamma)=1.
\tag{2}
$$
它在原四个分量上均作用为 $-1$。检测元 $\tau$ 则在最高分量作用为 $1$、在其余三分量作用为非一三次单位根。两者不混用。

令 $K[n]$ 表示导子 $n$ 环类域的最大 p 子域。原全 split tame 系统及 R886 附录 A 已在
$\mathcal U=\mathcal L_1\cup\mathcal U_\gamma$
上给出同一个真实有限系统
$$
c_n\in H^1(K[n],T),\qquad
c_1=z^{\rm end}_{i,p},
\tag{3}
$$
并满足最高角色的线性 Euler 范数关系。所有层只用一次固定分母；本文不以 canonical Heegner 类替换 (3)。

## 2. 辅助素数定理

固定一个良好分裂有理素数 $q\ne p$，指定 $\mathfrak q\mid q$，并取任意整数 $N\ge1$。设 $q$ 避开 $2,3,17$。则存在正密度的良好分裂有理素数 $l$，各可指定 $\mathfrak l\mid l$，同时满足：

1. $l\equiv1\pmod{p^N}$，且在 $H_\eta K(E_0[p^N])$ 上
   $\operatorname{Fr}_{\mathfrak l}$ 等于 (2) 的像。特别
   $l\in\mathcal U_\gamma$。
2. $l$ 在整个 $K[q]/K$ 中分裂。
3. 若 $h_l=p^{v_p(l-1)}$，则
   $\operatorname{Fr}_{\mathfrak q}$ 在
   $\operatorname{Gal}(K[l]/K)$ 中的阶恰为 $h_l$。
   $\operatorname{Fr}_{\bar{\mathfrak q}}$ 的像是其逆，阶也恰为 $h_l$。

可以同时删除任意预先指定的有限素数集。也可将条件 2 中的 $K[q]$ 换为它与任意固定、在十七处不分歧的有限阿贝尔扩张 $B/K$ 的合成域。这里只扩大阿贝尔条件；没有无证加入任意非阿贝尔上同调测试域。

## 3. Anti-Kummer 扩张及其最大阿贝尔子域

$K$ 的类数为一，故选择
$$
\mathfrak q=(\pi_q),\qquad
\alpha_q=\pi_q/\bar\pi_q.
\tag{4}
$$
其在 $\mathfrak q,\bar{\mathfrak q}$ 处的赋值分别是 $1,-1$，其它有限位的赋值为零，并且
$\bar\alpha_q=\alpha_q^{-1}$。

置
$$
M_N=K(\mu_{p^N}),\quad
L_{N,q}=M_N(\alpha_q^{1/p}),\quad
A_{N,q}=H_\eta K(E_0[p^N])K[q].
\tag{5}
$$
$M_N/K$ 在 $q$ 处不分歧，所以 (4) 的赋值在 $M_N$ 中仍为 $1$。因此 $\alpha_q$ 不是 $M_N$ 中的 p 次幂，且
$$
[L_{N,q}:M_N]=p.
\tag{6}
$$
这里不以一个未定的单位 Kummer 类代替 (4)。

$K\cap\mathbf Q(\mu_{p^N})=\mathbf Q$，因为 $p>3$。故
$\Delta_N=\operatorname{Gal}(M_N/K)\simeq(\mathbf Z/p^N\mathbf Z)^\times$。
$\Delta_N$ 的元可延拓为固定所选 $\alpha_q^{1/p}$ 的自同构；它们对 $\mu_{p^N}$ 作原 cyclotomic 作用。这给
$$
\operatorname{Gal}(L_{N,q}/K)
\simeq C_p\rtimes\Delta_N,
\tag{7}
$$
其中 $\Delta_N$ 在 $C_p$ 上按模 p cyclotomic 角色作用。该作用非平凡，且 $\Delta_N$ 交换，因此
$$
[\operatorname{Gal}(L_{N,q}/K),
  \operatorname{Gal}(L_{N,q}/K)]=C_p.
\tag{8}
$$
所以 $L_{N,q}$ 中最大的 K-阿贝尔子扩张准确是 $M_N$。

$E_0$ 的全部 CM 自同态在 $K$ 上定义，故 $K(E_0[p^N])/K$ 阿贝尔；$H_\eta/K$ 与 $K[q]/K$ 也阿贝尔。Weil 配对给
$M_N\subset K(E_0[p^N])$。由 (8) 得到完整交域等式
$$
\boxed{A_{N,q}\cap L_{N,q}=M_N.}
\tag{9}
$$
加入定理中允许的阿贝尔 $B$ 后，证明完全相同。若 $B$ 未在复共轭下稳定，先以 $B\,B^c$ 取代；它仍在 $K$ 上阿贝尔且十七处不分歧，只加强所求分裂条件，并使后面的整个合成域在复共轭下稳定。

原 $\gamma$ 在十七处惯性；$E_0$ 在十七处良好，$K[q]$ 与允许的 $B$ 在十七处不分歧。因此 $\gamma$ 在 $A_{N,q}$ 上的像固定
$K(E_0[p^N])K[q]B$，在 $H_\eta$ 上取 (2) 的值。其在 $M_N$ 上为一。

另一方面，任取
$1\ne b\in\operatorname{Gal}(L_{N,q}/M_N)=C_p$。
(9) 说明 $\gamma|_{A_{N,q}}$ 与 $b$ 在交域上一致，故给出合成域上的真实自同构。Chebotarev 应用于这个具体自同构的共轭类。所有这些域在复共轭下稳定；特别
$\bar\alpha_q=\alpha_q^{-1}$
保证 $L_{N,q}/\mathbf Q$ 为 Galois。因此可选在 $K$ 中分裂的有理 $l$ 及其一个素点 $\mathfrak l$，使其 Frobenius 正是上述相容对。

这立即给条件 1、2，并且在剩余域 $\mathbf F_l$ 中
$$
\boxed{\alpha_q\bmod\mathfrak l
       \notin(\mathbf F_l^\times)^p.}
\tag{10}
$$
原因是 $l$ 在 $M_N$ 分裂、残余域含 $\mu_p$，而 Kummer 扩张上的 Frobenius 是非平凡的 $b$。所有选择只删有限多个分歧或分母素数，故仍为正密度。

## 4. 从非 p 次幂到原完整环类群的满阶

这一步使用原类数一和单位群 $\mu_6$，不能仅以 (10) 猜一个 p 阶子商。

对分裂的 $l$，按 $\mathfrak l,\bar{\mathfrak l}$ 排列有
$$
(\mathcal O_K/l\mathcal O_K)^\times
\simeq\mathbf F_l^\times\times\mathbf F_l^\times.
$$
除以对角的 $(\mathbf Z/l\mathbf Z)^\times$ 后，由
$(u,v)\mapsto u/v$
识别为 $\mathbf F_l^\times$。全局单位 $\epsilon\in\mu_6$ 在该商中的像是
$\epsilon/\bar\epsilon=\epsilon^2$，阶整除三。因 $p>3$，取 p 部分时它不改变群。因此环类精确序列给
$$
\boxed{
\operatorname{Gal}(K[l]/K)
\simeq(\mathbf F_l^\times)^{(p)}
\simeq C_{h_l},\qquad h_l=p^{v_p(l-1)}.
}
\tag{11}
$$
这里没有残留的 p 类群商。

在此识别下，主理想 $\mathfrak q=(\pi_q)$ 的 Artin 像是
$\alpha_q\bmod\mathfrak l$
的 p 部分，或在相反 Artin 规范下为其逆。改变生成元 $\pi_q$ 只乘上一个三次单位根，故不改变这个 p 部分。

在循环群 $\mathbf F_l^\times$ 中写 $\alpha_q=g^a$。条件 (10) 等价于 $p\nmid a$，从而其 p 部分的阶恰为
$p^{v_p(l-1)}=h_l$，而非仅保证阶至少 p。这证明定理条件 3。复共轭交换两个剩余坐标，所以在 (11) 上作取逆；故 $\bar{\mathfrak q}$ 的像也是满阶。

注意 $l\equiv1\pmod{p^N}$ 给 $h_l\ge p^N$；本文不要求 $v_p(l-1)$ 恰为 $N$。

## 5. 四角系统的准确局部结构

令
$$
E=K[q],\qquad L=K[l],\qquad EL=K[ql].
\tag{12}
$$
原环类 CRT 的 p 部分给
$$
\operatorname{Gal}(EL/K)
=\operatorname{Gal}(E/K)\times\operatorname{Gal}(L/K).
\tag{13}
$$
在 $\mathfrak q$ 处，$E/K$ 全分歧，阶为
$h_q=p^{v_p(q-1)}$；$L/K$ 不分歧，并由条件 3 在该处有完整剩余次数 $h_l$。同样的结论对 $\bar{\mathfrak q}$ 成立。

因此可以在原局部分解群中选择：

- 惯性元 $\sigma$，其在 $E$ 上生成 $\operatorname{Gal}(E/K)$、在 $L$ 上为一；
- 算术 Frobenius lift $\phi$，其在 $E$ 上为一、在 $L$ 上生成 $\operatorname{Gal}(L/K)$。

后一选择可将任意算术 Frobenius 乘以适当惯性元获得；这不改变原未分歧表示 $T$ 的 Frobenius 值，也不改变它在 $L$ 上的像。这里的两元只在有限阿贝尔商 (13) 中交换，不能无证将它们在绝对局部分解群中的交换子删掉。

设原最高 Euler 因子为
$$
P_{0,\mathfrak l}(X)
=1-\frac{\rho_i(\operatorname{Fr}_{\mathfrak l})}{l}X.
$$
条件 1 给同一个实际标量
$$
u_l=P_{0,\mathfrak l}(1)\equiv2\pmod{p^N\mathcal O},
\qquad u_l\in\mathcal O^\times.
\tag{14}
$$
因 $l$ 在 $E$ 分裂，原系统 (3) 在两个相对 l 方向的范数恰为
$$
\operatorname{cor}_{L/K}c_l=u_lc_1,\qquad
\operatorname{cor}_{EL/E}c_{ql}=u_lc_q.
\tag{15}
$$
两个角是同一个 $u_l$，全部等式均发生在原固定格上；没有扩大层数而引入新的 p 分母。两个 q 方向则仍保留其真实 Frobenius Euler 算子。绝对局部 cochain lift 上所需的交换性另由附录 A.3 使用原未分歧类证明，不能只由 (13) 推出。

## 6. 已付范围与下一步

(4)–(15) 完整支付 Rubin rigidity 方法在本题原环类系统中的辅助素数部分，包括此前容易遗漏的 anti-Kummer 比、全 $h_l$ 阶和两共轭素点。它不依赖全 ray-class Euler 系统，也不将 R886 的狭义 $\mathcal L_1$ 自动扩大为所有 split primes。

附录 A 在同一四角 (12) 上逐项证明连续 coinduced 模的范数满射、实际 lift 的范数误差消失和一侧有限—奇异读数；附录 B 再与原双点 selector 合成有条件秩一定理。这些步骤不是 (15) 的形式重述。原底类 $c_1$ 是否非零，及非零类在指定 ordinary 局部化是否仍非零，仍是另外两个问题。

原文对照：[Rubin, *Euler Systems*, 1999 作者讲义](https://swc-math.github.io/aws/1999/99RubinES.pdf)，Chapter IV §7（印 pp.74–76）以及 Chapter IX §1（印 pp.134–135）。原书使用的 Kummer 辅助选择在这里由 (4)–(11) 针对原环类商重新证明；未把原书全 ray 系统的结论直接套入。原完整 finite tame 来源及统一分母见
[原端点 tame 系统](../notes/2026-11-16-original-endpoint-tame-norm-system.md)，原两类辅助集合与单位归一见 R886 正文及附录 A。

本证明没有数学程序执行或新的数值证书。


## 附录 A. 原四角系统的一侧有限—奇异恒等式

本附录只用正文的实际 $E=K[q]$、$L=K[l]$、$EL=K[ql]$，以及 (3)、(15) 的同一类。没有要求完整 ray-class 系统，也没有将两个共轭素点认成一个。

### A.1 精度、范数与连续 coinduced 模

固定 $N\ge1$，置
$$
A_N=T/p^NT.
$$
取原检测集合中的 $q$，使
$$
q\equiv1\pmod{p^N},\qquad
a_q:=\rho_i(\operatorname{Fr}_{\mathfrak q})
       \equiv1\pmod{p^N\mathcal O}.
\tag{A1}
$$
这样的深度和后面所需的全部上同调读数，可以同时由
[原 finite-test 注的附录 A](../notes/2026-11-16-original-endpoint-finite-test-chebotarev-refinement.md)
实现。只需 $q$ 在 R886 的 $\mathcal L_1$ 中；没有额外要求两条 CM 根各自满足更强的深度条件。

按正文选择 $l$。所有四个原整类先约到 $A_N$，仍记
$c_1,c_q,c_l,c_{ql}$。令
$$
P_q(X)=1-\frac{a_q}{q}X,\qquad
u_l=P_{0,\mathfrak l}(1)\in\mathcal O^\times.
\tag{A2}
$$
由 (A1)，在 $\mathcal O/p^N\mathcal O$ 中
$P_q(X)=1-X$、$P_q(1)=0$，且 $p^N\mid h_q,h_l$。

记 $G=G_K$，取离散连续 G-模
$$
\mathscr I=\operatorname{Map}_{\rm cont}(G,A_N),
\qquad (g f)(x)=f(xg).
\tag{A3}
$$
将 $A_N$ 以 $\iota(t)(x)=x t$ 等变嵌入 $\mathscr I$，并置
$\mathscr Q=\mathscr I/\iota(A_N)$。以下把 $\iota(A_N)$ 与 $A_N$ 识别；它**不是**常值函数子模。

对任意开子群 $H\subset G$，
$\mathscr I^H$ 是有限右 $H$ 轨道集 $G/H$ 上的函数模。
限制 $\mathscr I$ 到 $H$ 后，是有限多个连续正则 coinduced 模的直和，所以
$H^1(H,\mathscr I)=0$。这里也有直接证明：在一份
$\operatorname{Map}_{\rm cont}(H,A_N)$ 上，对连续 1-cocycle $b$ 令
$f(x)=b(x)(1)$，则
$$
(gf-f)(x)=b(xg)(1)-b(x)(1)=b(g)(x).
$$
因 $H$ 紧且 $A_N$ 有限，所得函数连续；对有限多个右 $H$ 轨道分别作此构造即可。因此
$$
\mathscr I^H\longrightarrow\mathscr Q^H
 \xrightarrow{\partial_H}H^1(H,A_N)\longrightarrow0
\tag{A4}
$$
正合。

若 $H'\triangleleft H$ 为有限指数开子群，则
$$
N_{H/H'}:\mathscr I^{H'}\longrightarrow\mathscr I^H
\quad\hbox{满射}.
\tag{A5}
$$
确实，对每个右 $H$ 陪集，在其中选一个右 $H'$ 陪集承载给定函数值，其余置零。范数在每个纤维上求和，恰回到原函数。这里只涉及有限陪集，所得函数均局部常值。没有使用除以 $[H:H']$，也没有遗漏连续性条件。连接映射 (A4) 与这些范数、corestriction 自然相容。

### A.2 在商模中先固定两个真实范数角

采用正文 §5 的惯性元 $\sigma$ 与 Frobenius lift $\phi$，并令
$$
N_q=\sum_{j=1}^{h_q}\sigma^j,\qquad
D_q=\sum_{j=0}^{h_q-1}j\sigma^j,\qquad
N_l=\sum_{j=0}^{h_l-1}\phi^j.
\tag{A6}
$$
在绝对 Galois 群环中保留准确恒等式
$$
(\sigma-1)D_q=h_q\sigma^{h_q}-N_q.
\tag{A7}
$$
没有把 $\sigma^{h_q}$ 在绝对惯性群中误写为一。

由 (A4)，选
$$
Y_l\in\mathscr Q^{G_L},\qquad
Y_{ql}\in\mathscr Q^{G_{EL}}
$$
分别提升 $c_l,c_{ql}$。原 q 方向范数给
$$
\partial_{G_L}\bigl(N_qY_{ql}
       -P_q(\phi^{-1})Y_l\bigr)=0.
$$
由 (A4) 差项来自 $\mathscr I^{G_L}$；再由 (A5)，可从
$\mathscr I^{G_{EL}}$ 中取其范数原像，调整 $Y_{ql}$ 而不改变其上同调类。于是可以而且现在固定
$$
\boxed{N_qY_{ql}=P_q(\phi^{-1})Y_l\quad\hbox{在 }\mathscr Q\hbox{ 中}.}
\tag{A8}
$$

随后定义
$$
Y_1=u_l^{-1}N_lY_l,\qquad
Y_q=u_l^{-1}N_lY_{ql}.
\tag{A9}
$$
正文 (15) 准确给
$$
Y_1\in\mathscr Q^G,\quad
Y_q\in\mathscr Q^{G_E},\quad
\partial_GY_1=c_1,\quad
\partial_{G_E}Y_q=c_q.
\tag{A10}
$$
两个定义使用同一个原单位 $u_l$，不是分别重标定底类。

在 $\mathscr Q^{G_{EL}}$ 上，原有限商
$\operatorname{Gal}(EL/K)$ 交换，因此 (A8)–(A10) 给
$$
N_qY_q=P_q(1)Y_1=0.
\tag{A11}
$$
再由 (A7) 和 $h_qA_N=0$，$D_qY_q$ 被整个 $G$ 固定。定义
$$
\kappa_{q,N}=\partial_G(D_qY_q)\in H^1(K,A_N).
\tag{A12}
$$
其限制准确是
$$
\operatorname{res}_{E/K}\kappa_{q,N}=D_qc_q.
\tag{A13}
$$
原十七惯性元 $\gamma$ 固定 $E$ 并在 $A_N$ 上作用为 $-1$，故
$H^0(E,A_N)=0$。Inflation–restriction 因此说明满足 (A13) 的下降类唯一。特别 $\kappa_{q,N}$ 不依赖辅助 $l$ 或上述 lift 的选择；$l$ 用于证明它的实际局部读数。

### A.3 绝对局部分解群中的交换子为何真的消失

令 $D_{\mathfrak q}$、$I_{\mathfrak q}$ 为选定的绝对局部分解群与惯性群。先取 $M=L$ 或 $EL$，以及原类 $c_M$ 的任一 lift
$\widehat Y_M\in\mathscr I$。

原表示在 $q$ 处不分歧。原整类 $c_M$ 在 $M$ 的 q 位也确实未分歧：原最高有理局部群为零，而
$H^1(I_{\mathfrak q}\cap G_M,T)
=\operatorname{Hom}_{\rm cont}(I_{\mathfrak q}\cap G_M,T)$
无挠，所以原整局部类的惯性限制为零。约到 $A_N$ 后仍为零。
这里用的是原整类的来源，不是宣称全部 $H^1(M_w,A_N)$ 都未分歧。

因此，对 $s\in I_{\mathfrak q}\cap G_M$，
$$
(s-1)\widehat Y_M=0.
\tag{A14}
$$
因为 $A_N$ 的惯性作用平凡，这句话不依赖 cocycle 代表或 lift 的选择。

$M/K$ 阿贝尔，且 $D_{\mathfrak q}/I_{\mathfrak q}$ 交换，所以
$$
[D_{\mathfrak q},D_{\mathfrak q}]
\subset I_{\mathfrak q}\cap G_M.
\tag{A15}
$$
右侧在 $D_{\mathfrak q}$ 中正规。(A14) 因而也作用为零于
$\widehat Y_M$ 的整个 $D_{\mathfrak q}$ 轨道。于是局部分解群中的任意两个元在这个轨道生成的模上真正交换。

这正是后面交换 $N_q,N_l,P_q(\phi^{-1})$ 所需的结论。它并不从
$\operatorname{Gal}(EL/K)$ 交换直接提升到任意 $\mathscr I$-元；
原未分歧条件 (A14) 是必要的一步。

### A.4 完整 lift 范数误差由同一大剩余次数杀掉

固定任意 $\widehat Y_l,\widehat Y_{ql}$，并采用 (A9) 的实际 lifts
$$
\widehat Y_1=u_l^{-1}N_l\widehat Y_l,\qquad
\widehat Y_q=u_l^{-1}N_l\widehat Y_{ql}.
\tag{A16}
$$
由 (A8)，
$$
B=N_q\widehat Y_{ql}-P_q(\phi^{-1})\widehat Y_l\in A_N.
\tag{A17}
$$
由 A.3 的局部交换性，原 lift 误差准确为
$$
\begin{aligned}
N_q\widehat Y_q-P_q(\phi^{-1})\widehat Y_1
&=u_l^{-1}N_l
   \bigl(N_q\widehat Y_{ql}-P_q(\phi^{-1})\widehat Y_l\bigr)\\
&=u_l^{-1}N_lB=0.
\end{aligned}
\tag{A18}
$$
最后一步用了 $\phi$ 在 $A_N$ 上作用为
$a_q\equiv1$，以及正文已付的**完整** $h_l$ 阶：
$N_lB=h_lB=0$。因此
$$
\boxed{N_q\widehat Y_q=P_q(\phi^{-1})\widehat Y_1
       \quad\hbox{在 }\mathscr I\hbox{ 中}.}
\tag{A19}
$$
这不是只在商模中成立的等式，也没有留下未受控的 augmentation 误差。

### A.5 一侧有限—奇异读数

用 (A12) 的 boundary 代表并保 (A7)，得
$$
\begin{aligned}
\kappa_{q,N}(\sigma)
&=(\sigma-1)D_q\widehat Y_q\\
&=-N_q\widehat Y_q\\
&=-P_q(\phi^{-1})\widehat Y_1\\
&=(\phi^{-1}-1)\widehat Y_1\\
&=-\phi^{-1}(\phi-1)\widehat Y_1
=-c_1(\operatorname{Fr}_{\mathfrak q})
\quad\hbox{在 }A_N\hbox{ 中}.
\end{aligned}
\tag{A20}
$$
第二步用了 $p^N\mid h_q$；第四步用了 $P_q(X)=1-X$；
最后一步用了 $\phi|_{A_N}=1$ 以及 (A10)。

原 $c_1$ 在 $\mathfrak q$ 未分歧，故右边是其准确有限局部 Frobenius 读数。
$\sigma$ 在原 $G_q$ 中为生成元，因而其 tame p 分量是一个单位倍的拓扑生成元。因此左边确是完整奇异坐标；它没有额外的 p 因子。

本附录只证明 (A20) 在指定 $\mathfrak q$ 的等式。
$\bar{\mathfrak q}$ 的奇异坐标仍保留；没有将另一 Euler 方向的多项式或 Frobenius 规范悄悄换入。下一附录会用原双点 selector 令配对测试在那一位为零。

## 附录 B. 原底类非零时的 balanced Selmer 秩一

这里给一个直接的有条件结论，不调用尚未核到的 JNS 受限辅助集合扩张，也不调用通常 core-rank-one 的 Mazur–Rubin 定理。

### B.1 原局部条件与一个固定坏位指数

记 $V=T\otimes_{\mathcal O}\mathcal E$，其中 $\mathcal E$ 为系数域。
原 balanced 条件在 $\mathfrak p$ 为全局部群，在
$\bar{\mathfrak p}$ 为零。令 $\Sigma_0$ 为 $K$ 中位于 $2,3,17$ 上的有限素点。

对 $v\in\Sigma_0$，原纯权及共轭自对偶给
$$
H^j(K_v,V)=0\qquad(j=0,1,2).
\tag{B1}
$$
这是原有限 tame 注已核的 ACR Proposition 4.9 证明中 (4.2) 及其后局部对偶论证，且最高直接分量继承此结论。
因此 $H^1(K_v,T)$、$H^2(K_v,T)$ 都是有限 $\mathcal O$-模。
选非负整数 $b_{v,1},b_{v,2}$ 分别使 $p^{b_{v,j}}$ 杀掉它们，并令
$$
C=\max_{v\in\Sigma_0}(b_{v,1}+b_{v,2}).
\tag{B2}
$$
约化长正合列给
$$
0\longrightarrow H^1(K_v,T)/p^N
 \longrightarrow H^1(K_v,A_N)
 \longrightarrow H^2(K_v,T)[p^N]\longrightarrow0,
$$
所以
$$
\boxed{p^C H^1(K_v,A_N)=0
       \quad(v\in\Sigma_0,\ N\ge1).}
\tag{B3}
$$
使用两个指数之和正是为了保留可能非分裂的扩张。
$C$ 只依原固定 $p,T$，与 $N,q,l$ 均无关。

A.2 的 $\kappa_{q,N}$ 在 $q,\bar q,\Sigma_0,p$ 之外未分歧：
$E/K$ 在那里不分歧，其惯性群不变，而 (A13) 的右侧未分歧。
在 $\bar{\mathfrak p}$，原 $\rho_i$ 的惯性角色是
$\varepsilon_{\rm cyc}^{-1}$，其模 p 作用非平凡。
$E/K$ 在 p 处不分歧，因此
$$
H^0(E_w,A_N)=0\qquad(w\mid\bar{\mathfrak p}).
$$
局部 restriction 随之单射。原 $c_q$ 在这些素点严格为零：
若先从有理 balanced 条件读取，此处 $H^1(E_w,T)$ 无挠，仍给整零。
故 (A13) 迫
$$
\operatorname{loc}_{\bar{\mathfrak p}}\kappa_{q,N}=0.
\tag{B4}
$$
$\mathfrak p$ 的条件为全，无额外限制。
于是 $p^C\kappa_{q,N}$ 满足原 balanced 条件及所有固定坏位的零条件，
只有 $q,\bar q$ 可能有奇异分量。

### B.2 定理与最小系数环上的固定证明坐标

**定理。** 对每个原固定普通 $p>211$ 及每个原最高标签
$i\in\{4,10,16\}$，若原端点类
$$
z^{\rm end}_{i,p}=c_1\ne0\quad\hbox{在 }H^1(K,V),
\tag{B5}
$$
则
$$
\boxed{\dim_{\mathcal E}\operatorname{Sel}_{\rm bal}(K,V)=1,
\qquad
\operatorname{Sel}_{\rm bal}(K,V)=\mathcal E\,c_1.}
\tag{B6}
$$

为避免把扩大系数后的有限 Galois 像误认成整个系数模，秩界证明先回到实际最小环
$$
\mathcal O_0=\mathbf Z_p[\mu_{18}],\qquad
\mathcal E_0=\operatorname{Frac}(\mathcal O_0).
\tag{B7}
$$
它在 $\mathbf Z_p$ 上不分歧；$\rho_i$ 的值都在
$\mathcal O_0^\times$，因为两条 CM Tate 角色的值在
$\mathbf Z_p^\times$。选择原 $T$ 的一条整基，令
$T_0=\mathcal O_0(\rho_i)$ 使用该基，则
$T=T_0\otimes_{\mathcal O_0}\mathcal O$。

$\mathcal O$ 在 $\mathcal O_0$ 上有限自由。取一组这样的基及其坐标行
$\vartheta:\mathcal O\to\mathcal O_0$。
连续 cochain 及全部 restriction、corestriction 按这组基分解，故
$$
H^1(K[n],T)=H^1(K[n],T_0)\otimes_{\mathcal O_0}\mathcal O,
\qquad
\operatorname{Sel}_{\rm bal}(K,V)
=\operatorname{Sel}_{\rm bal}(K,V_0)
 \otimes_{\mathcal E_0}\mathcal E,
\tag{B8}
$$
其中 $V_0=T_0\otimes\mathcal E_0$。第二式也直接由原 full/zero 及未分歧局部条件的核与有限平坦扩系数相容得到。

由 (B5)，可一次选定一个 $\vartheta$，使
$$
c_1^0:=\vartheta(c_1)\ne0.
$$
在所有原层同时定义 $c_n^0=\vartheta(c_n)$。
最高 Euler 多项式 $P_q$ 的系数属于 $\mathcal O_0$，所以这仍是一族在 $T_0$ 上整的四角范数系统，具有同一个固定分母及同样的 balanced 条件。$\vartheta$ 在选择 $N,q,l$ **之前**固定，不随辅助层改变。

这只是秩界证明使用的一个原系数坐标。原实际系统仍是 (3)，原底类仍是 $c_1$；没有声称 $c_1^0$ 与它数值相等，更没有替成另一条 canonical 类。若在 $V_0$ 上证明维数至多一，(B8) 即将结论送回整个原 $V$，而 (B5) 保证原 $c_1$ 张成这一维空间。

令 $T_0^c$ 为同一底格、共轭 Galois 作用，系数保持固定。
$\rho_i\rho_i^c=\varepsilon_{\rm cyc}$ 给完美配对
$$
T_0\times T_0^c\longrightarrow\mathcal O_0(1).
\tag{B9}
$$
选择基归一这个 Tate 对偶标识不重标任何 Euler 类。

以下将 B.1 的固定指数 $C$ 应用于 $T_0$，仍与 $N,q,l$ 无关。
取固定分歧集
$\Sigma=\Sigma_0\cup\{v\mid p\}$，
令 $S_0$ 为原有理 balanced Selmer 群在
$H^1(G_{K,\Sigma},T_0)$ 中的逆像。
它有限生成且饱和。十七惯性标量 $-1$ 给
$H^0(K,V_0/T_0)=0$，故 $H^1(G_{K,\Sigma},T_0)$ 无挠，$S_0$ 自由；
饱和性还给
$S_0/pS_0\hookrightarrow H^1(K,T_0/p)$。

若其秩至少二，可以取
$$
c_1^0=p^v z,\qquad z,d\in S_0,
\tag{B10}
$$
使 $z$ 本原，且 $z,d$ 的模 p 像线性无关。这里 $\mathcal O_0$ 不分歧，故 p 本身是素元。固定
$$
N>C+v.
\tag{B11}
$$

### B.3 同一个检测素数处的两个完整读数

将已付的最小环双点 selector 应用于 $z,d$ 及它们的共轭类，
在平凡化 $T_0/p^N$、其共轭和 $\mu_{p^N}$ 的同一有限域上，
同时添加原 $H_\eta K(E_0[p])$ 的 $\tau$ 条件。
于是选到 $q\in\mathcal L_1$ 满足 (A1)，并在固定两点 Frobenius 标识下准确实现
$$
\begin{pmatrix}
z(\operatorname{Fr}_{\mathfrak q})&
d(\operatorname{Fr}_{\mathfrak q})\\
z(\operatorname{Fr}_{\bar{\mathfrak q}})&
d(\operatorname{Fr}_{\bar{\mathfrak q}})
\end{pmatrix}
=
\begin{pmatrix}1&0\\0&1\end{pmatrix}
\quad\hbox{于 }\mathcal O_0/p^N.
\tag{B12}
$$
这是最小环上的已证明全读数，不借扩大系数版本的非零行列式冒充任意矩阵。

原 $d$ 在两个 q 位未分歧，且有限模 Frobenius 作用为一，故
$$
\operatorname{loc}_{\mathfrak q}d=0,\qquad
d(\operatorname{Fr}_{\bar{\mathfrak q}})=1.
\tag{B13}
$$
第一项是完整有限局部零，不仅是一个部分读者为零。

现在对这个 $q$ 按正文选 $l$，再将附录 A 作用于固定坐标系统 $c_n^0$，
得到唯一 $\kappa^0_{q,N}$。其一侧读数是
$$
\kappa^0_{q,N}(\sigma)=-p^v
\quad\hbox{于 }T_0/p^N,
\tag{B14}
$$
而 $\bar{\mathfrak q}$ 的奇异项继续保留。
辅助 $l$ 不改变原检测 $q$、原十七数据或固定的 $\vartheta$。

### B.4 共轭配对与全局互反

将 $p^C\kappa^0_{q,N}$ 与 $d^c\bmod p^N$ 通过 (B9) 作 cup product，
再取局部不变量。这里
$d^c(g)=d(cgc^{-1})$，外部复共轭满足 $c^2=1$，不作用于系数。
所以 $d^c$ 在 $\mathfrak q$ 读取原 $d$ 在
$\bar{\mathfrak q}$ 的值，在 $\bar{\mathfrak q}$ 读取原 $d$ 在
$\mathfrak q$ 的值。这是消去第二个未知奇异项的准确方向。

全局互反给所有地方贡献之和为零，其各项为：

- 在 $\Sigma_0$，第一类由 B.1 的统一指数为零。
- 在 $\mathfrak p$，$d^c$ 为零，因为原 $d$ 在
  $\bar{\mathfrak p}$ 严格为零。
- 在 $\bar{\mathfrak p}$，第一类由 (B4) 为零。
- 在 $q,\bar q,\Sigma$ 以外，两类均未分歧；未分歧商的 p-上同调维数为一，所以 cup 为零。
- 在 $\bar{\mathfrak q}$，$d^c$ 是 (B13) 第一项的共轭标识，故整个局部类为零。
- 复地方不贡献。

因此只剩 $\mathfrak q$。该处 $T_0/p^N$、其对偶和
$\mu_{p^N}$ 都平凡。
$\sigma$ 的 tame p 分量是一个拓扑生成元的单位倍；用它与算术 Frobenius 作坐标，
局部 Tate 配对在“奇异 $\times$ 未分歧”部分是乘法乘一个单位。
由 (B12)–(B14)，剩余项是
$$
\text{一个单位}\ \cdot\ p^{C+v}
\quad\hbox{于 }\mathcal O_0/p^N.
\tag{B15}
$$
它由 (B11) 非零，与全局互反矛盾。

于是 $\dim_{\mathcal E_0}\operatorname{Sel}_{\rm bal}(K,V_0)\le1$。
(B8) 将此送回原系数域；再用 (B5) 得到恰为一及 (B6)。证毕。

### B.5 此结论新增了什么，仍保留什么

附录 A 的一侧有限—奇异式及本附录的秩界，已经针对原环类系统直接证明。因而这一步不再依赖“受限辅助集合是否几乎包含 JNS 默认集合”的未付扩展，也没有借通常 core rank 为一的定理。

结论的前提仍是**原端点** $z^{\rm end}_{i,p}$ 非零。
R817 在 $7993$ 检测的 canonical 类不因此自动成为该端点。
即使 (B6) 成立，指定 ordinary 局部化仍可能在这一维空间上为零；
本证明没有把它与底类非零合并，也没有由固定 p 的条件结论推出无穷目标 p。

实际原文依据为：
Rubin [1999 作者讲义](https://swc-math.github.io/aws/1999/99RubinES.pdf)
Chapter I §§4、7 的局部对偶与全局互反，
Chapter IV §7 的 lift 交换子计算及 Chapter IX §1 的 rigidity 机制；
以及 ACR [正式刊本](https://web.math.ucsb.edu/~castella/ACR1-print.pdf)
Proposition 4.9（印 pp.20–21）和 §8.1 的共轭自对偶局部条件。
这里 (A3)–(A20)、(B2)–(B15) 已对原四角、原两个素点与原固定格逐项证明，没有直接引用原书 full ray 系统的结论。

本增补未执行数学程序，未改变原最低层、测试函数、有限角色或任何来源归一。
