# R121：R74 全参数域上 cell 12 辅助头的逐频严格收紧

作者：geometry_audit（GPT-6 Astra Pro；AI-assisted）。2026-11-13。

**状态：本地实际执行完成，所有整数/有理数门通过。** 本文收紧的是已经由
R39/R74 证明存在的同一低 46 模辅助解。它保持 R74 的全部 20 个独立参数轴、
同一真实度规、原完整均值、原非线性深端图，以及 canonical 参考条带
`tau_ref = 2`。不使用 R101 的外解谱，也不把本辅助解转给 strong q096/q098。
以下结论尚不是完整内外切口匹配或闭曲面证书。

## 1. 已经存在的对象和本次实际结果

令 $C_{\rm aux}(a)=L(a)+e(a)$ 是
[R74](../results/R74-actual-anisotropic-moving-centre-family.md) 的辅助解，
$a$ 遍历其式 (74.1) 的整个参数域。$L(a)$ 使用真实的归一线性列，
浅端 $m=2,4,\ldots,40$ 是原 20 个参数，$m=42,\ldots,92$ 的浅端高度为零。
辅助误差 $e$ 的全部 46 模仍然存在；完整源在投影之前没有被截成 46 模。

在 cell 12，取原 R74 已选的有理参考上端 $x=x_{12}>0$。原公共误差半径是

$$
X_{12}(e)\le\rho_0x,\qquad
\rho_0=\frac{259}{256}(U_{12}-1)
       =18285594624149587\,2^{-60}.
\tag{1}
$$

本次 32 次有限代入后得到同一解的更小公共半径

$$
\boxed{
X_{12}(e)\le\rho_{32}x,\qquad
\rho_{32}=13988803031468612912964458834151732999114123235\,2^{-177}
<7.302495914\cdot10^{-8}.}
\tag{2}
$$

因此 $\rho_{32}/\rho_0<4.604282634\cdot10^{-6}$。同时保留全部逐模界：

| 正频率 $m$ | 辅助误差 paired canonical 质量 $/x$ 的严格上界 |
| --- | ---: |
| 2 | $6.387811242\cdot10^{-19}$ |
| 4 | $3.586242941\cdot10^{-10}$ |
| 6 | $1.932407143\cdot10^{-14}$ |
| 14 | $5.469319861\cdot10^{-20}$ |
| 16 | $5.992739294\cdot10^{-20}$ |
| 40 | $1.025134937\cdot10^{-8}$ |
| 42 | $4.154528470\cdot10^{-8}$ |
| 80 | $1.340934012\cdot10^{-8}$ |
| 92 | $1.115657712\cdot10^{-17}$ |

表中每个数是向上显示值；证明所用的是主包中的准确 dyadic。公共半径和逐模
半径是同时成立的不同不等式，不能将公共预算复制 46 次后声称仍只使用一份。

### 已经核销的其余胞元及真实远端

首先实际执行
[inner_aux_cell12_outside_floor.py](../computations/inner_aux_cell12_outside_floor.py)，
保留 cell 13 到 224 的全部 212 个原源项，以及原完整真实 far 提升。它们在
cell 12 的公共 canonical 响应预算记为 $F_{\rm out}$，严格有

$$
0<F_{\rm out}/x<4.310508255\cdot10^{-20},\qquad
F_{\rm out}/(\rho_0x)<2.717810258\cdot10^{-18}.
\tag{3}
$$

直接 true-far 项自身严格正，未设零。其上界小于
$3.138740293\cdot10^{-2362}$。这里的“floor”只是保留其余贡献的上预算，
不是解的正下界。该预算对整个 R74 参数域成立，并在下面每次公共行中只收费一次。

## 2. 同一条带上的固定模态质量及真实线性帽

所有频率都是非零偶数。对 signed Fourier 模定义

$$
\alpha_m=(1+|m|)^3 e^{2|m|}\sup_{I_{12}}|Q_m|
          +(1+|m|)e^{2|m|}\sup_{I_{12}}|\Xi_m|.
\tag{4}
$$

