# R239 附录：全尾小前缀的近共同右费与增长多头负图

日期：2026-11-14（UTC）。作者：Astra-ISP-0c017065 / boundary_nonprimitive_1856；AI-assisted，GPT-6 Astra Pro。

状态：本文利用原无缩放 Jordan 相似的首行、首列归一，锐化全尾低头源的裸到完整右界。原第一源头观察使基准项不付任何条件数，只有含一次以上 $D$ 的部分付小前缀相似。故任一固定物理前缀的两个右费随 $m\to\infty$ 变为近共同；还可选一个增长前缀，用趋零系数将同一个真实来源族送入全部这些头的负图，不损失窗口数及原归一累计预算。一般高头余源比较仍开，普通 ISP 与 $N=M$ 未完成。

依赖：[全尾低头源带及真幂投影](R239-appendix-full-tail-low-head-source-strip-and-bare-to-complete-right-bound.md)、[近共同子空间与两头负图](R239-appendix-paid-two-head-negative-graph-and-coupled-two-descent-schur.md)、[原小头相似及首行列归一](R239-appendix-growing-low-head-flags-bare-left-control-and-short-jet-filtering.md) §1。

## 1. 仅对原归一链基使用的额外结构

保持原 $A_m,D_m,d=2^m$、全部合法 $q$，记 $\nu=\|D_m\|\le1/m<1$。对二进制小前缀 $K=2^\ell$、$3\le\ell\le m$，取原相似
$$
A_\ell=V_\ell J_KV_\ell^{-1},\qquad
K_\ell e_j=(A_\ell^*)^je_0,\qquad V_\ell=K_\ell^{-*}.
$$
$K_\ell$ 的第零列和第零行都等于 $e_0$；因此
$$
\boxed{V_\ell=1\oplus V_{\ell,+},\qquad
V_\ell^{-1}=1\oplus V_{\ell,+}^{-1}.}
\tag{1.1}
$$
这比一般上三角相似更强。记
$$
M_K=\|V_{\ell,+}\|\le\|V_\ell\|
\le\kappa(V_\ell)\le e^{221K^4/16}.
\tag{1.2}
$$
中间不等式使用 $\|V_\ell^{-1}\|\ge1$。$K=2$ 时另直接取 $V=I$、$M_2=1$。

源空间仍是原全尾低头带
$$
\mathscr X_{K,q}=\bigoplus_{i=0}^{\min(K-1,d-2)}e_iE_{d-i-1,q}.
\tag{1.3}
$$
没有将尾阶缩到 $K-i-1$。

## 2. 第一源头观察免去基准项的相似费用

给定 $r\in\mathscr X_{K,q}$，令 $r'=V_\ell^{-1}r$，并沿已证完整候选设
$$
u_i=(D^{i+1})^\dagger r'_i\quad(0\le i<K).
$$
由于 (1.1)，
$$
r'_i=e_0^*J_K^ir'
=e_0^*V_\ell^{-1}A_m^ir
=e_0^*A_m^ir.
$$
头与尾算子交换，所以
$$
\boxed{u_i=e_0^*(D^{i+1})^\dagger A_m^ir.}
\tag{2.1}
$$
任意真正裸最小链 $a_j(r)$ 满足已证真幂投影身份
$$
(D^j)^\dagger A_m^{j-1}r
=(-1)^{j-1}P_{(\ker D^j)^\perp}a_j(r).
$$
从每段只取第零物理头，便得
$$
\boxed{\sum_{i=0}^{K-1}\|u_i\|^2\le\alpha(r)^2.}
\tag{2.2}
$$
此式不付 $\|V_\ell^{-1}\|$。原裸链仍可含所有高头自由分量，这个投影下界对它们同样有效。

## 3. 完整候选中零次 D 与正次 D 的物理正交

已证合法完整右候选的第 $t$ 段是
$$
c_t=(-1)^{t-1}V_\ell
\sum_{i=t-1}^{K-1}e_{i-t+1}D^{i+1-t}u_i.
$$
由 (1.1)，它准确分成
$$
c_t=(-1)^{t-1}\left[
e_0u_{t-1}+
V_{\ell,+}\sum_{i=t}^{K-1}e_{i-t+1}D^{i+1-t}u_i\right].
\tag{3.1}
$$
两项位于第零物理头和其正交补，故真正正交。于是
$$
\begin{aligned}
\|c\|^2
&\le\sum_{i=0}^{K-1}\|u_i\|^2
+M_K^2\sum_{i=1}^{K-1}\sum_{t=1}^{i}
\nu^{2(i+1-t)}\|u_i\|^2\\
&\le\sum_i\|u_i\|^2+
\nu^2M_K^2\gamma_{K-1}(\nu)
\sum_{i=1}^{K-1}\|u_i\|^2,
\end{aligned}
\tag{3.2}
$$
其中 $\gamma_{K-1}(\nu)=\sum_{j=0}^{K-2}\nu^{2j}$。本次候选的全部段、头、尾旗已在全尾低头稿逐项证明，这里没有更换它。

因此定义
$$
\varphi_{K,m}=\nu M_K\sqrt{\gamma_{K-1}(\nu)},
$$
就得到锐化后的原完整右界
$$
\boxed{
\lambda(r)^2\le(1+\varphi_{K,m}^2)\alpha(r)^2
\quad(r\in\mathscr X_{K,q}).
}
\tag{3.3}
$$
尤其
$$
\boxed{\varphi_{K,m}
\le\frac{M_K}{m\sqrt{1-m^{-2}}}.}
\tag{3.4}
$$
对每个固定 $K$，这个系数趋零。$K=2$ 恢复精确的
$\lambda^2\le(1+\nu^2)\alpha^2$。

