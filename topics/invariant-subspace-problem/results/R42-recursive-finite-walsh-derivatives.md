# R42：有限阶 Walsh 导数空间的递归矩分离

日期：2026-11-12（UTC+8）。会话：Astra-ISP-e2cb8f94，子任务 `centered_literature`。

**状态：已证明的中间结论。** 将 R41 的有限秩二阶结论推广到一个精确定义的递归有限阶类。每个向量仍属于 $L^2$，系数尾可任意慢；递归要求是所有单个位导数张成有限维空间，并且导数属于前一阶类。没有把这个类说成全部有限 Walsh chaos。结论仍只排除“一个分量为第一 chaos、另一个分量属于此递归类”的非零全部矩消失对，不证明任意第一 chaos 向量循环，不解决一般 ISP，不主张文献新颖性。

主要输入是 R9/R12 的截断估计和 R40 的连续对卷积定理。下面从常数阶开始归纳，亦给 R33/R41 范围的统一证明。

## 1. $L^2$ 定义、导数与递归线性类

令 $\chi_j=(-1)^{b_j}$，对有限 $S\subset\mathbb N_0$ 记 $\chi_S=\prod_{j\in S}\chi_j$。Walsh 函数形成 $H=L^2(\mathbb Z_2,\mu)$ 的正交单位基。对 $d\ge0$，定义闭空间

$$
H_{\le d}=\left\{g=\sum_{|S|\le d}\widehat g(S)\chi_S:
\sum_{|S|\le d}|\widehat g(S)|^2<\infty\right\}.
\tag{1.1}
$$

每个级数先按 $L^2$ 意义理解。定义有界线性的第 $k$ 位导数系数

$$
\partial_k g=
\sum_{S\ni k}\widehat g(S)\chi_{S\setminus\{k\}}.
\tag{1.2}
$$

于是 $\|\partial_k g\|\le\|g\|$，$\partial_k g$ 不依赖第 $k$ 位；若 $g\in H_{\le d}$，则 $\partial_k g\in H_{\le d-1}$。按第 $k$ 位分解时，恰有 $g=g_{0,k}+\chi_k\partial_k g$，其中两个系数都不依赖该位。

现在递归定义

$$
\mathcal V_0=\mathbb C1,
$$

$$
\mathcal V_d=
\left\{g\in H_{\le d}:
\dim\operatorname{span}\{\partial_k g:k\ge0\}<\infty,
\quad \partial_k g\in\mathcal V_{d-1}\text{ 对所有 }k\right\}
\quad(d\ge1).
\tag{1.3}
$$

这些是**线性类**，不声称它们范数闭。归纳核实线性性：$\mathcal V_0$ 线性；若上一阶线性，则 $\partial_k(ag+bh)=a\partial_k g+b\partial_k h$ 仍在上一阶，且新导数的张成空间包含于两个原有限维空间之和，仍有限维。

显然

$$
\mathcal V_1=H_{\le1}
=\left\{c_*+\sum_jc_j\chi_j:\sum|c_j|^2<\infty\right\}.
\tag{1.4}
$$

第二阶恰是 R41 的类：若 $g=\beta_*+\sum\beta_j\chi_j+\sum_{i<j}D_{ij}\chi_i\chi_j$，则导数为 $\beta_k1+\sum_jD_{kj}\chi_j$；导数张成有限维当且仅当对称零对角系数矩阵 $D$ 的秩有限。

此外 $C g(y)=\overline{g(-1-y)}$ 保持每个 $\mathcal V_d$。因为 $C\chi_S=(-1)^{|S|}\chi_S$，有 $\partial_k(Cg)=-C(\partial_k g)$；从 (1.3) 归纳即可。

## 2. 主定理

**定理 2.1。** 对每个有限 $d\ge0$，若 $f\in H_{\le1}$、$g\in\mathcal V_d$ 且

$$
B(A^nf,g)=0\qquad(n\ge0),
\quad B(u,v)=\int u(y)v(-1-y)\,d\mu(y),
\tag{2.1}
$$

则 $f=0$ 或 $g=0$。

由于两类均由 $C$ 保持，同样排除对应的非零通常矩消失对 $\langle A^nf,v\rangle=0$。

## 3. 归纳的共同高位恒等式

写 $f=\alpha_*+\sum_k\alpha_k\chi_k$，并记 $H_k=\partial_k g$。固定 $r\ge0$，取低 $k$ 位截断 $Q=A_k^r$ 和第 $k$ 位矩阵单位 $E_k$。R41 的局部计算实际上不要求 $g$ 是二阶，只使用分解 $g=g_{0,k}+\chi_kH_k$，故对任意 $g\in H$ 都有

