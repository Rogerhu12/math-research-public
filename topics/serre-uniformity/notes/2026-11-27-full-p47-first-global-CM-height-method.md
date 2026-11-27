# 原 full47 第一项全局 CM 高度的有限计算方法

日期：2026-11-27（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。  
**状态：新计算请求，未预设结果非零。** 原理论输入为 R1094、R1096–R1099，
不重跑原秩、MW、Hodge、CM-log、八盘标签或旧level41高度。

## 1. 本次准确目标

原 $X=X_{\rm ns}^+(47)$，$q=4513$，
$u_a=23y_a-C_\infty$（$a=4,16$），
$B=q+1-T_q$。只读第一新数值
$$
\Gamma(1)=q^{-1}h(Bu_4,Bu_{16})\pmod q.
$$
[R1094](../results/R1094-original-disjoint-CM-heights-and-first-global-intersection-functional.md)
和 [R1096](../results/R1096-certified-original-CM-moving-units-and-odd-Hecke-height-basis.md)
已付原 $h_q\in q^2\mathbf Z_q$，
所以准确地
$$
\Gamma(1)=\sum_{\ell\ne q}I_\ell(Bu_4,Bu_{16})
       \frac{\ell^{q-1}-1}{q}\pmod q.
\tag{1}
$$
Fermat商用 $\ell^{q-1}\bmod q^2$ 精确读取，符号为正；
这是原 $\chi_\ell(\ell)=-\log_q\ell$ 的归一，不是实高度。

## 2. 所有奇好素数一次枚举

[R1097](../results/R1097-original-level47-odd-prime-CM-intersections-and-sparse-norm-sum.md)
给 $m=1,q,q^2$ 的原交数
$$
G_\ell(m)=\frac1{16}
 \sum_{\substack{A+B=8m,\ A,B>0,\ 4\nmid A\\
                 2209\mid A\ {\rm or}\ 2209\mid B,\ \ell\mid B}}
 r_2(A)r_2(B/\ell)(v_\ell B+1)
$$
（$\ell\equiv3\bmod4,\ell\ne47$）；其余奇好素数为0。
两个进程恰为
$$
(A,B)=(2209s,8m-2209s),\quad(8m-2209s,2209s),
$$
$1\le s\le(8m-1)/2209$，$4\nmid s$。
因 $47\nmid m$，二者不重合。

对正整数 $t$ 精确因子分解后，
$r_2(t)$ 为 $4\prod_{r\equiv1(4)}(v_r(t)+1)$，
除非有 $r\equiv3(4)$ 的奇赋值，此时为0。
因此 $r_2(B/\ell)$ 非零恰当 $B$ 有且仅有一个
奇赋值的惰性素因子 $\ell$。
一次分解 $B$ 即支付所有 $\ell$；
不需要从2扫到 $8m$ 的素数窗口。
$47^2$ 为惰性素数的平方，故 $r_2(2209s)=r_2(s)$；
第二进程加上这个平方不改变奇赋值惰性因子列表。
消费者逐项除16并要求整数，完整保 $\ell=3$。

对三个 $m$ 的所得字典按
$$
c=(q^2+3q+1,\ -2(q+1),\ 1)
$$
线性组合并乘 $23^2$，得到全部奇好 $I_\ell$。
$T_{q^2}$ 是全部 degree $q^2$ 子群而非仅循环核。
本处 $q\equiv1\bmod4$，原 $q$ 局部项由(1)单独消失，
不在这个非q字典中。

## 3. 原2处与坏47水平项

[R1099](../results/R1099-original-level47-dyadic-CM-intersections.md) 的
$$
G_2(m)=\frac14\left(
 \sum_{2209s\le m}r_2(s)r_2(m-2209s)
 +\sum_{\substack{0<2209s<4m\\s\equiv2(4)}}
 r_2(s)r_2(4m-2209s)\right)
