# R150 补充：Phi=0、rank-one 值碰撞的精确原必要曲线与 2051 点覆盖

日期：2026-11-27（Asia/Taipei）  
会话：Astra-ISP-8542378f-20261127

## 1. 范围与本次结论

沿用已刊原 U-value atlas 的碰撞图及
[单首一 ell 的 8918 点覆盖](R150-appendix-unit211-Phi-zero-rank-one-value-monic-ell-8918-point-cover.md)、
[原 ell 单位目标消去](R150-appendix-unit211-Phi-zero-rank-one-value-actual-ell-unit-target-cancellation.md)。
本稿始终施加原 $\Phi=0$、$z_n=TB_3-A_2^2=0$ 与原物理单位，交换两 singleton 标签后取 $h=1$。
旧 atlas 的参数化不是本稿的新结论。

**结论。** 在这个选定的有序 $h=1$ 图中，所有实际原解的不同参数对 $(\lambda,\rho)$ 至多 **2051** 个；每一对仍保留原首一二次的两个 $\ell$ 根。因此不同 $(\lambda,\rho,\ell)$ 至多 4102 个。这里没有证明候选为空。$k=1$ 图由原 B/C 交换覆盖；未经说明，不能把两有序图的并集仍计成 2051。

本次严格加强不依赖计算任何大结式：新的精确 QQ 曲线互素性，结合固定 27 阶 Sylvester 的次数界和全部退化纤维上的核重数，已足够给出上述数目。

## 2. 同一个原图、原来源与原单位

记

$$
A_2=2\lambda^2-2\lambda+1,\qquad
B_3=4\lambda^3-6\lambda^2+3\lambda-1,\qquad
\gamma=A_2^3/B_3^2.
$$

原碰撞图为

$$
c=\gamma,\quad b=\ell-\gamma,\quad h=1,\quad
k=1+B_3/A_2,\quad
T=A_2^2/B_3,
$$

$$
p=1+\rho,\quad q=1-\rho,\quad Q=1-\rho^2,\quad
u=p\ell-2\gamma\rho.
$$

$\Phi=0$ 恰是

$$
-2p^2\ell^2+(8p\gamma\rho+6p-Q)\ell
-8\gamma^2\rho^2-12\gamma\rho-4+Q=0. \tag{2.1}
$$

其首项 $-2p^2$ 是原单位。所有计算在 (2.1) 的首一二次商中进行，保留非约化纤维。底环只倒置已付的
$\lambda,\rho,p,q,A_2,B_3,4\lambda^2-5\lambda+2$。

原两条恢复式给 $f=f_0/P_f$、$t=t_0/(bP_f)$，其中 $f_0=-P_c$，$t_0$ 由完整原 $N(V)$ 线给出；$P_f=T_0(J-Q)$ 已由整 $T_0=0$ 与整 $J=Q$ 排除支付。令 $H=bP_f$。共享原 Gram helper 直接构造 $H$ 倍原 Gram，因此均值行是 $H^2$ 倍原行，$N/P$ 行是 $H^3$ 倍原行。没有使用代数范数倒数。

对于同一点的两条原行 $r,s$，原单位目标计算给出了完整身份

$$
\delta\,H^3=A r+B s
\quad\hbox{或}\quad
\delta\,H^3\ell^3=A r+B s. \tag{2.2}
$$

所有临时 Cramer 分母均已清入 $\delta$，并逐系数乘回 (2.2)；只除去底环中已经支付的单位因子。因此所得必要曲线在临时主元为零处仍有效。乘 $\ell^3$ 的新目标依赖已付的整个 $\ell=0$ 排除，不以 $\operatorname{Nm}(\ell)$ 为单位。

## 3. 本次实际 QQ 因式与互素性

自含源重新生成所需同源原行及 (2.2)，对下列四个实际必要 core 做精确 QQ 因式分解，每项均完整乘回。表中次数按 $(\lambda,\rho)$ 排列。

| 原行与实际目标 | 二元次数 | 总次数 | 项数 | 实际 QQ 分解 |
|---|---:|---:|---:|---|
| $(E_1,E_B)$，$H^3$ | $(83,15)$ | 98 | 1344 | 一个一次幂因子 |
| $(E_1,E_C)$，$H^3$ | $(77,14)$ | 91 | 1170 | 一个一次幂因子 |
| $(E_1,\ell E_1)$，$H^3$ | $(76,15)$ | 91 | 1232 | 一个一次幂因子 |
| $(N_1,\ell N_1)$，$H^3\ell^3$ | $(75,13)$ | 88 | 1064 | 一个一次幂因子 |

