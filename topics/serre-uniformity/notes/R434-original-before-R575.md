# R434：指定 CM 型的本原 Cartan 迹与商对数的尺度不变首项

**状态：已证明。** 本篇处理 R390 之后的两个具体整性问题。对于指定原始角色 $\theta_{-1}$，非分裂 Cartan 迹在一个明确的有限群整格中本原；Mercuri–Schoof 公式显示的分子恰含一个 $p$ 因子。对于同一实际权一 CM 形式通道，形式对数保持 R390 的共同赋值和归一化后的模 $p$ 首项轮廓。因此一个未指定的非零微分比例不会改变这个一维通道的相对首项或零集。

这些结论没有把尖点的单位系数识别为实际 CM 小盘的 $b_1/p$，没有给共同赋值的绝对上界，也没有证明指定的 $L(g_{\theta_{-1}},1)$ 非零。

## 1. 实际角色与有限群模型

沿用 R348、R390：
$$
p\ge41,\qquad p\equiv2\pmod3,\qquad
K=\mathbb Q(\sqrt{-3}),\qquad M=p+1,
\tag{434.1}
$$
并固定 $K\hookrightarrow\overline{\mathbb Q}_p$ 及相容的 Teichmüller 提升。令
$$
\theta_-(y)=[y]^{-(p-1)},\qquad
g_-=f_{\Psi_{\theta_-}\kappa_4^{-1}}.
\tag{434.2}
$$
这是 R390 的 $\theta_{-1}=\theta_p$，阶为 $M$。设 $\mathcal O$ 是足够大的未分歧 $p$ 进整数环，含所有 $\theta_-$ 的值及所选 Hecke 系数位；剩余域记为 $k$。所有赋值均规范为 $v_p(p)=1$。

先只考虑有限群
$$
\mathsf G=\mathrm{PGL}_2(\mathbb F_p),\qquad
\Lambda=\mathcal O^{\mathbb F_p}/\mathcal O\mathbf 1.
\tag{434.3}
$$
$e_r$ 是点 $r$ 的特征函数类，关系为 $\sum_re_r=0$。取 $e_s$、$s\ne0$ 为整基。上三角 Borel 按仿射变换作用。

令 $\theta$ 为 $\theta_-$ 或其逆；两者给同一个特征零 cuspidal 表示。规定 $\theta(0)=0$，但下列 Weyl 求和仍明确只遍历非零元。Mercuri–Schoof §4 的模型给
$$
w e_r=-\frac1p
\sum_{y\in\mathbb F_{p^2}^{\times}}
\theta(y)e_{r\mathrm N(y)+\operatorname{Tr}(y)},
\qquad
w=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\tag{434.4}
$$
这里的字符值是特征零的 Teichmüller 值，不是把下面的模 $p$ 恒等当作特征零求和。

实际 $g_-$ 在 $p$ 处的单位化 Weil 角色是 $K_p/\mathbb Q_p$ 未分歧二次诱导，单位限制为 $\theta_-^{-1}$，导子指数为二；$\kappa_4$ 在该处平凡。这是 R348 的同一局部角色。深度零的 admissible-pair 构造给 $\mathrm{GL}_2(\mathbb F_p)$ 型 $V_{\theta_-^{-1}}=V_{\theta_-}$。局部 Langlands 中的 rectifier 在未分歧二次情形只是未分歧二次字符，所以不更改这个有限单位字符；参见 Loeffler–Weinstein §3.1–3.3，特别是 Remark 3.11。因而 (434.4) 是本篇指定的实际型，不是仅由根号或角色阶猜出的一个型。

## 2. 所有纤维上的准确模 $p$ 和

**引理。** 对每个 $r,s\in\mathbb F_p$，在 $\mathbb F_{p^2}$ 中有
$$
\sum_{\substack{y\ne0\\r\mathrm N(y)+\operatorname{Tr}(y)=s}}
 y^{p-1}=1.
\tag{434.5}
$$
把 $y^{p-1}$ 换成其逆，等式仍成立。

