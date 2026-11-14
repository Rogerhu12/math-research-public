# R295：五个普通盘的真实三同源支撑与完整主函数范数

日期：2026-11-13。状态：**已证明并实际执行。**

本结果对仍需第二方向判断的五个普通盘
ORD_j12、ORD_j15、ORD_j19、ORD_j27、ORD_j32，
构造真正的次数4除子 $T_3(P)$，并计算 R252 同一实际主函数
$\Phi_C$ 在该除子上的范数。这里 $C=P-b$，完整457函数和
正式终点已由各盘输入封存包保存；没有重新执行群链。

全部值模 $47^4=4879681$：

| 盘 | 三核分解型 | $\operatorname{Norm}_{T_3(P)}\Phi_C$ | $\log_{47}\operatorname{Norm}_{T_3(P)}\Phi_C$ |
|---|---|---:|---:|
| ORD_j12 | $1+1+2$ | 300875 | 488095 |
| ORD_j15 | $1+1+2$ | 4396806 | 2947323 |
| ORD_j19 | $1+1+2$ | 2151974 | 2506275 |
| ORD_j27 | $1+1+2$ | 2388997 | 154865 |
| ORD_j32 | $4$ | 4168707 | 3154875 |

这些是指定实际 $\Phi_C$ 的范数，不是完整规范截面高度。
还须加入真正固定支撑范数、第二变量 tiny 和 R292 的刚性化
系数，才能组装 $F_3$ 的局部高度。本文不宣称共同根已排除。

## 1. 实际三核和原始41结构

源点均使用 R231 保存的真正有理中心、完整41挠点半域和
准确项链，而非只用 $j$ 值确定一个模型。三核环为
$$
E=R_2[r]/f(r),\qquad
f(r)=r^4+2Ar^2+4Br-A^2/3.
$$
此多项式是 $\psi_3/3$，在47处 étale。
四个源 $j=12,15,19,27$ 的实际 Frobenius 迹分别为
$-6,-6,6,-6$，三核分解为 $1+1+2$；
$j=32$ 的迹为10，三核不可约四次。执行器另直接分解多项式，
没有把迹的推论代替实际根计算。

对每根 $r$，取
$$
t=2(3r^2+A),\qquad v=4(r^3+Ar+B).
$$
Vélu 映射和目标为
$$
x'=x+\frac{t}{x-r}+\frac{v}{(x-r)^2},\qquad
y'=y\left(1-\frac{t}{(x-r)^2}-\frac{2v}{(x-r)^3}\right),
$$
$$A'=-9A-30r^2,\qquad B'=-27B-42Ar-70r^3.$$
对四支分别验证真实椭圆曲线方程、41倍为零、原始 Weil 配对
$\zeta^3$ 和目标判别式单位。

R286 的行列式规范完整保留：保存的基是原始
$\phi(P),\phi(Q)$，其行列式为3。对基上的评价向量使用
$\operatorname{diag}(1,3^{-1})g_N$，其中 $g_N$ 对应
$\operatorname{diag}(1,3)$ 运输后的项链。这个评价向量矩阵的
行列式为 $3^{-1}\bmod41$。因此模形式乘积仍乘原始 $\zeta$，
不能把评价归一化误写成乘 $\zeta^3$。

四个分裂到 $R_2$ 的盘直接运行已冻结 R286 支撑执行器。
每个目标的1680个实际 Eisenstein 值、完整73行及相对迹见证
均重新从该盘真实挠点计算。

## 2. 四次核与原迹域相交时的准确处理

ORD_j32 的原41挠点半域 $K$ 的次数为120，因此它已经包含
四次核域。该核域也与次数40的 cyclotomic 迹域相交。
若对某一个几何目标直接作20项绝对 Frobenius 迹，Frobenius
会同时改变核 $r$，从而得到错误的目标组合。

本结果先在完整 étale 代数中计算，再对系数取迹。具体地，
设 $r_0,\ldots,r_3$ 是 $K$ 中四个提升根。对每个73维原始
基行，四支先得到未取相对迹的乘积 $U_0,\ldots,U_3\in K$。
利用单位差 $r_b-r_c$ 构造
$$
L_b(r)=\frac{\prod_{c\ne b}(r-r_c)}{\prod_{c\ne b}(r_b-r_c)},
\qquad U(r)=\sum_{b=0}^3U_bL_b(r)=\sum_{k=0}^3u_kr^k.
$$
所有四个代入等式都实际核验；这是
$K[r]/f\simeq K^4$ 的逆同构，没有拟合自由度。
它恢复在形式变量 $r$ 中的同一个代数表达式。

