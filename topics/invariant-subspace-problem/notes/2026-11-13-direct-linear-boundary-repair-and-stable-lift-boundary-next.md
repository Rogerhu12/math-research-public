# 原实际慢算子的线性低输出修复与直接稳定像提升

日期：2026-11-13（UTC）。作者：boundary_next。状态：完整中间证明；普通 ISP 与无权 $N=M$ 仍未完成。

本稿直接使用原 $T_N,T_Y$ 的“真实有限头加纯尾”线性模型。它重新构造低输出投影和核内提升，不把此前只对首位平方图 $J_m$ 证明的 $\Lambda$ 移用到新模型。相容多次原像来自 R254 第十附录；特殊输入的删除幂则由本稿的一阶低输出方程准确决定。

结果把已发布平方模型的直接平方对数参数 $b>1/\log2$ 改进为 $b>1/(2\log2)$，非零真缺陷的必要尾常数改进为 $1/(4\log2)$。本稿同时给一个直接在原 Hilbert 范数下定义的最小高尾修复能量。没有把这些正则结论当作一般核内稠密性。

## 1. 原算子、真实线性混合模型和物理位号

在原边界有限子集空间上，
$$
T=T_N=\sum_{j\ge0}(j+1)^{-2}N_j
\quad\text{或}\quad
T=T_Y=\sum_{j\ge0}(j+1)^{-2}Y_j,
$$
$$
Y_j=N_j(I+N_j)^{-1}.
$$
记
$$
M=\ker T,\qquad N=\overline{BM},\qquad
D_{\rm def}=M\ominus N.
$$

本稿的头直接包含原物理位 $0,\ldots,m-1$，不先删除原首位。令
$$
m\ge5,\qquad d=2^m,\qquad q=d^4.
$$
$A_m$ 表示 $T$ 在这个真实有限头上的截断；$D$ 表示其后独立的纯尾删除：
$$
D=\sum_{j\ge m}(j+1)^{-2}E_j,\qquad \|D\|\le1.
$$
定义真实线性混合模型
$$
\boxed{L_m=A_m+D.}
\tag{1.1}
$$
$A_m$ 是真实有限头快速后移的零常数多项式，所以
$$
A_m^d=0.
\tag{1.2}
$$
全部实际 $N/Y$ Cayley 因子均留在 $A_m$ 中。

原真实截断预算为
$$
\boxed{\|T-L_m\|\le26\eta_{m-1}.}
\tag{1.3}
$$
这里的物理位号比删除首位后的平方模型少一位，精确为
$$
\boxed{
-\log\eta_{m-1}
=\frac{175}{2}d^4-\frac{315}{4}d^3+150d.
}
\tag{1.4}
$$
不能沿用平方模型中的 $1400d^4$。

原有限头归一化幂范数至多 $1$，真实 Cayley 逆至多 $3$，而
$\sum_{j\ge0}(j+1)^{-2}<2$。因此统一使用
$$
\|A_m\|\le6.
\tag{1.5}
$$

以下 $P_\ell$ 数原前 $m$ 位之后的高尾孔，包含有限头恒等；$\tau_Q(w)$ 则始终表示原全部物理孔次数超过 $Q$ 的 Hilbert 尾。

## 2. 一次共同截平修复全部低输出方程

先为 $L_m$ 的任意完整低孔输入构造右逆。本节不要求输入已在某个纯核内。

置
$$
Q=q+d,\quad J=2Q+1,\quad
W=m+J+1=m+2q+2d+2,\quad \beta=W^{-2}.
$$
把纯尾的前 $J$ 个系数截平为 $\beta$，其余不变，记所得删除为 $\widetilde D$。全部新系数不超过 $\beta$，且平方和至少为 $J\beta^2$。所以在每个完整尾孔层 $\ell\le Q$，创建算子的实际 CCR 给
$$
\|\widetilde D^*f\|^2
\ge\beta^2(J-2\ell)\|f\|^2
\ge\beta^2\|f\|^2.
$$
存在实际逐层右逆 $\widetilde G_\ell$，满足
$$
\widetilde D\widetilde G_\ell=I,\quad
\widetilde G_\ell\mathcal H_\ell\subseteq\mathcal H_{\ell+1},
\quad \|\widetilde G_\ell\|\le\beta^{-1}=W^2.
\tag{2.1}
$$

