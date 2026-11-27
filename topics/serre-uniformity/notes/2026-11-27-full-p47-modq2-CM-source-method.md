# 原 full47 的模4513²截面与四个CM点来源

日期：2026-11-27（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。

**状态：完整有限实现和纸面来源；本说明不声称尚未执行的模平方数值。**
对应脚本为
[scripts/full_p47_modq2_CM_source.py](../scripts/full_p47_modq2_CM_source.py)。
它是R1108后继的截面输入，不执行首对数、Miller链、局部高度或QC排点。

## 1. 固定对象与消费者接口

沿用R1090/R1104/R1105/R1108的原
$Y=X_{\mathrm{ns}}^+(47)$，
$q=4513$、$R=\mathbf Z/q^2\mathbf Z$，
$\mathcal L=\Omega^1(C_\infty)$。
95个描述子、全部23个cusps、标准Tate标架
$47\,dt/t$和836项精度均不改变。

父消费者先取得已认证的完整旧graded来源，再调用：

    lifted = build_lifted_source(
        req, old_graded["source"], old_graded,
        deadline=absolute_parent_deadline,
        callback=optional_callback,
    )

三个位置参数固定。deadline可显式传入，也可从父程序正在运行的
SIGALRM读取剩余时间；不另开总预算。
旧seed子进程再受min(父剩余时间, field_worker_seconds)约束，
后者至多1800秒。

结果含：

- **ring**：真正的 $R$。
- **polynomial_ring、polynomials[1]、matrices[1]**：
  原95个section的836项模平方Tate级数。
- **cusp_values[1]**：23×95的section值，已除留数的width47。
- **residues**：保width47的完整23×95矩阵。
- **CM_rows**：dict，键为实际id，值为95个模平方projective整数。
- **CM_records**：各点的完整标记、绝对coarse系数和证书。
- **CM_projective_values、CM_candidate_ids**：
  四点顺序严格为 $[0,141,76,108]$。
- **all_CM_rows_modq**：全部八个旧CM点的实际coarse95，
  只供基除子避点；它们没有提升到模平方。
- **certificate**：原来源、模平方来源与四个点的全部哈希。

父程序沿旧product_pairs构造 $n=2,\ldots,5$，实施R1108的
unit-pivot RR、末端归一与有限trace。
本模块不重选95形式或产品基，**也不将旧73行的整数代表冒作
模平方holomorphic格**。
真正holomorphic提升必须对本模块的23个留数解整核。

请求的source_sha256必须同时固定本脚本、本说明、
原Hodge/八CM/transfer/input模块以及原CM、transfer请求。
独立入口另固定graded模块，提供原graded请求及证书，
显式给Sage10.6和总时限/reserve。
父API可合入一个完整请求。

## 2. 原95全局来源的提升

整数2仅是 $\mathbf F_q$ 中的原47次根。
先对 $X^{47}-1$ 作一次单位Newton：

$$
\zeta=2-\frac{2^{47}-1}{47\,2^{46}}\pmod{q^2}.
$$

直接检查 $\zeta^{47}=1$、$\zeta\bmod q=2$。
原Original47Source的权一Tate式、完整两phase Reynolds式和
23cusp式只用单位分母；子类将模数和系数环置为 $q^2,R$，
其他方法原样使用。
特别保留：

$$
\sum_{x\ne0}
 \zeta^{aNx}e_xe_{\rho x}
+\zeta^{-aNx}e_xe_{\bar\rho x}.
$$

不以对称相位的一半替换，不删pure-imaginary描述子。
46个完整norm fibers各有24个半向量，最后乘2。

新的95×836矩阵和23×95值矩阵逐项约化，与父程序的旧完整矩阵
比较；另核全部留数和为零、标准cusp值行等于836级数常数列。
不以短前缀或rank替代完整等式。

R1108 §3.1已证明这些是真正的整sections，
836 jets在模平方仍注入。
这里没有任选有限域坐标的整数lift。

## 3. 独立子进程只再生旧输入

Sage进程从不导入pip的python-flint。
fresh-exec子进程先检查没有FLINT载入，再导入
python-flint0.9.0，并检查实际loader恰有一条
python_flint.libs内的FLINT。

子进程调用旧八CM程序，只再生：

1. 原235标签输入及其既定哈希；
2. 八个指定有理CM数的旧模型；
3. 旧select_actual_model的实际唯一targettag选择；
4. 原 $I=13J$ 和norm rescaling，Weil根准确为2；
5. 八条旧coarse95，并分别核原网格、短heat、coarse三哈希。

这是父程序选择基除子所必需的旧输入再生，
不是一次新认证，也不重复完整4513点扫描或高阶CM对数。
id76的旧25项链由原tag选择；不预设同一 $j$ 的fiber只有一条。
其余旧八点范围也沿原函数。
id141保原 $A=343,B=0,P=(653,525),Q=(3860,232)$。

只有四个基本点导出旧不可约模数、扩张次数、正规化 $P,Q$
坐标、实际Frobenius矩阵和原标记。
全部八点只导出旧coarse95，且父进程再次核其字面固定哈希。

父子之间只传JSON整数，没有共享FFI对象或未经核准的字节cast。
子进程使用共同绝对deadline；父程序超时或异常均kill并reap。
loader检查不排除整个Sage prefix，因为正确wheel也可安装在其下。

## 4. 真实未分歧模平方环与Frobenius

设旧模数为 $\bar F$，使用

$$
R_f=R[\theta]/F(\theta),
$$

其中 $F$ 是原系数列表的整数lift。
代码核 $\bar F$ 不可约、monic及原次数。
这是相同未分歧扩张的模平方整数环。

