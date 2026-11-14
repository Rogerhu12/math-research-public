# R69：高阶临界组合、次数受控矩阵与实际 Gevrey 幂界

日期：2026-11-12（UTC）。经主会话逐段核验。**状态：以下两个充分条件均已证明；没有解决全部独立 $o(j^{-p})$ 次主尾的高阶取消。**

本条接续 [R67](R67-independent-subleading-critical-combinations.md)。这里分开处理两个实质不同的情形：

1. 主变量和横向变量的全部低总次数确实消失。这时 Weierstrass 多项式有受控的横向次数，伴随矩阵的指数仍是主尺度上的 $e^{o(M)}$。
2. 独立横向的一次项没有消失，但它形成一个已知 BW 负尾。利用真实算子的 Gevrey 幂界，原主变量的二阶及更高余项在这个新尺度上可以忽略。

第一条不能删去“低总次数确实消失”的假设；R67 §8 已给出删去它后的实际矩阵增长反例。第二条不要求各对数是同一个算子的解析函数，但需要对实际合成的横向尾有一个可验证的负 BW 条件。

## 1. 共同背景与记号

使用 R60–R61 的真实 $A,N_j,E_j,A_k$。特别地，
$$
\|N_j-E_j\|=\eta_j,\qquad
\eta_j\le e^{-770\,16^j},\qquad
N_j^{[k]}=A_k^{2^j}/W_{2^j},\qquad
A_k^{2^k}=0,
$$
并有
$$
\|N_j-N_j^{[k]}\|=a_k/a_j\quad(j<k).
$$

固定 $1<p\le12/5$，记 $\theta_j=(j+2)^{-p}$。取基准对数
$$
L=\sum_j[\log(I+N_j)-\log(I+(1-\theta_j)N_j)].
\tag{1.1}
$$
R61 给它的单射稠密性和
$$
\left\|L-G_k-\sum_{j\ge k}\theta_jE_j\right\|
\le C\eta_{k-1},\qquad
G_k^{2^k}=0,\quad\sup_k\|G_k\|<\infty.
\tag{1.2}
$$

各实际对数为
$$
L_i=\psi_i(A)+\sum_j[
\log(I+s_{i,j}N_j)-\log(I+t_{i,j}N_j)],
\tag{1.3}
$$
其中底参数共同有界、$\psi_i$ 是零常数标量解析芽，并且
$$
s_{i,j}-t_{i,j}=c_i \theta_j+\epsilon_{i,j},
\qquad\epsilon_{i,j}=o(\theta_j).
\tag{1.4}
$$
令 $R_i=L_i-c_iL$。所有算子都在 $\mathcal A$ 中、彼此交换、拟幂零。

以下“正算子”始终指函数格正算子，而非自伴正算子。R67 §§2–4 已逐项构造正的 $B\in\mathcal A$，使
$$
|Af|\le B|f|,\quad |R_if|\le B|f|,
$$
且
$$
\left\|B-K_k-\sum_{j\ge k}b_jE_j\right\|
\le C\eta_{k-1},\qquad
K_k^{2^k}=0,\quad\sup_k\|K_k\|<\infty,
\quad b_j=o((j+2)^{-p}).
\tag{1.5}
$$
其关键增长及正范数级数界为
$$
\sup_{|t|\le T_0M^p}\log\|e^{|t|B}\|=o(M),
\tag{1.6}
$$
$$
\sum_{n\ge0}\frac{s^n}{n!}\|B^n\|
\le2\|e^{2sB}\|\qquad(s\ge0).
\tag{1.7}
$$
(1.7) 来自逐项正序
$(2s)^nB^n/n!\le e^{2sB}$，不要求把某个有界正算子当作乘法算子。

所有有限维解析芽都按绝对范数收敛的级数作演算。具体地，有限个交换拟幂零算子 $Y_\ell$ 对每个 $\varepsilon>0$ 满足
$\|Y_\ell^n\|\le C_{\ell,\varepsilon}\varepsilon^n$；结合解析芽的 Cauchy 系数界即可验证绝对收敛及代数恒等式。

