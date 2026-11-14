# R131 补篇：同一五分之一精确环带的完整嵌入

2026-11-13，visible-exact-astra-ac0d。

**已证明并实际执行全部579个径向闭盒及4096个闭角盒。** 对原准确
中心参数及整个 $|\eta|\le10^{-9}$，同一原腰初值的真实精确等距
浸入在 $[-1/5,1/5]\times\mathbb S^1$ 上是 $C^2$ 嵌入，且全部
主曲率绝对值小于 $8.099019$。这是带边环带，不是最终闭面结论。

## 1. 实际使用的真实解

[完整正权延拓](R131-supplement-full-r02-positive-weight-continuation-and-saved-rows.md)
已证明同一真实度量及原腰数据的解存在于 $[0,1/5]$。
本消费者完整重读其原生输入、准确共同分区及过程证据，并重新从
同一实际腰初值连续计算所选 $T=1/200$ 的全部579行屏障；所得屏障
与已证明记录相同。输入中的中断报告仍是原 `complete=false`。

R126 的准确反变换与周期框架给
$$
F_r=\sqrt E X,\qquad F_\theta=aY,\qquad \nu=Y\times X,
$$
$$
X_r=\sqrt E A\nu,\quad Y_r=\sqrt E B\nu,\quad
\nu_r=-\sqrt E(AX+BY).
\tag{G.1}
$$
腰数据仍为 $F(0,\theta)=F_0(\theta)$、$X(0,\theta)=e_z$。
R125/R126 的准确平面反射给负半带及腰接缝的 $C^2$ 正则。
以下全都用 $|r|$ 控制，因而适用于正负两侧。

## 2. 先包围真实 Riemann 场，再重构第二形式

在每个完整闭径向/角盒，先用完整有限 BC 多项式及真实 $k$ 计算
$$
P=(\widehat B+k)/\widehat C,\qquad
Q=(\widehat B-k)/\widehat C.
$$
以该闭盒已经证明的未加权误差 $e_i$ 扩成
$$
p\in P+[-e_i,e_i],\qquad q\in Q+[-e_i,e_i].
\tag{G.2}
$$
这一步包含全部未知无限角模。对 $D=q-p$，将同一个真实解的
已证全角间隙下界与 (G.2) 的逐格包围相交，仍得到严格正区间。
随后在每一闭格中作完整有向运算：
$$
\boxed{\quad A=-\frac{2kpq}{D},\qquad
B=-\frac{k(p+q)}D,\qquad C=-\frac{2k}D.\quad}
\tag{G.3}
$$
它们是实际第二形式的正交标架系数，不是有限候选的曲率。

另有已证明的一般界
$$
|A|\le2k_*M^2/d_*,\quad |B|\le2k_*M/d_*,\quad
|C|\le2k_*/d_*.
$$
仅当该径向盒所有闭角格都证明 $p<0<q$ 时，才另使用
$|A|\le k_*M, |B|\le k_*$。各个独立有效上界可取较小者。
本次有部分盒未证明异号；程序在这些盒中仍使用一般界和 (G.3)，
因此没有把全段异号作为一个未付的假设。

完整角格上分别取 (G.3) 的最大绝对值，记有效上界为
$A_i^*,B_i^*,C_i^*$。对实际对称形算子，行和界给
$$
\max_j|\kappa_j|\le\max(|A|,|C|)+|B|
\le\max(A_i^*,C_i^*)+B_i^*.
\tag{G.4}
$$
全579盒的最大值严格小于 $8.099018265867$。

## 3. 对真实物理标架作连续积分

设第 $i$ 盒长度 $h_i$，真实 $\sqrt E\le e_i^*$。
由 (G.1) 和正交性，累计
$$
T_X=\sum h_i e_i^*A_i^*,\qquad
T_Y=\sum h_i e_i^*B_i^*,\qquad
T_\nu=\sum h_i e_i^*\sqrt{(A_i^*)^2+(B_i^*)^2}
\tag{G.5}
$$
分别控制 $|X-e_z|,|Y-Y_0|,|\nu-\nu_0|$。
积分没有在文件边界或权函数节点重置。

水平位移可用更精确的逐盒积分。第 $i$ 盒左端已经有
$|X-e_z|\le T_{X,i}$，因此
$$
\int_i\!\sqrt E|X_h|dr
\le\min\{h_i e_i^*,
h_i e_i^*T_{X,i}+\tfrac12h_i^2(e_i^*)^2A_i^*\}.
\tag{G.6}
$$
右边第一项来自 $|X_h|\le1$，第二项来自 (G.1) 的完整局部积分。
令其累计上界为 $H$。所有闭盒的有效数值给