对于约化非零的 $a$，先在同一有限域求
$\bar b=\bar a^{-1}$，取其系数lift $b_0$，再作

$$
b=b_0(2-ab_0).
$$

每次直接核 $ab=1$。
所有点运算调用这一单位逆，不让非域环暗中除以 $q$。

设 $r$ 为 $\bar\theta^q$ 的系数lift，定义

$$
\theta^{(\sigma)}=r-F(r)/F'(r).
$$

核 $F(\theta^{(\sigma)})=0$、约化正确，
并核 $\sigma^f(\theta)=\theta$。
把
$1,\theta^{(\sigma)},\ldots,(\theta^{(\sigma)})^{f-1}$
存成 $R$ 上矩阵，后续所有Frobenius都用它。
**不使用 $\theta\mapsto\theta^q$ 充当模平方Frobenius。**

degree1直接用 $R$，旧线性模数仍保在证书。
有限域系数由原不可约模数重建。
FLINT的零及尾零编码由packet明确给出，
用于逐字核旧网格哈希，不作未经确认的跨field转换。

## 5. 同一有理CM模型和47挠点的提升

四点是判别式 $-3,-4,-7,-8$，
id顺序 $[0,141,76,108]$。
Gaussian保 $A=343,B=0$，cubic保 $A=0,B=1$。
其余取同一有理CM数 $j$ 在 $R$ 中的值：

$$
A=\frac{3j}{1728-j},\qquad B=\frac{2j}{1728-j}.
$$

不把旧模 $q$ 的 $A,B$ 整数代表当作新CM模型。
直接核判别式单位，以及
$6912A^3/(4A^3+27B^2)=j\pmod{q^2}$。

按R1108 §6.2，先lift $x,y$，用单位 $2y$ 做一步Hensel，
使 $y^2=x^3+Ax+B$ 在模平方成立。
沿原链

$$
1,2,4,5,10,11,22,23,46
$$

计算 $P_{46}$，设

$$
s=\frac{x_{46}-x}{y_{46}-y},\qquad \tau=-s/47,
$$
$$
P^\sharp=(x+2y\tau,\ y+(3x^2+A)\tau).
$$

最后近竖直线只用逆斜率。
其分母 $y_{46}-y\equiv-2y\pmod q$ 为单位。
代码核 $s\equiv0\pmod q$、曲线方程、旧坐标逐项相同，
以及 $[46]P^\sharp=-P^\sharp$。
所以这是原点唯一的47挠提升。

对提升后的 $P,Q$，再核真实Frobenius矩阵和Miller Weil配对
准确等于 $\zeta$。
其余2208点由原加法网格生成。
遇到非单位分母或非法竖直步立即失败，不换标记或改浮点。

## 6. 原G1、短heat与粗projective值

权一种子仍由原斜率链给出：

$$
e(P)=-\frac1{47}\sum_{\text{原链}}\text{累计斜率}.
$$

doubling和addition的累计法与旧脚本完全一致。
全网格核负号和真实Frobenius，
另核Gaussian/cubic的真实自同构矩阵。

generic只取 $e$；Gaussian取一阶；
cubic取二阶：

$$
e_1=-xe-y,\qquad
e_2=-2e^2y-4x^2e-2Ae-2xy.
$$

这些是导数而非Taylor系数。
二阶式保完整heat的 $A_2'=4A$，没有冻结 $A_2$。
Reynolds乘积的二阶交叉项因此准确为 $2e_1e_1$。

完整两phase求和后，才核结果确在基环 $R$。
三种原粗参数 $z=j-j_{\rm CM}$ 的绝对系数为

$$
\frac{(4A^3+27B^2)F}{124416A^2B},\qquad
-\frac{\partial F}{41472A},\qquad
\frac{\partial^2F}{331776B}.
$$

Gaussian的 $F$，cubic的 $F,\partial F$，
须在 $R$ 中**精确为零**，仅模 $q$ 为零不通过。
这就是R1103/R1105原KS尺度，没有新增2、3或CM周期。

每点选首个模 $q$ 非零的粗系数作单位分母，
给95个projective比值；分母值为1。
其模 $q$ 各项与原coarse95同分母归一结果相同。

## 7. 回执与后继边界

本脚本字面固定R1105真实
run45968484065/job140402824955的三组旧哈希。
对四个新模平方点逐项约化后核：

- 全部2208点的原坐标编码和相应heat阶网格；
- 95×(order+1)完整原导数；
- 原coarse95。

这些期望值不是本次计算后自取。
新证书另给模平方网格、短heat、绝对coarse和projective哈希。

全部23cusp值和95×836矩阵留在父消费者内存中直接使用；
公开回执只打印紧凑证书及四个95点值，
不把大矩阵写入仓库。
父程序仍必须付R1108的unit-pivot相对RR及末端有效除子归一。
未执行前没有新Abel对数、height或QC结论。

数学没有在会话或本地运行。
只有本公开仓库的Actions可执行，
失败保留明确完成的来源回执，未完成项仍未决。


## 8. 精确运行库接口核对

实现已按Sage10.6的官方源码核对，而未本地执行：

- [finite field coefficient construction](https://github.com/sagemath/sage/blob/10.6/src/sage/rings/finite_rings/element_pari_ffelt.pyx)：
  list按该有限域生成元的升幂系数解释；polynomial()返回唯一次数小于扩张次数的代表。
- [polynomial quotient elements](https://github.com/sagemath/sage/blob/10.6/src/sage/rings/polynomial/polynomial_quotient_ring_element.py)：
  lift()返回原多项式环中的规范低次代表。

新模平方环与旧有限域间只使用这些明确的系数接口。
若请求另列certified_CM_low_jet_hashes，代码要求其与嵌入的原八组三哈希完全一致。