在被截平的位置置 $\rho_j=(j+1)^{-2}/\beta$，其他位置置 $\rho_j=1$，令 $S$ 对孔集 $F$ 乘以 $\prod_{j\in F}\rho_j$。它是有限位置的实际正可逆对角，保持孔层，且
$$
SD=\widetilde DS,\qquad
\|S^{-1}\|\le1.
$$
全空间最大对角乘子给
$$
\|S\|\le\left(\frac{W^J}{J!}\right)^2
\le \exp(2J+2m+2)
=\exp(4q+4d+2m+4).
\tag{2.2}
$$

令 $\widetilde G$ 为实际层右逆的代数直和。因它与有限头 $A_m$ 交换，
$$
\widetilde R
=\sum_{j=0}^{d-1}(-A_m)^j\widetilde G^{\,j+1}
$$
在输入尾孔数至多 $q-1$ 上满足
$$
(A_m+\widetilde D)\widetilde R=I.
$$
输出次数至多 $q-1+d$，每次右逆都在 (2.1) 的范围内。由 (1.2) 有限和准确望远镜；没有无穷级数收敛问题。

变回原坐标，
$$
R^{\rm low}_{m,q}=S^{-1}\widetilde R S,
$$
则
$$
L_mR^{\rm low}_{m,q}=I,\qquad
\|R^{\rm low}_{m,q}\|
\le d(6W^2)^d e^{4q+4d+2m+4}.
\tag{2.3}
$$
这是完整低孔空间上的界，位置不需有限。

固定实际 $w\in M$。令
$$
r_0=P_{\le q-1}L_mw
=P_{\le q-1}(L_m-T)w,
$$
$$
z=w-R^{\rm low}_{m,q}r_0.
$$
则 $P_{\le q-1}L_mz=0$。因为 $L_m$ 只下降零次或一次尾孔，截掉 $z$ 的 $>q$ 部分不会改变 $\le q-1$ 的输出。所以 $P_{\le q}z$ 属于闭空间
$$
\boxed{
\mathcal W^{\rm lin}_{m,q}
=\mathcal H_{\le q}\cap\ker(P_{\le q-1}L_m).
}
\tag{2.4}
$$
令 $v_m$ 是 $w$ 到这个实际闭空间的正交投影。最佳逼近性给
$$
\|v_m\|\le\|w\|,
$$
$$
\|v_m-P_{\le q}w\|
\le\epsilon_m\|w\|,
$$
$$
\epsilon_m=
26\eta_{m-1}d(6W^2)^d e^{4q+4d+2m+4}.
\tag{2.5}
$$
高尾不乘这个右逆常数。

现在直接核 $q=d^4,m\ge5,d\ge32$ 的预算。因 $W\le3d^4$，(1.4)、(2.5) 给
$$
\log\epsilon_m
\le-\frac{167}{2}d^4+\frac{315}{4}d^3
-146d+2m+4+\log26+\log d+d\log6+2d\log W.
$$
用 $\log W<2+4\log d$、$\log d\le d/2$、$2m\le d$，除 $(315/4)d^3$ 外的正项至多 $5d^2$。
又
$$
\frac{315}{4}d^3\le\frac52d^4,\qquad 5d^2\le d^4.
$$
于是
$$
\boxed{
\|v_m-P_{\le q}w\|\le e^{-80d^4}\|w\|,
\qquad v_m\to w.
}
\tag{2.6}
$$
最后的强收敛只使用 $\|P_{>q}w\|\le\tau_q(w)\to0$。

## 3. 线性低输出方程的准确删除幂

本节令 $v=v_m$，并置
$$
r=L_mv.
$$
由 (2.4) 和不升次数性，
$$
\boxed{r\in\mathcal H_q,\qquad r=A_mv_q,\quad v_q=P_qv.}
\tag{3.1}
$$
它只有一层输出。

