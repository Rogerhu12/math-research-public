# 参考消期的固定 jet 修复与原始 Frobenius 的收缩

日期：2026-11-12。**状态：以下四维资料的恢复、最小九阶 jet 和
原始算子的行为已证明。尚没有得到目标中央系数的 Frobenius 比较。**

沿用 [实际覆盖及 exact kernel](2026-11-12-reference-cover-class-and-exact-kernel.md)：

$$
 D_+:Z^2=f(u)=2u(u^2-4)(u^2-8),\qquad
 \eta_R=\frac{256}{u^7}R((u^2-4)/4)\frac{du}{Z},
$$

其中 $R=r_0X^3+r_1X^2+r_2X+r_3$，$A_R=\sqrt{x}R(x^2)\sigma^{17}$。
本文只保留固定参考 $S=(x^2+1)\sigma^4$ 的实际规范，不把
$A_R/S^{17/4}$ 的乘法商换成系数的商。

## 1. class 加两个 primitive 模态准确恢复四参数

对每个 $R$，前篇的三角 Hermite reduction 唯一给

$$
 \eta_R=dF_R+(a u+b u^3)\frac{du}{Z},\qquad
 F_R=Z\left(\frac{c_1}{u}+\frac{c_3}{u^3}
                      +\frac{c_5}{u^5}+\frac{c_7}{u^7}\right).
                                                               \tag{1.1}
$$

唯一性来自依次消去 $u^{-7},u^{-5},u^{-3},u^{-1}$；其非零主系数
分别为 $-416,-288,-160,-32$。余下的两个多项式项是

$$
                    a=c_3+12c_1,\qquad b=-3c_1.             \tag{1.2}
$$

因此给定 $(a,b)$ 就已确定 $c_1,c_3$。
完整线性映射

$$
        R\longmapsto(a,b,c_5,c_7)\in\mathbb Q^4              \tag{1.3}
$$

是同构。事实上若四坐标全零，由 (1.2) 还得 $c_1=c_3=0$，
故 $F_R=0$、$\eta_R=0$；(2.4) 的显式下降式随即给 $R=0$。
两边同为四维，故单射即为同构。

这一步保留了在 de Rham 类中被抛掉的两个 exact primitive 模态。
它没有改变实际截面，也没有把无关的 Taylor 参数添加为自由变量。

## 2. 两个模态就是第五、九阶 jet

在从 $E_1$ 原点选择的实际分支上，$z=\log_Et$，有

$$
 x(z)=z^{-2}+\frac15z^2+O(z^6),\qquad
 u=2\sqrt{x^2+1}=2z^{-2}\left(1+\frac7{10}z^4+O(z^8)\right).
                                                               \tag{2.1}
$$

原曲线规范 $y(z)=-z^{-3}+\cdots$ 及前篇的 $Y_+,Z$ 定义固定符号为

$$
 Z=-\sqrt2\,u^{5/2}
                 \left(1-\frac6{u^2}+O(u^{-4})\right).
$$

根号在这里仅用来写所选局部分支；最终 Laurent 系数有理。
代入 (2.1) 得

$$
 \boxed{
 \frac{Z}{u^5}=-\frac14z^5+\frac{13}{16}z^9+O(z^{13}),
 \qquad
 \frac{Z}{u^7}=-\frac1{16}z^9+O(z^{13}).
 }                                                             \tag{2.2}
$$

给定 (1.1) 的 class 坐标后，先减去已确定的
$Z(c_1/u+c_3/u^3)$。剩余原函数 $F_R^{\rm ex}$ 的两个实际 jet 为

$$
 [z^5]F_R^{\rm ex}=-c_5/4,\qquad
 [z^9]F_R^{\rm ex}=(13c_5-c_7)/16.                            \tag{2.3}
$$

该三角矩阵可逆。因此

$$
 R\longmapsto
 \bigl([\eta_R],\ [z^5]F_R^{\rm ex},\ [z^9]F_R^{\rm ex}\bigr)
                                                               \tag{2.4}
$$

准确恢复原四参数。

九阶是这个规范下必要的最低统一截断阶数。前篇
$K(X)=9X^2-15X+2$ 有

$$
 [\eta_K]=0,\qquad
 F_K=-16Z/u^7=z^9+O(z^{13}),                                  \tag{2.5}
$$

所以保留到八阶仍把这个非零 $K$ 送到零。保留到九阶则由 (2.3)
已经足够。

## 3. 参考因子怎样实际参与 prime jet

沿所选分支，(1.1) 不是直接给 $A_Rdz$，而是给

$$
 A_R(z)\,dz=S(z)^{17/4}
       \left(dF_R+(a u+b u^3)\frac{du}{Z}\right).             \tag{3.1}
$$

所以 exact primitive 对目标系数的贡献不能在积分前丢掉。
作为最低阶的准确核验，$S(z)=1+\tfrac43z^4+O(z^8)$，故

$$
 S(z)^{17/4}=1+\frac{17}{3}z^4+O(z^8).
$$

若 $[\eta_R]=0$ 且 $F_R=A_5z^5+A_9z^9+\cdots$，则

$$
 [z^4]A_R=5A_5,\qquad
 [z^8]A_R=9A_9+\frac{85}{3}A_5.                              \tag{3.2}
$$

取 (2.5) 即得到 $[z^8]A_K=9$。这逐式展示了原函数的九阶 jet
如何在同一个参考因子下改变 $p=7$ 的 prime diagonal。

一般权仍须使用 (3.1) 的完整卷积，而不是仅用 $[\eta_R]$ 或
两个模态的静态值。式 (2.4) 表明这些固定资料足以恢复整个截面，
但本身没有提供作用在它们上的实际 Frobenius 插值定理。

## 4. 原始 Cartier 与原始 Frobenius 不保留所需两个模态

在好素数处，Cartier 准确杀掉 $dF_R^{\rm ex}$。
因此在 (2.4) 上仅使用通常的 cohomology Cartier，仍会忘掉两个
新增坐标；补上它们的名字不构成目标与 Cartier 的比较。

另一方面，对 $p\ge11$，原始绝对 Frobenius 在原点九阶 jet 环
$\mathbb F_p[z]/(z^{10})$ 上把每个正阶幂都送到零。
尤其是两个模态 $z^5,z^9$ 分别被送到 $z^{5p},z^{9p}$，在这个
固定截断中均为零。
这里 $z$ 可与整代数参数交换：惰性高度二的形式对数在次数小于
$p^2$ 时整，已在 [半因子首层](2026-11-12-inert-half-factor-first-layer.md)
§2 证明；所以这个低阶 jet 判断与坐标选择无关。

这只说明**原始** Frobenius/Cartier 的直接补充不够。
若使用带除 $p$ 的算子、Gauss–Manin 比较、参考 theta 连接或更高
模 $p^2$ 的资料，必须把该算子与 (3.1) 的完整参考乘积逐式比较。
本篇没有否定这样的比较，也没有把一个任意 Frobenius lift 的
修正项当成规范的算术输入。

## 5. 已闭合与未闭合的接口

已闭合的是一个固定四维、保持实际规范的恢复问题：两个 class
坐标加第五和第九阶 primitive jet，准确恢复原 $R$，且九阶必要。
它使“需要保留 exact 数据”具体化为有限的两个模态。

未闭合的是给这一恢复资料构造一个与中央插值一致的、规范的
带参考因子 Frobenius 操作。原始 Cartier 和原始 Frobenius 已按
上节准确排除；没有据此重新声称覆盖普通性足以给主课题非零。
