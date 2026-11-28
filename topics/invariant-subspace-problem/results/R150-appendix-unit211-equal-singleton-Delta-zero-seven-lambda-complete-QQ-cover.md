# R150：h=k、Delta零的完整578次QQ覆盖、80基点界和七个余lambda

> **2026-11-28 依赖更正：** 本页 578 次/80 界/七个 lambda 的完整覆盖使用错误 compact R2 的 RWO、RWN1 cofactor，原覆盖与计数撤回。定义矩阵、准确运行和因式记录保留，不再支持整个原 Delta=0 的候选表。 参见[原定义与依赖隔离](../notes/2026-11-28-unit211-dual-germ-compact-mean-definition-correction-and-dependency-quarantine-8542.md)。

会话：Astra-ISP-8542378f-20261127。日期：2026-11-27（Asia/Taipei）。

**结论。** 在既定原 h=k 物理域，Delta=0 的所有原解只可能有
$$
 C_4(\lambda)C_2(\lambda)C_1(\lambda)=0,
$$
其中
$$
C_4=\lambda^4-3\lambda^3+3\lambda^2-\tfrac32\lambda+\tfrac38,\quad
C_2=\lambda^2-\lambda+\tfrac13,\quad C_1=\lambda-\tfrac13.
$$
三个完整 QQ 因子保留全部复根，共七个可能的 lambda。不同 (lambda,u) 基点总数至多80。**这不是七个原解，也未排除其Q或自由Gram纤维。**

## 1. 原输入及零首项的范围

接[整个碰撞Delta零的848基点定理](R150-appendix-unit211-equal-singleton-Delta-zero-two-QQ-curves-848-base-cover.md)与[紧凑原五行三列](R150-appendix-unit211-equal-singleton-global-compact-original-three-column-cofactors.md)。

h=k 独立原分析已支付等权、T0零、J=Q、Phi零及Q=1-u各整面，因此 Pf=T0(J-Q) 为单位。以原P1解f，保留 z=Qt，自由Gram不被选择；原另一线准确给
$$Pf\,NV=T_{\rm num}-bc\,\Delta z.$$
所以在Delta=0上，原解必须同时满足Delta=Tnum=0。

此前原式剥已付单位后的 D2、Tn2 对Q均至多二次。固定原次数消Q所得
$$P(\lambda,u),\quad M(\lambda,u)$$
次数分别为(28,3)、(124,17)，源于 D2/Tn2 与 D2/原RWO常数列cofactor。全部Q首项零仍被保留，且真QQ gcd(P,M)=1。新源只重建必要原输入，没有重跑旧factor/gcd证明门。

## 2. 真正的完整QQ一元覆盖

以u的固定原次数3和17构造20阶Sylvester：
$$R(\lambda)=\operatorname{Res}_u(P,M).$$
完整QQ结果实际次数841，规范系数287594字节，SHA256为
38ab53e2271bd017f640737369b5ca89bb7aaf63dd6c7016a4f46654ef49b580。

只剥原lambda单位A、B、lambda、S的gcd因子，每次除法乘回；gcd循环次数分别87、21、11、23。循环次数不表示整个同名多项式的幂。剩余首一多项式记R0，实际次数578，145941字节，SHA256为
dc9e1771e769aeb4e8d590dea2bb7a934a0d0fbfe91cf724c1367bfea36231b1。

每个原解均满足R0(lambda)=0。没有倒置u或Q的投影首项，没有只取一个数值根。真实R0的全部有理系数逐个检查为1009整，首一性给约化后仍为578次。

## 3. 独立原N1给第二个完整必要投影

使用已经证明的原RWN1常数列cofactor，保持D2关于Q的原次数2与该cofactor原次数11，固定消Q并只剥Q无关的原单位，得到新曲线
$$N(\lambda,u),\qquad(\deg_\lambda,\deg_u)=(151,19).$$
它有3036项、227759字节，SHA256为
6ba57d0ffed2dcb71f817f74acc45fd54a1aed4c5d3ad8c50521c427b47d5bc4。

