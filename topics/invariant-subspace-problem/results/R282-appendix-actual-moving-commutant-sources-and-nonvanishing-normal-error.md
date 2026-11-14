# R282 附录：实际高尾乘子极限、均有界真来源与正常迹误差

2026-11-14，normal-annihilator / 789f。**状态：已证明。**

本稿从 [R282](R282-complete-multiplier-stabilizer-classification-and-finite-head-splitting.md) 的恢复稿独立拆出；原 §§1–9 的分类结论不依赖本附录。这里只使用原 Haar 模型 $H=L^2(\mathbb Z_2,\mu)$、$Uf(y)=f(y-1)$、$A=M_wU$ 与实际归一化幂 $N_m=A^{2^m}/\|A^{2^m}\|$。物理位上的 $E_m=e_{10}$ 满足 $N_m=E_m+\eta_mE_m^*N_{m+1}$，$0<\eta_m\le e^{-770\cdot16^m}$；$\mathcal A$ 是 $A$ 生成的含单位算子范数闭代数。以下保留恢复稿的第 10 节编号便于核对；最后的第 11 节给出交换子在不变空间上成为逐点乘子的准确限制。

## 10. 实际归一化幂的尾乘子极限及一致有界真来源障碍

本节准确检查由高位幂提取 §9 稳定乘子的一个入口。固定向量上的近似成立，但一致有界的尾操作只能得到标量弱*极限；更强地，真正一致有界的 $\mathcal A$ 右来源已足以使移动向量上的同一近似失败。

### 10.1 原权乘子的准确递推

写

$$
N_m=M_{q_m}U^{2^m},\qquad
p_m^\epsilon(y)=\mathbf1_{\{\text{第 }m\text{ 位}=\epsilon\}}.
$$

真实进位恒等式 $N_m=E_m+\eta_mE_m^*N_{m+1}$ 给

$$
\boxed{q_m=p_m^1+\eta_mp_m^0q_{m+1}.}
\tag{10.1}
$$

确实，在第 $m$ 位为 $0$ 的输出上，$E_m^*$ 的加 $2^m$ 不改变更高位，因此其后的高位乘子仍为 $q_{m+1}$；另一半由 $E_m$ 给乘子 $1$。这也可直接用原 $A^{2^m}$ 的权积核对。

于是 $q_m$ 只依赖第 $m$ 位及更高位，$0\le q_m\le1$，且

$$
\|q_m-p_m^1\|_\infty\le\eta_m,\qquad
\int q_m\,d\mu\longrightarrow\tfrac12,
$$

$$
\boxed{
\|q_m\|_2^2
=\tfrac12+\tfrac{\eta_m^2}{2}\|q_{m+1}\|_2^2
\longrightarrow\tfrac12.}
\tag{10.2}
$$

对任意固定 $f\in H$，由 $U^{2^m}\to I$ 强，

$$
\|N_mf-M_{q_m}f\|_2
\le\|U^{2^m}f-f\|_2\longrightarrow0.
\tag{10.3}
$$

这个收敛在范数紧的向量集合上统一；有限秩给出的固定有限个向量属于这种情形。但它不在任意有界的移动向量族上统一。

### 10.2 全部一致有界高尾乘子只有标量弱*聚点

设 $b_m$ 仅依赖第 $m$ 位及更高位，且 $\sup_m\|b_m\|_\infty\le C$。对任意固定有限低头的 $L^1$ 测试函数 $g$，充分大的 $m$ 满足准确分离

$$
\int b_mg\,d\mu
=\left(\int b_m\,d\mu\right)\left(\int g\,d\mu\right).
$$

用有限柱函数在 $L^1$ 中稠密和统一 $L^\infty$ 界，得到

$$
\boxed{b_m-\left(\int b_m\,d\mu\right)1
\longrightarrow0\quad\text{弱*}.}
\tag{10.4}
$$

所以任何弱*聚点都是标量。这包括 $q_j$（$j\ge m$）的任意联合 Borel 函数，只要最后得到的乘子一致有界。单凭此类高尾运算，不能提取 §9 所需的非有限柱乘子。

特别，(10.2)、(10.4) 给 $q_m^2\to I/2$ 弱*。

### 10.3 一个直接的移动角色反例

令

$$
c_m(y)=\exp\left(2\pi i\frac{y\bmod2^{m+1}}{2^{m+1}}\right).
\tag{10.5}
$$

它模长为 $1$，且 $U^{2^m}c_m=-c_m$。故

$$
\|N_mc_m-M_{q_m}c_m\|_2=2\|q_m\|_2
\longrightarrow\sqrt2.
\tag{10.6}
$$

这里还没有声称 $c_m$ 位于某个未知不变空间。下一节用真 $\mathcal A$ 来源将同一失败搬到任意固定向量的来源轨道中。

