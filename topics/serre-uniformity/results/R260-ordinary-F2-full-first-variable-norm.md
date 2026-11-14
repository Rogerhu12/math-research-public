# R260：ORD_j05 的完整 F2 第一变量范数，含 106 点典范支撑及两处碰撞首项

## 1. 结论与精确范围

设 $q=47^4=4879681$，$P$ 为 R231 的真实有理普通中心 ORD_j05，
$b=P_{-3}$，$u=P_{-12}$，$c=P_{-7}$，$C=P-b$。沿用 R248、R252 的
实际整数 $m$、54 点第一 Abel 族 $A_1(t)$ 和完整主函数

$$
\operatorname{div}\Phi_C=mC-A_1(t).
$$

这里的 $m$ 是 R248 真正群链的 304 位整数，$m\bmod q=459340$、
$m\bmod47=9$；没有用其模 $q$ 值代替整数除子关系。

R148/R151 的 $K_{g_1}$ 规范给出实际第二变量除子

$$
D_P=27T_2P+81u-27Z_{-8}-54c+4P+4b+4K_{g_1}.
\tag{260.1}
$$

其度数为

$$
27\cdot3+81-27\cdot20-54+4+4+4\cdot106=0.
$$

在 $P,b$ 两点统一以 $j-j(Q)$ 为实际粗曲线局部参数，采用首项
单位定义碰撞处的函数取值，则本次实算得到

$$
\boxed{\log_{47}\Phi_C[D_P]=3780398\pmod q.}
\tag{260.2}
$$

这是完整第一变量主函数运输项。尚需 R259 的规范截面坐标、
第二变量运输和形式双变量值才能成为实际 $\sigma_{F_2,b}$ 高度；
本条不把 (260.2) 称为局部高度、QC 共同根或 Serre 一致性结论。

### 全部真实支撑的数值

| 支撑 | 未加权的实际对数，模 $q$ | 在 $D_P$ 中的系数 |
|---|---:|---:|
| 完整三次目标 $T_2P$ | 2233158 | 27 |
| $u=P_{-12}$ | 1385701 | 81 |
| 全部 20 点 $Z_{-8}$ | 3918437 | -27 |
| $c=P_{-7}$ | 2253838 | -54 |
| $P$，以 $j-j(P)$ 取首项 | 4596271 | 4 |
| $b$，以 $j$ 取首项 | 838480 | 4 |
| 完整 106 点 $K_{g_1}$ | 1932828 | 4 |

上述七项按表中系数相加即为 (260.2)。所有有理范数的虚部均由
实际复数系数相加得到零，没有在输出时删除虚部。三次目标项直接
绑定 R254 的真实 determinant-two 水平结构及全三次代数范数，
这里不再重算椭圆曲线的 41 阶挠点。

## 2. 原 R160 典范商代数的恢复

R160 的完整候选 1 商代数曾只保留 compact 证书。本次通过原
p41_canonical_restriction47.py，在 R241 已证明等价的精确消元和
R222 整数安全矩阵乘法下重建。

重建的三个取值矩阵为

$$
\Phi_1\in R^{106\times73},\qquad
\Phi_2\in R^{106\times199},\qquad
\Phi_3\in R^{106\times325},
\quad R=(\mathbf Z/q\mathbf Z)[i].
$$

它们分别是 $W/f_0$、$V_2/f_0^2$、$V_3/f_0^3$ 在
$K_{g_1}$ 上的取值。恢复后逐项核对原证书中的三个矩阵 SHA、
106 次最小多项式、典范系数、分母系数、原始元、Krylov 单位行列式
和比较三次截面的范数。压缩 raw 文件本身也精确恢复为原记录字节：

$$
\text{SHA256}=
\texttt{96ebb1c92fe45b098d73daca0da424073ef9a8302fc41b4faf3ce36be880dc41}.
$$

这不是重新选择典范微分。54 维 $g_1$ 系数先经原模型的典范包含矩阵
嵌入 73 维；执行器再验证

$$
\Phi_1g_1=0,\qquad \Phi_1f_0=1.
$$

原 106 次多项式精确分成已保存的四次低因子与 102 次高因子。
低因子的四个实际根仍采用原标签 canonical1_root_3、23、43、44；
这些数字是原始元模 47 的根，不能当作 $j$ 标签。高因子模 47
的不可约因子次数是 $6,8,22,31,35$，全部重数为 1。

## 3. 102 次高因子的完整范数

对 R252 的全部 455 条实际主截面，以及 $f_b,f_0,v_1,F_P,G_Q$
五个固定截面，用上述 $\Phi_d$ 求值，再模高因子 $H_{102}$。
所有实际有理截面都下降为实系数多项式。逐项核验

$$
\gcd(\overline F,\overline H_{102})=1.
$$

故全部 460 项在这个完整 102 次有限平展代数中都是单位。本次
没有跳过任何闭点，也没有只取一个不可约因子或一个代表值。

对每个已求值多项式 $a(X)$，先在整数多项式环精确计算

