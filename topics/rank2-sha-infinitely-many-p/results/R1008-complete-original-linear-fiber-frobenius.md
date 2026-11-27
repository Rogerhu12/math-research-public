# R1008：原306维线性纤维的完整乘法张量与精确 Frobenius 后继

日期：2026-11-27。状态：下述算法恒等式及完整原输入保留已证明；源码只作静态检查，尚无本后继的公开数学执行回执。原 v8 未结束前不启第二份重作业。

## 1. 原输入及适用范围

始终用 R909、R924–927 已从原全局零点界证明的同一正规化

$$
A=\bigoplus_{i=0}^{305}\mathbf F_r[T]e_i,\qquad r=29\ \text{或}\ 41.
\tag{1}
$$

输入不是重建的猜测乘法表。每一个对称乘积都在实际 source 中按

$$
e_i e_j=\sum_{k=0}^{305}\sum_{e=0}^{d_i+d_j-d_k}
 c_{ij;k,e}T^e e_k,\qquad c_{ij;k,e}\in\mathbf F_r
\tag{2}
$$

表示；负上限的和为空。这里 $0\le d_i\le4$，完整 $306\cdot307/2=46971$ 对称行及每一 recipe 列都来自同一全局证明证书。有限图采用(2)，无穷图的原加权基采用

$$
e_i^\infty e_j^\infty
=\sum_{k,e}c_{ij;k,e}U^{d_i+d_j-d_k-e}e_k^\infty,\qquad U=T^{-1}.
\tag{3}
$$

不把(3)错误地再按 $U^e$ 求值。

本后继只在下列条件同时满足时选择新分支：

1. 调用者的原基素因子 $\pi$ 为一次；
2. 实际 $A/(I+\pi A)$ 的关系空间全为零，余维仍为306，free 坐标恰为原顺序 $0,\ldots,305$；
3. $\pi$ 的实际相对剩余次数为1；
4. 调用者自己的常数域 $k$ 的绝对次数为1或2。

其它关系商、其它基素次数及其它常数塔逐字保留 R974 的实现。这里只加速其完整线性纤维；没有把任意306维商认作无关系的原纤维。

原构造函数在设置关系和单位时还会调用乘法方法。新类先置 eligible 为 false，完整调用原构造函数，待所有原关系/单位检查结束后才检测上述条件，因此不会在原对象尚未初始化时调用张量。

## 2. 完整张量的求值与原坐标

令 $a$ 为调用者的实际 $\pi$ 根。有限图中(2)的系数变为

$$
\sum_e c_{ij;k,e}a^e,
\tag{4}
$$

无穷图中则为

$$
\sum_e c_{ij;k,e}a^{d_i+d_j-d_k-e}.
\tag{5}
$$

所有指数都在0至8间。源码按总权 $w=d_i+d_j$，对每个 shift 同时选出该完整 product block 的306个目标列。有限图选择 recipe $(k,\mathrm{shift})$，无穷图选择 $(k,w-d_k-\mathrm{shift})$，缺项用一个新增的全零列表示。逐块断言：

