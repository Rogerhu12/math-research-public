# 正确 Phi 的 f=u 支：t−2 与 u−ell Q 的真实原单位

日期：2026-11-28（Asia/Taipei）。会话 Astra-ISP-8542378f-20261127；GPT-6 Astra Pro（AI-assisted）。

**状态：下述原单位身份已证明。** 以下是直接由原 Gram 定义得到的纸面恒等式与整零支排除；不声称另有数值或脚本执行。

## 1. 范围

在当前 $D_{\mathrm{val}}\ne0$、非零孤立均值的正确 $\Phi=0$ 图，取 $f=u$。引用[正确整 t=0 排除](R150-appendix-unit211-Phi-zero-true-entire-tzero-original-exclusion.md)和[本支整 u=3/2 排除](R150-appendix-unit211-Phi-zero-fu-entire-u-three-half-original-exclusion.md)。于是
$$
bc\,Q\,\delta\,(u-1)(2u-3)L\ne0,
\qquad
\delta=1-Q,\quad L=\ell Q=Q-2(u-1)(u-2).
$$
这里没有倒置 u、旧错误头、一般 $2\ell-3$ 或任何新几何范数。

记
$$
\begin{gathered}
p=1+\rho,\quad q=1-\rho,\quad \rho^2=\delta,\qquad
m=u-\ell=(b-c)\rho,\quad a=1-\ell,\\
X=x+\rho y_0,\quad Y=x-\rho y_0,\qquad
V=bX+cY=\ell x+my_0,\\
W=bpX+cqY=ux+\theta y_0,\qquad
\theta=u-\ell Q.
\end{gathered}
$$
$y_0$ 是 singleton 均值的奇坐标，不是前篇单参数 $y=4(u-1)^2-Q+2L\lambda$。

## 2. 正确 germ 均值只给一个实际线性式

原 $E_0=0$ 在 $f=u$ 上给
$$
2W=T_0+4u^2,\qquad T_0=2u-\ell Q-2u^2.
\tag{1}
$$
令 $z=Qt,\ v_n=QV,\ n_n=2Q(W-V)$。正确紧凑 germ 组合是
$$
R=bc\,z^2+z(4bcuQ-\ell v_n)
      +\frac{m}{2\delta}z n_n.
$$
由 $4bc\delta=\ell(2u-\ell Q)-u^2$ 和
$\theta=\ell\delta+m$，逐项整理得
$$
\boxed{R=bc\,Q^2t(t+4u-4x).}
\tag{2}
$$
这是正确的 $E_1-bE_B-cE_C$ 原组合；不使用被撤回的错误 germ 平方。因 $bcQt$ 已付，原点上
$$
x=u+\frac t4.
\tag{3}
$$
把 (3) 代回 (1)，并写
$$
v=t-2,\qquad \xi=y_0-\frac12,
$$
得到完整线性关系
$$
\boxed{H:=4\theta\xi+uv=0.}
\tag{4}
$$

## 3. 原 odd mean 的短恒等式

原 Gram 的 B 行为 $(p,r,0,t)$，其中
$r=X-ap-ct$。在 $f=u$ 时，第一 germ 均值
$d_1=(1+\ell)u-V$，且 $F_2=2u$。依照真实双数乘法直接展开 B 均值：
$$
E_B=-ap^2+(2p+2u)X-2p d_1
+c\,t(t+2u-2p-2Y)-2X^2.
\tag{5}
$$
C 行是 $\rho\mapsto-\rho$ 的共轭。因此
$E_{\mathrm{Bo}}=(E_B-E_C)/(2\rho)$ 是 (5) 的奇系数。使用 (3)，先整理为
$$
E_{\mathrm{Bo}}
=-a+\frac{av}{2}-av y_0
-\frac{m v^2}{4\delta}+\frac m\delta.
$$
正确 Phi 恒等式 $aQ=2(u-1)(u-2)$ 给
$$
m-a\delta=(u-1)(2u-3)=:r_0.
$$
所以
$$
\boxed{\delta E_{\mathrm{Bo}}
=r_0-a\delta v\xi-\frac m4v^2.}
\tag{6}
$$
式 (5)–(6) 保留全部原项；没有以旧紧凑 E1 代替原 Gram。

## 4. 两个完整零支排除及原逆式

令
$$
B_0=a\delta\xi+\frac m4v.
$$
式 (6) 等价于
$$
r_0=\delta E_{\mathrm{Bo}}+vB_0.
\tag{7}
$$
$r_0$ 是本支已付单位。因此原点不可能有 $v=0$，并在原商中有
$$
\boxed{(t-2)^{-1}=B_0/r_0.}
\tag{8}
$$
这是整 $t=2$ 支的原均值排除。

再由 $u=L+\theta$，式 (4) 给
$$
H=L v+\theta(v+4\xi).
$$
利用已付 L，式 (7) 可完全清楚地写成
$$
r_0=\delta E_{\mathrm{Bo}}+\frac{B_0}{L}H
-\theta\,\frac{(v+4\xi)B_0}{L}.
\tag{9}
$$
故在原商中
$$
\boxed{\theta^{-1}
=-\frac{(v+4\xi)B_0}{Lr_0}.}
\tag{10}
$$
这排除了整 $\theta=u-\ell Q=0$ 权支，不需要倒置 u；即使 u 本身为零，也由同一身份覆盖。

以上身份在已付原 $E_0$ 和正确 R 的商中成立，而这两条本来属于原均值理想，故 (8)、(10) 是该原局部商的真实逆式。也可以仅按 (7)、(9) 理解为完整复点零支排除。

## 5. 使用边界

新结论只是在正确 Phi 的 f=u 当前物理图中支付
$$
(t-2)(u-\ell Q)\ne0.
$$
它不排空整个 f=u 支，不改变前篇 $\Psi(u,Q)=0$ 的全部零纤维，更不把固定权处 y 的纤维自动变成有限。新增单位可用于下一真正原输入；已经冻结的单 y/cofactor、十二坐标新源均保持原字节和执行身份。
