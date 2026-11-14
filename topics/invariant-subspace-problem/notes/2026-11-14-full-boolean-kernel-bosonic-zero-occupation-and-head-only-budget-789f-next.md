# 全出生真实 Boolean 核的集体零占据重构与仅含原头的费用

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / literature_audit；AI-assisted，GPT-6 Astra Pro。

**状态：已证明的中间结论。** 本稿在原平方自由 Hilbert 空间的真正核
\(\ker(A_m+D_m)\) 上，给出完整 bosonic 零占据重构。它同时保留所有物理孔层和所有出生；没有低占据或碰撞小量假设。重构的全部范数费用只含真实有限头的幂。对本课题原慢尾和原 \(N/Y\) 头，这一费用满足
\[
\log C_m=O(m\log(m+1)).
\]
因此，**完整左前缀零源 graph** 的原 Gram 与同一 graph 的零占据 Gram 按这个常数比较。这里的 graph 是环境 \(A_m+D_m\) 的真核；不把未来 bare 商中的压缩删除 \(\delta=P_{\rm lo}D_m\) 当作同一个 bosonic annihilator，也未支付该商的高返回。

本稿的 bosonic 空间、零占据投影与 [R286](../results/R286-fixed-source-l1-zero-mode-energy-and-uniform-all-height-tail-bounds.md) 相同。它给的是原整个 graph 的正预算，不把 R286 的固定出生源结论外推成增长出生的最小逆界。

## 1. 完整空间、实际闭域与集体模式

设 \(\mathcal E\) 为有限维头 Hilbert 空间，
\[
A\in B(\mathcal E),\qquad A^d=0,\qquad d\ge1.
\]
取有限或可数正权行 \(b=(b_i)\in\ell^1\)，并置
\[
S=\sum_i b_i^2>0,\qquad D=\sum_i b_iE_i.
\]
原尾空间 \(\mathcal H_{\rm hc}\) 的标准正交基为有限子集 \(e_I\)；\(E_i\) 删除第 \(i\) 位。因为 \(b\in\ell^1\)，\(D\) 在整个原尾空间有界，\(\|D\|\le\sum_i b_i\)。

令 \(\mathcal F=\Gamma_{\rm s}(\ell^2)\) 为完整 bosonic Fock 空间，其标准占据基 \(e_\alpha\) 满足
\[
a_ie_\alpha=\sqrt{\alpha_i}\,e_{\alpha-\mathbf e_i}.
\]
通过 \(e_I\mapsto e_{1_I}\) 将 \(\mathcal H_{\rm hc}\) 等距嵌入 \(\mathcal F\)。完整集体 annihilator 为
\[
\mathcal B=\sum_i b_i a_i=\sqrt S\,a_0,\qquad
u=b/\sqrt S,\quad a_0=a(u).
\]

在有限平方自由向量上，\(\mathcal B=D\)。对任意原向量 \(v\)，用其有限子集截断 \(v_n\to v\)；有 \(Dv_n\to Dv\)。由 \(\mathcal B\) 的闭性，
\[
\boxed{\mathcal H_{\rm hc}\subseteq\operatorname{Dom}\mathcal B,\qquad
\mathcal B|_{\mathcal H_{\rm hc}}=D.}
\tag{1.1}
\]
所以以下核的包含是在真实闭域中成立：
\[
\mathcal K:=\ker(A+D)
\subseteq\ker(A+\mathcal B).
\tag{1.2}
\]
头上的算子默认张量尾恒等。

按一粒子正交分解 \(\ell^2=\mathbb Cu\oplus u^\perp\)，完整 Fock 空间有酉分解
\[
\mathcal F=\Gamma_{\rm s}(\mathbb Cu)\otimes\Gamma_{\rm s}(u^\perp).
\]
以 \(|j\rangle_0\) 表示第一个因子的标准占据基，令
\[
P_0=|\Omega\rangle_0\langle\Omega|\otimes I
\]
为集体模式的零占据正交投影。它保持完整总孔数，但通常不保持原平方自由子空间。

