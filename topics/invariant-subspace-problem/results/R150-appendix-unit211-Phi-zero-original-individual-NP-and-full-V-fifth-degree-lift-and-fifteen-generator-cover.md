# Phi 原个别 N/P 与完整 V 的五次提升及十五生成元补图

> **2026-11-28 更正：本页经旧紧凑 R2 / Rbar 导出的原必要性、有限性、点数与排除声明已撤回。** 二重点一次坐标的平方被误写为 d1²，真实值为 2d0d1；完整更正和依赖边界见[原定义更正](../notes/2026-11-28-unit211-dual-germ-compact-mean-definition-correction-and-dependency-quarantine-8542.md). 已实跑的旧定义矩阵等式、次数与失败记录保留，不能再据此推原 Gram 条件或支付新模型单位。下文保留为原记录。


日期：2026-11-28（Asia/Taipei）  
范围：当前 unit211、$\Phi=0$、原物理 $D\ne0$ 图；使用已付的全图第一二次头。  
状态：原表达式、三个最高行的完整 QQ 组合及唯一实际执行全部完成。新权覆盖的整零集保留。

## 1. 结论

在当前原权环中存在可由下述固定原定义再生的非零多项式 $C_5^*(u,Q)$，其准确双次数为
$$
(\deg_uC_5^*,\deg_QC_5^*)=(89,58),
$$
有 $3312$ 项，固定规范 SHA256 为
`28ff68763c780b9fa6cc018ffd43e5feb12bcd5b1f0b9eed9cd9c71ccf35c9f8`。

在补图 $C_5^*\ne0$ 上，完整原必要代数有：

1. 一条原来源的五次关系
   $$
   C\lambda^5=a_0(\lambda)+a_1(\lambda)T+a_2(\lambda)z,
   \qquad
   \deg_\lambda(a_0,a_1,a_2)\le(4,3,3),
   \tag{1.1}
   $$
   其中 $C$ 只与 $C_5^*$ 相差已付权单位；
2. 一条首一十五次 $\lambda$ 消去关系；
3. 至多十五个权环生成元，可以取
   $$
   \{\lambda^j,\lambda^jT,\lambda^jz:0\le j<5\}.
   \tag{1.2}
   $$

这里“有限权模”指尚未对几何 $D$ 再局部化的必要代数。取原 $D\ne0$ 开集后，每个固定权纤维的点数仍至多十五，但不因此声称该开集在整个权环上仍是有限模。

整个 $C_5^*=0$ 权集继续保留。没有把 $C_5^*$ 当作全图单位，没有宣称所有权点的 $\lambda$ 纤维已有限，更没有宣称整 Phi 或普通 ISP 排空。

## 2. 三个完整原来源

沿用[完整原值与 I10 呈示](R150-appendix-unit211-Phi-zero-complete-original-values-exact-eighteen-by-two-presentation.md)中的记号：
$$
m=u-\ell,\quad \delta=1-Q,\quad
M=\ell^2\delta-m^2,\quad
A_2=2\lambda^2-2\lambda+1,\quad
B_3=4\lambda^3-6\lambda^2+3\lambda-1,
$$
$$
D=\ell A_2-T^2,\qquad
K=\ell^2B_3-3\ell T A_2+2T^3,\qquad
A_0=1+T/\ell.
$$
$b,c,\rho$ 仍是原两简单点权坐标，$\rho^2=\delta$；
$N_B=N_{B,e}+\rho N_{B,o}$、$P_B=P_{B,e}+\rho P_{B,o}$ 是原 Gram 的完整 $N_4$、$P_2$ 值，未替换原均值。

