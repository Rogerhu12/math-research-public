# R271 附录：方差向下薄窗口的缺陷序、同 actual-u 相干运输及原强极限

日期：2026-11-16（UTC）。作者：Astra-ISP-789f / root、boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：已证明。** 在原 N/Y 头及原尾 $D_m$ 不变的条件下，本文允许相干源参数从 $S_m$ 向下变化到 $S_me^{-c/m}$，其中 $c$ 是任意固定非负常数。完整逆的变化由原逆的幂等缺陷 $X_m-X_m^2$ 支付；同一个原 $V_{m,q}/K_{m,q}$ 测试来源保持不变，新的 forcing 缺陷只增加一个明确的 $c$ 常数和超快头幂尾。

这不是把物理尾换成另一条尾，也不将小残量当真核距离。固定比例的方差下降 $s/S_m<1$、完整终端条件及原 carry/返回 Schur 仍未由本文支付。

依据：
- [低物理孔借位四次幂](R271-appendix-low-physical-hole-borrow-powers-and-complete-gram-compression.md) §§1--3；
- [扩大方差及同源相干矩](R271-appendix-enlarged-variance-inverse-grams-and-same-source-damped-coherent-moments.md)，提供原共同嵌入的 $H_m(S_m)^{-1}\to P_M$ 及同源投影框架；
- [直接 actual-u 的完整 Gram](R271-appendix-direct-actual-low-hole-chebyshev-kernel-approximation.md) §1，提供本稿使用的原 $V_{m,q},K_{m,q}$ 定义。

## 1. 原头、完整逆及窗口

令 $m\ge10$、$d=2^m$，$A_m$ 是原 N/Y 有限头，$D_m=\sum_{i\ge m}(i+1)^{-2}E_i$ 是原无限纯尾。置
$$
S=S_m=\sum_{i\ge m}(i+1)^{-4},\qquad
\frac1{3(m+1)^3}\le S\le\frac1{3m^3},
$$
$$
H(t)=\sum_{j=0}^{d-1}\frac{(A_m^*)^jA_m^j}{t^j j!}\succeq I,
\qquad X=H(S)^{-1},\quad Y=H(s)^{-1}.
\tag{1.1}
$$
这里始终先取完整 $d$ 维头 Gram 的逆，没有先删去高头或中间 nuisance。

固定 $c\ge0$，假设
$$
m^4\ge2c,\qquad Se^{-c/m}\le s\le S.
\tag{1.2}
$$
为简化记号，令
$$
L=e^{2c},\qquad \gamma=\frac{770}{256}>3,\qquad
\tau_m=2e^{-\gamma m^4}.
\tag{1.3}
$$
本文全部有限 $m$ 估计对原完整头上的任意 $g$ 同时成立；后文强极限另明确要求固定物理测试。

## 2. 同时支付两个最低方差的高幂尾

借位稿的输入投影取全部 $m$ 个物理头孔，直接给
$$
\|A_m^j\|\le6^j e^{-\gamma(j-m)_+^4}.
\tag{2.1}
$$
因此对任意
$$
t\ge Se^{-2c/m},
$$
有
$$
\boxed{
\left\|\sum_{j>2m}^{d-1}
\frac{(A_m^*)^jA_m^j}{t^j j!}\right\|
\le\tau_m.
}
\tag{2.2}
$$
证明：设 $j>2m$。由 $j-m\ge j/2$，
$$
\frac{\|A_m^j\|^2}{t^j j!}
\le
\exp\!\left[
j\{\log108+3\log(m+1)+2c/m\}
-\frac{\gamma j^4}{8}
\right].
$$
$m\ge10$ 时 $\log108+3\log(m+1)\le m^3/2$，(1.2) 给 $2c/m\le m^3$。所以花括号不超过 $3m^3/2$，而
$$
\frac{3m^3}{2}\le\frac{\gamma j^3}{16}.
$$
故该项不超过 $e^{-\gamma j^4/16}$。相邻项比小于 $1/2$，求和得
$$
\sum_{j>2m}e^{-\gamma j^4/16}
\le2e^{-\gamma(2m+1)^4/16}
\le2e^{-\gamma m^4}.
$$
若有限和为空，结论直接成立。

特别 (2.2) 同时适用于 $t=s$ 和 $t=s^2/S$；后一个最低方差是物理相干 Gram 真正需要的参数，不能只支付 $H(s)$ 就省掉它。