本稿的覆盖论证只需要这些精确乘积与互素性，不把因式分解当作任何原单位判定。令第二行 core 为 $F$，第四行 core 为 $G$；实际完整 QQ 计算得

$$
\gcd_{\mathbb Q[\lambda,\rho]}(F,G)=1. \tag{3.1}
$$

两者的规范系数 SHA256 分别为：

- $F$：$10868a19c5de665f9c4dc56a2f6e2c7196081de1e2a0fd9f74b3c1dbbc18ac23$；
- $G$：$d23259f5b889511937e4b6d034a0eebccdae9e4f4f5f007e8d4dac89500ba879$。

同次也核了第三行与第四行的 QQ gcd 为 1。普通总次数 Bézout 给 $91\cdot88=8008$，但下面使用实际二元次数得到更强的 2051；8008 不作为最终界。先前 ca53 那次所选另一对的 9009 没有改进旧 8918，也没有被当成新界。

## 4. 固定 27 阶 Sylvester 保全部首项退化的计数

将 $F,G$ 看成 $\mathbb Q[\lambda][\rho]$ 中的多项式，其固定 $\rho$ 次数分别为 $m=14,n=13$。取完整 Sylvester 矩阵 $\mathcal S(\lambda)$：其前 $n$ 行是 $\rho^jF$，后 $m$ 行是 $\rho^jG$ 的全部 27 个系数，缺项补零。此矩阵只用于证明，不在本次执行中计算其行列式。

由 (3.1)，$F,G$ 在 $\mathbb Q(\lambda)[\rho]$ 中互素，故

$$
R(\lambda)=\det\mathcal S(\lambda)\ne0.
$$

每个行列式项恰选 $13$ 个 $F$ 系数和 $14$ 个 $G$ 系数，所以

$$
\deg_\lambda R\le 13\cdot77+14\cdot75=2051. \tag{4.1}
$$

不需要任何 $\lambda$ 处的 $\rho$ 首项非零。固定 $\lambda_0\in\mathbb C$，设共同零点有 $r$ 个不同有限 $\rho$ 值 $\rho_1,\ldots,\rho_r$。两个多项式不可能都在这条整垂直线恒等于零，否则 $\lambda-\lambda_0$ 是公共因子，违背 (3.1) 在 $\mathbb C$ 上的共同曲线排除。因此该纤维有限，且 $r\le14$。

对每个共同根，

$$
v_j=(1,\rho_j,\ldots,\rho_j^{26})^\mathsf T
$$

都是 $\mathcal S(\lambda_0)$ 的右核向量。不同 $\rho_j$ 的 Vandermonde 列独立，故该矩阵的亏秩至少为 $r$。取一个常数可逆列变换，把这些核向量放到末 $r$ 列；变换后这些列的每个多项式条目都被 $\lambda-\lambda_0$ 整除。行列式于是给出

$$
\operatorname{ord}_{\lambda_0}R\ge r. \tag{4.2}
$$

这个证明包含任一或两个首项降阶、重根、临时 Cramer 主元为零等纤维，未从这些纤维除去任何参数。

对全部有限 $\lambda_0$ 相加，(4.1)–(4.2) 得不同共同仿射点数至多 2051。由 (2.2)，每个实际原解都映入这共同点集，故得到第 1 节的结论。等价地，可将 (3.1) 的两条曲线双齐次化到 $\mathbb P^1\times\mathbb P^1$，交数正是 $77\cdot13+14\cdot75$。

## 5. 自含源与真实执行

源：
[exact-original-core-factorization](../notes/2026-11-27-unit211-Phi-zero-rank-one-value-exact-original-core-factorization-8542.py)。

- 源 blob：$3ebc53021692bc358cef21a55509788198e6a146$。
- 源 SHA256：$c36f8f1ef5829b11432e8dfcf76a5dbcc0bf3d6139e69b86fc66c16accc9b472$。
- 原始 Actions run/job：45993367371 / 140486548450。
- 实际内层 exit：0；2.734921032 秒；52388 KiB。
- stdout：10973 字节；SHA256 $3fc89253abc8ee92db255b010390503b4a9a35c203afee5c2f856d6135ec4326$。
- 源所在实际 main：$eba5378edc2634aec5d7091669da52d5b6389606$。
- 11:47:58.203203 UTC 的真实 pull 后，两 README blob 均无变。

源使用已刊、逐 SHA 核对的 monic-six scalar helper 与 rank-one cleared Gram helper。原八行已在 1.515 秒完整生成，四因式及三个实际 QQ gcd 在 2.672 秒完成。本次没有运行 27、28 或 29 阶 QQ 结式，没有构造任何 2051 或 2113 次覆盖多项式的系数，也没有声称整 Phi 面、整个碰撞图或 ordinary ISP 完成。