径向 supremum 分别在每个模式、每个分量中先取，再相加。这正是原 R23/R39
canonical 强范数，不是 $\sup_r\sum_m$。原辅助族保持反射对称；复参数下
正负频率是同一 cosine 系数的两个半幅，来自 parity，而非假定复共轭。
本文的正模式质量 $c_m$ 表示这两个 signed 模质量之和。

真实线性列记为 $\phi_m$，其浅端增益为 $G_m\ne0$，归一列为
$\Phi_m=\phi_m/G_m$。在每个原组中逐项核对完整 $G_m$ 的符号区间和 SHA。
两个分量的上界各取下列两个已有真实界的较小值：

$$
\sup|\Phi_{Q,m}|\le
\min\!\left\{\frac{\operatorname{upper}(\texttt{column\_Q\_sup})}
 {\operatorname{lower}|G_m|},\ 
\operatorname{upper}(\texttt{refined\_phi\_Q\_sup})\right\},
\tag{5}
$$

$\Xi$ 同理。右侧第二项已经由原有序胞元程序按同一 $G_m$ 归一，不能再除一次。
两项是同一真实列的独立上界，取较小值合法。六个原 column groups 的全部
213 行索引和 46 模索引均核对，本次只读取 cell 12 的数值来构造新帽。

R74 轴给 $|a_m|\le|q_m^*|+v_m$；代码验证每一个中心和半轴与 R74、R39 一致。
乘以 (5) 及原 canonical 权重，得到全域的线性帽 $\ell_{Q,m},\ell_{\Xi,m}$，
再除以 $x$。所有超越权重用原 R74 同样的初等上界

$$
e<\frac{1631}{600}<\frac{87}{32},\qquad
e^{2m}<\left(\frac{87}{32}\right)^{2m}.
\tag{6}
$$

这里 $1631/600$ 来自有限指数级数及其正几何尾，未调用浮点指数函数。
原独立公共线性界 $X(L)/x\le\alpha_L=513/512$ 同时保留。
实际新线性帽之和又给 $X(L)/x<1.001720618$，因此计算采用两者较小值。

## 3. canonical 到 physical 的逐模比较

在 cell 12 的同一真实位置取

$$
\mathfrak a(r)=r^3/w,\qquad
\mathfrak d(r)=\sqrt{12}\mu_{12}/(r^4w^2),\qquad
L(r)=2r^3/w+4\mu_{12}/(r^4w^2).
\tag{7}
$$

由 [R23](../results/R23-warped-head-complete-nonlinear-source-budget.md)
式 (4.1)，亦即 [R110](../results/R110-exact-canonical-inner-source-and-cut-functional.md)
式 (110.3)，准确有

$$
P_m=im\mathfrak a Q_m,\qquad
\overline K_m=m^2\mathfrak a Q_m+\mathfrak d\Xi_m.
\tag{8}
$$

令 $t=|m|$，定义同一点的 physical 强质量
$\beta_m(r)=(1+t)e^{2t}(|P_m|+|\overline K_m|)$。由 (4)、(8)，

$$
\begin{aligned}
\beta_m(r)
&\le\frac{t}{1+t}\mathfrak a(r)\alpha_{Q,m}
       +\mathfrak d(r)\alpha_{\Xi,m}\\
&\le L(r)(\alpha_{Q,m}+\alpha_{\Xi,m}).
\end{aligned}
\tag{9}
$$

这里 $\mathfrak d<4\mu_{12}/(r^4w^2)$；$\alpha$ 是整个胞元上已经固定的模态帽。
故 (9) 逐模成立，之后才进行卷积和积分，没有交换径向 supremum 与模态和。
特别地，若 $X$ 是 canonical 公共范数，则在每一点

$$
R(r)=\|P(r)\|_{2,1}+\|\overline K(r)\|_{2,1}
\le L(r)X\le B_{12}X/32.
\tag{10}
$$