## 3. 完整逆的幂等缺陷序

记 $B=H(s)-H(S)\succeq0$。在 $1\le j\le2m$，
$$
(S/s)^j-1\le L-1.
$$
高幂部分用 (2.2)，得到完整的算子序
$$
B\preceq(L-1)(H(S)-I)+\tau_m I.
\tag{3.1}
$$
因 $H(s)=H(S)+B$，真正非交换 resolvent 身份给
$$
X-Y
=
X^{1/2}\!\left[
I-(I+X^{1/2}BX^{1/2})^{-1}
\right]X^{1/2}.
$$
对正算子 $T$ 有 $0\preceq I-(I+T)^{-1}\preceq T$，所以
$$
0\preceq X-Y\preceq XBX.
$$
将 (3.1) 作同源合同，注意 $X(H(S)-I)X=X-X^2$，遂得
$$
\boxed{
0\preceq X-Y
\preceq(L-1)(X-X^2)+\tau_m I.
}
\tag{3.2}
$$
全部逆和乘积的次序均保留。没有使用一般不成立的逆平方单调性。

对任意 $g$，写
$$
q=\langle Xg,g\rangle,\quad a=Xg,\quad
\epsilon=q-\|a\|^2=\langle(X-X^2)g,g\rangle,
$$
$$
q_s=\langle Yg,g\rangle,\quad a_s=Yg,\quad
\epsilon_s=q_s-\|a_s\|^2.
$$
则
$$
\boxed{0\le q-q_s\le(L-1)\epsilon+\tau_m\|g\|^2.}
\tag{3.3}
$$
又 $0\preceq X,Y\preceq I$，且
$$
\epsilon\le\|g\|^2-q,\qquad
\epsilon_s\le\|g\|^2-q_s;
\tag{3.4}
$$
例如第一式的差正是 $\|g-Xg\|^2\ge0$。

## 4. 同一原 V/K 来源，不移动物理尾

令
$$
\omega_j=(D_m^*)^j\Omega,\qquad
\sigma_j^2=\|\omega_j\|^2=(j!)^2e_j((i+1)^{-4}:i\ge m).
$$
准确有
$$
\sigma_j^2\le j!S^j.
\tag{4.1}
$$
定义有限相干行
$$
R_s a=\sum_{j=0}^{d-1}
\frac{(-A_m)^ja\otimes\omega_j}{s^j j!},
\qquad F_s=R_sYg.
\tag{4.2}
$$
即使 $s<S$，这也是原物理 Hilbert 空间中的有界有限列；每个 $\omega_j$ 都在整个无限尾的真实 $j$ 孔层中。

取任意原 cut 整数 $q_{\rm cut}\ge d-1$，用
$$
V=\{v:\Pi_{\le q_{\rm cut}}v=v,\
\Pi_{<q_{\rm cut}}(A_m+D_m)v=0\},
$$
$$
K=\{v:\Pi_{\le q_{\rm cut}}v=v,\
(A_m+D_m)v=0\},\qquad
u_g=(P_V-P_K)i_0g.
\tag{4.3}
$$
$i_0$ 只张量原尾真空。对 $v\in V$，原低行给
$$
D_m^j v_j=(-A_m)^jv_0
\qquad(0\le j\le d-1).
$$
因此
$$
R_s^*v=H(s)i_0^*v,\qquad
P_VR_s=P_Vi_0H(s).
$$
同式在 $K\subset V$ 上也成立。所以准确有
$$
\boxed{
P_VF_s=P_Vi_0g,\qquad
P_KF_s=P_Ki_0g,\qquad
(P_V-P_K)F_s=u_g.
}
\tag{4.4}
$$
没有重选实际来源，也没有用 MP 交换代替投影恒等式。

各 $j$ 孔层正交，(4.1) 给完整物理 Gram 的正确上界
$$
R_s^*R_s
=
\sum_{j<d}
\frac{\sigma_j^2(A_m^*)^jA_m^j}{s^{2j}(j!)^2}
\preceq H(s^2/S).
\tag{4.5}
$$
对 $H(s^2/S)-H(s)$ 再作 (2.2) 的低/高段拆分，得到
$$
R_s^*R_s
\preceq H(s)+(L-1)(H(s)-I)+\tau_m I.
\tag{4.6}
$$
这保留了 $r=S/s>1$ 时的真实物理费用。

