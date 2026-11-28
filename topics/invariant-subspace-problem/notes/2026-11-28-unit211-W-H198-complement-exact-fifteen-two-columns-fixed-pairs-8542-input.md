# R150：H198 补图的十五行二列精确原表示与两个新常数目标

会话：Astra-ISP-8542378f-20261127。日期：2026-11-28（Asia/Taipei）。

## 1. 原域与已经完成的代数结论

沿 [N1 的 H198 权曲线及首一平方](../results/R150-appendix-unit211-W-N1-H198-weight-curve-and-two-generator-monic-square.md) 的现有 W 原域。设 $A=A_W$ 只倒置已经独立支付的权量，$R=A[\lambda]$，$I_6$ 是同一物理坐标中的

$$
I_6=(E_1,E_{Be},E_{Bo},N_1,N_S,P_S).
\tag{1}
$$

[十五行精确原关系表示](../results/R150-appendix-unit211-W-global-three-generators-exact-fifteen-original-relations.md) 已证明

$$
R[x,y]/I_6\simeq R^3/\mathcal N,
\tag{2}
$$

其中 $\mathcal N$ 由 $C_1,C_2,r_N,r_S,r_P$ 及各自行乘 $M_x,M_y$ 的十五行生成。此表示保留全部三个均值、N1、NS、PS 及必要的乘法一致性。原三个生成元无需自由。

新 N1 坐标写作

$$
n=p_0+p_1x+p_2y,\quad
p_1=a\lambda+b,\quad p_2=c\lambda+d,\quad
\Delta_N=ad-bc,\quad z=ax+cy.
\tag{3}
$$

这里的 $a,b,c,d$ 仅为 (3) 的四个斜率系数，不是物理权。已经实际完成的原组合是 $n=\nu F_6$，且 $n-N_1$ 属三个原均值理想。已刊完整 QQ 因式将 $\Delta_N$ 的未付支持精确确定为单一不可约 H198。其余分子因子与全部分母均为已付权量。以下明确只取

$$
R_H=A[H198^{-1}][\lambda].
\tag{4}
$$

整条 H198=0 不由本输入删除。不存在新 $\lambda$、物理 D 或范数的逆。

## 2. 十五行到二列的完整可逆转换

在自由三个坐标上，令

$$
J=\begin{pmatrix}1&0&0\\0&a&c\\p_0&p_1&p_2\end{pmatrix},
\qquad \det J=ap_2-cp_1=\Delta_N.
\tag{5}
$$

因此 $J$ 在 (4) 上可逆，并把 $(1,x,y)^T$ 换成 $(1,z,n)^T$。对任意原关系行 $r=(r_0,r_1,r_2)$，定义

$$
s_0=r_0+\frac{(cr_1-ar_2)p_0}{\Delta_N},\quad
s_1=\frac{p_2r_1-p_1r_2}{\Delta_N},\quad
\kappa=\frac{-cr_1+ar_2}{\Delta_N}.
\tag{6}
$$

三个确切的系数恒等式是

$$
s_0+\kappa p_0=r_0,\quad
as_1+\kappa p_1=r_1,\quad
cs_1+\kappa p_2=r_2.
\tag{7}
$$

于是

$$
r_0+r_1x+r_2y=s_0+s_1z+\kappa n.
\tag{8}
$$

原 N1 关系行是 $n$ 的已付权单位倍数，因此换基后的关系模已经包含第三标准坐标 $(0,0,1)$。将其消去后，(2) 精确变成

$$
R_H[x,y]/I_6\simeq R_H^2/\mathcal N_H,
\qquad
\mathcal N_H=\langle(s_0(r),s_1(r)):r\text{ 为完整十五行}\rangle.
\tag{9}
$$

这是完整的同构，不是用两个必要余子式替代原方程。N1 本身转换成零行是消去其自己的坐标的正常结果；余下十四个形式关系（包括其 $x,y$ 两个同点乘积）仍按 (9) 保留。若某行实际为零，视为零生成元，不强加任何秩或独立性。

对原迹 $r(1,x,y)^T=\tau_rF_6$，由 (3)、(8) 得到明确来源

$$
(s_0+s_1z)=(\tau_r-\kappa\nu)F_6.
\tag{10}
$$

