# R146：二次径向帽与真实根容量的必要筛查

2026-11-26，visible-exact-astra-198c63d-20261126 / correlated_energy。

**已证明（解析部分）：** [RS](R138-supplement-radial-weight-independent-root-budget-screen.md)
的完整根对偶必要性适用于下面不同的二次径向测试函数。新积分尚未执行时不赋值。
本篇保留任意正径向权、任意自由外截段、真正 $D_H^{-1}$、全部 high、真实 mean
与当前 $Q_{repair}$；只检验当前 CV/RA 的非负体/根费用格式。

## 1. 完整根算子与不同的合法测试函数

RS.1–RS.5 与实际 signed96/97 三个整球已经证明，任何有限接收器 $W$ 若用于
支付真实根型的负部，必须满足

$$
W^*W\succeq C^*(\vartheta D_H)^{-1}C-A_L,
\qquad 0<\vartheta\le1,
\qquad \|We_{96}\|^2>148.
\tag{QP.1}
$$

这里 $D_H$ 是真正的原 high97 压缩，未换成统一标量下界。
根代数输入 $e_{96}=\sqrt2\sin(384\phi)$、$\mathsf H=0$ 的完整旋转函数
$\omega_{96}$ 含原 mean rank 和环境 primitive。
[RN.9–RN.12](R138-supplement-root-anchored-spectral-budget-necessary-screen.md)
只读原 high41 球已得

$$
\|\omega_{96}\|_{L^2_{\phi,\mathrm{av}}}<1,
\qquad
\|\partial_\phi\omega_{96}\|_{L^2_{\phi,\mathrm{av}}}<377.
\tag{QP.2}
$$

不重新计算这两个范数或原三个 signed 条目。取新的有理长度
$\ell=3/200$，令 $x=r-r_*$ 并设

$$
f_2(x)=\left(1-\frac{x}{\ell}\right)_+^2,
\qquad f_2(0)=1,
\qquad
f_2'(x)=-\frac2\ell\left(1-\frac{x}{\ell}\right)
\quad(0<x<\ell).
\tag{QP.3}
$$

它在 $x=\ell$ 处的值与一阶导数均为零，是合法的 $H^1$ 比较函数。
若原局部根段较短就限制到该段，外值仍自由；若较长则继续取零。
它不向真实 PDE 添加新边界条件，也不把根代数数据当作 PDE 解。

## 2. 任意径向权的共同完整积分

沿用 RS.11–RS.13 的同一符号

$$
\eta=-\gamma m>0,
\qquad
h(r)=\frac{222}{125}
\min_{\epsilon\in\{+,-\}}
\frac{|v_\epsilon(r)|}{1+K(r)v_\epsilon(r)^2},
$$
$$
\frac{\alpha(r)}{C_{E,\alpha}}\le h(r),
\qquad p=\alpha/\eta,\quad q=\alpha\eta K.
\tag{QP.4}
$$

两个轴角仍是同一 moving/physical 角 $0,\pi/4$。$v_\pm$ 含全部32模、
独立 moving mean 和原修补，$K\ge0$ 只用于真正根右侧。

因此对任一上述权与局部段，完整能量满足

$$
\frac{\mathcal G_{p,q}[f_2\omega_{96}]}{C_{E,\alpha}}
\le T_2,
\tag{QP.5}
$$

只要新的完整上界 $T_2>0$ 支配

$$
\boxed{
\int_{r_*}^{r_*+3/200}h(r)
\left[
\frac{4}{\eta(r)\ell^2}
 \left(1-\frac{r-r_*}{\ell}\right)^2
+377^2\eta(r)K(r)
 \left(1-\frac{r-r_*}{\ell}\right)^4
\right]dr .}
\tag{QP.6}
$$