| 真实量 | 全段上界 |
|---|---:|
| $|F-F_0|$ | $0.228459724$ |
| $T_X$ | $0.415089553$ |
| $T_Y$ | $0.146588643$ |
| $T_\nu$ | $0.446073731$ |
| $H\ge|F_h-F_0|$ | $0.056233954$ |

水平法向不必支付整个 $T_\nu$。令
$\mathcal J(v_x,v_y)=(v_y,-v_x)$。对任意正交单位 $X,Y$，
$\nu=Y\times X$ 给准确恒等式
$$
|\nu_h-\mathcal JY_h|=1-X_z
=\tfrac12|X-e_z|^2.
\tag{G.7}
$$
例如水平旋转后写 $X=(\sin t,0,\cos t)$，
$Y=(\cos t\cos u,\sin u,-\sin t\cos u)$，两边直接相等。
由于 $\nu_0=\mathcal JY_0$，有
$$
|\nu_h-\nu_0|\le T_Y+\tfrac12T_X^2
<0.232738311,\qquad
X_z\ge1-\tfrac12T_X^2>0.91385033162.
\tag{G.8}
$$

## 4. 圆柱投影给整个环带的单射

[R128](R128-quantitative-embedding-of-the-exact-waist-annulus.md) 已给
同一原腰圈的严格支撑和半径界
$$
F_0\cdot\nu_0>\tfrac12,\qquad |F_0|<\tfrac{13}{10}.
\tag{G.9}
$$
于是整个环带满足
$$
\tfrac12-H<|F_h|<\tfrac{13}{10}+H,
$$
$$
\det_h(F_h,Y_h)\ge\tfrac12-H-\tfrac{13}{10}T_Y,
$$
$$
F_h\cdot\nu_h\ge\tfrac12-H-
\tfrac{13}{10}(T_Y+\tfrac12T_X^2).
\tag{G.10}
$$
完整有向计算的下界为
$$
|F_h|>0.44376604625,\quad
\det_h(F_h,Y_h)>0.25320081122,\quad
F_h\cdot\nu_h>0.14120624233.
$$

令 $\phi=\arg F_h$、$z=F_z$。用每盒真实 $a,\sqrt E$ 的下界和
整个 $|F_h|$ 的上界，准确恒等式给
$$
\phi_\theta=\frac{a\det_h(F_h,Y_h)}{|F_h|^2}
>0.14711768015,
$$
$$
J:=z_r\phi_\theta-z_\theta\phi_r
=\frac{\sqrt E\,a}{|F_h|^2}F_h\cdot\nu_h
>0.09095483284.
\tag{G.11}
$$
这些门对整个连续真实曲面成立。

原腰圈绕轴次数为1；非零水平半径的径向同伦保持次数。因此固定
任意 $r$ 时，$\theta\mapsto\phi$ 是一次定向圆微分同胚。
用 $(r,\phi)$ 作全局坐标后，链式法则给
$\partial_rz|_\phi=J/\phi_\theta>0$。若两点的三维像相等，它们
的柱角和高度相等，严格单调性先给相同 $r$，再给相同 $\theta$。
所以整个闭环带单射。紧性与已经证明的 $C^2$ 浸入完成嵌入证明，
包括正负半带的腰接缝。

## 5. 实际文件和范围

程序为 `scripts/fourfold_codazzi_positive_weight_sign_geometry.py`，
完整输出为
`notes/2026-11-13-R131-positive-weight-complete-r02-geometry-native.json.gz`。
报告保留每盒完整候选范围、真实误差范围、(G.3) 的实际范围、所用
系数界和连续标架积分，以及全部输入/依赖身份。四个几何门都通过；
全段异号旗标为 false 并原样保留，没有用它替代几何门。

```bash
python scripts/fourfold_codazzi_positive_weight_sign_geometry.py \
  --continuation notes/2026-11-13-R131-positive-weight-complete-r02-C0-native.json.gz \
  --out /tmp/complete-r02-positive-weight-geometry-new.json.gz
```

参数盒内的不同 $\eta$ 仍可能对应不同度量。本条不把它们叫作公共
度量弯曲族，也没有将带边环带的曲率界称为整闭面的 reach。
接下来的真实 body/帽/regular 匹配、全闭面可见振幅和非全等相位族
继续在各自完整接口上求证。