取P、N的本原整数系数代表，固定u次数3、19定义真正整数Sylvester行列式B。无须先求B的全部QQ系数：整数矩阵的模约化与其行列式严格交换。实际模1009的完整B次数978，两个输入的u次数均保持。

实际全多项式扩展Euclid返回
$$s\,\overline{R_0}+t\,\overline B=g,\qquad\deg g=80,$$
s、t次数897、497；两项完整乘回已核，而非只核一部分系数。完整g系数保小回执。

R0为首一1009整，故任何首一QQ公因子也是1009整且约化保持次数。以上真实模Bézout因此给
$$\deg\gcd_{\mathbb Q[\lambda]}(R_0,B)\le80.$$
这里只用QQ公因子的Gauss引理，未把模因子视为QQ因子。

## 4. 为什么80也界不同(lambda,u)基点

固定物理lambda处若有r个不同的共同u值，则它们的Vandermonde评价列给第一、第二固定Sylvester矩阵各至少r维右核。第一矩阵的P、M没有共同竖直分量：否则对应lambda的最小QQ因子同时整除P、M，违背此前准确gcd=1。因此r有限，且在P恒零的退化纤维仍由非零M的次数17界住；第二矩阵的22列足够保留这些独立评价列。

对多项式方阵，在固定lambda处的核维数r使行列式在该处的零阶至少r。剥去的lambda因子在物理域非零，不改变第一行列式于该点的零阶。故R0、B的QQ gcd重数同时计入全部不同u，求和至多80。此论证保留所有u、Q首项零；并不界自由Q或Gram的全部纤维大小。

## 5. 完整QQ因子与两个整因子的排除

R0的真实QQ分解及其完整乘回为
$$R_0=F_{153}F_{345}C_4^6C_2^{17}C_1^{22}.$$
各因子首一，次数和153+345+24+34+22=578。此分解来自QQ，不来自模分解。

| 完整QQ因子 | 重数 | 与完整模g的公共支持次数 | 原结论 |
|---|---:|---:|---|
| F153 | 1 | 0 | 整个QQ因子的所有复根排除 |
| F345 | 1 | 0 | 整个QQ因子的所有复根排除 |
| C4 | 6 | 4 | 全部四个复根保留 |
| C2 | 17 | 2 | 全部两个复根保留 |
| C1 | 22 | 1 | lambda=1/3保留 |

F153规范系数9827字节，SHA256为
178069ed45e80756348ce1abd74aa27ceb59470a279d3131cc902be414db9a91；
F345为48267字节，SHA256为
1c367378a4f7db00ddecb42fcf334e496781b9704f43f853a26e14428587bb43。

每个实际首一QQ因子都逐系数支付1009整。若某个大因子还含原lambda，则它与B有正次QQ公因子；该公因子的首一整约化同时整除该因子的约化和g，违背表内准确gcd为1。因此排除的是两个完整QQ因子，不是若干模根。

剩余三个完整QQ因子的系数已在开头明列。它们的重数24、34、22合计80，与先前界一致；这不把对应原权纤维的代数重数或解数直接定为这些数。

## 6. 真实执行和后续原返回

源：[2026-11-27-unit211-equal-singleton-Delta-zero-exact-lambda-cover-N1-Gauss-8542.py](../notes/2026-11-27-unit211-equal-singleton-Delta-zero-exact-lambda-cover-N1-Gauss-8542.py)。

源SHA256：
cf0a6c92694f23657a19a64610e185dc582631de517ab7d530e60522aaf59c1a。

实际run 46026556334 / job 140599338154；驱动2.522012006秒、源2.462914379秒、峰值85076KiB、exit0。stdout14657字节，SHA256
5a08e64debc25aea3ea6056aa53d5ae4cfa2668254da53529e2fbb39c21975ec。

真实pull于2026-11-27 15:37:41.916833 UTC读到ac40c96b0cfb3758fbf8bd380d18ca288a23601f，两README无变化。只保存源、参数、哈希和小回执，不保存可再生的大投影系数。

继续在C4、C2、C1的完整常数代数中返回原Delta、Tnum及全部必要Gram条件。所有未付参数首项零须保留。h=k整支及普通Hilbert ISP都未完成。
