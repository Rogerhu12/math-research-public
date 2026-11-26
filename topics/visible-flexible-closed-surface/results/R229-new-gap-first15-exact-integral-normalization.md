# R229：前 15 格完整精确积分归一化：角逆、中心缩放与自身曲率

本条消费已登记 R227 的完整 native Gram 证书和 R228 的原场自身曲率证书；不重新登记它们。第三次临时环境丢失后的公开源重生，得到相同原件 master SHA，随后仅为新链重建两个报告。本文新增的是完整精确积分归一化的连续域预算。

## 实际结论及精确定义

在 R227 同一前 15 个 Fourier–quintic 格上，令原场为 $Y(s,\theta)$，$q=|Y_\theta|$，并取

$$
a=\frac1{2\pi}\int_0^{2\pi}q\,d\theta,\qquad
C=\frac1{2\pi a}\int_0^{2\pi}Yq\,d\theta,\qquad
\lambda=f/a.
$$

$A,B$ 是 master 中冻结的准确 dyadic 椭圆半轴，$\ell=(A^2\sin^2\theta+B^2\cos^2\theta)^{1/2}$，$a_\ell=(2\pi)^{-1}\int\ell$。本文取 $f(s)=a_\ell+vrJ((s-c)/r)$，即中央初值是准确椭圆周长半径，而非存储的浮点 $a_0$。R227 的目标参数盒包含这个准确选择。准确角逆定义为

$$
\int_0^{\theta(s,u)}q(s,\tau)\,d\tau=a(s)u,\qquad
X(s,u)=C(s)+\lambda(s)[Y(s,\theta(s,u))-C(s)].
$$

这是本条所证明的准确函数。它在准确中央柱上是恒等归一化，因此中央位置和两阶径向端迹保持。对其自身诱导度量，以 $ds^2+f(s)^2du^2$ 作相对谱范数，实际整数区间预算给出

$$
\|\widehat g-g_f\|_{g_f}
\le
\frac{325741373730009091869965}{79228162514264337593543950336}
<0.000004112.
$$

其自身主曲率绝对值最大值满足

$$
\max|\widehat\kappa_i|
\le
\frac{390909177807532976662469554099}{39614081257132168796771975168}
<9.868<\frac{1000}{97}.
$$

最坏的度量上界来自第 0 格，曲率上界来自第 8 格。上述量是全格、全角连续上界。保留所有保存 Fourier 系数；没有以有限点抽样代替连续证书。

本条没有认证字面上的有限求积/数值角逆 consumer；没有认证末端第 16 格的准确 coast 端口 repair；没有给出准确等距、全闭曲面、非局部 reach 或全时等距族。这里的小度量误差也不是准确等距论证。

## 角逆和中心缩放的完整导数

记 $b=(f/a_\ell)\ell$，$r_G=q^2-b^2$，$\omega=f_s/f$。令 R227 给出 $\varepsilon_j\ge|\partial_s^j r_G|$，$j=0,1,2$，以及 $\varepsilon_E\ge||Y_s|^2-1|$、$\varepsilon_F\ge|Y_s\cdot Y_\theta|$ 和相对谱误差 $\delta$。以下所有常数逐格取严格有理上界；向下界也作定向舍入。

取 $q_*>0$、$\Omega\ge|\omega|$、$\Omega_1\ge|\omega_s|$，使

$$
q_*^2\le B^2-\varepsilon_0,\quad
\Omega\ge v/a_{\ell,-},\quad
\Omega_1\ge \frac{v}{r a_{\ell,-}}\frac{630}{256}+\Omega^2.
$$

恒等式

$$
e:=q_s-\omega q
=\frac{(r_G)_s-2\omega r_G}{2q}
$$

给出

$$
\eta=\frac{\varepsilon_1+2\Omega\varepsilon_0}{2q_*}\ge|e|,
\qquad
\eta_1=
\frac{\varepsilon_2+2\Omega_1\varepsilon_0+2\Omega\varepsilon_1}{2q_*}
+\eta\left(\Omega+\frac{\eta}{q_*}\right)\ge|e_s|.
$$

令 $\rho=\varepsilon_0/(q_*+B)$、$a_*=a_{\ell,-}-\rho$，则 $|a-f|\le\rho$。设

$$
d=\rho/a_*,\qquad
\lambda_-=1-d,\qquad \lambda_+=1+d,
$$

$$
L_1=\lambda_+\eta/a_*,
\qquad
L_2=\lambda_+\left(2\eta^2/a_*^2+\Omega\eta/a_*+\eta_1/a_*\right).
$$

这些分别控制 $|\lambda-1|,|\lambda_s|,|\lambda_{ss}|$。其依据是 $a_s=\omega a+m$，$m=(2\pi)^{-1}\int e$，以及准确恒等式 $\lambda_s=-\lambda m/a$；没有遗漏半径随 $s$ 的变化。

由 R228 全 Cartesian 导数界取 $M_0\ge|Y|$、$M_{ss}\ge|Y_{ss}|$，并令 $M_1=(1+\varepsilon_E)^{1/2}$、$Q_0=2M_0$。加权中心是凸平均，因此 $|Y-C|\le Q_0$，且

$$
C_1=M_1+Q_0\eta/a_*\ge|C_s|,
$$

