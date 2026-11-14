# R192：有限解析末段的精确 metric 必要系数与可选限制坐标

**状态：已证明；有一次非零实际 V8 末段核。** 结论只针对 R187/R190 的固定有限 spline 场，在其末段采用所声明的精确解析 B32 brake，且要求完整角、完整径向上的 metric 准确相等。它不是一般 $C^2$ 等距问题的障碍，也不是当前有限求积目标的已证残差下界。当前主线 LM 不因本条自动改变。

## 1. 准确末段假设与实际有限布局

记切口为 $s=S$，$\tau=S-s$，切口半径 $a_c=4/5$。实际 B32 的最后物理段是两端相位导数都为零的 cubic phase bridge，长 $L_b=.026$，起始相位 $-1.45$，末相位准确为 $-\pi/2$。令 $D=\pi/2-1.45>0$，则在精确物理坐标中
$$
\varphi_b(S-\tau)=-\frac{\pi}{2}
+D\left(3\frac{\tau^2}{L_b^2}-2\frac{\tau^3}{L_b^3}\right).
$$
因此
$$
a_{{\rm base},s}=-1+O(\tau^4),\qquad
z_{{\rm base},s}=O(\tau^2),\qquad
a_{\rm base}=a_c+\tau+O(\tau^5).
$$
这里使用同一个准确 $S$ 和准确 endpoint phase 语义。机器数 $\pi$、分界舍入及实际浮点查询另有数值误差；不把这些字节当成上述解析恒等式的证明。

R189 记径向步长 $h=(S-c)/(J+3)$。当
$$
0<\tau<\min(h,L_b)
$$
时，仅最后一个径向基 $B_{J-1}$ 仍可非零，且
$$
B_{J-1}(S-\tau)=\frac{\tau^3}{6h^3}.
$$
记最后一行 theta 系数为 $t_k$，$1\le k\le K$，R190 的最后半径系数为 $\rho$。R187 没有半径设计块，在本文中取 $\rho=0$。

实际参考的 quintic step 满足 $1-\chi=O(\tau^3)$。其 $q=(1-\cos(\pi(1-\chi)))/2=O(\tau^6)$、$r=\sin(\pi(1-\chi))/2=O(\tau^3)$，从原完整单位切向参考的 atan2/asin 定义得
$$
\theta_0-u=O(\tau^6),\qquad \phi_0=O(\tau^3).
$$
所有大 $O$ 连同所需有限阶导数在本固定有限场、整个角域上一致；常数允许依赖其参数、$J,K$。于是存在光滑角函数 $g$，使
$$
\theta=u+\tau^3 f(u)+O(\tau^6),\qquad
f(u)=\frac1{6h^3}\sum_{k=1}^K t_k\sin(2ku),
$$
$$
\phi=\tau^3g(u)+O(\tau^4).
$$
高度修正与末高 step 的径向导数也都是 $O(\tau^2)$，故完整中心高度 $Z_s=O(\tau^2)$。

R190 的完整半径为
$$
a_\rho=a_c+\tau+\frac{\rho}{6h^3}\tau^3+O(\tau^5),\qquad
a_{\rho,s}=-1-\frac{\rho}{2h^3}\tau^2+O(\tau^4).
$$

## 2. 完整 primitive 的平面首项

记 $e_r=(\cos u,\sin u,0)$，$e_u=(-\sin u,\cos u,0)$。实际单位切向量是
$$
T=(-\sin\theta\cos\phi,\ \cos\theta\cos\phi,\ \sin\phi).
$$
代入上节展开，
$$
T=e_u+\tau^3[-f(u)e_r+g(u)e_3]+O(\tau^4).
$$
令 $\mathcal P$ 为 R187/R189 的完整 quarter primitive，包含其第三分量的完整一阶矩；于是
$$
Y=\mathcal PT=e_r+\tau^3[W_h(u)+W_z(u)e_3]+O(\tau^4).
$$
平面首项为 $W_h=\mathcal P_h[-f e_r]$。这里没有截断 $T$ 或 primitive 的 Fourier 模。

