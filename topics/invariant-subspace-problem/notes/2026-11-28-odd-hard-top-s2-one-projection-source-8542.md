# 奇数硬端 S2：同一物理来源的一次完整核投影与平方预算

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127 / stable_kernel_return。

**状态：§§1–4 的来源恒等式与条件蕴含已证明。五位或一般 S2 的正性不在本条中宣称。** 本条为新的五位精确输入给出纸面推导，并保留其一般奇数硬端的准确范围。原大有理展开曾在形成费用前超时，不能据此作数学失败结论。

## 1. 原对象、完整最小逆及硬端

令 $M=2s+1$，$s\ge1$，取全部独立正权
$$
d=\sum_{i=1}^{M}a_iE_i,\qquad
K=\ker d|\mathcal H_s,\qquad L=\ker d|\mathcal H_{s-1}.
$$
记
$$
R=d:\mathcal H_s\to\mathcal H_{s-1},\qquad
d_+=d:\mathcal H_{s+1}\to\mathcal H_s,\qquad
R_2=d^2/2:\mathcal H_{s+1}\to\mathcal H_{s-1}.
$$
这些是完整物理层之间的原行；$Rd_+=2R_2$。有限正权 incidence 满秩给 $d_+$ 可逆、$R_2$ 满射。所以
$$
F_2=R_2R_2^*>0,\qquad
P=I-R_2^*F_2^{-1}R_2
\tag{1.1}
$$
是 $\mathcal H_{s+1}$ 上到 $\ker R_2$ 的完整物理正交投影，没有先压缩该逆。

上源的合法最高高度是一。记
$$
J_1=\mathcal J_{1,s}=d_+^{-1}|_K,\quad
G_u=J_1^*J_1,\quad C_u=G_u^{-1}.
$$
下源的合法高度为零至三，记
$$
J_2=\mathcal J_{2,s-1}=R_2^*F_2^{-1}|_L,\qquad
L_j=\mathcal J_{j,s-1}^*\mathcal J_{j,s-1}\quad(j=1,2,3).
$$
这些 Gram 的源与伴随均使用原物理内积。

令完整三次下降及倒数权上升为
$$
C=\sum_i a_i^3E_i:\mathcal H_s\to\mathcal H_{s-1},
\qquad
e=\sum_i a_i^{-1}E_i^*:\mathcal H_{s-1}\to\mathcal H_s.
$$
实际 primitive 桥为 $B=C|_K:K\to L$，倒数权下降桥为 $E_d=e^*|_K:K\to L$。两者取值于 $L$，因为相应下降均与 $d$ 交换。因此
$$
B^*=P_K C^*|_L,\qquad E_d^*=P_K e|_L.
\tag{1.2}
$$

## 2. 从已付 Ward 式得到同一个完整来源

采用 [R275 §4](../results/R275-appendix-first-edge-three-block-equivalence-and-parameter-free-sos.md) 的原定义
$$
\Delta=\tfrac12(C_uB^*L_3-B^*L_2),\qquad
A=\tfrac12(C_uB^*L_2+B^*L_2L_3^{-1}L_2).
$$
[R297 的奇数硬端 Ward 式](../results/R297-appendix-odd-hard-top-innovation-and-dual-lowering-cancellation.md)给
$$
\Delta^*G_u=-L_1E_d,\qquad
\Delta=-C_uE_d^*L_1.
\tag{2.1}
$$
将其用于准确的 $A=C_uB^*L_2-\Delta L_3^{-1}L_2$，得到
$$
\boxed{A=C_u(B^*+E_d^*L_1L_3^{-1})L_2.}
\tag{2.2}
$$
定义完整、同一个下源上的映射
$$
F=C^*|_L+e|_L L_1L_3^{-1}:L\to\mathcal H_s,
\qquad
V=d_+^*F L_2:L\to\mathcal H_{s+1}.
\tag{2.3}
$$
全部 $C_u$ 均按零延拓到 $K^\perp$ 读取，则 (1.2) 给 $A=C_uF L_2$。这里没有在两项中选择不同来源。

## 3. 一次完整核投影的准确身份

因为 $d_+$ 可逆且 $R_2=\tfrac12 Rd_+$，
$$
\operatorname{Ran}J_1=d_+^{-1}K=\ker R_2.
\tag{3.1}
$$
$J_1$ 单射，故这个范围的正交投影为
$$
P=J_1C_uJ_1^*.
$$
另一方面，
$$
J_1^*d_+^*=(d_+J_1)^*=P_K
$$
是完整 $\mathcal H_s$ 到 $K$ 的原正交投影。将其代入 (2.3)，得到
$$
\boxed{J_1A=PV.}
\tag{3.2}
$$
所以真正的上来源费用准确为
$$
\boxed{
K_A:=A^*G_uA
=V^*PV
=V^*V-(R_2V)^*F_2^{-1}(R_2V).
}
\tag{3.3}
$$
这保留同一物理来源中的全部交叉项；最后的负平方来自完整 Moore–Penrose 投影，不能丢掉。

也可独立用完整 $F_{\rm mid}=d_+d_+^*>0$ 的实际 Schur 短接核对：
$$
\widetilde C_u
=F_{\rm mid}
-F_{\rm mid}R^*(R F_{\rm mid}R^*)^{-1}R F_{\rm mid},
\quad R F_{\rm mid}R^*=4F_2.
$$
把该式夹在 $L_2F^*$ 与 $FL_2$ 之间，两个真实因子二与分母四相消，恰得 (3.3)。

