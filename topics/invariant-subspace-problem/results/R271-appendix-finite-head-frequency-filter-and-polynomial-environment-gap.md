# R271 附录：有限头差谱的避让、精确频率滤波与全环境多项式能量下界

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / boundary_resume_1cf。
状态：已证明；Astra-ISP-1cf8c51d 与 kernel_resume_1cf 核对全部频率、傅里叶矩、原环境能量与显式常数。本文只给整个环境上的联合 $L,L^*$ 能量；不将该下界传给未知不变空间中的压缩伴随、联合旗或最小修复 Gram。

[旧全孔层环境稿](R239-appendix-all-hole-environment-energy-gap-and-actual-tail-stability.md)
已用有限次嵌套交换子隔离纯尾单个位，得到 $\log L_m=O(m\log m)$ 的纯尾常数。
下面改用一个有明确一阶时间矩的傅里叶窗，既改善纯尾常数，也允许加入任意有限维头。
头的相似矩阵及其条件数不进入证明。

## 1. 模型、全域和明确结论

设 $m\ge5$、$d\ge1$，令 $A$ 是任意 $d$ 维 Hilbert 空间上的有界算子。
它无需正规或幂零。纯尾仍是原有限子集 Boolean 模型
$$
D=D_m=\sum_{j\ge m}a_jE_j,\qquad a_j=(j+1)^{-2}.
$$
所有级数按算子范数收敛。
在头尾 Hilbert 张量积上记
$$
L=A\otimes I+I\otimes D,\qquad M=\|L\|,\qquad J=m+d^2.
$$
省略张量单位时仍只作这个物理头尾分解。
定义
$$
\mathcal E_L(x)=\|Lx\|^2+\|L^*x\|^2.
$$

**定理。** 对整个 Hilbert 空间内的每个 $x$，
$$
\boxed{
\mathcal E_L(x)\ge
\frac{\|x\|^2}
{2048(1+M^2)^2(J+2)^{14}}.
}
\tag{1.1}
$$
本式同时涵盖全部孔层和它们的任意叠加。

对原实际有限头 $A=A_m$、$d=2^m$，若使用既有 $\|A_m\|\le6$、
$\|D_m\|\le1/m$，可粗取 $M\le7$。
于是环境下界倒数仅为 $O((m+d^2)^{14})$，
其平方根的对数为 $O(m)$。
这不是原最小修复成本的上界。

## 2. 头差谱与尾频率的精确分离

令
$$
C=[L,L^*]=LL^*-L^*L.
$$
头尾交换给
$$
C=C_A\otimes I+I\otimes C_D,\qquad
C_A=[A,A^*],\qquad
C_D=[D,D^*].
\tag{2.1}
$$
两个算子均为有界自伴算子。
在尾上记 $n_j=E_j^*E_j$，逐位矩阵关系给
$$
C_D=\left(\sum_{j\ge m}a_j^2\right)I
       -2\sum_{j\ge m}a_j^2n_j,
\qquad [n_j,E_j]=-E_j.
$$
因此准确的正频率是
$$
\boxed{[C_D,E_j]=\omega_jE_j,\qquad \omega_j=2a_j^2=2(j+1)^{-4}.}
\tag{2.2}
$$

取 $C_A$ 的谱分解 $C_A=\sum_{\nu=1}^s\lambda_\nu P_\nu$，
其中 $s\le d$、全部 $\lambda_\nu$ 为实数。
头算子的共轭展开为
$$
e^{itC_A}Ae^{-itC_A}
=\sum_{\nu,\mu}e^{it(\lambda_\nu-\lambda_\mu)}P_\nu AP_\mu.
$$
所以全部头频率位于有限集合
$$
\mathcal F_A=\{\lambda_\nu-\lambda_\mu:1\le\nu,\mu\le s\},
\qquad |\mathcal F_A|\le d^2.
\tag{2.3}
$$
不需要任何两个头特征值差之间有正的定量分离。