## 2. Weierstrass 系数的真正次数约束

记横向变量 $y=(y_1,\ldots,y_s)$，它们最终将取为 $A,R_i$ 的有限线性组合；仍可由扩大常数后的 (1.5) 型正算子支配。

**引理 2.1。** 设标量解析芽 $F(w,y)$ 满足：

- $F(w,0)$ 在 $w=0$ 的零点阶恰为 $r\ge1$；
- $F$ 的全部总次数小于 $r$ 的 Taylor 项均为零。

作通常的 Weierstrass 分解
$$
F(w,y)=U(w,y)P(w,y),\qquad U(0)\ne0,
$$
$$
P(w,y)=w^r+\sum_{j=0}^{r-1}b_j(y)w^j.
\tag{2.1}
$$
则
$$
\boxed{\operatorname{ord}_y b_j\ge r-j\quad(0\le j<r).}
\tag{2.2}
$$

**证明。** 单位 $U$ 不改变非零形式幂级数的最低总次数：若 $P_d$ 是 $P$ 的最低非零齐次项，则 $UP$ 的最低齐次项恰为 $U(0)P_d$。因此 $\operatorname{ord}_{w,y}P=\operatorname{ord}_{w,y}F\ge r$。$P$ 含有系数一的 $w^r$，所以该阶其实为 $r$。逐个查看 $b_j(y)w^j$ 的单项式，得到 (2.2)。不存在跨不同 $w$ 次数的相消。证毕。

这里的总次数假设必须是在已知的实际线性关系消去之后，对所选独立形式变量成立。不能仅因沿直线 $y=0$ 有 $r$ 阶零点就声称 (2.2)。

## 3. 伴随矩阵的路径次数与指数界

把 $y$ 代入交换实际算子 $Y=(Y_1,\ldots,Y_s)$，均满足
$$
|Y_\ell f|\le B|f|.
\tag{3.1}
$$
令 $C=C(Y)$ 为 $r\times r$ 伴随矩阵，行列编号为 $0,\ldots,r-1$：
$$
C_{i,i+1}=I\quad(0\le i<r-1),\qquad
C_{r-1,j}=-b_j(Y),
$$
其余条目为零。

**引理 3.1。** 若 (2.2) 成立，则存在固定常数 $K,C_0$，使
$$
\boxed{\|C^n\|\le K C_0^n\|B^{n-r+1}\|
\qquad(n\ge r-1).}
\tag{3.2}
$$
从而
$$
\boxed{\|e^{tC}\|
\le K'(1+|t|^{r-1})\|e^{2C_0|t|B}\|
\qquad(t\in\mathbb C).}
\tag{3.3}
$$
特别地，$|t|\le T_0M^p$ 时，$\log\|e^{tC}\|=o(M)$。

**证明。** 逐项取 $b_j$ 的绝对 Taylor 系数，并把所有横向变量置为同一个标量 $x$。得到非负系数芽
$$
\phi_j(x)=x^{r-j}g_j(x),
$$
其中 $g_j$ 也是非负系数解析芽，且
$$
|b_j(Y)f|\le\phi_j(B)|f|.
$$
用这些正算子及上对角的 $I$ 构造正矩阵 $\mathcal C(B)$。则逐坐标有
$$
|C^nv|\le \mathcal C(B)^n|v|.
\tag{3.4}
$$

每条矩阵路径从列 $\ell$ 到行 $i$，若取一条上对角边，其 $B$ 次数为零，恰等于 $1+\text{行}-\text{列}$；若取末行第 $j$ 条边，其已提取的 $B$ 次数为 $r-j=1+(r-1)-j$。因此一条长度 $n$、从列 $\ell$ 到行 $i$ 的路径，其提取出的 $B$ 次数精确为
$$
\sum_{\text{边}}(1+\text{行}-\text{列})
=n+i-\ell.
\tag{3.5}
$$
这个计算使用实际路径，不是只对矩阵的形式谱作判断。

