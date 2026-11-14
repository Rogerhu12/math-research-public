# R271 附录：临界两簇的真实最小逆与二层规范旗退化

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / kernel_continue；AI-assisted，GPT-6 Astra Pro。

状态：**已证明。** 本稿在实际有限正权 Boolean 模型中，给出二层规范短旗本身的明确退化；不是任意输入 creation 像的辅助角度反例。它不声称原规则尾 $a_j=(j+1)^{-2}$ 有同样退化，也不否定真正的相邻三 Gram 系数一。

## 1. 结论

任取整数 $p\ge2$。用 $p$ 个权 $1$ 的位和 $2p$ 个权 $1/\sqrt2$ 的位，组成实际有限删除算子
$$
D=D_{\rm s}+2^{-1/2}D_{\rm w},\qquad
S=\sum_i a_i^2=2p,\qquad
\delta=\frac{\max_i a_i^2}{S}=\frac1{2p}.
\tag{1}
$$
记 $K_r=\ker D\cap\mathcal H_r$，并取完整层的真正 Moore–Penrose 逆
$$
J_1=D^\dagger|_{K_p}:K_p\longrightarrow\mathcal H_{p+1}.
$$
存在下面显式给出的单位 $f_p\in K_p$，使
$$
\boxed{
\|J_1f_p\|^2=
\frac{1+(2p+1)c_p}{p},
\qquad c_p=4^{-p}\binom{2p}{p}.}
\tag{2}
$$

输出最高孔层 $P=p+1$、旗高 $H=2$ 的真正规范映射是
$$
V_{P,2}:K_{p+1}\oplus K_p\longrightarrow
\ker(D^2|_{\mathcal H_{p+1}}),
\qquad
V_{P,2}(k,g)=k+\sqrt S\,J_1g.
\tag{3}
$$
这里正是单位一粒子行 $D/\sqrt S$ 的规范归一化。两个输出项正交，且 (3) 是整个短核上的同构。因此
$$
\boxed{
\|V_{P,2}(0,f_p)\|^2
=2+2(2p+1)c_p.}
\tag{4}
$$
特别 $\|V_{P,2}\|\to\infty$，而
$$
\boxed{\delta HP=1+\frac1p\longrightarrow1.}
\tag{5}
$$
所以不存在仅依赖 $\delta HP$、在 $1$ 附近局部有界的普适规范旗范数上界。尤其不能对全部有限正权和全部出生，将既有的小 $\delta HP$ 定理无条件延伸为
$$
\|V_{P,H}\|\le e^{C\delta HP}
$$
或把右侧换成固定常数倍的同类表达。

## 2. 全部在原内积中的 primitive 源

强、弱组的规范对称孔向量分别记为
$$
e_j=\binom pj^{-1/2}\sum_{|I|=j}e_I,
\qquad
w_k=\binom{2p}k^{-1/2}\sum_{|J|=k}e_J.
$$
这些基在原 Boolean Hilbert 空间中正交归一。删除准确满足
$$
D_{\rm s}e_j=\sqrt{j(p-j+1)}e_{j-1},
\qquad
D_{\rm w}w_k=\sqrt{k(2p-k+1)}w_{k-1}.
\tag{6}
$$
置
$$
Z_p=\sum_{j=0}^p 2^{-j}\binom{p+j}{j},
\qquad
c_j=Z_p^{-1/2}(-2^{-1/2})^j
\sqrt{\binom{p+j}{j}},
$$
$$
f_p=\sum_{j=0}^p c_j e_jw_{p-j}.
\tag{7}
$$
其范数为一。相邻系数满足
$$
\frac{c_{j+1}}{c_j}
=-\frac1{\sqrt2}\sqrt{\frac{p+j+1}{j+1}}.
\tag{8}
$$
将 (8) 代入 (6)，每个 $e_jw_{p-j-1}$ 坐标上的强、弱删除项准确抵消。因此 $Df_p=0$。

所需的有限和有简单的精确形式：
$$
\boxed{Z_p=2^p.}
\tag{9}
$$
例如，将 $2^{-p-1}Z_p$ 解释为公平抛硬币中，第 $p+1$ 次正面出现前至多出现 $p$ 次反面的概率；它也就是 $2p+1$ 次抛掷中正面至少 $p+1$ 次的概率，按正反面对称性恰为 $1/2$。这是有限二项式恒等式，不是概率极限。

## 3. 完整空间内的真正最小原像

定义
$$
v_p=\sum_{j=0}^p
\sqrt2\,c_j\sqrt{\frac{p+1-j}{p+j}}\ e_jw_{p+1-j}.
\tag{10}
$$
全部分母正，因为 $p\ge2$。在 $Dv_p$ 的 $e_jw_{p-j}$ 坐标中，弱删除贡献为
$$
c_j(p+1-j),
$$
强删除由 (8) 给
$$
-c_j(p-j).
$$
两者之和就是 $c_j$；端点按零项解释。因此
$$
Dv_p=f_p.
\tag{11}
$$