$$
\{\text{已使用 recipe 列，计重数}\}
=\{0,\ldots,\#\mathrm{recipe}-1\}.
\tag{6}
$$

因而每个原列恰好使用一次；没有靠随机抽样或初始几列确认整块。每个 $(i,j)$ 的结果分别放到 $i$ 乘法算子的第 $j$ 行与 $j$ 乘法算子的第 $i$ 行，随后把46971个原结果的两个次序全部读回。原单位的306个乘积也全部返回。

若 $k=\mathbf F_r$，这得到306个原素域矩阵。若 $[k:\mathbf F_r]=2$，保留调用者自己给出的生成元 $g$，逐个系数按

$$
k=\mathbf F_r\oplus \mathbf F_r g,\qquad
g^2=t+sg
\tag{7}
$$

拆成两个原素域坐标。源码逐个系数重建 $a_0+a_1g$ 并断言相等，且由调用者自己的 $g^2$ 求 $t,s$。不假设 $g$ 是原 $\omega$，也不另选不可约多项式或共轭根。原 $\omega$ 已由旧常数域对象保留。

记乘以 $e_j$ 的完整原算子为

$$
M_j=A_j+gB_j.
\tag{8}
$$

一般元素 $v=\sum_j(\alpha_j+\beta_jg)e_j$ 的乘法矩阵准确是

$$
M_v=
\sum_j(\alpha_jA_j+t\beta_jB_j)
+g\sum_j(\alpha_jB_j+\beta_jA_j+s\beta_jB_j).
\tag{9}
$$

因此这不是只够计算 Frobenius 的部分表；后续幂等元、残余点和原值计算所调用的完整 multiplication_matrix 仍得到同一个算子。所有列及实际目标域均不变。

## 3. Frobenius 及约化投影

每个原基向量的 $r$ 次幂严格按

$$
e_j^r=e_jM_j^{\,r-1}
\tag{10}
$$

计算。二次常数情形中，每一步的原行向量乘法由恒等式

$$
(a+gb)(A+gB)
=(aA+t\,bB)+g(aB+bA+s\,bB)
\tag{11}
$$

完成。右侧全部矩阵和行向量只在原 $\mathbf F_r$ 上运算，再用同一生成元 $g$ 还原。这里是 $r-1$ 次原算子作用，不是把系数 Frobenius 当成代数 Frobenius。

将306个(10)排列成 $B_r$。对任意原坐标行 $x$，

$$
\operatorname{Frob}_r(x)=\phi(x)B_r,
\qquad \phi(c)=c^r.
\tag{12}
$$

源码继续逐字使用 R974 的半线性复合规则

$$
(n,B_n)\circ(m,B_m)
=(n+m,\phi^m(B_n)B_m)
\tag{13}
$$

和实际 $[k:\mathbf F_r]$，得到 $q=\#k$ 的线性 Frobenius $F$。这里复合顺序按先作用左项再作用右项的原行约定。原单位在 $B_r,F$ 下的返回都保留。

对完整306维 Artin 代数，所有幂零元的幂零指数至多306，而 $q^2>306$。其约化商为有限域的乘积，Frobenius 可逆；因此 $\operatorname{im}F^2$ 恰是该有限代数的系数代数。令 $U$ 的行组成 $\operatorname{im}F^2$ 的基，令

$$
C=\operatorname{coord}_U(F^2),\qquad
T=\operatorname{coord}_U(UF^2).
\tag{14}
$$

$T$ 是 $F^2$ 在其像上的可逆矩阵，正确的原约化投影为

$$
P=CT^{-1}U.
\tag{15}
$$

保留完整检查 $P^2=P$、$F^2P=PF^2=F^2$、$\operatorname{rank}P=\dim U$、单位返回及 $F^3$ 同像维数。**没有把 $F^2$ 本身当成幂等投影。**

原回执的完整 residual/reduced/nilradical 维数、半线性矩阵、线性 Frobenius、实际投影摘要、原常数嵌入及所有复合指数均继续返回；新增的是整块线性纤维求值的来源和逐块摘要。

## 4. 内存生命周期与几何对象

同一个 factory 只缓存一个完整张量，键为调用者常数域对象本身、实际根及原图标志。另一个键到来时，先移除旧缓存再分配新张量；报告只保留小型来源/摘要记录，不保留旧矩阵。

二次常数一次保存 $2\cdot306$ 个 $306\times306$ 原素域矩阵，另有一个 product block 的求值临时量。这里只给出数组规模，不承诺未经公开运行测量的内存字节数或速度比。每次实际使用仍要在公开 Actions 中经过全部门。

本节没有改变：

- 原厚理想及其全部多项式行模；
- 余维、局部长度和幂零部分；
- 全部残余点、原坐标返回或完整范数的目标常数域；
- 四个交点条件、原两图、七个映射、三退化及18×9 shadow。

特别，线性纤维上可用(4)–(11)不等于允许把厚交点约化后丢去厚度。厚长度和完整范数仍由原调用链消费。

## 5. 与 R975、R986 的明确接线

新入口调用既有 v8 入口的 main，不拷贝或删除其验收条件。旧 v8 入口及原 producer 由逐文件 SHA256 固定。仅在该次离线进程中明确设置以下对象：

| 原对象 | 后继 |
|---|---|
| row、preimage、value、W transport 及入口内的完整 Hermite aliases | R975 完整 gcd-pair 提取、全尾 Popov 重置及原 bounded-shift fallback |
| closed-point 的实际 residual class | 本文的条件式完整张量类 |
| closed-point 与 Artin norm 内的原剩余域 constructor | R986 只对同一个原二次常数域采用规范化范数多项式，其它塔用 R974 |
| 实际 map builder | 调用同一个完整 equation-transport builder，并只在取得原 affine/常数/omega 后绑定上述类 |

R975 的每一步都是完整行的可逆行变换，attached block 同步作用；只有一行或两行确实生成整个当前列 gcd 时才用新提取，否则完整旧移位回退。每次快速提取后重置整个余尾，不把一次 gcd 计算当成完整 Hermite。其左块界仍为 $\max(D,3\delta+1)$；attached block 使用 R975 证明的真实较大界，未冒同界。

R986 对原 $k=\mathbf F_{r^2}$ 和实际 $\omega^2+\omega+1=0$ 使用同一 $\pi(T)$。若 $\pi$ 不定义于素域，$T$ 生成绝对次数 $2\deg\pi$；若定义于素域，由其在二次常数域上不可约可知度数为奇数，$T+\omega$ 生成所需绝对域。写平移后 $\pi=A+\omega B$，绝对多项式为 $A^2-AB+B^2$，并从 $\omega=-A(\alpha)/B(\alpha)$ 还原指定嵌入。两方向完整坐标空间返回仍保留。一次 $\pi$ 继续使用调用者的原常数域对象本身。

所有七个 Hermite 名字绑定都在开始与完整执行后检查对象身份，包括 W transport 内自己的两个 aliases，防止只改外层而漏下层。两个剩余域名字也同样检查。没有修改共享源码文件、另一正在运行作业或已经认证的输入。

新入口结束前先要求 v8 原本的全部几何门完成，再要求确实至少使用过一次完整新张量及实际完成 Frobenius；仅输出选择了新实现不算它已被消费。

## 6. 源码与当前执行状态

完整算法：

- [original_linear_fiber_frobenius.py](../scripts/original_linear_fiber_frobenius.py)，SHA256 为 70e94b3c9d221d52f3696e3d7875255b21b069f3fff888c7365b853ec8b6d1c5；
- [produce-original-linear-fiber-artinian-shadow.py](../scripts/produce-original-linear-fiber-artinian-shadow.py)，完整明确接线，保留原 v8 main；
- [R975](R975-original-pair-pivot-popov-reset-and-whole-attached-bound.md)与[R986](R986-original-quadratic-two-shift-native-residue-model.md)的恒等式分别由入口固定其源码摘要后采用。

本文登记时只做本地 AST、源码文本/摘要及绑定检查；没有在本地导入 Sage 或执行数学。v8 的旧运行仍是 run45882239615/job140124138541，已从真实日志见 negative 首块的完整厚因子推进，但四交/全厚范数/shadow 尚无终值。

本后继尚未接入 workflow/request，也未得到新的数学 PASS。后续必须先读 v8 的实际终点，再以同一公开 Actions 认证两份原 PASS、同一 r29/q2453/batch64、全部旧几何门运行。即使新运行全部通过，也只完成该原 shadow 的有限几何消费，不由此声称无穷素数或通常全 Sha 已完成。

