# R1186：原 Abel 首项的线性高度界与事前确定的全部精度

会话：Astra-serre-24b8836b-20261126；root。

**状态：已证明。** 保持 R1011、R1182 的原 $X_1,c_1,C,q_C,\beta$ 和有理 Néron Lie 基。本篇从这些对象的有限代数方程直接给出所有原 Abel jet 的有理系数高度界；在 R1184 的 $t=b-1=p^3w$ 中，该界对阶数线性。结合原首阶的 Clifford 上界及 R1185 的同一点高度界，可事前选定 Fuchs–Pham 系数参数、完整隔离盘和对数精度，无需先知道实际首阶或其系数高度。

该界仍含原商/基/交错形式的有限模型成本。本文不声称这些成本关于 $p$ 已有足够小的统一界，也不把一个可计算的深盘等同于全部候选所在的盘。没有执行数学程序。

## 1. 一个带准确分母与复界的有理隐函数引理

设 $\Phi=(\Phi_1,\ldots,\Phi_h)\in\mathbf Q[t,Y_1,\ldots,Y_h]^h$ 满足

$$
\Phi(0,0)=0,\qquad \partial_Y\Phi(0,0)=0.
\tag{1186.1}
$$

其唯一形式不动点记为

$$
Y(t)=\Phi(t,Y(t))=\sum_{r\ge1}Y_rt^r\in t\mathbf Q[[t]]^h.
\tag{1186.2}
$$

取整数 $D,A\ge1$，其中 $D$ 清除全部 $\Phi_i$ 的有理系数分母，$A$ 不小于这些多项式全部系数绝对值的总和。置

$$
\mathcal C=64A^2.
\tag{1186.3}
$$

则对每个 $r\ge1$，

$$
\boxed{\quad D^{2r-1}Y_r\in\mathbf Z^h,
\qquad \|Y_r\|_\infty\le\mathcal C^r.\quad}
\tag{1186.4}
$$

### 1.1 分母的完整归纳

每个出现的单项式 $c\,t^aY^\alpha$ 不是常数，亦不是 $a=0,|\alpha|=1$。若 $|\alpha|=s\ge1$，它对 $t^r$ 的每个贡献由 $s$ 个正阶 $r_1,\ldots,r_s$ 构成，且

$$
\sum r_i=r-a.
$$

这些阶数都严格小于 $r$。归纳假设使该乘积的分母整除

$$
D^{\sum_i(2r_i-1)}=D^{2(r-a)-s}.
$$

再乘 $c$，分母至多为 $D^{1+2(r-a)-s}$；而

$$
1+2(r-a)-s\le2r-1
\quad\Longleftrightarrow\quad 2a+s\ge2,
$$

对全部允许项成立。$s=0$ 时只在 $a=r\ge1$ 贡献一个原系数，分母至多为 $D\mid D^{2r-1}$。这也支付 $r=1$ 的开始项。所有求和项使用同一分母，故没有额外的组合分母。

等价地，每个系数的根树展开至多有 $2r-1$ 个系数节点；这里的归纳已经证明这个计数所需的完整边界，未省掉 $tY$ 或纯高次 $t$ 项。

### 1.2 一个与变量数无关的复解析界

令

$$
\rho=\frac1{64A^2},\qquad s=\frac1{8A},\qquad
u=\rho+s\le\frac9{64A}.
\tag{1186.5}
$$

在 $|t|\le\rho,\|Y\|_\infty\le s$ 上，唯一可能的一次项是 $t$。其余项总次数至少二，全部系数绝对值总和至多为 $A$，故

$$
\|\Phi(t,Y)\|_\infty\le A\rho+Au^2
\le\frac{145}{4096A}<\frac1{8A}=s.
\tag{1186.6}
$$

对总次数 $d\ge2$ 的单项式，关于 $Y$ 的导数行和至多为其系数绝对值乘 $d u^{d-1}$。因为 $u\le9/64$，有 $d u^{d-1}\le2u$ 对全部 $d\ge2$ 成立。于是

$$
\|\partial_Y\Phi(t,Y)\|_{\infty\to\infty}
\le2Au\le\frac9{32}<1.
\tag{1186.7}
$$

从零迭代在这个闭盘上一致收敛，给全纯解，其 Taylor 级数就是 (1186.2)。Cauchy 系数估计给

$$
\|Y_r\|_\infty\le s\rho^{-r}\le(64A^2)^r.
$$