选尾候选
$$
j=m,m+1,\ldots,J
$$
共 $d^2+1$ 个。
置
$$
\Delta_J=\omega_J-\omega_{J+1}
=2\bigl((J+1)^{-4}-(J+2)^{-4}\bigr),\qquad r=\frac{\Delta_J}{4}.
$$
函数差单调递减；用积分还得到
$$
\boxed{
\Delta_J
=8\int_{J+1}^{J+2}x^{-5}\,dx
\ge\frac8{(J+2)^5},
\qquad
\frac2{(J+2)^5}\le r<1.
}
\tag{2.4}
$$
闭区间
$$
I_j=[\omega_j-r,\omega_j+r]\qquad(m\le j\le J)
$$
两两不交，因为候选相邻频率的距离至少为 $\Delta_J=4r$。
每个头频率至多落在其中一个区间。
由 (2.3) 与抽屉原理，存在一个 $j_*\in[m,J]$，使
$$
I_{j_*}\cap\mathcal F_A=\varnothing.
\tag{2.5}
$$
此外，所有尾频率而非仅候选频率都满足
$$
|\omega_\ell-\omega_{j_*}|\ge\Delta_J=4r
\qquad(\ell\ge m,\ \ell\ne j_*).
\tag{2.6}
$$
对候选区间之外的较大 $\ell$，最近的频率已经是
$\omega_{j_*+1}$，其间距仍至少为 $\Delta_J$。
这同时检查了所选窗口的两端，没有遗漏无限尾。

## 3. 一个有显式时间矩的紧支撑频率窗

取
$$
\chi(u)=
\begin{cases}
(1-u^2)^3,&|u|\le1,\\
0,&|u|>1.
\end{cases}
$$
它满足 $\chi(0)=1$，且 $\chi,\chi',\chi''$ 在两个端点均为零。
令
$$
\phi_0(t)=\frac1{2\pi}\int_{\mathbb R}\chi(u)e^{-itu}\,du.
$$
对 $|t|\le1$，有 $|\phi_0(t)|\le1/\pi$。
对 $|t|>1$，三次分部积分以及
$$
\chi'''(u)=72u-120u^3\quad(|u|<1),\qquad
\|\chi'''\|_{L^1}\le132
$$
给
$$
|\phi_0(t)|\le\frac{66}{\pi}|t|^{-3}.
$$
所以
$$
\boxed{
\|\phi_0\|_{L^1}\le\frac{68}{\pi}<23,\qquad
\int_{\mathbb R}|t\phi_0(t)|\,dt
\le\frac{133}{\pi}<45.
}
\tag{3.1}
$$
傅里叶反演在这里绝对收敛：
$\chi(u)=\int_{\mathbb R}\phi_0(t)e^{itu}\,dt$。

定义
$$
\phi(t)=r e^{-i\omega_{j_*}t}\phi_0(rt).
$$
其频率响应准确为
$$
\int_{\mathbb R}\phi(t)e^{it\omega}\,dt
=\chi\left(\frac{\omega-\omega_{j_*}}r\right).
\tag{3.2}
$$
缩放给
$$
\|\phi\|_1<23,\qquad
\int|t\phi(t)|\,dt<45/r.
\tag{3.3}
$$
构造有界算子范数中的 Bochner 积分
$$
Z=\int_{\mathbb R}\phi(t)e^{itC}Le^{-itC}\,dt.
\tag{3.4}
$$
它存在，因为共轭因子酉且 $\phi\in L^1$。

由 (2.1)，头尾共轭分别展开。
(2.5) 使全部头项的频率响应为零；
(2.6) 使全部未选尾位的响应为零；
(3.2) 在选定频率处等于 $1$。
尾级数本来就按范数绝对收敛，故与积分交换合法。
于是得到全环境上的准确恒等式
$$
\boxed{Z=a_{j_*}E_{j_*}.}
\tag{3.5}
$$
这是精确提取，不带近似余项。

## 4. 滤波成本只读取原联合能量

