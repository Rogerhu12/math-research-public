# R678：材料反射的两条固定母线排除 R673 的半径路镜合中点

2026-11-28。令 $g_+$ 是 [R673](R673-thick-bowed-tilted-endpoint-metric-with-strict-intrinsic-chord-slack.md) 的实际正端度量。端点环带关于 $xz$ 面反射对称，故材料对合 $S(r,\varphi)=(r,-\varphi)$ 是 $g_+$ 的等距。令 $A=\operatorname{diag}(1,-1,-1)$ 为绕 $x$ 轴转 $\pi$。对带外标准平圈的任一环带 $F$，操作 $F\mapsto A F\circ S$ 固定外圈材料标识；它把 R673 的准确正端环带换成准确负端环带，因此看似可用一半路径及镜合产生另一半。以下证明满足此操作固定条件的同 $g_+$ 中点根本不存在。结论只针对这个具体的时间拼接法。

假设 $F=A F\circ S$ 逐点且满足相同的内、外 $C^1$ 真平圈接合。材料 $\varphi=0,\pi$ 是 $S$ 固定的两条整母线，故它们的全部像都在 $A$ 的固定集合，即 $x$ 直线上。因为 $F$ 为浸入，$F_r$ 在每条线上连续且非零，故有符号单调。外圈准确的径向切向在 $\varphi=0$ 为 $+e_x$，在 $\varphi=\pi$ 为 $-e_x$。内圈实际中心 $C$ 为这两端点的中点，故 $C=d e_x$；内刚姿 $Q$ 满足 $Q e_x$ 平行于 $e_x$。两阶刚接的一阶径向迹以及上面的单调取向强制 $Qe_x=+e_x$，反向姿态不能用于延长直线。于是这两条材料经线的真实长度分别为
$$
 b-a-d,\qquad b-a+d .
$$
两者为正且总和准确 $2(b-a)$，不需预设 $d=0$ 或提前界定 $|d|$。

另一方面，在定义同一 $g_+$ 的 R673 正端，内外同名两对刚圈材料端点的欧氏距离各为
$$
 L=\sqrt{(b-a)^2+2ab(1-\cos\vartheta)}>b-a .
$$
中央弓在两个接圈为零且内心无平移，故该式直接使用真实端姿。两条给定材料经线的 $g_+$ 长各至少 $L$，与中点所迫的长度总和矛盾。因而即使在中点允许自由平移及其他兼容刚姿，$F=A F\circ S$ 亦不可能。将中点的参考竖直场选为 $H\sin(2\varphi)$ 虽可符合此对称，其固定位母线仍是直线，不能补上同度量长度。本稿不排除不采用此对合的完整 $t$ 路径；[R671](R671-saturated-material-meridian-and-discrete-twist-of-the-exact-endpoint-metric.md) 对旧度量的扭转锁定也是不同机制。

后来的 [R679](R679-elliptic-sign-separates-material-reflections-of-any-nonplanar-flat-rim-annulus.md) 已用椭圆点符号排除同一反射端对的任何精确连续路径；本文保留其更具体的固定母线与长度机制。