这证明 (1186.4)。仅有理方程及全部系数进入 $A,D$；没有选择一个未知的复收敛半径。

## 2. 将原全部拉回微分放进同一个有限系统

保持原 $t=b-1$。在有理光滑点 $c_1$ 周围选择有限 affine 方程

$$
F(t,Z)=0,\qquad F(0,0)=0,\qquad
J=\partial_ZF(0,0)\in\operatorname{GL}_d(\mathbf Q).
\tag{1186.8}
$$

这里 $Z$ 已平移使其原点值为零。光滑性和 $dt(c_1)\ne0$ 保证可以选取这样的局部完整交方程；选定 Jacobian minor 与原 affine open 共同确定经过 $c_1$ 的原分支。其它全局分支不进入这个形式解。

令 $L_1,\ldots,L_n$ 为 R1182 的原有理 Néron Lie 基，$\omega_i$ 为其对偶整不变微分。原 Abel 映射 $f_C(x)=q_C[x-c_1]$ 给

$$
f_C^*\omega_i=\varphi_i(t,Z(t))\,dt,
\qquad \varphi_i=\frac{P_i(t,Z)}{Q_i(t,Z)},
\quad Q_i(0,0)\ne0.
\tag{1186.9}
$$

这些有理函数可从原映射和微分的有限方程取得。因为 $t$ 是局部参数且 $f_C^*\omega_i$ 正则，其系数在 $c_1$ 正则，故可以选取所写的非零分母。若原公式含 $dZ$，由 (1186.8) 的 Jacobian 逆消去，仍是相同类型的有理函数。

置 $v_{i,0}=\varphi_i(0,0)\in\mathbf Q$，再加变量

$$
W_i=\varphi_i-v_{i,0}
$$

及方程

$$
(W_i+v_{i,0})Q_i(t,Z)-P_i(t,Z)=0.
\tag{1186.10}
$$

完整系统在 $(Z,W)$ 中的 Jacobian 为可逆块三角矩阵，对角块是 $J$ 和 $\operatorname{diag}(Q_i(0,0))$。用它的有理逆归一化，便成为 §1 的有限多项式系统

$$
Y=\Phi(t,Y),\qquad Y=(Z,W),
\tag{1186.11}
$$

满足 (1186.1)。

现在选 $D$ 为全部归一化系数及全部 $v_{i,0}$ 的共同正整数分母，选整数 $A\ge1$ 同时大于等于归一化系数绝对值总和及所有 $|v_{i,0}|$。这都是从原有限方程作有理运算得到的具体数；包括 Jacobian 逆、原商映射和 Néron 基的实际尺度。

写

$$
\varphi_i(t,Z(t))=\sum_{k\ge0}v_{i,k}t^k.
\tag{1186.12}
$$

由 §1，$k\ge1$ 时 $D^{2k-1}v_{i,k}$ 为整数，且 $|v_{i,k}|\le\mathcal C^k$；$k=0$ 时 $Dv_{i,0}$ 为整数且 $|v_{i,0}|\le A$。这给原全部微分的共同证书，而非先抽一个未知的非零微分。

## 3. 原 $p^3$ 参数中全部 Abel jet 的高度

使用 [R1184](R1184-original-uniform-cubic-CM-disc-and-Neron-integrality.md) 已成的同一完整图册

$$
t=p^3w,\qquad
U^{(3)}(w)=\log_p f_C(x(w))
=\sum_{r\ge1}U_r^{(3)}w^r.
\tag{1186.13}
$$

在原基 $L_i$ 中，形式微分和零常数项给准确式

$$
U_{r,i}^{(3)}=\frac{p^{3r}}r\,v_{i,r-1}.
\tag{1186.14}
$$

置

$$
E_r=rD^{2r-1}.
\tag{1186.15}
$$

则对全部 $r\ge1$，

$$
\boxed{\quad
E_rU_r^{(3)}\in\mathbf Z^n,\qquad
\|E_rU_r^{(3)}\|_\infty
\le D^{2r-1}p^{3r}\mathcal C^r.
\quad}
\tag{1186.16}
$$

对于 $r=1$，这是原常数 $v_{i,0}$ 的共同分母；对于 $r\ge2$，所需的实际微分分母只有 $D^{2r-3}$，(1186.15) 使用了一个共同的安全上界。注意积分分母 $r$ 被完整计入，$p^{3r}$ 也由原参数实际导数产生，未按 $p^3$ 错计。

