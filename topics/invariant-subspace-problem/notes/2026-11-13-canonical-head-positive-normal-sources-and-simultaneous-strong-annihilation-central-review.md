# 工作补充：完整有限头矩代表给同一正正常泛函的全部强湮灭残量

日期：2026-11-13 UTC。作者：central_review / Astra-ISP-0c017065；AI-assisted，GPT-6 Astra Pro。

状态：完整推导经 root 与 normal_complex 独立核验。
它使用原实际模型和同一个固定正迹类 $\rho$。
新增点是：完整有限头矩代表本身既是全 $A'$ 正常泛函的近似真空源，又同时具有所有已知湮灭算子的强向量残量。
不要求 $\rho$ 支持于这些算子的核。
这与使用真核条件得到的既有交叉截断源估计是两个不同源的结论，不能互换。

## 1. 原模型与准确有限头

令
$$
H=H_{<p}\otimes H_{\ge p},\qquad
\Omega=\Omega_{<p}\otimes\Omega_{\ge p},
$$
其中原真空 $\Omega=1$，各因子范数均为一。
置
$$
\Pi_p=I_{<p}\otimes
|\Omega_{\ge p}\rangle\langle\Omega_{\ge p}|.
$$
于是 $\operatorname{Ran}\Pi_p$ 是前 $p$ 位 Walsh 柱空间，
$\Pi_p\to I$ 强收敛。
原反线性对合
$$
Cf(y)=\overline{f(-1-y)}
$$
分解为两因子的同类对合，并保持 $\operatorname{Ran}\Pi_p$，
且 $C\Omega=\Omega$。

