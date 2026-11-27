# 原 q=11 指定半 Norm 类：完整局部 Fitting 长度

日期：2026-11-27。会话：Astra-rank2-Sha-0b097461-20261127。

本入口继续消费已付原 q=11 点、原谱平方根 R 和完整 Prym Norm
除子。它只计算 [R1041](../results/R1041-original-four-point-spectral-cover-pell-unit-and-half-norm.md)
(36)指定的半类 $A_Q$；不从完整零类任意选择一半。
源码：
[scripts/consume-original-q11-specified-half-norm.py](../scripts/consume-original-q11-specified-half-norm.py)。
本稿写成时尚未执行，以下是完整算法及其所算对象的证明。

## 1. 实时固定输入

直接输入为完整 Norm 回执：

- run45980566265 / job140443090086；
- source4b315bb783233d98ce623d99fa3dffdca9228683；
- request_id 2026-11-27-1015-original-q11-prym-norm-divisors；
- 原源码 SHA256
  732332d88af3b58952a998c34c46728c9771838a58640264644cade0176622ea；
- stdout4516字节、SHA256
  2b0cb545e42234c5958484b4af29108d8562689891f40eb00321be9e798aa742；
- 必要完整除子数据摘要
  1a45359417b39f1425fac1f3f3d93ad80877de7c04cc4c1fd35ab557e807ee13。

此回执所钉的 lift 回执、以及 lift 所钉的原唯一截面回执，
均按其中原 run/job/source/request/script/stdout 身份实时读取。
原4516字节和两层原输出均不缓存入源码或数据文件。
程序不调用三个旧入口的 main，不重新搜索 D、
不重新求平方根、不重新分解完整 Norm。
仅导入已钉 SHA256 的原读取器。

有限域为 $\mathbf F_{121}=\mathbf F_{11}(\delta)$，
保持 $\delta^2=-3$、$\delta^{11}=-\delta$。
输出所有常数都使用准确基 $1,\delta$ 的两个系数，
与库内部选择的有限域基无关。
换另一个 δ 根等于一致地更换原反点方向；
R1041(37)已经证明最终 $A_Q$ 不受这个整体选择影响。

## 2. 同一个二盖上的准确选择函数

保持真实扭曲模型
$$
 E_T:\ Y_T^2=X_T^3-108X_T-540,\qquad
 X_T=-3x_L,\quad Y_T=-3\delta y_L,
\tag{1}
$$
及原反向
$$
 z=5\frac{X_T+12}{X_T+3},\quad
 Z=\delta W_L=\frac{9\cdot25\,Y_T}{(X_T+3)^2}.
\tag{2}
$$
在它的真正二盖中
$$
 s^2=g(z),\quad w=sZ/\delta,\quad
 X=-3z/(z^3-4),\quad
 2Y+1=w(z^3+2)/(z^3-4)^2.
\tag{3}
$$
代入已经付出的 R 和原 W，取
$$
 F=F_Q=\frac{sR}{z-2X}
        +\delta\,\frac{1-w/(z^3-4)}6,
$$
$$
 L_+=\delta W-t,\qquad L_-=\delta W+t,\qquad t=-Y/27.
\tag{4}
$$
W 由原唯一截面的原坐标直接代入；没有在这里重新从 Norm
猜一个 W 符号。

原 x=0 时，Q=P3 与 Q=−P3 分别由 $L_+=0$、
$L_-=0$ 识别。对好纤维的 $P_3=(0,0)$，
原 Tate 方程给 y 的局部阶是 x 的三倍，
所以 $L_+=x+2y$ 与 x 有相同零阶，而 $L_-$ 是单位。
在另一三挠点相反。因此
$$
 \gcd(\operatorname{div}_0F,\operatorname{div}_0L_+)=Z_+,
 \qquad
 \gcd(\operatorname{div}_0F,\operatorname{div}_0L_-)=Z_-,