所有余下的 $g_j(B)$ 都与 $B$ 交换。令
$$
G=\max(1,\max_j\|g_j(B)\|).
$$
长度 $n$ 的路径至多 $r^{n-1}$ 条，每条余下因子的范数不超过 $G^n$。故
$$
\|(C^n)_{i\ell}\|
\le r^{n-1}G^n\|B^{n+i-\ell}\|
$$
（若 $n+i-\ell<0$，路径不存在，该条目为零）。当 $n\ge r-1$，全部指数非负且落在
$[n-r+1,n+r-1]$。于是
$$
\|B^{n+i-\ell}\|
\le \max(1,\|B\|)^{2r-2}\|B^{n-r+1}\|.
$$
再用一个 $r$ 倍条目范数上界控制整体矩阵，得到 (3.2)。

在指数级数中先保留 $n<r-1$ 的有限项，其范数至多一个次数 $r-2$ 的固定多项式。对余下各项令 $q=n-r+1$，由 (3.2) 得
$$
\begin{aligned}
\sum_{n\ge r-1}\frac{|t|^n}{n!}\|C^n\|
&\le K(C_0|t|)^{r-1}
\sum_{q\ge0}\frac{(C_0|t|)^q}{(q+r-1)!}\|B^q\|\\
&\le2K(C_0|t|)^{r-1}\|e^{2C_0|t|B}\|.
\end{aligned}
$$
合并有限项并使用 $\|e^{sB}\|\ge1$，即得 (3.3)；$r=1$ 直接使用后一式。最后代入 (1.6)，多项式前因子只贡献 $O(\log M)$。证毕。

这个证明没有假设存在有界的 $B^{-1}$，也没有用非法的对角相似变换 $\operatorname{diag}(I,B,\ldots)$。

## 4. 低总次数消失时的高阶临界定理

**定理 4.1。** 在第 1 节的实际模型中，设 $Y$ 由 $A,R_i$ 的有限线性组合构成，$F(w,y)$ 满足引理 2.1。则
$$
\boxed{F(L,Y)\text{ 单射且值域稠密。}}
\tag{4.1}
$$

**证明。** 单位 $U(L,Y)$ 可逆，所以只需处理 $P(L,Y)$。若
$P(L,Y)f=0$，令
$$
\mathbf f=(f,Lf,\ldots,L^{r-1}f)\in H^r.
$$
伴随关系给
$$
(LI_r-C(Y))\mathbf f=0.
$$
$L$ 与每个矩阵条目交换，故
$$
e^{tL}\mathbf f=e^{tC(Y)}\mathbf f.
\tag{4.2}
$$

取 R61 的负 BW 区间：$p\le2$ 用 $[1,20]$，$p>2$ 用 $[1/10,30]$。置 $M=m+2$、$k=\lfloor(3/4)\log_2M\rfloor$、$t=uM^p$，并把 (1.2) 写为
$$
T_k=H_{k,m}+C_m,\qquad
H_{k,m}=G_k+\sum_{k\le j<m}\theta_jE_j,\qquad
C_m=\sum_{j\ge m}\theta_jE_j.
$$
则逐坐标有
$$
e^{tH_{k,m}}\mathbf f-
e^{-tC_m}e^{tC(Y)}\mathbf f
=e^{-tC_m}(e^{tT_k}-e^{tL})\mathbf f.
\tag{4.3}
$$
右侧范数至多
$$
\exp[-cM^3+O(M^p+\log M)]\|\mathbf f\|.
\tag{4.4}
$$
没有假设 $C(Y)$ 与近似的 $H_{k,m},C_m$ 交换。

