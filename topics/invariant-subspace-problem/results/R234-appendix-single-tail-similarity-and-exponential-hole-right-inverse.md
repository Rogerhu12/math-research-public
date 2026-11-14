# R234第四附录：一次共同尾相似与指数孔次数权上的真实右逆

日期：2026-11-13（UTC+8）。作者：boundary；Astra-ISP-1cf8c51d 复核。状态：以下已证明，主问题未完成。

本稿再次构造新的逐层右逆，避免在连续的纯尾右逆中重复支付对角相似成本。结论由 $e^{Cq^{4/3}}$ 改进为一个固定指数权 $e^{24q}$：真实形式原像整层有指数增长上界，未知非零缺陷的次数尾不能快于某个指数。它仍不推出全部次数的无权平方和。

## 1. 对整个有限头模型只作一次相似

仍取 [R234](R234-slow-boundary-right-inverses-on-cubic-hole-degree-space.md) 的
$$
m=10+\lceil\log_2(q+1)\rceil,\qquad d=2^m,
\qquad1024(q+1)\le d<2048(q+1).
$$
纯尾权为 $a_j=(j+1)^{-2}$，$j\ge m$。这次对固定输入次数 $q$ 统一选一个平顶
$$
J=2m+4(q+d+1),\qquad
b_j=\min(a_j,J^{-2}),
\qquad \rho_j=a_j/b_j\ge1.
\tag{1.1}
$$
$\rho_j$ 只在有限多个位置不等于 $1$。令 $S$ 为整个纯尾 Fock 空间上的正有界可逆对角乘子
$$
S e_F=\left(\prod_{j\in F}\rho_j\right)e_F.
$$
虽然它的全空间范数很大，$S^{-1}$ 是收缩，且后文只需 $S$ 在输入次数不超过 $q$ 时的范数。
记
$$
D_a=\sum_{j\ge m}a_jE_j,\qquad D_b=\sum_{j\ge m}b_jE_j.
$$
逐坐标比较给
$$
D_a^*=S D_b^*S^{-1},\qquad
\boxed{D_a=S^{-1}D_bS.}
\tag{1.2}
$$
$S$ 只作用于尾，故与真实头矩阵 $T_m$ 交换。因此整个模型满足
$$
\boxed{T_m+D_a=S^{-1}(T_m+D_b)S.}
\tag{1.3}
$$
关键是对 (1.3) 的整个模型右逆作一次相似，而不是对每一步右逆各付一次相似成本。

## 2. 中间全部次数的统一平顶右逆

对每个 $0\le s\le q+d$，纯矩阵 CCR 在整个尾第 $s$ 层给
$$
D_bD_b^*\ge
\left(\sum_{j\ge m}b_j^2-2s\max_jb_j^2\right)I.
$$
前 $J-m$ 个权都等于 $J^{-2}$，故由 (1.1)，
$$
\sum b_j^2-2s\max b_j^2
\ge(J-m-2(q+d))J^{-4}
=(m+2q+2d+4)J^{-4}\ge\frac1{2J^3}.
\tag{2.1}
$$
所以在所有所需中间次数，$D_b$ 有右逆 $Q^b_s:H_{\ge m,s}\to H_{\ge m,s+1}$，统一满足
$$
D_bQ^b_s=I,
\qquad \|Q^b_s\|\le U:=\sqrt2\,J^{3/2}.
\tag{2.2}
$$
例如可取 $(D_b^*|_{H_s})(D_bD_b^*|_{H_s})^{-1}$。这些右逆一般不保持有限位置，但恰好增加一个孔。

