# R259：ORD_j05 中心的真实规范 F2 截面高度

## 1. 结论与精确范围

沿用 R102–R260 的同一实际模曲线、双 Abel 族、Hecke 相容对称 Poincaré 对数及典范规范。置
$$
X=X_{\mathrm{ns}}^+(41),\quad g=54,\quad q=47^4=4879681,\quad
b=P_{-3},\quad C=P-b.
$$
这里 $P$ 是 R231 的真正有理普通中心 ORD_j05，物理椭圆模型为
$y^2=x^3+2x+17$，实际 $j$ 值模 $q$ 为 1559512。对于 $F_2=27T_2+4$ 和 R148 的全局规范截面，本次完成
$$
\boxed{\lambda_{47}(\sigma_{F_2,b}(P))=4213785\pmod{47^4}.}
\tag{259.1}
$$

该值同时包含实际范数纤维的连接值和规范截面坐标，没有将非形式代数框架的高度设为零，也没有用全局二次型替代局部截面高度。本条只完成一个真正普通中心；整盘展开、其他中心及全部 53 个 QC 方向的共同根仍由后续计算处理。

最终数据 ORD_j05_actual_canonical_F2_height47.json.gz 的 SHA256 为
~~~
afd046cbad7657edf0dc13950b5bdad3031ad59872174a492d1228ae1dd4eded
~~~
冻结生成器 p41_ordinary_F2_connection47.py 的 SHA256 为
~~~
4ef5e267a5d730e9bb0c102eba708ff8dca5221a8b339258cf89464170fa9917
~~~

## 2. 同一个实际第二除子

记 $u=P_{-12}$、$c=P_{-7}$、$D$ 为全部 20 个尖点，$B=Z_{-4}-D$。
R148/R151 的 $K_{g_1}$ 规范给实际度零除子
$$
D_P=27T_2P+81u-27Z_{-8}-54c+4P+4b+4K_{g_1}.
\tag{259.2}
$$
利用真实除子等式 $T_2b=3u$，可写成
$$
D_P=27T_2C+4C+162(u-b)-27(Z_{-8}-20b)
       -54(c-b)+4(K_{g_1}-106b).
\tag{259.3}
$$

设 $\eta_E$ 是原 R140/R141 对称 Hecke 相容连接对实际度零除子 $E$ 的第三类微分。它的留数为 $E$，对除子可加，并满足
$\eta_{\operatorname{div}f}=d\log f$。本次先真实构造
$$
\eta_C,\ \eta_{u-b},\ \eta_{c-b},\ \eta_{Z_{-8}-20b},\
\eta_{D-20b},
$$
再用真正二同源对应求 $\eta_{T_2C}=T_2\eta_C$。典范项由第 6 节的实际 $j$ 关系得到。全部微分均按原 R141 第二 Abel 族校准，没有另加任意全纯微分。

## 3. 从 SS 图恢复固定除子的实际校准值

R240 的实际第二类微分行 $\nu$ 满足
$$
\nu_j=\left.\frac{\partial}{\partial t_j}
               \eta_{A_2(t)}\right|_{t=0}.
$$
因此对实际度零除子 $E$，$g_E=\int_E\nu$ 正是 $\eta_E$ 在原 54 个第二族点的物理参数系数。

R246 的移极点函数和有理基满足
$$
\nu=(\mu-dF^{\mathrm{rat}})\,C^{-1}.
\tag{259.4}
$$
R247 保存的是全部 3154 个旧 SS 图中心上
$U_Q=20Q-D$ 的 $\mu$ 积分实部。本次并未假称已保存每个非有理顶点的完整复数积分，而是只对真正 Frobenius 稳定的实际除子求和。

对 $b,u,c$ 及全部 20 个 $Z_{-8}$ 点，执行器使用 R160 的完整 73 维真点坐标，以实际单位标架 $w$ 归一化；按模 47 完整射影坐标在图中唯一定位后，计算 $z\in47R_2$ 的真实位移。把保存的三阶射影级数复合，全部 73 个坐标逐项吻合，再以同一图中的 $\mu$ 原函数补上 tiny 积分。共 23 个实际点的顶点编号、参数位移及完整坐标检验均保留。

