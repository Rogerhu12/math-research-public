# 原 full47 的四基本CM首log：模4513²执行方法

日期：2026-11-27（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。

**状态：原有限算法与实现已写出，实际新值必须由执行回执取得。**
证明沿 [R1108](../results/R1108-original-CM-first-log-mod-q2-and-finite-residue-algebra.md)；
旧原95/836-jet及乘法来源沿R1090/R1104，
旧八CM源沿R1105，完整旧 $N=\#J(\mathbf F_{4513})$ 沿R1089。
没有用一个抽象同维Jacobian取代原 $X_{\rm ns}^+(47)$。

## 1. 有限新目标及原输入

仅求四个原CM点 ids $0,141,76,108$、判别式 $-3,-4,-7,-8$ 上的
$$
\lambda_y=q^{-1}\log_J(23y-C_\infty)\pmod q,\qquad q=4513,
$$
在同一原73维Hodge基中的完整列。
其它四CM列通过R1108的实际 $T_2,T_3$ 关系得到；
本次不重算原Gaussian高矩、全局高度或全辅助点扫描。
R1093的列是 $\log(B_qu_4)/q$，这里的列是 $\log(u_4)/q$，
两个对象在尚未应用真实 $B_q$ 前不得直接比较。

原大整数 $N$ 和它的JSON字符串SHA由旧已完成run消费；
$N\bmod q=551$。不在此次重算 $T_q$ 或群阶。

源消费者在runner内按已给95描述子和原产品规则重建输入，
逐项核先前完整证书；这仅供新模平方运算使用，
不登记为对旧结论的第二次计算。
所有raw矩阵和点坐标留在runner临时内存。

## 2. 同一原CM与Tate来源的模平方提升

新来源脚本沿R1108 §6：
真实Hensel提升 $\zeta_{47}\equiv2$；
用同一原95双phase Reynolds式重建836项。
全部23 cusp值保持原宽47归一，标准cusp那一行必须逐项等于
长jet的第零列，连模 $q^2$ 也相同。

旧CM模数、原47基、项链标记和Weil2在独立pure-Python/flint子进程中读取。
只传整数JSON；随后Sage父进程在同一不可约模数的模平方lift中运算。
Sage与wheel FLINT不得在同一进程装载。
真正的未分歧Frobenius由旧 $\bar\theta^q$ 的Hensel根定义；
不能把 $\theta^q$ 当作模平方ring automorphism。

47挠点的lift只除单位：曲线平方根Newton、原46链、逆斜率
$s=(x_{46}-x)/(y_{46}-y)$、$\tau=-s/47$ 和
$(x,y)\mapsto(x+2y\tau,y+(3x^2+A)\tau)$。
实核曲线、$46P=-P$、Frobenius及Weil根，
然后按原加法/heat完整重建95点值。
generic用值，Gaussian/cubic用原第一/第二heat消掉粗分支的共同零。
pivot归一的95行是原曲线真正的 $R=\mathbf Z/q^2$ 点；
所有旧mod $q$ 哈希必须吻合。

## 3. 自由像和核：只在真实平坦空间上提升

给定模平方矩阵 $A$，先以 $\bar A$ 选独立行 $I$ 和unit列 $J$。
每个square minor的逆用
$$
B=B_0(2I-AB_0)
$$
并核两侧乘积均为单位阵。
完整行像必须满足
$$
A=A_J\,(A_{I,J})^{-1}A_I
$$
于所有列，不能只查模 $q$ 秩。

对左核，令 $L$ 是非独立行，计算
$$
C=A_{L,J}(A_{I,J})^{-1}.
$$
必须核 $A_L=CA_I$ 的全部列；
随后每行 $e_l-\sum_iC_{li}e_i$ 就是完整自由核。
若实际余项仍有非零 $q$-torsion，停止该运算并报告真实不平坦，
不将它吞掉为有限域误差。

对试选的residual-gcd，先核mod $q$ 维数恰为最小Riemann–Roch维数；
维数较大时只换下一个section，不把那个可能跳维的核提升。
维数正确时special fiber没有额外gcd，
相对除子不交与 $H^1=0$ 才给出所需平坦性。

### 两个铅笔条件必须同时取核

对真正 $Z=H^0(\mathcal L^4(-E_1-E_2))$，
AddFlip使用
$$
U=\{s\in V_3:s\,s_0\in Z,\ s\,s_1\in Z\}.
$$
$s_0,s_1$ 是原无基点pencil，因此这恰是
$H^0(\mathcal L^3(-E_1-E_2))$，degree167、自由rank95。
实现把两组quotient residual矩阵横向拼接后**一次取核**。

分别做两个colon在有限域中合法；
但在模平方中，单个条件的中间space可能因special-fiber交点而跳维。
不能先对它假设平坦再相交。
终点 $H^0(\mathcal L(-\bar E_N))$ 只在有限域中读取；
模平方最终归一仍用上述同时条件。

## 4. 原除子链与全部cusps的准确初始类

