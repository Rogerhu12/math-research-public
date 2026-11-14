# R235 附录：连续积分核的相对尾迹与正常湮灭者排除

日期：2026-11-13（UTC）。作者：normal_next / Astra-ISP-0c017065；AI-assisted，GPT-6 Astra Pro。

**状态：以下结论完整证明，属于中间进展。** 对两个实际慢符号，任何具有联合连续积分核、迹非零的迹类泛函都不能湮灭其主理想。特别，排除任意有限组复连续函数给出的正正常见证；没有假设这些函数同相、保持非负锥或具有 Walsh 次数指数矩。一般可测的有限秩见证仍未排除，不证明普通 ISP。

本文只使用 R253 的实际相位乘积和已经支付的 carry 误差。纯尾算子只用于比较；不将原代数替换为纯模型，也不从恒等右因子的真空比趋零反推完整理想范数。

## 1. 模型、核与主结论

令
$$
H=L^2(\mathbb Z_2,\mu),\qquad
H=K_m\otimes H_m,\qquad
K_m=\bigotimes_{0\le j<m}\mathbb C^2,
$$
参考向量为 Haar 常数函数 $1$。记
$$
\mathcal A=\overline{\mathbb C[I,A]}^{\|\cdot\|},
\quad
S_N=\sum_{j\ge0}a_jN_j,\quad
S_Y=\sum_{j\ge0}a_jY_j,\quad
a_j=(j+1)^{-2}.
$$
所有 $N_j,Y_j,A$ 都是原 Haar 表示中的实际算子。

对 $S=S_N$ 或 $S_Y$，R253 的实际相位乘积为
$$
P_m=\prod_{\zeta^{2^m}=1}\gamma_\zeta(S)
=I_{K_m}\otimes Q_m\in S\mathcal A,
\qquad
\gamma_\zeta(A)=\zeta A.
\tag{1.1}
$$
令 $q=2^m$，
$$
D_m=\sum_{j\ge m}a_jE_j,\qquad E_j=e_{10}^{(j)},
\qquad
T_m=I_{K_m}\otimes D_m^q,
\qquad
h_m=\langle D_m^q1,1\rangle>0.
\tag{1.2}
$$
这里 $E_j$ 是物理位上的纯矩阵，$D_m$ 不被声称属于实际尾代数。

积分核按下述约定：
$$
(Rf)(x)=\int_{\mathbb Z_2}K_R(x,y)f(y)\,d\mu(y).
\tag{1.3}
$$
内积线性于第一个变量。若 $\rho=\sum_\nu f_\nu\otimes f_\nu$，则其核为
$K_\rho(x,y)=\sum_\nu f_\nu(x)\overline{f_\nu(y)}$。

**定理 1.1。** 若 $\rho$ 是迹类算子，并有联合连续积分核
$K\in C(\mathbb Z_2\times\mathbb Z_2)$，则
$$
\boxed{\quad
\frac{\operatorname{Tr}(\rho P_m)}{h_m}
\longrightarrow\operatorname{Tr}\rho.
\quad}
\tag{1.4}
$$
此结论本身不要求 $\rho$ 为自伴或正。

因此，若上述 $\rho$ 满足
$$
\operatorname{Tr}(\rho SF)=0\qquad(F\in\mathcal A),
\tag{1.5}
$$
则 $\operatorname{Tr}\rho=0$。特别，任何非零正迹类算子若具有连续核，都不能满足 (1.5)。

“具有连续核”是对原正常泛函的额外假设。任意秩一密度的分量只有 $L^2$ 正则性时，并不能免费满足此条件。

## 2. 保函数正锥算子的核一致范数迹界

令 $H_+$ 为实值非负函数锥。写 $T\ge_{\rm lat}0$ 表示有界算子 $T$ 保持此锥；这与 Hilbert 自伴正序不同。