写
$$
B(f,g)=\langle f,Cg\rangle,\qquad
\Phi_v(R)=\langle Rv,\Omega\rangle
=B(v,R\Omega)\quad(R\in\mathfrak C=A').
\tag{1.1}
$$
最后一个等号使用原实际 $\mathfrak C$ 的 $C$ 对称性。
以下一律保留这个对合，不将 $B$ 当作不含位反射的坐标配对。

沿用 [R230 正密度截断稿](../results/R230-appendix-positive-density-walsh-truncation-and-small-trace-tail-improvement.md)
的实际乘子 $V_j$、准确局部乘子 $V_j^{[p]}$ 及局部代数 $\mathcal A_p$。
局部代数只作用于前 $p$ 位，在头外张量恒等；
它是交换的，并具有局部 $C$ 对称性。
所有 $F\subset[0,p)$ 都有
$$
V_F\Omega=V_F^{[p]}\Omega=\chi_F.
\tag{1.2}
$$
因此真空在有限头上循环且分离。

对 $a\in\operatorname{Ran}\Pi_p$ 定义
$$
X_a=\sum_{F\subset[0,p)}\widehat a(F)V_F,\qquad
X_a^{[p]}=\sum_{F\subset[0,p)}\widehat a(F)V_F^{[p]}.
$$
它们的准确预算为
$$
K_p=10^{p/2},\qquad
D_p=6\eta_{p-1}
\left(\sum_{F\subset[0,p)}|F|^2\,9^{|F|}\right)^{1/2}
\le6p\eta_{p-1}K_p,
\tag{1.3}
$$
$$
\|X_a\|,\ \|X_a^{[p]}\|\le K_p\|a\|,
\qquad
\|X_a-X_a^{[p]}\|\le D_p\|a\|.
\tag{1.4}
$$
$X_a\in\mathcal A\subset\mathfrak C$；
$X_a^{[p]}\in\mathcal A_p$，不把后者称为实际 $\mathfrak C$ 元素。
它们都把真空送到 $a$。

## 2. 完整有限头代表与正的重置密度

固定 $\rho\ge0$ 为迹类，令
$$
\tau=\operatorname{Tr}\rho>0,\qquad
\delta_p=\operatorname{Tr}(\rho(I-\Pi_p))\longrightarrow0.
$$
定义辅助密度
$$
\boxed{
\widehat\rho_p=
\bigl(\operatorname{Tr}_{\ge p}\rho\bigr)
\otimes|\Omega_{\ge p}\rangle\langle\Omega_{\ge p}|.
}
\tag{2.1}
$$
这是对原密度作头外真空重置。
它正、迹为 $\tau$，且支持于 $\operatorname{Ran}\Pi_p$。
它只用于证明源近似；原见证始终是固定的 $\rho$，
不把 $\widehat\rho_p$ 宣称为同样的湮灭者。

对每个 $R_p\in\mathcal A_p$，部分迹的定义给准确等式
$$
\operatorname{Tr}(\widehat\rho_pR_p)
=\operatorname{Tr}(\rho R_p).
\tag{2.2}
$$

下面给不需要尾衰减速度的迹范数预算。
取任意平方分解
$$
\rho=\sum_i f_i\otimes f_i,\qquad
a_i=\Pi_pf_i,\quad b_i=(I-\Pi_p)f_i.
$$
于是
$$
\sum_i\|a_i\|^2=\tau-\delta_p,\qquad
\sum_i\|b_i\|^2=\delta_p.
$$
记
$$
\rho_{aa}=\sum_i a_i\otimes a_i,\qquad
\sigma_p=\sum_i b_i\otimes b_i.
$$
头外部分迹消去每个 $a_i\otimes b_i$ 及其伴随项：
$a_i$ 的头外因子是真空，$b_i$ 在头外真空方向的分量为零。
因此
$$
\widehat\rho_p
=\rho_{aa}+\widehat\sigma_p,
$$
其中 $\widehat\sigma_p\ge0$ 且迹为 $\delta_p$。
由两交叉项的迹范数 Cauchy--Schwarz，
$$
\boxed{
\|\widehat\rho_p-\rho\|_1
\le
2\delta_p+2\sqrt{(\tau-\delta_p)\delta_p}
\le2\delta_p+2\sqrt{\tau\delta_p}.
}
\tag{2.3}
$$
这特别证明 $\widehat\rho_p\to\rho$ 迹范数收敛。
没有用 $K_p\delta_p\to0$ 一类未给出的速度条件。

### 2.1 两个准确源的比较

在有限维头上取正平方分解
$$
\widehat\rho_p=\sum_{\ell} a_{\ell,p}\otimes a_{\ell,p},
\qquad a_{\ell,p}\in\operatorname{Ran}\Pi_p,\qquad
\sum_\ell\|a_{\ell,p}\|^2=\tau.
$$
定义
$$
u_p=\sum_\ell X_{a_{\ell,p}}Ca_{\ell,p},\qquad
v_p=\sum_\ell X_{a_{\ell,p}}^{[p]}Ca_{\ell,p}.
\tag{2.4}
$$
这些是有限和，且 $v_p\in\operatorname{Ran}\Pi_p$。
由 (1.4)，
$$
\boxed{
\|u_p\|,\ \|v_p\|\le\tau K_p,\qquad
\|u_p-v_p\|\le\tau D_p.
}
\tag{2.5}
$$

对任意实际 $R\in\mathfrak C$，
原 $C$ 对称性与交换关系给
$$
\begin{aligned}
\Phi_{X_aCa}(R)
&=B(X_aCa,R\Omega)\\
&=B(Ca,X_aR\Omega)\\
&=B(Ca,Ra)\\
&=\langle Ra,a\rangle.
\end{aligned}
$$
故
$$
\boxed{\Phi_{u_p}=\varphi_{\widehat\rho_p}
\quad\text{于整个实际 }\mathfrak C.}
\tag{2.6}
$$

在同一个有限头内逐字作此计算，则
$$
\boxed{
B(v_p,R_p\Omega)
=\varphi_{\widehat\rho_p}(R_p)
=\varphi_\rho(R_p)
\quad(R_p\in\mathcal A_p).
}
\tag{2.7}
$$
因 $\mathcal A_p\Omega=\operatorname{Ran}\Pi_p$，
(2.7) 唯一确定 $v_p$。
所以 (2.4) 的 $v_p$ 与平方分解无关；
它正是原完整有限头矩代表 $v_p^\rho$，
不是只保留 $\Pi_p\rho\Pi_p$ 的低部代表。

结合 (2.3)、(2.5)、(2.6)，得到
$$
\boxed{
\|\Phi_{v_p}-\varphi_\rho\|_{\mathfrak C_*}
\le
\tau D_p+2\delta_p+2\sqrt{\tau\delta_p}
\longrightarrow0.
}
\tag{2.8}
$$
这里的范数针对整个实际 $\mathfrak C$ 单位球。
实际乘子提升与局部乘子间的差已经由 $\tau D_p$ 支付。

令 $R_p=I$ 还得到准确锚定
$$
\boxed{\langle v_p,\Omega\rangle=\tau.}
\tag{2.9}
$$

## 3. 任意正常湮灭式给这个同一源的强残量

设 $Z\in\mathfrak C$ 有界，并且原固定密度满足
$$
\varphi_\rho(ZR)=0\qquad(R\in\mathfrak C).
\tag{3.1}
$$
取任何准确局部头 $Z_p\in\mathcal A_p$，记
$$
d_p(Z)=\|Z-Z_p\|,\qquad
\Gamma_p(Z)=2K_pd_p(Z)+\|Z\|D_p.
\tag{3.2}
$$
不假设 $Z\rho=0$，也不假设 $\Pi_p$ 与 $Z$ 交换。

**命题。** 对 §2 的同一个完整有限头代表，
$$
\boxed{
\|Zv_p\|\le\tau\,\Gamma_p(Z).
}
\tag{3.3}
$$

**证明。**
取任意 $w\in\operatorname{Ran}\Pi_p$，$\|w\|=1$。
因为局部 $Z_p$ 为 $C$ 对称，
$$
\begin{aligned}
B(Z_pv_p,w)
&=B(v_p,Z_pw)\\
&=B(v_p,Z_pX_w^{[p]}\Omega)\\
&=\varphi_\rho(Z_pX_w^{[p]}),
\end{aligned}
\tag{3.4}
$$
最后一步只用 (2.7)，因为乘积属于同一个 $\mathcal A_p$。
这里没有把局部算子放入实际零式 (3.1)。

正确的实际零项是 $\varphi_\rho(ZX_w)=0$，其中 $X_w\in\mathfrak C$。
减去该项，并用
$$
Z_pX_w^{[p]}-ZX_w
=(Z_p-Z)X_w^{[p]}+Z(X_w^{[p]}-X_w),
$$
得到
$$
|B(Z_pv_p,w)|
\le
\tau\bigl(K_pd_p(Z)+\|Z\|D_p\bigr).
$$
$Z_pv_p$ 仍在有限头内，且 $C$ 保持该头，
所以对全部单位 $w$ 取上确界即给相同的范数界。
最后使用
$$
\|(Z-Z_p)v_p\|
\le d_p(Z)\|v_p\|
\le\tau K_pd_p(Z)
$$
即得 (3.3)。证毕。

这证明的是准确有限头代表的强向量预算，
不是从 $\|\Phi_{Zv_p}\|$ 小反推 $\|Zv_p\|$ 小。
两者之间的缺口是由有限头循环性、局部 $C$ 对称性和真实提升误差共同支付的。

同一证明还有近湮灭版本。
若
$$
\epsilon(Z)=\|\varphi_\rho(Z\,\cdot)\|_{\mathfrak C_*},
$$
则
$$
\boxed{
\|Zv_p\|
\le\tau\Gamma_p(Z)+K_p\epsilon(Z).
}
\tag{3.5}
$$
准确零式对应 $\epsilon(Z)=0$。

## 4. 全部已知零式同时作用于同一个源

设固定有限族 $Z_1,\ldots,Z_d\in\mathfrak C$
均满足 (3.1)，各自有准确局部头 $Z_{\nu,p}\in\mathcal A_p$。
则同一个 $v_p^\rho$ 满足
$$
\|Z_\nu v_p^\rho\|
\le\tau\Gamma_p(Z_\nu)\qquad(1\le\nu\le d).
\tag{4.1}
$$
若
$$
K_p d_p(Z_\nu)\longrightarrow0
\quad\text{对每个 }\nu,
$$
则全部这些强残量同时趋零。
(2.8) 仍把这些源的正常泛函带回同一个固定原 $\rho$；
没有给不同的算子重选密度、子商或参数。

若其中一个 $Z_\nu=S$ 在整个 $H$ 上单射，
则 $\|v_p^\rho\|\to\infty$。
否则存在范数有界子序列，取弱收敛子列 $v_{p_k}\rightharpoonup v$；
(2.8) 给 $\Phi_v=\varphi_\rho\ne0$。
又 (4.1) 给 $Sv=0$，与单射性矛盾。
同理，所有 $v_p/\|v_p\|$ 的弱聚点均为零：
对其任意弱聚点使用
$$
\Phi_{v_p/\|v_p\|}\longrightarrow0
$$
及原真空的伴随循环性即可。
所以
$$
\boxed{
\|v_p\|\to\infty,\qquad
\frac{v_p}{\|v_p\|}\rightharpoonup0,\qquad
\langle v_p,\Omega\rangle=\tau.
}
\tag{4.2}
$$
这里未给范数发散的下速度。

## 5. 当前迟首二次联合见证的实际头误差

沿用已经固定的同一个 $\zeta,H=H_\zeta,\rho$，置
$$
X=\sum_ja_jQ_j,\quad
Y=\sum_jc_jQ_j,\quad
B_0=\sum_ja_j^2Q_j^2,
$$
$$
T=X^2-B_0+Y,\quad
S=X+H,\quad
G=B_0-H^2,\quad
Z=Y-G.
\tag{5.1}
$$
原联合见证给
$$
\varphi_\rho(S\mathfrak C)
=\varphi_\rho(T\mathfrak C)
=\varphi_\rho(Z\mathfrak C)=0.
\tag{5.2}
$$
本节使用 $H$ 的真解析芽性质；
不把整个 $G$ 无证写成真解析芽。

取同一个物理头中的 $Q_j^{[p]}$，定义
$$
X_p=\sum_{j<p}a_jQ_j^{[p]},\quad
Y_p=\sum_{j<p}c_jQ_j^{[p]},\quad
B_p=\sum_{j<p}a_j^2(Q_j^{[p]})^2.
$$
设 $A^{[p]}$ 为相同 nilpotent 头的实际截断，
并置
$$
H_p=H(A^{[p]}),\quad
S_p=X_p+H_p,\quad
G_p=B_p-H_p^2,
$$
$$
Z_p=Y_p-G_p,\qquad
T_p=X_p^2-B_p+Y_p.
\tag{5.3}
$$
全部属于同一个 $\mathcal A_p$。

为免把实际 carry 当成等式常数，记粗上界
$$
\bar\eta_j=e^{-770\,16^j}.
$$
原递推给
$$
\|A-A^{[p]}\|\le C_A\bar\eta_{p-1}.
$$
$A^{[p]}\to A$ 按范数收敛，且二者谱均为 $\{0\}$。
在 $H$ 的一个固定解析圆周上，原 $A$ 的预解有界；
充分大 $p$ 时预解恒等式给 $A^{[p]}$ 同一圆周上的一致界。
解析积分遂给
$$
\|H-H_p\|\le C_H\bar\eta_{p-1}.
\tag{5.4}
$$
有限个早期 $p$ 可以不使用，所有渐近结论不受影响。
这是固定 $H$ 的真正解析演算，常数不随 $p$ 变化。

原实际及局部估计给
$$
\|X-X_p\|
\le C_a\bar\eta_{p-1}
+4\sum_{j\ge p}|a_j|,
$$
$$
\|Y-Y_p\|
\le C_c\bar\eta_{p-1}
+4\sum_{j\ge p}|c_j|.
\tag{5.5}
$$
二阶行的尾要保其真实 carry。
因为
$$
Q_j^2=4\eta_jN_{j+1}(I+N_j)^{-2},
\qquad
\|Q_j^2\|\le36\eta_j,
$$
可得
$$
\boxed{
\|B_0-B_p\|
\le C_{a,2}\bar\eta_{p-1}.
}
\tag{5.6}
$$
低头差由
$\|Q_j-Q_j^{[p]}\|\le18\eta_{p-1}$
及平方差估计支付；高尾由
$36\sum_{j\ge p}|a_j|^2\bar\eta_j$
支付。
此处需要 $a\in\ell^2$，当前 $a\in\ell^1$ 已足够。

由 (5.4)--(5.6)，
$$
d_p(S)\le
C\left(\bar\eta_{p-1}+\sum_{j\ge p}|a_j|\right),
$$
$$
\boxed{
d_p(Z)\le
C\left(\bar\eta_{p-1}+\sum_{j\ge p}|c_j|\right).
}
\tag{5.7}
$$
对 $T$ 用完整平方差
$X^2-X_p^2=X(X-X_p)+(X-X_p)X_p$，
得到
$$
d_p(T)\le
C\left(\bar\eta_{p-1}
+\sum_{j\ge p}(|a_j|+|c_j|)\right).
\tag{5.8}
$$
不要求实际 $X$ 与局部 $X_p$ 交换。

特别，在当前固定余族
$$
a_j=e^{-\beta j^\alpha},\qquad
c_j=a_j^\kappa\mathbf1_{j>j_0},\qquad
\alpha>1,\quad\kappa>1,
$$
凸性和几何级数给相应尾和的准确指数包络。
因此 §3 给同一个完整有限头源
$$
\boxed{
\|Sv_p\|
\le C_\rho10^{p/2}
\left(e^{-\beta p^\alpha}+p\bar\eta_{p-1}\right),
}
$$
$$
\boxed{
\|Zv_p\|
\le C_\rho10^{p/2}
\left(e^{-\kappa\beta p^\alpha}+p\bar\eta_{p-1}\right),
}
$$
$$
\boxed{
\|Tv_p\|
\le C_\rho10^{p/2}
\left(e^{-\beta p^\alpha}+p\bar\eta_{p-1}\right).
}
\tag{5.9}
$$
全部趋零。
第二式保留了辅助行更快的实际指数，
没有把 $B_0$ 错作一个慢 $a^2$ 尾，也没有混用不同 $\zeta$。

## 6. 与既有真核交叉源的区别及仍未付的步骤

既有实际交叉截断源为
$$
h_p=\sum_i
\left(X_{a_i}Ca_i+X_{a_i}Cb_i+X_{Ca_i}b_i\right),
\quad
a_i=\Pi_pf_i,\ b_i=(I-\Pi_p)f_i.
$$
它满足
$$
\Phi_{h_p}=\varphi_\rho-\varphi_{\sigma_p},
\qquad
\|\Phi_{h_p}-\varphi_\rho\|=\delta_p.
$$
若另外有真实核支持 $T\rho^{1/2}=0$，
[核支持源补充](2026-11-13-kernel-supported-positive-density-and-strong-truncated-source-residual-normal-complex.md)完整证明
$$
\|Th_p\|
\le
\bigl(2K_pd_p(T)+\|T\|D_p\bigr)\sqrt{\tau\delta_p}.
$$
这比某些相应 $v_p$ 估计保留了额外 $\sqrt{\delta_p}$，
但对 $S$ 不能从泛函零式直接在这个 $h_p$ 上使用同一强估计。

本稿改用完整局部代表 $v_p$：
它的正常泛函误差为 (2.8)，
而所有准确正常湮灭式都给 (3.3)。
二者都是原固定 $\rho$ 的合法源序列，
但本稿不声称它们的向量范数之差趋零。

即使 (5.9) 同时成立，
仍不能在没有实际右逆或谱间隙的条件下推断
$v_p$ 到某个联合核的距离趋零。
不能从小 $Sv_p$ 和 $S$ 全空间单射推出 $v_p$ 有界，
更不能删除 (4.2) 中确实发散的源费用。
本稿没有构造非零 $\mathcal G$ 元素属于
$SA'+ZA'$ 的实际理想证书；
这个需要继续证明的连接仍保留。
