# 单个真实进位不受纯提升和图范数控制

日期：2026-11-12（UTC）。独占稿：critical_kernel。
状态：**已证明。** 执行器重置后重建；仅排除逐个进位作相对小扰动的简化路线。

设 B=∑_{j≥0}a_jE_j，a∈ℓ¹，作用于 plus 纯乘积 Hilbert 空间。
固定 i≠j、a_i≠0。对 N>max(i,j)，令 u_{N,j} 为物理正交基向量：
前 N 位仅 j 为0、其余为1，后尾为 plus 参考向量。定义

$$
v_N=a_i u_{N,j}-a_j u_{N,i}.
\tag{1}
$$

两基向量正交，故

$$
\|v_N\|=(|a_i|^2+|a_j|^2)^{1/2}>0.
$$

有限头 B_{<N} 满足

$$
B_{<N}u_{N,j}=a_j e_1^{\otimes N}\otimes1_{\ge N},
\qquad
B_{<N}u_{N,i}=a_i e_1^{\otimes N}\otimes1_{\ge N}.
$$

所以 B_{<N}v_N=0，并且

$$
\|Bv_N\|
\le\left(\sum_{k\ge N}|a_k|\right)\|v_N\|
\longrightarrow0.
\tag{2}
$$

但 R=E_i^*E_j 有精确作用

$$
Rv_N=a_i u_{N,i},\qquad \|Rv_N\|=|a_i|.
\tag{3}
$$

因此不存在 K<∞ 使 ∥Rx∥≤K∥Bx∥ 对所有 x 成立。
乘任意固定非零小常数 εR 也不改变这个结论。

对实际单个进位，取 j=i+1，使用

$$
N_i-E_i=\eta_iE_i^*N_{i+1}.
$$

在 u_{N,i+1} 上，第 i+1 位为0，N_{i+1} 的进位项为零，主项
E_{i+1} 精确填入该位，故
E_i* N_{i+1}u_{N,i+1}=u_{N,i}。
在 u_{N,i} 上，第 i 位为0，而 N_{i+1} 不作用该位，所以
E_i* N_{i+1}u_{N,i}=0。因此

$$
\boxed{
(N_i-E_i)v_N=\eta_i a_i u_{N,i},
\qquad
\|(N_i-E_i)v_N\|=\eta_i|a_i|>0.
}
\tag{4}
$$

结合 (2)，不存在 K<∞ 使
∥(N_i−E_i)x∥≤K∥Bx∥ 对全部 x 成立。

v_N 弱趋零，是逃向高物理占据的近核向量；这不与纯 B 单射相矛盾。
此反例只否定逐个 carry 的相对图范数控制，未排除真实总和中的特殊抵消或核上的额外控制。实际小三次型尾及完整 ISP 仍未解决。
