# R239 附录：原线性模型的低输出修复、直接稳定提升和最小能量

日期：2026-11-13。作者：Astra-ISP-0c / boundary_next。完整证明见[同日逐步稿](../notes/2026-11-13-direct-linear-boundary-repair-and-stable-lift-boundary-next.md)。本附录保留原物理位，不移用首位平方图的提升；普通 ISP 和无权 $N=M$ 仍开放。

## 定理与模型

对原两个实际边界
$$
T_N=\sum_{j\ge0}(j+1)^{-2}N_j,\qquad
T_Y=\sum_{j\ge0}(j+1)^{-2}Y_j,
$$
记 $M=\ker T$、$N=\overline{BM}$、$D_{\rm def}=M\ominus N$，$\mathcal N$ 为原全部物理孔次数。则
$$
M\cap\operatorname{Dom}\exp\!\left(b\log^2(2+\mathcal N)\right)
\subseteq N\qquad\left(b>\frac1{2\log2}\right).
$$
若 $0\ne w\in D_{\rm def}$，其原孔尾满足
$$
\limsup_{Q\to\infty}
\frac{\log(\|w\|/\tau_Q(w))}{\log^2(Q+2)}
\le\frac1{4\log2}.
$$
第二式是非零缺陷所必需的慢尾条件，不是任意核向量的尾上界；临界参数和无权核心仍未证明。

取 $m\ge5$、$d=2^m$、$q=d^4$。真实前 $m$ 位头为 $A_m$，其后纯删除为 $D=\sum_{j\ge m}(j+1)^{-2}E_j$。有
$$
L_m=A_m+D,\quad A_m^d=0,\quad\|A_m\|\le6,\quad
\|T-L_m\|\le26\eta_{m-1},
$$
$$
-\log\eta_{m-1}
=\frac{175}{2}d^4-\frac{315}{4}d^3+150d.
$$
这里不得使用删首位平方模型的 $1400d^4$ 进位指数。

## 低输出投影与特殊输入

一次共同截平取 $Q=q+d$、$J=2Q+1$、$W=m+2q+2d+2$、$\beta=W^{-2}$。完整尾孔层的 CCR 给截平删除右逆范数不超过 $W^2$；对角相似满足 $\|S^{-1}\|\le1$、$\|S\|\le e^{4q+4d+2m+4}$。有限几何和给原低输出右逆
$$
R^{\rm low}=S^{-1}\sum_{j<d}(-A_m)^j\widetilde G^{\,j+1}S,
\qquad
\|R^{\rm low}\|\le d(6W^2)^d e^{4q+4d+2m+4}.
$$
它修复完整 $\le q-1$ 输出，不把高尾乘入右逆常数。令 $v_m$ 为 $w\in M$ 到
$$
\mathcal H_{\le q}\cap\ker(P_{\le q-1}L_m)
$$
的正交投影，其中 $P$ 只数前 $m$ 位之后的尾孔。则
$$
\|v_m-P_{\le q}w\|\le e^{-80d^4}\|w\|,
\qquad \|v_m\|\le\|w\|,\qquad v_m\to w.
$$

置 $r=L_mv_m=A_m(v_m)_q\in\mathcal H_q$。准确低方程给
$$
D^kv_m=P_{\le q-k}(-A_m)^kv_m,\qquad
D^kr=(-1)^kA_m^{k+1}(v_m)_{q-k}.
$$
故 $D^dv_m=D^dr=0$。这些恒等式保留真实头幂，不能只替换成粗核阶。

## 相容原像和一次头预算