证明是将 $f_2\omega_{96}$ 代入准确加权能量，使用(QP.2)、(QP.4)，
并在截短时仅删除非负积分。与旧 RS 的区别是径向函数、长度和完整被积式；
没有将旧线性帽积分拆成未保存的分量，也不重算那个旧目标。

取 $c=We_{96}/\|We_{96}\|$。原准确对偶式给
$|\langle P_c',\omega_{96}\rangle|=|\rho|\|We_{96}\|$。
对原准确自由外值容量，或其任意合法更大的 Gram 上界，由定义与(QP.5)得

$$
\mathcal N_{p,q}(P_c')^2\ge
\frac{\rho^2\|We_{96}\|^2}
     {\mathcal G_{p,q}[f_2\omega_{96}]},
\qquad
(\alpha_E^{root})^2>\frac{148\Lambda^2}{T_2}
\ge\frac{148}{T_2}.
\tag{QP.7}
$$

这里 $\Lambda\ge1$ 是该格式所用的 scalar Jacobian 转授因子；RA 真根初值
给 $\Lambda^2=\Gamma_{loc}\ge1$。第一式直接由准确容量的对偶定义与合法测试
函数得到，不从已有容量 upper 反推实际容量 lower。完整 $H$、mean 与其他
source 费在该格式为非负，仍保留。

## 3. 与已完成 CV 体预算的准确二维比较

令当前 CV 实际保存的所选上界为 $a=a_{EE,corr}$、$b=a_{EB,corr}$，
旧完整 GB 为 $c=a_{BB}$。CV actual/执行文件来自
notes/correlated_gram_body_budget_ci/run-45762052058-1/ 下的完整两件。
沿 [R143 OC.3–OC.5](R143-correlated-body-energy-and-optimal-root-screen.md)，
只把根 EE 必要费用由 $37/30$ 换成(QP.7)的新值，得到

$$
\mathcal M\succ0
\ \Longrightarrow\
1-c>0,
\qquad
2-\frac{148}{T_2}-a-\frac{b^2}{4(1-c)}>0.
\tag{QP.8}
$$

实际计算先保存整个 $T_2$ 球并读回 upper $T_{2,+}>0$，再读当前 CV 两球与
旧 GB 球的 lower $a_-,b_-,c_-$。因此

$$
Q_+=\operatorname{upper}
\left(2-\frac{148}{T_{2,+}}-a_-
-\frac{b_-^2}{4(1-c_-)}\right)
\tag{QP.9}
$$

是最有利必要测试的合法 upper。$Q_+\le0$ 便严格排除当前完整 CV/RA 费用门；
无须再形成它的有限负部 Gram 或全高压缩逆。若 $Q_+>0$，只表示本次尚未排除。
这不否定实际 BVP，不排 PDE 可达迹的额外关系、同向有符号联合能量或直接逆。

## 4. 全部误差与新计算范围

新 consumer 固定320 bits、每个原交段32个子片；完整区间保守覆盖
$[r_*^{lo},r_*^{hi}+3/200]$。首 germ 使用原 whole 球和正侧 $K\ge0$，
之后每个 candidate/intrinsic 接口完整拆分。原 parent 的 $\gamma,K,m$ 球
不因子片而免费收窄；两个轴线性投影从原 exact dyadic cubic 完整计算，
保独立 mean 及 $4\cdot10^{-18}$ 修补。

在子片 $[l,r]$ 取 $x_-=\max(0,l-r_*^{hi})$，
$z_+=\max(0,1-x_-/\ell)$。两个非负幂分别用 $z_+^2,z_+^4$，
所有其他量按完整 Arb 区间运算取 upper，再乘真实子片长度。
多出的根下方/末端 padding 只增加非负费用；不把 padding 当真实正区。
原 whole 输入、根位置、mean、3594接口全部保持，所有旧科学目标调用为零。

只输出新完整 $T_2$、(QP.9)测试球及其明确比较，数组不发布。
完整 false 与真正未完成前缀分开保留。任何结果都不等于本课题完成。