有限几何恒等式为
$$
D^kv-(-A_m)^kv
=\sum_{j=0}^{k-1}D^{k-1-j}(-A_m)^j r.
$$
右边所有项的最低次数至少为 $q-k+1$，而 $D^kv$ 的最高次数为 $q-k$。所以
$$
\boxed{
D^kv=P_{\le q-k}(-A_m)^kv.
}
\tag{3.2}
$$
因此 $D^dv=0$。比较 (3.2) 的恰 $q-k$ 层，并使用 (3.1)，得到更强的单层身份：
$$
\boxed{
D^kr=(-1)^k A_m^{k+1}v_{q-k},
\qquad 0\le k<d.
}
\tag{3.3}
$$
特别 $D^dr=0$；事实上 $D^{d-1}r=0$ 也成立，但后文只用较弱版本。

这保留了每个删除幂对应的**实际头幂**及其输入层，而不只给一个粗核阶。

## 4. 相容多次原像与单次头进位预算

使用 R254 第十附录的同一辅助头方法，输入上界 $q$，最大原像阶 $d$。本稿系数是 $(j+1)^{-2}$；把其纯尾指标改为 $j'=j-1$ 就是该附录的 $(j'+2)^{-2}$，且以下取稍大的 $m+Q+2$ 仍是有效上界。

得到实际 $R_t$，
$$
R_0=I,\quad DR_t=R_{t-1},\quad
R_t\mathcal H_p\subseteq\mathcal H_{p+t},
\qquad 0\le t\le d,\ p\le q.
$$
令
$$
a=512\sqrt{q+d+1}(m+q+d+2)^{3/2}.
\tag{4.1}
$$
保留该附录双和中的 $\|D^kf\|$ 后，已经核验的细界是
$$
\boxed{
\|R_tf\|\le
\sum_{k=0}^{q}\binom{k+t-1}{k}a^{k+t}\|D^kf\|
\le\sum_{k=0}^{q}(2a)^{k+t}\|D^kf\|.
}
\tag{4.2}
$$
完整孔层、共同辅助头、有理分母正性及非齐次直和均按原证明成立。

定义线性混合右逆
$$
\boxed{
\mathcal R_{m,q}
=\sum_{j=0}^{d-1}(-A_m)^jR_{j+1}.
}
\tag{4.3}
$$
因 $A_m$ 与纯尾各算子交换，$DR_{j+1}=R_j$ 和 $A_m^d=0$ 给
$$
L_m\mathcal R_{m,q}=I.
\tag{4.4}
$$
输入单层 $q$ 的第 $j$ 项输出恰在 $q+j+1$，故全部输出在 $[q+1,q+d]$。

真实头的二进位归约给，对包含 $n$ 个归一化头因子的非零词，其进位代价满足
$$
E\ge(n-m)_+^4/256.
$$
原物理系数 $\eta_j\le e^{-770\,16^j}$ 及所有 Cayley 逆的预算给
$$
\boxed{
\|A_m^n\|\le
6^n e^{-\gamma(n-m)_+^4},
\qquad \gamma=770/256.
}
\tag{4.5}
$$
这里的 $6^n$ 来自慢系数和小于 $2$ 以及每个真实 Cayley 逆至多 $3$。它与删除首位后的 $2^n$ 不是同一个常数，但只影响低阶对数项。

令
$$
c_m=\mathcal R_{m,q}r.
$$
对 (4.3) 的第 $j$ 项，先把头 $A_m^j$ 与 $R_{j+1}$ 交换，再使用 (4.2)、(3.3)，得到
$$
\|(-A_m)^jR_{j+1}r\|
\le\sum_{k=0}^{d-1}
(2a)^{j+k+1}
\|A_m^{j+k+1}v_{q-k}\|.
$$
置
$$
R(v)=\|P_{[q-d+1,q]}v\|,\qquad
\Theta_m=\log(12a).
$$
所有 $v_{q-k}$ 的范数至多 $R(v)$。由 (4.5)，总和至多有 $d^2$ 项，且
$$
\Theta_m n-\gamma(n-m)_+^4
\le m\Theta_m+3\Theta_m^{4/3}.
$$
因此
$$
\boxed{
\|c_m\|\le e^{F_m}R(v),
\qquad
F_m=2\log d+m\Theta_m+3\Theta_m^{4/3}.
}
\tag{4.6}
$$
两段真实头因子在 $A_m^{j+k+1}$ 中已经合并；没有分别支付两个头长度。