按次数拼接 $\mathcal Q_b$。它与 $T_m$ 交换，并在全部组合需要的层上满足 $D_b\mathcal Q_b=I$。定义
$$
R^b_{m,q}=\sum_{k=0}^{d-1}(-T_m)^k\mathcal Q_b^{k+1}
\quad\text{于尾次数不超过 }q.
$$
有限和望远镜消去、$T_m^d=0$ 给
$$
(T_m+D_b)R^b_{m,q}=I.
$$
由 (1.3)，定义真正需要的新模型右逆
$$
\boxed{\widetilde R_q=S^{-1}R^b_{m,q}S|_{H_q}.}
\tag{2.3}
$$
于是
$$
T^{[m]}\widetilde R_q=I|_{H_q}.
\tag{2.4}
$$
三个因子都不改变各自的头尾分解；$S^{\pm1}$ 保孔次数。输出仍满足
$$
\widetilde R_q H_q\subset H_{\le r_q},\qquad
r_q=q+m+d,\qquad r_q+1\le4096(q+1).
\tag{2.5}
$$

## 3. 单次相似的输入成本和模型内部成本

### 3.1 输入只付 $e^{22q}$

因 $2m\le d$、$4(q+1)\le d/256$，
$$
J<6d<12288(q+1).
$$
在所有尾次数不超过 $q$ 上，$S$ 的最大范数在第 $q$ 层、最小的 $q$ 个位上取得。若 $q\ge1$，对数积分下界给
$$
\|S|_{H_{\ge m,\le q}}\|
\le\left(\frac{J^q}{\prod_{r=1}^q(m+r)}\right)^2
\le\left(\frac{eJ}{m+q}\right)^{2q}.
$$
由于 $m\ge1$，$m+q\ge q+1$，因此
$$
\boxed{\|S|_{H_{\ge m,\le q}}\|\le e^{22q}.}
\tag{3.1}
$$
这里 $2(1+\log12288)<22$。$q=0$ 时由 $S|_{H_0}=I$ 成立。
输出端只付 $\|S^{-1}\|\le1$，而不是再付一个正相似因子。

### 3.2 $R^b_{m,q}$ 只有对数平方级成本

置 $x=q+1\ge1$、$\ell=\log x$。则
$$
m\le11+2\ell,\qquad
\log U\le15+2\ell,\qquad
\log d\le8+2\ell.
\tag{3.2}
$$
沿用真实四次头幂
$$
\|T_m^k\|\le6^k,
\qquad
\|T_m^k\|\le6^ke^{-\gamma k^4}\quad(k\ge2m),
\qquad \gamma=770/16^4>1/100.
$$
第 $k$ 项的对数范数至多
$$
15+2\ell+k(17+2\ell),
$$
而当 $k\ge2m$ 时，再减去 $\gamma k^4$。

低幂 $k<2m$，加上项数成本，统一至多
$$
397+116\ell+8\ell^2.
$$
高幂由准确优化
$$
\sup_{t\ge0}(vt-\gamma t^4)
=\frac{3v^{4/3}}{4^{4/3}\gamma^{1/3}}<3v^{4/3}
$$
得到上界
$$
23+4\ell+3(17+2\ell)^{4/3}
\le890+208\ell+12\ell^2.
$$
后一式也覆盖低幂。因此
$$
\boxed{\log\|R^b_{m,q}\|\le890+208\log(q+1)+12\log^2(q+1).}
\tag{3.3}
$$
(2.3)、(3.1)、(3.3) 给
$$
\boxed{
\log\|\widetilde R_q\|
\le22q+890+208\log(q+1)+12\log^2(q+1).
}
\tag{3.4}
$$
特别，存在有限常数 $A$ 使
$$
\|\widetilde R_q\|\le A e^{23(q+1)},
\tag{3.5}
$$
并且一个供全部实际误差使用的粗预算为
$$
\boxed{\log\|\widetilde R_q\|\le2000(q+1)\le d(q)^3.}
\tag{3.6}
$$
核对 (3.6) 只需 $\log x\le x$、$\log^2x\le x$，以及 $d\ge1024x$。

## 4. 全部真实 carry 在三次权及指数权中的收缩