从定义直接有
$$
\|Cx\|
\le M\bigl(\|Lx\|+\|L^*x\|\bigr)
\le\sqrt2 M\,\mathcal E_L(x)^{1/2}.
\tag{4.1}
$$
因 $C$ 自伴，
$$
(e^{-itC}-I)x=-i\int_0^t e^{-isC}Cx\,ds,
$$
其中负 $t$ 使用有向积分。因此
$$
\|(e^{-itC}-I)x\|\le|t|\,\|Cx\|.
\tag{4.2}
$$
所以
$$
\begin{aligned}
\|e^{itC}Le^{-itC}x\|
&=\|Le^{-itC}x\|\\
&\le\|Lx\|+M\|(e^{-itC}-I)x\|\\
&\le(1+\sqrt2 M^2|t|)\mathcal E_L(x)^{1/2}.
\end{aligned}
$$
结合 (3.3) 和 $\sqrt2\,45<64$，
$$
\|Zx\|
\le\left(23+\frac{64M^2}r\right)\mathcal E_L(x)^{1/2}.
\tag{4.3}
$$
同样的证明对 $L^*$ 成立。
取 (3.4) 的伴随时只把 $\phi$ 换成 $\overline\phi$，
它的两个绝对矩不变，因此
$$
\|Z^*x\|
\le\left(23+\frac{64M^2}r\right)\mathcal E_L(x)^{1/2}.
\tag{4.4}
$$

由 $r<1$ 及 (2.4)，两式共同的括号不超过
$$
\frac{64(1+M^2)}r
\le32(1+M^2)(J+2)^5.
\tag{4.5}
$$
另一方面，真实单个位满足
$$
E_{j_*}^*E_{j_*}+E_{j_*}E_{j_*}^*=I.
$$
使用 (3.5)、(4.3)–(4.5)，
$$
\begin{aligned}
a_{j_*}^2\|x\|^2
&=\|Zx\|^2+\|Z^*x\|^2\\
&\le2048(1+M^2)^2(J+2)^{10}\mathcal E_L(x).
\end{aligned}
$$
又 $j_*\le J$ 给
$a_{j_*}^2\ge(J+1)^{-4}\ge(J+2)^{-4}$，
遂得 (1.1)。

## 5. 纯尾的直接多项式常数

若没有头项，头频率只有 $0$，可以直接选 $j_*=m$，
不需要 $d^2+1$ 个候选。
仍取 $r=(\omega_m-\omega_{m+1})/4$。
由 $\|D_m\|\le1/m$、(2.4) 的同样估计，
(4.3) 的括号不超过
$$
23+32\frac{(m+2)^5}{m^2}\le65(m+2)^3
\qquad(m\ge5).
$$
这里用了 $(m+2)^2/m^2\le49/25<2$。
故
$$
\boxed{
D_m^*D_m+D_mD_m^*
\ge\frac1{2^{14}(m+2)^{10}}I.
}
\tag{5.1}
$$
最后只把 $2\cdot65^2=8450$ 放宽到 $2^{14}$。
这是旧纯尾环境结论的较强明确常数，仍是环境 $D_m^*$。

## 6. 一般小扰动及准确适用边界

若 $\widetilde L=L+E$、$\|E\|\le\varepsilon$，令
$$
\gamma=\bigl[2048(1+M^2)^2(J+2)^{14}\bigr]^{-1/2}.
$$
在两个分量的 Hilbert 直和中，三角不等式给
$$
\bigl(\|\widetilde Lx\|^2+\|\widetilde L^*x\|^2\bigr)^{1/2}
\ge(\gamma-\sqrt2\varepsilon)\|x\|.
\tag{6.1}
$$
特别 $\varepsilon\le\gamma/(2\sqrt2)$ 时，新的联合能量下界至少为
$\gamma^2/4$。
把它应用到任一实际 carry 扰动时，仍使用该模型已证的完整算子差；
本节不删去头部误差。

对 $x\in\ker L$，(1.1) 确实给
$\|L^*x\|\ge\gamma\|x\|$。
但是本文中的 $e^{itC}$ 不曾被证明保持未知的 $M$、$W$ 或原联合旗，
(3.5) 也不是在这些受限空间上的滤波恒等式。
因此不能由此给
$P_{\mathscr C}L^*$、$P_{\ker D^h}D^*$ 或任一 Schur 补相同下界。
旧两位例中环境 $D^*h\ne0$ 而
$P_{\ker D^2}D^*h=0$ 的区别仍原样存在。

实际高孔规范源的观测费用、原窄 $\overline f$ 的两侧能量比较和无权
$N=M$ 均未由本稿关闭。新增的是任意有限头存在时仍然成立的、只耗多项式常数的全环境联合能量证书。
