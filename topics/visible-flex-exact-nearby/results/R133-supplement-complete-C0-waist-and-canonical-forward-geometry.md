# R133：完整 C0 腰见证与从共同腰规范出发的全区间几何比较

2026-11-14，visible-exact-astra-ac0d。

**已证明的条件性定理；下述全部数值常数已实际计算。** 本篇直接将完整
物理状态的 $C^0$ 误差转成腰位移误差，包含未知均值与无限角频率；无需另给
一个 Wiener 腰球。再将已成7722盒的连接差系数按正向积分，得到以共同腰
规范为起点的位置比较。准确原候选、$\eta=\eta_0$、原 $\nu$ 及其
$10^{-5}$ 邻域，与[完整状态几何比较](R133-supplement-complete-C0-state-and-nu-geometry-response.md)
相同。

若完整状态差为 $\epsilon\le10^{-3}$，则准确腰法向位移见证满足

$$
 |\Delta-\Delta_c|
 \le 2\bigl(\sec(\pi/8)-1\bigr)\epsilon
 <.164785\epsilon.                                      \tag{W.1}
$$

对于下文定义的同一共同腰规范径向模型，令 $t=|\widetilde\nu-\nu|\le10^{-5}$，
则整个 $0\le r\le25/8$ 上

$$
 \boxed{\begin{aligned}
 \|\widetilde Q-Q^{\rm can}\|_{C^0,\rm op}
   &\le15.736315\epsilon+.304809t,\\
 \|\widetilde F-F^{\rm can}\|_{C^0}
   &\le7.578231\epsilon+.612629t.
 \end{aligned}}                                         \tag{W.2}
$$

这里 $F^{\rm can}$ 是从准确候选腰支撑函数及标准腰标架生成的辅助模型。
它与已经保存的外端锚定模型 $F^R$ 不同；两者的准确腰对齐费在第5节中
明确保留。本文不证明真实解存在、校正已经在该球内、闭合或平帽已经成立。

## 1. 全周期的准确支撑函数核

记四重周期 $L=\pi/2$。在 $0\le s\le L$ 上定义

$$
 G_L(s)={L\over2\sin(L/2)}\cos(s-L/2),
 \qquad G_L(s+L)=G_L(s).                                \tag{W.3}
$$

端点的函数值相等，且 $G_L'(0+)=L/2$、$G_L'(L-)=-L/2$。
因此分布意义下

$$
 (\partial_s^2+1)G_L=L\delta_0.
$$

卷积统一采用归一化测度 $L^{-1}ds$。任一完整连续 $L$ 周期函数 $v$
都有唯一的 $L$ 周期解

$$
 p=-G_L*v,\qquad p''+p=-v.                              \tag{W.4}
$$

唯一性来自齐次解 $a\cos s+b\sin s$ 在周期 $L$ 下只能为零。
分布解因右端连续而为 $C^2$；可先对光滑函数证明，再取一致逼近。
特别，(W.4) 不要求有限 Fourier 支撑，也不要求未知扰动零均值。

由于 $0<L<\pi$，核 $G_L$ 为正，且

$$
 {1\over L}\int_0^L G_L(s)\,ds=1,
 \qquad {1\over L}\int_0^L|G_L'(s)|\,ds
 ={1-\cos(L/2)\over\sin(L/2)}=\tan(L/4).                \tag{W.5}
$$

所以对于 $\|\widetilde v-v\|_\infty\le\epsilon$，其准确支撑函数满足

$$
 \|\widetilde p-p\|_\infty\le\epsilon,
 \qquad \|\widetilde p'-p'\|_\infty
       \le\tan(\pi/8)\epsilon=(\sqrt2-1)\epsilon.        \tag{W.6}
$$

设 $N_0=(\cos\phi,\sin\phi,0)$、$Y_0=(-\sin\phi,\cos\phi,0)$，定义
准确平面曲线 $F_0^{\rm can}(v)=pN_0+p'Y_0$。由两个向量正交，得到