由 (2.4)，
$$
T\widetilde R_q-I
=\sum_{L\ge m}K_L\widetilde R_q,
\qquad \|K_L\|\le52e^{-77016^{L-1}}.
$$
$K_L$ 作用于前 $L+1$ 位，所以第 $L=m+t$ 项输出次数不超过 $r_q+m+t+1$，且
$r_q+m+t+2\le3d+t$。

先在原三次权 $X_{1,3}$ 中。由 (3.6)，逐项对数预算为
$$
-48.125d^4\,16^t+d^3+\log52+\tfrac12\log(3d+t)+(3d+t)^3.
$$
与 R234 相同，正项不超过 $55d^3\,16^t$。故
$$
\boxed{
\|(T\widetilde R_q-I)v\|_{X_{1,3}}
\le2e^{-40d(q)^4}\|v\|.
}
\tag{4.1}
$$
这里没有使用新右逆的有限位置性质。

再定义指数孔权
$$
X_{24,1}=\left\{f:\sum_{q\ge0}e^{24(q+1)}\|\mathsf P_qf\|<\infty\right\}.
$$
在此权下，相同真实误差项的正指数为
$$
 d^3+\log52+\tfrac12\log(3d+t)+24(3d+t).
$$
它不超过 $3d^3\,16^t$，因为 $d\ge1024$ 且 $t+1\le16^t$。因此同样有
$$
\boxed{
\|(T\widetilde R_q-I)v\|_{X_{24,1}}
\le2e^{-40d(q)^4}\|v\|.
}
\tag{4.2}
$$
由 (3.5)，$\widetilde R=\sum_q\widetilde R_q\mathsf P_q$ 有界
$X_{24,1}\to H_-$。由 (4.2)，$\widetilde E=T\widetilde R-I$ 在
$X_{24,1}$ 上的范数小于 $1/4$。所以
$$
\boxed{
\widetilde G=\widetilde R(I+\widetilde E)^{-1}:
X_{24,1}\to H_-,\qquad T\widetilde G=I.
}
\tag{4.3}
$$

## 5. 有限输入的核差和真实形式原像整层指数界

仍设 $M=\ker T$、$N=\overline{BM}$、$w\in M\ominus N$，并取已有形式原像
$T^*h=w$。有限位置测试满足
$$
\langle h,v\rangle=\langle w,J_Tv\rangle,\qquad TJ_Tv=v.
$$
由 (4.1)，按输出三次范数及输入层的 Cauchy–Schwarz 求和，
$$
\widetilde E:H_-\to X_{1,3}\quad\text{有界}.
\tag{5.1}
$$
对有限位置 $v$，令 $y=(I+\widetilde E)^{-1}v$。因
$y=v-\widetilde Ey$，得到 $y\in X_{1,3}$。而 (2.5)、(3.6) 给
$$
\widetilde R:X_{1,3}\to X_{\gamma_0,3}
\quad\text{有界},\qquad \gamma_0=(4\cdot4096^3)^{-1}.
$$
故 $\widetilde Gv-J_Tv\in M\cap X_{\gamma_0,3}\subset N$，最后一步使用已经证明的 [三次正则核饱和](R234-appendix-fixed-hole-primitives-and-cubic-regular-saturation.md)。由有限测试稠密性，
$$
\boxed{
 h_q=(\widetilde G|_{H_q})^*w,\qquad
 \|h_q\|\le\|\widetilde G\|e^{24(q+1)}\|w\|.
}
\tag{5.2}
$$
此式合法应用于真正缺陷的形式原像，且对一个完整固定孔层的全部位置成立。

## 6. 指数次数空间本身在真实 $T$ 下不变

