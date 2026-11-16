# R891. 原环类系统的 anti-Kummer 辅助素数与四角局部结构

日期：2026-11-16。**状态：本文先完整证明原有限 tame 系统所需的辅助素数引理。** 它同时保留原十七处角色、任意指定的 p-adic 深度、此前的整个 p 环类层，以及新环类层中两个共轭素点的完整分解群。这里尚不声明有限—奇异关系、Selmer 秩界或原底类非零；后续 cochain 论证须作用于下述同一四角系统。

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
两个角是同一个 $u_l$，全部等式均发生在原固定格上；没有扩大层数而引入新的 p 分母。两个 q 方向则仍保留其真实 Frobenius Euler 算子。本文尚未从 (13) 的有限交换性推出任意 cochain lift 上的交换性。

## 6. 已付范围与下一步

(4)–(15) 完整支付 Rubin rigidity 方法在本题原环类系统中的辅助素数部分，包括此前容易遗漏的 anti-Kummer 比、全 $h_l$ 阶和两共轭素点。它不依赖全 ray-class Euler 系统，也不将 R886 的狭义 $\mathcal L_1$ 自动扩大为所有 split primes。

接下来须在同一四角 (12) 上逐项证明连续 coinduced 模的范数满射、实际 lift 的范数误差消失以及一侧有限—奇异读数；这些尚不由 (15) 单独推出。原底类 $c_1$ 是否非零，及非零类在指定 ordinary 局部化是否仍非零，是另外两个问题。

原文对照：[Rubin, *Euler Systems*, 1999 作者讲义](https://swc-math.github.io/aws/1999/99RubinES.pdf)，Chapter IV §7（印 pp.74–76）以及 Chapter IX §1（印 pp.134–135）。原书使用的 Kummer 辅助选择在这里由 (4)–(11) 针对原环类商重新证明；未把原书全 ray 系统的结论直接套入。原完整 finite tame 来源及统一分母见
[原端点 tame 系统](../notes/2026-11-16-original-endpoint-tame-norm-system.md)，原两类辅助集合与单位归一见 R886 正文及附录 A。

本证明没有数学程序执行或新的数值证书。
