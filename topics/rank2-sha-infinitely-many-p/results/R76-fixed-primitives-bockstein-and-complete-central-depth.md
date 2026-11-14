# R76：固定原函数的实际 Bockstein 与完整中央深度

日期：2026-11-12。状态：下列转译与非 D-finite 结论已证明；跨素数非零仍未证明。
完整证明见[固定原函数与完整深度](../notes/2026-11-12-fixed-primitive-bockstein-and-complete-depth.md)。

沿用 R66/R75 的同一固定全权一系列

$$
\mathcal B_1(u)=\sum_{4\mid m}C_mu^m,
\qquad C_m=\frac{h_m^2}{24\,17^{m-4}m!},
\qquad h_m=m![z^m]A_1\in\mathbb Z.
$$

定义不随素数变化的

$$
\mathcal H_i=\sum\frac{C_m}{m-1}u^{m-1},\qquad
\mathcal H_o=\sum\frac{C_m}{(m+1)^2}u^{m+1},\qquad
\mathcal H=\mathcal H_i+\mathcal H_o.
$$

## 1. 实际有限 jet 复形及其规范

在 $\mathcal A_p=u\mathbb Z_p[u]/(u^{p+1})$ 上令 $\mathscr E=u\partial_u$。
两个复形 $[\mathcal A_p\xrightarrow{\mathscr E}\mathcal A_p]$ 与
$[\mathcal A_p\xrightarrow{\mathscr E^2}\mathcal A_p]$ 的零次上同调为零，
一次上同调分别为 $(\mathbb Z/p)u^p$、$(\mathbb Z/p^2)u^p$。
第一复形的第一 Bockstein 为恒等；第二复形第一 Bockstein 为零、第二为恒等。

实际输入为 $\mathcal B_1/u$ 与 $u\mathcal B_1$，原有整除使其上同调类为零。
特征零方程固定的除后坐标准确为

$$
\Gamma_{i,p}=[u^p]\mathcal H_i=C_{p+1}/p,
\qquad \Gamma_{o,p}=[u^p]\mathcal H_o=C_{p-1}/p^2.
$$

二者都是实际平方乘单位，正赋值至少为二。
真实 Frobenius 坐标 $u_F=V_p/U_p$ 满足 $u_F-u=O(t^p)$；
因原函数分别始于三次、五次，以上两个 $p$ 次系数在坐标替换后特征零完全相等。
这只使用指定有限 jet，没有把整个坐标变换误当整可逆换基。

## 2. 同一固定对象中的完整导数条件

普通 $p\ge13,p\ne17$ 时，R56 与阶乘赋值给

$$
J'_{o,p}(0)=0\iff
\begin{cases}
v_p([u^p]\mathcal H_o)\ge2,\\
v_p([u^{(p-1)p^n+1}]\mathcal H_o)\ge4n+5-p^n&\text{所有 }n\ge1.
\end{cases}
$$

惰性 $p\ge7$ 时，R62 同样给

$$
J'_{i,p}(0)=0\iff
v_p([u^{(p+1)p^n-1}]\mathcal H_i)\ge4n+2-p^n
\quad\text{所有 }n\ge1.
$$

[R77](R77-iterated-frobenius-and-short-input-complete-inert-certificate.md)
进一步用实际半因子的模 $p^2$ 展开将后一逐层界加强为 $4n+4-p^n$；
两组条件在对所有 $n$ 量化后均与完整导数为零等价。
普通导数非零与初级有限等价；惰性导数非零目前仅证明充分性。

若导数非零、赋值分别为 $j_o,j_i$，充分大 $n$ 的上述系数赋值准确为
$2n+3+2j_o-p^n$、$2n+2j_i-p^n$。
因此完整中央消失控制的是指定稀疏指标的额外深度，不能直接解释为整条级数整性或半径改善。

## 3. 一个固定原函数同时包含两类素数

$\mathcal H_i$ 只含模四为三的次数，$\mathcal H_o$ 只含模四为一的次数。
故两个首层及全部完整深度条件都可统一写成 $\mathcal H$ 的系数，无交叉项。

这个和本身也非 D-finite：在实际周期 torsor 上

$$
\delta(sKL\mathcal H')
=-\frac{M_1K}{sL^2}
 +\frac{M_1'K^2+M_1K K'}L+\frac{M_1}{sK}.
$$

不同 cusp monodromy 分支沿不同 $L_n=0$ 有不能被简单极项消去的双极点，
故分支线性独立。D-finite 的乘积与导数封闭性排除 $\mathcal H$ 为 D-finite。
这没有排除指定对角的其他有限几何比较。

**剩余任务：** 在这个实际固定偏连接中，证明无穷多个素数至少违反一个完整深度条件。
