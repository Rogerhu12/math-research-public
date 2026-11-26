# R149 TM：原 graph-model adjoint 对完整有限 Theta 行的作用

**已证明。** 会话 `visible-exact-astra-fb31ed6-20261127`，2026-11-27。

本条只把原 [WFI](R133-supplement-graph-domains-and-finite-index-ledger-for-the-reflected-waist-row.md)
的 $\overline G$ 接到完整有限行。它保持 WFI 的低频 reference、
原 $a,b,\Omega,\mu$，不重做 CYA 的旧 gap 计算。

## TM1. 真正目标 Hilbert 空间和原低频定义

采用 WFI.1、7 的完整 normalized real bases

$$
 u_n^b=\sqrt2\cos(4nx-2nb-\pi/4)\in X_b^0,
 \qquad v_n^a=\sqrt2\cos(4nx-2na)\in Y_a^0,
 \quad n\ge1.
 \tag{TM.1}
$$

两空间均为原 mean-zero reflected 子空间，继承 normalized $L^2$
norm；$b=a+\Omega$，$a=2\mathcal H(0)$，不把相位置零。
原 root-even $e_j=\sqrt2\cos4jx$ 仍是96条输出坐标的基。

由 WFI.8–15，$\nu=-\mu/2$ 是同一 first-coefficient mean，并且

$$
 \overline G v_n^a=\gamma_nu_n^b,
 \qquad
 \gamma_n=\begin{cases}
 1,&1\le n\le96,\\[1mm]
 \displaystyle{1\over\cos\theta_n-(\nu/(4n))\sin\theta_n},&n\ge97,
 \end{cases}
 \quad\theta_n=2n\Omega+\pi/4.
 \tag{TM.2}
$$

低频的1来自 $L_{low}u_n^b=v_n^a$，绝不能换成未经验证的低频
$M_\nu$ reciprocal。它也不是实际 physical low column。

完整 [CYA](R133-supplement-actual-finite-Cayley-scalar-gap-and-selected-inverse.md)
run43757868884/1 已给 $K_{CY}=256$，含原 finite box 和其独立
native infinite scope。WCS.13 及 WFI.15 因此给

$$
 \|\overline G:Y_a^0\longrightarrow X_b^{-1}\|
 \le \max(1,2K_{CY})=512.
 \tag{TM.3}
$$

这是对已成 exact rational 常数的解析后果，没有计算新 gap 或
重新枚举7416个旧 label/root pairs。需要实际有向除法时计算的
signed $\gamma_n$ 是本次有限 row carrier 的新作用，不是旧距离目标。
完整旧 CYA actual、其 whole mean interval 和同一 selected-family
identification 仍须由后继 owner 准入。

## TM2. 一个有限实行的全 model action

设 $\widehat r_j$ 是从同一完整 IR trial 和同一完整 AS
$\widehat\alpha$ 形成的原 DT 行

$$
 \widehat r_j=(Id+I\mathcal T_{\widehat\alpha})G\widehat z_j,
 \quad G=|D_x|^{-1},\qquad
 \widehat r_j(x)=\sum_{0<|n|\le R}p_{j,n}e^{4inx},
 \quad p_{j,-n}=\overline{p_{j,n}},
 \tag{TM.4}
$$

其中所有同号卷积 outputs 已保留，$R=M+K=192+2048=2240$。
这不是把完整 $M_\alpha$ 与 same-sign Toeplitz 混用；也没有将输入
的负频卷进正输出 block。

实际 pairing 的两符号 Parseval 给

$$
 \langle\widehat r_j,u_n^b\rangle
   =\sqrt2\operatorname{Re}\{p_{j,n}e^{i(2nb+\pi/4)}\}.
 \tag{TM.5}
$$

因此 $\widehat V_Q\overline G:Y_a^0\to\mathbb R^{96}$ 的完整
有限 signed coefficient rows 为

$$
 \boxed{\tau_{j,n}=\gamma_n\sqrt2\operatorname{Re}
     \{p_{j,n}e^{i(2nb+\pi/4)}\}},
 \quad1\le n\le2240,\qquad \tau_{j,n}=0\ (n>2240).
 \tag{TM.6}
$$

这里 $\widehat V_Q f=(\langle\widehat r_j,f\rangle)_{j=1}^{96}$。
model 保留每个原 $\pm n$ reflection block，故有限 support 在
TM.6 后没有扩展，也没有被漏掉的 model Fourier tail。

若 $p_{j,n}$ 由 directed finite arithmetic 给整球，直接使用原
$b$ 和 $\mu$ 的完整球，TM.6 给 $\tau_{j,n}$ 的整实球。相位和
mean 的相关性可以保留，或安全地放大成包含它们的笛卡尔 box；
不能用中心代替真实值后省去此误差。实际 $a$ 还保留在目标基
$v_n^a$ 中，没有另设一个独立近似 target reflection。

## TM3. 确定 trial 和完整 operator error

任选整个 row ball array 的 exact-dyadic centers
$\widehat\tau_{j,n}$，并为每一项保完整误差
$|\tau_{j,n}-\widehat\tau_{j,n}|\le\eta_{j,n}$。在同一真实
orthonormal $v_n^a$ basis 中定义

$$
 \widehat\Theta y
   =\left(\sum_{n=1}^{2240}\widehat\tau_{j,n}
                                      \langle v_n^a,y\rangle\right)_{j=1}^{96}.
 \tag{TM.7}
$$

此 definition 不需要把未知真实 $a$ 数值置零。它定义了同一真实
target Hilbert 空间中的有限坐标算子。有限 model-action error 满足

$$
 E_{model}:=\left(\sum_{j=1}^{96}\sum_{n=1}^{2240}
                              \eta_{j,n}^2\right)^{1/2}
 \ge\|\widehat V_Q\overline G-\widehat\Theta\|.
 \tag{TM.8}
$$

必须先形成并保存全部96条完整 row arrays，再从每个正式读回的
整 ball 计算此 sum。没有把不正交的原 approximate rows 当正交；
这里只用真正目标基的正交性和有限矩阵的 Hilbert–Schmidt upper。

设原 DT/DB 完整 one-loss joint error 给
$\|(V_Q-\widehat V_Q)\overline G\|\le E_{DT}$。则同一完整
算子的实际 trial error 为

$$
 \boxed{\|\Theta-\widehat\Theta:Y_a^0\to\mathbb R^{96}\|
                      \le E_{DT}+E_{model}},
 \qquad\Theta=V_Q\overline G.
 \tag{TM.9}
$$

不额外乘 $\sqrt{96}$。$E_{DT}$ 必须含全 IR residual、原 AS
coefficient error、old same-sign $A$ norm、原 DB regularity 和
TM.3 model loss；它不是仅在有限 frequencies 验证过的 residual。
如果使用 AS 的 $L^2$ error，须另付 finite-$G\widehat z$ product
bridge，不得直接将其冒充 $L^\infty$ error。

本条提供精确 model-adjoint 作用、low reference 和最后完整 rounding
error 公式。它不产生新 numerical entries，不证明 actual physical
low columns、two means、metric parameter/phase rows、full Schur 或
非线性嵌入族。后继只有在整 IR、AS、SDI、CYA actual inputs 到齐
后才可启动一次真正完整 signed $\Theta$ 行计算。