因为 $p^{3r}\mathcal C^r\ge r$，若把有理向量的 affine 高度定义为 $(1,U_{r,1}^{(3)},\ldots,U_{r,n}^{(3)})$ 的绝对对数射影高度，则

$$
h_{\rm aff}(U_r^{(3)})
\le (2r-1)\log D+3r\log p+r\log\mathcal C.
\tag{1186.17}
$$

这是从原有限模型来的线性阶数界。它与 R1184 的 $p$ 处整性 $rU_r^{(3)}\in\Lambda$ 同时成立；(1186.15) 并不表示这些多余的 $p$ 分母在原向量中真实出现。

## 4. 同一两列线性形式的高度，不把 $p$ 进系数送入 FP

保持 R1182 的原有理非退化交错形式 $\Omega$。在 $L_i$ 中写其有理矩阵为 $M_\Omega$，取正整数 $D_\Omega$ 清除全部有理分母，并置

$$
\Xi=D_\Omega M_\Omega\in\operatorname{Mat}_n(\mathbf Z),\qquad
S_\Omega=\max\left\{1,\max_i\sum_j|\Xi_{ij}|\right\}.
\tag{1186.18}
$$

若原首非零阶为 $m$，给 FP 的有理线性形式仍是

$$
\ell_m(v)=\Omega(v,U_m^{(3)}),
\tag{1186.19}
$$