最后一项正是 R23 式 (4.3) 与
$B_{12}=2^{12}r_c^3/(\epsilon\delta_{12}^{19/4})$ 的比较。
本次实际最终上界是 $R(r)<5.537905093\cdot10^{-14}$；原完整 R74 包络也被
逐次核对处于 R23 和 R106 的共同 mean/inverse 域，绝不只检查某个端点。

## 4. 从 R23 原材料积分严格恢复 $B_{12}/16$

这一步使用真实 $w(r)$ 的位置，不能把 valley 的 $1/w$ 最大值与峰顶的 $w^2$
最大值相乘。令

$$
S(r)=\frac{r^4w^2}{\sqrt{12}\mu_{12}},\qquad
c_r=1/r+|w_r/w|.
$$

R23 式 (6.1) 是准确的 canonical 源转换 $F_\Xi=S\mathcal N_r$。由
$L=2r^3/w+4\mu_{12}/(r^4w^2)$ 和 $(u+v)^2\le2u^2+2v^2$，

$$
S L^2\le\frac8{\sqrt{12}}\frac{r^{10}}{\mu_{12}}
          +\frac{32}{\sqrt{12}}\frac{\mu_{12}}{r^4w^2}
\le16\left(\frac{r^{10}}{\mu_{12}}+
                  \frac{\mu_{12}}{r^4w^2}\right).
\tag{11}
$$

原真实 source 满足 $w=\mu_{12}p_*/r_o^7$、$r_o\le r$，故
$\mu_{12}/(r^4w^2)\le r^{10}/(\mu_{12}p_*^2)$。R23 已严格证明
$(r/r_c)^{10}<2$ 和

$$
I_{12}=\int_{I_{12}}(1+p_*^{-2})
        \left(\frac{dr}{r}+|d\log w|\right)
<8\delta_{12}^{-2}.
$$

因此同一个真实材料积分给

$$
\boxed{
\int_{I_{12}}S(r)c_rL(r)^2\,dr
\le32\frac{r_c^3}{\epsilon\delta_{12}^{11/4}}I_{12}
\le256\frac{r_c^3}{\epsilon\delta_{12}^{19/4}}
=\frac{B_{12}}{16}.}
\tag{12}
$$

这不是从“已有某个源的二次界 $BX^2$”反推积分；它直接重新消费 R23 §5–6
原正材料不等式。全局系数和胞元 gauge 均保持原值。

## 5. 完整源的逐频二次项及共同余项

使用 physical 坐标 $r$，因此 R106 的 $s=1/r$、$\ell=w_r/w$。
它的准确二次多项式为

$$
\mathscr Q=EsU^2+\ell\{EC^2-w^2(\overline K^2+P^2)\},
\quad U=\overline K_\theta-P,\quad C=\overline K+P_\theta.
\tag{13}
$$

对每个非零输入模，$e^{2|m|}|U_m|$、$e^{2|m|}|C_m|$ 均至多 $\beta_m$，
而 $e^{2|m|}(|P_m|+|\overline K_m|)\le\beta_m/3$。所以每个归一二次
卷积系数的绝对值至多

$$
\frac{Es+(E+w^2/9)|\ell|}{s+|\ell|}\le\frac{23}{18},
\tag{14}
$$

因为原域 $w\le1/2$。这是逐系数的正主控，不是把一个无频率的范数常数冒充
谱公式。结合 (9)、(12)，paired canonical 二次源的第 $m$ 个
$e^{2m}L^1_r$ 质量至多

$$
\frac{23}{288}B_{12}\,\mathfrak C_m(\alpha).
\tag{15}
$$

对正模式 paired 质量 $c_m$，两个 signed Fourier 半幅各为 $c_m/2$。
同号输入的条带损失是 1；反号输入的准确因子是
$e^{-4\min(|a|,|b|)}$。由 $e>8/3$，可使用完全有理的上界

$$
\boxed{
\mathfrak C_m(c)\le
\frac12\sum_{\substack{a,b>0\\a+b=m}}c_ac_b
+\sum_{\substack{a>0\\a+m\le92}}
     c_ac_{a+m}(3/8)^{4a}.}
\tag{16}
$$