$$
 \|F_0^{\rm can}(\widetilde v)-F_0^{\rm can}(v)\|_\infty
 \le\sqrt{1+\tan^2(\pi/8)}\epsilon
 =\sec(\pi/8)\epsilon.                                 \tag{W.7}
$$

只以 (W.6) 的两个分量上界求欧氏范数已经足够；本文不需要断言 (W.7)
是向量值算子的最优范数。

## 2. 腰法向差的完整 C0 估计

令 $a=L/4=\pi/8$、$c=L/(2\sin(L/2))$。对 $0\le s\le L/2=2a$，

$$
 G_L(s)-G_L(s+L/2)
   =c\bigl(\cos(s-2a)-\cos s\bigr)
   =2c\sin a\sin(s-a).                                 \tag{W.8}
$$

该核差在平移 $L/2$ 后变号。因而

$$
 \begin{aligned}
 {1\over L}\int_0^L|G_L(s)-G_L(s+L/2)|\,ds
 &= {8c\sin a(1-\cos a)\over L}\\
 &=2(\sec a-1).                                         \tag{W.9}
 \end{aligned}
$$

把 (W.4) 在 $0$ 和 $L/2$ 相减，再用 (W.9)，就得到 (W.1)。常数 mode
在核差中自动抵消；这是准确恒等式，未对 BVP 的未知 mean 作额外限制。
在反射偶类中 $p'(0)=p'(L/2)=0$，因为唯一解继承反射和周期。

当一个真实全闭解满足腰条件 $u(0,\phi)=0$、$\beta(0)=0$、$v<0$，且
其全域正支撑门已经成立时，原[腰与法向管定理](R133-supplement-waist-normal-offset-and-fifth-power-markers.md)
第2节从准确腰连接和平面简单闭曲线的转角推出 $m_0=-a_0$，随后得到
真实腰恰为 (W.4)、(W.7) 的标准曲线。本文只在这个完整闭合前提下将
$F_0^{\rm can}$ 认作真实腰；不先把 $m_0$ 的未知方程删除。

对于原候选的非零腰系数，已有准确有理计算给

$$
 \Delta_c=
 {464825964760589561753338576951713338585009044716676403114392150217956316046344897
  \over
  3583704934441768863733466278147929848916143102146718632271808446029554864095232000},
                                                               \tag{W.10}
$$

即 $0.12970542309253905343<\Delta_c<0.12970542309253905344$。
该值只取决于完整非零偶腰系数，故未知基态 mean 没有隐藏在所展示的小数中。
实际 Arb 计算得到

$$
 \begin{aligned}
 \sec(\pi/8)&<1.082392200293,\\
 2(\sec(\pi/8)-1)&<.164784400585,\\
 .12954063869195426549&<\Delta<.12987020749312384138
 \qquad(\epsilon\le10^{-3}).                             \tag{W.11}
 \end{aligned}
$$

特别，$0<\Delta<27/196$。只要同一最终精确闭面继续满足原腰定理的
全部几何与静态 marker 输入，向外法向管证明仍给
$\delta_{\rm hold}\ge\Delta$，并且在 $D\le511/200$ 时

$$
 {\delta_{\rm hold}\over D}
 >.05070083706143024089>.05.                             \tag{W.12}
$$

这条结论替换的只是原条件定理中的独立 Wiener 腰误差门。全域正支撑、
有向曲率、共同度量、真平盘、四个不同非共面的固定 marker 及全部闭合条件
仍须对同一精确解成立。这里只凭 $C^0$ 腰球没有证明这些条件。

## 3. 两个共同腰规范模型

用 $(u,v)$ 表示原准确候选的完整物理、未按振幅归一的 moving 状态；
它包含基态和 mean。用 $(\widetilde u,\widetilde v)$ 表示另一完整状态，设

