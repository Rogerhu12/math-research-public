# R215：实际慢 dyadic 符号的平方根整函数界与正常湮灭态的指数柱尾下界

日期：2026-11-13（UTC+8）。作者：normal_states。

状态：以下全部估计有完整证明。本文不证明不存在任意 Haar-normal 湮灭态，不解决慢符号的普遍稠密像或普通 Hilbert 不变子空间问题。改进是把有限柱正常泛函测试的成本控制在 $\exp(Cm)$，而不是把一个 $2^m$ 阶 nilpotent 逆直接作几何级数估计所付的 $\exp(C2^m\log m)$。

## 1. 真实模型输入及量词

记原 Haar 空间为 $H=L^2(\mathbb Z_2,\mu)$，物理张量参考向量为各位的 $(e_0+e_1)/\sqrt2$。取
$$
N_j=A^{2^j}/d_j,\qquad Y_j=N_j(I+N_j)^{-1},\qquad
\eta_j=d_{j+1}/d_j^2.
$$
使用本题已有、带真实进位的恒等式
$$
\|N_j\|\le1,\quad N_j^2=\eta_jN_{j+1},\quad
0<\eta_j\le e^{-770\,16^j},\quad
\|(I+N_j)^{-1}\|<3,
\tag{1.1}
$$
以及物理递推
$$
N_j=E_j+\eta_jE_j^*N_{j+1},\qquad E_j=e_{10}^{(j)}.
\tag{1.2}
$$
所有 $N_j,Y_j$ 两两交换。

逐位任选 $X_j=N_j$ 或 $X_j=Y_j$，并取任意复数行满足
$$
|c_j|\le(j+1)^{-2}.
$$
定义范数收敛的真实算子
$$
T=\sum_{j\ge0}c_jX_j.
\tag{1.3}
$$
零系数、有限子和以及任意删项都包含在量词中。下述整函数及预解式常数同时适用于所有这些选择。

令 $P_m$ 为只依赖低 $m$ 位的有限柱空间投影：
$$
P_m=I_{<m}\otimes P_{\Omega_{\ge m}}.
$$
它是原 $H$ 上的有限秩投影。本文从不把 $P_mXP_m$ 当成对 UHF 或解析代数的乘法同态。

## 2. 真实归一化幂的四次衰减

若 $n=\sum_k n_k2^k$ 为二进展开，反复使用 (1.1) 给
$$
\|N_i^n\|
\le\prod_{k:n_k=1}\prod_{\ell=0}^{k-1}
\eta_{i+\ell}^{2^{k-1-\ell}}.
$$
未出现的空积为1；最后剩下的是不同高位 $N_{i+k}$ 的乘积，其范数至多1。因此
$$
-\log\|N_i^n\|
\ge55\,16^i\bigl(D_4(n)-n\bigr),\qquad
D_4(n)=\sum_{k:n_k=1}16^k.
\tag{2.1}
$$
这里用到准确有限和
$$
770\sum_{\ell=0}^{k-1}2^{k-1-\ell}16^\ell
=55(16^k-2^k).
$$

对全部整数 $n\ge0$ 有
$$
15D_4(n)\ge n^4+14n.
\tag{2.2}
$$
证明可按最高二进位 $a$ 归纳。写 $n=a+x$，$0\le x<a$，其中 $a$ 为2的幂。欲由 $x$ 的结论推出 $n$ 的结论，只需
$$
(a+x)^4-x^4+14a\le15a^4.
$$
左边随 $x$ 增大，在 $x=a-1$ 达到最大值
$$
15a^4-28a^3+18a^2+10a\le15a^4.
$$
最后一个不等式对 $a\ge1$ 成立，因为
$28a^3-18a^2-10a=2a(a-1)(14a+5)\ge0$。
基例 $n=0$ 成立，归纳完成。

所以
$$
\boxed{\|N_i^n\|\le
\exp\!\left[-\frac{11}{3}16^i(n^4-n)\right].}
\tag{2.3}
$$
特别 $n\ge2$ 时，$(11/3)(n^4-n)\ge n^4$，故对两种 $X_i$ 同时有
$$
\boxed{\|X_i^n\|\le3^n e^{-16^i n^4}\quad(n\ge2),
\qquad \|X_i\|\le3.}
\tag{2.4}
$$
对 $Y_i$ 使用 $Y_i^n=N_i^n(I+N_i)^{-n}$ 即可。本节没有把 $N_i$ 替换为纯平方零的 $E_i$。

## 3. 全复平面上的统一整函数界

