# R288 附录：一般出生 S1 的真实三塔展开与完整 Schur 消元

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / literature_audit。

**状态：以下恒等式已证明；一般出生 S1 的正性尚未证明。** 本稿把实际二次 creation 的三个出生塔全部保留，消去 S1 中上出生第二精度与第三阶完整逆。新增正项准确来自连续两次三次桥 $C^2$，不能省略，也不把它单独视为一般正性的证明。出生一时该项为零，身份准确退化到[已证对角减秩一式](R288-appendix-birth-one-s1-diagonal-reduction-and-degree-nine-integer-certificate.md)。

## 1. 物理层、归一约定与合法范围

取任意有限正权
$$
d=\sum_{i=1}^M b_iE_i,\quad S=\sum_i b_i^2,\quad
C=\sum_i b_i^3E_i,\quad H=[d,d^*].
$$
不要求 $S=1$。固定 $s\ge1$、$M\ge2s+1$，令
$$
K=K_s=\ker d\cap\mathcal H_s,\qquad
L=K_{s-1},\qquad K_-=K_{s-2}.
$$
$s=1$ 时约定 $K_-=0$，所有涉及它的映射为零。

完整归一最小逆是
$$
\mathcal J_{j,r}=(d^j/j!)^\dagger|_{K_r},\qquad
\Gamma_{j,r}=\mathcal J_{j,r}^*\mathcal J_{j,r}.
$$
记 $G_j=\Gamma_{j,s}$、$L_j=\Gamma_{j,s-1}$，并置
$$
C_1=G_1^{-1},\qquad
C_2=G_2^{-1}\quad\text{若 }M\ge2s+2.
$$
若 $M=2s+1$，旧上出生只有一阶，按照真正硬顶取 $C_2=0$，不构造不存在的 $\mathcal J_{2,s}$。

本稿所需下出生第三阶始终合法；当 $s\ge2$ 时，$K_-$ 的第四阶亦始终合法。定义
$$
B=C|_K:K\to L,\qquad
B_-=C|_L:L\to K_-,\qquad
Y=B_-B=C^2|_K:K\to K_-.
\tag{1.1}
$$
这些是真正受限算子，因为 $[d,C]=0$。记
$$
M_2=B^*L_2B,\qquad
N=B^*L_2L_3^{-1}L_2B,\qquad
H_0=P_KH|_K=C_1+M_2,
$$
$$
P_4=Y^*\Gamma_{4,s-2}Y.
\tag{1.2}
$$
其中 $P_4=0$ 若 $s=1$。目标 S1 缺陷为
$$
\mathcal E_{\mathrm{S1}}=C_1^2-C_2-\Delta L_3^{-1}\Delta^*,
\qquad
\Delta=\frac12(C_1B^*L_3-B^*L_2).
\tag{1.3}
$$

## 2. 二次 creation 的完整三个正交塔

使用 R275 [真实两带与联合占据身份](R275-appendix-joint-occupation-blocks-and-first-edge-necessary-bound.md)，得到
$$
d^*|_K=\mathcal J_{1,s}C_1-\mathcal J_{2,s-1}B,
$$
$$
d^*\mathcal J_{1,s}
=2\mathcal J_{2,s}C_2G_1-\mathcal J_{3,s-1}B,
$$
$$
d^*\mathcal J_{2,s-1}
=3\mathcal J_{3,s-1}L_3^{-1}L_2-\mathcal J_{4,s-2}B_-.
\tag{2.1}
$$
顶硬端第二式首项为零。将第一式再作用一次 $d^*$，使用 $G_1C_1=I$，得到
$$
\boxed{
\frac{(d^*)^2}{2}\bigg|_K
=\mathcal J_{2,s}C_2
-\frac12\mathcal J_{3,s-1}
\bigl(BC_1+3L_3^{-1}L_2B\bigr)
+\frac12\mathcal J_{4,s-2}Y.
}
\tag{2.2}
$$
三项分别在同一物理层 $\mathcal H_{s+2}$ 的
$$
\ker d^3\ominus\ker d^2,\qquad
\ker d^4\ominus\ker d^3,\qquad
\ker d^5\ominus\ker d^4
$$
中，因此严格正交。这里核与正交补均取在这个实际物理层；不是按任意代数 Jordan 坐标声明正交。

