# R150：W/b0 正 k 射线的 e 首值一中心由原 D/M 身份排除

日期：2026-11-29（Asia/Taipei）。会话 Astra-ISP-8542378f-20261127。GPT-6 Astra Pro（AI-assisted）。

**结论。** 在当前 W、完整 $b_0=0$、物理 $D_{\rm phys}\ne0$ 原图上，没有满足
$$
v(e)=0,\qquad \bar e=1,\qquad v(k)=a>0
\tag{1}
$$
的 $1009$ 进原解。证明只用原 $b_0,q_2,R_6$：原 $q_2$ 还给一个未倒 D 的精确身份 $D=M S$，而在本中心 S 是赋值环单位。它使第三矩式的两项具有严格不同的估值。

本文无新执行，也不使用物理 $f=0$、完整 NV 的 $N_5$、新中心分区或初始理想门。结合[正 k 射线仅余 e 首值正负一](R150-appendix-unit211-W-b0-positive-k-ray-only-e-plus-minus-one-original-centers.md)，本射线只须继续 $\bar e=-1$。本页不对该中心、其它射线或完整 W 排空作结论。

## 1. 同一点原定义

使用当前 W 的旧已付权环：
$$
u=e+1,\quad Q=ek,\quad \delta=1-Q,\quad \bar V=uk+2,
$$
$$
\ell=\frac{u((k+2)^2-2ek)}{k\bar V},\quad
m=u-\ell,\quad
M=\ell^2\delta-m^2=\ell(2u-\ell Q)-u^2,
$$
$$
J=2u(1-u)+\ell Q,\quad
A_*=4uQ-J,\quad
C_*=A_*m^2+J\delta\ell^2.
\tag{2}
$$
所有本页使用的 $u,Q,\delta,\ell,M$ 都已在当前原图支付，特别 M 非零。它们在赋值环中不必同时为单位，不能将原图单位与剩余单位混淆。

置
$$
\mu=2\lambda-3,\quad
A_2=2\lambda^2-2\lambda+1,\quad
B_3=4\lambda^3-6\lambda^2+3\lambda-1,
$$
$$
D=\ell A_2-T^2,\qquad
K=\ell^2B_3-3\ell A_2T+2T^3.
\tag{3}
$$
同一 $b_0$ 原一次关系和必要式为
$$
A_*T=uQ\ell\mu,
\tag{4}
$$
$$
q_2=2A_2C_*+2M\ell Q(3-4\lambda)
       -8uQ\delta\ell T^2=0,
\tag{5}
$$
$$
R_6=MK^2-4m^2D^3=0.
\tag{6}
$$
(5) 的准确重写见[负 e 射线原估值证明](R150-appendix-unit211-W-b0-negative-e-ray-complete-q2-R6-valuation-exclusion.md)；它由完整原 $a_\Delta$ 与 (4) 得到，不另除 $A_*$ 或任何值头。所有原条件始终取同一 $\lambda,T$。

## 2. 一个新的原 D/M 精确身份

由 (2)，有完整整式身份
$$
C_*=4uQ\delta\ell^2-MA_*.
\tag{7}
$$
将它代入 (5)，并用 $D=\ell A_2-T^2$，得到
$$
\boxed{
q_2=8uQ\delta\ell D
+2M\{\ell Q(3-4\lambda)-A_*A_2\}.
}
\tag{8}
$$
因此在原 $q_2=0$ 上，
$$
\boxed{
D=M S,\qquad
S=\frac{A_*A_2-\ell Q(3-4\lambda)}
        {4uQ\delta\ell}.
}
\tag{9}
$$
这里仅除旧已付 $4uQ\delta\ell$，没有 D 逆，也没有借 M 的首值非零或新权头。原尺度更明确地满足
$$
4uQ\delta\ell(D-MS)=q_2/2.
\tag{10}
$$
所以(9)是原必要式的同点身份，不是从模范数相等猜出的商。在后文，S 是否为赋值环单位将直接算出。

## 3. e 首值一时的权尺度

在含假想原解的 $1009$ 进代数扩张中，用 $\mathcal O$ 记赋值环、$\mathfrak m$ 记极大理想；上横线是约化。由 (1)，
$$
\bar u=2,\quad \overline{Q/k}=1,\quad
\bar\delta=1,\quad \overline{\bar V}=2.
$$
直接由 (2) 可得
$$
\overline{k\ell}=4,\qquad
\overline{km}=-4,\qquad
\overline{\ell Q}=4.
\tag{11}
$$
这些首值非零，所以 $v(\ell)=v(m)=-a$。

同时 $2u-\ell Q\in\mathfrak m$，且
$$
kM=(k\ell)(2u-\ell Q)-ku^2\in\mathfrak m.
$$
由于 M 是原非零量，置
$$
\gamma=v(M)>-a.
\tag{12}
$$
(12) 保留 M 任意更高的消失阶，包括 $e-1$ 与 k 同阶时的全部再次相消；没有预设 $v(e-1)$ 或 M 的下一个首值。

为得到 J 的准确尺度，在整个当前权图有
$$
J-Q=-\frac{2e^2k(2u-1)}{uk+2}.
\tag{13}
$$
故
$$
\overline{J/k}=-2,\qquad
\overline{A_*/k}=10.
\tag{14}
$$
特征1009中10非零，于是 $v(A_*)=a$；此处其剩余单位性是(13)的结论，不是删去其它中心的假设。

