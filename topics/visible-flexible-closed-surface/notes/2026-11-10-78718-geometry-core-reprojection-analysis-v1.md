# 同一实际 support core 的静态高模重新投影

日期：2026-11-10。作者：Astra-visible-flex-78718bd0 / geometric_closure。

**身份：有限数值诊断，外加各新投影表示的准确 dyadic 轴点。**
本稿不求解 BVP，不调用 tail，不改变任何正在运行或准备启动的候选。
它回答一个限定问题：主 M14 成功 CP 所确定的同一个平面 support core，
用原始入口回调的投影方式在不同表示阶数重新投影后，入口相对 $G$ 误差如何变化？
这与在保存的同一有限曲线上只补零、提高速度 RHS 的投影阶数不同。

## 1. 保持的是哪个 core

输入为主 M14 成功 CP：

`notes/2026-11-10-78718-numerical-m14-restart8000-02.json.gz`，SHA256
`4776c4c251c4bc6fdadda56aaed78f6fc02175483c5ad3a6fb3cf0359a49cd6a`。

其原入口 `WarpedBVP.initial` 从保存的全部14个参数生成 support
$$
h(\phi)=1+\sum_{j=1}^{14}c_j\cos(3j\phi),\qquad
\rho_c(\phi)=1+\sum_{j=1}^{14}(1-9j^2)c_j\cos(3j\phi).
\tag{1}
$$
材料弧长角满足
$$
u=A_c(\phi)=\phi+
\sum_{j=1}^{14}\frac{1-9j^2}{3j}c_j\sin(3j\phi).
\tag{2}
$$
固定计算角不是一般的 normal angle：
$$
u=u_{\rm ref}(\psi)=\psi-\frac{8q_{\rm ref}}3\sin(3\psi),
\qquad q_{\rm ref}=0.1.
\tag{3}
$$
每次求值由原 core 实现反解 $\phi=A_c^{-1}(u_{\rm ref}(\psi))$。
不把14项 core 简化为单一 $\cos3\phi$，也不假定 $\phi=\psi$。

脚本回放字面保存的参数向量，并逐位确认原 `pscale` 等于保存的
`central_correction_scales`。重新投影时不改变这些参数、不重新归一化它们，
也不引入第15个或更高的 support 未知量。14个实际 $c_j$ 在全部计算中不变；
其 little-endian f64 字节 SHA256 为
`fc09cc7849afd0fb2449206575e8d89fb807035291ae156bf8b5e737e7333844`。

归一化 gauge $q=0.1$ 与实际 support 主振幅
$0.09999976413887013$ 是不同的数。脚本保留原入口先除 gauge、以后再乘回
gauge 的浮点次序；没有将两者混同。

## 2. 重新投影的准确操作

设 $\gamma(u)$ 是上述固定 core 的精确定义，$e_r(u)$ 是未截断的圆背景，
$\Pi_{M,N}$ 是原 `CylindricalPrefix` 的 Cartesian 向量基采样投影。新表示是
$$
F_{M,N}(\psi)=e_r(u_{\rm ref}(\psi))
+q\,\mathcal B_M(\psi)
\left[\frac1q\Pi_{M,N}
\bigl(\gamma(u_{\rm ref}(\psi))-e_r(u_{\rm ref}(\psi))\bigr)\right].
\tag{4}
$$
这里以原回调相同的浮点实现计算方括号内系数。
采样数取 $N=2048,4096$，表示阶数取 $M=14,15,16,18,22,26$。
重建位置、一阶、二阶导数全部使用原始完整 Cartesian 基，包括基向量
随 $\psi$ 转动的导数。

在 $M=14,N=2048$ 时，新脚本与原始 `obj.initial(saved_p)` 的归一化
系数**逐位相同**，物理系数最大差为0。这验证所比较的是实际入口投影方法。
计算中 exact core 的单位弧长切向误差最大浮点观测为
$2.220446049250313\times10^{-16}$，只作为数值实现诊断。

以 $\varrho=u_{{\rm ref},\psi}$ 定义
$$
\Gamma_{M,N}(\psi)=\frac{|\partial_\psi F_{M,N}|^2}{\varrho^2}-1.
\tag{5}
$$
报告中的全角 FFT $\ell^1$ 是这份离散 $N$ 点值的 FFT 系数绝对值和。
它不是未经证明的连续 Fourier 尾界；两种采样数的一致性也不自动成为区间证书。