**引理 2.1。** 设 $R$ 是迹类算子，且有本质有界积分核 $K_R$。若
$T\ge_{\rm lat}0$，则
$$
\boxed{
|\operatorname{Tr}(RT)|
\le \|K_R\|_{L^\infty(\mu\times\mu)}
   \langle T1,1\rangle.
}
\tag{2.1}
$$
$R$ 不要求正或自伴，$T$ 也不要求自伴。右端不出现 $\|T\|$ 或柱空间的维数。

证明。令 $\Pi_n$ 为前 $n$ 位有限柱空间的正交条件期望，$d=2^n$。设
$C_1,\ldots,C_d$ 为该层等测度柱集，并取物理正柱基
$$
e_\alpha=\sqrt d\,\mathbf1_{C_\alpha},\qquad 1\le\alpha\le d.
$$
因为每个柱集的测度为 $1/d$，
$$
|\langle Re_\beta,e_\alpha\rangle|
=
\left|d\int_{C_\alpha}\int_{C_\beta}
K_R(x,y)\,d\mu(y)d\mu(x)\right|
\le\frac{\|K_R\|_\infty}{d}.
\tag{2.2}
$$
又因 $T$ 保非负锥，
$$
t_{\beta\alpha}:=\langle Te_\alpha,e_\beta\rangle\ge0.
$$
有限维矩阵迹因此给出
$$
\begin{aligned}
|\operatorname{Tr}(\Pi_nR\Pi_nT)|
&=\left|\sum_{\alpha,\beta}
 \langle Re_\beta,e_\alpha\rangle
 \langle Te_\alpha,e_\beta\rangle\right|\\
&\le\frac{\|K_R\|_\infty}{d}
 \sum_{\alpha,\beta}t_{\beta\alpha}\\
&=\|K_R\|_\infty\langle T1,1\rangle.
\end{aligned}
\tag{2.3}
$$
最后一个等式使用
$1=d^{-1/2}\sum_\alpha e_\alpha$，并不是对 $T$ 作矩阵元逐项绝对估计。

对迹类 $R$，$\Pi_n\to I$ 强且 $\|\Pi_n\|\le1$ 给
$\|\Pi_nR\Pi_n-R\|_1\to0$；可先对有限秩算子证明，再作迹范数逼近。因此 (2.3) 的左端趋向
$|\operatorname{Tr}(RT)|$，得到 (2.1)。证毕。

## 3. 任意正尾测试对连续核的相对迹极限

以下引理把需要的正性与特定慢符号分开。

**引理 3.1。** 设每个
$$
T_m=I_{K_m}\otimes Z_m
$$
都是保非负锥的有界算子，且
$$
h_m=\langle T_m1,1\rangle>0.
$$
不要求 $\|T_m\|$ 或 $\|T_m\|/h_m$ 一致有界。若迹类 $\rho$ 有联合连续核 $K$，则
$$
\frac{\operatorname{Tr}(\rho T_m)}{h_m}
\longrightarrow\operatorname{Tr}\rho.
\tag{3.1}
$$

证明。设
$$
\rho_m=\Pi_m\rho\Pi_m,
$$
其核是两个变量分别取前 $m$ 位条件期望所得
$$
K_m(x,y)=
2^{2m}\int_{x+2^m\mathbb Z_2}
       \int_{y+2^m\mathbb Z_2}
K(u,v)\,d\mu(v)d\mu(u).
\tag{3.2}
$$
$\mathbb Z_2\times\mathbb Z_2$ 紧，故 $K$ 一致连续，并且
$$
\varepsilon_m:=\|K-K_m\|_\infty\longrightarrow0.
\tag{3.3}
$$
$\Pi_m=I_{K_m}\otimes|1\rangle\langle1|$，所以存在有限维算子 $R_m$ 使
$$
\rho_m=R_m\otimes|1\rangle\langle1|.
$$
因此准确有
$$
\operatorname{Tr}(\rho_mT_m)
=\operatorname{Tr}(\rho_m)\,h_m.
\tag{3.4}
$$
对迹类差 $\rho-\rho_m$ 使用引理 2.1：
$$
\left|
\frac{\operatorname{Tr}(\rho T_m)}{h_m}
-\operatorname{Tr}\rho_m
\right|
\le\varepsilon_m.
\tag{3.5}
$$
又 $\rho_m\to\rho$ 于迹范数，故 (3.1) 成立。