在 $q=d^4,m\ge5$ 下，
$$
a\le2048d^8,\qquad
\Theta_m<11+\frac{28}{5}m\le8m.
$$
用 $3(8m)^{4/3}=48m^{4/3}\le24m^2$，得到
$$
\boxed{F_m\le64m^2\le d^4.}
\tag{4.7}
$$
同时
$$
a=512q^2(1+o(1)),\quad \log q=4m\log2,
$$
所以
$$
\boxed{F_m=(8\log2+o(1))m^2.}
\tag{4.8}
$$

## 5. 准确线性核向量及顶部修复界

由 (4.4)，
$$
k_m=v_m-c_m\in\ker L_m,
\qquad
c_m\in\mathcal H_{[q+1,q+d]},
\quad k_m\in\mathcal H_{\le q+d}.
\tag{5.1}
$$
低孔部分准确保持 $P_{\le q}k_m=v_m$。

若需纯高阶核归属，原有限伴随多项式
$$
\mathcal A_m=\sum_{j=0}^{d-1}(-A_m)^jD^{d-1-j}
$$
满足 $\mathcal A_mL_m=D^d$。于是
$$
D^dc_m=\mathcal A_mr=D^dv_m=0.
\tag{5.2}
$$
这不是一般性地宣称右逆保持同一核阶。

由 (2.6)，
$$
R(v_m)\le\tau_{q-d}(w)+e^{-80d^4}\|w\|.
$$
结合 (4.6)—(4.7)，得到
$$
\boxed{
\|c_m\|
\le e^{F_m}\tau_{q-d}(w)+e^{-79d^4}\|w\|.
}
\tag{5.3}
$$
也可直接用 $R(v_m)\le\|w\|$，得到
$$
\|c_m\|\le e^{d^4}\|w\|,\qquad
\|k_m\|\le2e^{d^4}\|w\|.
\tag{5.4}
$$

## 6. 独立支付原 T 的实际核到 N 提升

本节重新使用原 $T$ 的加权进位公式，不调用平方图的 $\Lambda$。

令 $T^{[h]}$ 是原前 $h$ 位真实头加纯高尾的混合截断；所以 $L_m=T^{[m]}$。已证明
$$
\|T-T^{[h]}\|\le26\eta_{h-1}.
$$
设 $K_L=T^{[L+1]}-T^{[L]}$。它只作用前 $L+1$ 个物理位，且
$$
\|K_L\|\le52\eta_{L-1}.
$$
原 $\mathscr X_7$ 范数为
$$
\|x\|_{\mathscr X_7}=\sum_{n\ge0}e^{7n}\|\mathsf P_nx\|,
$$
其中 $\mathsf P_n$ 数原全部物理孔。局部支撑的行/列层求和给
$$
\|K_L\|_{\mathscr X_7\to\mathscr X_7}
\le52\sqrt{2L+3}\,e^{7(L+1)}\eta_{L-1}.
$$
准确 $\eta$ 指数的相邻差大于 $16590$，使此正项尾级数的相邻比小于 $1/2$。因此
$$
\boxed{
\|T-L_m\|_{\mathscr X_7\to\mathscr X_7}
\le104\sqrt{2m+3}\,e^{7(m+1)}\eta_{m-1}.
}
\tag{6.1}
$$
这一估计适用于原 $N/Y$ 模型，指数位号保持 $m-1$。

原 R239 两权右逆已经给
$$
G_{7\to3}:\mathscr X_7\to\mathscr X_3,\qquad
TG_{7\to3}=I,\qquad
\|G_{7\to3}\|\le C_G=\frac43e^{2^{24}}.
\tag{6.2}
$$
并有 $M\cap\mathscr X_3\subseteq N$。

