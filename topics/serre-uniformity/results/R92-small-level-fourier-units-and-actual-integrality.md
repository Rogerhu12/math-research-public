# R92：四个小水平的 Fourier 单位理想与实际整性

日期：2026-11-12；会话：serre-uniformity-resume2。

**状态：已证明，附整系数 Bézout 证书。**
严格排除 $p=41,47,59,83$ 的全部 exceptional 素数，再接 R69/R72 的实际尖点判据。
特别，R91 中仅存的两个类数三候选必须有整 $j$。本文不将整性写成实际曲线已排除。

## 1. 结论

沿 R72 的定义，令
$$
I_p=(P_0(\zeta_p),P_1(\zeta_p),P_2(\zeta_p))\subset\mathbb Z[\zeta_p].
$$

**定理 92.1。** 对 $p\in\{41,47,59,83\}$，有
$$
\boxed{I_p=\mathbb Z[\zeta_p].}
\tag{92.1}
$$
特别，这四个水平没有任何 exceptional 有理素数；结论不只限于 $\ell\equiv\pm1\pmod p$。

**定理 92.2。** 设 $p\in\{41,47,59,83\}$，无 CM 的 $E/\mathbb Q$ 有完整非分裂正规化子像，
且 $\lambda(I_p)=C^3$。若 R66 实际三次角色的某个相关中心值非零，则
$$
\boxed{j(E)\in\mathbb Z.}
\tag{92.2}
$$

**推论 92.3。** R91 的“小惯性、$h_K=3$、$c(\eta)=1$”整个实际分支只余
$$
\boxed{p=47,\quad D\in\{643,907\},\quad j(E)\in\mathbb Z,}
\tag{92.3}
$$
并保持 R91 所列两个准确的四次幂角色值。
另外，在上述四个水平，实际 $h(\mathcal O_c)=3$ 分支全部有整 $j$。
这些整点仍需排除；关于已发表整点分类所被指出的缺口，见 §5。

## 2. 实多项式与共同零点的精确关系

本节完整重述所需有限代数，因此不以未发表文献的猜想或有限搜索为输入。
取 $p\equiv2\pmod3$、非平方 $z\in\mathbb F_p$，在
$\mathbb F_{p^2}=\mathbb F_p[\tau]/(\tau^2-z)$ 中取三阶字符。
把 $(1+b\tau)^{(p^2-1)/3}$ 的三个可能值标记为 $1,\omega,\omega^2$，定义
$$
B_j=\{b\in\mathbb F_p:\ (1+b\tau)^{(p^2-1)/3}=\omega^j\},
\qquad P_j(X)=\sum_{b\in B_j}X^b.
\tag{92.4}
$$
取 $0\le b<p$ 作为指数。$B_0=-B_0$、$B_2=-B_1$，且若 $m=(p+1)/3$，
$$
|B_0|=m-1,\qquad |B_1|=|B_2|=m,\qquad
P_0+P_1+P_2=\Phi_p.
\tag{92.5}
$$
这些等式也由 Cayley 同构
$b\mapsto(1-b\tau)/(1+b\tau)$ 将 $\mathbb F_p$ 与范数一群去掉 $-1$ 识别而直接得到。
验证器同时从有限域定义重算它们。

令 $n=(p-1)/2$，以整系数递推定义
$$
C_0=2,\ C_1=T,\ C_{r+1}=TC_r-C_{r-1},\qquad
V_0=1,\ V_1=T,\ V_{r+1}=TV_r-V_{r-1}.
$$
设
$$
\Psi_p(T)=1+\sum_{r=1}^n C_r(T),
$$
以及
$$
A_p(T)=1+\sum_{\substack{1\le b\le n\\b\in B_0}}C_b(T),\qquad
B_p(T)=\sum_{b=1}^n(\mathbf1_{B_1}(b)-\mathbf1_{B_2}(b))V_{b-1}(T).
\tag{92.6}
$$
对任意 $p$ 次非平凡根 $\xi$，令 $t=\xi+\xi^{-1}$，则
$$
\Psi_p(t)=0,\quad A_p(t)=P_0(\xi),\quad
(\xi-\xi^{-1})B_p(t)=P_1(\xi)-P_2(\xi).
\tag{92.7}
$$
第一式来自 $\Phi_p(X)=X^n\Psi_p(X+X^{-1})$，其余来自两条递推。

因此只要证明
$$
\boxed{(\Psi_p,A_p,B_p)=\mathbb Z[T],}
\tag{92.8}
$$
便不可能在任意特征 $\ell\ne p$ 同时有三个 $P_j(\xi)=0$：
此时 $\xi$ 阶恰为 $p$，$\xi-\xi^{-1}\ne0$，所以 (92.7) 与 (92.8) 矛盾。
这包括 $\ell=2,3$，无需除以二或三。

对唯一的 $p$ 上方素理想，$\zeta_p$ 约化为 $1$，而
$P_0(1)=m-1$ 严格在 $0$ 与 $p$ 之间，故也不能含 $I_p$。
每个真理想均含于某个极大理想，于是 (92.8) 推出 (92.1)。

改变非平方 $z$ 只缩放 $b$，对应 $\zeta_p$ 的 Galois 共轭；交换三次字符取向只交换颜色一、二。
故选择下表中的 $z$ 不损失一般性。

## 3. 整数恒等式证书

证书给整多项式 $S_A,T_A,S_B,T_B$，满足
$$
S_AA_p+T_A\Psi_p=d_A,\qquad
S_BB_p+T_B\Psi_p=d_B.
\tag{92.9}
$$
所用常数如下。