**证明。** 先取 $r=0$。若 $s=0$，非零迹零元有 $p-1$ 个，每项为 $-1$，所以和为一。若 $s\ne0$，所求元是
$F(Y)=Y^p+Y-s$ 的全部 $p$ 个根；这些根非零且互异。由
$$
y^{p-1}=s/y-1,\qquad
\sum_{F(y)=0}\frac1y=-\frac{F'(0)}{F(0)}=1/s
\tag{434.6}
$$
也得到一。

现在取 $r\ne0$，作可逆换元
$$
z=1+ry,\qquad t=1+rs.
\tag{434.7}
$$
原条件化为 $\mathrm N(z)=t$，而 $y\ne0$ 等价于 $z\ne1$；因为 $r\in\mathbb F_p^\times$，权变成 $(z-1)^{p-1}$。

若 $t=0$，域中的范数只在 $z=0$ 为零；这一个元的权为一。这单独处理了 $rs+1=0$ 的纤维。

若 $t\ne0,1$，$z$ 遍历 $Z^{p+1}-t$ 的 $p+1$ 个互异根，且没有 $z=1$。由 $z^p=t/z$，
$$
(z-1)^{p-1}
=\frac{t-z}{z(z-1)}
=-\frac t z+\frac{t-1}{z-1}.
\tag{434.8}
$$
这些根满足
$$
\sum\frac1z=0,\qquad
\sum\frac1{z-1}
=-\frac{(Z^{p+1}-t)'|_{Z=1}}{1-t}
=\frac1{t-1}.
\tag{434.9}
$$
故和仍为一。

最后，$t=1$ 时必须排除 $z=1$。对其余根，(434.8) 简化为 $-1/z$。全体根的倒数和为零，去掉 $z=1$ 后为 $-1$，于是所求和为一。所有零元、零迹及零范数情形均已包括。

共轭 $y\mapsto y^p$ 保持每个纤维，并将 $y^{p-1}$ 变成其逆，所以逆字符也满足同一公式。证毕。

## 3. 真正的整格与本原非分裂迹

写特征零的纤维和为
$$
S_{r,s}=
\sum_{\substack{y\ne0\\r\mathrm N(y)+\operatorname{Tr}(y)=s}}
\theta(y)\in\mathcal O.
\tag{434.10}
$$
由 (434.5)，全部 $S_{r,s}$ 都模 $p$ 同余于一。将 (434.4) 写入所选整基，得到
$$
w e_r=-\sum_{s\ne0}
\frac{S_{r,s}-S_{r,0}}p e_s\in\Lambda.
\tag{434.11}
$$
所以 $w$ 保持 $\Lambda$。Borel 已经保持它，而 Borel 与 $w$ 生成 $\mathsf G$；故 $\Lambda$ 是一个真正的 $\mathsf G$-稳定整格。

在其模 $p$ 商上定义
$$
\lambda:\Lambda/p\Lambda\longrightarrow k,\qquad
\lambda([\phi])=\sum_{s\in\mathbb F_p}\phi(s).
\tag{434.12}
$$
常数的和是 $p$ 倍常数，故该定义良好。它在 Borel 下不变，且
$\lambda(e_r)=1$。因为 $\theta$ 非平凡，真正的特征零总和为
$$
\sum_sS_{r,s}=\sum_{y\ne0}\theta(y)=0.
\tag{434.13}
$$
利用 (434.11) 计算可得
$$
\lambda(w e_r)
=-\frac{\sum_{s\ne0}S_{r,s}-(p-1)S_{r,0}}p
=S_{r,0}\equiv1\pmod p.
\tag{434.14}
$$
因此 $\lambda$ 是 $\mathsf G$-不变满射。

取任意非分裂 Cartan $\mathsf T'\subset\mathsf G$；其阶为 $p+1$。令
$$
\mathcal A_{\mathsf T'}=\frac1{p+1}\sum_{t\in\mathsf T'}t.
\tag{434.15}
$$
分母是 $p$ 单位，所以这是 $\Lambda$ 上的整幂等元。由有限群型的已知一维不变空间，$\Lambda^{\mathsf T'}$ 是秩一自由直和项，且取不变量与模 $p$ 交换。对每个 $r$，
$$
v_r:=\mathcal A_{\mathsf T'}e_r,\qquad
\lambda(\bar v_r)=1.
\tag{434.16}
$$
于是每个 $v_r$ 都是这个不变格的本原生成元；不再只是至少存在某个 $r$。所有 $v_r$ 模 $p$ 相等，因为其一维不变空间上的 $\lambda$ 是同构。

$\theta$ 在非分裂商环面的二阶元上取 $-1$。因此这个不变线也由正规化子 $\mathsf N'$ 固定，正是本题的 plus 型。

若 $\mathsf T'$ 对应 $u\in\mathbb F_p^\times$ 的非平方类，则 Mercuri–Schoof Proposition 4.1 的显示向量是
$$
P_r=p e_r-
\sum_{m\in\mathbb F_p}
\sum_{y\ne0}\theta(y)
 e_{\frac{(m+r)\mathrm N(y)}{m^2-u}+\operatorname{Tr}(y)+m}
=p\,\operatorname{Tr}_{\mathsf T'}e_r.
\tag{434.17}
$$
这里 $m^2-u$ 总非零。因为
$\operatorname{Tr}_{\mathsf T'}e_r=(p+1)v_r$ 本原，得到准确的整除次数
$$
P_r\in p\Lambda\setminus p^2\Lambda
\qquad\text{对每个 }r\in\mathbb F_p.
\tag{434.18}
$$
这消去了公式中表面的 $1/p$，并给出了不能再除一个 $p$ 的证明。

## 4. 尖点处的尺度及混合六层的适用范围

先固定任一与 $p$ 互素的 tame 向量，令 $f$ 是相应 split-Cartan 型向量。以
$Q$ 表示所选全 $p$ 水平尖点的形式参数；在素数层的经典规范中
$Q=\exp(2\pi i\tau/p)$。写
$$
f=\sum_{n\ge1}a_nQ^n,\qquad
f_r=\sum_{n\ge1}a_n\zeta_p^{-nr}Q^n.
\tag{434.19}
$$
这里先把 $f$ 取为 $Q$ 整，即 $a_n\in\mathcal O$；正规化的单一新向量有 $a_1=1$。混合 tame 层用中国剩余定理选取模 tame 水平为恒等的上幺幂元，并采用相应尖点参数，至多对 $r$ 作一个非零模 $p$ 常数的重标记，故仍得到同一公式。本型的 $p$-Euler 因子为一，故
$a_{pn}=0$，于是 $\sum_rf_r=0$。将 $e_0$ 送到 $f$ 的特征零型同构遂将
$e_r$ 送到 $f_r$；这就是 Mercuri–Schoof Proposition 6.3 的规范。

若 $v\in\Lambda$ 以整代表 $\sum_sc_se_s$ 给出，其像的第 $n$ 个系数为
$$
a_n\sum_sc_s\zeta_p^{-ns}.
\tag{434.20}
$$
换整代表只加上一个常数向量；当 $p\nmid n$ 时根和为零，而当
$p\mid n$ 时 $a_n=0$，故公式与代表无关。在 $\mathcal O[\zeta_p]$ 的剩余域中，$\zeta_p$ 变成一，所以对 $v=v_r$ 且 $a_n$ 为单位，(434.20) 的剩余值是
$$
\bar a_n\lambda(\bar v_r)=\bar a_n\ne0.
\tag{434.21}
$$
特别地，$a_1=1$ 时所得实际非分裂型向量的第一 $Q$ 系数为单位；(434.17) 的像恰含一个 $p$ 因子。由于 $\Lambda$ 在整个有限群下稳定，各个有限群平移也保持这种 $Q$ 整性。

在 R348 的混合六层中，$p$ 水平群与全部模六作用交换。可先保留整个 tame 型，再在 $p$ 因子上逐项作 (434.15)；这给张量积上的整算子
$\mathcal A_{\mathsf T'}\otimes1$，并与 $H_6$ 平均交换。$|\mathrm{GL}_2(\mathbb Z/6)|$ 只含 $2,3$，所以 $H_6$ 平均在本处也是整幂等元。

更具体地，在 R348 的 tame 型中取一个有限群稳定的全 $\mathcal O$-格：从任何全格出发，取它的有限个群平移之和即可得到。因群阶是 $p$ 单位，$H_6$ 平均把该格投到一个秩一自由直和项；选其本原生成元 $u_6$。于是
$$
\bigl(\Lambda\otimes\mathcal O u_6\bigr)^{\mathsf T'}
=\mathcal O v_r\otimes\mathcal O u_6
\tag{434.22}
$$
是本原直和项。这里的有限群整性不需把 Chen 的有理同源先假定为整同构。选择与这个 tame 向量相容的尖点/平移后，只要其首个非零系数是 $p$ 单位，(434.21) 逐项保留该单位；本结论本身不声称任意预先固定的尖点都有单位首项。

实际 $\sqrt[3]4$ 扭曲在 $p\equiv2\bmod3$ 的本地不改变此结论：立方映射在 $\mathbb F_p^\times$ 上可逆，Hensel 提升给一个
$\sqrt[3]4\in\mathbb Z_p^\times$。故 R348 的 $a=\sqrt[3]4\,u$ 在此为单位尺度的本地同构。

必须保留本节的范围：它证明的是有限型整格和相应尖点展开的本原性。全 $p$ 水平的坏约化、投影到指定 CM 商的微分格，以及 $c_1$ 附近的微分展开，还没有由 (434.21) 自动确定。

## 5. 实际权一通道的形式对数

现在固定 R390 的**同一个一维 CM 通道**。令
$$
e=p^2-1,\qquad \varpi^e=p,\qquad
w=\frac{a-1}{p^3},\qquad
G(w)=\sum_{n\ge1}b_nw^n\in R_0\langle w\rangle,
\tag{434.23}
$$
其中 $R_0$ 是足够大的未分歧整数环，实际目标坐标为
$Y=\varpi^{p-1}G(w)$。R390 给
$$
M_G:=\min_n v_p(b_n)\in\mathbb Z_{\ge1}.
\tag{434.24}
$$
$G$ 非零，所以此最小值有限。

R390 的完整 BT 群比较允许在固定良参考形式群上取坐标。其
$\mu_{p+1}\subset\mathcal O_{K_p}^\times$ 作用可整线性化：从任一整参数
$T$ 出发，对 $[\alpha]$ 的作用用阶为 $p+1$ 的单位平均，取得导数为一的特征参数 $Y$。于是
$$
[\alpha]^*Y=\alpha Y\quad(\alpha\in\mu_{p+1}).
\tag{434.25}
$$
这与 R390 的权一半线性下降相容；使用的是完整 BT 群上的
$\mathcal O_{K_p}$ 作用，不是声称椭圆曲线有阶 $p+1$ 的代数自同构。

将不变微分规范成 $(1+\cdots)dY$，形式对数写成
$$
\log_{\mathcal G}(Y)=Y+\sum_{d\ge2}\ell_dY^d.
\tag{434.26}
$$
不变微分整给
$v_p(\ell_d)\ge-v_p(d)$；而 (434.25) 与对数的函子性给
$$
\ell_d=0\quad\text{除非 }d\equiv1\pmod{p+1}.
\tag{434.27}
$$
两条陈述只涉及参考良模型上的整形式群。

定义实际缩放后的对数
$$
\mathscr L(w)=\varpi^{-(p-1)}
\log_{\mathcal G}\bigl(\varpi^{p-1}G(w)\bigr).
\tag{434.28}
$$
由 (434.27)，若 $d=1+j(p+1)$、$j\ge1$，对应项准确为
$$
\ell_d p^j G(w)^d.
\tag{434.29}
$$
所以该缩放没有留下分数赋值，且全部系数在 $\operatorname{Frac}(R_0)$ 中。

若 $j=1$，$d=p+2$ 不被 $p$ 整除。若 $j\ge2$，由
$$
p^j>1+(p+1)j=d,
\qquad v_p(d)\le j-1
\tag{434.30}
$$
也得到相同的上界。第一个不等式在 $p\ge5,j=2$ 成立，乘以 $p$ 后严格大于下一个右端，所以归纳成立。故对所有 $j\ge1$，(434.29) 的系数赋值至少
$$
j+dM_G-v_p(d)\ge1+dM_G\ge2M_G+1.
\tag{434.31}
$$
这些下界随 $d$ 趋向无穷，保证在 Tate 代数中收敛。于是得到实际整比较
$$
\boxed{\quad
\mathscr L-G\in p^{2M_G+1}R_0\langle w\rangle.
\quad}
\tag{434.32}
$$
因此
$$
\min_n v_p([w^n]\mathscr L)=M_G,\qquad
\overline{p^{-M_G}\mathscr L}
=\overline{p^{-M_G}G}\ne0.
\tag{434.33}
$$
R378 的实际共同赋值、第一次出现单位系数的位置，以及归一化后整个模 $p$ 多项式，都由同一形式对数保留。

## 6. 一维微分比例为何不再改变相对首项

为容纳 Cartan 向量、尖点或 slash 规范的定义域，允许任意有限系数扩域
$E/\operatorname{Frac}(R_0)$。取 $E$ 的一致化元 $\tau$，以整数赋值
$v_E(\tau)=1$ 规范，记 $e_E=v_E(p)$、剩余域为 $k_E$。对于非零
$F\in E\langle w\rangle$，定义本原约化轮廓
$$
\operatorname{in}_E(F)
:=\overline{\tau^{-m_E(F)}F},\qquad
m_E(F)=\min_n v_E([w^n]F).
\tag{434.34}
$$
它是非零的 $k_E$ 多项式。对任意 $c\in E^\times$，
$$
m_E(cF)=v_E(c)+m_E(F),\qquad
\operatorname{in}_E(cF)
=\overline{\tau^{-v_E(c)}c}\,\operatorname{in}_E(F).
\tag{434.35}
$$
因此其首个非零次数、一次项是否非零、以及零集，均不受这个非零比例影响。

若原来的 $F$ 在 $\operatorname{Frac}(R_0)\langle w\rangle$ 中，且共同
$p$ 赋值为 $M$，则 $m_E(F)=e_EM$，而
$\operatorname{in}_E(F)$ 等于原来的
$\overline{p^{-M}F}$ 扩张剩余域后，再乘剩余单位
$\overline{p^M/\tau^{e_EM}}$。所以 (434.33) 在任意这样的系数扩域上仍给相同的本原轮廓，至多相差一个非零剩余常数。选取另一一致化元也只改变这个常数。

把 (434.35) 应用于 (434.28) 有直接的算术意义。固定 $g_-$ 的所选系数嵌入，R348 的实际 $H_6$ 与 $\mathsf N'$ 不变通道重数为一。在这一条微分线上，任何另一个非零代数微分——例如 §4 的明确 Cartan 迹向量——在某个足够大的有限 $E$ 上与
$d\mathscr L$ 相差一个非零常数。两者在 $c_1$ 取零常数项的原函数也相差同一常数。

不需要假定这个常数在未分歧域中。一个有理同源或 slash 规范带来的非零常数可以改变 $m_E(F)$ 的数值，但不能改变本原轮廓，至多乘一个剩余单位。式 (434.32) 则说明从实际整坐标换到这种对数时，也不会改变该轮廓。

这个结论只针对**指定的一维微分通道**。有多个重数时，任意非整线性组合可能抵消最低系数；不能逐坐标套用 (434.35)。对于一个本原整格基的可逆整变换，保持的是所有向量系数生成的整系数理想及相应约化向量，而不保证每个坐标的首项各自保持。

特别地，如果将来真正证明这个通道满足
$$
\operatorname{in}_E(\mathscr L)=u\,w+w^2R(w),\qquad
u\in k_E^\times,\quad R\in k_E[w],
\tag{434.36}
$$
则 $\mathscr L/w$ 除去共同的 $\tau$ 次幂后在 $v_p(w)>0$ 上为单位，唯一零点为 $w=0$。这个判据不再需要先计算某个 Manin 比例的绝对赋值。反之，尖点处 (434.21) 并不证明 (434.36)：两式属于不同的实际展开盘。

若同时取得 $L(g_-,1)\ne0$，R374 给所有有理点在该商中的准确零像，便可把 (434.36) 用于 R390 的真实候选 $v_p(w)\ge1$。本篇没有取得这两个尚缺输入，不能据本篇单独排除候选。

## 7. 下一实际缺口与来源

有限群迹中的准确 $p$ 因子已被控制。形式对数进一步说明：在固定一维通道中，有理同源比例可以从相对首项问题中消去。剩余的局部工作是计算**同一个实际 CM 盘**上 §4 微分的原函数本原轮廓，或证明其等于 (434.36)。固定 tame 权四截面及 R390 的 Cartier 单位仍需经过这个实际比较；本篇没有省略坏约化的桥。

指定原始角色的中心值仍是另一个全局缺口。R348 的全族正平均不保证该指定角色非零。

使用的原文输入为：

- P. Mercuri–R. Schoof, *Modular forms invariant under non-split Cartan subgroups*, Math. Comp. **89** (2020),1969–1991，DOI 10.1090/mcom/3503；§2 Proposition 2.1，§4 pp.1975–1976 的函数模型及 Proposition 4.1，§6 p.1981 的 Proposition 6.3。[原刊作者 offprint](https://reneschoof.github.io/mcom3503.pdf)。本篇的模 $p$ 纤维和、整稳定性及每个迹向量的本原性均在正文独立证明。
- D. Loeffler–J. Weinstein, *On the computation of local components of a newform*, Math. Comp. **81** (2012),1179–1200；§3.1–3.3，尤其未分歧 admissible pair 的有限型构造与 p.1188 Remark 3.11 的未分歧 rectifier。[原刊机构稿](https://wrap.warwick.ac.uk/id/eprint/43666/1/WRAP_Loeffler_S0025-5718-2011-02530-5.pdf)。只用未分歧二次、深度零情形，不借用一般 ramified trace 符号或扭曲搜索算法。
- R348 的实际局部角色、混合六层分解及 $\kappa_4^{-1}$ 取向；R378 的真实源小盘；R390 的完整 BT 整比较、坐标权一与共同赋值至少一。

本篇为纯证明，无必需数据文件或验证脚本。有限素数试算没有进入证明。