这个新的权阶还有一个此前超线性权不具备的方便性质。对任意固定 $c\ge0$，记
$$
X_{c,1}=\left\{f:\sum_{q\ge0}e^{c(q+1)}\|\mathsf P_qf\|<\infty\right\}.
$$
则
$$
\boxed{T:X_{c,1}\to X_{c,1}\quad\text{有界}.}
\tag{6.1}
$$
证明：纯删除 $D$ 只将 $q$ 层送到 $q-1$ 层。局部 $K_L$ 至多改变 $L+1$ 个位，因此对输入第 $q$ 层，输出次数位于
$[\max(0,q-L-1),q+L+1]$；不是把所有 $0$ 到 $q+L+1$ 的次数都算作可达。
所以只有至多 $2L+3$ 个输出层，并且
$$
\|K_Lv\|_{X_{c,1}}
\le\sqrt{2L+3}\,e^{c(L+1)}\|K_L\|
 e^{c(q+1)}\|v\|.
$$
$\sum_L\sqrt{2L+3}e^{c(L+1)}52e^{-77016^{L-1}}<\infty$，得 (6.1)。

令 $X_{24,1}^+$ 的权为 $e^{24(q+2)}$；它的范数恰为 $e^{24}$ 倍的 $X_{24,1}$ 范数。
由真实夹置 $N_i\widetilde GE_i^*$ 取弱算子聚点，得到
$$
C_*:X_{24,1}^+\to H_-,\qquad
TC_*=I,\qquad \|C_*\|\le\|\widetilde G\|,
$$
且对有限位置 $v$，$C_*v-J_Tv\in N$。理由仍为真实等式
$N_iE_i^*=I-E_i^*E_i$，以及有限测试时核差属于
$M\cap\operatorname{Ran}B\subset N$。
有限位置 $x$ 因而满足 $x-C_*Tx\in N$。

利用 (6.1) 在同一个指数权中的连续性作有限位置逼近，得到
$$
\boxed{M\cap X_{24,1}\subset N.}
\tag{6.2}
$$
不需要再把输入权常数严格增加。仍未证明任意小的指数权或 $M$ 中的密度。

## 7. 未知非零缺陷不能具有超指数次数尾

设 $w\in M\ominus N$、$\|w\|=1$，并置
$$
u_q=\mathsf P_{\le q}w,\qquad
\tau_q=\|\mathsf P_{>q}w\|,\qquad q\ge1.
$$
由固定次数中有限位置逼近及第 6 节，$u_q-C_*Tu_q\in N$。所以
$$
\|u_q\|^2\le\|\widetilde G\|\,\|Tu_q\|_{X_{24,1}^+}.
$$
输出次数不超过 $2q$ 的部分，由 $Tw=0$ 有界为
$$
6\sqrt{2q+1}\,e^{24(2q+2)}\tau_q.
$$
高输出只能来自 $L\ge q$ 的局部 $K_L$，总余量至多
$$
52\sum_{L\ge q}\sqrt{q+L+2}
 e^{-77016^{L-1}+24(q+L+3)}\longrightarrow0.
$$
因此对充分大 $q$，
$$
\boxed{
\tau_q\ge
\frac{e^{-24(2q+2)}}{24\|\widetilde G\|\sqrt{2q+1}}.
}
\tag{7.1}
$$
特别，
$$
\boxed{-\log\tau_q=O(q).}
\tag{7.2}
$$
这是实际缺陷的孔次数尾，不是最高位置尾。它允许慢指数尾、亚指数尾以及多项式尾，故不推出缺陷为零。

## 8. 准确范围

本稿的新增输入是把一次尾对角相似放在整个有限头模型右逆的两端。输出端相似逆收缩，输入端只付 $e^{O(q)}$；中间所有次数共享平顶 CCR，使它们不再各自重复付 $e^{O(q)}$。真实有限头高幂付掉长 Neumann 和，全部实际 carry 则仍按三次误差估计控制。

结论包括 $X_{24,1}$ 上的实际右逆、真实形式原像每层指数上界、$M\cap X_{24,1}\subset N$，以及非零缺陷的指数次数尾下界。没有证明形式原像的全部无权平方和，也没有证明 $N=M$。