\tag{5}
$$
保全部原重数。两个除子各次数12；它们不是仅由
$N_Q$ 的某个多项式因子是否在 $\mathbf F_{11}$ 中分裂来区分。

## 3. 原完整回执为何允许完整局部矩阵

已付 Norm 回执证明 $N_Q$ 的全部零有限，正除子次数24，
且不存在无穷零。R1041又付 $\deg\operatorname{div}_\infty F=24$，
因此沿 r 取 Norm 没有零极相消。

这些实际零处，(2)的原图均处在 $s^2=g$ 的整 étale 图中：
g 的零基因子 $X_T^2+4X_T+8$ 已在原 Norm 的极中，
$X_T+3$ 也不出现在原零中。
原零上 $Y_T\ne0$；这是原全部不可约因子和指定分支的直接核对，
包含 $X_T=9,Y_T=8$ 的二重零。
所以在每个这样的 EL 点的离散赋值环 $\mathcal O$ 上，
$$
 \mathcal A=\mathcal O[s]/(s^2-g)
\tag{6}
$$
是完整整 étale 二次代数，基准确为 $1,s$。
F、$L_\pm$ 均在 $\mathcal A$ 中正则：
两个 r 分支都不含 F 的极，原 W、t 亦正则。
这些条件针对已钉的实际输入逐点使用，
没有把潜在坏支从一个一般算法里偷偷删去。

## 4. 两个 Fitting 长度准确分离全部厚零

将 $F=a+bs$、$L=c+ds$ 写在(6)中。
乘法矩阵是
$$
 M_F=\begin{pmatrix}a&gb\\b&a\end{pmatrix},\qquad
 M_L=\begin{pmatrix}c&gd\\d&c\end{pmatrix}.
\tag{7}
$$
有限 $\mathcal O$ 模 $\mathcal A/(F,L)$
由四列矩阵 $[M_F\ M_L]$ 呈示。
在 DVR 上作 Smith 标准形，便得
$$
 \operatorname{length}_{\mathcal O}\mathcal A/(F,L)
 =\min\{v(\text{全部六个二阶子式})\}.
\tag{8}
$$
此长度准确为 $r_*\gcd(\operatorname{div}_0F,
\operatorname{div}_0L)$ 在该 EL 点的重数。
它同时处理 r 的两个分支、剩余域次数和非约化厚点，
无需猜哪一支对应 $Q=P_3$。
特别原二重 Norm 零若由两个不同 r 点贡献，
(8)仍会按照 $L_\pm$ 分开，而不是将总重数2全部给某一半。

在每个原完整 Norm 零处，对 $L_+$ 和 $L_-$ 分别用(8)。
所得两个非负整数之和必须恰为该点已付的完整 Norm 零阶；
各点加上闭点次数之后，两半次数均为12。
这是(5)的完整局部分割。

## 5. 局部赋值不靠点采样

原 Norm 零因子在 $\mathbf F_{121}$ 上完全因式分解，
每个指定支记为
$$
 h(X_T)=0,\qquad Y_T\equiv r(X_T)\pmod h.
$$
其 $2r$ 可逆。对任意所需精度 M，
用
$$
 r_{\rm new}=r+(P-r^2)/(2r)
   \pmod{h^{\min(2m,M)}}
\tag{9}
$$
逐倍提升，得到该同一支在所有厚层上的根。
若子式写为
$$
 (A(X_T)+B(X_T)Y_T)/D(X_T),
$$
则完整赋值是
$$
 v_h(A+B r_M)-v_h(D).
\tag{10}
$$
精度取大于原 Norm 零阶加 $v_h(D)$，
足以准确求(8)的最小值：
矩阵本身包含 $\det M_F=N_Q$，
故该最小值不会超过已付的 Norm 零阶。
即使分子在某个指定支上与分母高阶相消，
(9)–(10)也保留正确阶数；只代入剩余域一次不够。

只允许将超过这个明确上界的阶截为上界，
不会把未决定的高阶零当成精确值。