令完整二阶物理 Gram 为
$$
F_2^{(s)}=\frac{d^2(d^*)^2}{4}\bigg|_{\mathcal H_s},
\qquad A_2=\frac{d^2}{2}.
$$
对 (2.2) 取 Gram，得到
$$
\boxed{
P_KF_2^{(s)}|_K
=C_2
+\frac14\bigl(BC_1+3L_3^{-1}L_2B\bigr)^*
L_3\bigl(BC_1+3L_3^{-1}L_2B\bigr)
+\frac14P_4.
}
\tag{2.3}
$$
此式在 $C_2=0$ 的硬顶亦成立。

## 3. 同一身份的完整 F3 Schur 来源

为避免把非primitive Schur 源误压缩，下面独立写出完整逆的顺序。令
$$
A_3=\frac{d^3}{6}:\mathcal H_{s+2}\to\mathcal H_{s-1},
\qquad
F_3^{(s-1)}=A_3A_3^*.
$$
由于 $M\ge2s+1$，这是所列完整物理层上的正可逆 Gram。先取这个完整逆，再在需要处限制到 $L$；特别
$L_3=P_L(F_3^{(s-1)})^{-1}|_L$。

定义实际 Schur 源
$$
\boxed{
V=-\frac13dF_2^{(s)}|_K=-A_3A_2^*|_K.
}
\tag{3.1}
$$
一般 $V$ **不是 primitive**。由 $\operatorname{ad}_d^3(d^*)=0$、
$\operatorname{ad}_d^2(d^*)=-2C$，Leibniz 展开给
$$
\operatorname{ad}_d^4((d^*)^2)=24C^2.
$$
对 $df=0$ 使用此式，得到
$$
dV=-2Y,\qquad d^2V=0.
\tag{3.2}
$$

完整最小原像准确为
$$
A_3^\dagger V
=-P_{(\ker A_3)^\perp}A_2^*|_K.
\tag{3.3}
$$
使用 (2.2)，这给
$$
\boxed{
A_3^\dagger V
=\frac12\mathcal J_{3,s-1}
\bigl(BC_1+3L_3^{-1}L_2B\bigr)
-\frac12\mathcal J_{4,s-2}Y.
}
\tag{3.4}
$$
所以真实完整逆确实落在
$\ker d^5\ominus\ker d^3$，由两个正交塔组成；其第二个系数 $-Y/2$ 也可直接由
$d^4A_3^\dagger V=6dV=-12Y$ 核验。

第一塔系数可在不把 $V$ 当成 $L$ 源的前提下核验：
$$
P_L(F_3^{(s-1)})^{-1}V
=-\frac12\mathcal J_{3,s-1}^*(d^*)^2|_K
=\frac12(L_3BC_1+3L_2B).
\tag{3.5}
$$
左乘 $L_3^{-1}$ 才得到 (3.4) 的第一塔系数。

实际完整 Schur 关系是
$$
dF_2^{(s)}d^*=9F_3^{(s-1)},
$$
$$
\boxed{
C_2=P_KF_2^{(s)}|_K
-V^*(F_3^{(s-1)})^{-1}V.
}
\tag{3.6}
$$
在通常合法高度，它是完整 $F_2^{(s)}$ 相对 $K\oplus\operatorname{Ran}d^*$ 的 Schur 补；在 $M=2s+1$ 时，同一 Schur 补为零。对 (3.4) 取 Gram，(3.6) 正好回到 (2.3)。整个过程没有把 $(F_3^{(s-1)})^{-1}$ 换成对 primitive 压缩后的逆。

## 4. 一般 S1 的准确消元结果

展开 (2.3) 得
$$
P_KF_2^{(s)}|_K
=C_2+\frac14C_1B^*L_3BC_1
+\frac34(C_1M_2+M_2C_1)
+\frac94N+\frac14P_4.
\tag{4.1}
$$
另一方面，创新的真实费用为
$$
\Delta L_3^{-1}\Delta^*
=\frac14C_1B^*L_3BC_1
-\frac14(C_1M_2+M_2C_1)+\frac14N.
$$
相减并利用 $C_1+M_2=H_0$，得到本稿主要身份：
$$
\boxed{
\mathcal E_{\mathrm{S1}}
=H_0^2-P_KF_2^{(s)}|_K-M_2^2+2N+\frac14P_4.
}
\tag{4.2}
$$
其中出现的平方仍是同一个物理 Hilbert 源上的算子平方。$P_KF_2^{(s)}|_K$ 是完整物理 Gram 的压缩，不是上出生最小逆 Gram 的逆。