### 10.4 移动角色来自一致有界的真交换子来源

记物理 Walsh 位函数 $\chi_j=p_j^0-p_j^1$，并置

$$
W_j=(I-N_j)(I+N_j)^{-1}\in\mathcal A.
\tag{10.7}
$$

所有 $W_j$ 相互交换。按第 $j$ 位写 $N_j=\begin{pmatrix}0&t_j\\I&0\end{pmatrix}$，$t_j=\eta_jN_{j+1}$；直接乘法给

$$
W_j-(I-2E_j)
=2t_j(I-E_j-E_j^*)(I-t_j)^{-1}.
$$

因此

$$
\|W_j\|\le1+\sqrt2+\frac{4\eta_j}{1-\eta_j}<3,
\tag{10.8}
$$

因为本题 $\eta_j\le e^{-770}<1/16$。同一个块公式给 $W_j1=\chi_j$，并且当输入是第 $j$ 位的 $\Omega_+$ 张量任意其余向量时，$W_j$ 将它准确变成该位的 $\Omega_-$。

尤其，对依赖比 $j$ 更低位的柱函数 $f$，

$$
W_jf=\chi_jf.
\tag{10.9}
$$

这不是 $W_j=M_{\chi_j}$ 的全 $H$ 算子等式。对有限乘积，将 $W_j$ 按 $j$ 递增依次作用：在每一步，前面形成的函数仍是该步的低位柱函数，才可用 (10.9)。因此有限乘积在 $1$ 上准确产生相应 Walsh 乘积。

对 $0\le j\le m$ 定义

$$
\theta_{j,m}=\frac{2\pi2^j}{2^{m+1}},\quad
\alpha_{j,m}=\frac{1+e^{i\theta_{j,m}}}{2},\quad
\beta_{j,m}=\frac{1-e^{i\theta_{j,m}}}{2},
$$

$$
R_m=\prod_{j=0}^m
\left(\alpha_{j,m}I+\beta_{j,m}W_j\right)\in\mathcal A.
\tag{10.10}
$$

因 $\alpha+\beta=1$，且 $\sum_{j\le m}\theta_{j,m}<2\pi$，有

$$
\|R_m\|
\le\prod_{j=0}^m(1+3\theta_{j,m}/2)
\le e^{3\pi}.
\tag{10.11}
$$

这是与 $m$ 无关的真实算子范数预算。上面的有限乘积计算给

$$
R_m1=\prod_{j=0}^m(\alpha_{j,m}+\beta_{j,m}\chi_j)=c_m.
\tag{10.12}
$$

还成立全空间上的逐固定向量结论

$$
\boxed{R_m-M_{c_m}\longrightarrow0\quad\mathrm{SOT}.}
\tag{10.13}
$$

为证明它，先固定一个只依赖前 $k$ 位的柱函数 $f$。将 (10.10) 分成低因子 $L_{m,k}$（$j<k$）和高因子 $H_{m,k}$（$j\ge k$）。低角度之和趋零，且

$$
\|\alpha_{j,m}I+\beta_{j,m}W_j-I\|
\le4|\beta_{j,m}|\le2\theta_{j,m},
$$

故 $L_{m,k}\to I$ 于算子范数。低位标量乘积

$$
\ell_{m,k}=\prod_{j<k}(\alpha_{j,m}+\beta_{j,m}\chi_j)
$$

也一致趋于 $1$。对高因子按 $j=k,k+1,\ldots,m$ 依次作用于 $f$，每一步已形成的函数都只依赖低于该步的位，故准确有

$$
H_{m,k}f=h_{m,k}f,\qquad
h_{m,k}=\prod_{j=k}^m(\alpha_{j,m}+\beta_{j,m}\chi_j),
\quad |h_{m,k}|=1.
$$

所有 $W_j$ 交换，因而

$$
\|R_mf-c_mf\|_2
\le e^{3\pi}\|L_{m,k}-I\|\,\|f\|_2
+\|1-\ell_{m,k}\|_\infty\|f\|_2\longrightarrow0.
$$

再由柱函数稠密及 (10.11)，得到 (10.13)。此论证没有让 $W_j$ 在任意移动向量上等于位乘法。

### 10.5 对任意固定向量及正常迹都有非消失误差

定义

$$
D_m=N_mR_m-M_{q_m}R_m.
$$

由 (10.13) 以及 $U^{2^m}c_m=-c_m$，对每个固定 $f\in H$，

$$
D_mf+2q_mc_mf\longrightarrow0\quad\text{于 }H.
\tag{10.14}
$$

其中剩下的平移误差仅为固定向量上的
$q_mc_m(U^{2^m}f-f)$，确实趋零；(10.13) 的误差经两个一致有界算子后也趋零。

结合 $q_m^2\to1/2$ 弱*，得到

