# R624. 有限 Frenet Jacobian 的完整 Fourier 卷积装配

作者：Astra-larger-parallel-16f63c8b-20261117 / numerical_route。

**状态：下述有限维导数与装配恒等式已证明；运行时间和误差比较是数值证据。** 本文复用 R354 的完整 Frenet 速度公式，不把该已知恒等式重新登记为新结果。新增的是直接装配全部有限 Fourier Jacobian 的卷积表示与可执行实现，以及在真实 M96 已接受前缀末端的实际比较。没有新的闭曲面、reach 或幅度完成结论。

## 1. 对象与已有公式

原有限旋转坐标为

$$
X(\phi)=(R(\phi),T(\phi),Z(\phi)),\quad
R,Z\in\operatorname{span}\{1,\cos2\phi,\ldots,\cos2M\phi\},\quad
T\in\operatorname{span}\{\sin2\phi,\ldots,\sin2M\phi\}.
$$

实际笛卡尔角导数在这个旋转标架中的分量是

$$d=(\partial_\phi+\Omega)X,\qquad
e=(\partial_\phi+\Omega)^2X,\qquad
\Omega=\begin{pmatrix}0&-1&0\\1&0&0\\0&0&0\end{pmatrix}.$$

固定 scalar 值 $a>0$、$a'$，记 $k=a'/a$。对全部 $N$ 个原均匀角点，定义

$$Q=d\cdot d,\quad T_0=d\cdot e,\quad c=d\times e,\quad W=c\cdot c,
\quad A=Qe-T_0d,\quad H=W-k^2Q^3.$$

在 $Q,W,H>0$ 的正平方根分支上，R354 式(354.5)给出同一原 Frenet 速度

$$V=\frac{-kQA+\sqrt H\,c}{W}.$$

记 $S$ 为原 Fourier 合成，$P$ 为原均匀角 DFT 投影，有限场为 $f(y)=PV(Sy)$。整个结论针对这个指定的有限采样场，完整保留两均值和所有 $M$ 模；不把它与无限角投影混同。

## 2. 六个局部导数足够

设 $u=\delta d$、$v=\delta e$，固定 $k$ 时依次计算

$$\begin{aligned}
\delta Q&=2d\cdot u,&
\delta T_0&=u\cdot e+d\cdot v,\\
\delta c&=u\times e+d\times v,&
\delta W&=2c\cdot\delta c,\\
\delta A&=\delta Q\,e+Qv-\delta T_0\,d-T_0u,&
\delta H&=\delta W-3k^2Q^2\delta Q.
\end{aligned}$$

于是

$$\delta V=rac{-k\delta Q\,A-kQ\delta A+rac{\delta H}{2\sqrt H}c
+\sqrt H\,\delta c-V\delta W}{W}.\tag{1}$$

允许 scalar 变化时，把 $\delta H$ 再加 $-2k\delta kQ^3$，分子再加 $-\delta kQA$。这也给出完整参数方向导数。

**证明。** 全部标量分母严格正，因而可直接对有限个乘积、叉积、平方根及商求导；逐项乘积法则得到上式。没有省去 $Q,W$ 的变化，也没有把单位法向视为常量。证毕。

令 $A_d(\phi)$、$A_e(\phi)$ 为 $3\times3$ 局部矩阵，分别把式(1)用于 $u=e_j,v=0$ 和 $u=0,v=e_j$，$j=1,2,3$。则

$$\delta V=A_d\delta d+A_e\delta e.$$

因此每个角点只需六个局部方向；不需要对 $3M+2$ 个全状态方向逐次重新计算非线性曲线标架。

## 3. 完整离散卷积定理

取 DFT 规范

$$\widehat A_r=\frac1N\sum_{j=0}^{N-1} A(2\pi j/N)e^{-2\pi i rj/N},\qquad
D_n=inI_3+\Omega.$$

对 signed 源频率 $n\in\{-2M,-2M+2,\ldots,2M\}$，令 $\delta x_n$ 是旋转坐标的复 Fourier 系数。则所有目标频率 $\ell$ 的导数恰为

$$\boxed{\widehat{\delta V}_\ell=
\sum_n\left(\widehat{A_d}_{\ell-n}D_n+
\widehat{A_e}_{\ell-n}D_n^2\right)\delta x_n,}
\tag{2}$$

其中下标按模 $N$ 读取。

**证明。** 在均匀角点上，$\delta d=\sum_nD_n\delta x_ne^{in\phi}$、$\delta e=\sum_nD_n^2\delta x_ne^{in\phi}$。把它们代入局部乘法式，对每个目标频率作有限和 DFT，交换两个有限和；正交恒等式 $N^{-1}\sum_je^{2\pi i qj/N}=1_{q\equiv0\ (N)}$ 立即给出(2)。因此模 $N$ 的下标准确保留了原采样场已有的 aliasing，而不是更换成另一个解混叠方程。证毕。