式 (4.2) 去掉了上出生第二精度 $C_2$ 和完整第三阶逆；下出生的 $L_3^{-1}$ 仅留在 $N$ 中。第四阶正项为真正连续两次三次桥的费用，不能当作任意源上的第四阶逆界。

## 5. 占据写法与逐物理位结构

若希望直接计算完整物理项，令
$$
W_2=\sum_i b_i^2n_i,\qquad
W_4=\sum_i b_i^4n_i,\qquad m_2=\sum_i b_i^4,
\qquad Z=e_2(b_i^2)=\frac{S^2-m_2}{2}.
$$
则 $H=SI-2W_2$、$[C,d^*]=m_2I-2W_4$。由
$$
\operatorname{ad}_d^2((d^*)^2)=2H^2-2(Cd^*+d^*C),
$$
且 $P_Kd^*C|_K=0$，得到
$$
\boxed{
P_KF_2^{(s)}|_K
=\frac12P_KH^2|_K-\frac{m_2}{2}I_K+P_KW_4|_K.
}
\tag{5.1}
$$
又真实占据分解给
$$
P_KW_2^2|_K=(P_KW_2|_K)^2+B^*L_1B.
$$
因此 (4.2) 也可以写成
$$
\begin{aligned}
\mathcal E_{\mathrm{S1}}={}&
P_K\bigl((S-W_2)^2-Z+W_2^2-W_4\bigr)|_K
-4B^*L_1B\\
&-M_2^2+2N+\frac14P_4.
\end{aligned}
\tag{5.2}
$$
这里 $W_2^2-W_4=2\sum_{i<j}b_i^2b_j^2n_in_j\succeq0$ 是实际多孔占据项；但其他项尚未获得一般正的重排，所以不能单凭这一项宣布 (S1)。

## 6. 任意共同非正交源坐标的可直接计算形式

设 $E:U\to K$、$E_-:U_-\to L$ 为任意固定的线性同构源坐标，记
$$
U_0=E^*E,\quad \widehat H=E^*HE,\quad
\widehat F_2=E^*F_2^{(s)}E.
$$
令下出生完整 Gram 形式为
$\widehat L_j=E_-^*\Gamma_{j,s-1}E_-$，真实三次桥坐标满足
$BE=E_-K_B$。
进一步选择 $E_{--}:U_{--}\to K_-$ 并令
$YE=E_{--}K_Y$、$\widehat L_4^-=E_{--}^*\Gamma_{4,s-2}E_{--}$。

则 (4.2) 在同一原范数中的二次型准确为
$$
\boxed{
\begin{aligned}
E^*\mathcal E_{\mathrm{S1}}E={}&
\widehat H U_0^{-1}\widehat H-\widehat F_2\\
&-(K_B^*\widehat L_2K_B)U_0^{-1}(K_B^*\widehat L_2K_B)\\
&+2K_B^*\widehat L_2\widehat L_3^{-1}\widehat L_2K_B
+\frac14K_Y^*\widehat L_4^-K_Y.
\end{aligned}
}
\tag{6.1}
$$
每个 $U_0^{-1}$ 都保留；下出生源 Gram 在正确伴随次序中抵消，未假定 $E_-$ 等距。若先作群固定部分等完整约化，应先把所有空间及算子同时限制到该共同约化部分，再选择上述同构；不能把任意非约化试源子空间的压缩当作该公式。这是有限群约化后可直接使用的形式，尤其不再需要上出生 $G_2$ 的完整逆。

## 7. 已付范围与未付部分

当 $s=1$ 时，$Y=0$，(5.2) 与真空 $L_j=e_j(b_i^2)^{-1}$ 准确化成已证的对角减秩一身份，相关完整支持证书已单列。对一般出生，本稿只证明这些实际恒等式及其完整逆来源；$N$、$M_2^2$ 与其他占据项的共同符号仍须控制。

旧下出生第二边只给 $N\preceq B^*L_1B$。在 (4.2) 中 $N$ 带正号，把它换成这个较大的上界不能证明所需下界。本稿也没有把 $P_4$ 的已知源费用推广到任意源，或把上出生普通首边误当作足以支付三次桥创新。