$$
 \epsilon=\max\{\|\widetilde u-u\|_{C^0_{r,\phi}},
                  \|\widetilde v-v\|_{C^0_{r,\phi}}\},
 \quad \epsilon\le10^{-3},\quad
 t=|\widetilde\nu-\nu|\le10^{-5},\quad\eta=\eta_0.       \tag{W.13}
$$

连续修复相对原候选的差、全部未知高频和 mean、以及参数变化引起的完整
状态变化都计入 $\epsilon$。参数 $\eta$ 在此固定；不能将其他参数的改变
只记作 $t$ 或由宽输入盒直接转授。

在共同腰平面、中心、轴和反射角规范中，取标准 $N_0,Y_0$，另取与原径向
规范符号相容的同一常单位垂直向量 $X_0$。两模型的初始标架都设为
$Q_0=(X_0,Y_0,N_0)$。它与状态无关。初始位置分别取
$F_0^{\rm can}(v)$ 和 $F_0^{\rm can}(\widetilde v)$。

分别沿原完整 moving 标架方程生成 $(F^{\rm can},Q^{\rm can})$ 与
$(\widetilde F,\widetilde Q)$。对任意适当连续状态，这定义逐条径向模型；
只有在另一状态确实解全部 GC 方程、腰与闭合条件时，后一模型才是真正
浸入。原候选无需已经闭合，也无需其原 mean 准确等于 $-a_0$；这正是
必须把该辅助模型与原外锚定模型分开的原因。

## 4. 完整正向传播及实际7722盒积分

记 $Q'=Q\Omega$、$F'=Qf$。沿用已经证明并实际消费的局部上界

$$
 |f|\le L,\quad
 \|\widetilde\Omega-\Omega\|_{\rm op}
    \le L_{\Omega,u}\epsilon+L_{\Omega,\nu}t,\quad
 |\widetilde f-f|\le L_{f,u}\epsilon+L_{f,\nu}t.          \tag{W.14}
$$

这些系数保留了准确紧支度量变化、完整 primitive 与 mean 分母；详细
有限差分见完整状态比较定理 (C.5)--(C.15)。本次没有重新近似这些输入。
连接反对称、基本解正交，变分常数公式给

$$
 \|\widetilde Q(r)-Q^{\rm can}(r)\|_{\rm op}
 \le\epsilon\int_0^rL_{\Omega,u}(s)\,ds
       +t\int_0^rL_{\Omega,\nu}(s)\,ds.                  \tag{W.15}
$$

对位置使用
$\widetilde Q\widetilde f-Qf=(\widetilde Q-Q)f+
\widetilde Q(\widetilde f-f)$，再用 (W.7)，得到

$$
 \begin{aligned}
 |\widetilde F(r)-F^{\rm can}(r)|
 \le{}&\sec(\pi/8)\epsilon\\
 &+\epsilon\int_0^r\left[L(s)\int_0^sL_{\Omega,u}(x)\,dx
                               +L_{f,u}(s)\right]ds\\
 &+t\int_0^r\left[L(s)\int_0^sL_{\Omega,\nu}(x)\,dx
                               +L_{f,\nu}(s)\right]ds.
 \end{aligned}                                           \tag{W.16}
$$

所有 integrands 非负。按从 $0$ 到 $25/8$ 的准确7722盒次序，若某盒宽为
$h$，在进入该盒前的连接累计为 $O$、位置累计为 $P$，则对状态或参数列
分别更新

$$
 P\leftarrow P+hLO+\tfrac12h^2LL_\Omega+hL_f,
 \qquad O\leftarrow O+hL_\Omega.                         \tag{W.17}
$$

同盒三角积分面积准确为 $h^2/2$。每个 $L,L_\Omega,L_f$ 使用原生区间记录
的向外上端点，实际计算以256位 Arb 继续向外取整；没有把 float 展示值
当作上界。准确有理 cover 无 gap 或重叠，末端恰为 $25/8$。

