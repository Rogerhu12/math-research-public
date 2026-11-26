# R150 附录：二重加单点 H 与非约化 rankV2 的本质六维截面为空

日期：2026-11-26（UTC）。作者：Astra-ISP-347c-20261126 / prior_results_map；AI-assisted GPT-6 Astra Pro。

**状态：已证明。** 原完整临界点若 rankH3 为 $2+1$ 物理支撑，rankV2 为二重 jet，则 $\dim\operatorname{ess}(T_3)\le5$。新内容关闭 H Gram 非退化的全部分支，与已登记的退化 Gram 排除合并。证明保留完整 mean、H 与最高梯度；全部新步骤为显示手证。

另外，在任何尚余的 $2+1$ H 本质六维反设中，V 必约化，且 $F\ne0$、$e=uKv\ne0$。

## 1. 原规范与已经支付的退化边界

沿用[二重加单点 H 的退化 Gram 全排除](R150-appendix-rank-three-double-plus-single-second-cumulant-degenerate-gram-essential-six-exclusion.md)的原规范：
$$
H=h(z_0z_1+z_1z_0)+\frac12w^2,\qquad h\ne0,
$$
$$
K_R=
\begin{pmatrix}0&0&g\\0&b&c\\g&c&0\end{pmatrix},
\qquad b=K(z_1,z_1),\quad g=K(z_0,w),\quad c=K(z_1,w).
\tag{1.1}
$$
其中 $z_0,z_1$ 为同一实际物理点的值与一阶 Taylor 列，w 为不同物理点的非零代表。退化分支 $bg=0$ 已全部排除，包括特殊源与无穷远。因此只需
$$
bg\ne0.
\tag{1.2}
$$
本质六维反设始终使 $(y,z_0,z_1,w,u,v)$ 为原整个六空间的基。

记 $p=Ky$、$F=yKy/2$、$\mathfrak b=p^{\mathsf T}Hp$。仍使用完整原恒等式
$$
(2HK-FI)Hp=0,\qquad F^2-2\mathfrak b+4hgc=0,
\tag{1.3}
$$
$$
F^3+12Fhgc-12h^2bg^2=8V^{\mathsf T}J_3V,
\tag{1.4}
$$
以及
$$
N=Fyy^{\mathsf T}-2FH
-2\bigl(y(Hp)^{\mathsf T}+(Hp)y^{\mathsf T}\bigr)
+4HKH+4V_p,
\quad k_x^{\mathsf T}Nk_x=0.
\tag{1.5}
$$
最高式为 $p(x)^3-6p(x)H(k_x,k_x)+4V(k_x,k_x,k_x)=0$。式 (1.4) 是原最高梯度、加权 Euler 及完整 Gaussian mean 的准确合并，不是删去 V 项的 Gaussian 方程。

## 2. 非退化 H 中 $F=0$ 全部排除，约化 V 的 $e=0$ 亦排除

$A=HK|_R$ 可逆，因为其行列式为 $h^2bg^2/2\ne0$。若 $F=0$，(1.3) 先迫 $Hp=0$，再迫 $c=0$。但 (1.4) 左边为 $-12h^2bg^2\ne0$，所以非约化 V 已不可能。

若 V 约化，规范 $V=(u^3+v^3)/2$，$e=uKv$，则 (1.4) 给 $e^3=-3h^2bg^2\ne0$。取保 V 的单位根尺度使 $p(u)=p(v)=e$。写 $C_i=K(z_i,u),D_i=K(z_i,v)$。原最高和 H 极线在 H 二重点值处给
$$
C_0^3+D_0^3=C_0^2+D_0^2=0,
$$
所以 $C_0=D_0=0$。但原 N 极线的一次 Taylor 系数此时准确为
$$
2N(Kz_0,Kz_1)=4hbg^2\ne0.
$$
这里 $F=Hp=0$，V 的一次贡献为 $4e(C_0C_1+D_0D_1)=0$，唯一留下的是原 $HKH$ 项。因此 $F=0$ 的约化情形也矛盾。

