# 原负五矩的完整 Katz 点及反射根数

日期：2026-11-14。状态：R540 全权公式的直接推论。

本 note 固定 R599、R605 所用的原
$$
I_1=\int_{\mathbf Z_p^\times}x^{-5}\,d\nu_{f_1,17}(x),
\qquad f_{1,b}=-x_{\wp,b}y_{\wp,b}\sigma_b^6.
$$
它是负五矩，不能替换成同一来源的正一次单位矩。

## 1. 同一 norm-weight-one 点

沿用 [R540](../results/R540-original-degree-six-schwartz-full-weight-and-negative-two-katz.md)
的基曲线 $E_0:y^2=x^3+1$、完整有限角色 $\xi$、基 Hecke 角色
$\psi_0$、primitive 导子 $(6)$、Katz 晶格周期和 Artin 规范。
令 $d=p-1$。该篇的完整权族是
$$
\nu_m=\xi\psi_0^{m+1}\bar\psi_0^{-m},
$$
所以原负五点准确是
$$
\boxed{\nu_{-5}=\xi\psi_0^{-4}\bar\psi_0^5.}
\tag{1}
$$
这里不能把全权 $2m+1=-9$ 误写成 (1) 的 $\psi_0$ 指数。

在同一个 tame 指数 $-5$ 上定义
$$
J_{1,-5,0}(u)=\int_{\mathbf Z_p^\times}
x^{-5}\langle x\rangle^{du}\,d\nu_{f_1,0}(x).
$$
令 $\mathcal K_{1,-5,p}(u)$ 是 R540 的同一实际 Katz 分支
$m=-5+du$。R540(46) 沿合法权 $m\equiv1\bmod6$ 的密集正权极限，
以及同篇已付的解析恒等，直接给
$$
\boxed{
\mathcal K_{1,-5,p}(u)=
6^5c_1\Omega_{p,0}\langle6\rangle^{-du}
J_{1,-5,0}(u)^2 .
}
\tag{2}
$$
$c_1$ 正是 R540(36)–(37) 已完整确定的固定非零代数常数。
两个普通 Euler、二三处分歧及原平滑规范均继承该完整公式；
没有为负五点另取一个未说明比例。

特别
$$
\boxed{
\nu_{-5}(\mathcal L_{(6)}^{\rm prim})
=6^5c_1\Omega_{p,0}
 \left(\int_{\mathbf Z_p^\times}x^{-5}d\nu_{f_1,0}\right)^2 .
}
\tag{3}
$$

## 2. 返回原 b=17 的全部尺度

令 $\theta=17^{1/6}$，取 R540 固定的原普通嵌入。
其真实微分和 Amice 规范给
$$
\Omega_{p,0}=\theta\Omega_p,\qquad
f_{1,17}(z)=\theta^{-1}f_{1,0}(\theta z),\qquad
\nu_{f_1,0}=\theta\,\nu_{f_1,17}.
$$
最后一式是在同一个 $\mathbf Z_p$ 物理变量上的测度标量，
不是以 $\theta$ 乘该变量的 push。
因此负五矩也只乘 $\theta$，没有额外 $\theta^{-5}$。

原结果准确为
$$
\boxed{
\mathcal K_{1,-5,p}(u)=
6^5c_1\theta^3\Omega_p\langle6\rangle^{-du}
J_{1,-5,17}(u)^2,
}
\tag{4}
$$
$$
\boxed{
\nu_{-5}(\mathcal L_{(6)}^{\rm prim})
=6^5c_1\,17^{1/2}\Omega_p\,I_1^2.
}
\tag{5}
$$
若以后需要前因子在全部研究素数为单位，还须保
$c_1$ 的固定有限坏集；“固定非零代数数”本身不等于处处单位。

## 3. 真正的裸反射仍是负根数

(1) 的裸复共轭为
$$
\boxed{
\nu_{-5}^c=\xi^{-1}\psi_0^5\bar\psi_0^{-4}
         =\xi^{-1}\psi_0^9\mathrm N^{-4}.
}
\tag{6}
$$
故其反射复中心是 $L(\xi^{-1}\psi_0^9,5)$。

置 $\vartheta=\psi_0\mathrm N^{-1/2}$。
比较 $\xi\vartheta^{-9}$ 与 $\xi\vartheta^3$：
幂差为 $-12$，所以 R540 已列出的二、三处完整有限角色相同，
包含 uniformizer 值而不只包含单位角色。
其他有限处的角色未分歧、标准加性角色未分歧，epsilon 因子为一。
无穷处绝对角权九和三给准确 epsilon 比
$$
i^{9-3}=-1.
$$
R540 的 $f_1$ 正一次首权已证明
$L(\xi\psi_0^3,2)>0$，故 $\xi\vartheta^3$ 的中心根数为 $+1$。
由此
$$
\boxed{
W(\xi\vartheta^{-9})=
W(\xi^{-1}\vartheta^9)=-1,\qquad
L(\xi^{-1}\psi_0^9,5)=0 .
}
\tag{7}
$$
两个 unitary $L$ 函数的相同由理想复共轭换元得到，
同时保 $\xi^c=\xi^{-1}$、$\vartheta^c=\vartheta^{-1}$。

同 CM-type 的 Katz involution 是
$\nu\mapsto\mathrm N(\nu^c)^{-1}$。
因为 $\nu_{-5}\nu_{-5}^c=\mathrm N$，它逐点固定 (1)，
没有把 (1) 送到 R540 已知非零的正一次点。
裸复共轭则交换两个普通位置，不能省略这个局部变化。

(5) 只支付原负五行的准确算术身份，未证明 $I_1\ne0$。
[固定 CM 多项式单位密度引理](2026-11-14-fixed-cm-polynomial-unit-density.md)
也不能应用到 (5) 的 Katz 值或 $I_1$：
它们没有被识别成固定 $F(\bar\pi_0)$。
R605 的完整余补域和其全部原中央项继续保留。