## 2. 真核的准确重构；全部集体占据至多 \(d-1\)

任意 \(v\in\ker(A+\mathcal B)\) 可唯一写为
\[
v=\sum_{j\ge0}|j\rangle_0\otimes v_j,\qquad
v_j\in\mathcal E\otimes\Gamma_{\rm s}(u^\perp).
\]
闭域条件保证 annihilation 系数逐项合法。核方程准确给
\[
Av_j+\sqrt{S(j+1)}\,v_{j+1}=0\qquad(j\ge0).
\tag{2.1}
\]
因此令 \(h=v_0=P_0v\)，便有
\[
v_j=\frac{(-A)^j h}{\sqrt{j!\,S^j}},
\qquad v_j=0\quad(j\ge d).
\tag{2.2}
\]
特别，**任何真实平方自由核向量的集体模式占据都至多 \(d-1\)**，不依赖其总孔数、出生数或尾位数。

把零占据空间同 \(\mathcal E\otimes\Gamma_{\rm s}(u^\perp)\) 识别，定义
\[
\boxed{
\mathcal R_Ah
=\sum_{j=0}^{d-1}
\frac{(-A)^j(a_0^*)^j h}{S^{j/2}j!}.
}
\tag{2.3}
\]
这里 \((a_0^*)^jh/\sqrt{j!}=|j\rangle_0\otimes h\)，所以 (2.3) 是一个处处有定义的有限和有界算子；没有在整个 Fock 空间上使用无界指数。

由 (2.1) 望远镜直接得到
\[
(A+\mathcal B)\mathcal R_Ah=0,\qquad P_0\mathcal R_Ah=h.
\tag{2.4}
\]
反向由 (2.2)，
\[
\boxed{v=\mathcal R_AP_0v\qquad(v\in\mathcal K).}
\tag{2.5}
\]

## 3. 完整正 Gram 与真实零占据像

不同集体占据 \(j\) 在物理 Fock 范数中正交。因此
\[
\boxed{
\|v\|^2
=\sum_{j=0}^{d-1}\frac{\|A^jP_0v\|^2}{S^j j!}
\qquad(v\in\mathcal K).
}
\tag{3.1}
\]
定义作用在头上的严格正矩阵
\[
\boxed{
\mathsf H_{A,S}
=\sum_{j=0}^{d-1}\frac{(A^j)^*A^j}{S^j j!},
\qquad
C(A,S)=\sum_{j=0}^{d-1}\frac{\|A^j\|^2}{S^j j!}.
}
\tag{3.2}
\]
于是
\[
\mathcal R_A^*\mathcal R_A
=\mathsf H_{A,S}\otimes I,\qquad
I\preceq\mathsf H_{A,S}\preceq C(A,S)I
\]
及
\[
\boxed{
\|P_0v\|^2\le\|v\|^2
\le C(A,S)\|P_0v\|^2.
}
\tag{3.3}
\]

须准确保留零占据像。置
\[
\boxed{
\mathcal Z_A
=\{h\in\mathcal E\otimes\Gamma_{\rm s}(u^\perp):
        \mathcal R_Ah\in\mathcal E\otimes\mathcal H_{\rm hc}\}.
}
\tag{3.4}
\]
这是闭子空间，因为 \(\mathcal R_A\) 有界且原平方自由空间闭。由 (2.4)–(2.5)，
\[
P_0\mathcal K=\mathcal Z_A,\qquad
\mathcal R_A\mathcal Z_A=\mathcal K.
\tag{3.5}
\]
所以 \(P_0:\mathcal K\to\mathcal Z_A\) 是有界同构，逆就是 \(\mathcal R_A|_{\mathcal Z_A}\)，逆范数至多 \(\sqrt{C(A,S)}\)。

本稿**不**将 \(\mathcal Z_A\) 替换为整个横向 Fock 空间，也不将其向量称为原平方自由 primitive 向量。构造一个任意横向 \(h\) 后，\(\mathcal R_Ah\) 未必平方自由；这样的向量不是原问题的可行点。