随后保持形式 $r$ 不动，只对 $u_k$ 作原来的20项迹：
$$
W(r)=\sum_{k=0}^3\operatorname{Tr}_{K_{40}/R_2}(u_k)r^k.
$$
实际292个 $u_k$ 全部满足 $\varphi^{40}(u_k)=u_k$。
设 $d=[K:\mathbf Q_{47}]=120$，两实坐标通过
$$
\left(\frac{20}{d}\operatorname{Tr}_{K/\mathbf Q_{47}}u_k,\
-\frac{20}{d}\operatorname{Tr}_{K/\mathbf Q_{47}}(iu_k)\right)
$$
提取。第一原始基行的四个系数还各自保存并验证完整20项
$\sum_{a=0}^{19}\varphi^{2a}(u_k)$ 见证。
这正是 $\operatorname{id}_E\otimes\operatorname{Tr}$；
核域相交不会使它变成对单个几何分支的绝对迹。

输出保留全部四支原始41点、73个未取迹乘积、Lagrange 系数、
全部292个形式系数以及最终四次坐标。旧 R286 文件未改。
该四次实际支撑运行约13.8秒，随后全部验证通过。

## 3. 模型和 Hecke 尺度的独立约束

五盘均在整个四次环中验证73坐标的全部2701个二次乘法关系。
四次坐标系数满足同一模型的半线性下降。
若 $W(r)=W_0+W_1r+W_2r^2+W_3r^3$，Newton 和给
$$
\operatorname{Tr}_{E/R_2}W=4W_0-4AW_2-12BW_3.
$$
按归一化 Vélu 拉回，实际对应的完整权二迹为上式的 $1/3$。
每盘分别验证
$$
\frac13\operatorname{Tr}_{E/R_2}W
=W(P)\,T_3^{(73)}
$$
的全部73个坐标，并通过同一典范核独立核全部54个全纯坐标。
这些矩阵只用作实际四目标计算后的验证，未被用于生成目标。

## 4. 同一真实主函数及相交因子的处理

使用 R252 的准确表达式
$$
\Phi_C=f_{\rm final}^{-1}\frac{v_1}{f_c}\frac{F_P}{G_Q},
\qquad\operatorname{div}\Phi_C=mC-A_1(t).
$$
所有455个链函数（454次群运算和最初负点）、两个终点函数
以及 $f_b,f_c,v_1$ 都由既存函数档案和完整系数读入。
最初 $f_b$ 的指数为 $-m$，最后 $f_c$ 的总整数指数准确为0；
中间运算仍保留它以及终点 $v_1/f_c$，没有提前略去尺度。

对四个 $R_2$ 分裂盘，复用 R265 的真实 Weierstrass 执行器，
在实际目标上生成0至27阶 $W,V_2,V_3$。每个目标验证全部455
有效除子关系，并使用初始、负点、最终和 $A_1$ 的全73列理想。
因此非单位截面先作准确 distinguished 因子消去，再取单位。
最后 distinguished 因子都为1，前向 DAG 单位值与完整整数
指数表达式逐目标一致。

四目标合计每盘1840个截面准备的剩余次数统计：

| 盘 | $e=0$ | $e=1$ | $e=2$ | $e=3$ |
|---|---:|---:|---:|---:|
| j12 | 1805 | 22 | 13 | 0 |
| j15 | 1801 | 23 | 15 | 1 |
| j19 | 1810 | 20 | 10 | 0 |
| j27 | 1812 | 17 | 11 | 0 |

最高次数3满足 R159/R265 的 $4e+3<28$，所以27阶 jet
足以保证模 $47^4$ 的单位值。四个约0.534MB的 jet 缓存一并封存。

对 j32，所有455个真实函数截面及5个固定因子在四次环中的
范数均为47进单位，故可直接在真正四次代数中求逆。
未假定一般截面都单位：每个值的范数均实际断言为单位。
最终
$$
\Phi_C=
2819583+4875153r+2846653r^2+500187r^3\pmod{47^4}.
$$
其四次乘法矩阵行列式为4168707。完整整数权重因子范数之积
独立给同值，47进对数为3154875。

## 5. 独立重核和数据边界

标准库核验器已实际运行：

