# R150：H198 补图完整十五行二列表示与两条本原物理 λ 六次原约束

会话：Astra-ISP-8542378f-20261127。日期：2026-11-28（Asia/Taipei）。

## 1. 新结论与准确范围

在 [N1 斜率与 H198 定理](R150-appendix-unit211-W-N1-H198-weight-curve-and-two-generator-monic-square.md) 的当前 W 原权域内，只对明确的 H198 非零补图再作局部化。令 $A=A_W$ 是仅倒置已付权量的环，

$$
R_H=A[H198^{-1}][\lambda],\qquad
I_6=(E_1,E_{Be},E_{Bo},N_1,N_S,P_S).
\tag{1}
$$

本次已经得到：

- 同一完整六式商的精确十五行、二列 $R_H$ 模表示；全部 NS/PS 与它们的四个同点乘积均保留；
- 两条实际原理想标量 $C_N,C_{NP}\in I_6R_H[x,y]$，对物理 $\lambda$ 均恰为六次，完整 $\lambda$ 内容均为非零 QQ 常数；
- 所有基变换系数身份、图内清分母、两对真实 cofactor 乘子除法及最终两列乘回均已完成。

两条式的 $\lambda$ 首项尚未支付，不称其首一。整个 H198=0 仍开放；本结果也没有排除补图上的全部原点。这里的 I6 是完整原均值与加权 NS/PS，个别原值 N/P 条件仍须继续同点施加。

唯一首次 Actions 为 run 46087811145、job 140801426764，内层真实 exit 0；source 14.028170757 秒，driver 14.074930164 秒，峰值 RSS 93644 KiB。

## 2. 原十五行表示与 N1 的权坐标

[全域十五行精确原关系](R150-appendix-unit211-W-global-three-generators-exact-fifteen-original-relations.md) 已从三条真实原均值规则证明

$$
A[\lambda,x,y]/I_6\simeq A[\lambda]^3/\mathcal N.
\tag{2}
$$

$\mathcal N$ 由五行 $C_1,C_2,r_N,r_S,r_P$ 及各自右乘 $M_x,M_y$ 的十五行生成；$C_1,C_2$ 为实际乘法交换子非零行。该表示已经证明稳定性及双侧循环模同构，不要求三个原生成元自由。

同一 N1 原迹给

$$
n=p_0+p_1x+p_2y=\nu F_6,\quad
p_1=a\lambda+b,\quad p_2=c\lambda+d,\quad
z=ax+cy,\quad \Delta_N=ad-bc.
\tag{3}
$$

这里四个 $a,b,c,d$ 是斜率系数，不是物理权。$n-N_1$ 属三条均值理想；$\deg_\lambda(p_0,p_1,p_2)\le(2,1,1)$。此前完整 QQ 因式已经证明 $\Delta_N$ 除已付权量外恰含不可约 H198；本次没有重跑该因式门。

在 (1) 上，以下坐标矩阵可逆：

$$
\begin{pmatrix}1\\z\\n\end{pmatrix}
=
J\begin{pmatrix}1\\x\\y\end{pmatrix},\quad
J=\begin{pmatrix}1&0&0\\0&a&c\\p_0&p_1&p_2\end{pmatrix},
\quad \det J=ap_2-cp_1=\Delta_N.
\tag{4}
$$

仅 $\Delta_N$ 的纯权逆用于此次转换；没有引入 $\lambda$、物理 D 或任何范数逆。

## 3. 完整十五条关系的二列身份

对任意原关系行 $r=(r_0,r_1,r_2)$，置

$$
s_0=r_0+\frac{(cr_1-ar_2)p_0}{\Delta_N},\qquad
s_1=\frac{p_2r_1-p_1r_2}{\Delta_N},\qquad
\kappa=\frac{-cr_1+ar_2}{\Delta_N}.
\tag{5}
$$

实际逐条返回

$$
s_0+\kappa p_0=r_0,\qquad
as_1+\kappa p_1=r_1,\qquad
cs_1+\kappa p_2=r_2.
\tag{6}
$$

所以 $r(1,x,y)^T=s_0+s_1z+\kappa n$。若原完整来源是 $r(1,x,y)^T=\tau_rF_6$，则

$$
s_0+s_1z=(\tau_r-\kappa\nu)F_6.
\tag{7}
$$

原 N1 行是 $n$ 的图内权单位倍数，故换基后的关系模包含第三标准坐标 $(0,0,1)$。删去这个已经由原关系杀掉的坐标，得到完整同构

$$
\boxed{
R_H[x,y]/I_6\simeq R_H^2/
\left\langle(s_0(r),s_1(r)):r\in\mathcal R_{15}\right\rangle .
}
\tag{8}
$$

$\mathcal R_{15}$ 保留 $C_1,C_2,r_N,r_S,r_P$ 的全部一次 $M_x,M_y$ 闭包。实际原三列中十五行均非零，换基后 N1 行恰变零；其余十四个形式关系全部保留，其中包括 N1 的两个同点乘积和 NS/PS 的四个同点乘积。