从 (7)、(11)、(12)、(14)，
$$
kC_*=4u(Q/k)\delta(k\ell)^2-kMA_*,
$$
第二项估值为 $\gamma+2a>a>0$，所以
$$
\overline{kC_*}=128,\qquad v(C_*)=-a.
\tag{15}
$$
另外
$$
\overline{uQ\ell}=8,\qquad
\overline{8uQ\delta\ell}=64,\qquad
v(M\ell Q)=\gamma>-a.
\tag{16}
$$

## 4. 不预设 lambda 的原 q2 半阶结论

先允许任意 $\lambda$，包括极点和零。若 $\mu\ne0$ 且 $s=v(\mu)\le0$，由 (4)、(14)、(16)，有
$$
v(T)=s-a.
\tag{17}
$$
因为 $\lambda=(\mu+3)/2$，有
$$
v(A_2)\ge2s,\qquad v(3-4\lambda)\ge s.
$$
由 (12)、(15)，(5) 的非 $T^2$ 两项分别满足
$$
v(2A_2C_*)\ge-a+2s,\qquad
v\{2M\ell Q(3-4\lambda)\}\ge\gamma+s>-a+2s.
$$
但 $T^2$ 项的估值恰是 $2s-2a<-a+2s$，所以独占最低项，不能使 $q_2=0$。因此
$$
\mu=0\quad\text{或}\quad v(\mu)>0.
\tag{18}
$$
两种情况都给
$$
\bar\lambda=3/2,\qquad
\bar A_2=5/2,\qquad
\bar B_3=7/2,\qquad
\overline{3-4\lambda}=-3.
\tag{19}
$$
没有把特征零 $\lambda$ 设为 $3/2$。

由原 (5)，
$$
kT^2=
\frac{2A_2(kC_*)+2(kM)\ell Q(3-4\lambda)}
     {8uQ\delta\ell}.
$$
分母是(16)已证明的赋值环单位，$kM\in\mathfrak m$，所以
$$
\boxed{
\overline{kT^2}=\frac{5\cdot128}{64}=10,\qquad
v(T)=-a/2.
}
\tag{20}
$$
特别 T 非零；原 $\mu=0$ 并未被漏掉，它不能满足(4)和(20)。

## 5. D 与 M 同阶，而 K 保留二阶首项

现在用精确原 (9)。由(11)、(14)、(19)，其分子和分母的剩余值分别是
$$
\overline{A_*A_2-\ell Q(3-4\lambda)}=0-4(-3)=12,
$$
$$
\overline{4uQ\delta\ell}=32.
$$
因此
$$
\boxed{S\in\mathcal O^\times,\qquad \bar S=3/8,\qquad v(D)=\gamma.}
\tag{21}
$$
这个步骤使用完整原 $D=M S$，不能只由此前 $kD$ 首值为零猜测 D 的阶数。

另一方面，K 中 $\ell^2B_3$ 的估值为 $-2a$，而另外两项 $\ell A_2T,T^3$ 的估值均为 $-3a/2>-2a$。故
$$
\boxed{\overline{k^2K}=4^2\cdot(7/2)=56,\qquad v(K)=-2a.}
\tag{22}
$$
所有用于(21)–(22)的非零常数均在特征1009中为单位。

## 6. 原第三矩必要式的严格矛盾

由 (11)、(12)、(21)、(22)，原 (6) 的两项分别有估值
$$
v(MK^2)=\gamma-4a,\qquad
v(4m^2D^3)=3\gamma-2a.
\tag{23}
$$
二者之差是
$$
(3\gamma-2a)-(\gamma-4a)=2(\gamma+a)>0
$
所以二者严格不相等。第一个非零项独占最低估值，故 $R_6$ 不可能为零。这排除了(1)的整个中心，包括所有 M 的高阶相消和全部可能 $\lambda$ 估值。

此证明没有为 $e-1$ 与 k 分段，也没有建立或假定一个模初始理想完备表。所有估值来自原有理式与已付单位，不能把结论外推为尚未处理的其它剩余中心为空。

## 7. 已用来源和准确后继

- [原 q2/R6 重写与负 e 整射线排除](R150-appendix-unit211-W-b0-negative-e-ray-complete-q2-R6-valuation-exclusion.md)，blob 93b1fab5b28a436beafaee41b2b3804d0c8de349；用于核对(4)–(7)。
- [正 k 射线仅余 e 首值正负一](R150-appendix-unit211-W-b0-positive-k-ray-only-e-plus-minus-one-original-centers.md)，blob be08067020cbcd72ea1587ba4b30137610200572；本文的 E=1 证明不依赖它的 N5 推导，但两条结论可合并。
- [旧完整原定义小源](../notes/2026-11-28-unit211-W-entire-b0-new-full-N5-two-low-original-scalars-8542.py)，blob 47281af16fdd0ad7500ecda377c3cb9f9d65e725。本文仅阅读必要定义，不重跑其标量或冻结输入。

本页是新原恒等式和估值推论，没有数学执行记录或新增验收门。正 k 射线的 $\bar e=-1$ 中心、其它四条权射线、完整整权模型、原方程及实际算子桥继续；普通 ISP 未由本文完成。
