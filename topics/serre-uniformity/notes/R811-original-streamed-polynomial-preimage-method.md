# R811 后继：原正常环的流式完整极前像实施契约

状态：执行契约与准确程序；本文件不报告原 $A/B$ 的极除子已经计算完成。
数学依据为 [R811 完整前像与两图证明](../results/R811-original-normal-polar-ideal-preimages-and-two-chart-certificates.md)。
首 scope 的 regular-multiplier 程序、方法和证明保持原样；本文件定义独立后继 scope。

- 主核：`scripts/R811_original_polynomial_polar_preimages.py`。
- 多项式模块：`scripts/R811_exact_L_polynomial_modules.py`。
- 原字段 adapter：冻结的 `R754_original_periods_and_Hom_kernel.py`，
  SHA-256 `f196cb805d1ca91e8995866032a0a3ec3f96aac06e03b67a7c1f196fff759251`。
- RESULT：`R811-original-polynomial-polar-preimages`。
- scope：`complete_base_y_two_chart_polar_preimages`。
- FINAL：`p41-original-polynomial-polar-preimages-certificate.json`。
- CLI：`--config --proof --method --module-helper --field-core --retained --output --budget-minutes`。

所有新算术只在公开仓库 Actions 运行。没有原 A/B 的真实成功 producer 时，
请求保持 pending，不填入假 run、SHA、核秩或极除子次数。

## 1. 最小真实来源闭包

后继只读取原首 scope 的成功 producer，标签仍为 R811，
但来源 RESULT 是 `R811-original-regular-multipliers-and-polar-preimages`，
来源 scope 必须是 `base_regular_multipliers`。
其 run/source/core/full manifest/certificate 和 source-bound
stage inventory 全部绑定到请求。

数学输入是两个 target index、各自十四个有理分量的 certified index，
以及两个图上的准确 matrix row blocks。分量确为零时只消费原准确零证明；
非零分量不能从模零推成零。原 normal basis 的秩272、次数
$(0,1^{144},2^{127})$、原 $n$、两图相同截面次数5和原B非零声明都须由真实 producer 给出。

不再次读取旧 Hodge、period、Laurent、Fourier、S5 或 Dixon 大输入。
R811首 scope已经在原第一列和全部多项式交换子上识别了真正乘法矩阵；
这里不重新求这些矩阵。

原 $b$ 的最小多项式直接读取两个 target 的
`target_configuration.original_b_model`，并准确比较A/B相等。
该字段的已成传递是 R809 target ← R803 mixed scalar ← R774 原模型见证。
因此没有必要为同一个最小多项式重新下载已过期的R735原 artifact。
这只是消费已有准确模型，不选择新的根或嵌入。

## 2. 原字段换基与多项式乘法

原输入的十四个有理分量是
$$
b^0,\ldots,b^6,\quad sb^0,\ldots,sb^6,\qquad s=1+2\zeta.
$$
冻结R754字段用 $a(b)+\zeta c(b)$ 存储。只作
$$
a(b)+s\,c(b)=(a(b)+c(b))+\zeta\,2c(b).
$$
不改变 $b$，不另乘 $\zeta$，不重插已消掉的共同content、分母或任何82尺度。

设 $L=\mathbb Q[b,\zeta]$，$b$ 的原最小多项式次数7，$\zeta^2+\zeta+1=0$。
$L[z]$ 系数在 $b$ 上的度至多6。乘两个 $L[z]$ 多项式时可将
$z^i b^j$ 临时编码为 $X^{13i+j}$：任何两个 $b$ 次数之和至多12，
所以没有一项越过下一条 $z$ 系数的13槽边界。
对 $\zeta$ 的两分量作
$$
(a+\zeta b)(c+\zeta d)
=(ac-bd)+\zeta\bigl((a+b)(c+d)-ac-2bd\bigr),
$$
再按13槽解包，每一槽准确模原七次多项式。
这给准确乘法；stride13不是辅助素数或数值近似。

除法余式使用原 $L$ 的非零首系数逆；每步严格降低余式次数。
xgcd最后准确核
$d=sa+tb$、$a=da_1$、$b=db_1$ 和
$sa_1+tb_1=1$。
所有零判断都是原字段的准确零。

## 3. 不可变原矩阵和两个工作列

每图先建立独立label
`R811-polar-{tau|sigma}-source-pair`，存
$$
P=[M_A\mid-M_B].
$$
它的544列、每列272项按16项tile存储。
从原十四个有理matrix block只做一次字段合成；
已完成的tile在续算中按同源SHA复用。

约化工作矩阵使用另一label，初始只借用这些不可变列。
任何工作清理都不能删改来源label的列。
最终直接检验 $PH_{\mathrm{joint}}=0$ 时，
明确使用这个未约化的原 $P$，不是已经成为 $[\Gamma,0]$ 的工作矩阵。

普通一次二列变换最多驻留两个16项tile与少数算子多项式，
不把两个完整 $272\times544$ 的 $L[z]$ 数组同时装入内存。
恒等作用的那一列直接沿用旧spec，剪切不重复写一份相同主元列。

## 4. 原子操作和中断恢复

每次操作分为三个已有明确边界的对象：

1. 完整plan保存真正的初等矩阵 $E$、当前两列的spec、控制位置和前receipt；
   保存之前已经准确核其行列式是 $L^\times$ 中的单位。
2. 每个输出tile独立原子落盘，绑定plan和两个输入tile；
   只有全部所需tile齐全后才写新的列index及完整operation receipt。
3. 最后原子替换current checkpoint，一次同时改变两个列引用和transcript尾。
   在此之前旧checkpoint仍指向完整旧矩阵；在此之后新checkpoint只指向完整新矩阵。