还必须证明 (10) 是整个孔层中的最小原像。令 $\mathcal G=S_p\times S_{2p}$ 分别置换两组，平均投影记为 $P_{\mathcal G}$。它与 $D$ 交换，且 $P_{\mathcal G}f_p=f_p$。所以任一完整空间解 $Dz=f_p$ 的平均仍为解，且
$$
\|z\|^2=\|P_{\mathcal G}z\|^2+\|(I-P_{\mathcal G})z\|^2.
$$
在第 $p$、$p+1$ 孔层的组不变部分，维数同为 $p+1$。相应的删除矩阵为双对角矩阵，弱删除的对角元
$$
2^{-1/2}\sqrt{(p+1-j)(p+j)}\qquad(0\le j\le p)
$$
全部非零，故这个完整组不变块上的解唯一。由 (11) 它就是 $v_p$。于是所有解均满足 $\|z\|\ge\|v_p\|$，严格证明
$$
v_p=J_1f_p.
\tag{12}
$$
这里没有先把 $DD^*$ 压到 primitive 线再取逆，也没有使用顺次链代替幂逆。

## 4. 真费用的准确求和

由 (10)，
$$
\|v_p\|^2
=\frac2{Z_p}\sum_{j=0}^p
2^{-j}\binom{p+j}{j}\frac{p+1-j}{p+j}.
\tag{13}
$$
令
$$
A_p=\sum_{j=0}^p2^{-j}\binom{p+j-1}{j},
\qquad
B_p=\sum_{j=0}^p j\,2^{-j}\binom{p+j-1}{j}.
$$
同样的有限二项式尾和给
$$
A_p=2^{p-1}(1+c_p),
\qquad
B_p=p\,2^{p-1}(1-c_p).
\tag{14}
$$
第一式对应 $2p$ 次公平抛掷中至少 $p$ 次正面的概率 $(1+c_p)/2$。对第二式，先用
$$
j\binom{p+j-1}{j}=p\binom{p+j-1}{j-1}
$$
将求和指标降一，再使用同一 $2p$ 次抛掷中至少 $p+1$ 次正面的概率 $(1-c_p)/2$，便得到 (14)。

又因
$$
\frac1{p+j}\binom{p+j}{j}=\frac1p\binom{p+j-1}{j},
$$
(13) 等于
$$
\frac2{pZ_p}\big((p+1)A_p-B_p\big)
=\frac{1+(2p+1)c_p}{p}.
$$
这证明 (2)，继而证明 (4)。

不需要渐近展开即可看出退化。由
$$
\frac{c_{p+1}}{c_p}=\frac{2p+1}{2p+2},\qquad c_0=1,\quad c_1=\frac12,
$$
直接归纳可得
$$
\frac1{2\sqrt p}\le c_p\le\frac1{\sqrt{p+1}}\qquad(p\ge1).
\tag{15}
$$
故这个明确单位输入满足
$$
2\sqrt p
\le\|V_{P,2}(0,f_p)\|^2
\le8\sqrt p.
\tag{16}
$$
即该输入的规范旗放大量准确处在 $p^{1/4}$ 阶；(16) 没有声称给整个规范旗的上界。

## 5. 完整短核、条件数与原问题范围

此处完整层的 $D:\mathcal H_{p+1}\to\mathcal H_p$ 满射：正权删除与等权包含矩阵正对角相似，而 $p+1\le3p-p$ 落在其满射区间。因此 $J_1$ 在整个 $K_p$ 上有定义。

对任意 $x\in\ker D^2\cap\mathcal H_{p+1}$，有 $Dx\in K_p$，而
$$
x-J_1Dx\in K_{p+1}.
$$
真正最小原像属于 $(\ker D|_{\mathcal H_{p+1}})^\perp$，故此分解正交且唯一。这证明 (3) 的完整像和单射性。对于 $p\ge2$，$K_{p+1}\ne0$，所以 (3) 还含一个范数完全不变的非零方向；因此它的条件数同样无界，至少大于等于 (4) 的平方根。

作为同一源的独立校准，交换子
$$
[D,D^*]=S I-2\sum_i a_i^2n_i
$$
与 $Df_p=0$ 给
$$
\|D^*f_p\|^2
=p-\sum_{j=0}^p j|c_j|^2
=(2p+1)c_p-1=O(\sqrt p).
\tag{17}
$$
最后一个有限和也由 (14) 的同类二项式尾和得到。其倒数仅是最小逆费用的下界；真正费用已经由 (10)–(14) 完整支付，未把两者等同。

本族只有两种正权，故 [R239 两权全部高度相邻严格系数一](R239-appendix-two-weight-groups-all-heights-strict-primitive-gram-bound.md)仍适用。没有矛盾：相邻比较限制连续三个真 Gram 的相对变化，本稿揭示的是规范归一化后的绝对费用随出生增长。

原规则尾以及实际边界的窄 Schur 源并未由本族识别。要越过既有短旗窗口，必须使用原规则尾或实际源的额外结构；任意有限正权、仅依赖 $\delta HP$ 的有界规范旗方案已被 (1)–(16) 排除。