若限制原核到有限孔前缀 \(\mathcal K_{\le q}=\mathcal K\cap\mathcal H_{\le q}\)，同样以
\[
\mathcal Z_{A,q}=P_0\mathcal K_{\le q}
\]
为其准确闭像；(3.1)–(3.3) 的常数完全不变。

## 4. 原 \(N/Y\) 头的真实四次幂成本

现在取本课题原线性近似
\[
A=A_m,\qquad d=2^m,\qquad
D=D_m=\sum_{j\ge m}(j+1)^{-2}E_j,\qquad m\ge5.
\]
有限头 \(A_m\) 是原 \(T_N\) 或 \(T_Y\) 的前 \(m\) 位限制，保持原头内积和全部 carry；没有换成相似的标准 Jordan 矩阵。

所用真实头幂界来自 [R234 四次头幂附录 §2](../results/R234-appendix-quartic-head-powers-and-super-four-thirds-hole-weights.md)。下面保留其短证明以明确原对象和阈值。实际归一位满足
\[
N_j^2=\eta_jN_{j+1},\qquad
0<\eta_j\le e^{-770\,16^j},\qquad
\|N_j\|\le1,\quad\|(I+N_j)^{-1}\|\le3.
\tag{4.1}
\]
在有限头上，越过第 \(m\) 位的进位项为零。对于含 \(k\) 个 \(N_j\) 因子的单项，全部进位数 \(c_j\) 满足
\[
C_{\rm car}=\sum_jc_j
=k-\operatorname{popcount}\!\left(\sum_jk_j2^j\right).
\]
当 \(k\ge k_0:=\max(2m,16)\) 时，
\[
C_{\rm car}\ge k/4.
\]
置 \(E_{\rm car}=\sum_j16^jc_j\)。进位递推给
\(c_{j+\ell}\ge\lfloor c_j/2^\ell\rfloor\)，从而
\(c_j\le2E_{\rm car}^{1/4}2^{-j}\)，故
\[
C_{\rm car}\le4E_{\rm car}^{1/4},\qquad
E_{\rm car}\ge(k/16)^4.
\]
(4.1) 遂给该单项范数至多 \(e^{-\gamma k^4}\)，其中
\[
\gamma=\frac{770}{16^4}>\frac1{100}.
\]
原慢系数绝对和小于 \(2\)。\(Y\) 型将相互交换的实际 Cayley 逆拉到同一侧，只再付 \(3^k\)。于是两型统一满足
\[
\boxed{
\|A_m^k\|\le6^k\quad(k\ge0),\qquad
\|A_m^k\|\le6^ke^{-\gamma k^4}\quad(k\ge k_0).
}
\tag{4.2}
\]
所有估计均在原物理头上。\(A_m^d=0\) 也保持原准确 nilpotence。

尾平方和为
\[
S_m=\sum_{j\ge m}(j+1)^{-4}
\ge\frac1{3(m+1)^3}.
\tag{4.3}
\]
令
\[
\tau_m=\log(36/S_m)>0,\qquad
T_m=\log108+3\log(m+1),
\]
则 \(\tau_m\le T_m\)。

把 (4.2) 代入 (3.2)，低阶和满足
\[
\sum_{j<k_0}\frac{\|A_m^j\|^2}{S_m^j j!}
\le k_0e^{k_0\tau_m}.
\]
对于高阶项，实变量最大值给
\[
\tau x-\gamma x^4
\le \frac{3}{4^{4/3}\gamma^{1/3}}\tau^{4/3}
\le3\tau^{4/3}\qquad(x,\tau\ge0).
\]
因此
\[
\sum_{j\ge k_0}\frac{e^{\tau_mj-2\gamma j^4}}{j!}
\le e^{3\tau_m^{4/3}}\sum_{j\ge0}\frac{e^{-\gamma j^4}}{j!}
\le e\,e^{3\tau_m^{4/3}}.
\]
可取下面完全显式、与所有孔层无关的预算：
\[
\boxed{
C_m:=C(A_m,S_m)
\le (k_0+e)\exp\!\left(k_0T_m+3T_m^{4/3}\right).
}
\tag{4.4}
\]
特别
\[
\boxed{\log C_m=O(m\log(m+1)).}
\tag{4.5}
\]
沿原 \(m(q)=O(\log\log(q+2))\) 头选择，\(C_{m(q)}=q^{o(1)}\)。这是原真核的零占据重构费用，不是完整两费修复常数。