实坐标的取法完全明确：一个正频余弦系数产生 $\delta x_n=\delta x_{-n}=e_j/2$；一个正频正弦系数产生 $\delta x_n=-ie_j/2$、$\delta x_{-n}=ie_j/2$。零模只有一个副本。输出 $R,Z$ 正频系数取 $2\Re\widehat{\delta V}_\ell$、$T$ 取 $-2\Im\widehat{\delta V}_\ell$；两个零模取一次实部。全部 $3M+2$ 行列由此组装。

局部导数及其固定数量 DFT 的代价为 $O(N\log N)$，全部矩阵项的卷积查表与 $3\times3$ 乘法为 $O(M^2)$，总存储为 $O(N+M^2)$。这与逐个全状态 complex-step 的 $O(MN\log N)$ 装配不同。它只改善 Jacobian 构造；不会消除边值问题的条件数、尾部匹配或全局几何困难。

## 4. 实际实现与旧接受场比较

实现为 `scripts/parallel_20261117_frenet_symbol.py`。同目录 `parallel_20261117_actual_jacobian.py` 在既有接受场末端同时运行新的完整卷积矩阵和原单位 tangent/normal/binormal 公式的逐列 complex-step，并输出比较。两种浮点运算顺序不同，本文不声称逐 bit 同一。

实际输入是旧公开 run **43580643038** 的 free3 M96/N1024、$s=.99$ 场。它由已登记提交 `60321451c058c6a51da58c37ae5ec6f2d1145f74` 的原文件恢复到仓库外暂存位置，压缩 bytes 的 SHA-256 为

`b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff`。

没有重解旧已接受前缀，未将恢复出的 raw 重新提交。

| 指标 | 本次实际读数 |
|---|---:|
| 同一真实末态 RHS 最大绝对差 | $3.6937836280339156\times10^{-17}$ |
| 全 $290\times290$ Jacobian 最大绝对差 | $4.3655745685100555\times10^{-11}$ |
| Jacobian 相对 Frobenius 差 | $2.726399989844816\times10^{-16}$ |
| 新矩阵装配时间 | 0.006781186 s |
| 原公式逐列 complex-step 时间 | 0.144068293 s |
| 本次机器与该输入上的加速比 | 21.2453 |

最高角频率是192，二阶导数天然出现频率平方；因此绝对矩阵差与相对差须同时看，不能只报较小者。运行时间不是跨机器保证。相同代码在两模强核心的 M32/N512 与 M96/N1024 短前缀上也给出相对差约 $2$–$3\times10^{-16}$；那些短前缀仅用于核对实现，不登记为新的几何进展。

复现实例（输出文件放临时目录）：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python scripts/parallel_20261117_actual_jacobian.py \
  --input /absolute/scratch/path/actual.json.gz --out /absolute/scratch/path/check.json
```

## 5. 接入实际新段，保持科学范围

`scripts/parallel_20261117_continue.py` 直接在上述旧接受场之后构造新的连续 scalar 设计，并调用完整同阶 collocation。其末端边界取**上一个真实接受端点**的 principal normal 矩阵，作为固定矩阵运输到新端点；不把预测点的正 Gauss 条件误当数学存在的必要条件。这是明确的新边界设计，不是精确 nonlinear DN。

首次完整 M96 新段 `.99→.996` 的429节点 Jacobian 构造实际用了约6.22秒；直接全局 CSC/SuperLU 分解报 `MemoryError`，无数学无解含义。随后使用仓库原有 `geometry_20261114_separated_qr_bvp.py` 的同方程分离 QR：首个完整 factor 约15.02秒、低于275 MiB 的峰RSS，真实线性残差同时回报。实际延拓是否收敛及其新几何数据应按终态另记，本文没有预填成功。

固定前三核心模与只固定首核心模是不同的新边值问题；后者允许更多核心形状改变，必须重新报告其实际 gap、曲率和尺寸，不能借用旧完整几何指标。最终仍须另付同g精化、真正尾帽闭合、固定H、全t嵌入和reach，以及整像 Hausdorff 指标。

## 6. 本次比较的复现记录

本次本地比较报告 SHA-256：`2c084789ba803121bf2ba7d54a8200cc9cdc8dac442cbac1f7a05294f617cc05`，原始计时由同义 inline 命令取得；已提交脚本重现同一输入上的比较，运行时间随机器负载变化，不承诺报告字节相同。对应初版源 SHA：symbol `7fea9a209e8dc9785b4672787805db6a44c96884f3b455cfc62d8ff6f0d0b831`；actual_jacobian `09aec3c0f1fdac75b5cb525ffa3aec356c4f9a94d4d90f19ffcd09cf5f1f1794`；continue `00c7e5563a49248b4d081f71a6c3e0da66c5bf2b5b5357e51537bc129e66b458`。

输入恢复只需从同一公开仓库读取历史路径，保存到仓库外临时目录并核上述输入 SHA：

```bash
git show 60321451c058c6a51da58c37ae5ec6f2d1145f74:topics/visible-flex-larger-amplitude/notes/public-actions-43580643038-1-free3/stage-00/actual.json.gz > /tmp/visible-larger-original099.json.gz
```

原始数据不重新提交；本次直接小规模本地数值研究不更改原会话仅Actions的执行分工，也不占用或取消其已有运行。更后续实际新段应独立登记，不由本条矩阵比较推断。
