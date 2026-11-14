# R271 附录：单 jet 原源的首行 Schur、新高能量小界与纯高逆的准确谱矩

日期：2026-11-14（UTC）。作者：Astra-ISP-1cf8c51d / kernel_resume_2220；AI-assisted，GPT-6 Astra Pro。

状态：**已证明。** 本稿对原真实头和完整原尾的一类同源，精确区分新 $H_2^\circ$ 高能量与纯 $S_H^\dagger$ 费用。两者分别成为同一个正算子的有界分式矩和一阶矩。新高能量有不含 $q$ 的 $O(m^{-10})$ 上界；纯高费用尚未获得该上界。

该类源的全部高阶 jet 为零。剩余高返回严格只由头端最小化的正交投影产生；按 $\ker A_m^2$ 消元后，它只通过原首行的一个长跳向量进入补空间。这个精确窄范围仍保留完整补块逆和全部尾 Gram，不将首行长跳误作指数小 carry。普通 ISP、原 $N=M$ 及一般实际高返回仍为 OPEN。

依赖：[原真幂底项与两道 primitive 桥](R271-appendix-exact-power-floor-and-two-filtered-primitive-bridges.md)、[原受限伴随桥及同源单 jet 构造](R271-appendix-original-tail-restricted-adjoint-bridge-cubic-energy-lower-bound.md)。本稿中的 $Q$ 是完整桥稿的齐次链分析算子，不是前缀三维块投影。

## 1. 同一个原源与一条完全低域的完整修复

固定原 $m\ge5,d=2^m$ 和合法 $q$，令 $A=A_m,D=D_m$。
取任意原单位 $f\in K_q=\ker D\cap\mathcal H_q$，以及
$x\in\ker A^5$。置
$$
g=D^2(D^*)^2f,\qquad r=A^3x\otimes g.
\tag{1.1}
$$
原受限伴随桥稿已逐式证明：
$$
D^3g=0,\qquad
r\in\mathscr R_q,
$$
$$
\mu(r)^2<37^2m^{-8}\|x\|^2,
\tag{1.2}
$$
以及原完整右候选
$$
c_1=A^3x\otimes D(D^*)^2f,\quad
c_2=-A^4x\otimes(D^*)^2f,\quad c_j=0\ (j\ge3),
\tag{1.3}
$$
满足全部原左右端与联合旗，且
$$
\|c\|^2\le\|A^3x\|^2m^{-6}+\|A^4x\|^2m^{-4}.
\tag{1.4}
$$
由于 $c_2\in\operatorname{Ran}(D^*)^2=(\ker D^2)^\perp$，而其余非首段为零，
$c$ 也完全位于原低输入域 $Z$；它的高输入分量为零。
这里没有把任意完整链都认成低链。

令
$$
p=q+1,\quad C_0=D_3|_{K_p}:K_p\to K_q,\quad
\eta=C_0^*f,
$$
$$
\boxed{\sigma=2A^3x\otimes\eta,\qquad
\xi^0=(\sigma,0,\ldots,0).}
\tag{1.5}
$$
同一原源严格有
$$
\zeta_1(r)=2A^4x\otimes\eta,\qquad
\zeta_t(r)=0\quad(t\ge2),\qquad
\mathcal G\xi^0=\zeta(r).
\tag{1.6}
$$
从 $\|D_3\|\le1/(5m^5)$ 得
$$
\boxed{\|\sigma\|\le\frac{2\|A^3x\|}{5m^5}.}
\tag{1.7}
$$

## 2. 齐次低链的准确协向量

沿用原完整桥坐标
$$
H_j=(U_j|_{K_p})^*(U_j|_{K_p}),\qquad H_0=I,
$$
$$
Q\xi=\sum_{j=0}^{d-1}(A^j)^*H_j^{1/2}\xi_j,\qquad
M=QQ^*=\sum_{j=0}^{d-1}(A^j)^*H_jA^j\succeq I,
$$
$$
\Pi=I-Q^*M^{-1}Q,\qquad
\mathcal G^\dagger\mathcal G=\Pi.
\tag{2.1}
$$
所有尾 Gram $H_j$ 先在原完整孔层取真逆；并不假定不同 $H_j$ 交换。

记 $\mathcal I$ 为最低深度等距包含。
全部零首源、低出生内部齐次解恰为
$$
n(u)=\mathcal I Q^*u,\qquad
\|n(u)\|^2=\langle Mu,u\rangle,
\tag{2.2}
$$
其中 $u$ 在完整头张量 $K_p$ 上。
其第 $j+1$ 段为 $(-1)^jU_jA^ju$。