对每个坐标向量 $e_\ell$，取多项式
$$
p_{m,\ell}(u)=
\langle e^{uM^pH_{k,m}}\mathbf f,\ 1\otimes e_\ell\rangle.
$$
它的次数至多 $M+M^{3/4}$，常数项为该坐标的均值。由引理 3.1 及真实尾范数公式，
$$
|p_{m,\ell}(u)|
\le\|\mathbf f\|\exp[Mh_p(u)+o(M)].
$$
尾范数下界 $e^{-CM}$ 使 (4.4) 可吸收。BW 的严格负常数迫每个坐标的均值为零。特别地，对任意 $f\in\ker P(L,Y)$ 都有 $\langle f,1\rangle=0$。

该核在 $A$ 下不变，因为 $P(L,Y)\in\mathcal A$。$1$ 对 $A^*$ 循环，所以核为零。最后 $F(L,Y)\in\mathcal A$ 的复对称性给稠密值域。证毕。

### 4.1 对乘积组合的准确适用范围

令
$$
X=\sum_i\alpha_i e^{-c_iL-R_i}.
$$
若在实际已知的线性关系中选取横向变量 $Y$ 后，解析芽
$$
F(w,y)=\sum_i\alpha_i e^{-c_iw-r_i(y)}
$$
的低于 $r$ 的全部总次数消失，且 $\sum_i\alpha_i c_i^r\ne0$，则定理 4.1 适用。其中 $r_i(y)$ 是表达实际 $R_i$ 的线性式。

例如 $r=2$ 时，充分条件为
$$
\sum_i\alpha_i=0,\qquad
\sum_i\alpha_ic_i=0,\qquad
\sum_i\alpha_iR_i=0
$$
作为真实算子恒等式，并且 $\sum_i\alpha_ic_i^2\ne0$。选择一个非零 $\alpha_i$ 消去对应的 $R_i$ 后，横向一次项的确逐系数消失，不是只在某条主方向上消失。

对恰好三个非零系数，若上述真实线性关系成立，三个对数的差其实仿射共线；此时常可归约为 R62 的单一对数指数和。因而不能把这个三项特例冒充新的独立方向结果。一般多项及高维横向变量的定理不依赖这种归约。

## 5. 真实正主算子的 Gevrey 幂界

第二条路线允许横向一次项实际存在。先证明需要的全局幂范数。

**引理 5.1。** 设 $1<p<4$，正算子 $B_0\in\mathcal A$ 具有
$$
\left\|B_0-K_k-\sum_{j\ge k}\beta_jE_j\right\|
\le C\eta_{k-1},\qquad
K_k^{2^k}=0,\quad\sup_k\|K_k\|<\infty,
$$
其中 $0\le\beta_j\le C_1(j+2)^{-p}$。则存在常数 $C_2,C_3$，使
$$
\|e^{tB_0}\|\le C_2 e^{C_3t^{1/p}}\quad(t\ge0),
\tag{5.1}
$$
并有
$$
\boxed{\|B_0^n\|\le C_4^n(n!)^{1-p}\quad(n\ge1).}
\tag{5.2}
$$