每个评价除子在完整模 $47^4$ 坐标上都核对为 Frobenius 稳定，因此其有理基积分之和必为实数。将顶点积分实部及 tiny 积分实部相加，正好给完整的和，没有丢弃未控制的虚部。

若 $S$ 的次数为 $d$，则
$$
g^\mu_{S-db}
=\frac{\sum_{Q\in S}U_Q^\mu-dU_b^\mu}{20},
$$
而 (259.4) 给
$$
g^\nu_{S-db}
=\left(g^\mu_{S-db}-F^{\mathrm{rat}}(S)
                    +dF^{\mathrm{rat}}(b)\right)C^{-1}.
\tag{259.5}
$$
尖点函数和也在原完整尖点代数中保留：
$$
U_b^\nu=
\left(U_b^\mu-20F^{\mathrm{rat}}(b)+F^{\mathrm{rat}}(D)\right)C^{-1},
\qquad
g_{D-20b}=-U_b^\nu.
\tag{259.6}
$$
所使用的 $v,w$ 在这些真点处均为单位。普通点 $C$ 的梯度直接取 R248 已完成的 54 个真实第二类大积分，再降到模 $47^3$。全部五个梯度均核验原 $\nu$ 基的 Frobenius 共轭置换。

## 4. 五个完整有限极 Riemann–Roch 空间

仍令 $\mathcal L=K_X+D$，$\deg\mathcal L=126$，$V_1=H^0(\mathcal L)$、$V_2=H^0(2\mathcal L)$ 的维数分别为 73、199。设有限极点支撑 $Z$ 含 $n$ 个不同几何点。选实际有理截面 $q_Z\in V_1$，使
$$
\operatorname{div}(q_Z)=Z+R_q,\qquad \deg R_q=126-n.
$$
所有有限点显式采用真正的 $f_0=1$ 标架。程序在全部 $Z$ 上核 $q_Z=0$ 及 $H_{f_0}(q_Z)$ 为单位，故这些指定零点都是简单零点。两个 Abel 族及所用完整尖点取值处的分母也核为单位。

候选微分以权二商表示为
$$
\eta=s/q_Z,\qquad s\in H^0(2\mathcal L-R_q).
\tag{259.7}
$$
在物理参数 $t$ 下还须乘真正的 $\beta(t)dt$。有限留数准确为
$$
\operatorname{res}_Q\eta=
s(Q)/H_{f_0}(q_Z)(Q).
\tag{259.8}
$$

### 4.1 候选空间是完整整格

取 $g\in H^0(\mathcal L-Z)$，施加 $(g/q_Z)s\in V_2$ 的 colon 条件。在分母为单位的 817–820 个实际评价点上插值并核验全部方程；清分母后的式子属于 $H^0(3\mathcal L)$，次数 378 小于这些点数，因此是忠实的全局恒等式。

全部 $H^0(2\mathcal L-R_q)$ 截面都满足上述条件，而
$$
\deg(2\mathcal L-R_q)=126+n>2g-2,\qquad
h^0(2\mathcal L-R_q)=73+n.
$$
实际 colon 秩为 $126-n$，所以核维数恰为 $73+n$；由包含和同维性，求得完整空间。单位子式保证这个结论在整截断环上成立，而非仅特征零维数计算。

| 微分 | $n$ | 有限留数 | 每个尖点留数 | colon 秩 | 候选维数 | 忠实行数 |
|---|---:|---|---:|---:|---:|---:|
| $\eta_C$ | 2 | $1,-1$ | 0 | 124 | 75 | 820 |
| $\eta_{u-b}$ | 2 | $1,-1$ | 0 | 124 | 75 | 819 |
| $\eta_{c-b}$ | 2 | $1,-1$ | 0 | 124 | 75 | 817 |
| $\eta_{Z_{-8}-20b}$ | 21 | 二十个 $1$、一个 $-20$ | 0 | 105 | 94 | 820 |
| $\eta_{D-20b}$ | 1 | $-20$ | 1 | 125 | 74 | 820 |

### 4.2 全留数与 54 个实际校准条件

R110 的真正 Tate 参数为 $q_{41}$，宽度为 41，故尖点留数是 $41s/q_Z$。程序使用两个完整 $R_{80}$ 取值，它们代表 Frobenius 平方的两个 10 点轨道，合起来覆盖全部 20 个尖点；不是只核两个几何点。