$$
C_2=M_{ss}+
\frac{2(M_1+C_1)\eta+\Omega Q_0\eta+Q_0\eta_1}{a_*}
\ge|C_{ss}|.
$$

这由 $\int(Y-C)q=0$ 微分两次得到；$\omega$ 项准确抵消后的剩余项已全部计入。

准确角逆满足

$$
W:=q\theta_s=um-\int_0^\theta e\,d\tau.
$$

将右侧写成
$-(1-u/(2\pi))\int_0^\theta e+(u/(2\pi))\int_\theta^{2\pi}e$，可得粗而完整的 $|W|\le2\pi\eta$。这里没有假设 $u=\theta$。进一步，

$$
|X_s-Y_s|
\le V:=d(M_1+C_1)+\lambda_+(2\pi\eta)+L_1Q_0.
$$

又 $X_u=fY_\theta/q$ 准确成立，所以

$$
G_X=f^2,\qquad
|E_X-1|\le\varepsilon_E+2M_1V+V^2=:\widehat\varepsilon_E,\qquad
|F_X|/f\le\varepsilon_F/q_*+V=:\widehat\varepsilon_F.
$$

相对误差矩阵的右下项为零，因此其谱范数不超过

$$
\frac{\widehat\varepsilon_E}{2}
+\sqrt{\frac{\widehat\varepsilon_E^2}{4}+\widehat\varepsilon_F^2}.
$$

这支付了完整 $s$ 依赖角逆。后续可用正确去均值 Fourier primitive 改善 $W$，但本条结论不依赖这个尚未完成的改善。

## 曲率是实际二阶扰动预算

角重参数不改变几何，先考察 $Z=C+\lambda(Y-C)$。令

$$
\sigma=\sqrt{1-\delta},\quad
\tau=(dC_1+L_1Q_0)/\lambda_-,\quad
\alpha=\tau/\sigma<1.
$$

准确关系 $Z_s=\lambda(Y_s+p)$、$|p|\le\tau$，$Z_\theta=\lambda Y_\theta$，给出

$$
g_Z\ge\lambda_-^2(1-\alpha)^2g_Y,\qquad
|\nu_Z-\nu_Y|\le2\alpha.
$$

后一估计来自同向法向量的标准归一化差界；$\alpha<1$ 保证不翻向。设 R228 给出 $M_{\theta\theta},M_{s\theta},M_\theta$ 及真实 $\kappa_Y$。取

$$
M_2=
\frac{\max(M_{ss},M_{\theta\theta}/B^2)+M_{s\theta}/B}{1-\delta},
$$

$$
R_{ss}=2L_1(M_1+C_1)+dC_2+L_2Q_0,\qquad
R_2=\frac{R_{ss}+L_1M_\theta/B}{1-\delta}.
$$

$M_2$ 控制以 $g_Y$ 单位切向量输入的环境二阶导数；$R_2$ 控制 $D^2Z-\lambda D^2Y$，包括混合导数项。于是对每个切方向的法曲率，再取最大值，

$$
|\kappa_Z|
\le
\frac{\lambda_+\kappa_Y+\lambda_+(2\alpha)M_2+R_2}
{\lambda_-^2(1-\alpha)^2}.
$$

这里没有用集合 Hausdorff 差代替曲率控制，也没有借用背景旋转面的曲率。

## 本次真实计算身份

入口脚本：$6a65$ 的 ramp normalization budget（下列精确 SHA 唯一标识本文版本），8321 bytes：

- `6a65-geometry-ramp-normalization-budget.py` SHA256 `b0326cd38b52484b8bd9a29b55fda976d7593aa630de46778f4050c9c5289482`。
- 同一 ramp master SHA256 `0e2865ed7fd2fa5e1061718cc96b8be691f5f7d1a5b9460cf11d564d799f38e7`。
- 本次仅供新链的 Gram 恢复报告 SHA256 `be0c2ad9610bc6a63edf1e6eced42f82a22fb8ed2c73f65412f017c14fb71d3e`，实际 exit 0，34.212475970 s。
- 本次仅供新链的 raw curvature 恢复报告 SHA256 `c8f43da932ec21d9925e358b1a025c1e38df067a4ed96e3384d9eeb6c53af48e`，实际 exit 0，30.378359633 s。
- 新归一化报告 `gap105-normalization-coarse01-report.json` SHA256 `b7e9c3e55432256e0bf8468490df92a7189d96690e6e31c2f16b6034dfb84931`。
- 新进程实际 exit 0，0.207634107 s；进程回执 `gap105-normalization-coarse01-report-process-receipt.json`。该回执中的 peakChildrenRSSKiB 40924 是顺序恢复父进程的累计子进程高水位，不能单独归给这次 0.208 s 预算。
- 新进程 log SHA256 `99010d5dc167b467a85732b4b26e8c996d62f783490b17e70b26dd80e12fe7bb`。

全部正性、平方根和最终门槛比较使用 96-bit 定向整数区间；显示小数仅供阅读。脚本还绑定两个源报告、master 和整数算术源码 SHA，要求完整有序 15 行。原件恢复不是新增研究结论；本条新增结论仅为上述准确归一化场的完整连续度量与曲率预算。