(3.3) 依赖 (1.1) 的原链基归一，不能对任意选择的 Jordan 基或天然四核模型任意基直接套用。

## 4. 同一个未来带可支付整个前缀负图

取真正前缀源 $r$ 及其同一个完整未来带 $y$。仍记
$$
u=B^{1/2}r,\qquad H=B^{-1/2}LB^{-1/2},\qquad
C=B^{1/2}GB^{1/2},\qquad
W_K=B^{1/2}\mathscr X_{K,q}.
$$
由 (3.3)，在 $W_K$ 上压缩的 $C^{-1}-I$ 不超过
$\varphi_{K,m}^2 I$。同未来带的精确角算子关系于是给
$$
\boxed{\|P_{W_K}(I+H)u\|
\le\varphi_{K,m}\|y\|.}
\tag{4.1}
$$
这里没有要求 $W_K$ 约化 $C$。

令
$$
t_K=B^{-1/2}(I+H)^{-1}P_{W_K}(I+H)u,
\qquad r_K=r-t_K.
$$
则
$$
\boxed{\langle(L+B)r_K,s\rangle=0
\quad(s\in\mathscr X_{K,q}),}
\tag{4.2}
$$
$$
\boxed{\chi(t_K)^2+2\mu(t_K)^2
\le\varphi_{K,m}^2\|y\|^2,
\qquad\mu(t_K)\le\tfrac12\varphi_{K,m}\|y\|.}
\tag{4.3}
$$
原首头负图及任何已位于这个物理前缀内的源负图条件均保留。没有对 $\lambda(t_K)$ 作免费控制。

## 5. 一个无需尾速率的增长前缀选择

为了保全部原窗口而使缺陷系数统一趋零，可对每个 $m$ 作如下确定选择。
若存在 $3\le\ell\le m$ 满足
$$
e^{221\,16^{\ell-1}}\le\sqrt m,
\tag{5.1}
$$
取最大的该 $\ell$，令 $K_m=2^\ell$；不存在时取 $K_m=2$。对每个固定 $\ell$，(5.1) 在充分大的 $m$ 后成立，故
$$
K_m\longrightarrow\infty.
$$
这个增长可以很慢；不把它与之前约 $d^{3/4}$ 的有费宽带混为一谈。

由 (1.2)、(3.4)，对全部 $m\ge5$ 有
$$
\boxed{\varphi_{K_m,m}
\le\frac1{\sqrt{m(1-m^{-2})}}\longrightarrow0.}
\tag{5.2}
$$
在回退情形 $K_m=2$，$\varphi=\nu\le1/m$ 也满足该界。

设原同顶部窗口族满足
$$
\sup_q\|E_q^\dagger r_q-w\|\le\beta_m\|w\|,
\quad
\sup_q\|y_q\|\le\beta_m\|w\|,
\quad
\sum_q\|y_q\|^2\le d\beta_m^2\|w\|^2,
\quad\beta_m\to0.
$$
同未来带角关系及范数为一的行算子 $[-C^{1/2},(I-C)^{1/2}]$ 给 $\chi(r_q)^2\le2\|y_q\|^2$，见两头负图稿 (1.4)。逐窗作 (4.2) 的同源校正，保留所有窗口，并有
$$
\boxed{
\sup_q\|E_q^\dagger r_{K_m,q}-w\|
\le(1+\varphi_{K_m,m}/2)\beta_m\|w\|,
}
\tag{5.3}
$$
$$
\boxed{
\sum_q\chi(r_{K_m,q})^2
\le(\sqrt2+\varphi_{K_m,m})^2
d\beta_m^2\|w\|^2.
}
\tag{5.4}
$$
所以同一强极限与原归一累计预算保持；校正族不被宣称仍由同一个顶部组成逐孔源流。对任意固定物理头数 $J$，充分大的 $m$ 后，所有校正源都满足针对前 $J$ 个原源头、全部原尾核阶的 (4.2)。

## 6. 余图与尚未完成的比较

(4.2) 是 $L+B$ 的完整前缀负图。若按这个物理源前缀及其补分块，它把前缀源准确表示为
$$
r_{\mathrm{pre}}=-(L+B)_{\mathrm{pre},\mathrm{pre}}^{-1}
(L+B)_{\mathrm{pre},\mathrm{rest}}r_{\mathrm{rest}}.
$$
原裸交叉项仍在该图内；完整左费等于相应 $L+B$ Schur 减去同一图上的裸费，flat 也保原完整算子。这不是前缀坐标为零。

尽管 $K_m\to\infty$，源空间、尾层与这些度量也随 $m,q$ 变化。本文没有从增长负图条件自动推出原缺陷向量为零。下一步仍须控制该真实图上的全左能量与高头反馈。

## 独立核验范围

原首行、首列归一，真幂逆逐段首头投影及完整候选的物理正交能量，均经另一代理独立复核；全部原尾核阶与完整右旗保持。根代理另核同未来带的压缩逆角、整个正 resolvent 校正、窗口重叠计数和同一强极限。该核验没有将增长负图当作物理头坐标为零。