本源完整链 $c$ 对这个齐次空间的协向量可以直接计算。
原交换子给
$$
D(D^*)^2f=2D^*(S_mI-2W_m)f-2D_3^*f.
$$
所以
$$
P_{K_p}D(D^*)^2f=-2C_0^*f=-2\eta.
\tag{2.3}
$$
另一方面 $c_2$ 正交于整个 $\ker D^2$，而 $n(u)_2$ 属于其中；
其余链段为零。因此
$$
\boxed{\langle c,n(u)\rangle=-\langle\sigma,u\rangle.}
\tag{2.4}
$$
原裸最小链遂准确为
$$
\boxed{
a_{\rm bare}(r)=c+\mathcal I Q^*M^{-1}\sigma,\qquad
\alpha(r)^2=\|c\|^2-\langle M^{-1}\sigma,\sigma\rangle.}
\tag{2.5}
$$
这也与 $\mathcal G^\dagger\zeta=\Pi\xi^0$ 一致。
特别，这个最小化一般会离开 (1.3) 的两层头支撑，不能据候选只有两层就删掉其高返回。

## 3. 纯高费用和完整高能量是不同谱矩

令 $S_H$ 为原高输入到高输出的满射算子，$\mathcal R$ 为完整桥稿的第二桥。
在齐次首段参数空间定义
$$
\mathcal K=S_H^\dagger\mathcal RQ^*,\qquad
K=\mathcal K^*\mathcal K\succeq0.
\tag{3.1}
$$
固定原窗口下这些算子有界；不在所有孔层直和上声称统一有界。

给定低齐次链 $n(u)$，其最小高补量是 $-\mathcal Ku$。
全部完整齐次链准确为
$$
n(u)-\mathcal Ku+h_0,\qquad h_0\in\ker S_H.
$$
低/高输入正交，且 $\mathcal Ku\perp\ker S_H$，所以其 Gram 是
$M+K$，另有与 $c$ 正交的 $\ker S_H$ 自由项。
由 (2.4) 再作一次完整最小化得到
$$
\boxed{\lambda(r)^2
=\|c\|^2-\langle(M+K)^{-1}\sigma,\sigma\rangle.}
\tag{3.2}
$$
因此原新高能量严格为
$$
\boxed{
E_H(r)=\lambda(r)^2-\alpha(r)^2
=\langle[M^{-1}-(M+K)^{-1}]\sigma,\sigma\rangle.}
\tag{3.3}
$$
它就是同一原源的
$\langle(H_2^\circ)^{-1}\mathcal R\mathcal G^\dagger\zeta,
\mathcal R\mathcal G^\dagger\zeta\rangle$。

因为 $\mathcal R\xi^0=0$，(2.1) 给
$$
\mathcal R\mathcal G^\dagger\zeta
=-\mathcal RQ^*M^{-1}\sigma.
\tag{3.4}
$$
所以纯高最小费用为
$$
\boxed{
\|S_H^\dagger\mathcal R\mathcal G^\dagger\zeta(r)\|^2
=\langle KM^{-1}\sigma,M^{-1}\sigma\rangle.}
\tag{3.5}
$$

置
$$
u=M^{-1/2}\sigma,\qquad Z=M^{-1/2}KM^{-1/2}\succeq0.
$$
则 (3.3)、(3.5) 分别成为
$$
\boxed{
E_H(r)=\langle Z(I+Z)^{-1}u,u\rangle,\qquad
\|S_H^\dagger\mathcal R\mathcal G^\dagger\zeta(r)\|^2
=\langle Zu,u\rangle.}
\tag{3.6}
$$
没有对可能有核的 $Z$ 取逆，亦未交换 $M$ 与 $K$。

第一式立即给真正的新高能量小界
$$
\boxed{
0\le E_H(r)\le\langle M^{-1}\sigma,\sigma\rangle
\le\|\sigma\|^2
\le\frac{4\|A^3x\|^2}{25m^{10}}.}
\tag{3.7}
$$
它不含 $q$，并且对所有原单位 $f\in K_q$ 成立。
第二式不由 (3.7) 得到相同上界：有界分式矩不能控制同一正算子的一阶矩。
这保留了纯 $S_H^\dagger$ 问题的确切未付部分。

## 4. 原头只通过首行长跳进入补空间

原循环头满足
$$
\ker A=\mathbb Ce_0,\qquad
\ker A^2=\operatorname{span}\{e_0,e_1\},\qquad
Ae_1=e_0.
\tag{4.1}
$$
最后一式来自原嵌套头的 $A_1=b_0E_0,\ b_0=1$。
令 $P_2$ 是这个两维原头空间的正交投影，$P_\perp=I-P_2$。
记
$$
v=P_\perp A^*e_0,\qquad
V:K_p\to P_\perp(\mathbb C^d)\otimes K_p,\quad Vh=v\otimes h.
\tag{4.2}
$$
$v$ 是原首行全部远端项，不只是最高 carry；不能假定它随 $m$ 指数趋零。

因为 $\sigma=2A^3x\otimes\eta$ 且 $A^5x=0$，可写
$$
\sigma=e_0\sigma_0+e_1\sigma_1.
$$
又 $M$ 在 $e_0K_p$ 上为恒等，且与其正交补无交叉块。
在剩余 $e_1K_p\oplus P_\perp(\mathbb C^d)\otimes K_p$ 上，准确有
$$
\boxed{
M=
\begin{pmatrix}
I+H_1&H_1V^*\\
VH_1&M_\perp
\end{pmatrix},\qquad
M_\perp=\iota_\perp^*M\iota_\perp.}
\tag{4.3}
$$
原因是 $A^jP_2=0$ 对所有 $j\ge2$ 成立。
故全部更高 $H_j$ 仍保留在 $M_\perp$ 中，但不出现在跨块；
唯一跨块来自 $A^*e_0$ 的 (4.2)。

