# Phi 整 D2=0 最高方向：三条原权 cofactor 与整头单位的新返回

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。
状态：新输入尚未执行，60 秒 / 1 GiB。

## 1. 固定原图与新的数学目标

[原五权支持](../results/R150-appendix-unit211-Phi-zero-highest-D2-zero-five-weight-support.md)已从原 F6 和已付 M、ell 证明：当前 Phi=0、物理 D≠0 图的最高 D2=0 共同方向必须满足
$$
\ell=\frac12,\quad t=1,\quad Q=4(u-1)(u-2).
$$
同一原 Rbar、W4、Obar、N1 的最高部分定义为
$$
h_i(u,s)=[\lambda^2]F_i\bigl(u,4(u-1)(u-2),\lambda,\lambda,\lambda s\bigr).
$$
之前在 QQ(u)[s] 的四原来源给 C16，剥已付单位后为六次 C6；其完整分解为四次因子乘一次因子平方，留下五个整权纤维。未排除这些纤维。

本次改变目标：三组固定原式各作不除首项的纯权 cofactor，随后在 QQ[u] 中求真实多项式 Bezout gcd。特别是 Obar、N1 必须参与最后的纯权共同支持；不再以泛型 QQ(u)[s] 常数行代替全 u 返回。源码只读此前构造 h_i 的必要前缀，停在旧 Euclid 执行之前。

## 2. 包含所有首项零纤维的明确原恒等式

写两个原二次式
$$
A=as^2+bs+c,\qquad B=ds^2+es+f,
$$
并置
$$
l_1=ae-db,\qquad l_0=af-dc.
$$
固定 2/2 次 Sylvester 多项式为
$$
R_{A,B}=l_0^2-l_1(bf-ce).
$$
不除 a、d 或 l1 的完整身份是
$$
\boxed{
R_{A,B}
=(e l_1+d l_1s-d l_0)A
 -(a l_1s+b l_1-a l_0)B.
}
$$
源码完整乘回这个原多项式等式。它在 a=d=0 或其它首项下降时仍成立。

本次固定三组为
$$
(Rbar,W4),\qquad(Rbar,Obar),\qquad(Rbar,N1).
$$
它们均取第 1 节的真实最高部分。每条 cofactor 的全部分母逐项验证只含原已付权因子；清这些分母及非零 QQ 常数，得到三个真正原理想元素 r1(u)、r2(u)、r3(u)。没有把未知权内容或谱首项提前除掉。

## 3. 真正完整的 QQ[u] 共同支持

源码对三个 r_i 在 QQ[u] 中扩展 Euclid，每次多项式除法乘回，并保持三个完整来源：
$$
G(u)=v_1(u)r_1(u)+v_2(u)r_2(u)+v_3(u)r_3(u).
$$
这里的 v_i 是 QQ[u] 多项式，系数逆仅为非零有理常数。因此在每个例外 u 纤维上，这仍是真实原最高理想身份；与泛型 QQ(u)[s] 的中间主元不同。

若 G 为非零常数，整个 D2=0 最高原方向排除。否则只可剥第 4 节的已付单位，保全部最终剩余多项式的零纤维。三个 r_i 的 gcd 为一若发生，是一元 QQ[u] 的实际 Bezout 单位身份，不是多变量 gcd 判空。

## 4. 当前原图的全部所用单位

此前已有 u、u−1、Q、delta、ell；在整曲线 Q=4(u−1)(u−2) 上也可付 u−2。新增使用的既有单位是：

- m=u−ell：来自[整等权 b=c 原排除](../results/R150-appendix-unit211-equal-weights-complete-original-exclusion.md)，原 rho 已付且 b−c=(u−ell)/rho。当前 ell=1/2，故 2u−1 为单位；不外推 D0 碰撞图。
- u+Q−1：来自[整个一般 Q=1-u 原排除](../results/R150-appendix-unit211-Q1minusU-complete-original-exclusion.md)，在曲线上保持原多项式 u+4(u−1)(u−2)−1。
- 整个第一二次头：来自[整 H1 原排除](../results/R150-appendix-unit211-Phi-zero-whole-H1-complete-original-exclusion.md)。新源码直接从原 Rbar、W4、Obar 的 T²、Tz、z² 三列构造 3×3 头行列式，再代整权曲线；只构造行列式，不求其逆、不运行旧原头图 cofactor。

原头的分母已由同一原权单位验证，所以该分子的全部因素在当前图都可付。若整个曲线上原头恒为零，则当前曲线直接由整 H1 排除；否则只按其真实分子剥最后 G 的公因子。每次精确整除及全部剥除乘积均返回。

新的单位返回若成功，只关闭当前 D2=0 的整个最高原方向；不声称其余最高方向、原仿射图、一般 D0 图或 ordinary ISP 已完成。

## 5. 唯一新源

源文件：
notes/2026-11-28-unit211-Phi-zero-whole-D2-infinity-original-weight-cofactor-unit-8542.py

blob：297a59c19e56196101af746bd881e444f3b809b8。
6821 字节，SHA256：
be4e95231be36d1de37a33a76abf87dda587a982cb7b77df0a8318c346eb4b90。

两个依赖按同目录完整 basename 暂存：

1. 2026-11-28-unit211-Phi-zero-whole-D2-zero-infinity-original-four-quadratics-8542.py，SHA256 baf684e40df5e447c6dfcb9f5eb3eef8173d28d6ae1a37e152c4475ff342b03c；只执行 g=rows[0] 之前的原式构造，旧 Euclid 不执行。
2. 2026-11-27-unit211-Phi-zero-first-quadratic-head-three-original-rows-D-input-8542.py，SHA256 100ce4dfb7380da1591cd453aae392e2dafcaaceb3a601c4500d07852841ecaf；内部只执行 quads 构造前的 4452 字节原式定义。

外层和全部嵌套 alarm/setitimer 都钳制在最初绝对 60 秒截止。不读取历史系数 JSON，不重算旧 Gaussian、P6/P9、范数或模块，不保存可重算系数载荷、编码或分片。仅保源、原定义、哈希和本次准确回执。