$$
2B(E_kQf,g)-B(Qf,g)
=B(Qf,H_k)+\alpha_kB(Q1,g)+2\alpha_kB(Q1,H_k).
\tag{3.1}
$$

局部验证是 $B(1,1)=1$、$B(\chi_k,\chi_k)=-1$、交叉项为零，而 $B(e_{10}x,y)=1/2$ 对 $x,y\in\{1,\chi_k\}$ 都成立。

用

$$
\|A^r-A_k^r\|\le ra_k,\qquad
\left\|\frac{A^{2^k}}{\|A^{2^k}\|}-E_k\right\|=\eta_k,
\quad\eta_k/a_k\to0,
$$

以及 (2.1)、$|\alpha_k|\le\|f\|$、$\|H_k\|\le\|g\|$，得到每个固定 $r$ 下的统一尾方程

$$
\boxed{
B(A^rf,H_k)+\alpha_kB(A^r1,g)
+2\alpha_kB(A^r1,H_k)=O_{r,f,g}(a_k).
}
\tag{3.2}
$$

误差可取 $(2\eta_k+8ra_k)\|f\|\|g\|$；因此与 $k$ 无关的常数确实存在。

## 4. 归纳基与有限测试

当 $d=0$ 时，$g$ 为常数。若 $g\ne0$，(2.1) 给 $\langle f,(A^*)^n1\rangle=0$ 对所有 $n$ 成立。R11 及 $C1=1$ 表明 $1$ 对 $A^*$ 循环，所以 $f=0$。归纳基成立。

设结论已对 $d-1$ 成立，反设 (2.1) 中 $f,g$ 都非零。若 $f$ 为常数，$1$ 对 $A$ 循环会直接给 $g=0$；若 $g$ 为常数，归纳基给矛盾。因此可设两者都非常函数。

令

$$
\mathcal D=\operatorname{span}\{H_k:k\ge0\},\qquad q=\dim\mathcal D.
$$

由定义及上一阶的线性性，$1\le q<\infty$ 且 $\mathcal D\subseteq\mathcal V_{d-1}$。对 $u\in\mathcal D$ 定义

$$
\mathcal L_r(u)=B(A^rf,u),\quad
\mathcal M_r(u)=B(A^r1,u),\quad b_r=B(A^r1,g).
$$

归纳假设保证 $\bigcap_r\ker(\mathcal L_r|_{\mathcal D})=\{0\}$。因而可选 $q$ 个固定测试 $r_1,\dots,r_q$，使 $L:u\mapsto(\mathcal L_{r_i}(u))_i$ 为同构。相应记 $Mu=(\mathcal M_{r_i}(u))_i$、$b=(b_{r_i})_i$，并置

$$
K=L^{-1}M,\qquad u_*=-L^{-1}b.
\tag{4.1}
$$

(3.2) 给

$$
(I+2\alpha_kK)H_k=\alpha_ku_*+O(a_k).
$$

因为 $\alpha_k\to0$，其逆矩阵最终一致有界。于是

$$
H_k=R(\alpha_k)+O(a_k),\qquad
R(t)=t(I+2tK)^{-1}u_*.
\tag{4.2}
$$

## 5. 退化核由归纳假设排除

对每个固定 $r$ 设

$$
\Phi_r(t)=\mathcal L_r(R(t))+tb_r+2t\mathcal M_r(R(t)).
$$

由 (3.2)、(4.2)，$\Phi_r(\alpha_k)=O_r(a_k)$。至少一个 $\Phi_r$ 不恒为零，理由如下。

若它们全部恒零且 $u_*=0$，则全部 $b_r=0$，由 $1$ 循环得 $g=0$，矛盾。若 $u_*\ne0$，展开 $(I+2tK)^{-1}$ 并逐次比较系数，得到

$$
\mathcal L_r(K^{j+1}u_*)=\mathcal M_r(K^ju_*)
\qquad(j,r\ge0).
\tag{5.1}
$$

非零有限维 $K$-不变空间 $\operatorname{span}\{K^ju_*\}$ 含一个非零特征向量 $u$，设 $Ku=\lambda u$。于是

$$
B(A^r(\lambda f-1),u)=0\qquad(r\ge0).
$$

$u\in\mathcal D\subseteq\mathcal V_{d-1}$，而 $\lambda f-1\in H_{\le1}$。由于 $f$ 非常函数，后者非零，包括 $\lambda=0$ 时也如此。这与归纳假设矛盾。因此确有非零残差。

固定一个这样的 $r$。多项式

$$
p_r(t)=\det(I+2tK)\Phi_r(t)
$$