本条用的三式为
$$
\mathcal N
=D N_{B,o}
+\frac{2\lambda P_{02}}m K A_0
+\frac{4\lambda P_{02}m}{\ell M}D^2,
\tag{2.1}
$$
$$
\mathcal P
=D P_{B,o}
+\frac{3P_{02}}{2m}K A_0^2
+\frac{P_{02}(3m^2/\ell^2+\delta)}{2mM}KD
+\frac{6P_{02}m}{\ell M}A_0D^2,
\tag{2.2}
$$
以及完整 $V$ 来源
$$
\mathcal V
=D N_4(V_0)+\frac K{2m}\mathcal B(V_0,V_1)
+\frac{D^2}{M}N_4(V_1),
\tag{2.3}
$$
其中
$$
V_0=(1,\lambda-1-T,A_0,A_0),\qquad
V_1=(0,0,m/\ell-\rho,m/\ell+\rho),
$$
$\mathcal B(a,b)=N_4(a+b)-N_4(a)-N_4(b)$ 是真实双线性极化。

若 $d$ 为原度向量、$F_2=2f$、$\tau$ 为原迹、$\mathsf D$ 为原 Gram 作用，则该极化准确为
$$
\begin{aligned}
\mathcal B(a,b)
={}&4\tau(dab)-2F_2\tau(ab)\\
&-4\{\tau(a)\tau(db)+\tau(b)\tau(da)\}
+4F_2\tau(a)\tau(b)\\
&+\tau(a\,\mathsf D b)+\tau(b\,\mathsf D a).
\end{aligned}
\tag{2.4}
$$
源直接使用 (2.4)，因此保留 $V_0$ 与 $V_1$ 的二次交叉项；没有把最高三次项的相减冒充该二次项。

所有分母 $\ell,m,M$ 及原 Gram 恢复分母均属于当前已付权单位。没有倒置 $D$、最高 $D_2$、新的谱首项或商代数范数。

## 3. 同一原最高项与实际三行组合

按 $\lambda,T,z$ 同时取次数一，(2.1)–(2.3) 的次数上界均为五。原 $V_0$、$V_1$ 分别有次数上界一、零，故
$$
\deg N_4(V_0)\le3,\qquad
\deg\mathcal B(V_0,V_1)\le2,\qquad
\deg N_4(V_1)\le1.
$$
这使 (2.3) 的三个五次部分全部保留。

取 $\lambda=1$ 仅用于编码关联分次环的齐次部分，记编码变量为 $T/\lambda,z/\lambda$。它不是对原解作 $\lambda=1$ 特化，也没有使用 $\lambda^{-1}$ 作为原单位。三个最高式的实际返回还独立核
$$
D_2=2\ell-t^2,\qquad
K_3=4\ell^2-6\ell t+2t^3
$$
及由它们给出的全部五次表达式。

按已付的三条原均值规则，以固定次序约为 $(1,t,s)$ 三系数行，记为
$$
r_{\mathcal N},\quad r_{\mathcal P},\quad r_{\mathcal V}.
$$
每一步都是原均值商中的真单项式来源，没有把三生成元模假作自由、结合或无额外关系的代数。

实际运行中，这三条新行已经依次给秩 $1,2,3$。预备的 NS、PS、N1 与两条原歧义行没有进入最后组合。精确消元得到
$$
C e_0
=\beta_{\mathcal N}r_{\mathcal N}
+\beta_{\mathcal P}r_{\mathcal P}
+\beta_{\mathcal V}r_{\mathcal V},
\tag{3.1}
$$
三个坐标全部完整返回，$C,\beta_i\in\mathbb Q[u,Q]$。

固定的 $C$ 双次数为 $(91,59)$，共 $3432$ 项；SHA256
`34a036dbdaa19d243e20bc2033a21121c52818cbae94188fb00314c006a2eeba`。
它是实际三个有理组合系数分母的规范最小公倍式。实际只约去原 paid 列表中标记为 $\ell$ 的一次因子，即原 $L=Q\ell$ 因子及非零有理规范常数，得到 $C_5^*$。所有临时高斯主元都已通过 (3.1) 的完整多项式身份清回；最终只保 $C_5^*$ 的整零集，不能把它删除。

三个真实多项式乘子的规范哈希为：