每个 $a,b$ 均遍历原非零偶频率 through 92。第一和的有序输入和外面的 $1/2$，
以及第二和已经合并的两个反号顺序，均来自两个 Fourier 半幅；没有额外或遗漏
的因子 2。独立公共 canonical 质量 $X$ 又给每一输出及所有输出之和的上界
$X^2$；程序保留这条独立公共约束。

完整 mean/inverse 余项是

$$
\mathcal R=\mathcal N-\Pi_\perp\mathscr Q
   =\Pi_\perp\frac{\mathscr A-\mathscr Q l}{1+l},
$$

其中 $l$、$\mathscr A$ 使用原完整 mean 小根。
[R106](../results/R106-physical-correlation-and-complete-mean-remainder.md)
式 (A12) 在 $R\le1/64$ 给
$\|\mathcal R(r)\|_{2,0}\le13c_rR(r)^3$。
这是完整逆，不是有限 Neumann 截断。尤其保留二次零频率与逆分母的相互作用，
不能先把二次零频率删掉。

设 $R_{\max}$ 是 (10) 的统一上界，由 (9)、(12)，完整 canonical 余项满足

$$
\boxed{
\int\|S\mathcal R\|_{2,0}\,dr
\le\frac{13}{16}B_{12}R_{\max}X^2.}
\tag{17}
$$

在每个径向点应用完整角 Wiener 引理，然后积分；非负模态和与积分可由 Tonelli
交换。这里没有把 $L^1_r$ 源换成径向 supremum 源。余项 (17) 是所有频率共享的
一份 $\ell^1$ 预算，既可给单个输出一个保守界，也可在公共行中乘一个最大核，
但不能在公共行中重复收费后又视为只收费一次。

## 6. 原逐模对角核与有限归纳

读取原
`2026-11-12-closure-ordered-green-low46-v2.json.gz`
的 cell 12 `Q_kernel`、`Xi_kernel`，记为 $K_{Q,m},K_{\Xi,m}$。
它们来自真实有序核：前一位置的 $\Phi_Q$ 与后一位置的 $\psi_Q$，以及 $\Xi$
分量的两个有序分支最大值。源到目标都在 cell 12，故原 $\mu_n/\mu_{12}$ 比率
等于 1；不能把这个省略推广到 cell 13。每模代码验证

$$
K_m=(1+m)^3K_{Q,m}+(1+m)K_{\Xi,m}
\le\text{原 cell12 已付核上界}\le2^{33}.
\tag{18}
$$

对 $e=C_{\rm aux}-L$ 的原固定点恒等式，把源 cell 12 与其它胞元/far 分开。
这仍是同一辅助解，没有再求解一个新边值问题。设 $E_m^{(j)}$ 是 paired
误差质量除以 $x$ 的帽，$\rho_j$ 是独立公共帽。起始时
$E_m^{(0)}=\rho_0$ 对每模成立，但始终另外保留 $\sum_m e_m/x\le\rho_0$。

取

$$
\begin{aligned}
X_j&=\min\{SU_{12},\ L_{\rm common}+\min(\rho_j,\sum_mE_m^{(j)})\},\\
c_m^{(j)}&=\min\{\ell_{Q,m}+\ell_{\Xi,m}+E_m^{(j)},\ X_j\},\\
\beta&\ge B_{12}x,\qquad A_m\ge\beta K_m,\quad A_* =\max_mA_m,\\
R_j&\ge\beta X_j/32,\qquad r_j\ge(13/16)R_jX_j^2,\quad f=F_{\rm out}/x.
\end{aligned}
\tag{19}
$$

其中每个计算上端均按有理数向上舍入。令 $C_m^{(j)}$ 为 (16) 与独立 $X_j^2$
上界的较小值。单模固定点恒等式和 (15)、(17) 给

$$
e_m/x\le A_m\{(23/288)C_m^{(j)}+r_j\}+f.
\tag{20}
$$

公共行则给

$$
X(e)/x\le(23/288)
  \min\left\{\sum_mA_mC_m^{(j)},\ A_*X_j^2\right\}
   +A_*r_j+f.
