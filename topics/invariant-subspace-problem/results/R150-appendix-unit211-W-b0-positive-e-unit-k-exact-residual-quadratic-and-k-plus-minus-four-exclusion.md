# R150 补充：W/b0 正 e 单位 k 图的准确二次剩余式及 k 等于正负四中心排除

日期：2026-11-29（Asia/Taipei）。会话 Astra-ISP-8542378f-20261127。

## 1. 结论与当前范围

在当前剩余特征 $1009$ 的 W/b0 赋值分析中，设
$$
v(e)=a>0,\quad v(k)=0,\quad \zeta=\bar k\ne-2.
$$
[原 lambda 限制](R150-appendix-unit211-W-b0-positive-e-ray-original-lambda-valuation-and-two-pole-centers.md)
与[正四中心完整极点排除](R150-appendix-unit211-W-b0-positive-e-k-four-pole-complete-original-tangent-cone-exclusion.md)
已经证明这里 $\lambda$ 必为单位。本稿在这个已付范围内给出完整准确的 q2 剩余二次式，并排除：

1. $\zeta=4$ 的全部剩余点；
2. $\zeta=-4$ 的全部剩余点，包括 $M$ 及 $\Phi$ 的任意更深首项相消。

这两项不由旧初始理想的必要 gcd 次数推出，也没有重跑已完成的六射线初始理想门。全文为原式纸面推理；没有新数学运行。

## 2. 一般单位图的完整 q2 剩余式

设
$$
L=\bar\ell=\frac{\zeta+2}{\zeta},\qquad
h=3-2L,\qquad \mu=2\bar\lambda-3.
\tag{1}
$$
由于 $\zeta\ne0,-2$，$L\ne0,1$。又 $\lambda$ 单位，故 $\mu$ 整且 $\mu+3\ne0$。

完整原定义给出
$$
u,\delta\to1,\quad m\to1-L,\quad M\to2L-1,
$$
$$
J/Q\to1,\quad A_*/Q\to3,\quad
C_*/Q\to G:=4L^2-6L+3,\quad T\to L\mu/3.
\tag{2}
$$
其中 $2L-1$、$G$ 可以为零，(2) 不倒这些首项。

由完整原
$$
q_2=2A_2C_*+2M\ell Q(3-4\lambda)-8uQ\delta\ell T^2
$$
除以 $Q$，得到准确必要式
$$
G(\mu^2+4\mu+5)-2L(2L-1)(2\mu+3)
       -\frac89L^3\mu^2=0.
\tag{3}
$$
其二次、一次和常数系数分别是
$$
G-\frac89L^3=\frac{(3-2L)^3}{9},
$$
$$
4G-4L(2L-1)=-4(3-2L)(L-1),
$$
$$
5G-6L(2L-1)=2(3-2L)^2-3.
$$
因此完整剩余关系为
$$
\boxed{\frac{h^3}{9}\mu^2-4h(L-1)\mu+2h^2-3=0.}
\tag{4}
$$
它保留所有低次项；没有把最高项单独当作原方程。

若 $h=0$，(4) 给 $-3=0$，不可能。由 (1)，这准确对应 $L=3/2$、$\zeta=4$。与已经关闭的 lambda 极点支合并，整个正四中心关闭。

对其余点，$h$ 因 (4) 已证非零。若需使用新残余坐标 $y=h\mu$，同一点关系准确等价于
$$
h y^2+18(h-1)y+18h^2-27=0.
\tag{5}
$$
(5) 只是新的精确参数关系，不是额外的排空结论，也没有把未付系数倒掉。

## 3. 负四中心的完整深 M 排除

现取 $\zeta=-4$，故 $L=1/2$、$h=2$。原 (4) 化为
$$
q(\mu):=8\mu^2+36\mu+45=0.
\tag{6}
$$
特别 $\mu\ne-3$，也可直接由 $q(-3)=9\ne0$ 看出。由 (3) 或 (6)，
$$
A_2=\frac{\mu^2+4\mu+5}{2}=\frac{\mu^2}{18}.
\tag{7}
$$

这里 $M$ 的剩余为零，但原物理 $M$ 非零。令 $\gamma=v(M)>0$；允许任意更深的相消。原 q2 的完整恒等式始终是
$$
D=MS,\qquad
S=\frac{A_*A_2-\ell Q(3-4\lambda)}{4uQ\delta\ell}.
\tag{8}
$$
用 (2)、(7) 取剩余：
$$
\bar S=\frac{3A_2+L(2\mu+3)}{4L}
       =\frac{(\mu+3)^2}{12}\ne0.
\tag{9}
$$
因此 $v(D)=\gamma$，不是只知道 $D$ 的第一项为零。

另一方面，由原
$$
K=\ell^2B_3-3\ell A_2T+2T^3,\qquad
B_3=(\mu^3+6\mu^2+12\mu+7)/2
$$
及 $T\to\mu/6$，在 (6) 上
$$
\bar K=\frac{13\mu^3}{108}+\frac{3\mu^2}{4}
             +\frac{3\mu}{2}+\frac78
       =-\frac{22\mu+57}{192}.
\tag{10}
$$
这一普通多项式余式的完整身份为
$$
\frac{13\mu^3}{108}+\frac{3\mu^2}{4}
+\frac{3\mu}{2}+\frac78
=
\frac{26\mu+45}{1728}\,q(\mu)-\frac{22\mu+57}{192}.
$$
若 $\bar K=0$，则 $\mu=-57/22$，但
$$
q(-57/22)=\frac{657}{121}\ne0
\quad\text{于特征 }1009.
$$
故 $K$ 为单位。又 $m\to1/2$，也是单位，所以完整原 R6
$$
MK^2-4m^2D^3=0
$$
的两项估值分别是 $\gamma$ 和 $3\gamma$，严格不同。这排除所有 $\gamma>0$，包括与原 $\Phi$ 的任意共同深相消。证明没有倒 $M$、$\Phi$ 或 $D$ 的剩余，也不需要选择 $K$ 之外的新一般开图。

## 4. 与其余边界的准确合并

本稿只关闭正 e、单位 k 图中的两个指定中心。现有状态为：

- 五条其他候选无穷射线已经分别完成原排除；
- 正 e、$\bar k\ne-2$ 必须 lambda 单位，并且现在 $\bar k\ne4,-4$；
- 正 e、$\bar k=-2$ 的正 ell 及[整个 ell 极点](R150-appendix-unit211-W-b0-positive-e-k-minus-two-entire-ell-pole-original-exclusion.md)已关闭，ell 单位图继续；
- 一般剩余 k、内部权图及原已付分母的 DVR 边界仍须完成。

完整 q2、R6、D=MS 来源与本稿相同：原定义源 blob **47281af16fdd0ad7500ecda377c3cb9f9d65e725**。本稿未执行旧源或旧六射线源，不从旧 degree 54 必要 gcd 推断根，不把纸面边界结论改称整个 W 空性。普通 ISP 尚未完成。