**定理3.1。** 对 (1.3) 的全部选择和全部 $z\in\mathbb C$，
$$
\boxed{\|e^{zT}\|\le e^{16\sqrt{|z|}}.}
\tag{3.1}
$$

先估计单个因子。置 $u=3|w|$、$a=16^i$、$L=\log_+u$。由 (2.4)，
$$
\|e^{wX_i}\|
\le1+u+\sum_{n\ge2}\exp(nL-an^4).
$$
Young 不等式（或直接最大化四次多项式）给
$$
nL\le\frac a2n^4+a^{-1/3}L^{4/3}.
$$
且
$$
\sum_{n\ge2}e^{-an^4/2}
\le\sum_{n\ge2}e^{-n/2}<1.
$$
所以
$$
\boxed{\|e^{wX_i}\|
\le2(1+u)\exp\!\left(16^{-i/3}(\log_+u)^{4/3}\right).}
\tag{3.2}
$$

现在令 $r=|z|$。$r\le1/3$ 时，由 $\|T\|\le3\sum(j+1)^{-2}<6$，
$$
\|e^{zT}\|\le e^{6r}\le e^{16\sqrt r}.
$$
若 $r\ge1/3$，置
$$
v=\sqrt{3r}\ge1,\qquad m=\lceil v\rceil\le2v.
$$
对低 $m$ 位的每个因子用 (3.2)，对其余因子用普通指数估计。由于全部 $X_i$ 交换，先对有限和有准确乘积公式，最后按范数取极限。低位的线性对数满足
$$
\sum_{i<m}\log\left(1+\frac{v^2}{(i+1)^2}\right)
\le\int_0^\infty\log(1+v^2/x^2)\,dx=\pi v.
\tag{3.3}
$$
积分值可由分部积分直接得到。高位则满足
$$
3r\sum_{i\ge m}(i+1)^{-2}\le\frac{3r}{m}\le v.
\tag{3.4}
$$
最后，$\sum_i16^{-i/3}<2$，而单变量微积分给
$$
\sup_{v\ge1}\frac{(\log v)^{4/3}}v
=\left(\frac4{3e}\right)^{4/3}<\frac12.
$$
故 (3.2) 中额外的对数总和至多
$$
2(2\log v)^{4/3}\le2^{4/3}v.
$$
合并 (3.2)—(3.4)，
$$
\log\|e^{zT}\|
\le(2\log2+\pi+1+2^{4/3})v<9v<16\sqrt r.
$$
最后两步例如使用 $\log2<0.7$、$\pi<22/7$、$2^{4/3}<2.6$、$\sqrt3<7/4$。证明完成。

本证明只用了系数绝对值，因此包括任意相位、全部复 $z$、逐位混用 $N/Y$、任意删项；不是仅沿正实半轴的正算子估计。

## 4. 预解式与有限头的一致版本

对每个 $c>0$，Bochner 范数积分
$$
R_c(T)=\int_0^\infty e^{-ct}e^{-tT}\,dt
$$
收敛。因为
$$
16\sqrt t\le\frac c2t+\frac{128}{c},
$$
所以
$$
\boxed{\|(cI+T)^{-1}\|\le\frac2c e^{128/c}.}
\tag{4.1}
$$
确实，对 $e^{-t(cI+T)}$ 积分其导数，端点 $t=\infty$ 的范数趋于0，得到左右逆恒等式。因此没有预先假定一个形式逆已经有界。

令 $N_i^{[m]}$ 为 (1.2) 在第 $m$ 位截去进位后的低头矩阵，$i<m$，并令 $N_i^{[m]}=0$ 对 $i\ge m$。这些矩阵仍交换，满足 (1.1) 的递推和范数上界，只是最后一项为0。其逆 $I+N_i^{[m]}$ 的范数同样小于3：可由 $N^2=\eta N'$ 写
$$(I+N)^{-1}=(I-N)(I-N^2)^{-1}$$
并使用 $\|N\|\le1$、$\eta\le e^{-770}$。
定义 $Y_i^{[m]}=N_i^{[m]}(I+N_i^{[m]})^{-1}$。
第2—3节的证明原样适用这些有限头矩阵，常数不依赖 $m$。因此 (4.1) 也同时适用于任意有限头慢和。

## 5. 低头测试元素：不把压缩当作乘法