$$
\boxed{
\|N_mR_mf-M_{q_m}R_mf\|_2
\longrightarrow\sqrt2\,\|f\|_2.}
\tag{10.15}
$$

若 $f\in M$，因 $R_m\in\mathcal A$，每个 $R_mf$ 都在同一个未知 $M$ 中。因此，正常性、有限秩及右来源一致有界本身，仍不允许把 (10.3) 统一到这些移动输入。

甚至固定正常迹配对中的误差也不消失。令 $Q_m=2^{m+1}$、$\zeta_m=e^{2\pi i/Q_m}$。由 (10.1)，

$$
\int q_mc_m\,d\mu
=-\frac{2}{Q_m(1-\zeta_m)}+O(\eta_m)
\longrightarrow-\frac{i}{\pi}.
\tag{10.16}
$$

这来自对 $p_m^1c_m$ 在 $Q_m$ 个余类上的准确几何求和。

事实上 $q_mc_m\to-i/\pi$ 弱*。对固定低 $k$ 位测试函数，用上面的 $c_m=\ell_{m,k}h_{m,k}$ 分解：$q_mh_{m,k}$ 属于高尾，$\ell_{m,k}\to1$ 一致，故其配对与均值乘测试函数积分之差趋零。再用统一绝对值界推广到全部 $L^1$ 测试函数。

(10.14) 及统一算子界因此给

$$
D_m\longrightarrow\frac{2i}{\pi}I\quad\mathrm{WOT},
$$

$$
\boxed{
\operatorname{Tr}(\rho D_m)
\longrightarrow\frac{2i}{\pi}\operatorname{Tr}\rho
\quad(\rho\text{ 任意固定迹类}).}
\tag{10.17}
$$

最后一步先对有限秩配对取极限，再由迹范数逼近和 $\sup_m\|D_m\|<\infty$ 推广。若实际正常见证存在且迹锚非零，(10.17) 同样适用；它表明删去该移动来源误差会直接改变迹锚，而不是仅漏掉一个无法估计的范数项。

本节没有构造湮灭态，没有证明 (10.13) 的伴随版本或逆来源版本，也没有将 (10.13) 用在未经控制的另一移动输入上。固定来源与移动来源之间的差别在 (10.15)、(10.17) 中已由真实来源完全量化。


## 11. 真实交换子在非零不变空间上若成为固定乘子，则只能为标量

**命题 11.1。** 设 $M\ne0$ 为原 $A$ 的闭不变子空间，$R\in\{A\}'$，$b\in L^\infty(\mu)$。若对每个 $f\in M$ 都有 $Rf=bf$，则 $b$ 几乎处处为常数。

**证明。** 先付支撑。因 $H$ 可分，取 $M$ 的可数稠密列 $(f_k)$，令

$$
E=\bigcup_k\operatorname{ess\,supp}f_k.
$$

这是 $M$ 的总本质支撑：$M$ 中每个向量都几乎处处在 $E$ 外为零。原 $w>0$ 几乎处处，且 $A=M_wU$，所以 $Af_k\in M$ 给 $\tau^{-1}E\subseteq E$ 模零，其中 $\tau(y)=y-1$。Haar 保测使包含升级为模零等号，odometer 遍历性及 $M\ne0$ 给 $\mu(E)=1$。

对任意 $f\in M$，$Af\in M$，而 $RA=AR$，故

$$
M_bAf=RAf=ARf=AM_bf.
$$

写成实际函数等式并消去几乎处处正的 $w$：

$$
\bigl(b-b\circ\tau\bigr)(f\circ\tau)=0.
$$

对可数稠密列同时应用，且其平移后的总支撑仍为满测，便得 $b=b\circ\tau$ 几乎处处。遍历性迫使 $b$ 为常数。$\square$

**推论 11.2（固定乘子极限也有同一限制）。** 设 $R_n\in\{A\}'$，且对每个 $f\in M$，$R_nf\to bf$ 于范数，其中 $b\in L^\infty(\mu)$ 固定。则 $b$ 为常数；此处不需要事先假设 $\sup_n\|R_n\|<\infty$。

确实，分别在 $f$ 和 $Af$ 上取极限可直接传递 $R_nAf=AR_nf$，得到命题证明中的乘法交换等式。即使仅有对每个 $f\in M$ 的弱收敛，固定有界 $A$ 同样允许传递该等式，因此结论仍成立。

这与 R282 的稳定乘子分类不同：一般保持 $M$ 的有限头乘子无需与 $A|_M$ 交换；这里额外使用了它是在全部 $M$ 上由真实交换子限制或极限得到。§10 中 $c_m$ 随 $m$ 移动，所以不受“固定 $b$”推论排除。命题不能用于只对单个向量成立的乘法近似，也不把未控制的移动输入、伴随或逆来源收敛补出来。