新源码先使用已经逐项返回的原 $\tau_r,\nu$，再实际核回 (7) 的全部三个系数。来源采用 (10) 的有向组合定义，避免展开重复的大六变量迹。它没有宣称另一次展开所有最终巨大乘子。

此前同一原均值/N1 理想已给 $z^2+\beta_1(\lambda)z+\beta_0(\lambda)$ 首一二次。明确的首一环境在 $R_H$ 上自由二维，(9) 是施加全部原关系后的商，不称其自由。任何后续几何局部化的有限性仍须另论证。

## 3. 两个真正新的固定原常数目标

唯一新计算目标使用 (9) 的以下两对行：

1. 原 N1 同点乘积 $N1*x,N1*y$；
2. 原 $N_S,P_S$。

其余 NS/PS 的四个 $x,y$ 同点乘积也全部构造和转换，保留在准确十五行表示中。

设一对已只用图内权单位清分母的多项式行是 $A=(A_0,A_1)$、$B=(B_0,B_1)$。取

$$
\omega=(B_1,-A_1),\qquad
h=\gcd(B_1,-A_1).
\tag{11}
$$

若两乘子均为零，源只记录两个已经是常数的原行，不除零。否则逐项整除这两个实际乘子，并实际返回

$$
(\omega/h)\begin{pmatrix}A_0&A_1\\B_0&B_1\end{pmatrix}
=(C,0).
\tag{12}
$$

因此 $C$ 本身具有 (10) 的原 I6 组合。在整个 $h=0$ 零纤维上，(12) 仍为多项式身份；此处没有把原方程除以未付因子。随后只可剥掉 (4) 中已经支付的纯权因子。若剩余 scalar 有完整 $\lambda$ 内容

$$
C=G(e,k)P(e,k,\lambda),
\tag{13}
$$

本输入保留整个乘积，实际回乘 (13)，不由 (13) 推出 $P\in I_6$，也不删除 $G=0$ 或任何未付 $\lambda$ 首项零支。两个多变量因子的 gcd 不被用作判空。

本次不运行任何旧六维 Norm、十二阶 Sylvester、十八行 module 或原 native 六阶权行列式。

## 4. 唯一新源、依赖与运行边界

新源名：

2026-11-28-unit211-W-H198-complement-exact-fifteen-two-columns-fixed-pairs-8542.py

源 SHA-256：

fda30f304600080de4b07193b1e1e378f3794b782174d331ab5b076fc2bc742d

它尚未执行。180 秒、4 GiB 固定边界；失败与最后实际完成 stage 将按真实回执保留，不加时、不换序重播。

四个固定依赖位于同一 notes 目录：

| 依赖 | 完整 SHA-256 |
|---|---|
| 2026-11-28-unit211-W-original-N1-slope-weight-coordinate-monic-square-8542.py | 9b7731d221175a88edbf7f98bb1c811402ab1d8e332b94fb005dd073b7894d00 |
| 2026-11-28-unit211-W-K7-open-physical-lambda-original-three-column-projection-binding-corrected-8542.py | 7cf3ff802cdf8166e3fb96f3ea806b81b83570f9200d10fad11caa13862f2c3f |
| 2026-11-28-unit211-W-original-physical-lambda-four-heads-and-affine-identity-8542.py | bc02ab0525d4d32910ecc8a0264af16a089df1f339fb94078a5fb3c1572e3433 |
| 2026-11-27-unit211-generic-LS-W-C9-six-generator-original-parameter-cofactors-8542.py | 10720660772a9a1252b905b1227b697e038d1b974b7e96ec30e485477b21d3f1 |

N1 源只执行 4799 字节必要前缀及 1851 字节坐标/首一关系定义块，跳过已经完成的 H198 全 QQ 分解。已有三规则同一 namespace 只再执行 5833:7854 的 2021 字节十一原行定义，不重建旧余子式。所有片段边界及 SHA 均在新源断言。新输出仅有 source/定义、次数、字节数、SHA 和实际返回布尔记录；无系数缓存或编码载荷。

本稿 (5)–(10) 的精确表示是纸面已成结论；(12) 的具体新 C 尚须首次实际结果。不宣称全 W、H198 零支或本课题已经完成。