从本节起固定两个具体正慢符号之一：
$$
S=S_N=\sum_{j\ge0}a_jN_j
\quad\text{或}\quad
S=S_Y=\sum_{j\ge0}a_jY_j,
\qquad a_j=(j+1)^{-2}.
$$
统一用 $X_j$ 表示相应选择，置
$$
L_m=\sum_{i<m}a_iX_i,\quad
U_m=\sum_{i\ge m}a_iX_i,\quad
H_m=\sum_{i<m}a_iX_i^{[m]}.
\tag{5.1}
$$
这里将 $H_m$ 在高尾张量恒等后也记为 $H_m$。$U_m$ 精确只作用于高尾；$H_m$ 精确只作用于低头。$L_m$ 同时有低头及真实 carry，因此没有把它写成纯低头算子。

由 (1.2) 展开，
$$
\|N_i-N_i^{[m]}\|\le\prod_{\ell=i}^{m-1}\eta_\ell
\le\eta_{m-1}\quad(i<m).
$$
逆差恒等式又给
$$
\|Y_i-Y_i^{[m]}\|\le9\eta_{m-1}.
$$
所以两种模型同时有
$$
\boxed{\|L_m-H_m\|\le18\eta_{m-1}=:\varepsilon_m.}
\tag{5.2}
$$

定义尾真空标量
$$
c_m=\langle U_m\Omega_{\ge m},\Omega_{\ge m}\rangle.
$$
对 $N$ 模型，由 (1.2) 和真空正性有 $1/2\le\langle N_j1,1\rangle\le1$。对 $Y$ 模型，实际恒等式 $Y_j1=(1-\chi_j)/2$ 给真空期望准确等于 $1/2$。后一等式也可直接把 $(1-\chi_j)/2$ 代入 $(I+N_j)y=N_j1$ 核验。因此对 $m\ge1$，
$$
\boxed{\frac1{2(m+1)}\le c_m\le\frac1m.}
\tag{5.3}
$$
这里只使用 $(m+1)^{-1}\le\sum_{j\ge m}(j+1)^{-2}\le m^{-1}$。

令
$$
R_m=(c_mI+L_m)^{-1},\quad
\widetilde R_m=(c_mI+H_m)^{-1},\quad
D_m=4(m+1)e^{256(m+1)}.
$$
(4.1)、(5.3) 给
$$
\|R_m\|,\|\widetilde R_m\|\le D_m,
\qquad
\|R_m-\widetilde R_m\|\le\varepsilon_mD_m^2.
\tag{5.4}
$$
$R_m$ 属于真实 $\mathcal A=\overline{\mathbb C[I,A]}^{\|\cdot\|}$：上节的逆是 $L_m\in\mathcal A$ 的范数积分，或其真正的收敛 Neumann 逆；不存在形式除法步骤。

置
$$
\boxed{J_m=SR_m\in S\mathcal A,\qquad \|J_m\|\le6D_m.}
\tag{5.5}
$$
由于 $H_m,\widetilde R_m$ 只作用于低头，$U_m$ 只作用于尾，准确张量计算给
$$
P_m(H_m+U_m)\widetilde R_mP_m=P_m.
\tag{5.6}
$$
这是对这些指定张量因子的计算，绝非声称一般压缩保乘法。对真实 $S=L_m+U_m$，使用 (5.2)、(5.4) 分别支付两个误差，得到
$$
\begin{aligned}
\|P_mJ_mP_m-P_m\|
&\le\|S\|\,\|R_m-\widetilde R_m\|
 +\|L_m-H_m\|\,\|\widetilde R_m\|\\
&\le7\varepsilon_mD_m^2
\le126e^{-77016^{m-1}}D_m^2.
\end{aligned}
\tag{5.7}
$$
对全部 $m\ge2$，最后一项小于 $1/4$。例如其对数至多
$$
\log2016+2\log(m+1)+512(m+1)-77016^{m-1};
$$
在 $m=2$ 小于 $-10^4$，此后严格递减。因此
$$
\boxed{\|P_mJ_mP_m-P_m\|\le\tfrac14
\quad(m\ge2).}
\tag{5.8}
$$

注意 (5.8) 是双侧有限柱压缩的范数结论。本文未声称 $J_mP_m\to P_m$，也未声称 $J_m$ 在全 $H$ 中强收敛；高尾非真空分量没有被丢弃。

## 6. 任意正常正湮灭态的明确尾下界

**定理6.1。** 设 $\rho\ge0$ 是原 Haar 空间上的迹类算子，$\operatorname{Tr}\rho=1$。设
$$
\phi(T)=\operatorname{Tr}(\rho T),\qquad
\phi(SF)=0\quad(F\in\mathcal A).
\tag{6.1}
$$
定义其有限柱尾质量及平方根
$$
q_m=\operatorname{Tr}(\rho(I-P_m)),\qquad
\delta_m=\|(I-P_m)\rho^{1/2}\|_{\mathrm{HS}}=\sqrt{q_m}.
$$
则对每个 $m\ge2$，
$$
\boxed{\delta_m\ge\frac1{32D_m}
=\frac{e^{-256(m+1)}}{128(m+1)}.}
\tag{6.2}
$$
等价地，
$$
\boxed{q_m\ge\frac{e^{-512(m+1)}}{16384(m+1)^2}.}
\tag{6.3}
$$

