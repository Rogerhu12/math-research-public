# R244 后续附录：广义预解单位类与真空的有限自然词域

日期：2026-11-13（UTC）。作者：normal_resume_1cf / Astra-ISP-1cf8c51d。
状态：完整证明的中间结论。本文承接 [预解图与正真空锚](R244-appendix-empty-resolvent-and-common-graph-vacuum-defect.md)，把有限秩结论从普通标量预解点扩到任意有界交换扰动及交换单位倍数。共同代数主理想、实际值域及共同图闭像都不随这些选择改变。本文还给出真空原像与一组有限自然词域的准确等价；没有证明该域条件总成立。

## 1. 固定的原最小图

记 $\mathfrak C=A'$，$B(x,y)=\langle x,Cy\rangle$。
取
$$
\rho=\sum_{i=1}^r f_i\otimes f_i\ge0,\qquad
\tau=\sum_i\|f_i\|^2>0,\qquad
M_i=X_{Cf_i}.
$$
每个 $M_i$ 是原有限 Walsh 核的最小闭乘子，$M_i1=Cf_i$。
[前附录](R244-appendix-empty-resolvent-and-common-graph-vacuum-defect.md) 已证明
$$
F\operatorname{Dom}M_i\subseteq\operatorname{Dom}M_i,\qquad
M_iF=FM_i\quad(F\in\mathfrak C)
\tag{1.1}
$$
及原 $C$ 对称性；不预设各最小图已经最大。

定义共同最小图
$$
\Gamma=\overline{\{(u,M_1u,\ldots,M_ru):u\text{ 为有限 Walsh 列}\}}
\subset H^{r+1}.
\tag{1.2}
$$
它等价于共同多项式列的闭包，故每个 $F^{(r+1)}$、$F\in\mathfrak C$ 都保持 $\Gamma$。这个共同闭包不被换成各个最大定义域的交。

固定全空间单射 $S\in\mathfrak C$，假设
$$
\phi_\rho(SF)=0\qquad(F\in\mathcal A).
\tag{1.3}
$$
R88 和正常性将其延拓到全部 $F\in\mathfrak C$。

## 2. 允许的广义预解式与有界恒等式

对每个 $i$，假设可以找到
$$
U_i\in\mathfrak C\text{ 为有界单位},\quad
F_i\in\mathfrak C,\quad
\lambda_i\in\rho(L_i),\qquad
L_i=M_iU_i+F_i.
\tag{2.1}
$$
$U_i^{-1}$ 也属于 $\mathfrak C$。
由 (1.1)，$U_i$ 及其逆都保持 $\operatorname{Dom}M_i$，故
$$
\operatorname{Dom}L_i=\operatorname{Dom}M_i,\qquad
M_iU_i=U_iM_i
$$
于这个域成立。$L_i$ 是闭算子，且完整交换 $A$。

置
$$
R_i=(L_i-\lambda_iI)^{-1},\qquad B_i=F_i-\lambda_iI.
$$
逆的唯一性给 $R_i\in\mathfrak C$。
它单射，且
$$
R_iH=\operatorname{Dom}M_i
$$
稠密。由 $(M_iU_i+B_i)R_i=I$ 得
$$
\boxed{
D_i:=M_iR_i
=U_i^{-1}(I-B_iR_i)\in\mathfrak C,
\qquad
U_iD_i+B_iR_i=I.
}
\tag{2.2}
$$
这是实际有界算子恒等式，不是在未经定义的无界域上形式清分母。

它还准确识别最大商域：
$$
\boxed{
M_i=R_i^{-1}D_i,\qquad
\operatorname{Dom}M_i
=\{x:D_ix\in\operatorname{Ran}R_i\}.
}
\tag{2.3}
$$
一向由 $D_ix=R_iM_ix$ 在 $\operatorname{Dom}M_i$ 上成立。
反向若 $D_ix=R_iy$，则 (2.2) 给
$$
x=U_iD_ix+B_iR_ix
=R_i(U_iy+B_ix)\in R_iH=\operatorname{Dom}M_i.
$$
随后由 $R_i$ 单射得到商作用等于 $M_i$。
本段不需要 $R_i$ 在未知不变限制上像稠密。