$$
N(a)=\operatorname{Res}_X(H_{102}(X),a(X))\bmod q.
$$

因为 $H_{102}$ 首一，这就是乘法算子的行列式；整数 resultant
还避免了在合成模数下使用可能非单位的 Euclidean 主系数。
输出保存了全部 460 个多项式及其实际范数。

用原群链正向递推这些范数，并独立用 R252 的整数反向权重相乘，
两种结果精确相同：

$$
\operatorname{Norm}_{K_{\rm high}}\Phi_C=807519,\qquad
\log_{47}\operatorname{Norm}_{K_{\rm high}}\Phi_C=497260.
\tag{260.3}
$$

低因子四点的完整圆盘计算给对数和 1435568。因而

$$
\log_{47}\operatorname{Norm}_{K_{g_1}}\Phi_C
=1435568+497260=1932828\pmod q.
$$

## 4. 28 个低次与碰撞点上的真实圆盘计算

本次同批处理：

- 原 p41_cm_quadratic_jets47_raw.json.gz 中的 $b,u,c$ 三个实际 CM 点；
- Z_minus8_16、34、54、76、122、175、209、239、247、290、
  365、440、480、525、610、647、679、689、735、762 共 20 点；
- 上述四个低次典范点；
- R231 的实际 ORD_j05 中心 $P$。

所有常数输入都是原 73 维模型中的实际点坐标。R222 的全局
射影导子在单位标架 $v$ 下构造

$$
Wv=1,\qquad Wc=W(0)c+z,
$$

并递推 $W,V_2,V_3$ 到 $z^{27}$。每批最多 16 点；两个完整 jet
文件都保留，可直接复用而不重跑群链。

全部 $28\cdot454=12712$ 个三次截面圆盘取值，其模 47 首个非零阶
的分布为

| 残余阶 $e$ | 截面与点的实际配对数 |
|---:|---:|
| 0 | 12457 |
| 1 | 192 |
| 2 | 58 |
| 3 | 3 |
| 4 | 2 |

对每个非单位截面做 $F=W_FU_F$ 的 Weierstrass 预备，保留首一
distinguished 多项式 $W_F$ 和单位对数，不只保留 $F(0)$。
最大 $e=4$，本实现恢复四位单位常数需要至多 $4e+3=19$ 阶，
故 27 阶已满足所实际出现的精度需求。

另对 initial、negative、final、family1 四个真实有效除子，
逐点从完整 73 列理想中选最小残余阶的单位见证列，再核
其余全部 72 列被同一个 distinguished 因子整除。这给出四个
完整理想的局部有效除子，不是只看随机一列。

## 5. 整数除子递推与所有零点因子的抵消

令 $L=\operatorname{div}(f_0)$，原群链节点的实际有效除子记为 $E_T$。
R252 保留了精确关系

$$
D_T=E_T-L=k_TC+\operatorname{div}(f_T).
$$

initial 节点用 $f_T=f_b/f_0$。每个 AddFlip 的实际截面 $F$
满足有效除子和关系；在有两个输入时 $d=3$，在初始负点时 $d=2$。
于是

$$
f_{\rm out}=\frac{F/f_0^d}{\prod f_{\rm in}},\qquad
k_{\rm out}=-\sum k_{\rm in}.
\tag{260.4}
$$

本次在每一个点都依此核验

$$
W_F=\prod W_{E_{\rm in}}\;W_{E_{\rm out}},
\tag{260.5}
$$

所有商都用实际首一多项式做精确除法，余式必须为零。初始节点
的 distinguished 多项式另独立核为

$$
W_{E_{\rm initial}}=
\begin{cases}
zW_{f_b},&Q=P,\\
W_{f_b}/z,&Q=b,\\
W_{f_b},&\text{其余 26 点}.
\end{cases}
\tag{260.6}
$$

其中 $b$ 处的除法也是实际多项式整除，并非仅根据抽象阶数推定。
初始负节点和最终节点分别与上述完整理想提取的因子逐项相同。

R248 的实际终点函数为

$$
h_Y=\frac{v_1}{f_0}\frac{F_P}{G_Q},\qquad
\operatorname{div}(h_Y)=D_{\rm final}-A_1(t).
$$

执行器核验 family1 理想的 distinguished 因子等于 $W_{v_1}$；
这同时确认实际 $A_1(t)$ 在这些圆盘中没有剩余移动支撑。再核验

$$
W_{v_1}W_{F_P}=W_{E_{\rm final}}W_{G_Q}.
\tag{260.7}
$$

因此全部 455 步及终点的 distinguished 因子精确抵消后，完整
函数 $\Phi_C=f_{\rm final}^{-1}h_Y$ 恰只剩

$$
W_{\Phi_C}=
\begin{cases}
z^m,&Q=P,\\
z^{-m},&Q=b,\\
1,&\text{其余 26 点}.
\end{cases}
\tag{260.8}
$$