证明。Hilbert–Schmidt 分解及迹范数乘积不等式给
$$
\|\rho-P_m\rho P_m\|_1\le2\delta_m.
\tag{6.4}
$$
具体把 $AA^*-P_mAA^*P_m$ 写成
$$(I-P_m)AA^*+P_mAA^*(I-P_m),\qquad A=\rho^{1/2},$$
两项的迹范数均至多 $\delta_m$。

由 (5.8)，$P_mJ_mP_m$ 在 $P_mH$ 上的实部至少为 $3I/4$。所以正性给
$$
\operatorname{Re}\phi(P_mJ_mP_m)\ge\frac34(1-\delta_m^2).
$$
另一方面，由 (6.1)、(5.5)、(6.4)，
$$
|\phi(P_mJ_mP_m)|
=|\phi(P_mJ_mP_m)-\phi(J_m)|
\le12D_m\delta_m.
$$
因此
$$
\frac34(1-\delta_m^2)\le12D_m\delta_m.
\tag{6.5}
$$
若 $\delta_m<1/(32D_m)$，右边小于 $3/8$，左边大于 $3(1-1/1024)/4>3/8$，矛盾。定理得证。

量词包括任意秩的正常正状态，并不局限于有限秩。如果
$$
\rho=\frac1M\sum_{\nu=1}^d x_\nu\otimes x_\nu,
\qquad M=\sum_\nu\|x_\nu\|^2>0,
$$
则 (6.3) 准确读为
$$
\frac1M\sum_{\nu=1}^d\|(I-P_m)x_\nu\|^2
\ge\frac{e^{-512(m+1)}}{16384(m+1)^2}.
\tag{6.6}
$$
所以任何满足
$$
m e^{256m}\left(\sum_\nu\|(I-P_m)x_\nu\|^2\right)^{1/2}\longrightarrow0
$$
的非零有限列，都不能给出这种正湮灭泛函。常数与秩 $d$ 无关。

## 7. 有限放大不变子商的同一几何限制

设 $N\subseteq M\subseteq H^{(d)}$ 对 $A^{(d)}$ 不变，把子商识别为
$$
Q=M\ominus N.
$$
若 $S^{(d)}M\subseteq N$，则对每个 $x\in Q$，
$$
\langle (SF)^{(d)}x,x\rangle=0\quad(F\in\mathcal A),
$$
因为 $F^{(d)}x\in M$，而 $S^{(d)}$ 把它送入 $N$。
于是 (6.2) 应用于 $x$ 的有限坐标列，给
$$
\boxed{\|(I-P_m^{(d)})x\|\ge\frac{\|x\|}{32D_m}
\quad(x\in Q,\ m\ge2).}
\tag{7.1}
$$
这不假定 $P_m^{(d)}$ 保持 $M,N,Q$。它是环境 Haar 柱投影对未知子商向量的必要尾下界。

## 8. 仍未解决的步骤

正常性只给 $q_m\to0$，允许任意慢的下降。因此 (6.3) 与正常性相容，不能推出不存在正常湮灭见证。

有限秩本身也不提供通用的柱尾速率：一个向量即可沿指定稀疏 Walsh 位携带任意慢的 $\ell^2$ 尾。尚缺利用准确关系 (6.1) 与有限秩结构的新机制，而不能单凭正性和正常性把 (6.3) 升为固定正下界。

本稿的实际增量是统一的真实半群/预解式成本和由此得到的指数尾必要条件。它没有把边界奇异态变成 Haar-normal 态，没有声称子商消去等同于 $\phi(S^*S)=0$，也没有降低普通 ISP 的完成标准。

## 内部依赖

仅使用 R12/R174 的真实 dyadic 归一化幂及 carry 恒等式、R191 §4 的有限头记号（其误差在 §5 重新证明）、实际 $Y_j1=(1-\chi_j)/2$。强主理想失败化为有限秩正正常湮灭态的逻辑见 [正常态接口](../notes/2026-11-12-pure-squarezero-quotient-weak-null-obstruction-and-haar-moment-interface-0c-agent.md) §7；本文的全部新估计与迹范数推导已写出。