## 6. 返回准确原 E_L 和有限参考点

两半的每个完整闭点、指定支和重数按
[完整除子入口](2026-11-27-original-q11-g-cover-prym-divisors.md)§5
已经给出的 Cantor 公式分别相加。
得到 $E_T(\mathbf F_{121})$ 上两点；
相加应为 O，因为完整 Norm 零除子类已付为 O。

准确返回原模型的坐标是
$$
 \boxed{x_L=-X_T/3,\qquad y_L=\delta Y_T/9.}
\tag{11}
$$
程序检查第一点的两个原坐标均固定于11次 Frobenius；
由 R1041(36)–(38)，它正是指定的
$A_Q\in E_L(\mathbf F_{11})$。
第二点返回其负点。

为给所得点一个固定有理参考，取
$$
 G=(-2,-6)\in E_L(\mathbf Q).
$$
原群律给 $2G=(4,6)$、$4G=(1,3)$。
在 q=11，$2(1,3)=(3,0)$，故 G 恰有阶16。
Hasse 界使 $\#E_L(\mathbf F_{11})$ 位于6与18之间，
于是这个阶16子群就是整个群。
程序因此输出唯一的 $k\in\{0,\ldots,15\}$ 使
$A_Q=kG$，以及该点的准确阶。
这一步只对已经得到的一个点作固定有限群律，
不搜索素数、不重新搜索截面。

本次实际结果尚待公开执行，不预设 k、$A_Q\ne0$，
也不把 q=11 的半类与原27对有权和或最高 AJ 等同。


## 7. 本次公开请求