[R254 相容多次原像](R254-appendix-compatible-multiple-preimages-and-quarter-stable-range.md)给同一族 $DR_t=R_{t-1}$、$R_0=I$。令
$$
a=512\sqrt{q+d+1}(m+q+d+2)^{3/2}.
$$
原双和保留删除幂后有
$$
\|R_tf\|\le\sum_{k\le q}\binom{k+t-1}{k}a^{k+t}\|D^kf\|.
$$
取
$$
c_m=\sum_{j<d}(-A_m)^jR_{j+1}r.
$$
有 $L_mc_m=r$、$c_m\in\mathcal H_{[q+1,q+d]}$、$D^dc_m=0$。真实二进位估计
$$
\|A_m^n\|\le6^n\exp[-(770/256)(n-m)_+^4]
$$
作用于合并后的 $A_m^{j+k+1}$，而非两个分离范数。因此，置
$$
\Theta_m=\log(12a),\qquad
F_m=2\log d+m\Theta_m+3\Theta_m^{4/3},
$$
可得
$$
F_m\le64m^2\le d^4,\qquad F_m=(8\log2+o(1))m^2,
$$
$$
\|c_m\|\le e^{F_m}\tau_{q-d}(w)+e^{-79d^4}\|w\|.
$$
$k_m=v_m-c_m$ 是精确的 $L_m$ 核向量。

## 原算子的独立实际提升

原混合截断增量 $K_L=T^{[L+1]}-T^{[L]}$ 只作用前 $L+1$ 位。局部孔层和给
$$
\|T-L_m\|_{\mathscr X_7\to\mathscr X_7}
\le104\sqrt{2m+3}\,e^{7(m+1)}\eta_{m-1}.
$$
[R239 两权右逆](R239-appendix-mixed-low-hole-kernel-regular-lift-to-stable-range.md)在原 $T$ 上给 $G_{7\to3}:\mathscr X_7\to\mathscr X_3$、$TG_{7\to3}=I$，常数 $C_G=(4/3)e^{2^{24}}$，且 $M\cap\mathscr X_3\subseteq N$。因此
$$
\Lambda^{\rm lin}k=k-G_{7\to3}Tk\in N
\qquad(k\in\ker L_m\cap\mathcal H_{\le q+d}).
$$
其范数误差是
$$
\Delta_m=
104C_G\sqrt{(2m+3)(q+d+m+1)}
e^{7(q+d+2m+1)}\eta_{m-1}
\le e^{-61d^4}.
$$
即使乘入 $\|k_m\|\le2e^{d^4}\|w\|$，仍有
$$
n_m=\Lambda^{\rm lin}k_m\in N,\qquad
\|n_m-(v_m-c_m)\|\le e^{-59d^4}\|w\|.
$$
这付清原线性模型的核与稳定像接口。结合 $\log(q-d)=4m\log2+o(1)$，得到定理。缺陷情形用 $\langle c_m,w\rangle\to\|w\|^2$ 及高尾支撑，得 $e^{F_m}\tau_{q-d}(w)^2\ge\|w\|^2/4$，再以相邻网格对数差有界推出全序列尾常数。

## 原 Hilbert 最小修复能量

定义闭非空仿射集
$$
\mathcal C_m^{\rm lin}(w)=
\{c\in\mathcal H_{[q+1,q+d]}:L_mc=r,\ D^dc=0\},
$$
以及唯一最小元 $c_m^{\min}$ 和 $\lambda_m(w)=\|c_m^{\min}\|$。这不是旧平方图能量 $\gamma_m$。有
$$
\lambda_m(w)\le
e^{F_m}\bigl(\tau_{q-d}(w)+e^{-80d^4}\|w\|\bigr).
$$
最小元的原全部孔窗口 $[q+1,q+d+m]$ 两两不交；同一实际提升适用。正凸平均和 Bessel 分别给
$$
\sum_{m\ge5}(1+\lambda_m(w)^2)^{-1}=\infty
\ \Longrightarrow\ w\in N,
$$
$$
0\ne w\in D_{\rm def}
\ \Longrightarrow\
\sum_{m\ge M}\lambda_m(w)^{-2}
\le\frac{4\tau_{2^{4M}}(w)^2}{\|w\|^4}
\quad(M\ \text{充分大}).
$$
现有候选上界没有从一般 Hilbert 尾推出该级数发散；继续这一无权缺口，不将正则类饱和记为 $N=M$。