| 完整累计量 | 向外严格上界 |
|---|---:|
| 状态到标架 $\int L_{\Omega,u}$ | $15.736314562$ |
| 参数到标架 $\int L_{\Omega,\nu}$ | $.304808091$ |
| 状态到位置的正向径向双积分 | $6.495838010$ |
| 参数到位置的正向径向双积分 | $.612628757$ |
| 原速度长度 $\int L$ | $1.950539012$ |
| 另加完整腰位置后的状态系数 | $7.578230211$ |

这证明 (W.2) 中稍放宽的十进制有理界。相同的局部系数从不同端点累计
产生不同的双积分常数；并未将原外锚模型的状态费用擅自换小。

## 5. 原外锚模型与共同腰模型之间的费用

设 $(F^R,Q^R)$ 是先前已定义的原外端锚定径向模型，在同一世界坐标中令

$$
 b_{F,0}=\sup_\phi|F^R(0,\phi)-F_0^{\rm can}(v)(\phi)|,
 \quad b_{Q,0}=\sup_\phi\|Q^R(0,\phi)-Q_0(\phi)\|_{\rm op}.
                                                               \tag{W.18}
$$

这两个全圆周量必须实际支付；它们不是自由指定为零的边界数据。由于
这两个参考模型使用完全相同的 $\Omega,f$，它们的标架差只是初值差右乘
一个正交矩阵。因此整个区间上

$$
 \begin{aligned}
 \|Q^R-Q^{\rm can}\|_{\rm op}&\le b_{Q,0},\\
 |F^R-F^{\rm can}|&\le b_{F,0}+1.950540b_{Q,0}.
 \end{aligned}                                           \tag{W.19}
$$

与 (W.2) 合并得

$$
 \boxed{\begin{aligned}
 \|\widetilde Q-Q^R\|_{\rm op}
  &\le b_{Q,0}+15.736315\epsilon+.304809t,\\
 |\widetilde F-F^R|
  &\le b_{F,0}+1.950540b_{Q,0}+7.578231\epsilon+.612629t.
 \end{aligned}}                                         \tag{W.20}
$$

之后若使用原保存的网格或插值模型，还须另加其已经证明的径向、角向
积分/插值误差。任何共同刚体坐标选择须具体固定；若改变世界原点，半径和
支撑计算也必须在同一原点下重付。本文只证明 (W.18)--(W.20) 的准确接线，
没有声称原外锚模型与标准腰已经一致。

## 6. 实际原生报告与可重建身份

源码为
`scripts/fourfold_codazzi_C0_waist_and_forward_geometry.py`，其 SHA256 为
`71f8f22e16340a9da950460d0cb5808f2c183d4310f2f0c884fb3a326a55f1de`。
原生报告为
`notes/2026-11-14-R133-complete-C0-waist-forward-geometry-native.json.gz`，SHA256
`86a3e4c75a1eac47a668f53830d3fc6b40b4d5453b8e32b8b7fb8d27951c72a8`。
实际进程正常返回0，报告时间6.778645413秒，全部9项 gate 通过，完整7722
个正向累计行保留。输入仅为已成完整状态/参数几何报告及原准确腰有理报告；
没有重跑候选、primitive、几何 ODE 或已经完成的数值门。

```bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/runtime-deps \
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python3 scripts/fourfold_codazzi_C0_waist_and_forward_geometry.py \
  --out notes/2026-11-14-R133-complete-C0-waist-forward-geometry-native.json.gz
```

源码拒绝覆盖已有原生报告；复核时应另选输出路径。完整文件及输入身份见
`notes/2026-11-14-R133-complete-C0-waist-forward-geometry-identities.json`。
当前仍须构造同一全频精确解、支付真实状态球、准确腰对齐与全闭面/平帽
输入；本篇没有达到课题的最终完成标准。