若进程停在plan或tile之后，续算读原plan和已成tile，不重新求已成Bezout算子。
若停在receipt之后、current commit之前，只完成commit。
若停在commit之后、清旧列之前，构造器先按最新receipt完成清理。
清理逐tile执行，列index最后删除，保证中途再停也仍能找到剩余待删tile。
只删本工作label拥有且不再活动的列，原始借用列保持不可变。

小plan、receipt和前项SHA全部保留；大型工作矩阵只保当前引用的版本。
这些检查是程序续算语义，不是额外人工批准流程。

## 5. 完整核、联合Hermite和直接多项式等式

第 $i$ 行对剩余列作完整Euclidean消元，准确得到
$PE_1\cdots E_m=[\Gamma,0]$。
每一个swap、单位缩放、shear和Bezout算子都保留。
不把模秩或几个零列冒充全核。

从 $(0,I)^t$ 出发，逆时间**左乘原 $E_j$ 本身**，得到整个核基
$(J,W)^t$。
存储器按真正的右矩阵
$$
E=\begin{pmatrix}s&-b_1\\t&a_1\end{pmatrix}
$$
记录：右列作用使用 $E_{jk}$，逆时间的左行作用使用 $E_{kj}$。
两种方向不交换，也不对 $E$ 取逆。

把核按纯IO转置为列布局后，继续用前272行J作pivot，
同一列操作同时运输后272行W。
得到J的列Hermite形H；此时仍是整个前像的一组基。
先完成这一步能缩短随后直接检验的多项式，不影响全核证明。

最终额外直接计算
$$
M_AH-M_BW=0
$$
的全部 $272\times272$ 项，在原 $L[z]$ 上逐块准确相加。
每一个输出列/16行块都有独立的current部分和、已消费输入列位置及完成证书。
续算不重新累加已经原子记录的部分和。
此检验和原可逆transcript同时存在：直接等式只证明包含，
可逆transcript才证明前像全部性。

不生成特征零Krylov矩阵或它的逆。

## 6. 两图相容性与实际次数

两图各自使用首scope已成的真正regular矩阵。
A/B在第二图共同的 $t^5$ 已准确取消。
理想函数坐标的过渡仅为
$$
D(t)H_\tau(1/t),\qquad D(t)=\operatorname{diag}(t^{-\epsilon_a}),
$$
没有额外截面次数因子。

每个包含方向都用目标三角基准确求解。
Laurent系数规范为 $t^k p(t)$，$p(0)\ne0$；
除以对角多项式时先取出其 $t$ 因子，其余必须在 $L[t]$ 中整除。
所以每个约化后分母只能是常数乘 $t$ 的幂。
每一步都准确乘回，完整余向量最终必须为零。

反向在 $z$ 变量下的公式仍为
$\operatorname{diag}(z^{-\epsilon_a})H_\sigma(1/z)$，
因为 $D(1/z)^{-1}=\operatorname{diag}(z^{-\epsilon_a})$；
不是把指数随手变为正号。

最后才计算
$$
\deg E=\sum_i\deg(H_\tau)_{ii}
+\sum_i\operatorname{ord}_{t=0}(H_\sigma)_{ii}.
$$
准确计入所有剩余域次数和非约化重数。
原映射的1206只用于最后独立比对；不参与选主元、改H、补秩或调倍数。
若不符，保留真实degree stage并让该scope未完成。

## 7. 已闭合单图的保存边界

单图完成完整核、联合Hermite和原 $M_AH=M_BW$ 的直接准确检验后，
其大型source-pair、reduced-pair和reverse-kernel工作矩阵已不再供后继使用。
这时才清除它们，保留最终联合H/W大矩阵。

清理前，将每128次操作的原plan/receipt gzip文件**原字节**装入临时tar archive，
再逐member核原bytes/SHA，保存小archive index后才删原单文件。
不更改操作系数、不重放算术、不伪造新来源tag。
source/final/index等小证据继续保存；历史大文件的原spec在pruning plan里可查。
中途退出后，先核已成archive再继续删除，不能重新做数学。

所有这些可重算数据只进入当前一日Actions artifact；
Git和Release只存源代码、参数、run和哈希。
归档分组是活跃续算载体的IO整理，不用于把数据分块提交到Git。

## 8. 独立的确定性generic验证

专门的公开workflow
`serre-p41-generic-polynomial-module-validation.yml`
消费同一多项式模块，另取
$\mathbb Q(c,\zeta)$、$c^7=2$ 和曲线 $u^2=z$，
明确标为generic，绝不说它是原CM模型。

令 $\alpha=c+\zeta$，输入
$$
\frac{u^2-\alpha^2}{(u-\alpha)^2}.
$$
真实极理想是 $(u-\alpha)$，故该测试确有非平凡共同因子消去。
两图完整核、Hermite、直接矩阵等式、双向Laurent包含和度数1都与闭式答案比较。
还用独立字段系数卷积检验最高 $b$ 度12的stride13乘法。

另四个子进程分别在完成tile、receipt、current commit和清旧首tile后
真正调用 `os._exit(97)`；重新启动后，完成的数学结果文件SHA
必须与不中断基线完全相同。
运行编号和真实成败另在日志登记，不在本契约预填成功。
该workflow与实际producer并行，**不作为原producer激活门禁**。

## 9. 输出边界

只有两图完整前像、原矩阵直接等式、双向重叠包含和实际次数都完成，
才写 `original_base_map_polar_divisor_computed=true`。

输出继续明确为false：
small-divisor/radical提取、五函数DAG、原 $\eta$、刚性化函数、高度，
以及抽象原 $A$ 中任何未经认证的同源核前像。
原函数A/B的常数、原 $b$ 和所有已成normalization均不随理想基首一化改变。