完整 S2 的两座原正交塔映射还可写为
$$
\begin{aligned}
\mathcal T
&=J_1A+J_2L_2^{-1}L_1\\
&=\boxed{V+R_2^*F_2^{-1}(L_2^{-1}L_1-R_2V)}.
\end{aligned}
\tag{3.4}
$$
它是把同一 $Vy$ 投到仿射约束 $R_2z=L_2^{-1}L_1y$ 后的原最小修正。由两个正交范围，
$$
\boxed{
\|\mathcal Ty\|^2
=\|Vy\|^2-\|F_2^{-1/2}R_2Vy\|^2
+\langle L_1L_2^{-1}L_1y,y\rangle.
}
\tag{3.5}
$$
这些式子只在上述奇数硬端给出；一般较长上塔的 $\ker R_2$ 还可能含别的 primitive 分量，不能据此省去它们。

## 4. 五位的真实平方预算接口

现在取 $M=5,s=2$，于是 $\dim K=5,\dim L=4$。新[四、五位出生一二分之一界](../results/R271-appendix-four-five-sites-birth-one-half-first-last-edges.md)在这个同一低源给
$$
L_1L_2^{-1}L_1\prec\tfrac12 I_L.
\tag{4.1}
$$
因为 $K_A=V^*PV\succeq0$，有限维物理谱满足
$$
\|K_A\|^2\le\operatorname{Tr}_L(K_A^2).
$$
因此以下是一个准确的充分接口：
$$
\boxed{
\operatorname{Tr}_L(K_A^2)\le\tfrac14
\quad\Longrightarrow\quad
K_A+L_1L_2^{-1}L_1\prec I_L.
}
\tag{4.2}
$$
右端就是原 S2；这里只用了同一个低源的正费用，未改用别的范数或来源。更强的 $3/16$ 平方迹上界若成立，可进一步给统一正余量，但此处不声称它已付。

相反，不能用 $2\operatorname{Tr}K_A<1$ 代替 (4.2)。在真实 $a=(\sqrt t,1,1,1,1)$ 家族的三维标准部分，直接链计算给
$$
L_1=\frac1{t+2},\quad L_2=\frac1{2t+1},\quad L_3=\frac1t,\quad
G_u=\frac{2t+1}{t+2},\quad B^*B=\frac{2t(t-1)^2}{t+2}.
$$
这里可在四个等权位的单位 $v\in K_1(1,1,1,1)$ 上直接复原全部列：旧二孔标准块的正交基为
$
A_v=d_{\rm pool}^*v/\sqrt2,\qquad B_v=e_{\rm head}\otimes v,
$
上 primitive 单位向量为 $(\sqrt t\,A_v-\sqrt2\,B_v)/\sqrt{t+2}$。原下降分别给 $\sqrt2\,v,\sqrt t\,v$；倒数权上升在该 primitive 上的平方范数为 $(2t+1)/(t+2)$，三次桥平方范数为上列数值。低源前三个完整行的平方范数依次为 $t+2,2t+1,t$，故得到所列 $L_j$。四位池的 $K_1$ 有三维，完整低源另有一维组置换平凡部分；上源没有这种平凡表示，所以在该剩余方向 $A=0$。每个标准方向的费用为
$$
k(t)=\frac{2t(t^2-1)^2}{(t+2)^2(2t+1)^3}\longrightarrow\frac14.
$$
所以 $\operatorname{Tr}K_A=3k(t)\to3/4$，而
$\operatorname{Tr}(K_A^2)=3k(t)^2\to3/16$。这个同源极限解释了为什么必须保留矩阵预算或平方迹，不能改成不成立的一次迹门。

## 5. 五点坐标与新精确输入的对应

在原 $p$ 孔层使用 $v_I=a_Iu_I$ 坐标，物理度量为 $\operatorname{diag}(z_I)$，$z_i=a_i^2$。因此对于 $I=\{i,j\}$，
$$
e_{I,i}=1/z_j,\qquad (e^*)_{i,I}=1,
$$
而 $d_+^*$ 与 $R_2^*$ 的坐标均为相应包含 incidence。它们的普通欧氏转置不代替物理伴随。

五点 $L_3^{-1}$ 的完整零延拓使用 [R298 §4](../results/R298-five-independent-positive-weights-birth-two-hard-top-strengthened-s1.md) 的已付式。记 $\pi=\prod_i z_i$，则
$$
L_3^{-1}=K/e_4,\qquad
K_{ii}=\frac{\pi}{z_i}e_3(z_{\widehat i}),\qquad
K_{ij}=-\frac{\pi^2}{z_i^2z_j}\quad(i\ne j).
$$
新输入直接构造
$$
V=d_+^*(C^*+eL_1L_3^{-1})L_2,\qquad
V^*=L_2(C+L_3^{-1}L_1e^*)d_+,
$$
按 (3.3) 计算同一 $K_A$。分母只按明确的正因子
$2,3,z_i,S,e_4,\delta,\epsilon$ 作准确整除，其中
$$
\delta=S^2e_3-4Se_4+12\pi,\qquad
\epsilon=e_4^2e_2-4Se_4\pi+12\pi^2.
$$
后两者分别来自完整五点首 Gram 行列式 $4\delta$ 与二阶 Gram 行列式 $9\epsilon$。因子消约只减去确实整除全部分子的因子，未假定其他因子不存在。

[新精确输入](2026-11-28-five-bit-s2-ward-factored-cost-square-8542.py)的最终系数检查针对 (4.2)，并将所有负系数保留；只有实际报告 CERTIFIED 才能把它接到 S2。本文不把该输入已写成或数值方向核对，当作平方迹已证明。一般出生、普通 Hilbert ISP 及原稳定核的同一 $w$ 费用均仍须继续。