而不是系数为 $p$ 进对数的 $\lambda_{\beta'}$。其一个整数系数向量为

$$
c_m^{\rm raw}=D_\Omega E_m\,M_\Omega U_m^{(3)}
=E_m\Xi U_m^{(3)}\in\mathbf Z^n.
\tag{1186.20}
$$

因此

$$
\|c_m^{\rm raw}\|_\infty
\le S_\Omega D^{2m-1}p^{3m}\mathcal C^m.
\tag{1186.21}
$$

这里 $E_m$ 指本篇 (1186.15) 的安全共同分母。为避免与 R1182 的最小分母混淆，记后者为 $E_m^{\min}$：即清除 $\ell_m$ 的全部系数分母的最小正整数。它整除 $D_\Omega E_m$，所以原 FP 的整数系数向量

$$
c_m=E_m^{\min}\ell_m
$$

是 (1186.20) 乘一个不大于一的正有理数；它的系数绝对值不超过 (1186.21)。故 R1182 的参数 $\mathsf b=\log\max\{3,\|c_m\|_\infty\}$ 满足

$$
\boxed{\quad
\mathsf b\le
\log S_\Omega+(2m-1)\log D+3m\log p+m\log\mathcal C.
\quad}
\tag{1186.22}
$$

右边至少为 $\log3$。此外仍保留 R1182 的原整性：$v_p(E_m^{\min})\le v_p(m)$。本篇多余的全局分母不被拿来替代这个较强的实际 $p$ 分母结论。

## 5. 消去未知首阶，事前选择 FP 的全部高度参数

令 $g=g(X_1)$、$n=\dim C$。原 $q_C^*H^0(C,\Omega^1)$ 是 $n$ 维子空间，故已成的原 Clifford 界给

$$
1\le m\le M_X:=2(g-n)+1.
\tag{1186.23}
$$

这里不另宣 $m=1$，也不把总 CM 商的饱和性搬给原 $C$。因为 (1186.22) 对阶数单调递增，可在读取实际首阶之前，选取一个可计算有理上界

$$
\mathsf b_*\ge
\max\left\{\log3,
\log S_\Omega+(2M_X-1)\log D
+3M_X\log p+M_X\log(64A^2)\right\}.
\tag{1186.24}
$$

例如使用整数系数的二进制位数给各对数的有理严格上界即可，不需判定某个实数是否恰为整数。

同时用 [R1185](R1185-original-CM-point-height-and-quotient-cost.md) 的原实际商证书取 $\mathsf h_*\ge\log\max\{3,H(\beta')\}$。若当前 FP 嵌入采用该文的对称完整嵌入，可以取

$$
\mathsf h_*\ge
\max\left\{\log3,
18M^2K\frac g{g-1}H_{\rm br}(3p(p-1))
+\frac{E_{\mathcal L}}3\right\};
\tag{1186.25}
$$

坚持原嵌入时则用 R1185 (1185.33) 的实际比较矩阵 $c_T$。$M$ 仍是原 $\beta$ 进入实际 FP 指数小球的倍数，不与 $M_X$ 混用。

保持原嵌入、Lie 基的有效常数 $c_{\rm FP}$ 和 R1182 的 $W_L$。选择一个可计算整数 $B_*\ge1$，严格大于

$$
c_{\rm FP}W_L^{n+3}\,
\mathsf b_*\mathsf h_*^n
(\log\mathsf b_*+\log\mathsf h_*)^{n+3}.
\tag{1186.26}
$$

所有量均有原有限模型、已成终止算法或已刊有效界的来源。R1182 的原有理超平面几何半稳定及同一点解析子群论给

$$
0\ne a_m^{(3)}=\ell_m(\log_p\beta'),\qquad
v_p(a_m^{(3)})<B_*.
\tag{1186.27}
$$

单调代入合法，因为 $\mathsf b,\mathsf h\ge\log3>1$。没有用未知的 $p$ 进系数高度，也没有先假设实际首项为单位。

## 6. 完整深盘和预定对数精度

置

$$
L_X=\left\lceil\log_p(M_X+1)\right\rceil,\qquad
N_*=B_*+\left\lfloor\log_p M_X\right\rfloor.
\tag{1186.28}
$$

R1184 的全部整尾和 R1182 的严格首尾比较给

$$
\boxed{\quad
v_p(b-1)\ge3+B_*+L_X
\quad\Longrightarrow\quad
x=c_1
\quad\text{对原分支上的 }x\in X_1(\mathbf Q).
\quad}
\tag{1186.29}
$$

这里 $L_X\ge\lceil\log_p(m+1)\rceil$，所以不需知道 $m$ 就可选这个闭盘。若写 $a_{m+k}$ 为同一原消去函数的尾系数，则 $v_p(a_{m+k})\ge-v_p(m+k)$；对盘中 $w$ 的估值逐项比较，尾项严格大于非零首项，整个收敛尾都被控制。

令 $h_\lambda$ 为 R1182 的原消去泛函系数共同赋值。原 $mU_m^{(3)}\in\Lambda$ 给

$$
h_\lambda\le v_p(a_m^{(3)})+v_p(m)
<B_*+\lfloor\log_p M_X\rfloor=N_*.
\tag{1186.30}
$$

因而在读取实际首项之前，以下有限精度已经足够：

- 读取原 $\log_p\beta'$ 到 $p^{N_*}$，即可确定 $h_\lambda$；
- 原 $\beta'$ 的实际 Néron 形式坐标在 $p\mathbf Z_p^n$ 中，R1182 §9 的径向对数截到总次数 $2N_*$，其余项均不影响该精度；
- 原 rational jet 只需读到 $M_X$，就能找到真正的 $m$，并由原整数线性形式读出准确的 $e_m^{(3)}$，然后使用 R1184 (1184.29) 或 (1184.30) 的更短盘。

这些是事前确定的界和终止证明，本文没有执行该读取。尤其没有将一个以“继续算到非零”为停止条件的无界循环称为预定精度。

## 7. 新支付的量与实际尚待控制的量

本篇已把未知的原首项阶数和其单独系数高度，替换成明确的 $M_X,D,A,S_\Omega$。$D,A$ 来自原曲线、原商、原 Néron 基及全部拉回微分的一张有限图册；$S_\Omega$ 来自原有理交错形式。R1184 固定图册缩盘指数为三，R1185 给同一 $\beta'$ 的点高度。本篇把三者合在同一原数据上，不另选 MW 点、曲线或对数线。

继续需要控制这些实际模型参数、FP 的原向量场常数及进入指数域的倍数随 $p$ 的增长，并比较 (1186.29) 与真实候选的深度。一个只依给定模型可计算的半径，尚不构成 Serre 统一性，更不处理 R1003 所保留的全部全局分支或变化 $X_d$。

## 来源

- [R1011](R1011-original-nonCM-half-rank-quotient-and-rational-CM-jet-transversality.md) 与 [R1182](R1182-original-effective-Abel-jet-valuation-and-CM-disc-radius.md)：原半秩商、同一两列泛函、实际 FP 前提、原 Clifford 首阶界及全尾比较。
- [R1184](R1184-original-uniform-cubic-CM-disc-and-Neron-integrality.md)：经过指定 $c_1$ 的完整 $t=p^3w$ 图册和任意原商的 Néron 整尾。
- [R1185](R1185-original-CM-point-height-and-quotient-cost.md)：同一原 CM 点差的高度与原商极化/倍二坐标证书。

§1 的分母与复界、§§2–4 的完整微分系统和全部高度因子在本文纸面自证；没有新增文献性猜想或数值窗口。