下面暂对 V 约化假设 $e=0$。此时 $p(u)=p(v)=0,V_p=0$。若 $Hp=0$，完整 N 在 $z_0$ 处就是 $-Fg^2\ne0$。若 $Hp\ne0$，从 (1.3) 直接得到
$$
p_0=gp_w/F,\quad
p_1=(2hbg/F^2+c/F)p_w,\quad
F^3=4hgcF+4h^2bg^2.
\tag{2.1}
$$
置 $t=hgc/F^2$，Gaussian 标量式进一步给
$$
(3-4t)\,\frac{p_w^2}{F^2}=1+4t.
\tag{2.2}
$$
另一方面，完整 N 在 $z_0$ 的值为 $-F(p_0^2+g^2)=0$，所以 $p_w^2/F^2=-1$。代入 (2.2) 给 $-3=1$，矛盾。故尚余约化情形也必须 $e\ne0$。这里没有除以可能为零的 $3-4t$。

## 3. 对非约化 V 的全部合法尺度

从此考虑目标非约化 V。由 §2，$F\ne0$。先作原加权非零尺度
$$
(y,H,V)\mapsto(\lambda y,\lambda^2H,\lambda^3V)
$$
使 $F=1$；平方根的两个选择都允许。再在 H 的实际 jet 中取
$$
z_0'=z_0/g,\qquad z_1'=hg\,z_1,\qquad w'=w.
$$
此可逆改变由局部参数和非零平凡化实现，而且
$z_0'z_1'+z_1'z_0'=h(z_0z_1+z_1z_0)$。
于是可完整规范
$$
\boxed{F=h=g=1,\quad
H=z_0z_1+z_1z_0+\frac12w^2,\quad b\ne0.}
\tag{3.1}
$$
仍用 b、c 记新基的原 Gram 项。此时
$$
A=
\begin{pmatrix}0&b&c\\0&0&1\\1/2&c/2&0\end{pmatrix},
\quad
\det(\lambda I-A)=\lambda^3-c\lambda-b/2.
\tag{3.2}
$$
非约化 V 的 $V^{\mathsf T}J_3V=0$ 使 (1.4) 成为
$$
1+12c-12b=0.
\tag{3.3}
$$

原非约化表示为
$$
V=\alpha u^3+\beta\operatorname{Sym}_{\Sigma}(u^2v),\quad\beta\ne0.
$$
完整 V mean 与最高系数给
$$
p(u)=0,\quad H(Ku,Ku)=H(Ku,Kv)=0,\quad
V_p=\beta\,p(v)u^2.
\tag{3.4}
$$
先以 $v\mapsto v+\alpha u/(3\beta)$ 消去 $\alpha$；因 $p(u)=0$，这不改变 $p(v)$。

在下面两种 Gaussian 分支中，完整 N 在 H 值处将分别给
$-1+4\beta p(v)C_0^2=0$ 或
$-3/2+4\beta p(v)C_0^2=0$。
所以 $\beta p(v)C_0\ne0$。取
$$
u'=a u,\qquad v'=v/p(v),\qquad a^2=2\beta p(v)
$$
即可同时规范
$$
\boxed{V=\frac12\operatorname{Sym}_{\Sigma}(u^2v),\qquad
p(v)=1,\qquad V_p=u^2/2.}
\tag{3.5}
$$
这是值尺度和一阶 jet 尺度的可逆改变，允许二者不同；对应的局部坐标斜率非零。两种平方根都被包含。

## 4. Gaussian 分支只有两个准确的常数 Gram

若 $Hp=0$，则 $p_0=p_1=p_w=0$，而 (1.3) 给 $c=-1/4$。再由 (3.3) 得
$$
\boxed{Hp=0:\qquad b=-\frac16,\qquad c=-\frac14.}
\tag{4.1}
$$

若 $Hp\ne0$，$1/2$ 是 A 的特征值，所以 (3.2) 给
$1-4c-4b=0$。与 (3.3) 联立得到
$$
b=\frac16,\qquad c=\frac1{12}.
$$
直接代入完整 (1.3)，准确有
$$
p_0=p_w=r,\qquad p_1=5r/12,\qquad r^2=1/2.
$$
因此
$$
\boxed{Hp\ne0:\qquad
b=\frac16,\quad c=\frac1{12},\quad
(p_0,p_1,p_w)=(r,5r/12,r),\quad r^2=\frac12.}
\tag{4.2}
$$
这里保留两个 r 符号，不作未经说明的实数选择。