若 $k\in\ker L_m\cap\mathcal H_{\le q+d}$，其原全部孔数至多 $q+d+m$。所以
$$
\|k\|_{\mathscr X_7}
\le\sqrt{q+d+m+1}\,e^{7(q+d+m)}\|k\|.
$$
$Tk=(T-L_m)k$ 确实属于 $\mathscr X_7$。定义
$$
\boxed{
\Lambda^{\rm lin}_{m,q}k
=k-G_{7\to3}Tk.
}
\tag{6.3}
$$
准确有
$$
T\Lambda^{\rm lin}_{m,q}k=0,\qquad
\Lambda^{\rm lin}_{m,q}k\in\mathscr X_3,
$$
所以
$$
\boxed{\Lambda^{\rm lin}_{m,q}k\in M\cap\mathscr X_3\subseteq N.}
\tag{6.4}
$$
没有从旧的 $\mathscr X_c\to H$ 右逆猜测输出正则性。

由 (6.1)—(6.2)，
$$
\|\Lambda^{\rm lin}_{m,q}k-k\|_{\mathscr X_3}
\le\Delta_m\|k\|,
$$
$$
\boxed{
\Delta_m=
104C_G\sqrt{(2m+3)(q+d+m+1)}
e^{7(q+d+2m+1)}\eta_{m-1}.
}
\tag{6.5}
$$
直接代入 $q=d^4$：
$$
\begin{aligned}
\log\Delta_m={}&
-\frac{161}{2}d^4+\frac{315}{4}d^3-143d
+2^{24}+14m+7+\log(416/3)\\
&+\tfrac12\log((2m+3)(d^4+d+m+1)).
\end{aligned}
$$
对 $d\ge32$，
$$
\frac{315}{4}d^3\le\frac52d^4,\quad
2^{24}\le16d^4.
$$
剩余正对数项至多 $d^2\le d^4$，例如由
$2m+3\le2d$、$d^4+d+m+1\le2d^4$ 和
$14m\le7d$ 即可核验。丢掉负项 $-143d$，得到
$$
\boxed{\Delta_m\le e^{-61d^4}\qquad(m\ge5).}
\tag{6.6}
$$

应用于 (5.1) 的 $k_m$，置
$$
n_m=\Lambda^{\rm lin}_{m,q}k_m\in N.
$$
由 (5.4)、(6.6)，完整乘入修复范数后仍有
$$
\boxed{
\|n_m-(v_m-c_m)\|
\le e^{-59d^4}\|w\|.
}
\tag{6.7}
$$
这完成了直接原算子提升；没有借用任何平方图范数或平方模型核等价。

## 7. 直接平方对数饱和及真缺陷尾常数

**定理。** 对两个原实际边界，任意 $b>1/(2\log2)$ 都有
$$
\boxed{
M\cap\operatorname{Dom}
\exp\!\left(b[\log(2+\mathcal N)]^2\right)
\subseteq N.
}
\tag{7.1}
$$
其中 $\mathcal N$ 是原全部物理孔次数算子。

若 $w$ 属于该域，
$$
\tau_s(w)\le C_w e^{-b[\log(s+3)]^2}.
$$
取 $s=q-d=d^4-d$，则
$$
\log(s+3)=4m\log2+o(1).
$$
由 (4.8)，
$$
F_m-b[\log(s+3)]^2
=\bigl(8\log2-16b(\log2)^2+o(1)\bigr)m^2\to-\infty.
$$
所以 (5.3) 给 $c_m\to0$。再由 (2.6)、(6.7)，有 $n_m\to w$ 强收敛；$N$ 闭，得 (7.1)。
此证明直接作用于原 $w$，不要求任何缺陷投影保权。临界等号未声明。