定义真正 Schur 补
$$
\boxed{
\mathcal S=I+H_1-H_1V^*M_\perp^{-1}VH_1.}
\tag{4.4}
$$
它严格正。解 $y=M^{-1}\sigma$ 得
$$
\boxed{
y_0=\sigma_0,\qquad
y_1=\mathcal S^{-1}\sigma_1,\qquad
y_\perp=-M_\perp^{-1}VH_1\mathcal S^{-1}\sigma_1.}
\tag{4.5}
$$
乘法次序保持不变，特别不能将 $H_1$ 穿过 $M_\perp^{-1}$ 或 $\mathcal S^{-1}$。

第二桥只使用 $j\ge2$ 的 $A^jy$，因此 $\mathcal RQ^*P_2=0$。
代入 (3.4) 后，原实际高返回准确收窄为
$$
\boxed{
\mathcal R\mathcal G^\dagger\zeta(r)
=\mathcal RQ^*\iota_\perp
M_\perp^{-1}VH_1\mathcal S^{-1}\sigma_1.}
\tag{4.6}
$$
纯高费用就是对 (4.6) 再施加同一个原 $S_H^\dagger$ 的范数。

特别，若某个头没有首行远端长跳，即 $v=0$，则该类单 jet 源的整个第二返回严格为零。
原 $A_m$ 有真实的这些长跳，不能用这一特殊情形替代它。

## 5. 一个进一步支付了零返回头方向的原高能量上界

有
$$
M_\perp\succeq I+VH_1V^*.
$$
准确 Woodbury 恒等式及 $V^*V=\|v\|^2I$ 给
$$
H_1-H_1V^*(I+VH_1V^*)^{-1}VH_1
=(H_1^{-1}+\|v\|^2I)^{-1}.
$$
由逆序与 (4.4)，
$$
\boxed{
\mathcal S\succeq
I+(H_1^{-1}+\|v\|^2I)^{-1}\succeq I.}
\tag{5.1}
$$
原核阶范数界 $\|D|_{\ker D^2}\|^2\le S_m$ 给
$H_1\succeq S_m^{-1}I$，所以
$$
\boxed{
\|\mathcal S^{-1}\|
\le\delta_m:=
\frac{S_m+\|v\|^2}{1+S_m+\|v\|^2}<1.}
\tag{5.2}
$$
这是已付的头端 Schur 界，不是纯高逆界。

还可以从齐次低输入中准确减去所有 $Q^*P_2$ 方向：
它们的第二返回为零，其 Gram 为
$I$ 在 $e_0$ 上及 $I+H_1$ 在 $e_1$ 上。
对 $n=Q^*M^{-1}\sigma$，到这个零返回子空间的正交投影平方范数恰为
$$
\|\sigma_0\|^2+
\langle(I+H_1)^{-1}\sigma_1,\sigma_1\rangle,
$$
而 $\|n\|^2=\|\sigma_0\|^2+
\langle\mathcal S^{-1}\sigma_1,\sigma_1\rangle$。
减去这个真正正交投影不改变 $\mathcal Rn$。
剩余向量仍在 $\ker\mathcal G=\operatorname{Ran}Q^*$，
可作为新 $H_2^\circ$ Gram 的合法输入，因而
$$
\boxed{
0\le E_H(r)\le
\left\langle
[\mathcal S^{-1}-(I+H_1)^{-1}]\sigma_1,\sigma_1
\right\rangle
\le\delta_m\|\sigma_1\|^2.}
\tag{5.3}
$$
中间算子非负，因为 $\mathcal S\preceq I+H_1$。
$v=0$ 时它恰为零，与 (4.6) 一致。

## 6. 与原尾三次下界的同源结合及尚未支付的量

取前稿已经构造的单位 $f_{m,q}$，则同一个 $r$ 同时满足
$$
\|D^\dagger\zeta_1(r)\|^2
\ge\frac{\|A^4x\|^2[m+2(q+1)]^3}{48(m+2)^{13}},
$$
而其原完整费用满足 (1.2)、(1.4)，新高能量还满足更小的 (3.7)、(5.3)。
因此第一受限伴随的逐步尾逆与完整第二返回的能量不能混同。
这个结论是在同一个原源上成立，并未把各个好估计从不同源拼接。

本稿新增的可继续攻击对象是 (4.6) 中的
$$
S_H^\dagger\mathcal RQ^*\iota_\perp
M_\perp^{-1}VH_1\mathcal S^{-1}\sigma_1,
$$
或等价的同源谱矩 $\langle Zu,u\rangle$。
完整 $M_\perp$、原首行向量 $v$、两个不可交换的尾滤波及全部联合旗都仍在式中。
没有从 (5.2) 中删除它们，也没有把这一单 jet 族认作固定 $w\in W$ 的实际负图来源。