| $p$ | $z$ | $d_A$ | $d_B$ | $\gcd(d_A,d_B)$ |
|---:|---:|---:|---:|---:|
|41|3|19433|41154708253|1|
|47|44|5171|116660767|1|
|59|56|9360469|14756907703243|1|
|83|80|13138147478627519|59240494644425942707858337|499|

前三行的整数 Bézout 关系分别是
$$
\begin{aligned}
336726116\,d_A-159\,d_B&=1 &&(p=41),\\
13423546\,d_A-595\,d_B&=1 &&(p=47),\\
7000417688003\,d_A-4440442\,d_B&=1 &&(p=59).
\end{aligned}
\tag{92.10}
$$
结合 (92.9) 已直接证明 (92.8)。

$p=83$ 不能仅用两个标量最大公因数作结；共同素因子可能来自不同的圆分剩余根。
证书在这里另给整多项式 $S_C,T_C$，满足
$$
S_C(A_{83}+2B_{83})+T_C\Psi_{83}=d_C,
\quad d_C=1796216889585274186350006290023565311.
\tag{92.11}
$$
严格有 $d_C\equiv96\pmod{499}$，故
$$
\gcd(d_A,d_B,d_C)=1.
$$
对应的三个整数 Bézout 系数也存于证书，并直接验证线性组合为一。
因为 $A+2B$ 属于 $(A,B)$，仍得 (92.8)。

全部整多项式系数以升幂顺序存于
`scripts/data/small_level_exceptional_units.json`。
验证器只作整数多项式乘加，并核对每条 (92.9)、(92.11) 的所有系数；
同时从 (92.4) 重建颜色、从 (92.6) 重建三个多项式。
因此表中常数不需要解释为某个数值近似 resultant，更不需要大整数的因数分解。
生成时使用有理数 Euclid 算法，再清分母；生成和验证均仅依赖 Python 标准库。

运行：

```bash
python -B scripts/verify_small_level_exceptional_units.py
```

加 `--write` 可从头重建证书。JSON 的 SHA256 为

```text
43301a794b2e4cede3329bbb938271fceea70d9b9e910673d74490880a1dd611
```

这证明定理 92.1。

## 4. 与实际椭圆曲线的衔接

在定理 92.2 的假设下，非零中心值经 R69 给真实有理点群有限的非零 Jacobian 商。
R72 的已证最优商整微分、尖点形式浸入及有理点排除，说明每一个 $j(E)$ 分母素数都必须 exceptional。
定理 92.1 使四个水平没有这种素数，故 $j(E)\in\mathbb Z$，证明定理 92.2。

R91 对 $h_K=3,c=1$ 的小惯性分支完整覆盖全部 $p>37$，只留下
$(D,p)=(643,47),(907,47)$。R90 给这两对实际周期非零，故至少一个相关中心值非零；
现在应用定理 92.2，即得 (92.3)。
同样，R90 对所有实际原始环类数三序均给非消失，所以四个水平的此分支全部有整 $j$。

## 5. 整性之后的准确缺口与文献纠正

Aurélien Bajolet、Yuri Bilu、Benjamin Matschke，*Computing integral points on
$X_{\rm ns}^+(p)$*，Algebra & Number Theory **15** (2021), 569–608，
Theorem 1.1（[DOI](https://doi.org/10.2140/ant.2021.15.569)，
[作者终稿](https://arxiv.org/abs/1212.0665)）声明 $11\le p\le97$ 的有理整 $j$ 点全部为 CM。

但 Furio–Lombardo，*Serre's uniformity question and proper subgroups of
$C_{\rm ns}^+(p)$*，[v2 原文](https://arxiv.org/html/2305.17780v2)，
Introduction，Claim 1.4 后明确指出该证明似有缺口，具体指向 Furio 博士论文 Remark 5.3.10。
本仓库此前两份文献笔记已经保留此警示。
本轮也核对了作者原文的准确措辞；仅凭发表状态不能消去这项已知异议。

因此，本篇**不调用 BBM 的完整整点排除，不声称 (92.3) 已不存在**。
这不等于证明 BBM 所声明的结论错误；目前缺少的是足以独立使用的完整证明或修补。
Furio 论文的正式存储页标记原文至2028年2月19日禁运，作者CV给出的公开PDF链接返回404，
故本轮没有读取该 Remark 的具体细节，也不臆测错误位置。
后续须核查公开算法、可复验数据或针对两个指定商域另给整点排除。

定理 92.1 的有限计算也不能推成所有 $p$ 的 Fourier 单位理想。
例如 $p=83$ 已显示单独两个逆分母的互素判据并非必要；统一论证必须控制真正共同理想。

引用接口：

- [R69](R69-forgetful-maps-and-unconditional-rank-zero-quotient.md)：真实有限秩零商。
- [R72](R72-optimal-quotient-cusp-immersion-and-exceptional-denominators.md)：完整整微分与非 exceptional 尖点形式浸入。
- [R90](R90-class-number-three-periods-and-actual-frobenius-exclusions.md)：全部原始环类数三序的实际非消失。
- [R91](R91-unramified-cubic-class-number-three-prime-bound.md)：全部十六类数三底域、全部素数的实际有限筛。
- [既有文献边界笔记](../notes/2026-11-12-literature-resume2.md) §1；[Furio 论文存储记录](https://tesidottorato.depositolegale.it/handle/20.500.14242/215414)：保留尚未修补的整点分类问题。