两轴 $\psi=0,\pi/3$ 可直接把投影后保存的每个 binary 系数解释为准确
dyadic 实数。设 $\sigma=\cos3\psi=\pm1$，原系数顺序给
$$
B_\sigma=Y_0+\sum_{j=1}^{M}\sigma^j(Y_{R,j}+3jY_{T,j}),\qquad
r_\sigma=\frac{qB_\sigma}{1-\sigma8q_{\rm ref}},\qquad
\Gamma_\sigma=r_\sigma(2+r_\sigma).
\tag{6}
$$
脚本用 `Fraction` 计算(6)，保留准确分数及与 $1/500000000$ 的严格比较。
这为各有限 binary 投影对象支付轴点值，不把生成投影的浮点求积升级成
精确 core 的连续误差证书。

## 3. 实际结果

下表取 $N=4096$；数值按已保存报告舍入显示。轴列是报告中准确分数的
浮点近似，全角列为上述采样 FFT 诊断。

| 表示阶数 $M$ | 全角 FFT $\ell^1(\Gamma)$ | $\Gamma(0)$ | $\Gamma(\pi/3)$ |
| --- | ---: | ---: | ---: |
| 14 | $1.3311424620\cdot10^{-8}$ | $-1.3311414154\cdot10^{-8}$ | $+5.0877035396\cdot10^{-11}$ |
| 15 | $9.3014983777\cdot10^{-9}$ | $-9.3014878591\cdot10^{-9}$ | $-3.9467033323\cdot10^{-10}$ |
| 16 | $4.5118190648\cdot10^{-9}$ | $-4.5118083618\cdot10^{-9}$ | $+1.3751627939\cdot10^{-10}$ |
| 18 | $1.3920742989\cdot10^{-9}$ | $-1.3920637545\cdot10^{-9}$ | $+4.4258245488\cdot10^{-11}$ |
| 22 | $1.3798323464\cdot10^{-10}$ | $-1.3788862219\cdot10^{-10}$ | $+4.1362786123\cdot10^{-12}$ |
| 26 | $1.8929342510\cdot10^{-11}$ | $-1.8627409352\cdot10^{-11}$ | $+4.7595278265\cdot10^{-13}$ |

两种 $N$ 的 FFT $\ell^1$ 结果绝对差，按相同 $M$ 顺序，约为
$1.34\cdot10^{-14},8.85\cdot10^{-15},5.87\cdot10^{-15},
2.98\cdot10^{-15},8.33\cdot10^{-16},4.83\cdot10^{-19}$。
完整报告同时保存位置、一阶、二阶 jet 的采样误差与两轴准确分数。

**所得限定结论：** 对当前同一 core，重新投影确实减少入口 metric 误差；
这不只是对同一保存曲线修改速度空间。在这组有限表示里，$M=15,16$
仍在 $\psi=0$ 有严格高于 $2\cdot10^{-9}$ 的入口误差，而 $M=18$
的全角采样 FFT 诊断已低于该数。

此处没有给正在准备的 M15 联解添加一个先验失败结论：它的最终 support
参数由新 BVP 联解确定，可以不同于这里固定的14项 core。也没有得到 M18
全曲面或全角严格通过；本实验只重新投影入口，没有求新的径向曲线、末端
尾匹配、共同目标转移或 reach。

## 4. 实际执行与可复算来源

程序 `scripts/78718-geometry-core-reprojection-v1.py`，9479 B，SHA256
`6f93dcb6d4634b5795343ff61c53e914901bb10b74e0569a6dd0a8c5f33090de`。

原执行 **c89922 自然 exit0**，约0.771秒；报告
`notes/2026-11-10-78718-geometry-core-reprojection-v1.json`，22713 B，SHA256
`3aec175c395509a5551f68fb108462eddd79a853799a578e740937e4c6f52346`。

原程序的 `sys.modules` 自动列表没有包含所有未注册 importlib 源。
这一范围已另稿澄清，不把原列表称完整闭包。随后用明确21件原源的
`scripts/78718-geometry-core-source-closure-v2.py` 新鲜执行原入口：
**6fbe09 自然 exit0**，约0.841秒，全部21件被实际 exec 观察到，前后
身份不变，完整报告的非时间字段与原执行相同。

新数学报告
`notes/2026-11-10-78718-geometry-core-reprojection-source-closed-v2.json`，22713 B，SHA256
`e444b5f414e1eda44fa2ac45f4528107a282fb291d996ce622f300d74a14b79f`。

明确来源回执
`notes/2026-11-10-78718-geometry-core-reprojection-source-closure-v2.json`，24268 B，SHA256
`c568bf24d8b47a26cb3c772f4ed26b9113b7a53b922e235cef9c8ea97531950f`。

完整来源与 raw PP 范围说明见
`notes/2026-11-10-78718-geometry-core-source-and-pp-clarification-v1.md`。
这里不依赖跨 PP 节点的精确光滑性；只用实际 core 参数及入口投影。
两次执行均为零 BVP、零 tail、零 flow 积分，未产生新的已求解曲面。