有限与尖点留数之间只有总和为零这一条关系。指定留数后剩余维数
$$
(73+n)-(n+20-1)=54
$$
恰为全纯微分空间。然后在原第二族的所有 54 点施加
$$
\beta_0s(Z_{2,j})/q_Z(Z_{2,j})=g_{E,j},
\qquad \beta_0=-3/27652.
\tag{259.9}
$$
R141 的典范取值矩阵 $\Omega_2$ 有单位行列式，因此这些条件唯一消除全纯自由度。程序核验全部留数方程、完整尖点域方程、全部 54 个校准方程以及 Frobenius 下降；总约束实际秩为 $73+n$。

## 5. 第六个连接是真正的 T2 trace

本次没有用 54 维 Lie 矩阵替代 $\eta_{T_2C}$。从 R131 的三个实际二同源目标逐支求值，使用原项链运输和规范 Vélu 微分的 $1/2$：
$$
T_2\eta_C
=\beta_{\rm source}
\left(\frac12\sum_{\text{三支}}
       s_C(W_{\rm target})/q_C(W_{\rm target})\right)dt.
\tag{259.10}
$$
三支共同有定义的源点数为 819，两个 Abel 族全部在其中。

R254 的完整三次代数给出 $T_2P$，另有 $T_2b=3u$，所以 trace 的极点仅可能是三个 $T_2P$ 点与 $u$，留数分别为三个 $1$ 及 $-3$。选实际 $q_T\in V_1$ 在完整四次支撑上消失：用三次代数的全部三个系数和 $u$ 的真坐标施加四个独立条件。

乘以 $q_T$ 后，(259.10) 的全部第三类极点被消去，权和正确，所得实际截面属于 $V_2$。用 199 个单位插值行求 $s_T$，再核全部 819 行。819 大于 $\deg(2\mathcal L)=252$，因此忠实确定全局截面。完整尖点域上的分子再次核为零，系数满足 Frobenius 下降。

由原 R140 的实际 Hecke 相容性，$\eta_{T_2C}=s_T/q_T$ 就是同一个连接的 $T_2C$ 项，不存在另一个未求的全纯修正。

## 6. 实际粗曲线的典范 j 关系

R102/R208 给 $j:X\to\mathbf P^1$ 的次数 820，全部尖点宽度 41；保留三阶椭圆点为 $b$ 一个，保留二阶椭圆点为 $Z_{-4}$ 的 20 点。$j=0$ 的其他点分歧指数 3，$j=1728$ 的其他点分歧指数 2，20 个尖点的分歧指数 41。

Riemann–Hurwitz 因而给
$$
K_{dj}=-82D+\frac23(\operatorname{div}_0(j)-b)
+\frac12(\operatorname{div}_0(j-1728)-Z_{-4})+40D.
$$
将两个零除子各换成主除子加 $41D$，得到
$$
\boxed{6K_{dj}=4\operatorname{div}(j)+3\operatorname{div}(j-1728)
               +35D-4b-3Z_{-4}.}
\tag{259.11}
$$
度数为 $(35\cdot20-4-3\cdot20)/6=106=2g-2$。这里使用真正粗曲线参数，没有把椭圆堆叠方向当作普通方向。

由 $K_{g_1}=K_{dj}+\operatorname{div}(g_1/dj)$，准确得到
$$
\boxed{\begin{aligned}
\eta_{K_{g_1}-106b}
={}&d\log(g_1/dj)+\frac23d\log j+\frac12d\log(j-1728)\\
&+\frac{16}{3}\eta_{D-20b}-\frac12\eta_B .
\end{aligned}}
\tag{259.12}
$$
因此 $g_1$ 的实际主函数尺度保留在连接中。$\eta_B$ 使用 R194/R197 的原实际连接，本次在原第一族上重现其 tiny 积分 2918700。

## 7. 同一实际第一 Abel 族上的积分