在两行中，完整 N 在 H 值处的 Gaussian 部分分别为 $-1$、$-3/2$，从而确已付清 §3 对 $\beta p(v)C_0\ne0$ 的断言。

## 5. 同一组完整 H 值、一次系数与 V mean

令 $C_0=K(z_0,u),C_1=K(z_1,u),C_w=K(w,u)$。由 (3.5)，完整 N 在二重点值的常数项和一次项分别给下表前两列；由 (3.4) 的 $H(Ku,Ku)=0$ 得第三列：
$$
\begin{array}{c|c|c|c}
 &C_0^2&C_0C_1&C_w^2=-4C_0C_1\\ \hline
Hp=0&1/2&1/24&-1/6\\
Hp\ne0&3/4&-1/48&1/12
\end{array}
\tag{5.1}
$$
为使原项来源可核查，常数 H 式分别为
$-1+2C_0^2=0$、$-3/2+2C_0^2=0$。
一次 H 式除去共同非零 Taylor 因子 2 后，分别为
$$
-\frac1{12}+2C_0C_1=0,\qquad
\frac1{24}+2C_0C_1=0.
$$
第一行的 Gaussian 项来自 $-c+2b=-1/12$；
第二行来自 $-(p_0p_1+c)+2b=1/24$。
两个式子均含完整 $4HKH$，没有把 N 作为零矩阵。

(5.1) 也准确给
$$
C_1=C_0/12\quad(Hp=0),\qquad
C_1=-C_0/36\quad(Hp\ne0).
\tag{5.2}
$$

## 6. 完整 N 在 V 的物理值处给最终矛盾

原物理值 u 满足 $p(u)=0$、$H(Ku,Ku)=0$、$uKu=0$。因此完整 (1.5) 在 u 处所有项除 $HKH$ 外都准确为零，故
$$
(HKH)(Ku,Ku)=0.
\tag{6.1}
$$
在 (3.1) 的原基中，直接乘法给
$$
HKH=bz_0^2+\frac c2(z_0w+wz_0)
+\frac12(z_1w+wz_1),
$$
所以 (6.1) 正是
$$
bC_0^2+(cC_0+C_1)C_w=0.
\tag{6.2}
$$

若 $Hp=0$，(4.1)、(5.1)—(5.2) 将它变为
$$
-\frac1{12}-\frac16C_0C_w=0,
$$
故 $C_0C_w=-1/2$。但其平方又应为
$C_0^2C_w^2=(1/2)(-1/6)=-1/12$，不可能等于 $1/4$。

若 $Hp\ne0$，同一完整式变为
$$
\frac18+\frac1{18}C_0C_w=0,
$$
故 $C_0C_w=-9/4$。但其平方应为
$C_0^2C_w^2=(3/4)(1/12)=1/16$，不可能等于 $81/16$。
这是特征零中明确的 $80=0$ 矛盾，与 r 的两个符号无关。

## 7. 完整结论与准确余项

非退化 H Gram 中非约化 V 的两种 Gaussian 分支均空；$F=0$ 也已先独立排除。结合已登记的退化 Gram 全排除，得到
$$
\boxed{
\operatorname{rank}H=3,\ H\text{ 为 }2+1\text{ 物理支撑},
\quad \operatorname{rank}V=2,\ V\text{ 为二重 jet}
\quad\Longrightarrow\quad
\dim\operatorname{ess}(T_3)\le5.
}
$$
H 孤立点或 V 的源在无穷远不构成额外分支：本稿只用原物理代表与合法局部 jet，不曾除以这些点的仿射坐标。H 二重点的特殊源则在 $bg=0$ 的既有完整排除中已经支付。

尚余的 $2+1$ H 本质六维反设必须满足
$$
bg\ne0,\qquad F\ne0,\qquad
V=(u^3+v^3)/2,\qquad e=uKv\ne0.
$$
本稿不将这个约化剩余层、本质四五维或普通 ISP 宣称完成。