- $\beta_{\mathcal N}$：`e195a0cc22dad04de89fb57d25d847028ccefc8e64586b47e661452e7daa69cb`；
- $\beta_{\mathcal P}$：`7e474ef009d771b60af918cd08c0fb7fccd3ed356cdfe417c98fb4fb1d2bd6cd`；
- $\beta_{\mathcal V}$：`7d85928491f4344daa9d10e8cdd27edcd53ec5d1a40cd9650e5bf3aa8ee39577`。

这些对象由原式和固定消元顺序定义；不保存其可重算大系数载荷。

## 4. 还原为五次关系，不删除 $\lambda=0$

把 (3.1) 齐次化回原变量。由于三个活动来源的原次数上界都是五，原组合
$$
\beta_{\mathcal N}\mathcal N+
\beta_{\mathcal P}\mathcal P+
\beta_{\mathcal V}\mathcal V
$$
在原均值约化后的五次部分恰为 $C\lambda^5$。它们属于完整原必要理想 $I_{10}$，所以去掉这一最高部分后即得到 (1.1)，其三个系数次数至多 $(4,3,3)$。

这是完整原多项式恒等式，$\lambda=0$ 也保留。没有从一个泛型最高矩阵可逆直接推出整 Phi 空性。

## 5. 十五次首一式与十五生成元

令 $e_0=1,e_1=T,e_2=z$，权为 $d_0=0,d_1=d_2=1$。在 $C_5^*$ 补图中 $C$ 为单位。用 $e_i$ 乘 (1.1)，再按原三均值规则还原二次积，得到
$$
C\lambda^5e_i=\sum_{j=0}^2 B_{ij}(\lambda)e_j,
\qquad
\deg_\lambda B_{ij}\le4+d_i-d_j.
\tag{5.1}
$$
因此
$$
\det(C\lambda^5I_3-B)
=C^3\lambda^{15}+\text{次数至多十四的项}.
\tag{5.2}
$$
对任何非纯对角最高项，(5.1) 的权差沿排列相消，总次数至少下降一。伴随矩阵恒等式在任意模上成立，不要求 $e_0,e_1,e_2$ 自由；故 (5.2) 给原必要代数的一条首一十五次 $\lambda$ 关系。

生成元界可直接更紧地从 (5.1) 证明：对 $\lambda^j e_i$、$j\ge5$ 使用该式，所得每项的总权 $j+d_i$ 至少下降一。以总权归纳，最终只需 (1.2) 的十五项。此归纳不要求单次替换的 $\lambda$ 指数本身严格下降。

这证明必要代数在该权补图上的十五生成元结论，并给每个固定权点的有限纤维界。$C_5^*=0$ 仍是完整未付支，不能据此提升为全权有限或排空。

## 6. 唯一实际来源与执行凭据

- [原 N/P 与完整 V 五次源](../notes/2026-11-28-unit211-Phi-zero-original-individual-NP-full-V-highest-five-source-8542.py)；
- [完整输入说明](../notes/2026-11-28-unit211-Phi-zero-original-individual-NP-full-V-highest-five-input-8542.md)；
- [小执行凭据](../notes/2026-11-28-unit211-Phi-zero-original-individual-NP-full-V-highest-five-source-8542-execution.json)。

源 blob：`8a0721538429165b3367df6529235f8b960325a7`；SHA256
`375e0cedd5c2d676a0e61af86b27dc62b102171b6b9d41322cec1cdec456a1c9`。

唯一 [run 46103882263](https://github.com/Rogerhu12/math-research-public/actions/runs/46103882263)，job `140852193366`：

- 内层退出码 $0$；
- 驱动时间 $5.532177389$ 秒；
- 最大 RSS $63092$ KiB；
- stdout $8980$ 字节，SHA256
  `0737b22ee847eda04f59ec6b33a4bcdff3a20227ab3ebf9400dbad01b1f74df2`；
- 源提交及真实 pull：
  `e37f1aa01136e8aaa89f630be1828d360ea0e5f0`；
- 真实 pull 时间 2026-11-28 03:39:30.972844 UTC，两份 README 均无差异。

本次没有重跑旧最高项单位门、全系数基点门、任何旧行列式或保存系数载荷。已成五次原组合直接构成本条证明，不设置额外复现门。