## 5. 同 actual-u 的完整缺陷常数

记原 forcing 缺陷
$$
\Delta_g^2=\|g\|^2-\|u_g\|^2\ge0.
$$
先在基准 $s=S$ 用 (4.4)--(4.5)，有
$$
\|u_g\|^2\le\|R_SXg\|^2\le q.
$$
结合 (3.4)，
$$
\epsilon\le\|g\|^2-q\le\Delta_g^2.
\tag{5.1}
$$
于是 (3.3) 给
$$
\|g\|^2-q_s\le L\Delta_g^2+\tau_m\|g\|^2,
\qquad
\epsilon_s\le L\Delta_g^2+\tau_m\|g\|^2.
\tag{5.2}
$$

由 (4.6)，
$$
\|F_s\|^2
\le q_s+(L-1)\epsilon_s+\tau_m\|g\|^2.
$$
(4.4) 说明 $u_g$ 是 $F_s$ 到同一个闭子空间 $V\cap K^\perp$ 的正交投影。因此
$$
\|F_s-u_g\|^2=\|F_s\|^2-\|u_g\|^2.
$$
再用 $q_s\le q\le\|g\|^2$ 和 (5.2)，得到
$$
\boxed{
\|F_s-u_g\|^2
\le
(L^2-L+1)\Delta_g^2
+L\tau_m\|g\|^2,
\qquad L=e^{2c}.
}
\tag{5.3}
$$
这是整个 moving 头上的统一同源估计。其常数依赖固定 $c$，不依赖 $m$、$q_{\rm cut}$、头维数或远尾位置截断。

此外，零孔行就是 $a_s$，故 (4.6) 也给
$$
\boxed{
\|F_s-i_0a_s\|^2
\le L\epsilon_s+\tau_m\|g\|^2.
}
\tag{5.4}
$$

## 6. 原强极限及其准确范围

将有限头逆按原物理头嵌入同一个 Hilbert 空间，已付
$$
X_m=H_m(S_m)^{-1}\longrightarrow P_M
$$
强收敛。因 $P_M$ 是正交投影，$X_m-X_m^2\to0$ 也强收敛。(3.2) 及一致有界性于是给
$$
\boxed{
H_m(s_m)^{-1}\longrightarrow P_M
\quad\text{当 }S_me^{-c/m}\le s_m\le S_m,\ c\text{ 固定}.
}
\tag{6.1}
$$
例如对差算子 $A_m=X_m-Y_m$，$0\preceq A_m\preceq I$，故
$\|A_m f\|^2\le\langle A_mf,f\rangle$；右端由 (3.2) 趋零。没有从环境逆的上界免费推出受限逆下界。

对固定有限物理测试 $g$，从而
$$
a_{s_m}\to P_Mg,\quad q_{s_m}\to\|P_Mg\|^2,\quad
\epsilon_{s_m}\to0.
$$
再用 (5.4)，得到同一原物理向量族
$$
\boxed{F_{s_m}\longrightarrow P_Mg\quad\text{强收敛}.}
\tag{6.2}
$$
这里的相干列仍用 $D_m^*$，不是另一条尾的创建算子。

一个可直接代入的数值参数是任固定整数 $k\ge0$：
$$
\frac{S_{m+k}}{S_m}
\ge\left(\frac{m}{m+k+1}\right)^3
\ge e^{-3(k+1)/m}.
$$
故 $s_m=S_{m+k}$ 落在 (6.1)，可取 $c=3(k+1)$。这句话只替换 Gram/forcing 的标量参数；若另把物理尾改成 $D_{m+k}$、把中间位置真空，原 (4.4) 必须重新核对，不能由方差数值相同推出。

本稿没有给 $s_m/S_m$ 固定小于 $1$ 的统一常数：那会使 $c$ 随 $m$ 增长，(5.3) 出现未付的 $e^{O(m)}\Delta_g^2$。也没有缩短全相干行的最高高度 $d-1$，没有完成终端 $\ker C^{J+1}$ 的全部最小化，更没有把原 $Q$ 的 carry/同 $w$ 运输窗口扩大。已付的新范围是薄的下降方差窗口及其对原实际来源的明确缺陷支付。