## 5. 完整左前缀 graph 的同源 Gram 比较

取原归一链基
\[
A_m=V_mJ_dV_m^{-1},\qquad V_m=1\oplus V_{m,+},
\]
并在固定原尾前缀置
\[
\mathcal F_{d,q}=\ker D_m^d\cap\mathcal H_{\le q}.
\]
完整左前缀零源 graph 是
\[
\mathcal T_qf=\sum_{j=0}^{d-1}(V_me_j)(-D_m)^jf,
\qquad f\in\mathcal F_{d,q}.
\tag{5.1}
\]
望远镜给 \((A_m+D_m)\mathcal T_qf=0\)；反向逐头方程给
\[
\operatorname{Ran}\mathcal T_q=\mathcal K_{\le q},\qquad
e_0^*\mathcal T_qf=f.
\]
这是原真实 \(D_m\)，没有未来高出生商。

定义
\[
\Gamma_q=\mathcal T_q^*\mathcal T_q,\qquad
Y_q=P_0\mathcal T_q,\qquad
\Xi_q=Y_q^*Y_q=\mathcal T_q^*P_0\mathcal T_q.
\]
由 (2.5)–(3.2)，得到完整非交换身份
\[
\boxed{
\Gamma_q
=Y_q^*(\mathsf H_{A_m,S_m}\otimes I)Y_q.
}
\tag{5.2}
\]
因 \(\Gamma_q\succeq I\)，(3.3) 给
\[
\boxed{
C_m^{-1}\Gamma_q\preceq\Xi_q\preceq\Gamma_q,\qquad
\Xi_q\succeq C_m^{-1}I.
}
\tag{5.3}
\]
两者在同一个原 first-head 源空间上均可逆，且
\[
\boxed{\Gamma_q^{-1}\preceq\Xi_q^{-1}\preceq C_m\Gamma_q^{-1}.}
\tag{5.4}
\]
这不是把任意压缩逆互换：两次比较使用相同的 \(\mathcal T_q\)、相同源、相同完整 \(P_0\)，最后才取正序逆。

更一般地，给定 \(\mathcal F_{d,q}\) 上同一组线性约束，若其可行集非空，分别以 \(\Gamma_q\) 和 \(\Xi_q\) 的二次型取下确界，则对应最小值也在因子 \(C_m\) 内。该断言只比较同一可行集的同一源，不将实际源自由度或 nuisance 块删掉。

## 6. 与固定源能量及真实图问题的准确接点

R286 中的 \(J^*\mathsf E_pJ\) 是指定最小逆列的零占据 Gram。本稿的 \(\Xi_q\) 则保留**完整原头 graph 的全部列和交叉**。式 (5.2) 表明，若能在同一个 \(\Xi_q\) 上处理实际测试的逆传播或源 Schur，回到原 \(\Gamma_q\) 只需支付 (4.4) 的头费用。这个费用没有增长出生数，也不含整个 Jordan 相似矩阵的条件数。

然而下列两步仍未得到：

1. 实际 \(Z_p^{-1}\) 后的源是否具备可用的 \(\Xi_q\) 同源逆能量预算；固定物理测试不自动成为固定 primitive 出生。
2. R239 左加 bare graph 使用 \(\delta=P_{\rm lo}D_m\)。其核向量可能带有尚未修复的环境高返回，因此不能直接代入 (2.5) 或 (5.2)。必须保留对应的完整环境残量或另行构造真正核提升。

此外 \(P_0\) 通常把原平方自由向量送到含重复占据的横向向量；(3.4) 的实际像约束不可丢弃。普通 ISP、原无权 \(N=M\)、一般相邻 primitive 不等式及完整两费比较均未由本稿完成。