$$
完整保 $s=0$ 和半整数 Hurwitz 格；$r_2(0)=1$。
实际 $I_2=23^2\sum c_jG_2(q^j)$。

[R1098](../results/R1098-original-bad47-CM-intersections-and-exact-vertical-correction.md)
的坏47水平式进一步按 $B=47^3t$ 写为
$$
H_{47}(m)=\frac1{16}
 \sum_{\substack{0<47^3t<8m\\4\nmid t}}
 r_2(t)r_2(8m-47^3t)(2+v_{47}t).
$$
这是 $r_2(47^2t)=r_2(t)$ 的直接代入。
坏47不能加好素处的模2209筛选。
$m=1,q$ 的和为空；
$m=q^2$ 只有约一千五百个候选，无大degree核扫描。

## 4. 五维 Brandt 的实际基标定与完整垂直项

用官方 Sage10.6 的 $B_{47}=\operatorname{BrandtModule}(47)$。
它的五个 monodromy weights 排序为 $1,1,1,2,3$；
唯一 weight2 的标准行向量 $e_4$ 是原 $j=1728$。
实际 row-action 矩阵 $M_2$ 满足
$$
v_{16}=(e_4M_2-e_4)/2.
$$
消费者验证此为另一个标准基向量，因原 literal
$T_2[E_4]=[E_4]+2[E_{16}]$，它准确标定原 $j=44$。
不猜 right-ideal basis 的排序。

取 $H_q=B_{47}.\operatorname{hecke\_matrix}(q,\text{algorithm='brandt'})$。
官方10.6源码用 theta series 到 $2q+10$，
并在取得 Hecke 矩阵时转置 Brandt series；
消费者使用前者的实际 row convention，
不直接取后者的未转置系数。
检查全部行和 $q+1$、原 $W=\operatorname{diag}(e_i)$ 的
$H_qW=WH_q^{\mathsf t}$、与 $M_2$ 交换。
$$
b(1)=(v_{16})_4,\quad b(q)=(v_{16}H_q)_4,\quad
b(q^2)=(v_{16}(H_q^2-qI))_4.
$$
此外只在小指标 $q$，按 R1098 的直接范数式独立核 $b(q)$，
支付矩阵方向和2核尺度；不扫描 $q^2$ 范数。
完整垂直项是
$$
23(v_{16}((q+1)I-H_q)^2)_4
=23\sum c_jb(q^j).
$$
加 $23^2\sum c_jH_{47}(q^j)$ 得准确 $I_{47}$。

官方源码：
[Sage10.6 brandt.py](https://github.com/sagemath/sage/blob/10.6/src/sage/modular/quatalg/brandt.py)，
函数 `hecke_matrix`、`_compute_hecke_matrix_brandt`、
`_compute_hecke_matrix_directly`、`monodromy_weights`。
整数分解使用 PARI，`proof=True`，并逐次核乘积。
没有浮点比较或启发式因子分解。

## 5. 执行与输出契约

仅本公开仓库 Actions，固定官方 SageMath10.6镜像
sagemath/sagemath@sha256:60dfb09e8d1399e127a0d7b62b45eef1044574bae397df51bb6ba38df5498879。
请求锁两README、五个理论结果、本方法及消费者 SHA256，
核实际 checkout 与 GITHUB_SHA 相同。
总数学900秒，reserve30秒，超时输出已经完成的阶段并失败退出，
不把部分素数和当成高度。

输出真实 $\Gamma(1)$ 及零/非零、2/47/奇好三项贡献、
三个 $m$ 的小摘要与完整局部表hash。
零是合法答案；并不因此放宽目标。
不输出或保存长数组、全部分解、theta series、artifact或Release。
仓库只留代码、参数、真实run/job、输出hash和小结论。

本次只给一个原全局高度。即便非零，也不等于全部73维块单位，
不等于八CM盘内部分类，更不等于全素数 Serre 一致性。
后继继续完整实际高度泛函及 open.md 的全局障碍。