原源码 20848 字节，SHA256 `7a560c5e2855fa6c38f5e73d0b67a7e9a7eb7251e13b0d94a752f586e1e694b3`。本次请求 `2026-11-27-1048-original-q11-specified-half-norm`，使用固定 python-flint 0.9.0；仅消费三层已付回执并计算本篇新指定半类，不缓存旧生成数据。实际结果待原公开作业返回。有限域/多项式接口按 [fq_default](https://python-flint.readthedocs.io/en/latest/fq_default.html) 与 [fq_default_poly](https://python-flint.readthedocs.io/en/latest/fq_default_poly.html) 的0.9.0原文。


## 8. 首次真实终态及唯一兼容修复

原请求实际 run45985234568 / job140459035605 / source a4e66e2d32dba6d46a74c1f7ce6c220e5d3ac762 于10:48:57 UTC以 failure 结束。10:48:55 的栈明确是 `ELT(delta) → fp → GF(value)`：python-flint 0.9.0 的 `fq_default_ctx` 不接受再次包装现成的 `fq_default`。原三层回执已读，新的局部 Fitting 尚未执行；不存在半类结果。

完整日志10835字节，SHA256 `03dc9c396f9f72dec0851514eaf27e9e6217209ab0f9cea75ccc087c3730a9cf`。只为同一个固定有限域的原元素增加恒等 `field_coerce`，并在 `fp`、`encode_constant` 两处使用；δ、所有原点、厚层、六minor和Cantor公式均原样保持。新源码21050字节，SHA256 `3864c88a9f05bf50801afd46d83a496103193bc9d4aa5567bffefda084c3a6bd`。后继唯一请求 `2026-11-27-1050-original-q11-specified-half-norm-native-coercion`，实际回执待。


## 9. 真实完整结果：指定半类为 −G

唯一修复后继已实际成功：

- run [45985515813](https://github.com/Rogerhu12/math-research-public/actions/runs/45985515813)，job140459993008；source `239d3f42206392460b4c345ec85fbb547104c739`。
- 2026-11-27 10:50:49–10:51:00 UTC；原数学主体2.6749128069999983秒。
- stdout4014字节，SHA256 `27241069e4ac437e85b8a51bf3900e1f59e268a1a10e366fe49157d618143d54`。
- 完整日志13198字节，SHA256 `23b2ada476c29948dc7344f0ef3646db99294a7abcb503f64dd88c23b00b6fe7`。
- 必要除子payload2525字节，SHA256 `534b05290b9865e4f6de7dce44e67de2549f6fab1172fd1804c2fef0796eb853`。根从实际JSON逐字重建两项摘要；生成输出未保存入库。

下面只保辨认指定半类所需的完整闭点、厚重数和原方向。所有多项式系数按低到高排列，系数在 $\mathbf F_{11}(\delta)$，$\delta^2=-3$；每行给基因子 $h$、实际 $Y_T\bmod h$ 与两个完整局部 Fitting 长度。

| $h$ 的系数 | $Y_T\bmod h$ 的系数 | 度 | 原全零阶 | $Q=P_3$ 长度 | $Q=-P_3$ 长度 |
|---|---|---:|---:|---:|---:|
| $[0,1]$ | $[2δ]$ | 1 | 1 | 1 | 0 |
| $[0,1]$ | $[9δ]$ | 1 | 1 | 0 | 1 |
| $[2,1]$ | $[8]$ | 1 | 2 | 1 | 1 |
| $[3+3δ,10+9δ,1]$ | $[10δ,6+4δ]$ | 2 | 1 | 0 | 1 |
| $[3+8δ,10+2δ,1]$ | $[δ,6+7δ]$ | 2 | 1 | 1 | 0 |
| $[4+2δ,7+δ,5+3δ,1]$ | $[7+8δ,10+3δ,8+9δ]$ | 3 | 1 | 1 | 0 |
| $[4+9δ,7+10δ,5+8δ,1]$ | $[7+3δ,10+8δ,8+2δ]$ | 3 | 1 | 0 | 1 |
| $[5+3δ,4,1]$ | $[10+δ,9+4δ]$ | 2 | 1 | 1 | 0 |
| $[5+8δ,4,1]$ | $[10+10δ,9+7δ]$ | 2 | 1 | 0 | 1 |
| $[6+2δ,8+3δ,1]$ | $[10δ,7+3δ]$ | 2 | 1 | 0 | 1 |
| $[6+9δ,8+8δ,1]$ | $[δ,7+8δ]$ | 2 | 1 | 1 | 0 |
| $[8,1]$ | $[2δ]$ | 1 | 1 | 0 | 1 |
| $[8,1]$ | $[9δ]$ | 1 | 1 | 1 | 0 |

特别，$(X_T,Y_T)=(9,8)$ 的真实二重零分成 $1+1$，没有整批划入一个半部。全部两半次数分别为12，和为完整24；没有无穷零或漏支。分别用本篇完整 Cantor 公式返回，得
$$
[r_*Z_+-12O_{E_T}]=(6,4\delta),\qquad
[r_*Z_--12O_{E_T}]=(6,7\delta).
$$
准确去 twist 后，
$$
\boxed{A_Q=(9,6)=-G\in E_L(\mathbf F_{11}),\qquad
[r_*Z_--12O_{E_L}]=(9,5)=G,\qquad\operatorname{ord}(A_Q)=16.}
$$
这是使用原 $\delta W=t$ 指定的第一半，实际 $k=15$；不是从整零类中任取一个非零分解。两半完整类相加为 O，原13个闭点/厚层、两总次数、全部 Norm 及原坐标 Frobenius 均已返回。

还有一个必须保持的范围结论。因为 $4G=P=(1,3)$、$16G=0$，
$$
\boxed{[12]A_Q=[4]G=P\ne O.}
$$
原 q11 的旧最高 shadow 被 $q+1=12$ 杀，故这个指定半 Norm 类**本身**不能未经其它原投影或对应就等同该 shadow。这里得到了非零的二主半类，未证明一般 q 的固定公式、原27对非零或无穷目标 p。后继继续原 halving 图、固定边界及真实最高权的比较，不扩大有限素数扫描。