可进一步给出单个一致连续模量控制。有限维核迹公式给
$$
\operatorname{Tr}\rho_m=\int K_m(y,y)\,d\mu(y).
$$
由 (3.3) 和迹范数收敛，
$$
\operatorname{Tr}\rho=\int K(y,y)\,d\mu(y),
\qquad
|\operatorname{Tr}\rho_m-\operatorname{Tr}\rho|
\le\varepsilon_m.
$$
因此
$$
\boxed{
\left|
\frac{\operatorname{Tr}(\rho T_m)}{h_m}
-\operatorname{Tr}\rho
\right|
\le2\varepsilon_m.
}
\tag{3.6}
$$
证毕。

这里不曾对 $\|\rho-\rho_m\|_1\|T_m\|/h_m$ 作控制。关键是引理 2.1 把核的一致误差直接乘以同一个 $h_m$。

## 4. 真实相位乘积的全部 carry 误差

现在使用 R253 第三附录
[《实际消元尾的恒等右因子真空比趋零》](../results/R253-appendix-identity-multiplier-vacuum-ratio-decay.md)
§§2、3、5 已证的准确估计。

各 $E_j$ 保函数非负锥，彼此交换且 $E_j^2=0$。因为 $a_j>0$，
$$
D_m^q=
q!\sum_{\substack{F\subset[m,\infty)\\ |F|=q}}
a_FE_F
\ge_{\rm lat}0,
\qquad
E_F=\prod_{j\in F}E_j.
\tag{4.1}
$$
展开按算子范数绝对收敛。每个 $E_F$ 的真空矩为 $2^{-q}$，因此
$$
h_m=q!\sum_{|F|=q}\prod_{j\in F}\frac{a_j}{2}>0.
\tag{4.2}
$$
特别，只保留 $F=\{m,\ldots,m+q-1\}$，用 $m\le q$ 及
$q!\ge(q/e)^q$，得到
$$
h_m\ge q!2^{-q}(m+q)^{-2q}
\ge(8eq)^{-q}.
\tag{4.3}
$$

令
$$
a_\Sigma=\sum_{j\ge0}a_j,\qquad M=3a_\Sigma,\qquad
e_m=13a_\Sigma\,q M^{q-1}\exp(-770\,16^{m-1}).
$$
该附录保留真实有限头、真实相位作用及两种 Cayley 逆后，证明
$$
\boxed{
\|P_m-T_m\|=\|Q_m-D_m^q\|\le e_m.
}
\tag{4.4}
$$
该等式中的尾提升是等距的。简述其准确来源：先截断低头实际 $N_j$，每项误差不超过
$\exp(-770\,16^{m-1})$；真实 $Y_j$ 的预解恒等式只多因子 $9$，高尾 $Y_j-E_j$ 只多因子 $4$。截断低头是 $q$ 维真幂零移位的零常数多项式，故 $q$ 个 dyadic 相位因子的乘积准确消去全部低头，只留 $D_m^q$。最后对 $q$ 个有界因子作望远镜差分，得到 (4.4)。这里没有把压缩当作代数同态。

由于 $16^{m-1}=q^4/16$，(4.3)—(4.4) 给
$$
\log\frac{e_m}{h_m}
\le-\frac{770}{16}q^4+O(q\log q)
\longrightarrow-\infty.
\tag{4.5}
$$
所以 $e_m/h_m\to0$。

引理 3.1 适用于 (1.2) 的 $T_m$。再用通常迹类不等式
$|\operatorname{Tr}(\rho B)|\le\|\rho\|_1\|B\|$，得到完整的定量结论
$$
\boxed{
\left|
\frac{\operatorname{Tr}(\rho P_m)}{h_m}
-\operatorname{Tr}\rho
\right|
\le
2\varepsilon_m+\|\rho\|_1\frac{e_m}{h_m}
\longrightarrow0.
}
\tag{4.6}
$$
这证明定理 1.1。