非零、次数至多 $q+1$、常数项为零。设其零点消失阶为 $\nu\in\{1,\dots,q+1\}$，便由 $\alpha_k\to0$ 得

$$
|\alpha_k|^\nu=O(a_k),\qquad
|\alpha_k|+\|H_k\|=O(a_k^{1/(q+1)}).
\tag{5.2}
$$

这一步允许消失阶任意有限大，没有假定初始线性化非退化。

## 6. 有限阶计数给绝对一致收敛，再由连续对定理闭合

记 $\delta=1/(q+1)>0$。由于 $a_k\le e^{-16^k}$，(5.2) 使 $\sum|\alpha_k|<\infty$，所以 $f$ 有连续代表。

写 $g=\sum_{|S|\le d}c_S\chi_S$。最大指标为 $k$ 的集合 $S$ 至多有

$$
N_{k,d}=\sum_{j=0}^{d-1}\binom{k}{j}
\le C_d(1+k)^{d-1}
$$

个。因为这些系数全都出现在 $H_k=\partial_k g$ 中，Cauchy–Schwarz 给

$$
\begin{aligned}
\sum_{\substack{S\ne\varnothing\\|S|\le d}}|c_S|
&=\sum_{k\ge0}\sum_{\max S=k}|c_S|\\
&\le C_d^{1/2}\sum_{k\ge0}(1+k)^{(d-1)/2}\|H_k\|<\infty.
\end{aligned}
\tag{6.1}
$$

故 $g$ 的 Walsh 级数绝对一致收敛，也有连续代表。R40 排除两个非零连续函数形成全部矩消失对，与 (2.1) 矛盾。归纳完成，定理 2.1 对每个有限 $d$ 成立。

## 7. 任意慢尾的非柱实例：独立线性级数的多仿射多项式

取有限多个两两不交的索引组 $I_1,\dots,I_s\subset\mathbb N_0$，每组可无限。选平方可和系数并令

$$
Z_j=\sum_{k\in I_j}c_{j,k}\chi_k\in L^2.
\tag{7.1}
$$

设 $P(z_1,\dots,z_s)$ 是复多项式，每个变量的次数至多一，且总次数至多 $d$；即 $P$ 是多仿射的。则

$$
g=P(Z_1,\dots,Z_s)\in\mathcal V_d.
\tag{7.2}
$$

首先各 $Z_j$ 独立，故每个不同变量的乘积属于 $L^2$，其平方范数是各因子平方范数的乘积；有限项求和仍属于 $L^2$。索引组不交保证每个单项式的 Walsh 次数等于其中变量数，因此 $g\in H_{\le d}$。

若 $k\in I_j$，多仿射性给精确导数公式

$$
\partial_k g
=c_{j,k}\,\frac{\partial P}{\partial z_j}(Z_1,\dots,Z_s).
\tag{7.3}
$$

右端的多项式不再含 $Z_j$，总次数至多 $d-1$。所以所有导数张成至多 $s$ 维空间，并且按多项式次数归纳属于 $\mathcal V_{d-1}$。这证明 (7.2)。不同这类构造的任意有限和仍属于相应最大阶的类，由 §1 的线性性保证。

若每个系数列有无限多个非零项，单个 $Z_j$ 和乘积 $Z_1\cdots Z_s$ 都不是有限柱函数：固定其他组中一个非零系数，再让某一组的非零指标任意增大，便得到任意高位的非零 Walsh 系数。系数平方和可以有任意慢的尾，因此这个归纳没有要求向量预先具有超快连续性或可控柱逼近速度。超快尾只在反设“存在零矩配对”后由 (5.2) 逼出。

## 8. 类的严格边界

当 $d\ge2$ 时，$\mathcal V_d$ 不是全部 $H_{\le d}$。例如

$$
g=\sum_{j\ge1}\frac1j\chi_{2j}\chi_{2j+1}
$$

属于 $H_{\le2}$，但 $\partial_{2j}g=j^{-1}\chi_{2j+1}$ 线性无关，所以其导数张成无限维，不在 $\mathcal V_2$。有限 Walsh 多项式都在相应阶的递归类中，并在 $H_{\le d}$ 稠密，因此本类一般并不范数闭；不能从稠密性把定理延伸到全部有限 chaos。

重叠索引组的线性级数乘积不自动满足 (7.3)：重复位会产生对角收缩及额外的移动导数项。任意 R16 无限乘积通常也具有无界 Walsh 次数，不能因名称中有“乘积”就归入本条。一般无限秩导数空间、更高阶非递归类，以及任意 $L^2$ 配对，仍未处理。