## 3. 所有允许选择都只改变一个有界交换单位

对同一 $M_i$ 另取
$$
L_i'=M_iU_i'+F_i',\qquad
\lambda_i'\in\rho(L_i'),\qquad
R_i'=(L_i'-\lambda_i'I)^{-1}.
$$
令
$$
V_i=(L_i'-\lambda_i'I)R_i
=U_i'D_i+(F_i'-\lambda_i'I)R_i,
$$
$$
W_i=(L_i-\lambda_iI)R_i'.
\tag{3.1}
$$
两者均为全域有界 $\mathfrak C$ 元。

对任意 $x\in H$，$R_i'x$ 属于共同的实际域 $\operatorname{Dom}M_i$。
所以逐步使用真正的逆恒等式，得到
$$
V_iW_ix
=(L_i'-\lambda_i'I)R_i(L_i-\lambda_iI)R_i'x
=(L_i'-\lambda_i'I)R_i'x=x.
$$
反向同理，$W_iV_i=I$。因此
$$
\boxed{V_i\in\mathfrak C^\times,\qquad
R_i'=R_iV_i^{-1}.}
\tag{3.2}
$$

定义共同乘积
$$
R=\prod_{i=1}^rR_i,\qquad R'=\prod_{i=1}^rR_i'.
$$
$\mathfrak C$ 交换，所以 $R'=RV$，其中
$V=\prod_iV_i^{-1}$ 为有界交换单位。特别
$$
\boxed{
R'\mathfrak C=R\mathfrak C,\qquad
R'H=RH.
}
\tag{3.3}
$$
这是实际代数主理想及实际值域相同，强于只说像的闭包相同。

## 4. 共同图闭像和真空缺陷也不变

令
$$
R_{\ne i}=\prod_{j\ne i}R_j,\qquad
\widehat D_i=M_iR=D_iR_{\ne i}\in\mathfrak C.
$$
于是 $RH\subseteq\bigcap_i\operatorname{Dom}M_i$，并定义
$$
\mathcal R x=(Rx,\widehat D_1x,\ldots,\widehat D_rx),\qquad
\Gamma_R=\overline{\mathcal RH}.
$$
和前附录相同：先对有限 Walsh $x$ 令 $R^{(r+1)}$ 作用于其共同图，再利用 $\mathcal R$ 有界取极限，得到
$$
\Gamma_R\subseteq\Gamma,\qquad
\boxed{\Gamma_R=\overline{R^{(r+1)}\Gamma}.}
\tag{4.1}
$$
$V$ 及 $V^{-1}$ 的对角放大都保持 $\Gamma$，因此
$$
\boxed{\Gamma_{R'}=\Gamma_R.}
\tag{4.2}
$$

在 (1.3) 的真湮灭前提下，单端配对给
$$
h=\sum_iM_iRf_i,\qquad
\phi_\rho(RF)=B(Fh,1).
$$
使用 $S$ 的单射性和 $1$ 循环，得 $h=0$。因此
$$
\boxed{\phi_\rho(RF)=0\quad(F\in\mathfrak C).}
\tag{4.3}
$$
由 (3.3)，更换全部 $U_i,F_i,\lambda_i$ 后仍是同一个被湮灭的代数主理想。

置
$$
v=(1,Cf_1,\ldots,Cf_r)\in\Gamma,\qquad
w=(0,Cf_1,\ldots,Cf_r).
$$
有界 $\widehat D_i$ 的 $C$ 对称性给 $w\perp\Gamma_R$，
而 $\langle v,w\rangle=\tau$、$\|w\|=\sqrt\tau$，故
$$
\boxed{\operatorname{dist}(v,\Gamma_R)\ge\sqrt\tau.}
\tag{4.4}
$$
每个单独二坐标投影仍图稠密。确切地，
$$
z\mapsto(R_iz,D_iz)
$$
是 $H$ 到 $\operatorname{Graph}M_i$ 的有界图范数同构；
逆为 $(x,M_ix)\mapsto U_iM_ix+B_ix$。
$R_{\ne i}H$ 稠密，遂得
$$
\overline{\operatorname{pr}_{0,i}(\Gamma_R)}
=\operatorname{Graph}M_i.
\tag{4.5}
$$
(4.4) 的共同图缺口不由逐个 (4.5) 消除。

## 5. 真空共同原像的有限自然词域判据

对一个排列 $\pi$，定义下述有限域条件 $\mathcal C_\pi$：

对每个子序列
$$
1\le k_1<\cdots<k_s\le r
$$
（包括空子序列），自然词
$$
M_{\pi(k_s)}\cdots M_{\pi(k_1)}1
\tag{5.1}
$$
按从右到左的实际域逐步有定义。

这里只涉及至多 $2^r$ 个字母不重复的自然词。
不能只检查完整的一个最高阶词，因为展开有界扰动后会出现全部较低子词。

**定理 5.1。** 在 (2.1) 的广义预解前提下，下列条件等价：

1. $1\in RH$；
2. 对某个排列 $\pi$，$\mathcal C_\pi$ 成立；
3. 对每个排列 $\pi$，$\mathcal C_\pi$ 成立。

此条件也不依赖广义预解参数的选取。

**证明 $1\Rightarrow3$。** 设 $1=Rg$。
对任意互异指标 $i_1,\ldots,i_s$，利用 $M_iR_i=D_i$ 和 (1.1)，逐次得到
$$
\boxed{
M_{i_s}\cdots M_{i_1}1
=\left(\prod_{\nu=1}^sD_{i_\nu}\right)
 \left(\prod_{j\notin\{i_1,\ldots,i_s\}}R_j\right)g.
}
\tag{5.2}
$$
每一步确实有定义：在应用下一个 $M_i$ 之前，右端仍含 $R_i$，其余有界交换因子保持 $\operatorname{Dom}M_i$。
因此全部这些自然词存在；其值还与指标顺序无关。
这不是预先假定未知无界乘子在所有自然乘积域上可交换。

**证明 $2\Rightarrow1$。** 固定满足 $\mathcal C_\pi$ 的排列。
逐步展开
$$
g=(L_{\pi(r)}-\lambda_{\pi(r)}I)\cdots
  (L_{\pi(1)}-\lambda_{\pi(1)}I)1.
\tag{5.3}
$$
每个 $L_i-\lambda_iI=U_iM_i+B_i$。
全部 $U_i,B_i$ 有界并完整交换、保持各 $M_j$ 的实际域。
第 $k$ 步仅出现前 $k$ 个字母的子序列词 (5.1)；在应用下一步之前，$\mathcal C_\pi$ 正好保证各项属于所需域。
故 (5.3) 是实际 $H$ 向量。按逆序逐次使用对应 $R_i$ 的真逆，即得 $Rg=1$。
$3\Rightarrow2$ 显然。参数独立性来自 (3.3)。证毕。

秩二时，这恰还原前附录的准确条件
$$
1\in RH
\iff Cf_1\in\operatorname{Dom}M_2
\iff Cf_2\in\operatorname{Dom}M_1.
$$
更高秩时不能只从这些两两域条件推出全部 (5.1)。

## 6. 对真见证的结论及尚未关闭的条件

前附录的正真空锚说明：一旦 $1\in RH$，
$$
B\!\left(\sum_iM_iRf_i,g\right)=\tau>0
$$
与 $h=0$ 矛盾。因此，对一个非零正有限秩真湮灭者：

- 或者至少一个 $M_i$ 对所有单位 $U_i$ 和有界 $F_i$ 都无法产生广义预解点；
- 或者虽每个广义预解式都可构造，但同一个参数无关的共同图有 (4.4) 的真空缺陷，而且每个排列的自然词域条件 $\mathcal C_\pi$ 都必须失败。

这不是充分排除所有见证。正常性、有限秩和各单独闭图均未被证明强迫有限自然词域。
R267 的共同所有 $A$ 幂图核心也没有把 $1$ 送进这些新混合域。
后续需要来自真实正矩的额外交叉域或共同图稠密性，不能只继续调整有界扰动、单位倍数或预解点。
普通 Hilbert ISP 仍未完成。