每个代表是 $W_E=H^0(\mathcal L^2(-E))$，
$\deg E=167$、free rank95。

AddFlip首先以原95×95乘积取得
$H^0(\mathcal L^4(-E_1-E_2))$。
实际选定262个mod $q$ 独立乘积后，
Nakayama与相对Riemann–Roch保证它们就是完整空间；
未选的乘积不是需要保存的新数据。
上述同时pencil核给rank95的 $U$。
选 $s,u\in U$，用
$$
\{t\in V_2:tu\in sV_2\}
$$
读取剩余degree167的 $E_3$；核维95准确证明residual gcd为零。
真实类关系是
$[E_3-D_0]=-[E_1-D_0]-[E_2-D_0]$，
二进制链逐位保留这个符号。

取标准cusp为 $b$。
对于避开 $b$ 的有效 $P$、$\deg P=f$，
原初始colon按R1108引用的有限Miller方法，准确代表 $P-fb$。
这里先对 **一个完整degree22除子**
$$
P=C_\infty-b
$$
应用该方法，得到 $C_\infty-23b$；
23个cusp一项也没有删除。
不必先做22条点链再相加。

各CM点另代表 $y-b$，然后有限signed23链和准确负号给
$$
23(y-b)-(C_\infty-23b)=23y-C_\infty.
$$
实现始终保留这五个形式基元的整数label，
最终检查每个 $N$ 链为规定的 $\epsilon N$ 倍。
这既保23尺度，也保全部cusp项。

## 5. 固定有限étale代数与trace

选择 $f_0=s_0+c s_1$、$f_1=s_1$。
逐个核全部23cusps和八CM约化都避开 $D_0=\operatorname{div}f_0$。
R1108的存在界排除至多478+31个 $c$；
请求列出前512个常数，遇到非étale纤维则继续。

用真实836-jet构造
$$
W_0=(t/47)(F_0'F_1-F_0F_1'),\quad
A=V_2/(f_0V_1),\quad w=W/f_1^3\in A.
$$
通过 $V_3/(f_0V_2)$、$V_4/(f_0V_3)$ 和乘 $f_1,f_1^2$
获得原 $A$ 的乘法。必须实核 $w$ 乘法矩阵的det非零；
这正是 $D_0$ reduced 的判据。

选择实际 $a\in A$，核乘法charpoly $F$ squarefree、degree167，
及 $[1,a,\ldots,a^{166}]$ 可逆，
然后在同一个 $A\simeq\mathbf F_q[X]/F$ 中运算。
首试 $a=w$，然后固定若干坐标和seed前缀；
若该有限前缀没有primitive，不声称理论不存在。

原73个微分写成 $\omega_i=G_i\ell$，
$$
r_i=(G_i/f_1)w^{-1}.
$$
有限代数的全部trace由 $F$ 的Newton identities取得，
含全部167个几何共轭，无选取特定分支。
实际输出仅这些原矩阵、多项式和trace映射的SHA。

## 6. 强制终点归一与准确符号

$N$ 链只保证 $\bar E_N\sim D_0$。
先在mod $q$上读唯一
$\bar h\in H^0(\mathcal L(-\bar E_N))$。
对 $(E_N,D_0)$ 做一次AddFlip，
强制所选section的约化为
$$
\bar s=\bar h\bar f_0^2,\qquad
\bar u=\bar h\bar f_0\bar f_1.
$$
把这两个指定向量提升到实际自由rank95的 $U_R$；
不能直接任意lift其V3坐标。
两residual约化为不交的 $D_0,D_1$，
所以终点 $E'$ 满足
$$
\bar E'=D_0,\qquad[E'-D_0]=-\epsilon N[23y-C_\infty].
$$
实核 $W_{E'}\bmod q=f_0V_1$。

再取真 $h_{E'}\in W_{E'}$，强制 $\bar h_{E'}=\bar f_0\bar f_1$，
以原V2坐标读
$$
\delta h=(h_{E'}-f_0f_1)/q,\quad
\delta=(\delta h)/f_1^2\in A.
$$
R1108的真实积分公式是
$$
\lambda_y(\omega_i)=
\frac{\operatorname{Tr}_{A/\mathbf F_q}(\delta r_i)}{\epsilon N}.
$$
这里是正号：根位移的负号和末端AddFlip的负号相消。
整积分的高次尾在 $q^2$ 中，故此式是准确mod $q$值。

## 7. 执行、部分结果与保存

固定Sage10.6 image、四核，数学18000秒、reserve120秒。
独立field进程先完全退出，再fork四条Sage链；
每条链在完成时立即打印完整73列的小回执及SHA。
若另一条失败或总预算中断，已打印的完整case仍有效；
只为未完成的case另开新请求，不重算已成链。

所有旧输入只消费；新源码、方法、请求、run/job、
73维小结论及SHA可以入库。
836-jet矩阵、有限代数全乘法、点/中间除子/长链数据均不保存，
无artifact、Release或分块。
本计算即使全成也只付四个原CM首log，
不自动推出QC行秩、八盘唯一或Serre主目标完成。