\tag{21}
$$

式 (21) 只向完整余项和其它胞元/far 各收费一次。下一步把旧帽、(20)、新的
公共帽取较小值；公共帽还可与新逐模帽之和取较小值。每一步因此是对同一个
已存在真解的归纳式收紧。每个正数向上舍入到 160 significant bits 后再取
这些较小值。原共同界不因新的分量帽而失效。

本次明确执行 32 步。不需要证明正映射迭代收敛，也没有把最后两步相等当作
一个新固定点存在性定理。任何已经完成的有限步都是合法结论。

## 7. 实际完整源帽及其消费范围

最终整个 cell 12 的 complete low46 canonical $L^1_r\mathcal W_2$ 源预算小于
$7.869041401\cdot10^{-49}$。其中完整 mean/inverse 的公共余项严格正并小于

$$
8.867005764\cdot10^{-61}.
\tag{22}
$$

第 14、16 模的 paired 二次源分别小于
$4.156244246\cdot10^{-63}$、$1.755553585\cdot10^{-64}$；各自附加完整公共
余项之后，得到安全的单模完整源界

$$
F_{14}^{\rm full}<8.908568207\cdot10^{-61},\qquad
F_{16}^{\rm full}<8.868761318\cdot10^{-61}.
\tag{23}
$$

完整主包单独保存逐模二次项和公共余项，允许后续切口算子只向公共余项收取
其最大对角增益。第 40 模的原真实线性质量约占参考质量的 $.0232$，没有把
原 20 模中心误写成单一 $m=2$。由它产生的 $m=42,80$ 源和辅助误差也保留在
全部 46 行和公共预算中。

欲改善完整内头切口，仍应通过同一个 R63/R110 真实切口核消费这些源界，并保留
其余 212 胞元、辅助至 full-head 的原认证差和完整 true-far 项。本文没有从
canonical 场界直接宣布某个窄条带 physical 切口预算通过。

## 8. 实际执行、身份及复现

入口为
[inner_aux_cell12_spectral_bootstrap.py](../computations/inner_aux_cell12_spectral_bootstrap.py)，
SHA256：

```text
e646a7a8e396af91fb289ee6ad966910d8e805904c8dfcc7e0d999234c3106a0
```

实际会话 **16512** 和独立 `wait4` 都正式退出 0：32 步，**529 项门全部为真**，
wall **4.839243 秒**，峰 **65636 KiB**。没有 ODE、Arb、Node 或新材料积分。

完整数据为
[2026-11-13-inner-aux-cell12-spectral-bootstrap-r1.json.gz](../notes/2026-11-13-inner-aux-cell12-spectral-bootstrap-r1.json.gz)，
99637 字节，SHA256：

```text
490bbdaa71cbd14b4dab9fbf6ac820d72b895b7fc5664b8a3a2ff454bb63a1c6
```

它保存原全部 20 轴、六个真实列组的 SHA、46 个真实线性帽与对角核、每步全部
46 个卷积帽和误差帽、公共半径、完整余项及所有门。资源文件为
[2026-11-13-inner-aux-cell12-spectral-bootstrap-r1-resource.json](../notes/2026-11-13-inner-aux-cell12-spectral-bootstrap-r1-resource.json)。
其它胞元/far 的完整主包为
[2026-11-13-inner-aux-cell12-outside-floor-r1.json.gz](../notes/2026-11-13-inner-aux-cell12-outside-floor-r1.json.gz)，
其 SHA 是 `28e68f029dc61e22192407ee8b8c49c549ee37ab957b31c76d082b1f1bbbf02d`；
该步独立通过 878 个门。

在本课题目录可复现，必须给新的输出名：

```bash
python computations/inner_aux_cell12_spectral_bootstrap.py \
  --out notes/fresh-inner-aux-cell12-spectral-bootstrap.json.gz --passes 32
```

所有显示小数只用于阅读。认证比较只使用输入的定向 dyadic、整数及 Fraction。