对单个角基，直接积分并取 $W_1(\pi/2)=0,W_2(0)=0$，得到
$$
V_k(u)=\mathcal P_h[-\sin(2ku)e_r]
=
\frac12\begin{pmatrix}
\frac{\cos((2k+1)u)}{2k+1}+\frac{\cos((2k-1)u)}{2k-1}\\
\frac{\sin((2k+1)u)}{2k+1}-\frac{\sin((2k-1)u)}{2k-1}
\end{pmatrix}.
$$
微分可直接核 $V_k'=-\sin(2ku)e_r$，且上述两个边值正确，所以确为同一个完整 primitive。三角恒等式给
$$
e_r\cdot V_k=\frac{2k}{4k^2-1}\cos(2ku),\qquad
e_u\cdot V_k=-\frac1{4k^2-1}\sin(2ku).
$$
故
$$
W_h=\frac1{6h^3}\sum_{k=1}^K t_kV_k.
$$
竖直首项和高度系数在以下 $\tau^2$ metric 项中不出现，因为基准 $X_s$ 的首项是水平的 $-e_r$。

## 3. 真实 metric 的准确 leading 项

真实图为 $X=a_\rho Y+Ze_3$。记 $r=\rho/(6h^3)$。由上式及解析微分，
$$
X_s=-e_r+\tau^2[-3r e_r-3a_cW_h+v(u)e_3]+O(\tau^3)
$$
其中 $v$ 不必显式求出。因为 $X_u=a_\rho T$，provider 所用的归一残差正是
$$
r_E=|X_s|^2-1,\qquad r_F=X_s\cdot T.
$$
因此
$$
\boxed{
r_E=\frac{\tau^2}{h^3}
\left[\rho+a_c\sum_{k=1}^K
\frac{2k\,t_k}{4k^2-1}\cos(2ku)\right]+O(\tau^3)
}
$$
以及
$$
\boxed{
r_F=\frac{a_c\tau^2}{2h^3}
\sum_{k=1}^K\frac{t_k}{4k^2-1}\sin(2ku)+O(\tau^3).
}
$$
这是完整 $X$ 的 metric 展开，不是形式二阶基本形式的 Gauss 方程展开。

**定理。** 如果这个固定有限解析场在某个完整末邻域准确满足 $r_E=r_F=0$，则
$$
\rho=0,\qquad t_1=\cdots=t_K=0.
$$

**证明。** 对 $r_E$ 的展开除以 $\tau^2$，令 $\tau\downarrow0$。常数与不同 $\cos(2ku)$ 在 $[0,\pi/2]$ 上正交，所以常数项给 $\rho=0$，各余弦项给所有 $t_k=0$。也可先由 $r_F$ 的 sine 正交性得全部 $t_k=0$，再用 $r_E$ 的平均得 $\rho=0$。每个乘子 $a_c,h,2k,4k^2-1$ 都非零。证毕。

必要条件不是充分条件。没有在本条消去最后 phi 行或高度行；它们仍参与更高阶和全域方程。

## 4. 连续能量首项及其范围

写 $A=\pi/2$，$\langle f\rangle=A^{-1}\int_0^A f(u)\,du$。同一正交关系给
$$
\left\langle r_E^2+2r_F^2\right\rangle
=C\,\tau^4+O(\tau^5),
$$
$$
C=\frac1{h^6}\left[
\rho^2+a_c^2\sum_{k=1}^K
\frac{8k^2+1}{4(4k^2-1)^2}\,t_k^2
\right].
$$
若某个所列系数非零，则 $C>0$。对该固定场存在足够小的 $\epsilon>0$，其连续末邻域残差不能恒零。目标面积权下还可写成
$$
\int_0^\epsilon\int_0^A
a_\rho(S-\tau)\,[r_E^2+2r_F^2]\,du\,d\tau
=\frac{Aa_cC}{5}\epsilon^5+O(\epsilon^6).
$$

这里的 $\epsilon$ 和余项常数依赖当前有限场。本条没有给所有优化参数、所有分辨率或某个现存 Gauss2 网格的统一正下界。实际采样残差很小不自动满足定理的“准确全邻域 metric”前提；当前最大误差在别处时，也不能据本条归因。

一般 $C^2$ 族不必具有这些三次 leading 项，可能有不同正则阶或边界层。因此定理不排一般 $C^2$ 解，不是新全局完成门，也不能把精确解必需的有限解析条件移给所有构造。