若 $0\ne w\in D_{\rm def}$，由 $n_m\in N$、$v_m\to w$、(6.7)，
$$
\langle c_m,w\rangle\longrightarrow\|w\|^2.
$$
$c_m$ 的高尾孔数至少 $q+1$，故其原总孔数也至少 $q+1$。充分大 $m$ 时
$$
\|c_m\|\tau_q(w)\ge\tfrac12\|w\|^2.
$$
结合 (5.3)、尾单调性并吸收明确小项，得到
$$
e^{F_m}\tau_{q-d}(w)^2\ge\tfrac14\|w\|^2.
$$
相邻 $q-d$ 网格的比值趋于 $16$，对数只相差有界常数。由 (4.8)，
$$
\boxed{
\limsup_{Q\to\infty}
\frac{\log(\|w\|/\tau_Q(w))}
{[\log(Q+2)]^2}
\le\frac1{4\log2}.
}
\tag{7.2}
$$
这仍是非零真缺陷的必要慢尾条件，不是尾部上界。

## 8. 原 Hilbert 范数下的最小修复正能量

本稿重新定义一个线性模型能量，不与旧平方模型的 $\gamma_m$ 混同。

对同一 $v_m,r_m$，令
$$
\mathcal C_m^{\rm lin}(w)
=\{c\in\mathcal H_{[q+1,q+d]}:
L_mc=r_m,\ D^dc=0\}.
$$
它由 (5.1)—(5.2) 非空，并且是原 Hilbert 空间的闭仿射集。因此有唯一最小范数元 $c_m^{\min}$，记
$$
\lambda_m(w)=\|c_m^{\min}\|.
$$
新候选给
$$
\boxed{
\lambda_m(w)\le
e^{F_m}\left(
\tau_{q-d}(w)+e^{-80d^4}\|w\|
\right).
}
\tag{8.1}
$$
其范数不超过 (5.4)，所以同一真实线性提升仍适用。

$c_m^{\min}$ 在原全部孔次数上的支撑包含于
$$
[q+1,q+d+m].
$$
这些窗口随 $m$ 两两不交。于是最小能量与先前图能量一样满足正凸平均判据：
$$
\boxed{
\sum_{m\ge5}\frac1{1+\lambda_m(w)^2}=\infty
\quad\Longrightarrow\quad w\in N.
}
\tag{8.2}
$$
证明取权 $(1+\lambda_m^2)^{-1}$ 归一化平均相应 $n_m\in N$。正交高尾的平均平方范数至多是权和的倒数；$v_m-w$ 及实际提升误差在尾起点之后一致趋零。

若 $0\ne w\in D_{\rm def}$，则最小修复同样满足
$\langle c_m^{\min},w\rangle\to\|w\|^2$。对充分大 $M_0$ 及 $M\ge M_0$，Bessel 给
$$
\boxed{
\sum_{m\ge M}\lambda_m(w)^{-2}
\le\frac{4\,\tau_{q_M}(w)^2}{\|w\|^4},
\qquad q_M=2^{4M}.
}
\tag{8.3}
$$
这是原范数下的真实最小修复能量，不含额外首位图度量。

(8.1) 仍未保证 (8.2) 的级数发散。一般 Hilbert 尾可以慢于平方对数权；不存在从 $\tau_Q(w)\to0$ 到 (8.2) 的现成推论。无权 $N=M$ 和普通 ISP 继续开放。

已用完整来源：
- [R239 实际指数权与原混合截断预算](../results/R239-appendix-exponential-hole-right-inverses-and-true-tail-regularization.md)；
- [R239 实际两权正则提升](../results/R239-appendix-mixed-low-hole-kernel-regular-lift-to-stable-range.md)；
- [R239 低输出恒等式与平方对数稳定像](../results/R239-appendix-low-output-identities-and-log-squared-stable-range.md)；
- [R239 相容原像与一次头平方对数预算](../results/R239-appendix-compatible-preimages-and-single-head-log-squared-budget.md)；
- [R254 相容多次纯尾原像](../results/R254-appendix-compatible-multiple-preimages-and-quarter-stable-range.md)；
- [R216 原混合截断与实际进位](../results/R216-uniform-occupied-prefix-decay-in-actual-slow-kernels.md)。