R248/R252 已给全部 54 个真正物理参数 $t_j\in47R_2$，并以完整 73 列理想证明
$$
\operatorname{div}\Phi_C=mC-A_1(t).
\tag{259.13}
$$
本次不另换 Abel 族或解析框架。源模型仍为
$$
y^2=x^3+x+32+t,\qquad \beta(t)=-3/(4+27(32+t)^2).
$$
对六个已构造分式用真实 $W,V_2$ jets 求
$\beta(t)s(W(t))/q(W(t))$ 的 0、1、2 阶项；$\eta_B$ 用其原三次/二次分式。典范项保留
$$
g_1/dj=(\beta/j')Wg_1,\qquad
d\log(\beta/j')=d'/d-d''/d',
\quad d=4+27(32+t)^2.
$$
全部分母常数及 $g_1$ 在这些实际第一族圆盘中均为单位。

连接系数模 $47^3$ 足够：积分至少乘一个 $t_j\in47R_2$，误差因而进入 $47^4$。正规系数为整幂级数，省略第 $n$ 次积分项的估值满足
$$
v_{47}(t_j^n/n)\ge n-v_{47}(n)\ge4,\qquad n\ge4.
$$
所以前三项是严格模 $47^4$ 的值。共轭参数实际配对，所有总积分的虚部均为零。

| 微分 | 实际 tiny 积分，模 $47^4$ |
|---|---:|
| $\eta_C$ | 674262 |
| $\eta_{T_2C}$ | 1899975 |
| $\eta_{u-b}$ | 4358404 |
| $\eta_{c-b}$ | 3495672 |
| $\eta_{Z_{-8}-20b}$ | 183817 |
| $\eta_{D-20b}$ | 96867 |
| $\eta_B$ | 2918700 |
| $\eta_{K_{g_1}-106b}$ | 2188696 |

按 (259.3) 加权，
$$
\boxed{\int_{A_1(t)}\eta_{D_P}=4160581\pmod{47^4}.}
\tag{259.14}
$$
输出保留全部八组三阶系数和 54 个实际参数，可直接以标量算术重算每个积分。

## 8. 同一 j 切向下的规范截面坐标

$P$ 的 $j$ 值不与 $0,1728,54000,-3375,8000$ 同余，且
$\Phi_2(j(P),j(P))$、$\Phi_2(0,j(P))$ 模 47 都非零。所以其附近没有 $T_2$ 自交或基点轴相交，$T_2$ 因子的规范坐标是 1。对角因子仍须保留 R148 的实际微分尺度。

写 $g_1=a_Q(j)\,dj$。在 $P$ 的物理模型上，
$$
\beta/dj=(4A^3+27B^2)/(124416A^2B).
$$
以原物理权二尺度求 $a_P$，在 $b$ 处用原 R147/R208 的真正粗参数微分，得到
$$
a_b=3413944,\qquad a_P=621937\pmod q.
$$
二者均为单位，并与 R260 从独立 CM3 coarse jet 得到的结果完全相同。R148 规范交换线性化给
$$
\sigma_{F_2,b}(P)=(-a_b/a_P)^4e(C,D_P).
$$
负号因第四次幂相消。实际坐标及对数为
$$
s(P)=4217438,\qquad \log_{47}s(P)=1482521.
\tag{259.15}
$$
使用的是 R260 碰撞范数中的同一 $j-j(Q)$ 参数，故没有尚未补上的首项换参常数。

## 9. 完整范数运输与最终算式

由 (259.13) 的真实主函数及同一范数线丛规范，
$$
m\lambda(e(C,D_P))
=\int_{A_1(t)}\eta_{D_P}+\log_{47}\Phi_C[D_P].
\tag{259.16}
$$
R260 已完整保留全部主截面、四套实际理想、全部 106 个典范零点及各碰撞首项，得到
$\log_{47}\Phi_C[D_P]=3780398$。没有把任何未求范数隐藏为常数。

$m\bmod q=459340$、$m^{-1}\bmod q=4074216$；独立整数算术给
$$
\begin{aligned}
4160581+3780398&\equiv3061298,\\
4074216\cdot3061298&\equiv2731264,\\
2731264+1482521&\equiv4213785
\end{aligned}
\pmod q.
$$
最后一式即 (259.1)。$m\bmod47=9$，求逆不损失精度。R148 的 800 倍仅在把此单截面高度转为原 QC 高度差时使用，没有提前吸收到本条数值中。

## 10. 对已输出分式的独立审查

verify_R259_ordinary_center47.py 使用独立随机 colon 测试截面，直接检查冻结输出。五个空间均在第一组测试得到准确秩 124、125、105、124、124，另核：

- 全部有限简单极点和留数；
- 覆盖 20 个尖点的两个完整域方程；
- 全部五组共 270 个实际第二族校准值及 $\Omega_2$ 的单位秩 54；
- 已输出分子属于完整候选 Riemann–Roch 空间；
- 全部 819 行真实 $T_2$ trace 方程及 $1/2$ 尺度；
- 用另一套标量二元乘法重算全部八个 tiny 积分；
- 最终单位逆、范数元素高度及规范截面高度。

审查记录 R259-independent-fraction-and-arithmetic-audit.json 的 SHA256：
~~~
c6221a6e777e16757716fcff26755b93ddb3601975f80fe7999f56731822adeb
~~~
复核命令：
~~~bash
OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python agent-qc/verify_R259_ordinary_center47.py \
  --script-dir math-research/topics/serre-uniformity/scripts \
  --certificate root-recovery/ORD_j05_actual_canonical_F2_height47.json.gz \
  --build-dir agent-qc/native-build \
  --output agent-qc/R259-independent-fraction-and-arithmetic-audit.json
~~~

## 11. 整盘延拓的导数核对

此节给后续 R262 的准确公式，不把整盘 Taylor 系数列为本条输出。
写
$$
D_b=162(u-b)-54(c-b)-27(Z_{-8}-20b)+4(K_{g_1}-106b).
$$
在避开固定极点和 $T_2$ 自交的普通开集上，$D(P)=F_2C(P)+D_b$。
两个变量各贡献一次：移动 $T_2C$ 各给 $27T_2\eta_C$，对角项各给
$4\operatorname{reg}_j\eta_C\,dj$，固定 $D_b$ 仅给一次。规范坐标的
$-4d\log a_P$ 与 (259.12) 中的 $+4d\log(g_1/dj)$ 精确相消，于是
$$
\begin{aligned}
d\lambda(\sigma_{F_2,b})={}&54T_2\eta_C(P)
+8\operatorname{reg}_j\eta_C(P)\,dj\\
&+162\eta_{u-b}(P)-27\eta_{Z_{-8}-20b}(P)-54\eta_{c-b}(P)\\
&+\frac{64}{3}\eta_{D-20b}(P)-2\eta_B(P)
+\frac83\frac{dj}{j}+2\frac{dj}{j-1728}.
\end{aligned}
\tag{259.17}
$$
固定 $a_b$ 没有导数，也不额外产生基点尺度项。若以保存的射影
参数 $z$ 写 $\eta_C=(1/(z-p)+r_z+\cdots)dz$，则
$$
r_z=\operatorname{reg}_j\eta_C\,j'+\frac{j''}{2j'},\qquad
8\operatorname{reg}_j\eta_C\,dj=(8r_z-4j''/j')\,dz.
\tag{259.18}
$$
54 是双变量对称因子；(259.10) 的 $1/2$ 是每个二同源分支的真实
微分速度，两者均必须保留。更详细的独立推导另见
R259-independent-local-derivative-audit.md。


## 12. 从已推仓库重建的入口

冻结主生成器保留原运行参数，以确保上文源码SHA和数值证书的对应。
另提供 p41_rebuild_ordinary_F2_center47.py，只在指定工作目录建立
指向已推 scripts/data 的符号链接，再调用冻结生成器。
它将 R247 的 SS_second_kind_rhs47 目录映射到原 SS-second-kind-rhs
输入名，并将已推 ORD_j05_second_kind_complete47.json.gz 放入所需
ordinary-second-kind 输入路径；没有重新生成或改变任何数学输入。

在 topics/serre-uniformity 目录运行：

~~~bash
OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/p41_rebuild_ordinary_F2_center47.py \
  --script-dir scripts \
  --work-dir /workspace/scratch/rebuild-serre-R259 \
  --output /workspace/scratch/rebuild-serre-R259/center.json.gz
~~~

主生成器逐项核输入、51个SS图块SHA及全部实际等式。输出中的绝对
输入路径和运行时间随重建环境变化，因此重建文件不要求压缩字节与
原封存文件一致；所有数学系数、八个tiny和最终4213785应一致。
不必重跑B或普通点的304位群链，也不必重枚举41挠点。