$m$ 是原整数；程序只把巨大幂保持为整数指数，不展开成巨大多项式。
单位对数沿 (260.4) 正向递推，另用 R252 所有整数反向权重从
455 个主截面直接重组。每个点的两个结果均精确相同。
因此没有遗漏中间碰撞，也没有将“最终阶数为零”误当成可以
直接分别计算非单位函数值。

## 6. 两个碰撞点的同一 $j$ 参数

设射影图的参数 $z=\alpha_Q(j-j(Q))+\cdots$。若
$\Phi_C=z^rU(z)$，则实际 $j$ 首项为

$$
\operatorname{lc}_j(\Phi_C)=\alpha_Q^rU(0).
\tag{260.9}
$$

### ORD_j05

真实源模型为 $A=2,B=17$，$\Delta=4A^3+27B^2$。由 R218 的
Kodaira–Spencer 系数和真正的 $j$ 导数，

$$
\frac{\beta}{dj}=\frac{\Delta}{124416A^2B},\qquad
\alpha_P=\frac{\Delta}{124416A^2B}\,(W_{\rm raw}v)\,H_v(c).
$$

使用原 R231 物理尺度的 $W_{\rm raw}$，得到

$$
\alpha_P=4272830,\quad \log_{47}\alpha_P=44885,\qquad
\log_{47}U_P(0)=3772596.
$$

故 $j$ 首项对数为 $4596271$。

### 真正 CM3 基点

基点处使用 R208 已验证的粗参数 $u=A^3/B^2$，而不是堆叠方向。
有

$$
j=\frac{6912u}{4u+27},\qquad
\left.\frac{dj}{du}\right|_b=256.
$$

从 R208 实际 coarse jet 对选定射影参数求导，得到

$$
\alpha_b=4175570,\quad \log_{47}\alpha_b=4400469,\qquad
\log_{47}U_b(0)=2008310.
$$

这里 $\operatorname{ord}_b\Phi_C=-m$，故 $j$ 首项对数为 $838480$。
两个首项在第二除子中均取权重 4，合计切向修正为

$$
4m(\log\alpha_P-\log\alpha_b)=3495061\pmod q.
\tag{260.10}
$$

所有 28 点按各自第二除子权重相加的图中单位对数为 1436884，
加 (260.10) 后为 52264。再加高因子 $4\cdot497260$ 和 R254
三次目标 $27\cdot2233158$ 即为 (260.2)。两处交叉阶数加权和为
$4m-4m=0$，相应 tame-symbol 符号为 1。

供 R259 使用的实际典范微分尺度也已直接求出：

| 点 | $g_1/dj$ | $\log_{47}(g_1/dj)$ |
|---|---:|---:|
| $P$ | 621937 | 2978578 |
| $b$ | 3413944 | 2129288 |

它们都在模 47 下为单位。$P$ 处从物理 $W_{\rm raw}g_1$ 乘上述
$\beta/dj$；$b$ 处从原 CM3 的真实典范微分 $du$ 系数除以 256。
这两项只作为截面规范的明确输入；R260 本身不以此替代 R259 的
规范截面证明。

## 7. 可复现文件和命令

完整清单、字节数和 SHA 在 R260-handoff-manifest.json。
主执行器为 p41_ordinary_f2_fixed_norm47.py，最终证书为
ORD_j05_actual_F2_first_variable_norm47.json.gz。

原商代数的恢复执行器 p41_restore_canonical_candidate147.py 及
逐项/字节一致验证记录一并保留。正式主运算直接读取恢复后的
raw，不必重新执行 R160 消元，更不重跑 R248 的 454 次 AddFlip。

以下命令在当前工作区根执行；python-flint 已安装于 math-deps：

~~~bash
OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
PYTHONPATH=/workspace/scratch/76d0eb5f3db8/math-deps \
python agent-qc/p41_ordinary_f2_fixed_norm47.py \
  --script-dir math-research/topics/serre-uniformity/scripts \
  --based-points agent-qc/p41_all19_based_points47.json.gz \
  --second-kind-certificate agent-qc/ordinary-second-kind/ORD_j05_second_kind_complete47.json.gz \
  --multiplication agent-qc/ordinary-abel-with-transports/ORD_j05_multiply47.json.gz \
  --transport-directory agent-qc/ordinary-principal-transports/ORD_j05 \
  --principal-expression agent-qc/ORD_j05_actual_principal_function47.json.gz \
  --canonical-algebra agent-qc/p41_canonical_restriction47_candidate1_raw.json.gz \
  --ordinary-lifts root-recovery/p41_ordinary_point_lifts47.json.gz \
  --t2-norm agent-qc/ORD_j05_actual_T2_principal_norm47.json.gz \
  --cache-dir agent-qc/ordinary-norm-cache \
  --output agent-qc/ORD_j05_actual_F2_first_variable_norm47.json.gz
~~~

执行器绑定所有实际输入及四个复用执行模块的 SHA；最终数据明确
标记第一变量范数已完成、完整局部高度和共同根尚未完成。R248 的
完整主函数归档可恢复上述 transport 目录，运行时逐文件核其 SHA。