若 $\rho$ 满足 (1.5)，则 (1.1) 给
$\operatorname{Tr}(\rho P_m)=0$ 对所有 $m$ 成立。令 $m\to\infty$，得到
$\operatorname{Tr}\rho=0$。正且非零的迹类算子具有严格正迹，故矛盾。整个论证没有在 $\rho$ 上假设保函数非负锥。

## 5. 任意复连续分量、可数连续特征向量与有限旗

若 $f_1,\ldots,f_d$ 是任意复连续函数，则
$$
\rho=\sum_{i=1}^d f_i\otimes f_i
$$
具有连续核
$$
K(x,y)=\sum_{i=1}^d f_i(x)\overline{f_i(y)}.
$$
因此除非全部 $f_i=0$，该正正常泛函不能湮灭 $S_N\mathcal A$ 或 $S_Y\mathcal A$。各函数可以改变符号或具有不同且随点变化的相位。

同一结论扩到下述可数类。设
$$
F:\mathbb Z_2\longrightarrow\ell^2,\qquad
F(y)=(f_1(y),f_2(y),\ldots)
$$
为范数连续映射。其紧像有界，所以
$$
\sum_i\|f_i\|_2^2=\int\|F(y)\|_{\ell^2}^2\,d\mu(y)<\infty.
$$
因此 $\rho_F=\sum_i f_i\otimes f_i$ 在迹范数下收敛。紧像上的坐标尾一致趋零：
$$
\sup_y\sum_{i>N}|f_i(y)|^2\longrightarrow0.
$$
这可由有限坐标投影在 $\ell^2$ 中强收敛、收缩且在紧集上一致收敛直接证明。于是
$$
K_F(x,y)=\sum_i f_i(x)\overline{f_i(y)}
=\langle F(x),F(y)\rangle_{\ell^2}
$$
为一致收敛的连续核。只要 $F\ne0$，定理仍排除该正态为慢湮灭者。

这里不能只假设每个 $f_i$ 连续及 $\sum_i\|f_i\|_2^2<\infty$，便省去对 $\ell^2$ 值连续性的验证。一个方便的充分条件是
$\sum_i\|f_i\|_\infty^2<\infty$，但定理并不要求这一较强条件。

还有以下准确的有限旗推论。设
$$
N\subset M\subset H^{(d)}
$$
为闭 $A^{(d)}$ 不变子空间，$Q=M\ominus N$ 为商的正交实现，且 $S_Q=0$。
若 $q=(q_1,\ldots,q_d)\in Q$，则对每个 $F\in\mathcal A$，
$S^{(d)}F^{(d)}q\in N$，因此
$$
\operatorname{Tr}(\rho_qSF)
=\sum_i\langle SFq_i,q_i\rangle
=\langle S^{(d)}F^{(d)}q,q\rangle=0,
\qquad
\rho_q=\sum_i q_i\otimes q_i.
$$
定理推出
$$
\boxed{Q\cap C(\mathbb Z_2)^d=\{0\}.}
\tag{5.1}
$$
这是对正交实现中的真实向量 $q$ 的结论；没有声称商上任意代表的连续性会经过正交投影保留。

## 6. 不保锥、无任何次数指数矩的明确连续例

该节说明连续核条件不要求已知的点态正锥或 Walsh 系数可和条件。它不是普通 ISP 的反例。

取两两不交的有限位块 $B_k$，每块包含 $2k^2$ 个位，依次配成 $k^2$ 对。令 $x_j\in\{0,1\}$ 为物理位，并定义
$$
b_k(x)=(-1)^{\sum_{r=1}^{k^2}x_{j_{k,2r-1}}x_{j_{k,2r}}}.
$$
每个 $b_k$ 是连续的 $\{\pm1\}$ 值有限柱函数。单对的 Walsh 展开为
$$
(-1)^{xy}=\frac12(1+\chi_x+\chi_y-\chi_x\chi_y).
$$
因此 $b_k$ 的全部 $2^{2k^2}$ 个 Walsh 系数的绝对值都恰为 $2^{-k^2}$。