本次先实际返回旧十一行及新增四行的完整原六式迹，再核 (6) 三个系数乘积，并只用图内权单位清二列分母/内容。最终来源按 (7) 的精确组合 DAG 给出；没有声称又展开保存所有巨大六变量乘子。式 (6) 与已返回的 $\tau_r,\nu$ 已严格推出 (7)。

同一坐标已有首一 $z^2+\beta_1(\lambda)z+\beta_0(\lambda)$。其明确二次环境自由二维，而 (8) 是再施加全部原关系的商，不能据此称原商自由，也不能无条件把几何局部化后的商称为全权有限自由。

## 4. 两对原行及真正的 cofactor 内容取消

固定两对二列多项式行：

$$
(A_N,B_N)=(N1*x,N1*y),\qquad
(A_{NP},B_{NP})=(N_S,P_S).
\tag{9}
$$

所有归一只用 (1) 的权单位。对一对 $A=(A_0,A_1)$、$B=(B_0,B_1)$，取

$$
\omega=(B_1,-A_1),\qquad h=\gcd(B_1,-A_1).
$$

此次两对的实际 $h$ 恰为同一定义：双次数 $(8,12)$、总次数 16、69 项；其参数定义 SHA-256 为

0c675b3d0f732e60114a3a1bab0807f59d525e0df253fe0a800e62a56a27270b。

源将这两个实际乘子分别作多项式整除，并返回

$$
\frac{\omega}{h}
\begin{pmatrix}A_0&A_1\\B_0&B_1\end{pmatrix}
=(C^*,0),\qquad
hC^*=A_0B_1-A_1B_0.
\tag{10}
$$

所以 $C^*$ 本身具有原 I6 来源。式 (10) 在整个 $h=0$ 纤维上仍有效；这没有把原方程除以未付因子。随后剥去真正已付权因子及本节明确的 H198 补图因子，得到 $C_N,C_{NP}$。最后两个坐标的乘回再次实际核出，而非仅由 determinant 的数值判断作结论。

## 5. 实际两条本原六次式

| 原行对 | $(\deg_e,\deg_k,\deg_\lambda)$ | 总次数 | 项数 | 定义字节数 |
|---|---:|---:|---:|---:|
| N1*x、N1*y | $(30,40,6)$ | 58 | 5548 | 218781 |
| NS、PS | $(42,54,6)$ | 78 | 10570 | 484978 |

两条准确源定义的 SHA-256：

- $C_N$：a3ebccf7766f472aa6b0e80aee115aed541d5d09d4c89e619016c8507c16c1a9。
- $C_{NP}$：6d76f7db1dd1d311fb320fae4e14aeb3641e74ccbe30a1370d1da80ce70f1038。

在所有七个 $\lambda$ 系数上完成真正完整 gcd，结果均为非零 QQ 常数。故两条均对 $\lambda$ 本原，没有另一个未付的整权内容零支。这一事实不支付其最高 $\lambda$ 系数；所有首项零、两条式的全部同根以及 H198=0 仍须保留。

此处没有运行两条六次式的结果式或 gcd，也没有重新运行旧十二阶 Sylvester、旧六维 Norm 或十八行 module。两条新原组合可直接作为后继输入；它们本身不证明任何两参数理想为空。

## 6. 实际来源、资源和规则读取

唯一源：

[2026-11-28-unit211-W-H198-complement-exact-fifteen-two-columns-fixed-pairs-8542.py](../notes/2026-11-28-unit211-W-H198-complement-exact-fifteen-two-columns-fixed-pairs-8542.py)

源 blob 为 ecf383adc2b84179c1cad2cd9080f516719b4333；11739 字节，SHA-256 为 fda30f304600080de4b07193b1e1e378f3794b782174d331ab5b076fc2bc742d。固定 180 秒、4 GiB；此次实际全部完成。源只取 N1 坐标必要前缀、同 namespace 的十一行定义，并加入真正新的四个 NS/PS 同点乘积与基变换，不运行旧计算尾段。

source commit 为 50ee536d1e9cdac9a4760e8a853033eb9a342db8。2026-11-28 00:25:57.422877 UTC 真实 pull 到 70b78e5c3733fd3eb7ef0bb1ac1b836146a4f149，两 README 的 blob 仍分别为 282e86b03385d3b6245ce7100ae2e2af7b103c2d、5fbd905291dd044c88d35bd9c07ac0e586ff795a，差异为空。

stdout 为 17625 字节，SHA-256 为 04dac2de0fa913719f9fe0bb73b72f06a9ea013a254be6e012b3022b03a85c4a。只保存源码、参数定义及小回执；上表的大系数没有保存、分片或编码传送。附 [实际回执](../notes/2026-11-28-unit211-W-H198-complement-exact-fifteen-two-columns-fixed-pairs-receipt-8542.json)。

整个 H198 原权支、补图的原个别值返回及普通无限维 ISP 均未由本结论完成。