## 5. 可选坐标、明确新初猜与同场细化

独立模块 `scripts/fd2d_terminal_leading_metric_R192.cjs` 提供：

```javascript
const leading = terminalLeadingMetric(z, provider.definition, provider.base);
const restriction = createTerminalRestriction(provider.definition);

// 已满足零条件的完整场：
const free = restriction.reduce(z);
const full = restriction.expand(free);

// 非零旧场只能明确生成一个新初猜：
const proposal = restriction.zeroCopy(z);
// proposal.metadata 明记所改系数、是否改g、必须重算baseline；不作接受。

// 已真正求值的匹配完整 normal 可选取这些坐标：
const reducedNormal = restriction.selectNormal(fullNormal, full);
```

`reduce` 对被移除位置的非零值直接报错，不能静默丢掉旧参数。$\theta$ 清零改变图；$\rho$ 清零还改变物理 $g$。两者都保原中央/切口完整两 jet，但不能假称同一内部场。新全 F/normal 与实际 Armijo 仍由调用者原 provider 计算。模块不自动更改任何活动 LM、搜索域或已保存接受态。

限制坐标的 normal 是原列选择的严格主块：若 $Q$ 把自由向量补回移除位置为零，则
$$
J_{\rm free}=JQ,\quad H_{\rm free}=Q^THQ,\quad
g_{\rm free}=Q^Tg.
$$
原完整残差和平方范数不变；这要求 normal 已在传入的真实限制场求值，而不是把清零前 normal 当新场 normal。

R189 注入准确保持此子空间。新最后行只收到旧最后行的 $1/8$：
$$
t_k^+=t_k/8,\qquad \rho^+=\rho/8.
$$
新高角模为零。因此原零条件在任意多次同场径向/角向细化后仍准确为零，实际二进制零也保持。

反之，单纯同场细化不能消掉不满足条件的真实 leading metric：$h^+=h/2$，故 $t_k/h^3$ 和 $\rho/h^3$ 不变。必须区分场的表达加密与随后实际优化。

该必要子空间也没有制造新的 $C^2$ 表达障碍。将任意旧有限场准确细化 $\ell$ 次后，只把新的最后 theta/rho 系数清零，所改系数是旧值的 $2^{-3\ell}$，其支撑宽度是 $4h2^{-\ell}$。由
$$
\|B_3\|_\infty\le2/3,\quad
\|B_3'\|_\infty\le2/3,\quad
\|B_3''\|_\infty\le2
$$
得到径向 0、1、2 阶改变量分别为 $O(2^{-3\ell})$、$O(2^{-2\ell})$、$O(2^{-\ell})$。固定有限角阶下混合角导也趋零，因此新场在 $C^2$ 中逼近旧场。对 rho 的这种清零依然在每个有限阶改变 $g$，不能拿此纯稠密性说明冒充用户要求的固定 $g$ 实际收敛。

## 6. 一次实际有限核

实际 V8 检查使用完整冻结 R190 源与 B32 candidate、一个明确非零合成向量，31 ms 完成；未创建 OS 进程。仅取四个实际末端位置，每点保完整 quarter 角节点，未重跑 whole F/J/normal：

- $\tau/h=.08,.04,.02,.01$；
- 相对 leading $E$ 误差从 $.00108404$ 降至 $.0000237844$；
- 相对 leading $F$ 误差从 $.0134041$ 降至 $.00167464$；
- 实际角平均 $r_E/\tau^2$ 趋向解析系数 $-210.02047917537723$；
- 原数组保持；非零字段不能静默 reduce；
- 明确清零后的 reduce/expand 逐数相同，合成 normal 主块二次型/一次型差为 0；
- 193 维字段的可选自由坐标为 185 维；同场注入 865 维后，自由坐标 849 维，零子空间保持。

检查报告 `notes/2026-11-12-fd2d-R192-terminal-leading-v8-check-01.json` 保存全部公式系数、实际位置和新初猜变化元数据。该合成清零未做完整新 baseline，也未宣布被接受。主线当前 worst 不在切口，本工具作为明确可选接口保留，不替代主线实际误差定位。