置
$$
g=\sum_{k\ge1}2^{-k}b_k,\qquad f=1+ig,\qquad\rho=f\otimes f.
\tag{6.1}
$$
级数一致收敛，故 $f$ 连续，且 $\operatorname{Re}f=1$、$|g|\le1$。$g$ 非常数。于是 $f$ 不是某个固定常数相位乘以非负函数，$\rho$ 不保持函数非负锥：若秩一 $f\otimes f$ 保锥，选一个满足 $\langle h,f\rangle\ne0$ 的非负 $h$，其输出便迫 $f$ 具有固定非负相位。因 $\operatorname{Re}f=1$，固定相位还将迫 $f$ 为常数，与这里矛盾。

不同块的非空 Walsh 支撑不交，故
$$
\sum_{F\ne\varnothing}|\widehat f(F)|
=\sum_{k\ge1}2^{-k}(2^{k^2}-2^{-k^2})
=\infty.
\tag{6.2}
$$
特别 $\rho$ 的原 Walsh 矩阵不是 entrywise $\ell^1$。

对任意 $r>1$，其 Walsh 次数指数平方和等于
$$
\begin{aligned}
\sum_Fr^{2|F|}|\widehat f(F)|^2
&=|\widehat f(\varnothing)|^2+
 \sum_{k\ge1}4^{-k}4^{-k^2}
 \big((1+r^2)^{2k^2}-1\big)\\
&=\infty,
\end{aligned}
\tag{6.3}
$$
因为 $(1+r^2)/2>1$，各块正项已经趋向无穷。因此本例不满足任何次数指数矩假设。

它也不是“一个有限头块加上各尾位乘积”形式的向量。任取有限头之外的某个 $B_k$ 内一对物理位，固定其他位。该对上的函数矩阵具有形式
$$
\begin{pmatrix}
u+iv&u+iv\\
u+iv&u-iv
\end{pmatrix},
\qquad \operatorname{Re}u=1,\quad v=\pm2^{-k}\ne0.
$$
其行列式为 $-2iv(u+iv)\ne0$，故不能在这两个位上分解成单个位函数的乘积。这在任意有限头之外都成立。因此，这个秩一正态也不是 R237 所处理的有限头块加可实现单个位乘积基中的一个对角秩一态。

另一方面，$\rho$ 有连续核 $f(x)\overline{f(y)}$ 且迹严格为正，所以定理 1.1 排除它以及全部同类复连续有限正和作为慢理想湮灭见证。此处只声称缺少上述列出的充分正则性条件，不声称该函数不属于任何其他已经证明的循环类。

## 7. 剩余缺口

R253 第三附录证明
$|\omega_m(Q_m)|/\|Q_m\|\to0$。本稿与之完全相容：
连续核给的是对每个指定泛函的相对估计 (4.6)，并不提供
$\|Q_m\|/h_m$ 的统一上界，也没有求得完整尾理想范数 $q_m$ 的非消失下界。

对任意正正常态，只有
$\|\rho-\Pi_m\rho\Pi_m\|_1\to0$；这不能代替 (3.3) 的核一致收敛，因为通常迹界将额外付出发散的 $\|T_m\|/h_m$。任意有限组 $L^2$ 函数不必有连续代表，也没有证明能用保持慢湮灭条件的操作把它们送入这里的连续类。

因此，一般正有限秩见证、R244 的见证专属配对正则器、R253 的非平凡右因子及普通 Hilbert ISP 仍然开放。

## 已证依赖

- [R253](../results/R253-positive-tail-partial-traces-and-dyadic-phase-product-elimination.md) §§1、3：实际 dyadic 相位乘积、尾因子及 $P_m\in S\mathcal A$。
- [R253 第三附录](../results/R253-appendix-identity-multiplier-vacuum-ratio-decay.md) §§2、3、5：真实 carry 比较、正纯尾展开及 $e_m/h_m\to0$；该附录的其余真空比上界不用于本文证明。
- [R235](../results/R235-positive-cayley-power-coefficients-and-cone-normal-witness-exclusion.md)：只用于区分既有保锥迹类排除的范围，本文不将其假设套给一般正密度。