**证明。** 取固定 $\gamma$ 满足 $1/4<\gamma<1/p$；这正是使用 $p<4$ 的地方。对大 $t$ 令 $k=\lfloor\gamma\log_2t\rfloor$。低位指数的范数对数至多
$$
O(2^k\log(2+t))=O(t^\gamma\log t)=o(t^{1/p}).
$$
尾部的乘积范数用递减和积分比较得
$$
\sum_{j\ge k}\log(1+t\beta_j)
\le C t^{1/p}\int_0^\infty\log(1+x^{-p})\,dx
=O(t^{1/p}).
$$
Duhamel 的真实误差至多
$$
Ct\eta_{k-1}e^{C't}
\le\exp[-c t^{4\gamma}+O(t+\log t)],
$$
它趋于零，因为 $4\gamma>1$。调整有界时间段的常数即得 (5.1)。

正性给 $t^n\|B_0^n\|/n!\le\|e^{tB_0}\|$。在 (5.1) 中取
$t=(pn/C_3)^p$，得到
$$
\|B_0^n\|
\le C_2 n!\left(\frac{eC_3}{pn}\right)^{pn}
\le C_2 C_5^n(n!)^{1-p}.
$$
最后一步用 $(n!)^p\le n^{pn}$。把固定 $C_2$ 吸收进 $C_4^n$，即得 (5.2)。证毕。

**引理 5.2。** 若有限个交换实际算子 $Y_\ell$ 由 $B_0$ 逐点支配，且解析芽 $\Phi(y)$ 的总次数至少为 $d\ge1$，则
$$
Z=\Phi(Y)
$$
满足
$$
\boxed{\|e^{tZ}\|
\le \exp\!\left(C_\Phi |t|^{1/[d(p-1)+1]}\right)
\quad(t\in\mathbb C)}
\tag{5.3}
$$
（可按需要在右侧加一个固定常数因子）。

**证明。** 取绝对系数单变量芽 $\phi(x)=x^dg(x)$。与 R67 的正支配证明相同，
$$
\|Z^n\|\le\|\phi(B_0)^n\|
\le\|g(B_0)\|^n\|B_0^{dn}\|.
$$
由 (5.2) 和 $(dn)!\ge(n!)^d$，
$$
\|Z^n\|\le C^n(n!)^{-d(p-1)}.
$$
设 $s=d(p-1)+1>1$，则
$$
\|e^{tZ}\|
\le\sum_{n\ge0}\frac{(C|t|)^n}{(n!)^s}
\le
\left(\sum_{n\ge0}\frac{(C|t|)^{n/s}}{n!}\right)^s
=e^{s(C|t|)^{1/s}}.
$$
中间不等式是非负数列的 $\ell^s$ 范数不超过其 $\ell^1$ 范数。证毕。

在 (1.3)—(1.4) 的情形，存在这种共同的 $B_0$ 同时支配 $A,L_1,\ldots,L_r$：复制 R67 的绝对系数构造，但保留全部一阶系数的绝对值；所得 $\beta_j=O(j^{-p})$，高次项及截断误差仍为 $O(\eta_{k-1})$。

## 6. 有效横向对数的 BW 传递准则

这里先给一个不依赖具体渐近形式的准确版本。

设 $S\in\mathcal A$ 有真实近似
$$
\left\|S-S_k-\sum_{j\ge k}\sigma_jE_j\right\|
\le C\eta_{k-1},\qquad
S_k^{2^k}=0,\quad\sup_k\|S_k\|<\infty.
\tag{6.1}
$$
给定固定 $0<a<b$，令 $\nu_{a,b}$ 为 R60 的 BW 谐测，$g_{a,b}$ 为其常数。设存在非零复尺度 $\tau_m$、实连续函数 $h$ 和 $C>0$，对 $M=m+2$ 和 $u\in[a,b]$ 统一有
$$
\log\left\|\exp\left[-\overline{\tau_m u}
\left(\sum_{j\ge m}\sigma_jE_j\right)^*\right]1\right\|
\le Mh(u)+o(M),
\tag{6.2}
$$
$$
\left\|\exp\left[-\overline{\tau_m u}
\left(\sum_{j\ge m}\sigma_jE_j\right)^*\right]1\right\|
\ge e^{-CM},
\tag{6.3}
$$
以及
$$
g_{a,b}+\int_a^b h(u)\,d\nu_{a,b}(u)<0.
\tag{6.4}
$$
假设
$$
|\tau_m|=o(M^3).
\tag{6.5}
$$

**引理 6.1。** 若 $Z\in\mathcal A$ 与 $S$ 交换，且
$$
\sup_{u\in[a,b]}\log\|e^{\tau_m uZ}\|=o(M),
\tag{6.6}
$$
则 $S-Z$ 单射且值域稠密。

**证明。** 对核向量 $f$ 有 $e^{tS}f=e^{tZ}f$。取
$k=\lfloor(3/4)\log_2M\rfloor$，将 (6.1) 写成低位 $H_{k,m}$ 与尾 $C_m$。逐项重复 R67 的恒等式
$$
e^{tH_{k,m}}f-e^{-tC_m}e^{tZ}f
=e^{-tC_m}(e^{t(S_k+\sum_{j\ge k}\sigma_jE_j)}-e^{tS})f.
$$
由 (6.5)，右侧是 $\exp[-cM^3+o(M^3)]\|f\|$。标量多项式
$\langle e^{\tau_m uH_{k,m}}f,1\rangle$ 的次数至多 $M+M^{3/4}$。用 (6.2)、(6.3)、(6.6) 得边界
$\|f\|\exp[Mh(u)+o(M)]$。BW 和 (6.4) 迫核均值为零；$A^*$ 循环与复对称性完成证明。证毕。

若 $Z$ 满足引理 5.2，则 (6.6) 的一个直接充分条件为
$$
\boxed{|\tau_m|^{1/[d(p-1)+1]}=o(M).}
\tag{6.7}
$$

## 7. 真正双重取消但横向尾主导的定理

对 (1.3) 令 $a_i(z)$ 为有限个实际一元解析芽，$\alpha_i=a_i(0)$。考虑
$$
X=\sum_i a_i(A)e^{-L_i}.
\tag{7.1}
$$
假设
$$
\sum_i\alpha_i=0,\qquad
\sum_i\alpha_ic_i=0.
\tag{7.2}
$$
定义实际有效横向对数
$$
S=\sum_i\alpha_iL_i-\sum_i(a_i(A)-\alpha_i).
\tag{7.3}
$$
其一阶逐位尾恰为
$$
\sigma_j=\sum_i\alpha_i(s_{i,j}-t_{i,j})
=\sum_i\alpha_i\epsilon_{i,j}=o((j+2)^{-p}).
\tag{7.4}
$$

**定理 7.1。** 若这个实际 $S$ 满足第 6 节的负 BW 条件，且
$$
|\tau_m|^{1/(2p-1)}=o(M),
\tag{7.5}
$$
则 $X$ 单射且值域稠密。

**证明。** 精确展开
$$
\begin{aligned}
X&=-S+Z,\\
Z&=\sum_i\bigl[
-(a_i(A)-\alpha_i)L_i
+a_i(A)(e^{-L_i}-I+L_i)\bigr].
\end{aligned}
\tag{7.6}
$$
这里没有截掉任何余项。作为变量 $(A,L_1,\ldots,L_r)$ 的解析芽，$Z$ 的总次数至少为二。由共同正主算子 $B_0$ 和引理 5.2，
$$
\log\|e^{tZ}\|=O(|t|^{1/(2p-1)}).
$$
条件 (7.5) 给 (6.6)。$S$ 与 $Z$ 交换，引理 6.1 适用。乘一个负号不影响单射稠密性。证毕。

还需核实 (6.1)：$S$ 是有限个实际局部对数的线性组合，加上真正的标量解析芽。每个局部的高次系数仍是 $O((j+2)^{-p})$ 乘固定几何系数；即使线性尾发生了更强取消，高次项的原误差仍只需总计为 $O(\eta_{k-1})$。把低位全部在 $A_k$ 上评价并求和，正好得到 (6.1)。因此不曾把高次误差错误地按更小的 $|\sigma_j|$ 控制。

### 7.1 一项容易检查的完整参数范围

若
$$
\sigma_j\sim c(j+2)^{-q},\qquad c\ne0,
$$
其中
$$
\boxed{p<q\le12/5,\qquad q<2p-1,}
\tag{7.7}
$$
则取 $\tau_m=M^q/c$。R61 的同一尾范数证明给 (6.2)—(6.4)，且 $q<3$ 给 (6.5)，$q<2p-1$ 给 (7.5)。故全部这样的双重临界组合均单射稠密。

这里的 $S$ 不必能写成一个局部比值乘积的对数；BW 所需的是 (6.1) 和实际一阶尾。有限个局部对数的线性组合已经逐项验证这两项。

### 7.2 不要求横向尾有固定主系数

R64 的移动归一化同样可以直接代入：对某个 $1<q\le12/5$，存在 $c_m\ne0$，使
$$
\frac{M^{q-1}}{|c_m|}
\sum_{j\ge m}|\sigma_j-c_m(j+2)^{-q}|\to0,
\tag{7.8}
$$
且每个 $\varepsilon>0$ 下最终 $|c_m|^{-1}\le M^\varepsilon$。取
$\tau_m=M^q/c_m$。只要 $q<2p-1$，第 6 节全部条件及 (7.5) 成立。

尤其允许
$$
\sigma_j=(j+2)^{-p}(\log(j+3))^{-\rho+i\theta},
\qquad \rho>0,\ \theta\in\mathbb R.
\tag{7.9}
$$
它确是 $o(j^{-p})$；取 $q=p$，由于 $p<2p-1$，增长条件自动成立。$\theta\ne0$ 时相位无需收敛。

R64 的非零平均相位缺陷判据也能使用：若 $q=2$ 的有效尾满足该判据，而 $p>3/2$，则 $2<2p-1$，因此任意允许的持续小相位偏差、正密度稀疏反号等例子均可作为有效横向尾。仍须同时满足原问题的 $\sigma_j=o(j^{-p})$；例如可取 $3/2<p<2$。

### 7.3 三项确实独立的例子

取主常数 $(c_0,c_1,c_2)=(0,1,2)$、组合系数 $(1,-2,1)$，并取局部对数
$$
L_0=0,\qquad L_1=L,\qquad
L_2=\sum_j[\log(I+N_j)-\log(I+(1-2\theta_j-\varepsilon_j)N_j)].
$$
这里 $\varepsilon_j=\theta_j/\log(j+3)$。所有底参数有界，且
$L_2=2L+R_2$，$R_2$ 具有独立次主尾 $\varepsilon_j$；不要求、也没有使用 $R_2$ 是 $L$ 的解析函数。

此时
$$
X=I-2e^{-L}+e^{-L_2},\qquad
S=L_2-2L,
$$
而 $S$ 的有效尾恰为 $\varepsilon_j$，符合 (7.9)。所以 $X$ 单射且稠密。这个例子正处于 R67 §8 所示的“粗伴随矩阵范数可能超主尺度”区域，但改用真实横向 $S$ 的尺度和二阶余项增长，仍能证明结论。

给定一个共同 R16 锚，局部差选择足够晚的尾并允许任意有限前缀，R61 的实际映射机制把这类算子结论转成相应三乘积组合的循环性。任意有限前缀产生的解析系数应保留在 $a_i(A)$ 中，按 (7.2)—(7.4) 重新计算；不能先把它们无理由当成常数。

## 8. 尚未覆盖的范围

本条没有证明所有满足 (1.4) 的高阶临界组合都单射稠密。主要未覆盖点是：横向一次合成尾 $\sigma_j$ 非零，却既没有第 6 节的可用负 BW 尾结构，也不能通过真实恒等式消去以满足第 2 节的低总次数条件。

特别地，不能从 $\sigma_j=o(j^{-p})$ 单独推导某个固定的渐近幂律或相位条件；也不能从沿 $R=0$ 的 Vandermonde 主阶，推导独立横向低次项消失。若有效横向尺度过慢使 (7.5) 失效，本条的二阶 Gevrey 估计亦不够，须另找更细的核相关控制。

所有结论均为所列算子/向量类的结果，不是该课题 README 所要求的一般 Hilbert ISP 完成证明。