- 对四个分裂盘重算全部7360个保存单位对数、16个完整整数
  指数 $\Phi_C$ 乘积，以及四支范数乘积与其对数；
- 对 j32 从原函数文件的325维系数重新评价455个实际分子，
  从原数据重新评价全部5个固定因子；逐一核四次值及单位范数；
- 在四次代数中重新累乘完整整数表达式得到上式 $\Phi_C$，
  用单位主元消元求乘法矩阵行列式，独立于主执行器的24项
  排列公式，再核范数和对数；
- 核真实支撑、主函数、范数、函数档案和缓存的相关 SHA256。

标准库核验不重跑原群链，不宣称重新执行了27阶 Weierstrass
引擎或原始挠点求值。其边界和主执行器实际断言分别保留。

统一下游键为
actual_log_norm_Phi_T3_P_mod47four。相应文件名是
ORD_jNN_actual_T3_principal_norm47.json.gz；
真正目标文件名为 ORD_jNN_actual_T3_support47.json.gz。
合并清单为 p41_five_ordinary_candidate_T3_norms47.json.gz。

| 盘 | 实际支撑 SHA256 |
|---|---|
| j12 | 8733edbf7d6f4cdd02c39041c50becc1bef8c020bf7ab0641229549c3b4f6520 |
| j15 | 22e9c989163e7b2febb0bfd03b703ae185f292401a0e0e68915a61c554b689a1 |
| j19 | 905f92e1909210e86e98f2660b3cd31bcccb6dc22cf259d48a1c87a2087fe1df |
| j27 | b3f85259767c43c8a370bd037da4f7c6c3272bd8e0ca9b6de24bcaf5ed18480b |
| j32 | 0fbd1094cae5aadfd087db5cd6f90b46b0db632f7395668ad2cf3b4dbc5917e0 |

| 盘 | 实际范数 SHA256 |
|---|---|
| j12 | b106e594922759d6b9d8a98902ad3bfd36f059332a748fd2eb68ff78e9b0e3f9 |
| j15 | b27666fced652a504e46d916944ac029c4c9d53b0ec5d007815562e390529edf |
| j19 | d87189dccec53d06c607a945bc0cf08459cd86f39f7f1c672580118cd99e8aa5 |
| j27 | 36c46cb24ecfa0b3351dbf1bc87ae2e7addcedf742a48d268d4b42f56ca41d03 |
| j32 | 43f8e32cc993b56709d8f234190baad5af9e71072522d94f8f475df93a871555 |

新增四次支撑源码 SHA 为
20f29d3420ac7040b14dd205578358464a0034f390f8d2f922d46200e0228e3c；
四次范数源码 SHA 为
971fba039608c889e4957bb770bddc53609fe5c7e0d2cf08c917fa42695d2de9。
独立核验 JSON 的 SHA 为
d15e7278e2dc5bc0f4104d8bce683def70b8f838aad115ececce8ef251e3e97a。
所有文件及已发布依赖由 R295 封存清单逐项绑定。

## 6. 重建入口

先将各盘既存457函数 tar 包按原相对路径解包；它们仍是此前
F2输入封存的同一字节文件。四个分裂盘用 R286 的两个冻结
执行器，或运行 p41_ordinary_T3_candidate_batch47.py，
指定盘12、15、19、27、原输入根目录、原41提升和脚本目录。
新增执行器的命令行为：

~~~sh
OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/p41_ordinary_t3_quartic_support47.py \
  --script-dir scripts \
  --ordinary-lifts scripts/data/p41_ordinary_point_lifts47.json.gz \
  --j 32 --output /work/ORD_j32_actual_T3_support47.json.gz

OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/p41_ordinary_t3_quartic_norm47.py \
  --script-dir scripts \
  --support /work/ORD_j32_actual_T3_support47.json.gz \
  --principal-expression scripts/data/ORD_j32_actual_principal_function47.json.gz \
  --transport-directory /work/ordinary-principal-transports/ORD_j32 \
  --output /work/ORD_j32_actual_T3_principal_norm47.json.gz
~~~

独立核验器 verify_ordinary_candidate_T3_norms47.py 接同一输入
根目录的五盘既存函数、支撑、范数及缓存，输出核验 JSON。
本文的完整范数已经可接真正 $F_3$ 中心和局部函数；是否排除
各盘候选仍取决于同一坏分量标签上的后续实际 QC 计算。
